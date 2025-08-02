# Music Recommendation System

Welcome to our Music Recommendation App — a simple yet effective Python-based content filtering system that suggests songs similar to the one you like. Using text-based features like artist name, genre, and track metadata, this app finds songs that match your taste.

## Project Overview

This project uses a **content-based filtering** technique with **TF-IDF vectorization** and **cosine similarity** to recommend songs. It reads data from a `.csv` file and matches similar songs based on combined text features.


## Technologies & Libraries

- **Python**
- **pandas** – for data manipulation
- **scikit-learn** – for TF-IDF and similarity measures
- **numpy** – for vector operations


##  Features

- Simple command-line interface
- Reads song data from `songs.csv`
- Combines metadata (artist, genre, etc.) for recommendations
- Outputs top N similar songs to a given track


##  Setup Instructions

### Prerequisites

- Python 3.x installed
- Required libraries: `pandas`, `scikit-learn`, `numpy`

