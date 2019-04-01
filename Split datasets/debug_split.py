import argparse
import random
import os

from PIL import Image
from tqdm import tqdm

SIZE = 64

parser = argparse.ArgumentParser()
parser.add_argument('--data_dir', default='/home/nivii/Desktop/Data/wicv/Images', help="Directory with the dataset")
parser.add_argument('--output_dir', default='/home/nivii/Desktop/Data/wicv/Image_Data', help="Where to write the new data")

Masks_orig = r'/home/nivii/Desktop/Data/wicv/Masks'
Annotations_orig = r'/home/nivii/Desktop/Data/wicv/Annotations'

out_masks_train = r'/home/nivii/Desktop/Data/wicv/Image_Data/train/Masks'
out_annotation_train = r'/home/nivii/Desktop/Data/wicv/Image_Data/train/Annotations'

out_masks_test = '/home/nivii/Desktop/Data/wicv/Image_Data/test/Masks'
out_annotation_test = '/home/nivii/Desktop/Data/wicv/Image_Data/test/Annotations'

def resize_and_save(filename, output_dir, size=SIZE):
    """Resize the image contained in `filename` and save it to the `output_dir`"""
    image = Image.open(filename)
    # Use bilinear interpolation instead of the default "nearest neighbor" method
    image = image.resize((size, size), Image.BILINEAR)
    image.save(os.path.join(output_dir, filename.split('/')[-1]))


if __name__ == '__main__':
    args = parser.parse_args()

    assert os.path.isdir(args.data_dir), "Couldn't find the dataset at {}".format(args.data_dir)

    # Define the data directories
    train_data_dir = args.data_dir#os.path.join(args.data_dir, 'train')
    #test_data_dir = os.path.join(args.data_dir, 'test_signs')

    # Get the filenames in each directory (train and test)
    filenames = os.listdir(train_data_dir)
    filenames = [os.path.join(train_data_dir, f) for f in filenames if f.endswith('.jpg')]

    #test_filenames = os.listdir(test_data_dir)
    #test_filenames = [os.path.join(test_data_dir, f) for f in test_filenames if f.endswith('.jpg')]

    # Split the images in 'train_signs' into 80% train and 20% val
    # Make sure to always shuffle with a fixed seed so that the split is reproducible
    random.seed(230)
    filenames.sort()
    random.shuffle(filenames)

    split = int(0.8 * len(filenames))
    train_filenames = filenames[:split]
    val_filenames = filenames[split:]

    filenames = {'train': train_filenames,
                 #'val': val_filenames,
                 'test': val_filenames}

    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)
    else:
        print("Warning: output dir {} already exists".format(args.output_dir))

    # Preprocess train, val and test
    for split in ['train', 'test']: #, 'val'
        output_dir_split = os.path.join(args.output_dir, '{}'.format(split))
        if not os.path.exists(output_dir_split):
            os.mkdir(output_dir_split)
        else:
            print("Warning: dir {} already exists".format(output_dir_split))

        print("Processing {} data, saving preprocessed data to {}".format(split, output_dir_split))
        for filename in tqdm(filenames[split]):
            file_name = filename.split('/')[-1].split('.')[0]

            image = Image.open(filename)
            image.save(os.path.join(output_dir_split, filename.split('/')[-1]))
            #resize_and_save(filename, output_dir_split, size=SIZE)

            if ('train' in output_dir_split):
                mask = Image.open(os.path.join(Masks_orig, file_name + r'_masks.jpg'))
                mask.save(os.path.join(out_masks_train , file_name + r'_masks.jpg'))
            else:
                mask = Image.open(os.path.join(Masks_orig, file_name + r'_masks.jpg'))
                mask.save(os.path.join(out_masks_train , file_name + r'_masks.jpg'))


print("Done building dataset")
