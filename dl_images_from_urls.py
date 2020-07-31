from fastai.vision import download_images
import os
import csv
from dl_urls_csv import dl_urls_csv

# Download urls for a given nb of mountains
#dl_urls_csv(n_mtns=15)

def dl_images_from_urls():

    path = 'data/mountains/'
    folders = os.listdir(path)[1:]

    for mtn in folders:
        
        folder = mtn + "/"
        file = os.listdir(path + folder)

        # Check for hidden .DS_Store file
        if len(file) > 1:
            file = file[1]
        else:
            file = file[0]

        temp_csv_file = file[:-4] + '_tmp' + file[-4:]

        with open(path+folder+file, 'r') as inp, open(path+folder+temp_csv_file, 'w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if row:
                    writer.writerow(row)

        os.remove(path+folder+file)
        os.rename(path+folder+temp_csv_file, path+folder+file)

        with open(path+folder+file, 'r') as fp:
            reader = csv.reader(fp)
            print('nb of urls for {}: '.format(mtn), len(list(reader)))

        download_images(path+folder+file, path+folder, max_pics=300)

        print('nb of downloaded images for {}: '.format(mtn), len(os.listdir(path+folder))-1)
