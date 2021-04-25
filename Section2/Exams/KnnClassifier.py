import numpy as np
import math
import random
import operator
import cv2
import csv


def calcEucdistance(x1, x2, length):
    distance = 0
    for i in range(length):
        distance += pow(x1[i] - x2[i], 2)
    return math.sqrt(distance)


def knn(vectors, testInstance, k):
    distances = []
    length = len(testInstance)
    for x in range(len(vectors)):
        dist = calcEucdistance(testInstance,
                               vectors[x], length)
        distances.append((vectors[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def responseOfNeighbors(neighbors):
    all_possible_neighbors = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in all_possible_neighbors:
            all_possible_neighbors[response] += 1
        else:
            all_possible_neighbors[response] = 1
    sortedVotes = sorted(all_possible_neighbors.items(),
                         key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

def loadDataset(
    filename,
    filename2,
    training_feature_vector=[],
    test_feature_vector=[],
    ):
    with open(filename) as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)):
            for y in range(3):
                dataset[x][y] = float(dataset[x][y])
            training_feature_vector.append(dataset[x])

    with open(filename2) as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)):
            for y in range(3):
                dataset[x][y] = float(dataset[x][y])
            test_feature_vector.append(dataset[x])

def main(training_data, test_data):
    training_feature_vector = []
    test_feature_vector = []
    loadDataset(training_data, test_data, training_feature_vector, test_feature_vector)
    classifier_prediction = []
    k = 5
    for x in range(len(test_feature_vector)):
        neighbors = knn(training_feature_vector, test_feature_vector[x], k)
        print(neighbors)
        result = responseOfNeighbors(neighbors)
        print(result)
        classifier_prediction.append(result)
    return classifier_prediction