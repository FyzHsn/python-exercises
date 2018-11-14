import numpy as np


def retrieve_height_data():
    """
    Retrieve height data

    For a given mean and standard deviation, generate a normal distribution
    of heights. This method is meant to mock data retrieval from some
    database.

    :return: list of heights
    """

    heights = np.random.normal(6, 0.5, 10)
    return heights


def compute_height_stats():
    """
    Compute height statistics

    This method retrieves some height data from a database and computes the
    mean and the standard deviation.

    :return: tuple of the form (height mean, height standard deviation)
    """

    # Retrieve height data
    heights = retrieve_height_data()

    # Compute height statistics
    height_mean = np.mean(heights)
    height_std = np.std(heights)

    return height_mean, height_std

