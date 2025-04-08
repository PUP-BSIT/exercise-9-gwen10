LIST = '1'
ADD = '2'
UPDATE = '3'
DELETE = '4'
SEARCH = '5'
EXIT = '6'

song_book = []


def print_separator():
    print("\n========================")


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
