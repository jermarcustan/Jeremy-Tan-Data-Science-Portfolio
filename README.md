# Jeremy Tan Data Science Portfolio
This repository contains all the data science and applied mathematics-related projects completed by Jeremy Tan as part of the 5-year BS Applied Mathematics to Master's in Data Science program at Ateneo de Manila University.

## Projects

### Master's Capstone Project: Predictive Modeling of Marikina River Water Levels along the Sto. Niño and Montalban Gauging Stations using Artificial Neural Networks

The goal of my master's capstone project was to create an accurate forecasting model for the water level at the Sto. Niño station along the Marikina River Basin. Three artificial neural networks were trained and evaluated using historical rainfall and water level data obtained from the MMDA and PAG-ASA. The Long Short-Term Memory (LSTM) model outperformed the basic time series model and the other artificial neural networks in terms of MSE and NSE in the univariate and multivariate cases. Moreover, different lag structures were implemented to asses how varying input configurations influence the predictive performance of the models. The results show that shorter lag values generally yield better performance. 

<a href="/Final Thesis and Capstone Project/Final Manuscript/Final Manuscript.pdf" download>
  <button style="padding: 10px 15px; font-size: 16px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">
    📄 Download Full Capstone PDF
  </button>
</a>

<figure>
  <img src="/img/Capstone_24hr_stonino.png" alt="A 24-hour snippet from the Sto. Niño predictions during a high-rainfall event" style="width:100%;">
  <figcaption><strong>Figure:</strong> A 24-hour snippet of Sto. Niño water level predictions during a high-rainfall event.</figcaption>
</figure>

### Predictive Modeling: Classification of Fake and Real News from Filipino Sources using Neural Networks

I compared the classification performance of three neural networks: dense neural network, long short-term memory neural network, and convolutional neural network. The dataset for the language model was comprised of 1,603 real news articles from major news websites and 1,603 fake news articles, sourced and tagged by the National Union of Journalists in the Philippines. The models were built using the <b>R</b> programming language using RStudio software. While all three neural networks (DNN, LSTM, CNN) showed great overall performance, the convolutional neural network was the best model in terms of accuracy, loss, and kappa in predicting and classifying the fake news Filipino language dataset.

<figure>
  <img src="/img/Predictive_Modeling_for_Text.png" alt="Results of the Neural Networks on the Test Set" style="width:100%;">
  <figcaption><strong>Figure:</strong> Results of the Neural Networks on the Test Set </figcaption>
</figure>

### Data Visualization: Tableau Dashboard that Highlights the Globalization of the NBA

I created an interactive dashboard using NBA historical data from 1996 to the 2023 regular season. Tableau desktop was used to add interactivity to the dashboard in the form of tooltips, sliders, zoom, and drag functionalities. Moreover, filters can be applied to the charts by clicking on the categories. The data reveals that the NBA is transitioning to a more global game, with more players coming from different countries in the world.

<figure>
  <img src="/img/datavis_page1.png" alt="Tableau Dashboard (Page 1)" style="width:100%;">
  <figcaption><strong>Figure:</strong> Tableau Dashboard (Page 1) </figcaption>
</figure>

<figure>
  <img src="/img/datavis_page2.png" alt="Tableau Dashboard (Page 2)" style="width:100%;">
  <figcaption><strong>Figure:</strong> Tableau Dashboard (Page 2) </figcaption>
</figure>

### Time Series Analysis and Forecasting using ARMA Models: A Case Study of the Philippine Stock Exchange

I created an autoregressive moving average model (ARMA) to forecast the future prices of the Philippine Stock Exchange Composite Index (PSEi). The PSEi is the benchmark index for the Philippine stock exchange and is a good representation of the aggregate stock market performance of the largest companies in the Philippines. Publicly available data for the monthly closing prices of the PSEi from 1987 to 2022 were used for the time series models. The training data was preprocessed using log transformation and differencing to ensure that the data was stationary and to remove seasonal patterns or trends. The autocorrelation function (ACF) and the partial autocorrelation function (PACF) of the data were analyzed, which led to three candidate models: AR(1), MA(1), and ARMA(1,1). Based on the Akaike Information Criterion (AIC), a commonly used metric for model fit, the AR(1) was found to be the best-fitting model.

<figure>
  <img src="/img/time_series_prediction.png" alt="Time Series Forecasting" style="width:100%;">
  <figcaption><strong>Figure:</strong> Time Series Forecasting of the PSEi using the AR(1) Model </figcaption>
</figure>
