from HateSpeechClassification.configuration.gcloud_syncer import GCloudSync

obj = GCloudSync()

obj.sync_folder_from_gcloud("hatespeechclassification",'dataset.zip','downloads/dataset.zip')