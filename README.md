<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/harin329/harinBot">
  </a>
  <h3 align="center">HarinBot</h3>
  <p align="center">
  </p>
</p>


<!-- TABLE OF CONTENTS -->
  <h2 style="display: inline-block">Table of Contents</h2>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#deployment">Deployment</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>



<!-- ABOUT THE PROJECT -->
## About The Project

A chatbot trained on all my messages and will respond like me.


### Built With

* Embedchain - Modified by me into a chatbot version
* Open AI API - GPT
* Open AI Embedding API
* Hugging Face Embedding Models


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation
#### Basic Bot

1. `pip3 install -r requirements.txt`
2. Copy the .env.example file and rename it to .env with the correct environment variables
3. Ensure all your data is in the chatData folder and also added into the harinbot.py files according to the file type.
4. `python3 harinbot.py`

#### HuggingFace Inference Startup Commands

docker run --gpus all --shm-size 1g -p 8080:80 -v $PWD/data:/data ghcr.io/huggingface/text-generation-inference:0.8 --model-id bigscience/bloom-560m --num-shard 1 --disable-custom-kernels

<!-- DEPLOYMENT -->
## Deployment

Todo

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
2. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
3. Push to the Branch (`git push origin feature/AmazingFeature`)
4. Open a Pull Request
