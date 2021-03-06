import pylast
import vk_api
import time
import sys
from settings import *
import Log


def last_fm_init():
    network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                                   username=USERNAME, password_hash=pylast.md5(PASSWORD))

    return pylast.User("", network)


def vk_init():
    vk_session = vk_api.VkApi(token=VK_USER_TOKEN)

    return vk_session.get_api()


def main(lastfm, vk):
    tag = 'MAIN'
    errors = 0
    last_track = ''

    try:
        tag = 'LAST.FM'
        while True:
            if lastfm:
                results = lastfm.get_now_playing()
                if not results:
                    if last_track:
                        last_track = ''
                        Log.info(tag, "Nothing plays. Set an empty status.")
                        vk.status.set(text=DEFAULT_STATUS)
                    time.sleep(INTERVAL)
                    continue
                if results != last_track:
                    track_name = str(results.get_artist()) + " – " + str(results.get_title())
                    status_text = MUSIC_STATUS.format(track=track_name, username=USERNAME)
                    Log.info(tag, "Last.fm user {un} listening {res}. Setting VK status:\n{status}"
                             .format(un=USERNAME, res=results, status=status_text))
                    vk.status.set(text=status_text)
                    last_track = results
                    time.sleep(INTERVAL)
                else:
                    time.sleep(INTERVAL)
            else:
                Log.warning(tag, "Can't get user. Please check the \"settings.py\" file.")
                sys.exit()

    except pylast.NetworkError:
        errors += 1
        err_time_wait = ERR_INTERVAL * errors
        Log.warning(tag, "Network Error. Waiting {wait}s.".format(wait=err_time_wait))
        time.sleep(err_time_wait)


if __name__ == "__main__":
    tag = 'RUN'
    Log.info(tag, "Program start")
    try:
        tag = 'INITIALISATION'
        LastFmUser = last_fm_init()
        VkToken = vk_init()
        Log.info(tag, 'Init successfully.')

        main(LastFmUser, VkToken)
    except Exception as e:
        Log.error(tag, e)
