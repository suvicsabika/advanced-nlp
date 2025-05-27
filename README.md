# NLP Article Processing Pipeline

This project downloads articles from URLs, processes their textual content, and applies various Natural Language Processing (NLP) techniques such as summarization, title generation, named entity recognition (NER), zero-shot classification, and word cloud creation.

## Key Features

* **Web Scraping:** Downloads article content based on URLs.
* **Text Cleaning and Preprocessing:** Removes HTML tags, scripts, styles, and common boilerplate text.
* **Tokenization and Lemmatization:** Using spaCy.
* **Abstractive Summarization:** With a Hugging Face Transformers model (sshleifer/distilbart-cnn-12-6).
* **Title Generation:** With a Hugging Face Transformers model (t5-large).
* **Named Entity Recognition (NER):** With a Hugging Face Transformers model (dslim/bert-base-NER) and post-processing.
* **Zero-shot Text Classification:** With a Hugging Face Transformers model (MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli).
* **Word Cloud Creation:** With customizable options (mask, colors, font, etc.).
* **Results Saving:** All processed outputs (cleaned text, tokenized, lemmatized text, summary, title, named entities, word cloud image) are saved to a designated directory.

## Installation and Setup

### Prerequisites
* Python 3.x
* GPU usage is highly recommended for running the transformer models efficiently.

### Installing Dependencies
To install the necessary Python packages, run the following commands (or create and use a `requirements.txt` file based on these):
```bash
pip install requests beautifulsoup4 lxml spacy
pip install transformers torch torchvision torchaudio
pip install tensorflow # Although the main models are PyTorch-based, this is also installed
pip install wordcloud matplotlib Pillow numpy
pip install hf_xet # Installed, though its direct use in the main script is not explicit
