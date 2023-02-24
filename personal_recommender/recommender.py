from KNN_movie import Movie_KNN_recommender
import pandas as pd
from surprise import Reader, Dataset
import random


class Recommender:
    def __init__(self):
        self.df = pd.read_csv('../data/personal/movies.csv')
        # self.movies = self.df['title'].tolist()
        # self.ids = self.df['movieId'].tolist()
        # self.reader = Reader()
        self.userInput = 0
        self.getUserInput()
        self.getRecs()

    def getCandidates(self):
        # n = 5
        # self.candidates = random.sample(self.movies, n)
        self.candidates = self.df.sample(n=5)

    def getUserInput(self):
        self.getCandidates()
        while self.userInput == 0:
            print("Please choose a movie you like from the following:\n")
            for i, e in enumerate(self.candidates['title']):
                print(i + 1, e)
            print("\nIf none, type 0 for more selections.\n")
            self.userInput = int(input("Enter a number:"))
            if self.userInput == 0:
                self.getCandidates()
            elif self.userInput > 5:
                print('Invalid input\n')
                input()
                self.userInput = 0

        self.pickID = self.candidates['movieId'].iloc[
            self.userInput - 1]

    def getRecs(self):
        knn_rec = Movie_KNN_recommender()
        result = knn_rec.recommend(self.pickID, 10)
        for i in result:
            print(i.values[0])


if __name__ == '__main__':
    rec = Recommender()


# df = pd.read_csv('../data/personal/movies.csv')

# movies = df['title'].tolist()
# n = 4
# # printing n elements from list
# candidates = random.sample(movies, n)

# username = input("Enter username:")
# print("Username is: " + username)
