# 🚨 SafeSenseAI

**SafeSenseAI** is a dual-modality content filtering system that detects and classifies unsafe (NSFW) content in both **images** and **text**. It combines computer vision and natural language processing to create a reliable pipeline for moderating and sanitizing potentially harmful content.

---

## 📦 Features

- ✅ Download and organize large image datasets.
- 🧹 Validate and clean images using Python and `imghdr`.
- 🧠 Classify unsafe text content using multilingual transformer models.
- 🔄 Export trained models to ONNX for scalable deployment.
- 🔬 Preprocess and tokenize text with Hugging Face Transformers.
- 🔗 Ready to integrate into moderation or safety applications.

---

## 📁 Project Structure

SafeSenseAI/
├── imgs.zip # (Removed from Git, downloadable separately)
├── nlp_data.csv # CSV file for text classification
├── SafeSenseAI.ipynb # Jupyter notebook with full workflow
├── .gitignore # Ignores large and unnecessary files
└── README.md # Project documentation


---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/iskan-dar05/SafeSenseAI.git
cd SafeSenseAI

pip install transformers datasets scikit-learn torch onnx

🧠 Model Details
Text Classification:

Model: sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2

Output: Binary classification (Safe vs Unsafe)

Export: ONNX format for inference-ready deployment

Image Cleaning:

Filters corrupted or unsupported image files

Supported extensions: jpeg, jpg, png, bmp, webp

💡 How It Works
Image Processing:

Downloads ZIP file of images

Filters invalid files using imghdr

Prepares dataset for image classification (future step)

Text Processing:

Loads labeled text dataset (CSV)

Tokenizes using Hugging Face Transformers

Trains and optionally exports ONNX model

Model Export:

PyTorch → ONNX conversion using torch.onnx.export

📦 Dataset Note
Due to size restrictions, the imgs.zip file is not included in the Git repository.

📥 You can upload it separately to Google Drive or a server and link it here:

markdown
Copy
Edit
Download the image dataset: [Google Drive Link Here]

📄 License
This project is licensed under the MIT License.
Feel free to use, modify, and distribute responsibly.

🤝 Contributing
Pull requests and suggestions are welcome!
For major changes, please open an issue first to discuss the feature.

🙌 Acknowledgments
Hugging Face Transformers

Datasets Library

Google Colab

Community support and open-source contributors ❤️
