# Swiss_Mountain_app
Development of an app for the identification of swiss mountains. Wondering what peak you are facing while hiking in the swiss Alps? Take a picture with your cellphone and find out!

### Data Collection

- [x] Collect image URLs with javascript.
- [x] Automatically download into folders with fastai.
- [x] Scrap Wikipedia table of mountains in CH with bs4.
- [x] Create script to automate above steps.

### Data Cleaning and Augmentation

- [ ] Check for image duplicates, irrelevant images, etc.
- [ ] Balance classes (oversampling).
- [ ] Data Augmentation.

### Model/Training

- [ ] Download ResNet34/ResNet50 pretrained ImageNet model.
- [ ] Train head for *x* epochs.
- [ ] Train all layers for *y* epochs.
- [ ] Re-train with dynamic image re-sizing.

### Deployment

- [ ] Use Starlette to deploy model.
