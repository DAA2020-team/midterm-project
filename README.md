# Midterm-project
Midterm project for Design and Analysis of Algorithms 2020/2021 - Group 12

GitHub Repository: [https://github.com/DAA2020-team/midterm-project](https://github.com/DAA2020-team/midterm-project)

## Team Members
* [Giovanni Ammendola](https://github.com/giorge1)
* [Riccardo Imparato](https://github.com/r4004)
* [Stefano La Corte](https://github.com/phesmatos)
* [Vincenzo Petrone](https://github.com/v8p1197)

## Documentation
[//]: # "See the [documentation](documentation.pdf) for further information. TODO: add documentation pdf"

## Usage
The lower python version which these files have been tested is 3.6.9. Compatibility should not be a problem, assuming that a not too old version is used.

### Exercise 1
1. Change directory to `exercise1` folder.
2. Run [main.py](exercise1/main.py) to test the DoubleHashingHashMap.
    3. This will perform 70 add operation and then 30 delete operation, showing the total number of collisions.
    
The ADT implementation is in the `data_structures` folder, in the file `double_hashing_hash_map.py`.

### Exercise 2
1. Change directory to `exercise2` folder.
2. Run [main.py](exercise2/main.py) to test the Currency Class.
    2. This will test a few methods of the class

The implementation of the class is in the file [currency.py](exercise2/currency.py)

### Exercise 3
1. Change directory to `exercise3` folder.
2. Run [main.py](exercise3/main.py) to test the implementation of the MultiWaySearchTree.
    3. This will add some currencies to the tree and will print them.
    
The implementation of the ADT is in the `data_structures` folder, in the file [multi_way_search_tree.py](exercise1/multi_way_search_tree.py).

### Exercise 4
1. Change directory to `exercise4` folder.
2. Run [main.py](exercise4/main.py) to test the implementation of the `change()`.
    3. There are some parameters to pass to the test function that can customize the test. In particular
     there is the `manual` parameter and if is set to `True`, the test will print more information and will proceed step
     by step, waiting for a enter key press for each one.
   
## Other resources
In the `resources` folder there is the [primes.bin](resources/primes.bin) file, which contains prime numbers used by the DoubleHashingHashMap.

In the [utils.py](utils.py) there are some support function used by different modules.

