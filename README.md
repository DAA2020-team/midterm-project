# Midterm-project

Midterm project for Design and Analysis of Algorithms 2020/2021 - Group 12

GitHub Repository: [https://github.com/DAA2020-team/midterm-project](https://github.com/DAA2020-team/midterm-project)

## Team Members
* [Giovanni Ammendola](https://github.com/giorge1)
* [Riccardo Imparato](https://github.com/r4004)
* [Stefano La Corte](https://github.com/phesmatos)
* [Vincenzo Petrone](https://github.com/v8p1197)

## Usage
### Requirements
#### Python
The lower python version which these files have been tested is 3.6.9. Compatibility should not be a problem, assuming that a not too old version is used.

#### Dependencies
In order to run these file, it is necessary to install the [iso4217](https://pypi.org/project/iso4217/) ([github repository](https://github.com/dahlia/iso4217)) module for python. 
This module is used in order to get real ISO4217 codes and to check that the codes added are valid. 
It can be installed using pip, running the following command: 

`pip install iso4217`

### Exercise 1

1. Change directory to the root folder.
2. Run `python exercise1/main.py` to test the DoubleHashingHashMap.
    * This will perform 70 add operations and then 30 delete operations, showing the total number of collisions.
    
The ADT implementation is in the `data_structures` folder, in the file [double_hashing_hash_map.py](https://github.com/DAA2020-team/midterm-project/blob/master/data_structures/double_hashing_hash_map.py).

### Exercise 2

1. Change directory to the root folder.
2. Run `python exercise2/main.py` to test the Currency Class.
    * This will test a few methods of the class

The implementation of the class is in the file [currency.py](https://github.com/DAA2020-team/midterm-project/blob/master/exercise2/currency.py)

### Exercise 3

1. Change directory to the root folder.
2. Run `python exercise3/main.py` to test the implementation of the MultiWaySearchTree.
    * This will add some currencies to the tree and will print them.
    
The implementation of the ADT is in the `data_structures` folder, in the file [multi_way_search_tree.py](https://github.com/DAA2020-team/midterm-project/blob/master/data_structures/multi_way_search_tree.py).

### Exercise 4

1. Change directory to the root folder.
2. Run `python exercise4/main.py` to test the implementation of the `change()` function.
    * There are some parameters to pass to the test function that can customize the test. In particular
        there is the `manual` parameter and if is set to `True`, the test will print more information and will proceed step
        by step, waiting for a enter key press for each one.
        
The implementation of the `change()` function is in the [exercise4/main.py](https://github.com/DAA2020-team/midterm-project/blob/master/exercise4/main.py)
   
## Other resources
In the `resources` folder there is the [primes.bin](https://github.com/DAA2020-team/midterm-project/blob/master/resources/primes.bin) file, which contains prime numbers used by the DoubleHashingHashMap.

In the [utils.py](https://github.com/DAA2020-team/midterm-project/blob/master/utils.py) module there are some support functions used by different modules.
