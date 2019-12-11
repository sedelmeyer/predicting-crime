---
title: "About"
---

## Problem statement

Crime tends to be ubiquitous in all areas of the United States, including Boston and Cambridge. Pinpointing the exact causes of crime is impossible, as it is a highly nuanced and complex issue. However, factors such as gross income, economic disparity, and government infrastructure/support are often strong indicators. We wish to inspect factors that may be correlated and/or contributing to occurrences of Boston crimes and the types thereof (e.g., robbery, vandalism, etc.). 

We choose to explore datasets freely available from the City of Boston institutional website, starting (as recommended) from the Street Lights and Property Values dataset, and incorporating a wide variety of other sources that can help explain variability in frequency and type of crimes committed.

After collecting and unifying the data, we plan to construct models that learn relationships between predictors and crime from a training set, assess their performance on unseen data, and extrapolate from their predictions to postulate possible causal factors linked to crime.

## High-level design choices

Some design aspects of the projects were intentionally left to each group's taste and preference. We discussed these extensively in group meetings, and these are some of the motivations behind our choices.

### Grouping summary statistics by Census Tract

- For many of our datasets statistics were only provided at the Census Tract level. As there are more than 100 of those in the City of Boston alone, we deemed this to be sensitive enough without falling into the trap of overfitting. This principle is applied differently for each dataset, but as an example we prefer to aggregate property value statistics by Tract and feed that as an input into the model, rather than feeding for each instance of crime the value of the closest property to where the crime happened.

### Focusing on type rather than frequency of crime

- We saw too many ways we could box crime data into points to be predicted by a model. First, we could divide the city of Boston in small geographical region, and group all the crime instances happening in a region together, obtaining for each region one data point with crime measures associated to it. Or, we could treat each data point as an individual instance, and assign summary geographical statistics as a feature to it.

- We went with the second approach, for several reasons. First, we were afraid that even grouping reduces noise and outliers, we would be left with too few observations for complex models to be built on top of them. This would work better, for instance, if comparing different regions of multiple cities. Second, by leaving each crime instance as a single data point, we can observe which factors influence crime happening within the very same region or even in the exact same spot. This can shed further light to why crime happens and how it can be predicted/prevented.

Of course, many other design choices were made by individual members when analyzing, grouping, cleaning the data and when presenting the results of each model. These are fully explained in the relative pages.

## Data sources and limitations

We choose to analyze only datasets publicly available from the institutional City of Boston website. Although these span a wide variety of situations and variables, they cannot be fully exhaustive and a number of smaller factors are not captured by our models. Some of the main limitations are the following:

### Bias in crime reporting

- The crime dataset only reports incidents that were recorded by public officials, and does not report crimes that go untracked. A side effect of this is that areas with better law enforcement are likely to have a greater percentage of crimes tracked in the dataset and therefore show higher incidence of crimes. This makes it difficult, for example, to measure the effect of law enforcement on the relative frequency of crimes, as more police might mean less crimes happening but a higher percentage of those being reported. Some ways to address these concerns might employ the use of different crime-related sources, such as surveys of victimization, analysis of CCTV camera footage, etc.

### Normalizing crime numbers

- The relationship between the number of crimes that happen and the size and population density of a certain region is very complex. At a first approximation, the larger the region, the more crimes tend to happen; but at the same time the more people live in a region, the more likely it is that a crime is committed. But this is not enough. Although some classes of crime (e.g. burglary) are linked with people living there, others such as theft are linked with commercial activity, or the amount of traffic in the area, and the most populated zones are not necessarily where the most activity happens. Given that we could not find a source for activity, but just data for houses and population density, we are unable to fully normalize the number of crimes with respect to these factors. This is partially why we think that measuring frequency of crime detracts from the main (and more interesting in our opinion) objective of the project, or inspecting the distribution of different typologies of crime.

### Discrepancy between measurable quantities and underlying causes

- This point is kind of broad and has different implications for each of our data sources and predictors. As an example, we analyze the Property Value dataset as a proxy for underlying socioeconomic differences between regions of the city. But it's clear that this huge spectrum cannot be fully captured just by looking at a single factor, or even by the combination of all measurable factors available. Therefore we always try, for example if our models find a relationship between property values and a specific type of crime, to state that the relationship exists between those two things as per our model, and state possible extrapolations of the relationship to broader socioeconomic factors separately, as that is much more speculative and difficult to prove mathematically.

### Interpretability of our models

- Our aim of the project is to investigate the relationship of different types of crime and underlying features. Thus, recovering which variables had the greatest effect in the model's prediction for a certain data point is of paramount importance. For different kinds of models, as seen throughout the course, this can be done in different ways, but especially in models that are not easily interpretable (e.g. Neural Networks) we have to resort to approximations which might be distorting. We also try to state how statistically significant our findings are, and how dependent they might be on outliers or other features of the training set which do not necessarily generalize. 

## Sources of bias and ethical considerations

- As the Project Guidelines state, "this is purely an academic project whereby we want students to explore data and make statistical predictions in an area that is vastly affected by many confounding, real-world complex factors" and we therefore try to avoid any statements which might imply that this is more than an exploratory experiment in which we try to grapple with complex issues. In some sense, we often find that the data we have is not very good at explaining variance in crime, which suggests we take any of our results with a grain of salt and do not try to generalize unduly. 

- We are also aware this is a very sensitive issue, especially in the sense that certain groups of people can be unfairly associated with certain types of crime, and that we must remember the decision to commit a crime is ultimately each person's responsibility, even though a variety of outside factors can influence that choice. When we outline these correlations, we do not think that a certain demographic is more likely to commit "wrong" acts, but that underlying factors that might influence their choice should be addressed to better prevent crime from happening. Many other forms of bias (such as certain demographics being more likely to report crimes than others) should also be tackled before coming to definitive conclusions.

Any group seriously interested in tackling these broad issues should take much greater care of these factors than we have - we do believe data can be used against discrimination, but it is much easier to let discrimination propagate forward if one is not careful.
