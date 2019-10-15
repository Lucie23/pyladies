music_volume = float(input("How much is the music loud?"))
if music_volume < 30:
    print ("I can't hear anything.")
elif 30 <= music_volume < 60:
    print ("It is too quiet.")
elif 60 <= music_volume < 90:
    print ("I hear something.")
elif 90 <= music_volume < 120:
    print ("I hear very well right now.")
elif 120 <= music_volume < 150:
    print ("It is too loud.")
else:
    print ("My ears bleeding.")
