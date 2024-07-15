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
