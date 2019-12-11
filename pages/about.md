---
title: "About"
---

## Problem statement

Crime tends to be ubiquitous in all areas of the United States, including Boston and Cambridge. Pinpointing the exact causes of crime is impossible, as it is a highly nuanced and complex issue. However, factors such as gross income, economic disparity, and government infrastructure/support are often strong indicators. We wish to inspect factors that may be correlated and/or contributing to occurrences of Boston crimes and the types thereof (e.g., robbery, vandalism, etc). 

We choose to explore datasets freely available from the City of Boston institutional website, starting (as reccommended) from the Street Lights and Property Values dataset, and incorporating a wide variety of other sources that can help explain variability in frequency and type of crimes committed.

After collecting and unyfing the data, we plan to construct models that learn relationships between predictors and crime from a training set, assess their performance on unseen data, and extrapolate from their predictions to postulate possible causal factors linked to crime

## Data sources and limitations

We choose to analyze only datasets publicly available from the institutional City of Boston website. Although these span a wide variety of situations and variables, they cannot be fully exhaustive and a number of smaller factors are not captured by our models. Some of the main limitations are the following:

### Bias in crime reporting

- The crime dataset only reports incidents that were recorded by public officials, and does not report crimes that go untracked. A side effect of this is that areas with better law enforcement are likely to have a greater percentage of crimes tracked in the dataset and therefore show higher incidence of crimes. This makes it difficult, for example, to measure the effect of law enforcement on the relative frequency of crimes, as more police might mean less crimes happening but a higher percentage of those being reported. Some ways to address these concerns might employ the use of different crime-related sources, such as surveys of victimisation, analysis of CCTV camera footage, etc.

### Normalizing crime numbers

- The relationship between the number of crimes that happen and the size and population density of a certain region is very complex. At a first approximation, the larger the region, the more crimes tend to happen; but at the same time the more people live in a region, the more likely it is that a crime is committed. But this is not enough. Although some classes of crime (e.g. burglary) are linked with people living there, others such as theft are linked with commercial activity, or the amount of traffic in the area, and the most populated zones are not necessarily where the most activity happens. Given that we could not find a source for activity, but just data for houses and population density, we are unable to fully normalize the number of crimes with respect to these factors. Furthermore, we find that thinking about the frequency of crime detracts from the main (and more interesting in our opinion) objective of the project, or inspecting the distribution of different typologies of crime.

## Souces of bias and ethical considerations

