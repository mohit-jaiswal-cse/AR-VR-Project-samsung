## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Operating System**: Linux or Windos
- **Programming Language**: Python 3
- **Libraries**: PyTorch
- **Hardware**:
  - CPU (for basic functionality)
  - NVIDIA GPU with CUDA and CuDNN (for enhanced performance and training)
## Dataset Preparation

### Laval Indoor HDR Dataset

[Laval Indoor HDR Dataset](http://hdrdb.com/indoor/#intro)

Thanks to the intellectual property of the Laval Indoor dataset, the original datasets and processed training data cannot be released from me. Please get access to the dataset by contacting the dataset creator at jflalonde@gel.ulaval.ca.

We crop the images and create the pkl format images.

### Pickled Images:

- **Pickling**: This refers to the process of converting an object (like an image) into a byte stream format that can be stored and loaded later. Libraries like `pickle` in Python are commonly used for this purpose.
- **Benefits**: Pickling allows for efficient storage and retrieval of complex data structures like images.

### Combining Pickling and Cropping:

1. **Load Images**: Your code would likely start by loading the original dataset images using libraries like OpenCV or PIL.
2. **Cropping**: Implement logic to define the region of interest (ROI) for each image. This might involve techniques like bounding box selection or defining specific coordinates. Crop the image based on the chosen ROI.
3. **Pickling**: Convert the cropped image (now a NumPy array) into a byte stream using the `pickle` library. This creates a pickled file representing the cropped image data.

## Running the Code

Before running `train.py`, you need to run the following files in the `regression_network` folder:

1. `data.py`
2. `util.py`
3. `densnet.py`
4. `training.py`

### File Descriptions

- **data.py**: This script is responsible for handling the dataset. It includes functions for loading the dataset, preprocessing the images (including cropping and pickling), and creating data loaders for training and testing.

- **util.py**: This script contains utility functions that are used across different parts of the project. These functions might include image transformations, logging utilities, or any other helper functions needed for the training process.

- **densnet.py**: This script defines the architecture of the DenseNet model used for the regression task. It includes the implementation of the DenseNet layers and configurations specific to the model architecture.

- **training.py**: This script includes the training loop and logic for the regression network. It handles the training process, validation, and saving of the model checkpoints.

### How to Run

1. Ensure you have all the prerequisites installed and the dataset prepared as described in the previous sections.
2. Navigate to the `regression_network` folder in your terminal.
3. Run the following files in order:

```bash
python data.py
python util.py
python densnet.py
python training.py


