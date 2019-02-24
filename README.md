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

## The Point
This reimplemenation attempts to incentivize the agent to take actions toward to goal rather than strictly optimize toward not falling into holes

## The Penalties

#### `FireLake-v0`
Staying still incurs a penalty of 0.01 (reward = -0.01)

Falling into a hole incurs a penalty of 1 (reward = -1)

Game ends when agent falls into a hole or reaches goal

#### `HellLake-v0`
Staying still incurs a penalty of 0.01 (reward = -0.01)

Game *does not* end when agent falls into a hole. Agent simple continues to incur "staying still" penalty


## To Do

Examine better rate of penalty to end goal reward

Penalty/Reward based on distance to Goal

Add small chance of salvation to `HellLake-v0`