from playsound import playsound
import freesound
import random


def search(term):
    client = freesound.FreesoundClient()
    client.set_token(TOKEN, "token")

    results = client.text_search(query=term, fields="id,duration,name,previews")
    # filter really short and long stuff out
    short_results = list(filter(lambda result: result.duration < 20 and result.duration > 1, results))

    sound = random.choice(short_results)
    url = sound.previews.preview_lq_mp3
    print(f'Using: {sound.name}')
    print(url)

    return url


def play(url):
    playsound(url)


if __name__ == "__main__":
    import sys
    token = sys.argv[1]
    term = sys.argv[2]
    url = search(term)
    play(url)
