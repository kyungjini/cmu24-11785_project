# Understanding Disease Features in CXR Images Using XAI for Enhanced Diagnosis Model
- This is our git-hub repository for class project (CMU F24 11-785)

## Dependencies
- PyTorch 2.4.1
- scikit-learn 1.5.1
- OpenCV 4.10.0
- torchsummary 1.4.5

## Instructions
- Unfortunately, MIMIC-CXR data needs credentializing so we couldn't put the sample images for demo.
- In the code, you can find `<file_location>` that points folder that contains MIMIC-CXR images. After you get credentialized for the dataset, you can download the images and execute it by setting it manually.
### Learning
- Just follow the code to train the model
- There will be two `model.pth` files for later analysis.

### Analysis
- After loading the model, execute the gradCAM part for selected samples.
- There are example gradCAM results for each anonymous sample images at the end of the ipynb file.