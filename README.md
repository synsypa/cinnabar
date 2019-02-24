This repo is a PIP package for an OpenAI environment for a reimplementation of FrozenLake in which staying still incurs a penalty

## Installation

Install the [OpenAI gym](https://gym.openai.com/docs/).

Then install this package via

```
pip install -e .
```

## Usage

```
import gym
import gym_fire

env = gym.make('FireLake-v0')
```

