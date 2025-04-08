LIST = '1'
ADD = '2'
UPDATE = '3'
DELETE = '4'
SEARCH = '5'
EXIT = '6'

song_book = []

def print_separator():
    print("\n========================")

def song_number_input():
    song_number = input("Enter song number: ").strip()
    if not song_number.isdigit():
        print("Invalid input. Song number must be numeric.")
        print_separator()
        return None
    return song_number

def list_all():
    if not song_book:
        print("\nNo songs in the song book.")
        return
    print("\n====  List of Songs ====")
    for song in song_book:
        print(f"\nSong Number   : {song['song_number']}")
        print(f"Title         : {song['title']}")
        print(f"Artist        : {song['artist']}")
        print(f"Genre         : {song['genre']}")
        print(f"Year Released : {song['year']}")
        print_separator()

def add_song():
    print("\n======= Add Song =======")
    song_number = song_number_input()
    if song_number is None:
        return 
    
    song = {
        "song_number": song_number,
        "title": input("Enter song title: "),
        "artist": input("Enter artist name: "),
        "genre": input("Enter genre: "),
        "year": input("Enter year released: ")
    }
    
    song_book.append(song)
    print_separator()
    print("Song added successfully!")

def update_song():
    print("\n===== Update Song =====")
    song_number = input("\nEnter the song number to update: ").strip()
    if not song_number.isdigit():
        print("Invalid input. Song number must be numeric.")
        return

    for song in song_book:
        if song["song_number"] == song_number:
            print("\nYou can now enter the new details.")
            song["title"] = input(f"Title ({song['title']}): ")
            song["artist"] = input(f"Artist ({song['artist']}): ")
            song["genre"] = input(f"Genre ({song['genre']}): ")
            song["year"] = input(f"Year Released ({song['year']}): ")

            print_separator()
            print("\nSong updated successfully.")
            return

    print("\nSong not found.")
    print_separator()

def display_menu():
    print("\n==== SONG BOOK MENU ====")
    print(" 1. List all songs")
    print(" 2. Add a song")
    print(" 3. Update a song")
    print(" 4. Delete a song")
    print(" 5. Search for a song")
    print(" 6. Exit")
    return input("\nEnter your choice: ").strip()

choice = display_menu()
print_separator()

while True:
    if choice == LIST:
        list_all()
    elif choice == ADD:
        add_song()
    elif choice == UPDATE:
        update_song()
    elif choice == DELETE:
        delete_song()
    elif choice == SEARCH:
        search_song()
    elif choice == EXIT:
        print("\nExiting the program...")
        break
    else:
        print("\nInvalid choice. Please try again.")

    choice = display_menu()
