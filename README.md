# Movie Recommender System 

This repository contains Python scripts for a movie recommendation system based on Collaborative Filtering with K-Nearest Neighbors (KNN). The recommendation system allows the user to input a movie they like and receive recommendations for similar movies.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

The following Python packages are needed:
* pandas
* numpy
* surprise
* os

You can install them using pip:
```bash
pip install pandas numpy scikit-surprise
```

### Installation

1. Clone the repo
```bash
git clone https://github.com/your_username_/Project-Name.git
```
2. Navigate into the directory
```bash
cd Project-Name
```

## Usage

The scripts in this repository define two classes: `Movie_KNN_recommender` and `Recommender`.

`Movie_KNN_recommender` is the main class, which reads in a CSV file of movies and another of ratings, and trains a KNN model on this data. The model can be of three types: KNNBaseline, KNNWithMeans, or KNNBasic, determined by the `mode` parameter of the class's initializer.

The `get_similar_movies` method takes a `movieID` and an optional `num` (default 10) and returns the IDs of `num` movies similar to the input movie, according to the trained KNN model.

The `recommend` method takes the same parameters, but instead of returning movie IDs, it returns the actual movie titles.

The `Recommender` class is a user interface for the `Movie_KNN_recommender`. It prompts the user to select a movie they like from a randomly chosen list of 5 movies, and then uses the `Movie_KNN_recommender` to generate and print a list of 10 similar movies.

The recommender system can be run by executing the script `Recommender.py`.

## Example

An example usage of the `Movie_KNN_recommender` is commented out in the script:

```python
# test = Movie_KNN_recommender()
# result = test.recommend(122922, 10)
# for i in result:
#     print(i.values[0])
```

This example creates an instance of `Movie_KNN_recommender`, gets 10 recommendations for the movie with ID 122922, and prints each one.

## Dataset

The dataset used in this project is not included in the repository. It should include two CSV files located in a `data/personal` directory:

* `movies.csv` containing a `movieId` and `title` column
* `ratings.csv` containing `userId`, `movieId`, and `rating` columns
