import fiftyone as fo
import os.path as osp

def main():
    """Convert a YOLOv4 dataset into COCO dataset format.
    The file structure is
    <dataset_dir>/
    ├── obj.names
    ├── data/
    │   ├── <uuid1>.jpg
    │   ├── <uuid1>.txt
    │   ├── <uuid2>.jpg
    │   ├── <uuid2>.txt
    where `obj.names` contains one line: 'person'
    """
    dataset_dir = osp.expanduser('~/data/person_detection_data')

    # The cached fiftyone files may cause error 100
    # rm -rf ~/.fiftyone/

    # Create the dataset
    dataset = fo.Dataset.from_dir(
        dataset_dir=dataset_dir,
        dataset_type=fo.types.YOLOv4Dataset,
        name='coco_person',
    )
    # session = fo.launch_app(dataset)
    # input('Press Enter to continue...')

    dataset.export(export_dir=osp.expanduser('~/data/milestone_coco_person'), dataset_type=fo.types.COCODetectionDataset)

if __name__ == '__main__':
    main()