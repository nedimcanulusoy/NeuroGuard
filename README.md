# NeuroGuard: Safeguarding Prompted Platforms

NeuroGuard is a dedicated project designed to detect prompt injections within prompting platforms, thus providing robust protection against prompt attacks.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Comparative Analysis](#comparative-analysis)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Model Architectures and Approaches](#model-architectures-and-approaches)
  - [DNN (Deep Neural Network) Model](#dnn-deep-neural-network-model)
  - [CNN (Convolutional Neural Network) Model](#cnn-convolutional-neural-network-model)
  - [RNN (Recurrent Neural Network) Model](#rnn-recurrent-neural-network-model)
  - [DistilBert Model](#distilbert-model)
- [Result](#result)
- [License](#license)

## Project Overview

NeuroGuard enhances prompting platform security by identifying and mitigating prompt injection vulnerabilities. It is committed to making prompt attacks a thing of the past.

## Comparative Analysis

Neuroguard has rigorously tested four approaches to benchmark their performance against neural network techniques, ensuring the effectiveness of our solution in preventing prompt attacks. Of course, there is the potential for other approaches to be used and tested here.

## Live Demo

TBA

## Installation

1. Ensure you have Docker installed on your system.
2. Clone the repository:
   ```bash
   git clone [https://github.com/nedimcanulusoy/NeuroGuard.git]
   cd neuroguard
   ```

3. Build the Docker image:
   ```bash
   docker-compose build
   ```

4. Run the Docker container:
   ```bash
   docker-compose up
   ```

## Usage

Once the Docker container is up, you can access the NeuroGuard interface and API through the specified ports in `docker-compose.yml`.

- To interact with the API, navigate to `http://localhost:8000/`
- For the interface, navigate to `http://localhost:8501/`

Further documentation on API endpoints and interface operations can be found in `neuroguard_api.py` and `neuroguard_interface.py` respectively.

## Project Structure

- `ng_api/`: Contains the NeuroGuard API logic.
- `ng_interface/`: Handles the interface components and interactivity.
- `ng_models/`: Hosts the project's neural models, including DNN, CNN, RNN and distilled BERT.
- `Dockerfile`: Configuration for creating the Docker image.
- `docker-compose.yml`: Specifies the services, networks, and volumes for the Docker application.
- `entrypoint.sh`: Shell script for initializing services when the Docker container starts.
- `requirements.txt`: Lists the Python dependencies required for the project.

## Dataset
This project used the [Prompt Injections](https://huggingface.co/datasets/JasperLS/prompt-injections) dataset published by [JasperLS](https://huggingface.co/JasperLS) on Huggingface.

## Model Architectures and Approaches

<details>
  <summary>DNN (Deep Neural Network)</summary>

  In the DNN approach, data is represented using a bag-of-words technique. The architecture is deep and is characterized by multiple fully connected layers with ReLU activations in the hidden layers. A dropout layer was integrated to mitigate overfitting. During training, an early stopping mechanism was employed to prevent the model from memorizing the training data and to ensure it generalizes well to new, unseen data.

</details>

<details>
  <summary>CNN (Convolutional Neural Network)</summary>

  For the CNN model, the data is tokenized and encoded into text sequences. The core of the architecture is an embedding layer that converts the vocabulary into dense vector representations. This is followed by multiple convolutional layers with varying kernel sizes, which are adept at capturing local patterns in the data. After convolution operations, both max and average pooling techniques are applied. The model then passes the data through fully connected layers to finalize the classification. Layer normalization and dropout are also used in this approach for regularization purposes. The strength of this approach lies in its ability to utilize both convolutional and dense layers, capturing spatial and sequential patterns in the text data.

</details>

<details>
  <summary>RNN (Recurrent Neural Network)</summary>

  In the RNN approach, data is tokenized and subsequently encoded into text sequences. The architecture begins with an embedding layer, producing dense vector representations of the data. The heart of this model is its GRU (Gated Recurrent Unit) layers, which are designed to capture sequential patterns and long-term dependencies in the data. After processing through the GRU layers, dynamic max-pooling is applied to pool features from the sequences. This is followed by fully connected layers that handle the classification task. Layer normalization and dropout have been incorporated for regularization, ensuring the model does not overfit. The RNN model, with its GRU layers, excels in handling sequences, capturing the temporal dependencies present in the data.

</details>

<details>
  <summary>DistilBert</summary>

  For the DistilBert approach, data is tokenized and encoded using the specialized DistilBert tokenizer. The architecture employed is the `DistilBertForSequenceClassification` model, a distilled and more efficient version of the renowned BERT model, tailored for sequence classification tasks. The power of this approach comes from leveraging the pre-trained knowledge embedded within DistilBert, fine-tuning it specifically for the classification task at hand.

</details>

## Result


**DNN (Deep Neural Network) Model**: 
The DNN model showed commendable performance with a stellar training accuracy of 99.39%. Its ability to generalize was demonstrated by a validation accuracy of 89.09%. Subsequent fine-tuning sessions maintained this validation accuracy, underscoring the model's consistency.

**CNN (Convolutional Neural Network) Model**: 
The CNN model, known for its ability to capture spatial patterns, did not disappoint. It achieved perfection on the training set with 100% accuracy. On the validation set, it showed an impressive accuracy of 92.73%. Further fine-tuning brought the validation accuracy down slightly to 90.91%, but it still remained in the high performance range.

**RNN (Recurrent Neural Network) Model**: 
The RNN model tailored for sequence data demonstrated a robust training accuracy of 98.17% and validated its capabilities with an accuracy of 94.55%. However, subsequent fine-tuning indicated over-optimization, resulting in a reduced validation accuracy of 56.36%. This highlights the importance of vigilance during extended training periods.

**DistilBert Model**: 
The DistilBert model, a streamlined version of the heavyweight BERT, really shined in this evaluation. It performed flawlessly in both the training and validation phases, achieving a perfect 100% accuracy. Furthermore, when evaluated on the test set, the model maintained its robustness with an accuracy of 95.69%.

In summary, ranking of the model performances based on the results is;

1. DistilBert model is the clear frontrunner, achieving the highest accuracy on both validation and test sets.
2. RNN model follows next with a strong validation accuracy.
3. CNN model is in close competition with the RNN, especially before fine-tuning.
4. DNN model trails the others but still presents a respectable performance.

**_NOTE: Keep that in mind, modifying the architectures of DNN, CNN and RNN approaches can lead to variations in performance of these models._**

## License

This project is licensed under the terms provided in the `LICENSE` file.
