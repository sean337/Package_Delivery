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

At each step, the algorithm makes the 'greedy' choice by selecting the package closest to the truck's current location 
for the next delivery. This ensures that the truck always takes the shortest possible route to its next delivery, 
optimizing efficiency. This strategy is especially useful when dealing with a large number of delivery points, as it 
circumvents the need for computing a complete delivery route beforehand, which can exponentially increase with the 
number of delivery points. The greedy algorithm's simplicity and ease of implementation provide a clear advantage. It 
provides a reasonable approximation for the ideal solution, which would otherwise be computationally expensive to 
calculate, contributing to better maintainability and readability of the code. Although this approach does not 
necessarily result in the shortest overall route for all deliveries (because a globally optimal solution might sometimes 
require a longer route for the next delivery to achieve a shorter overall path), it does offer a locally optimal 
solution at each step, thus justifying its 'greedy' label.

Two alternative solutions to solve the problem could be the 'Held-Karp algorithm' or 'A* Search Algorithm'. The 
Held-Karp algorithm, is a dynamic programming solution, and would break the problem down into smaller subset problems. It 
aims to solve the Traveling Salesman Problem exactly, providing a global optimum. However, its time complexity of 
O(n^2 * 2^n) means it's not ideal for larger inputs. On the other hand, the A* Search Algorithm, is a graph traversal and 
path search algorithm, that could work as well. It is optimal when the heuristic function is admissible, and often 
performs well in practice. Its time complexity is O(b^d), where b is the branching factor 
(the average number of successors per state) and d is the depth of the optimal solution. However, this can vary 
significantly depending on the specifics of the problem at hand. The A* algorithm also has a significant memory 
requirement, as it needs to store all generated nodes. It might not be the most suitable for this scenario due to the 
dynamic nature of the problem, where the state of the graph changes after each delivery. In contrast, the chosen method,
a 'greedy' version of 'Dijkstra's Algorithm' or the 'Nearest Neighbor algorithm', does not necessarily provide the 
globally optimal solution, but it is more efficient for this specific scenario. It operates with a time complexity of 
O(n^2), which is considerably better for larger inputs. It also more directly meets the requirements of the scenario, 
where a truck must simply find the next shortest route from its current location and does not need to calculate a total 
optimized route beforehand.

#### References:

[A* Seach Wiki](https://en.wikipedia.org/wiki/A*_search_algorithm)

[Held-Karp Wiki](https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm)

### Self-Adjusting Data Structures

The hash table's key-value pairs enable us to establish a relationship between a package's ID (used as the key) and its 
corresponding details (the value). Similar to a built-in Python dictionary. This structure allows for quick insertion 
and retrieval of packages based on their IDs, both operations with a time complexity of O(1) on average.
The primary relationship managed in the application, the package ID to package details relationship, is made possible 
through the use of the hash table. When the application needs to update or query the details of a package, it uses the 
package ID to quickly and directly access the package's data. However it has some limitations. While it's great for 
direct and fast access, it's not designed to handle complex relationships between different packages, like ordering or 
hierarchical relationships. Also, in situations where hash collisions occur frequently, the lookup time can slow down, 
affecting the efficiency.

### Adaptability
The application is designed to adapt and scale to an increasing number of packages. The primary delivery algorithm is 
self-adjusting; it will handle any number of packages or trucks provided to it. Additionally, the hash-table data structure for package storage is also self-adjusting and will accommodate an increasing number of packages without changes to the code.

### Development Environment

This project was completed in the PyCharm IDE, using the latest version of python 3. No external libraries need to be installed.
This project was created on a 2021 16 inch MacBook Pro M1 Max running macOS Ventura 13.4

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