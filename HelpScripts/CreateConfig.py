import os
import shutil
import configparser

def main():
    # Get the desktop path
    desktop_path = os.path.join(os.path.expanduser("~"), "Downloads")
    folder_path = os.path.join(desktop_path, "SkinsFairBots")
    config_path = os.path.join(folder_path, "config.ini")

    #Check if folder already exists on the desktop
    if os.path.exists(folder_path):
        print("SkinsFairBots folder already exists on the downloads.")
        return
    else:
        # Get the file path from the user
        file_path = 'C:/Users/Rober/OneDrive/Bilder/Desktop/Python Test/SkinsFair/chromedriver.exe'

        # Check if the file exists
        if not os.path.isfile(file_path):
            print("Invalid file path!")
            return

        # Create the folder
        os.mkdir(folder_path)

        # Get the file name
        file_name = os.path.basename(file_path)

        # Copy the file to the folder
        shutil.copy(file_path, os.path.join(folder_path, file_name))

        # Update the file path in the config file
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'filepath': os.path.join(folder_path, file_name)}
        with open(config_path, 'w') as configfile:
            config.write(configfile)

        # Access the file path from the config file
        config.read(config_path)
        new_file_path = config['DEFAULT']['filepath']
        print("The new file path is: ", new_file_path)

if __name__ == '__main__':
    main()
