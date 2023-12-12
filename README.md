Real estate aggregator and analyzer.

This project is meant to dive into the topic of real estate offerings, by scraping, analyzing, and creating a regression model that can predict prices based on given features.

The project is divided into four files:
- main.py - providing a user interface to start scrapping program and access gathered data
- kamernet.py - actual program for web scraping
- visualization.ipynb - jupyter notebook providing simple EDA
- regression.ipynb - jupyter notebook for data preprocessing, splitting into train and test data, fitting model, predicting and assessing the outcome.

Although the current model is not very accurate (mean absolute error of 150) due to limited data and features, the project is still to be developed with the possible use of more data and neural networks.
