##################################################################
# DEFINE FUNCTIONS FOR CALCULATING ROC AND AUC AND PLOTTING CURVES
##################################################################

# MULTI-CLASS AUC REQUIRES scikit-learn v0.22

# required imports
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc, roc_auc_score


def generate_roc_auc(y_values_actual, predicted_probabilities, class_dict):
    """
    Creates a dictionary of ROC curve values generated using
    sklearn.metrics.roc_curve for every outcome class in a multi-class
    problem
    
    NOTE: multi-class AUC requires scikit-learn>=v0.22

    y_values_actual: np.array, the 1-dimensional array containing the 
                     multi-classs true y values against which you are evaluating
                     the predicted probabilities (i.e. y_test)
    predicted_probabilities: np.array, the 2-dimensional array generated
                             using sklearn's "model.predict_proba()" method
                             (i.e. test set predicted probabilities)
                     
    returns: tuple(float, float, dict), (1) a float representing the average macro AUC
             for all classes, (2) a float representing the average weighted AUC (weighted
             by the number of true samples for each class to account for class imbalance)
             and (3) a dictionary of dictionaries, where each top level key represents a
             different y class, and the value for each y class key is a dictionary
             containing the corresponding frp, tpr, threshold, and individual class AUC
             values for that particular y class outcome. Example output format shown below:
             
             (
                 auc_average,
                 auc_weighted_average,
                 output_dict = {
                    0: {
                        'frp': np.array of shape (n,)
                        'tpr': np.array of shape (n,)
                        'threshold': np.array of shape (n,)
                        'auc': float of micro auc for individual class
                        'name': str name of class
                    }
                    1: {
                        'frp': ...
                        ...
                    }
                    ...
                 }
            )
    """
    # create sorted list of all class labels
    class_labels = sorted(list(set(y_values_actual)))

    # convert y_values to binary indicators for each class and store as 2D
    # array of dimensions (n_classes, n_y_values), with each row containing one
    # set of class indicators
    y_class_array = np.vstack(
        [
            (y_values_actual==class_val).astype(int) for class_val in class_labels
        ]
    )

    # create roc curve dictionary
    roc_curve_dict = {
        crime_class: {
            key: value
            for key, value in zip(
                ['fpr', 'tpr', 'thresholds'],
                roc_curve(y_class, predicted_probs_class)
            )
        } for (crime_class, predicted_probs_class), y_class in zip(
            enumerate(predicted_probabilities.T),
            y_class_array
        )
    }
    
    # add individual class auc's and class names to dictionary
    for crime_class in class_labels:
        roc_curve_dict[crime_class]['auc'] = roc_auc_score(
            y_class_array[crime_class],
            predicted_probabilities[:,crime_class]
        )
        roc_curve_dict[crime_class]['name'] = class_dict[crime_class]
    
    # generate overall average auc's for all classes, weighted and unweighted
    auc_avg = roc_auc_score(
        y_values_actual, predicted_probabilities, multi_class='ovr', average='macro'
    )
    auc_weighted_avg = roc_auc_score(
        y_values_actual, predicted_probabilities, multi_class='ovr', average='weighted'
    )
    
    return auc_avg, auc_weighted_avg, roc_curve_dict


def plot_roc_all_classes(overall_auc, overall_auc_weighted, roc_curve_dict,
                         title='ROC plotted for all crime type TEST classes',
                         savepath=None):
    """
    Generates a plot of ROC curves for all responses classes

    overall_auc: float, an overall average auc generated using the
                 'generate_roc_auc' function
    overall_auc_weighted: float, an overall weighted auc generated using the
                          'generate_roc_auc' function
    roc_curve_dict: dict, an roc_curve dict generated using the 'generate_roc_auc'
                    function
    title: str, specifies the title used for the plot
    savepath: None or str, if none, .png file is NOT saved, otherwise, input the
              "filepath.png" string, indicating where you would like the image saved

    returns: A plotted image and saved .png file (if savepath is not None)
    """
    fig, ax = plt.subplots(figsize=(12, 7))

    plt.title(
        ''.join(
            [title, '\n(overall AUC, avg.: {:.3f}; weighted avg.: {:.3})'.format(
                overall_auc,
                overall_auc_weighted
            )
            ]
        ),
        fontsize=20,
    )

    rate_values=np.arange(0,100)/100

    ax.plot(rate_values, rate_values, ':', color='k', linewidth=2, alpha=1)

    for key in roc_curve_dict.keys():
        plt.plot(
            roc_curve_dict[key]['fpr'],
            roc_curve_dict[key]['tpr'],
            label='{} : {:.3f}'.format(
                key,
                roc_curve_dict[key]['auc']
            )
        )
        plt.legend(
            fontsize=14,
            title='class : AUC',
            title_fontsize=14,
            edgecolor='k',
            framealpha=1,
            loc=4
        )

    ax.tick_params(labelsize=16)
    ax.set_ylabel("TRUE positive rate", fontsize=18)
    ax.set_xlabel("FALSE positive rate", fontsize=18)
    ax.grid(':', alpha=0.4)
    plt.tight_layout()
    if savepath:
        plt.savefig(savepath)
    plt.show();


def plot_roc_all_classes_individual(overall_auc, overall_auc_weighted, roc_curve_dict,
                                    title='ROC plotted by crime type TEST class',
                                    savepath=None, subplots=(5,2), fig_height=15,
                                    suptitle_spacing=0.91):
    """
    Generates a set of subplot of ROC curves for all responses classes, each plotted
    individually
    
    overall_auc: float, an overall average auc generated using the
                 'generate_roc_auc' function
    overall_auc_weighted: float, an overall weighted auc generated using the
                          'generate_roc_auc' function
    roc_curve_dict: dict, an roc_curve dict generated using the 'generate_roc_auc' 
                    function
    title: str, specifies the title used for the plot
    savepath: None or str, if none, .png file is NOT saved, otherwise, input the 
              "filepath.png" string, indicating where you would like the image saved
    subplots: tuple, default=(5,2) to plot each of the 9 crime classes,
              provides the dimension of subplots for the figure (NOTE: currently this
              function is only configured to plot 2 columns of subplots, therefore
              no other value other than two is accepted for the subplots width dimension)
    fig_height: int or float, default=15, this value is passed directly to the 'figsize'
                parameter of plt.subplots() and determines the overall height of your plot
    suptitle_spacing: float between 0 and 1, default=0.91,
                      this value is passed to the 'rect' parameter for plt.tight_layout()
                      to specify the proportion of the overall plot space to reserve for
                      the plt.suptitle() text. If you change the fig_height parameter from
                      the default, you may find that you need to adjust suptitle_spacing
                      to adjust the position of your suptitle. The larger your fig_height
                      value, the larger suptitle_spacing you will need and vice versa.
    
    returns: A plotted image and saved .png file (if savepath is not None)
    """
    if type(subplots)!=tuple:
        raise TypeError("'subplots' parameter must be entered as a tuple, e.g. subplots=(3,2)")
    if subplots[1]!=2:
        raise ValueError(
            "'subplots' parameter columns dimension must be value=2, e.g. subplots=(5,2). "\
            "This function is not configured to handle more or less than 2 subplots."
        )
    
    fig, axes = plt.subplots(*subplots, figsize=(12, fig_height))

    plt.suptitle(
        ''.join(
            [title, '\n(overall AUC, avg.: {:.3f}; weighted avg.: {:.3})'.format(
                overall_auc,
                overall_auc_weighted
            )
            ]
        ),
        fontsize=20,
    )

    rate_values=np.arange(0,100)/100
    
    for (i, ax), (j, key) in zip(enumerate(axes.flat), enumerate(roc_curve_dict.keys())):
        ax.set_title('class {}: {}'.format(key, roc_curve_dict[key]['name']), fontsize=16)
        ax.plot(rate_values, rate_values, ':', color='k', linewidth=2, alpha=.3)

        ax.plot(
            roc_curve_dict[key]['fpr'],
            roc_curve_dict[key]['tpr'],
            label='{} ({:.4f})'.format(
                key,
                roc_curve_dict[key]['auc']
            ),
            color='k'
        )
        ax.text(0.7, 0.1, 'AUC = {:.3f}'.format(roc_curve_dict[key]['auc']), fontsize=14)
        ax.tick_params(labelsize=14)
        ax.set_ylabel("TRUE positive rate", fontsize=14)
        ax.set_xlabel("FALSE positive rate", fontsize=14)
        ax.grid(':', alpha=0.4)
    
    # hide all markings for axes if there is no corresponding subplot
    if i < np.product(subplots)-1:
        for pos in ['right','top','bottom','left']:
            axes[subplots[0]-1, 1].spines[pos].set_visible(False)
        axes[subplots[0]-1, 1].tick_params(
            axis='x', which='both', bottom=False, top=False, labelbottom=False
        )
        axes[subplots[0]-1, 1].tick_params(
            axis='y', which='both', right=False, left=False, labelleft=False
        )
    
    plt.tight_layout(rect=[0, 0.03, 1, suptitle_spacing])
    if savepath:
        plt.savefig(savepath)
    plt.show();

