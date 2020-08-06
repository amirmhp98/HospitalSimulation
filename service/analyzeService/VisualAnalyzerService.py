import math

import matplotlib.pyplot as plt


class VisualAnalyzerService:
    def __init__(self, simulation_matrix):
        self.simulation_matrix = simulation_matrix
        self.waiting_time_freq = dict()
        self.waiting_time_freq_corona = dict()
        self.waiting_time_freq_normal = dict()
        self.service_time_freq = dict()
        self.service_time_freq_corona = dict()
        self.service_time_freq_normal = dict()
        self.total_time_freq = dict()
        self.total_time_freq_corona = dict()
        self.total_time_freq_normal = dict()
        self.process_matrix()

    def process_matrix(self):
        for patient in self.simulation_matrix:
            self.increase_floor(self.total_time_freq_normal, patient['time_spent_in_system'])
            self.increase_floor(self.waiting_time_freq_normal, patient['time_waited_in_queue'])
            self.increase_floor(self.service_time_freq_normal,
                                patient['time_spent_in_system'] - patient['time_waited_in_queue'])
            if (patient['type'] == 'normal'):
                self.increase_floor(self.total_time_freq, patient['time_spent_in_system'])
                self.increase_floor(self.waiting_time_freq, patient['time_waited_in_queue'])
                self.increase_floor(self.service_time_freq,
                                    patient['time_spent_in_system'] - patient['time_waited_in_queue'])
            else:
                self.increase_floor(self.total_time_freq_corona, patient['time_spent_in_system'])
                self.increase_floor(self.waiting_time_freq_corona, patient['time_waited_in_queue'])
                self.increase_floor(self.service_time_freq_corona,
                                    patient['time_spent_in_system'] - patient['time_waited_in_queue'])

    def plot_diagrams(self):
        plt.plot(self.total_time_freq.keys(), self.total_time_freq.values())
        plt.title("total time freq corona and normal")
        plt.show()
        plt.plot(self.total_time_freq_normal.keys(), self.total_time_freq_normal.values())
        plt.title("total time freq normal")
        plt.show()
        plt.plot(self.total_time_freq_corona.keys(), self.total_time_freq_corona.values())
        plt.title("total time freq corona")
        plt.show()

        plt.plot(self.waiting_time_freq.keys(), self.waiting_time_freq.values())
        plt.title("waiting time freq corona and normal")
        plt.show()
        plt.plot(self.waiting_time_freq_normal.keys(), self.waiting_time_freq_normal.values())
        plt.title("waiting time freq normal")
        plt.show()
        plt.plot(self.waiting_time_freq_corona.keys(), self.waiting_time_freq_corona.values())
        plt.title("waiting time freq corona")
        plt.show()
        
        plt.plot(self.service_time_freq.keys(), self.service_time_freq.values())
        plt.title("service time freq corona and normal")
        plt.show()
        plt.plot(self.service_time_freq_normal.keys(), self.service_time_freq_normal.values())
        plt.title("service time freq normal")
        plt.show()
        plt.plot(self.service_time_freq_corona.keys(), self.service_time_freq_corona.values())
        plt.title("service time freq corona")
        plt.show()
        print("plotted")

    def increase_floor(self, the_dict, key):
        key = (math.floor(key * 100)) / 100
        if key in the_dict:
            the_dict[key] += 1
        else:
            the_dict[key] = 1
