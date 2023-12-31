import fiftyone as fo
import fiftyone.zoo as foz
from fiftyone import ViewField

name = "coco_person"
dataset_dir = "/home/zli/data/person_dataset"

# rm -rf ~/.fiftyone/

# Create the dataset
dataset = fo.Dataset.from_dir(
    dataset_dir=dataset_dir,
    dataset_type=fo.types.YOLOv4Dataset,
    name=name,
)
# session = fo.launch_app(dataset)
# input('Press Enter to continue...')

dataset.export(export_dir='/home/zli/data/coco_person', dataset_type=fo.types.COCODetectionDataset)