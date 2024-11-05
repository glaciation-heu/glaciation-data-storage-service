import json
import unittest
import influxdb_client

from unittest.mock import patch, Mock
from influxdb_client.domain.write_precision import WritePrecision
from datetime import datetime, timezone, time, timedelta
from influxdb_client.client.write_api import SYNCHRONOUS

from openapi_server.models.data_access_record import DataAccessRecord
from openapi_server.data_storage_service import utils
from openapi_server.models.metric import Metric


class TestDSS(unittest.TestCase):

    def test_write_read_data_access_record(self,):
        """ Test writing data access record and check by reading records """
        # Mock record
        data_access_record = Mock(spec=DataAccessRecord)
        data_access_record.data_id = 'D01'
        data_access_record.request_id = 'R01'
        data_access_record.time = '2024-10-01T00:00:00.000000Z'
        test_json_format = {
            'time': data_access_record.time,
            'dataId': data_access_record.data_id,
            'requestId': data_access_record.request_id
        }

        # Write mock record
        utils.writeDataAccessRecord(data_access_record)

        # Retrieve inserted mock record
        utils.readDataAccessRecord(data_access_record.data_id)
        self.assertTrue(any(json.loads(d) == test_json_format for d in utils.readDataAccessRecord(data_access_record.data_id)))

    def test_write_read_prediction(self,):
        """ Test wrting predictions and check by reading them back """
        # Mock record
        metric = Mock(spec=Metric)
        metric.metric_id = 'M00'
        metric.aggregation_interval = 86400
        metric.forecasting_period = 1
        metric.forecasting_model = 'ARIMA'
        metric.timeseries = [0.0]
        metric.forecasting_values = [6.0]
        metric.forecasting_upper_bounds = [6.0]
        metric.forecasting_lower_bounds = [6.0]
        metric.time = [datetime.strptime('2024-10-20T00:00:00Z', '%Y-%m-%dT%H:%M:%SZ')]

        # Write mock record
        utils.writePredictionResults(metric)
        
        # Read mock record back
        res = utils.readPredictionResults(metric.metric_id, metric.time[0].strftime("%Y-%m-%dT%H:%M:%SZ"))
        self.assertListEqual(metric.timeseries, json.loads(res)['timeseries'], 'timeseries are not equal')
        self.assertListEqual(metric.forecasting_values, json.loads(res)['forecasting_values'], 'forecasting values are not equal')
