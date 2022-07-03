# DTIwithNeuralNetworkDemo

Diffusion MRI (dMRI) can probe tissue microstructure properties by acquiring certain amount of dMRI measurements and solving the inverse problem of a diffusion model. Conventional model fitting-based methods usually require large amount of dMRI measurements with long acquisition time, which can be highly accelerated by deep learning-based methods through neural networks.

Taking the diffusion tensor imaging (DTI) model as an example, this demo builds neural networks to effectively solve the inverse problem of estimating fractional anisotropy (FA) and mean diffusivity (MD) measures from under-sampled diffusion dataset. The objectives of this project are to obtain 1) basic understanding of deep learning approaches applied in dMRI, 2) practical knowledge of essential components in building neural networks for diffusion model fitting.

## I. Guidance of environment setting and packages installation

### 1. Install Anaconda/Miniconda where you can use Conda commands to easily configure different environments

    Follow the installation here: <https://conda.io/projects/conda/en/latest/user-guide/install/index.html> targ

### 2. Setting up the environment for Python version of 3.7 

    # Create a new environment with python version of 3.7
    conda create --name your_env_name python=3.7   

    # Activate the environment when you need to use it
    conda activate your_env_name 
    
    # Deactivate the enviroment when you have finished using it   
    conda deactivate
 
### 3. Install necessary python packages
    
    conda activate your_env_name

    # Install tensorflow (which now includes keras) these two librarys are used for deep learning in python
    pip install tensorflow==2.3.1

    # Install scipy and numpy these libraries are used for performing mathmatical calculations on datasets 
    pip install scipy
    pip install numpy==1.17.0

    # Install nipy, this library is used for loading NIfTI images (.nii/.nii.gz). This is how MRI images are normally saved
    pip install nipy==0.4.2
    
### 4. Download MRIcron for convenient visualisation of Nifty image files

    <https://www.nitrc.org/frs/?group_id=152>

## II. Download the sample datasets and codes

### 1. Download the repository

    You can download the repository to your local system via the following command:
    git clone <https://github.com/Tinggong/DTIwithNeuralNetworkDemo>

### 2. Description about the datasets

    The dataset can be downloaded here: <https://drive.google.com/file/d/1aDoU8CJ695Xsm1C9uGnKvq0XOtgmgfwn/view?usp=sharing>  

    The DTI dataset contains data from two subjects (S1; S2) extracted from a publicly available multi-centre dataset. 
    Please refer to the paper for full dataset and imaging parameters: <https://www.nature.com/articles/s41597-020-0493-8>

    Folder structure:
    # subject folder S1 
    bval                 # the b-values associated with each image volume; 6 b0 images + 30 b=1000 s/mm2 images
    bvec                 # the directions of diffusion gradients
    diffusion.nii        # the diffusion dataset
    nodif_brain_mask.nii # the binary brain mask
    S1_FA.nii            # the FA and MD measures estimated from DTI model ...
    S1_MD.nii            # using dtifit in FSL <https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FDT/UserGuide#DTIFIT>

## III. Running the demos

### Step 1: Choose the under-sampled image volumes from full diffusion dataset (the nifty files), and format and save training and testing data to .mat file; /datasets folder will be generated containing the formatted data.

    # a. Formatting training dataset with the first 10 image volumes from the full diffusion dataset
        python FormatData.py --path /Your/Data/Dir/Data-DTI --subjects S1 --nDWI 10 --fc1d_train 
  
        # You can also format training dataset with a scheme file contained in the ${NetDir}/schemes folder, 
        # which are 1 for the target image volumes to choose and 0 for all other volumes. (see example file scheme1)
        # Use when you want to design new under-sampling schemes
        python FormatData.py --path /Your/Data/Dir/Data-DTI --subjects S1 --scheme scheme1 --fc1d_train 


    # b. Formatting test dataset (add --Nolabel option if the dataset contains no available labels
        python FormatData.py --path $DataDir --subjects S2 --nDWI 10 --test

### Step 2: network training; Check all available options and default values in /utils/model.py; /weights folder will be generated containing the trained model.

    # Using the first 10 volumes; you can also use a scheme file to determined the input DWI volumes. 
        python Training.py --train_subjects S1 --DWI 10 --model fc1d --train 

### Step 3: Test the model with dataset from S2; weights are saved from previous training; /nii folder will be generated containing the estimated parameters from testing data in nifty format, and you can view the results with MRIcron.

        python Testing.py --test_subject S2 --DWI 10 --model fc1d
