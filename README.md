## Startup Commands

<!-- docker run --gpus all --shm-size 1g -p 8080:80 -v $PWD/data:/data ghcr.io/huggingface/text-generation-inference:0.8 --model-id bigscience/bloom-560m --num-shard 1 --disable-custom-kernels -->

docker run --gpus all --shm-size 1g -p 8080:80 -v ~/Desktop/harinBot/data:/data ghcr.io/huggingface/text-generation-inference:0.8 --model-id bigscience/bloom-560m --num-shard 1 --disable-custom-kernels# harinBot
