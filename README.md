# Maya-City-Builder-Project

This project aim to use procedural modelling generate a city in maya by python

---
#  INTRODUCTION
The program allows the user to select building setting(width,depth and gap), block setting(block number in x and z direction) and type of city to produce(square or circle) in an open window and allow user delete and reproduce it.

---
#  Alogrithm Design
**structure**

The structure of the program is simply use of counting loop and branching. The structure of the whole function goes from top , going through many selections and finally reach the ending result. Calling single functions several times in the main function helps reduce a lot repeating lines. To increase the variety of the city, I design 2 kind of block---the tall building block and low building block which randomly select by if branching. Each block holds 3 different kind of roof which is also randomly select by if branching. Besides that, I design two kind of city--- square and circle, calculate differently using the distance from the centre of the block to the original point. The calculation for the street and street light are not using the double counting loop but single one, for the There are hardly constant value for the program, mostly settings are value passed by user in the GUI, so the calculation for the counting loop is mostly represent by variables. 

**flow of control**

The program go through many selection. Firstly the city shape selection, then the tall and low building selection  and the roof selections. Each selections are separate from each others and create 6 kind of different branching of building type at last. And by different input values, the diversity of the city is increased.

---
# Innovation
I firstly done the square city for the program with inspiration from https://github.com/stevenquinn/CityGen/blob/master/cityGen.py . The placement and calculation of it is similar to the placement of building in the block but added street and street light. After that, I tried lots of different shapes of cities using drafts on paper.(triangles, diamonds and so on )and finally I develop the new shape version of circle. I doing so by using the symmetry of points on a circle and treat the grid as a huge 2d grid with block as point on it. 
 Also I try to change the calculations in the past functions and leave spaces for the street. By using the different height of street and block, I try to create a stage like road.

---
# Usage
1. install the citybuilder.py file into maya script editor, highlighting it and run the script. 
2. using the slider or type in the number in the block for all the settings.(The last 4 options works for the circle city ,and the 6–9setting works for the square city.) 

**Sliders and buttons**

Building depth:z direction length of single building

Building width:x direction length of single building 

Building x number: building number in one block in x direction 

Building z number: building number in one block in z direction

Building gap: building gap between single buildings 

Block x number: block number in x direction 

Block z number: block number in z direction 

street width: street width 

circle gap: the gap between circle 

city initial radius:the initial radius of the circle city(radius of the most inner circle) 

circle time: how many circles

circle divisions: number of division of 90 degree in the circle. 

circle or square selection: selection between two different kind of circle 

ok: generate the city using the value above 

delete: delete all the existing object

---
