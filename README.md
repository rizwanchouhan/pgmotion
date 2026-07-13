# Gravity-Aware World-Coordinate Human Motion Estimation via Perceptual-Gravity Reference Frames

<img style="max-width:100%;" src="resources/framework.png" alt="Framework Overview">

# 📌 Overview

This repository contains the official implementation of **Gravity-Aware World-Coordinate Human Motion Estimation via Perceptual-Gravity Reference Frames**.

Our method introduces a **Perceptual-Gravity (PG) reference frame**, a canonical coordinate system constructed from two observable cues in monocular videos: the gravity direction and the camera optical axis. Instead of directly estimating motion in camera or world coordinates, the proposed framework first predicts human motion in the PG frame and then recovers world-coordinate trajectories using inter-frame camera motion. This formulation significantly reduces rotational ambiguity and improves both pose and trajectory estimation.

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

# 📊 Evaluation Metrics

We report standard camera-space and world-coordinate evaluation metrics.

### Camera-space Metrics

- PA-MPJPE ↓
- MPJPE ↓
- PVE ↓

### World-coordinate Metrics

- Translation Error ↓
- Orientation Error ↓
- Trajectory Error ↓
- MPJPE ↓

---

# 🚀 Training

```bash
python train.py \
    --config configs/train.yaml
```

---

# 🧪 Evaluation

```bash
python test.py \
    --checkpoint checkpoints/model.pth
```

---

# 📈 Results

Our method consistently outperforms existing trajectory-aware approaches by improving both local pose estimation and global trajectory reconstruction across multiple benchmark datasets.

---

# 📖 Citation

If you find this work useful, please cite:

```bibtex
@article{yourpaper2026,
  title={Gravity-Aware World-Coordinate Human Motion Estimation via Perceptual-Gravity Reference Frames},
  author={...},
  journal={...},
  year={2026}
}
```

---

# 📧 Contact

For questions or collaborations, please contact:

**Rizwan Abbas**

Email: your_email@sjtu.edu.cn
