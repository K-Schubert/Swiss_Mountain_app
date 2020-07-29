import os

for mtn in list_of_mountains[:1]:
    folder = mtn
    file = 'urls_' + folder + '.csv'
    
    path = Path('data/mountains')
    dest = path/folder
    dest.mkdir(parents=True, exist_ok=True)
    
    temp_csv_file = file[:-4] + '_2' + file[-4:]

    with open(path/folder/file, 'r') as inp, open(path/folder/temp_csv_file, 'w') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row:
                writer.writerow(row)

    os.remove(path/folder/file)
    os.rename(path/folder/temp_csv_file, path/folder/file)
    
    with open(path/folder/file, 'r') as fp:
        reader = csv.reader(fp)
        print('nb of urls: ', len(list(reader)))
        
    download_images(path/folder/file, dest, max_pics=1000)
    
    print('nb of downloaded images for {}: '.format(mtn), len(os.listdir(path/folder))-2)
    idx = len(os.listdir(path/folder))-2

