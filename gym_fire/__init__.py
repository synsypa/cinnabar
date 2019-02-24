from gym.envs.registration import register

register(
    id='FireLake-v0',
    entry_point='gym_fire.envs:FireLakeEnv',
)
register(
    id='HellLake-v0',
    entry_point='gym_fire.envs:HellLakeEnv',
)