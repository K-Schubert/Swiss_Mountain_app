# Swiss_Mountain_app
Development of an app for the identification of swiss mountains. Wondering what peak you are facing while hiking in the swiss Alps? Take a picture with your cellphone and find out!

# To Do
### Data Collection

- [x] Collect image URLs with javascript.
- [x] Automatically download into folders.
- [x] Scrap Wikipedia table of swiss mountains with bs4.
- [x] Create bot to automate above steps with Selenium.
- [x] Expand number of available mountains.

### Data Cleaning and Augmentation

- [x] Check for image duplicates, irrelevant images, etc.
- [ ] Balance classes (oversampling).
- [x] Data Augmentation.

### Model/Training

- [ ] Download pretrained ResNet model, re-train to new data, re-train with dynamic image re-sizing.

### Deployment

- [ ] Use Starlette to deploy model.

# The Bot
The bot was created using Selenium to crawl google images for a given search. It is programmed to scroll down to the end of the current page to display the maximum amount of images. Then the javascript code fetches the image urls.

# Remarks
A big challenge of this project was the data cleaning (as always...), but using a pretrained ImageNet model allowed to reduce the number of images per class to less than a thousand (they could probably have been even less) for model fine-tuning. Scraping the data from Google images was a simple task but ensuring proper labeling was tricky as many mountains look alike and I am by no means a mountain expert. Not all images contained nice angles of mountains, and I had to manually remove selfies, photos with weird angles (from the peak, looking downwards, etc.). I tried to keep photos with good angles and lighting that (taken from the base of the mountain or from a neighbouring peak). Cleaning the data significantly improved model accuracy, although we are not achieving the 95%+ accuracy for some more famous "toy" datasets. This is certainly due to the fact that classifying mountains is a difficult task as the mountains mostly have the same textures (snow, rock or grass) and similar shapes.

In the next steps, it would be interesting to use a semantic segmentation model to pre-process the data and allow the network to focus solely on mountains and their contours/shapes.
