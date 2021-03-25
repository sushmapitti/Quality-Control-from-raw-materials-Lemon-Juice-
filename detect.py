from watson_developer_cloud import VisualRecognitionV3
import json
def inputs(img_path):
    visual_recognition = VisualRecognitionV3(
    version='2019-02-11',
    iam_apikey='CCmCjvQEYRuljLJexV0N3gUBFlW8EUOSXa1k1pynLfWz')
    with open(img_path, 'rb') as images_file:
        classes = visual_recognition.classify(
        images_file,
        threshold='0.15',
	    classifier_ids='DefaultCustomModel_685796107').get_result()
        return((((((((classes["images"])[0])['classifiers'])[0])['classes'])[0])['class']))
