import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Function to load and play music
def play_music(file_path):
    if os.path.exists(file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print(f"Playing {file_path}")
    else:
        print("File not found!")

# Function to pause music
def pause_music():
    pygame.mixer.music.pause()
    print("Music paused")

# Function to resume music
def resume_music():
    pygame.mixer.music.unpause()
    print("Music resumed")

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()
    print("Music stopped")

# Main function
def music_player():
    while True:
        print("\nOptions: play, pause, resume, stop, exit")
        choice = input("Enter your choice: ").strip().lower()

        if choice == "play":
            file_path = input("Enter the path to the music file: ").strip()
            play_music(file_path)
        elif choice == "pause":
            pause_music()
        elif choice == "resume":
            resume_music()
        elif choice == "stop":
            stop_music()
        elif choice == "exit":
            stop_music()
            print("Exiting the music player.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    music_player()

