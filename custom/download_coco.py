import fiftyone as fo
import fiftyone.zoo as foz
from fiftyone import ViewField

# Download and load the validation split of COCO-2017
dataset = foz.load_zoo_dataset('coco-2017', splits=['validation'], classes=['dog'])
# session = fo.launch_app(dataset)
# input('Press Enter to continue...')

view = dataset.filter_labels("ground_truth", ViewField("label").is_in(["dog"]))
view.export(export_dir='/home/zli/data/coco_dog', dataset_type=fo.types.COCODetectionDataset, classes=['dog'])
