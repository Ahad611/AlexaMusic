# Copyright (C) 2021-2022 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
Alexa is a Telegram Audio and video streaming bot
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want.
"""

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("28209312", ""))
API_HASH = getenv("89def84a7894bb696ff20174c86889a4")

BOT_TOKEN = getenv("7866554017:AAHZ_0S-R_-veYpyQLYmvhWIxSIBAaj53tE")

MONGO_DB_URI = getenv("mongodb+srv://ahaan:ahaad@ahaan.hgkeruq.mongodb.net/?retryWrites=true&w=majority&appName=ahaan", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

LOG_GROUP_ID = int(getenv("-1002740659166", ""))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")

OWNER_ID = int(getenv("7710841624", None))

HEROKU_API_KEY = getenv("HRKU-AAMspfSnkbSK2uiNdnrxXkx6HVAHc9Qvy8i8n1SbSckA_w8o1lPmwkcU")

BOT_ID = getenv("BOT_ID")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TheTeamAlexa/AlexaMusic")

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Addiction_World")

SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+Ay_8Q6xrMbtkOTll")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")

AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "11500"))

AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "False")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/TheTeamAlexa/AlexaMusic")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)

SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "2"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "7"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))

TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

COOKIES = getenv("# Netscape HTTP Cookie File
# http://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file!  Do not edit.

.youtube.com	TRUE	/	TRUE	1777228644	PREF	f6=40000000&tz=Asia.Calcutta&f7=100
.youtube.com	TRUE	/	TRUE	1742668991	CONSISTENCY	AKreu9v_JYJFWrAok1YoNiQbm8Vp07BxoYR2M_NWe--JUXo_E_7sZq-73QawT1TZLF5_xwjdqMwBu-n_KXIiX_xDpLlKhLNlS3Ph16JFQNWwkdDEFUT0bu9zUQ
.youtube.com	TRUE	/	TRUE	1742670214	GPS	1
.youtube.com	TRUE	/	TRUE	1774204616	__Secure-1PSIDTS	sidts-CjEB7pHptQ69THEBs6-ha9hVOsVUxBPqJn-y37b8wcY9zJGlJxxBLK08h8v8dKNZByrFEAA
.youtube.com	TRUE	/	TRUE	1774204616	__Secure-3PSIDTS	sidts-CjEB7pHptQ69THEBs6-ha9hVOsVUxBPqJn-y37b8wcY9zJGlJxxBLK08h8v8dKNZByrFEAA
.youtube.com	TRUE	/	FALSE	1777228616	HSID	AWE8Dp5GjP_3bnwoS
.youtube.com	TRUE	/	TRUE	1777228616	SSID	AFJsyajsKnaeLoPCE
.youtube.com	TRUE	/	FALSE	1777228616	APISID	j1MkFF3KiGyTqXXH/ASpp-rFs1WbzU9kZ_
.youtube.com	TRUE	/	TRUE	1777228616	SAPISID	rbmIMM1Hd0-1y0rM/ABXlw8kyPh2VGTXpj
.youtube.com	TRUE	/	TRUE	1777228616	__Secure-1PAPISID	rbmIMM1Hd0-1y0rM/ABXlw8kyPh2VGTXpj
.youtube.com	TRUE	/	TRUE	1777228616	__Secure-3PAPISID	rbmIMM1Hd0-1y0rM/ABXlw8kyPh2VGTXpj
.youtube.com	TRUE	/	FALSE	1777228616	SID	g.a000vAhd5xS6oS2KYi0RanrN4tG3WSA_QlPSTM5hd1CjhY3-eOX91AO3u1yiti4rPj3GOpco8gACgYKAfYSARYSFQHGX2MiRZUOcBBytBl9mJos9yMQiRoVAUF8yKpP9yctuOZbFNQDrwnbDerr0076
.youtube.com	TRUE	/	TRUE	1777228616	__Secure-1PSID	g.a000vAhd5xS6oS2KYi0RanrN4tG3WSA_QlPSTM5hd1CjhY3-eOX9EMp5kNncTBDKH297Y93NFAACgYKAaISARYSFQHGX2MiX_R9RdezK9u36qtmpNNurBoVAUF8yKrASsoSXJyRcQQB4VUEzS4D0076
.youtube.com	TRUE	/	TRUE	1777228616	__Secure-3PSID	g.a000vAhd5xS6oS2KYi0RanrN4tG3WSA_QlPSTM5hd1CjhY3-eOX9sjdkYdgFuPsEayTHX_2ShAACgYKAQUSARYSFQHGX2MiDlm7cDDfjC-fX8nXsa2FgRoVAUF8yKrYyOgdDX0iN9MObG98c7qM0076
.youtube.com	TRUE	/	TRUE	1777228617	LOGIN_INFO	AFmmF2swRAIgDecC6JJNkO3KgzkoFHyPkzF3IJksvzOm_Ey0HaFXDGkCIHqOGyu5IsGpKxwDsQrbb5ApLhAmWrjrVjoAanBvbR_3:QUQ3MjNmeTFTOXo4dVRldDhtSndveE9NcWhSTVZja0RtTjN5V0NtZGJTVWNWdUoxazlQOE1IRFdkbEk2NUVBZEIwa2NWR25qdzRGRVFrejZ6NGEweGpCb0FtMG9WZkN1ZFp1dVU1ajBTOXcwQWtZUGRNcjA1VlU2ZFdlVnA3QXhDbXVXZlliSXFfRFpycEJMSzhLWUE4NnlFMWU5ZXljRkN3
.youtube.com	TRUE	/	FALSE	1774204803	SIDCC	AKEyXzXiAmPF5O239Xcfp5pOIbYJ7-TlrW36cikSWUDeAb0p3osYhw9Q4tgImLUOVyw__Bvc
.youtube.com	TRUE	/	TRUE	1774204803	__Secure-1PSIDCC	AKEyXzUIAai72nhUKxQd1aK8cUsuUEReIDxHFfQB_ttL8thVvf7Bws3VwsZi6vA1MZqJXnQB
.youtube.com	TRUE	/	TRUE	1774204803	__Secure-3PSIDCC	AKEyXzWzFZ1jNnUG8PymA29tylQJQWhdp6BYqjKDDAunT52c3jELnklrnvFh6OSAciOc7V1f", None)
# https://batbin.me

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("BQCOaU4AxARKjnw05xbtfoloNJ-aoETw3cDYx9Zb0-MSff9U9gRd2jzmYDN1mUvTxR7YW_Z6QCrzexzmncDt9kZ671bEtM7vju2MF907KNDJtRbM7A0coTWwk5x-r0YZVBTkvJqgvKnn3tPc6aKuwe3ntj_fTh4U3qeoymvdVLAySoqQbEO2YpWu0m44Ewr-TyifTw1DGTK8CetOvESqyA6-M4YyZqyuKFP7-NeztNa61PORTXYPq8mNd5Z_08Gpii_PuRqIfXIl0WB3NkrV4qrR3rO4no6xfPvBOt0KlvWI5goDMF7HV9-vhtazBnF_1jlr2XVIzGjVyAhTMo-PQEok56GAwQAAAAHbGwTmAA", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/ea393ad4ce0eed46d32c8-b287bce17388905e79.jpg"
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "assets/Ping.jpeg","https://graph.org/file/ea393ad4ce0eed46d32c8-b287bce17388905e79.jpg"
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "assets/Playlist.jpeg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "assets/Global.jpeg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "assets/Stats.jpeg","https://graph.org/file/ea393ad4ce0eed46d32c8-b287bce17388905e79.jpg"
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "assets/Audio.jpeg","https://graph.org/file/ea393ad4ce0eed46d32c8-b287bce17388905e79.jpg"
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "assets/Video.jpeg","https://graph.org/file/ea393ad4ce0eed46d32c8-b287bce17388905e79.jpg"
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "assets/Stream.jpeg","https://graph.org/file/ea393ad4ce0eed46d32c8-b287bce17388905e79.jpg"
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "assets/Soundcloud.jpeg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "assets/Youtube.jpeg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "assets/SpotifyArtist.jpeg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "assets/SpotifyAlbum.jpeg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "assets/SpotifyPlaylist.jpeg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    print(
        "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if SUPPORT_GROUP and not re.match("(?:http|https)://", SUPPORT_GROUP):
    print(
        "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if UPSTREAM_REPO and not re.match("(?:http|https)://", UPSTREAM_REPO):
    print(
        "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if GITHUB_REPO and not re.match("(?:http|https)://", GITHUB_REPO):
    print(
        "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
    )


if (
    PING_IMG_URL
    and PING_IMG_URL != "assets/Ping.jpeg"
    and not re.match("(?:http|https)://", PING_IMG_URL)
):
    print(
        "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if (
    PLAYLIST_IMG_URL
    and PLAYLIST_IMG_URL != "assets/Playlist.jpeg"
    and not re.match("(?:http|https)://", PLAYLIST_IMG_URL)
):
    print(
        "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if (
    GLOBAL_IMG_URL
    and GLOBAL_IMG_URL != "assets/Global.jpeg"
    and not re.match("(?:http|https)://", GLOBAL_IMG_URL)
):
    print(
        "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if STATS_IMG_URL and (
    STATS_IMG_URL != "assets/Stats.jpeg"
    and not re.match("(?:http|https)://", STATS_IMG_URL)
):
    print(
        "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if (
    TELEGRAM_AUDIO_URL
    and TELEGRAM_AUDIO_URL != "assets/Audio.jpeg"
    and not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL)
):
    print(
        "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if (
    STREAM_IMG_URL
    and STREAM_IMG_URL != "assets/Stream.jpeg"
    and not re.match("(?:http|https)://", STREAM_IMG_URL)
):
    print(
        "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if (
    SOUNCLOUD_IMG_URL
    and SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg"
    and not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL)
):
    print(
        "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if (
    YOUTUBE_IMG_URL
    and YOUTUBE_IMG_URL != "assets/Youtube.jpeg"
    and not re.match("(?:http|https)://", YOUTUBE_IMG_URL)
):
    print(
        "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if (
    TELEGRAM_VIDEO_URL
    and TELEGRAM_VIDEO_URL != "assets/Video.jpeg"
    and not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL)
):
    print(
        "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()
