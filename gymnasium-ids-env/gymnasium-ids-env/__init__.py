from gymnasium.envs.registration import register

register(
    id="gymnasium-ids-env/GridWorld-v0",
    entry_point="gymnasium-ids-env.envs:GridWorldEnv",
)
