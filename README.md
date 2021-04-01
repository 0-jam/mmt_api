# Regenerate Sentences API

The text generater API based on [0-jam/regen_my_sentences](https://github.com/0-jam/regen_my_sentences)

---

1. [Environment](#environment)
1. [Installation](#installation)
  1. [macOS](#macos)
1. [Configuration](#configuration)
  1. [Generate your Markovify model](#generate-your-markovify-model)
  1. [Specify the Markovify model](#specify-the-markovify-model)
1. [Usage](#usage)
  1. [Run locally](#run-locally)

---

## Environment

- macOS Big Sur 11.2.3 arm64
    - Homebrew is already set
- Python 3.9.2 on pyenv

## Installation

### macOS

```
% brew install mecab
% pipenv install --dev
```

## Configuration

### Generate your Markovify model

```
% pipenv run python
>>> from modules.mcmodel import MCModel
>>> mc_model=MCModel()
>>> mc_model.build_dataset('/path/to/your_text.txt')
>>> mc_model.build_model()
>>> mc_model.save_model('/path/to/your_markovify_model.json')
```

### Specify the Markovify model

Create `.env` and specify the model path:

```bash
# You can specify multiple model files by space between the model file
MC_MODEL_PATH="/path/to/your_markovify_model.json /path/to/second_model.json"
```

## Usage

### Run locally

Run `% uvicorn markovify_sentence:app --reload` then throw this simple query to `http://localhost:8000`:

```
{
  markovify
}
```

It will returns:

```json
{
  "data": {
    "markovify": "家人 が お 縁側 で 夕刊 を 読ん だら 、 何事 も 無かっ た 。"
  }
}
```
