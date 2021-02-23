# Molecurlar-properties-prediction
Molecular internal energy prediction by Computer Vision using CNN
## Quick preview
- Autor: Weicheng HE
- Supervisor: Dario Rocca
- Date: Oct. 2020 - Feb. 2021
- Context: For the scientific project at Mines Nancy (one day per week), I conducted research for the Labotorary of Theoretical Physics and Chemistry of Unversity of Lorraine. 
- Topic: molecular properties prediction by Artificial Neural Networks
- Methods: properties prediction by molecular image recognition using computer vision algorithms including MLP(Multi-layer perceptron), CNN(Convolutional Neural Network), GCN(Graph Convolutional Network)
- Programming: Python
- Result: the model can get a test RMSE of around 1, a reduction of 97% compared to the previous research.

## How to use this repository
- `molecular_properties_prediction.ipynb`: a jupyter notebook on development and training of ResNet on the augmented dataset
- In `data` folder
   - `structure.csv`: molecular structure information extracted from QM9 dataset
   - `energy.dat`: molecular energy information extracted from QM9 dataset
   - `image.py`: script for creating molecular images by Gaussian Representation from molecular structure information
   - `create_dataset.py`:create tensors for training Deep Learning algorithms from images and energy information
- In `model` folder, `ResNet50.py`: ResNet(Residual Network) from scratch

## To note
- More information of QM9 can be found on http://quantum-machine.org/datasets/
- `molecular_properties_prediction.ipynb` covers only ResNet, implementation of other models can be found in my Kaggle Notebook https://www.kaggle.com/hugo1995/projet-recherche
