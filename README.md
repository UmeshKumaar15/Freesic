# Freesic

## Overview
Freesic is a desktop music player that utilizes a Tkinter-based GUI. It features robust playlist management, integrates with YouTube and Google Custom Search API for song and album cover retrieval, and offers seamless multimedia playback controls for an enhanced user experience.

## Getting Started with Freesic:

### Fork the Repository:
Fork the Freesic 2023 repository on GitHub by clicking the "Fork" button at the top-right of the repository page. This creates your copy of the repository, allowing you to make changes.

### Clone the Repository:
Clone your forked repository to your local machine using the following command in your terminal or command prompt:

```bash
git clone https://github.com/UmeshKumaar15/Freesic.git
```

### Install Dependencies:
Navigate to the project directory and install the required dependencies from `dependency.txt` by running the following command:

```bash
pip install -r dependencies.txt
```

This command installs the necessary libraries, including pytube, youtubesearchpython, googleapiclient, pygame, and PIL, which are used by Freesic 2023.


### Obtain API Key and Custom Search Engine ID:

```url
https://developers.google.com/custom-search/v1/overview
```

Create a custom search engine and get the Custom Search Engine ID here then configure API Key and Custom Search Engine ID.

Open the Freesic 2023 project and locate the section in the code where the API key and Custom Search Engine ID are used. Update the values with your obtained API key and Custom Search Engine ID.


### Run the Application:
Execute the main script to launch Freesic 2023:

```python
python main.py
```

The application window should open, and you can start using Freesic seamlessly!

## Working:

### Main Function
The core functionality of the application is initiated through the main script where it creates the Tkinter application.

### Download Song:
The code for downloading songs and their respective album covers is included in the project. This functionality utilizes various libraries, including pytube, youtubesearchpython, and googleapiclient. The API key and custom search engine ID are required for song and album cover searches.

### Playback:
Playback controls include play, pause, previous, and next buttons. The application supports the display of album covers and provides options to add new songs to the playlist.
It also has the Tkinter interface which consists of a customized title bar with minimize, maximize, and close buttons. The main window includes a playlist display, playback controls, and the ability to add new songs. The interface is designed with a focus on user experience.

## Author
Umesh Kumaar

## Disclaimer
Please make sure to comply with YouTube's terms of service when using the song download functionality.

## Contribution
We welcome contributions! If you'd like to contribute to Freesic, fork the repository and submit a pull request. Your help is greatly appreciated.
