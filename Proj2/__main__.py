# By Dhwanil Patel
# Programming Lab 2

from pathlib import Path
import argparse
import os
import shutil
from Proj2 import hashtable
from Proj2.collisionhandler import Node
import time

# Creates arguments for command line usage
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input_file", type=str)
arg_parser.add_argument("output_directory", type=str)
args = arg_parser.parse_args()

# Creates file path variables for each of the arguments
input_path = Path(args.input_file)
dir_path = Path(args.output_directory)

# Check if a folder for outputs exist; if so, delete them to create a new one
if os.path.exists(dir_path):
    shutil.rmtree(dir_path)
os.makedirs(dir_path)


table_size = 120
# Different schemes being tested
schemes = [['division', 120, 1, 'linear'], ['division', 120, 1, 'quadratic'], ['division', 120, 1, 'chaining'],
           ['division', 127, 1, 'linear'], ['division', 127, 1, 'quadratic'], ['division', 127, 1, 'chaining'],
           ['division', 113, 1, 'linear'], ['division', 113, 1, 'quadratic'], ['division', 113, 1, 'chaining'],
           ['division', 41, 3, 'linear'], ['division', 41, 3, 'quadratic'], ['multiplication', 120, 1, 'linear'],
           ['multiplication', 120, 1, 'quadratic'], ['multiplication', 120, 1, 'chaining']]

# Goes through every scheme
for i in range(1,15):

    file_path = os.path.join(dir_path, f'Scheme{i}.txt')
    scheme = schemes[i-1][0]
    modulo = schemes[i-1][1]
    bucket_size = schemes[i-1][2]
    collision_type = schemes[i-1][3]
    hashtable.counter = [0,0,0]

    # Writes an output file for each scheme
    with input_path.open('r') as input, open(file_path,'w') as output:
        input_lines = input.readlines()
        keys = []
        for line in input_lines:
            line = line.strip().split()
            # Checks if the values from the input are integers. If not, they are ignored
            try:
                for num in line:
                    int_check = int(num)
                    keys.append(num)
            except:
                continue

        # Checks if the number of keys obtained from input file exceeds table size
        if len(keys) > table_size:
            raise Exception("There are more keys than possible buckets in the hash table")

        # Writes the parameters used at the top of output file
        output.write(f'Hash table size: {table_size}\n')
        output.write(f'Bucket size: {bucket_size}\n')
        output.write(f'Hashing Scheme: {scheme}\n')
        if scheme == 'division':
            output.write(f'Modulo: {modulo}\n')
        if scheme == 'multiplication':
            output.write(f'Multiplication parameters: a = 0.127, m = {modulo}\n')
        output.write(f'Collision Scheme: {collision_type}\n')
        output.write(f'_______________________________\n')

        # Timer starts before hash table is created and ends after all keys are entered
        start_time = time.time()
        # Creates a hash table using the HashTable class from hashtable.py
        hash_table = hashtable.HashTable(table_size, scheme, modulo, bucket_size, collision_type)
        for key in keys:
            hash_table.insert(key)
        end_time = time.time()

        # Obtains the results from hashtable.py and outputs them to the file
        hash_array = hash_table.get_array()
        total_collisions = hashtable.counter[2]
        total_primary = hashtable.counter[1]
        total_secondary = hashtable.counter[2] - hashtable.counter[1]
        total_comparisons = total_collisions + len(keys)
        total_time = (end_time - start_time) * 10 ** 3
        load_factor = len(keys) / table_size
        output.write(f'Load Factor: {load_factor}\n')
        output.write(f'# of comparisons: {total_comparisons}\n')
        output.write(f'# of collisions: {total_collisions}\n')
        output.write(f'# of primary collisions: {total_primary}\n')
        output.write(f'# of secondary collisions: {total_secondary}\n')
        output.write(f'Hashing runtime: {total_time:.3f} ms\n')
        output.write(f'_______________________________\n')

        # Formatting differs for different bucket sizes
        # For bucket size = 1, each line contains 5 buckets
        if bucket_size == 1:
            for num in range(0, len(hash_array), 5):
                line = hash_array[num:num + 5]
                for n in range(len(line)):
                    if type(line[n]) == Node:
                        line[n] = line[n].value
                    elif len(line[n]) == 0:
                        line[n].append("_____")
                output.write('\t'.join(map(str, line)) + '\n')

        # For bucket sizes greater than 1, each line contains one bucket and they are numbered
        if bucket_size > 1:
            linecount = 0
            for num in hash_array:
                linecount += 1
                printline = []
                for n in num:
                    printline.append([n])
                for i in range(bucket_size - len(num)):
                    printline.append(["_____"])

                output.write(str(linecount)+ '\t' + '\t'.join(map(str, printline)) + '\n')