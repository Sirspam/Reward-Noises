# Reward-Noises
*Reward-Noises is being [rewritten by Raine](https://github.com/dawnvt/Reward-Noises), it's recommended to use Raine's version, when it's available, as this repo is no longer being maintained.*

Simple Twitch listener which plays audio on specified reward redemptions

## Set-up

 1. Download latest release
 2. Run Reward-Noises.exe (Program will run then close)
 3. Open config.json
 4. Populate config.json accordingly, check [Config.json Definitions](#Configjson-Definitions) for info on the config
 5. Create corresponding rewards on [Twitch.tv dashboard](https://dashboard.twitch.tv/). **Ensure that reward name matches name defined in config.json**
 7. Populate audio directory with your audio files (must be .mp3 or .wav) **Ensure that file names match names defined in config.json**

## Config.json Definitions
#### app_auth
This is a list which should contain your twitch application's ID and secret. If you haven't already made a twitch application it can be done on the [Twitch Developers](https://dev.twitch.tv/console/apps/create) site
#### logging
Set to true if you want the program to generate logs in external files
#### logins
This is a list which should contain the Twitch usernames of the accounts you want this lister to listen on
#### rewards
This is a dictionary which should contain your rewards and they're desired audio files.
Each key in the dict should be the exact name of the reward you want them to link to. The value for each key should be the name of the audio file you want to be played, including the file's extension (.mp3 or .wav).
If a folder name is provided all of the mp3 and wav files in that folder will be used, when the reward is redeemed a random file within the folder will be played.

    {"reward_name": "audio_file_name_and_extension"}
or

    {"reward_name": "folder_containing_mp3_and_wav_files"}

#### user_auth
This is a list which will contain your user authentication. This is automatically filled out by the program. 
### Config Example
        {
            "app_auth": [
                "App_ID",
                "App_Secret"
            ],
            "logging": true,
            "logins": ["sirspam_"],
            "rewards": {
                "Baka (Sound)": "Aqua_Baka.mp3",
                "Nya (Sound)": "Nyas_Folder" 
            },
            "user_auth": []
        }
###### *I initially wrote this in TypeScript but couldn't get audio working and I'm still upset about it >:(*
