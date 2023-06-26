# Core Algorithm Overview

Author: Sean Lee (010506773)

### Stated Problem:

The purpose of this program is to implement an algorithm for the Western Governors University Parcel Service that self adjusts itself
to find the shortest path for delivering the packages on the truck. There are a total of 40 packages that need to be loaded between 3 trucks
and is limited to 2 drivers. 

### Algorithm Overview

The algorithm used is a greedy algorithm called the Nearest Neighbor algorithm. It finds the next closest delivery by doing the following:

1. Move all packages from the truck to a sorting list and empty the truck's packages list.

2. As long as there are packages in the sorting list:
    1. Set the "next distance" to infinity and "next package" to none. These will store the shortest distance to a package and that package.
  
    2. Loop over each package in the sorting list:
        1. Compute the distance from the truck's current location to the package's location.
      
        2. If this distance is smaller than the current "next distance", update "next distance" to this distance and "next package" to the current package.
  
    3. Append the "next package" back to the truck's packages list.
   
    4. Move the truck to the location of "next package", given the calculated "next distance".
   
    5. Calculate the time taken to travel to "next package" based on the "next distance" and the truck's speed.
   
    6. Remove the "next package" from the sorting list.
   
    7. Register the delivery of the "next package" and add it to the list of delivered packages of the truck.
   
    8. Update the truck's current time and total travel time by adding the time travelled.
   
    9. Update the delivery time and departure time of the "next package" using the truck's updated time.

The time complexity is O(n^2) where n is the number of packages. This is due to the nested loop for each package, 
we're checking the distance to all the other packages. This is done for each package in the list, hence the n^2 time complexity. 
This algorithm can perform well when the number of packages (n) is not too large.

### Advantages of the chosen algorithm:

At each step, the code makes the 'greedy' choice by choosing the package closest to the truck's current location to deliver next, thus ensuring that the truck always takes the shortest possible route to its next delivery.
This approach doesn't necessarily result in the shortest route for all deliveries (because a globally optimal solution might sometimes require taking a longer route for the next delivery to get a shorter overall path), 
but it does give a locally optimal solution at each step, which is why it's considered a 'greedy' algorithm.

Alternatively I could have used a dynamic solution to solve this like the 'Held-Karp algorithm'. This would have broken the 
problem down into smaller subset problems but this is even worse for larger inputs with a complexity of (O(n^2 * 2^n))

### Self-Adjusting Data Structures

The application utilizes a self-adjusting hash table to store package information. This structure allows for quick insertion and retrieval of packages, both operations with a time complexity of O(1) on average.
The hash table may have weaknesses in situations where collisions occur frequently, causing the lookup time to slow down quite a bit. 

### Adaptability
The application is designed to adapt and scale to an increasing number of packages. The primary delivery algorithm is 
self-adjusting; it will handle any number of packages or trucks provided to it. Additionally, the hash-table data structure for package storage is also self-adjusting and will accommodate an increasing number of packages without changes to the code.

### Development Environment

This project was completed in the PyCharm IDE, using the latest version of python 3. No external libraries need to be installed

### Software Efficiency and Maintainability

The entire program runs in polynomial time, with the most complex operation being the delivery algorithm with a time complexity of O(n^2). This makes the software efficient enough for practical purposes, given the expected number of packages and trucks.
The software's maintainability is enhanced by the clear, modular structure of the code. Functions are small, single-purpose, and named to reflect their behavior. Comments are included to describe the process and flow of the program.

### Space-Time and Big-O
The space-time complexity for each major block of code and the entire program has been documented using Big-O notation below.
The primary delivery algorithm, implemented in the deliver_packages function, is O(n^2) as it iterates over
the list of packages within a loop that iterates over the list of delivery trucks. This results in quadratic time complexity due to the nested loops.

## Time and Space Complexity

### Package Class Methods

| Method        | Time Complexity | Space Complexity |
|---------------|-----------------|------------------|
| update_status | O(1)            | O(1)             |
| __str__       | O(1)            | O(1)             |

### HashMap Class Methods

| Method | Time Complexity | Space Complexity |
|--------|-----------------|------------------|
| insert | O(1)            | O(1)             |
| remove | O(1)            | O(1)             |
| lookup | O(1)            | O(1)             |

### SimulateDelivery Class Methods

| Method                   | Time Complexity | Space Complexity |
|--------------------------|-----------------|------------------|
| csv_to_list              | O(n)            | O(n)             |
| load_package_map         | O(n)            | O(n)             |
| generate_lists           | O(n)            | O(n)             |
| generate_distance_matrix | O(n^2)          | O(n^2)           |
| find_distance            | O(n)            | O(1)             |
| load_truck               | O(n)            | O(1)             |
| deliver_packages         | O(n^2)          | O(n)             |