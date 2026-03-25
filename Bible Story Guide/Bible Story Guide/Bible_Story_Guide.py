import json  
  
def load_stories(filename):  
    with open(filename, 'r', encoding='utf-8') as f:  
        return json.load(f)  
  
def get_mood(moods):  
    print("Moods:")  
    for mood in moods:  
        print(f" - {mood}")  
    mood = input("How are you feeling? ").strip().lower()  
    return mood   
  
def show_recommendations(mood, stories):  
    if mood in stories:  
        print(f"\nStories for '{mood}':")  
        for s in stories[mood]["stories"]:  
            print(f"- {s}")  
        print(f"Book recommendation: {stories[mood]['book']}")  
    else:  
        print("No stories found for that mood.")  
  
def main():  
    filename = "bible_stories.json"  
    stories = load_stories(filename)  
    moods = list(stories.keys())  
    mood = get_mood(moods)  
    show_recommendations(mood, stories)  
  
if __name__ == "__main__":  
    main()  