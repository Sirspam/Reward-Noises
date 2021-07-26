# Reward-Noises

Simple Twitch listener which plays audio on specified reward redemptions

## Set-up

 1. Download latest release
 2. Download decencies from requirements.txt via pip
 3. Run Reward-Noises.exe (Program will run then close)
 4. Open config.json
 5. Populate config.json accordingly, check [Config.json Definitions](#Config.json-Example) for info on the config
 6. Create corresponding rewards on [Twitch.tv dashboard](https://dashboard.twitch.tv/). **Ensure that reward name matches name defined in config.json**
6. Populate audio directory with your audio files (must be .mp3 or .wav) **Ensure that file names match names defined in config.json**

## Config.json Definitions
#### app_auth
This is a list which should contain your twitch application's ID and secret. If you haven't already made a twitch application it can be done on the [Twitch Developers](https://dev.twitch.tv/console/apps/create) site
#### logging
Set to true if you want the program to generate logs in external files
#### logins
This is a list which should contain the Twitch usernames of the accounts you want this lister to listen on
#### rewards
This is a dictionary which should contain your rewards and they're desired audio files.
Each key in the dict should be the exact name of the reward you want them to link to. The value for each key should be a list containing the names and the file extension of the files which you would like to be played when the reward is redeemed.
If you provide multiple files within the value list the file played will be randomly chosen.

    {"reward_name": ["audio_file_name.mp3"]}

#### user_auth
This is a list which will contain your user authentication. This is automatically filled out by the program. 
### Config Example
        {
            "app_auth": [
                "App_ID",
                "App_Secret"
            ],
            "logging": false,
            "logins": ["sirspam_"],
            "rewards": {
                "Baka (Sound)": ["Aqua_Baka.mp3"],
                "Nya (Sound)": [
                    "Chocola_Nya.mp3",
                    "Vanilla_Nya.wav"
                ]
            },
            "user_auth": []
        }
###### *I initially wrote this in TypeScript but couldn't get audio working and I'm still upset about it >:(*