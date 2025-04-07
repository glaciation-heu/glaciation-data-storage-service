# Description
The data storage service has evolved into a long-term data storage solution for storing
time series data, such as daily energy consumption statistics or query access patterns
in the DKG. Behind the scenes, this microservice uses InfluxDB as the time series
database to store incoming time series data and exposes a set of REST APIs based
on predefined OpenAPI specification.
* URL: http://data-storage.integration/ or *validation* instead of *integration* for the one deployed in internal validation cluster
* Relevant work package and deliverable: WP6, D6.3

For example, the time series data retrieved from the Metric Store and used for training
the prediction service, along with its predictions are stored together daily via the data
storage service. This in turn will store the daily aggregated energy consumption time
series data as well as daily predictions. This information can also be used for
monitoring daily energy consumption and the performance of the [prediction service](https://github.com/glaciation-heu/glaciation-prediction-service).

# Endpoints
![image](https://github.com/user-attachments/assets/4545b326-25bf-43a7-b93d-5793f5b25d4e)
* The first endpoint allows us to store data access patterns, which can be used
by the metadata service.
* The second endpoint allows us to retrieve data access patterns stored earlier in
the InfluxDB.
* The third endpoint aims to store time series data used for training a forecasting
model for daily inference and its prediction in the time series database.
* The fourth endpoint allows us to retrieve prediction history for a certain metric
based on the metricId and forecasting_time specified.
* The last endpoint allows us to retrieve historical time series data for a certain
metric based on the metricId provided, with an option to specify a time range for
the retrieval.
* Use **M04** for the metric id of daily energy consumption time series measured by Kepler on the platform.

