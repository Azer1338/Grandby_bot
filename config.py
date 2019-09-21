from environs import Env

env = Env()
env.read_env()


API_GOOGLE_KEY = env.str("GOOGLE_KEY")

