#mental health
ps = {
  'overwhelm' : "write down your thoughts, spend time in nature",
  'anxious' : "meditate, skincare",
  'tired' : "power nap",
  'sad' : "exercise, listen to music",
  'stressed' : "walk",
  'angry' : "music",
  'lazy' : "reduce screen time, dress up",
  'burnt out' : "read",
  'confused' : "organize room",
  'failure' : "help others",
  'lonely' : "date yourself",
  'empty' : "social media break",
  'off track' : "create schedule",
  'worried' : "drop your jaw",
  'lost' : "healthy habits",
  'sleep deprivation' : " read",
  'unmotivated' : "change environment",
  'bored' : "go for a drive",
  'nervous' : "fix your posture"
}
feel = input("How are you feeling today?")
if feel == 'idk' or feel == 'IDK' or feel == "I don't know":
  print("If you have difficulty understanding, Type in one from the list- ")
  print(*ps.keys(), sep='\n')
  feel = input("\nSo any particular problem from the list you are facing?")
print(ps.get(feel))