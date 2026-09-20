# Proj 2
by Dhwanil Patel
Second Project on Hashing for EN.605.620.81.FA24

## Running Proj2 module
1. Download and install the latest version of Python on your computer
2. Navigate to this directory (containing the README.md)
3. The input files should be in the same directory as the README.md; if not, use the full path
4. The output files will be created in a new directory that is named by user
5. Run the program as a module (with real inputs): `python -m Proj2 <input_name> <output_dir_name>`

#### Possible "Hashing Scheme" parameters:
```commandline
1. "division"
    Modulo must be an integer, preferably a prime close to the hash table size (120).
2. "multiplication"
    Modulo will act as one of the parameters m for the multiplication equation which is as follows:
    
    floor(m * ((key * a) mod 1))
```
#### Possible "Bucket Size" parameters:
```commandline
Integer >= 1 that's a factor of the hash table size (ideally one of the smaller factors)
```
#### Possible "Collision Handling" parameters:
```commandline
1. "linear" - Linear Probing
2. "quadratic" - Quadratic Probing
3. "chaining" - Chaining within the table
```
### PatelD_StrassenLab Usage:
```commandline
usage: python -m Proj2 [-h] input_file output_dir_file

positional arguments:
  input_file
  output_dir_file

optional arguments:
  -h, --help  show this help message and exit
```

### PatelD_HashingLab Layout

* [PatelD_HashingLab](.): The parent or "root" folder containing all of these files
    * [README.md](README.md): The guide you're reading. All software should come with a readme!
    * [Proj2](Proj2): 
      This is a *module* in the *package*. 
      * [`__init__.py`](Proj2/__init__.py) 
        This is a very important file and is often blank. It is used to expose what functions, variables, classes, etc are exposed when scripts import this module. It can also hide functions/variables
      * [`__main__.py`](Proj2/__main__.py) 
        This file is the entry point to the program. It usually just handles command line arguments, similar to Java and C's main() functions.
      * [`hashtable.py`](Proj2/hashtable.py)
        This file contains the class for hash table
      * [`collisionhandler.py`](Proj2/collisionhandler.py)
        This file contains the class that handles collisions
    * [LabHashingInput.txt](LabHashingInput.txt)
      Required input provided by the professor
    * [required_outputs](required_outputs):
      * 14 different output files for each scheme using LabHashingInput.txt
    * [size36_outputs](size36_outputs):
      * 14 different output files for each scheme using size36_input.txt
    * [size84_outputs](size84_outputs):
      * 14 different output files for each scheme using size84_input.txt
    * [size108_outputs](size108_outputs):
      * 14 different output files for each scheme using size108_input.txt
    * [size124_outputs](size124_outputs):
      * size124_input.txt is an error input because it contains more numbers than buckets available.