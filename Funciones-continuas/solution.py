import numpy as np


class solution:

    def __init__(self, d: int, f):
        self.size = d
        self.cells = np.zeros(self.size, float)
        self.fitness = 0.0
        self.function = f

    def from_solution(self, origin):
        self.size = origin.size
        self.cells = np.copy(origin.cells)
        self.fitness = origin.fitness
        self.function = origin.function

    # Original code
    # def Initialization(self):
    #     self.cells = np.random.uniform(
    #         low=self.function.lower_bound, high=self.function.upper_bound, size=(self.size,))
    #     self.fitness = self.function.evaluate(self.cells)

    # def tweak(self, bandwidth: float):
    #     bandwidths = np.random.uniform(
    #         low=-bandwidth, high=bandwidth, size=(self.size,))
    #     self.cells = self.cells + bandwidths
    #     self.cells[self.cells <
    #                self.function.lower_bound] = self.function.lower_bound
    #     self.cells[self.cells >
    #                self.function.upper_bound] = self.function.upper_bound
    #     self.fitness = self.function.evaluate(self.cells)

    def Initialization(self):
        # Bimodal distribution
        # Creating first normal distribution
        self.mu_1, self.sigma_1 = self.function.lower_bound/2, abs(self.function.lower_bound/4+1)
        self.size_1 = self.size//2 
        self.cells_1 = np.random.normal(loc=self.mu_1, scale=self.sigma_1, size=self.size_1)
        # Creating second normal distribution
        self.mu_2, self.sigma_2 = self.function.upper_bound/2, (self.function.upper_bound/4+1)
        self.size_2 = self.size-self.size_1     
        self.cells_2 = np.random.normal(loc=self.mu_2, scale=self.sigma_2, size=self.size_2)
        # Concatenate normal distributions
        self.cells = np.concatenate((self.cells_1, self.cells_2))
        # Delimit lower and upper bounds
        self.cells[self.cells < self.function.lower_bound] = self.function.lower_bound
        self.cells[self.cells > self.function.upper_bound] = self.function.upper_bound
        self.fitness = self.function.evaluate(self.cells)

    def tweak(self, bandwidth: float):
        # Bimodal distribution for bandwidth
        # Creating first normal distribution
        self.mu_bw_1, self.sigma_bw_1 = -bandwidth/2, abs(bandwidth/4+1)
        self.size_bw_1 = self.size//2 
        self.bandwidths_1 = np.random.normal(loc=self.mu_bw_1, scale=self.sigma_bw_1, size=self.size_bw_1)
        # Creating second normal distribution
        self.mu_bw_2, self.sigma_bw_2 = -bandwidth/2, (bandwidth/4+1)
        self.size_bw_2 = self.size-self.size_bw_1     
        self.bandwidths_2 = np.random.normal(loc=self.mu_bw_2, scale=self.sigma_bw_2, size=self.size_bw_2)
        # Concatenate normal distributions
        self.bandwidths = np.concatenate((self.bandwidths_1, self.bandwidths_2))
        self.cells = self.cells + self.bandwidths
        self.cells[self.cells < self.function.lower_bound] = self.function.lower_bound
        self.cells[self.cells > self.function.upper_bound] = self.function.upper_bound
        self.fitness = self.function.evaluate(self.cells)

    def __str__(self):
        return "cells:" + str(self.cells) + \
               "-fit:" + str(self.fitness)
