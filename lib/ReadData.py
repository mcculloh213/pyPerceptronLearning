import math
import csv
__author__ = "H.D. 'Chip' McCullough IV"


def read_data(f_in):
    try:
        f = open(f_in, 'r')                                          # Open param:f_in
        n = int(f.readline())                                        # Read the number of variables & store it as an int
        dataset = list(csv.reader(f))                                # Read the rest of the data as a CSV
        f.close()                                                    # Close param:f_in
        for i in range(0, len(dataset)):                             # Clean the obtained data
            dataset[i] = [int(x) for x in dataset[i]]                # Convert data from str to int
            dataset[i].insert(0, -1)                                  # Insert bias x0
        n += 1                                                       # Increment n to account for bias x0

        return n, dataset                                            # Return N, data

    except Exception as e:
        # TODO: Handle exception
        pass
