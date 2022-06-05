import fiftyone as fo

# Create the dataset
dataset = fo.Dataset.from_dir(
    dataset_dir='/home/zli/data/coco_person/',
    dataset_type=fo.types.COCODetectionDataset,
    name='MyData',
)
session = fo.launch_app(dataset)
input('Press Enter to continue...')
