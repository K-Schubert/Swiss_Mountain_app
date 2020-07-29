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

- [ ] Check for image duplicates, irrelevant images, etc.
- [ ] Balance classes (oversampling).
- [ ] Data Augmentation.

### Model/Training

- [ ] Download pretrained ResNet model, re-train to new data, re-train with dynamic image re-sizing.

### Deployment

- [ ] Use Starlette to deploy model.

# The Bot
The bot was created using Selenium to crawl google images for a given search. It is programmed to scroll down to the end of the current page to display the maximum amount of images. Then the javascript code fetches the image urls.
