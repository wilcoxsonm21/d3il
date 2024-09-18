from gym.envs.registration import register

register(
    id="pushing-v0",
    entry_point="gym_pushing.envs.pushing:Block_Push_Env",
    max_episode_steps=500,
)
