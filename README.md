# Perceptual-Gravity Reference Frames for Globally Consistent Human Motion Estimation

<img style="max-width: 100%;" src="https://github.com/rizwanchouhan/pgmotion/blob/main/resources/wax.png" alt="pgmotion Overview">

# 📌 Overview

This repository contains the official implementation of Gravity-Aware World-Coordinate Human Motion Estimation via Perceptual-Gravity Reference Frames. The proposed method introduces a Perceptual-Gravity (PG) reference frame, a canonical coordinate system constructed from two observable cues in monocular videos: the gravity direction and the camera optical axis. Instead of directly estimating motion in camera or world coordinates, the proposed framework first predicts human motion in the PG frame and then recovers world-coordinate trajectories using inter-frame camera motion. This formulation significantly reduces rotational ambiguity and improves both pose and trajectory estimation.

<img style="max-width: 100%;" src="https://github.com/rizwanchouhan/pgmotion/blob/main/resources/overview.jpg" alt="EMOPOI Overview">

---

# 🧠 Framework

The proposed framework consists of the following components:

- Perceptual-Gravity (PG) Reference Frame Construction
- Image Feature Extraction
- Motion Transformer Network
- PG-Frame Human Motion Estimation
- Camera Motion Estimation
- World-Coordinate Motion Recovery

The complete pipeline estimates temporally consistent 3D human motion and reconstructs accurate world-coordinate trajectories from monocular videos.

---

# ✨ Features

- Gravity-aware canonical motion representation
- World-coordinate human motion estimation
- Transformer-based temporal motion modeling
- Robust trajectory reconstruction
- Improved pose and mesh estimation
- Compatible with monocular RGB videos

---

# 💻 System Requirements

- Ubuntu 20.04 / 22.04 (recommended)
- Python 3.10
- CUDA 12.1 or newer
- PyTorch 2.3+
- NVIDIA GPU (RTX 3090 24 GB used in our experiments)

---

# Clone the Repository

```bash
git clone https://github.com/your_username/PGMotion.git
cd PGMotion
```

---

# Create Conda Environment

```bash
conda create -n pgmotion python=3.10 -y
conda activate pgmotion
```

---

# Install PyTorch

```bash
conda install pytorch torchvision pytorch-cuda=12.1 -c pytorch -c nvidia
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ⚙️ Main Dependencies

- Python 3.10
- PyTorch
- torchvision
- OpenCV
- NumPy
- SciPy
- Open3D
- PyTorch3D
- matplotlib
- tqdm

---

## Download SMPL and SMPL-X Models

Please register and download the body models from the official websites:

- **SMPL:** https://smpl.is.tue.mpg.de/
- **SMPL-X:** https://smpl-x.is.tue.mpg.de/

After downloading, place the files in the following directory structure:

```text
inputs/
└── body_models/
    ├── smpl/
    │   └── SMPL_{GENDER}.pkl
    └── smplx/
        └── SMPLX_{GENDER}.npz
```

where `{GENDER}` should be replaced with `MALE`, `FEMALE`, or `NEUTRAL`, depending on the model you downloaded.

---

# 📂 Datasets

Our framework is evaluated on three challenging benchmark datasets.

## 3DPW

3DPW is a large-scale in-the-wild benchmark containing accurate SMPL pose and mesh annotations captured using IMU-assisted motion tracking. It evaluates world-coordinate human motion estimation under realistic conditions.

---

## RICH

RICH is a human-scene interaction dataset containing synchronized multi-view videos and accurate 3D body annotations. It provides challenging indoor sequences with diverse human-object interactions for evaluating world-coordinate motion reconstruction.

---

## EMDB-1

EMDB-1 is a benchmark for monocular human motion estimation containing diverse indoor and outdoor activities with accurate trajectory annotations. It evaluates both body pose estimation and global trajectory reconstruction.

---
