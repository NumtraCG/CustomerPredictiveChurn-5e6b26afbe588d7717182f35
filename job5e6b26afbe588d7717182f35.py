import traceback
import sys
from operations import TopOperation
from operations import JoinOperation
from operations import AggregationOperation
from operations import FormulaOperation
from operations import FilterOperation
from connectors import DBFSConnector
from connectors import CosmosDBConnector
from datatransformations import TranformationsMainFlow
from automl import tpot_execution
from core import PipelineNotification
import json

try: 
	PipelineNotification.PipelineNotification().started_notification('5e6b26afbe588d7717182f36','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
	CustomerPredictiveChurn_DBFS = DBFSConnector.DBFSConnector.fetch([], {}, "5e6b26afbe588d7717182f36", spark, "{'url': '/Demo/PredictiveChurnTraining.csv', 'file_type': 'Delimeted', 'dbfs_token': 'dapi0ef076722999cf4cd8859e9aafdb7b76', 'dbfs_domain': 'westus.azuredatabricks.net', 'delimiter': ',', 'is_header': 'Use Header Line'}")

	PipelineNotification.PipelineNotification().completed_notification('5e6b26afbe588d7717182f36','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e6b26afbe588d7717182f36','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify','http://13.68.212.36:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5e6b26afbe588d7717182f37','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
	CustomerPredictiveChurn_AutoFE = TranformationsMainFlow.TramformationMain.run(["5e6b26afbe588d7717182f36"],{"5e6b26afbe588d7717182f36": CustomerPredictiveChurn_DBFS}, "5e6b26afbe588d7717182f37", spark,json.dumps( {"FE": [{"transformationsData": {"feature_label": "State"}, "feature": "State", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2364", "mean": "", "stddev": "", "min": "AK", "max": "WY", "missing": "0"}, "transformation": "String Indexer"}, {"feature": "Account_Length", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "2364", "mean": "101.71", "stddev": "39.8", "min": "1", "max": "243", "missing": "0"}}, {"feature": "Area_Code", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "2364", "mean": "436.36", "stddev": "41.95", "min": "408", "max": "510", "missing": "0"}}, {"transformationsData": {"feature_label": "Phone"}, "feature": "Phone", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2364", "mean": "", "stddev": "", "min": "327-3053", "max": "422-8344", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "Intl_Plan"}, "feature": "Intl_Plan", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2364", "mean": "", "stddev": "", "min": "no", "max": "yes", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "VMail_Plan"}, "feature": "VMail_Plan", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2364", "mean": "", "stddev": "", "min": "no", "max": "yes", "missing": "0"}, "transformation": "String Indexer"}, {"feature": "VMail_Message", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "2364", "mean": "8.01", "stddev": "13.65", "min": "0", "max": "51", "missing": "0"}}, {"feature": "Day_Mins", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "2364", "mean": "178.35", "stddev": "54.49", "min": "0.0", "max": "350.8", "missing": "0"}, "transformation": ""}, {"feature": "Day_Calls", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "2364", "mean": "100.23", "stddev": "20.28", "min": "0", "max": "165", "missing": "0"}}, {"feature": "Day_Charge", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "2364", "mean": "30.32", "stddev": "9.26", "min": "0.0", "max": "59.64", "missing": "0"}, "transformation": ""}, {"feature": "Eve_Mins", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "2364", "mean": "201.36", "stddev": "51.01", "min": "0.0", "max": "363.7", "missing": "0"}, "transformation": ""}, {"feature": "Eve_Calls", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "2364", "mean": "100.16", "stddev": "20.18", "min": "0", "max": "170", "missing": "0"}}, {"feature": "Eve_Charge", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "2364", "mean": "17.12", "stddev": "4.34", "min": "0.0", "max": "30.91", "missing": "0"}, "transformation": ""}, {"feature": "Night_Mins", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "2364", "mean": "201.45", "stddev": "51.37", "min": "23.2", "max": "395.0", "missing": "0"}, "transformation": ""}, {"feature": "Night_Calls", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "2364", "mean": "99.98", "stddev": "19.59", "min": "33", "max": "175", "missing": "0"}}, {"feature": "Night_Charge", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "2364", "mean": "9.07", "stddev": "2.31", "min": "1.04", "max": "17.77", "missing": "0"}, "transformation": ""}, {"feature": "Intl_Mins", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "2364", "mean": "10.26", "stddev": "2.78", "min": "0.0", "max": "20.0", "missing": "0"}, "transformation": ""}, {"feature": "total_Mins", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "2364", "mean": "591.42", "stddev": "90.57", "min": "284.3", "max": "885.0", "missing": "0"}, "transformation": ""}, {"feature": "Intl_Calls", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "2364", "mean": "4.46", "stddev": "2.43", "min": "0", "max": "19", "missing": "0"}}, {"feature": "Intl_Charge", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "2364", "mean": "2.77", "stddev": "0.75", "min": "0.0", "max": "5.4", "missing": "0"}, "transformation": ""}, {"feature": "Total_Charge", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "2364", "mean": "59.27", "stddev": "10.51", "min": "23.25", "max": "96.15", "missing": "0"}, "transformation": ""}, {"feature": "CustServ_Calls", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "2364", "mean": "1.55", "stddev": "1.32", "min": "0", "max": "9", "missing": "0"}}, {"transformationsData": {"feature_label": "cluster_labels"}, "feature": "cluster_labels", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2364", "mean": "", "stddev": "", "min": "day_callers", "max": "vmailers", "missing": "0"}, "transformation": "String Indexer"}, {"feature": "Churn", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "2364", "mean": "0.14", "stddev": "0.34", "min": "0", "max": "1", "missing": "0"}}, {"feature": "State_transform", "transformation": "", "type": "real", "selected": "True", "stats": {"count": "2364", "mean": "22.36", "stddev": "14.47", "min": "0.0", "max": "50.0", "missing": "0"}}, {"feature": "Phone_transform", "transformation": "", "type": "real", "selected": "True", "stats": {"count": "2364", "mean": "1181.5", "stddev": "682.57", "min": "0.0", "max": "2363.0", "missing": "0"}}, {"feature": "Intl_Plan_transform", "transformation": "", "type": "numeric", "selected": "True", "stats": {"count": "2364", "mean": "0.09", "stddev": "0.29", "min": "0", "max": "1", "missing": "0"}}, {"feature": "VMail_Plan_transform", "transformation": "", "type": "numeric", "selected": "True", "stats": {"count": "2364", "mean": "0.27", "stddev": "0.45", "min": "0", "max": "1", "missing": "0"}}, {"feature": "cluster_labels_transform", "transformation": "", "type": "real", "selected": "True", "stats": {"count": "2364", "mean": "2.37", "stddev": "1.7", "min": "0.0", "max": "5.0", "missing": "0"}}]}))

	PipelineNotification.PipelineNotification().completed_notification('5e6b26afbe588d7717182f37','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e6b26afbe588d7717182f37','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify','http://13.68.212.36:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5e6b26afbe588d7717182f38','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
	CustomerPredictiveChurn_AutoML = tpot_execution.Tpot_execution.run(["5e6b26afbe588d7717182f37"],{"5e6b26afbe588d7717182f37": CustomerPredictiveChurn_AutoFE}, "5e6b26afbe588d7717182f38", spark,json.dumps( {"model_type": "classification", "label": "Churn", "features": ["State", "Account_Length", "Area_Code", "Phone", "Intl_Plan", "VMail_Plan", "VMail_Message", "Day_Mins", "Day_Calls", "Day_Charge", "Eve_Mins", "Eve_Calls", "Eve_Charge", "Night_Mins", "Night_Calls", "Night_Charge", "Intl_Mins", "total_Mins", "Intl_Calls", "Intl_Charge", "Total_Charge", "CustServ_Calls", "cluster_labels"], "percentage": "40", "executionTime": "5", "sampling": "1", "sampling_value": "over", "run_id": "5d67594f493a40d38fe86bca52c0c9fd", "model_id": "5e707de00dad826cbf345cce", "ProjectName": "ML Sample Problems", "PipelineName": "CustomerPredictiveChurn", "pipelineId": "5e6b26afbe588d7717182f35", "userid": "5df78f4be2f2eff24740bbd7", "runid": "", "url_ResultView": "http://13.68.212.36:3200", "experiment_id": "480623611921769"}))

	PipelineNotification.PipelineNotification().completed_notification('5e6b26afbe588d7717182f38','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e6b26afbe588d7717182f38','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify','http://13.68.212.36:3200/logs/getProductLogs')
	sys.exit(1)

