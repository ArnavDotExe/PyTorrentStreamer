# Python Movie Search and Streaming Application

This project is a command-line application for searching, streaming, and downloading movies using torrent technology.

The application allows users to search for movies by name, view detailed information about the search results, and then choose to either stream or download the selected movie. It utilizes the YTS API for fetching movie data and integrates with the WebTorrent CLI for handling the streaming and downloading processes.

## Repository Structure

- `index.py`: Main entry point of the application
- `movie.py`: Contains the Movie class for handling movie-related operations
- `fetch.py`: Implements the Fetch class for API interactions
- `build/`: Directory containing build artifacts (not directly relevant for users)

## Usage Instructions

### Installation

Prerequisites:
- Python 3.6+
- pip (Python package installer)
- WebTorrent CLI (for streaming and downloading)
- VLC media player (for streaming)

To install the required Python packages:

```bash
pip install requests tabulate
```

To install WebTorrent CLI (requires Node.js):

```bash
npm install -g webtorrent-cli
```

### Getting Started

1. Clone the repository or download the source files.
2. Navigate to the project directory in your terminal.
3. Run the application:

```bash
python index.py
```

### Using the Application

1. When prompted, enter the name of the movie you want to search for.
2. The application will display a list of matching movies with details like title, year, description, size, and torrent information.
3. Enter the index number of the movie you want to stream or download.
4. Choose the desired quality option if multiple are available.
5. Select whether you want to stream (1) or download (2) the movie.
6. The application will use WebTorrent CLI to handle the streaming or downloading process.

### Troubleshooting

Common issues and solutions:

1. Problem: "Command not found" error when trying to use WebTorrent
   - Error message: `webtorrent: command not found`
   - Solution: Ensure that WebTorrent CLI is installed globally and that your system's PATH includes the npm global bin directory.
   - Diagnostic steps:
     1. Run `npm list -g webtorrent-cli` to check if WebTorrent is installed globally.
     2. If not installed, run `npm install -g webtorrent-cli`.
     3. Verify the installation by running `webtorrent --version`.

2. Problem: VLC player not opening for streaming
   - Error message: No specific error, but the movie doesn't start playing
   - Solution: Ensure VLC is installed and properly configured in your system's PATH.
   - Diagnostic steps:
     1. Open a terminal and run `vlc --version` to check if VLC is accessible from the command line.
     2. If not found, install VLC and add its installation directory to your system's PATH.

3. Problem: Movie search returns no results
   - Error message: "{movie_name} resulted in 0 results"
   - Solution: Try different search terms or check your internet connection.
   - Diagnostic steps:
     1. Verify your internet connection by opening a web browser.
     2. Try searching for a very popular movie to test if the API is responding.
     3. Check if the YTS API is accessible by visiting their website.

### Debugging

To enable debug mode and verbose logging:

1. Open `index.py` in a text editor.
2. Add the following lines at the beginning of the `main()` function:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
```

3. Add `logger.debug()` statements throughout the code where you want to log information.

Log files are not explicitly created by this application. Debug output will be printed to the console.

## Data Flow

The application follows this data flow for processing user requests:

1. User inputs a movie name for search
2. `Fetch` class sends a request to the YTS API
3. API returns movie data in JSON format
4. `Movie` class processes and displays the movie information
5. User selects a movie and chooses to stream or download
6. `Movie` class generates a magnet link for the selected movie
7. WebTorrent CLI is invoked to handle streaming or downloading

```
[User Input] -> [Fetch] -> [YTS API] -> [Movie] -> [User Selection] -> [WebTorrent CLI] -> [Streaming/Downloading]
```

Important technical considerations:
- The application relies on external services (YTS API and torrent network) for functionality
- Streaming and downloading speeds depend on torrent seed availability
- VLC player is required for streaming functionality
