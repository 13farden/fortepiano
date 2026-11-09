from pygame import mixer

def Load_sounds(keys):
    sounds = {}
    for key, filename in keys.items():
        sounds[key] = mixer.Sound(f"assets/sounds/{filename}")
    return sounds