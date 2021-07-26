import logging
from os import getcwd, mkdir, path
from uuid import UUID
from json import load, dump
from random import choice
from datetime import datetime

from playsound import playsound

from twitchAPI.pubsub import PubSub
from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope, InvalidTokenException


logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s: %(message)s', 
    level=logging.INFO,
    handlers=[
        logging.StreamHandler()
    ]
)

cwd = getcwd()

# Creates audio file if it doesn't already exist
try:
    mkdir(cwd+"\\audio")
except FileExistsError:
    pass

# Loads config from config.json. Creates config.json if doesn't exist
try:
    config = (load(open("config.json",)))
except FileNotFoundError:
    logging.warning("config.json not found. Creating config\nPlease populate the config before starting the program again!")
    dump({
        "logins": list(),
        "rewards": dict(),
        "app_auth": ("App_ID","App_Secret"),
        "user_auth": tuple(),
        "logging": False
    }, open("config.json","w"), sort_keys=True, indent=4)
    config = (load(open("config.json",)))
    input("Press ENTER to close...")
    exit()

# Sets up file logging if enabled in config
if config["logging"] is True:
    try: 
        mkdir(cwd+"\\logs")
    except FileExistsError:
        pass
    handler = logging.FileHandler(f"logs\\{(datetime.now()).strftime('%d.%m.%Y-%H.%M.%S')}.log")
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    handler.setLevel(logging.INFO)
    logging.getLogger().addHandler(handler)
    del(handler)

# Checks app_auth has been filled out by user
if config["app_auth"][0] == "App_ID" or config["app_auth"][0] == "App_Secret":
    logging.error("app_auth hasn't been filled out! This can be done from the config.json file.\nIf you haven't created an application go to https://dev.twitch.tv/console")
    exit()

# Checks logins has been filled out by user
if not config["logins"]:
    logging.error("logins hasn't been filled out! This can be done from the config.json file.")
    exit()

# Checks all reward audio files are valid
for reward in config["rewards"]:
    for audio in config["rewards"][reward]:
        if not path.exists(cwd+"\\audio\\"+audio):
            logging.error(f"Audio file {audio} not found!\nMake sure it's in the audio file.")
            exit()

def callback_channel_points(uuid: UUID, data: dict):
    for reward in config["rewards"]:
        if data["data"]["redemption"]["reward"]["title"] == reward:
            logging.info(f"{data['data']['redemption']['reward']['title']} redeemed")
            audio = choice(config["rewards"][reward])
            playsound(cwd+"\\audio\\"+audio, block=False)
            logging.info(f"{audio} played")

def user_authenticate():
    auth = UserAuthenticator(twitch, [AuthScope.CHANNEL_READ_REDEMPTIONS], force_verify=False)
    token, refresh_token = auth.authenticate()
    config["user_auth"] = (token, refresh_token)
    dump(config, open("config.json","w"), sort_keys=True, indent=4)

# Setting up Authentication and getting user id
twitch = Twitch(config["app_auth"][0], config["app_auth"][1])
if not config["user_auth"]:
    user_authenticate()
try:
    twitch.set_user_authentication(config["user_auth"][0], [AuthScope.CHANNEL_READ_REDEMPTIONS], config["user_auth"][1])
except InvalidTokenException:
    user_authenticate()
    twitch.set_user_authentication(config["user_auth"][0], [AuthScope.CHANNEL_READ_REDEMPTIONS], config["user_auth"][1])

user_id = twitch.get_users(logins=config["logins"])["data"][0]["id"]
pubsub = PubSub(twitch)


# starting up PubSub
pubsub.start()
uuid = pubsub.listen_channel_points(user_id,  callback_channel_points)
# Likely a better way to block the program than this
logging.info("Listening to Twitch PubSub")
input("press ENTER to close...\n")
pubsub.stop()
