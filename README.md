# Smartail-Internship-task

For a time complexity of O(nlogn), Only divide and conquer approach can be used for building a closest pair algorithm.
The process that was followed included the following steps:
1. First of all 100 random X and Y coordinates were taken as input and stored depending on a class structure Point
2. Then these points are sorted based on either their x coordinates and their y coordinates (Any sort function can be employed)
3. After sorting, in this case, y coordinate is taken for determining the distances within each point by first assigning the mid value among the y coordinates as the midpoint
4. Each and every points in those sections are further divided recursively and the distances are calculated by defining a distance function and assigning the minimum distance to d.
5. After the points in both of the sections are covered, the points in a strip closer to the midpoint and within a minimum distance d are taken and distances are calculated for them also recursively
6. The smallest distance among the distance d and the distance of the points in the strip is the closest pair distance within a pair of points 
