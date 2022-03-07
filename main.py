def on_forever():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
basic.forever(on_forever)
