
# Distributed Sugarscape


This is the developmental model for Disitrbuted Space Mesa. 

Distributed Sugarscape requires

    Mesa>=0.8.4
    Distributedspace_mesa == 0.0.1
    NetworkX>=2.2
    Pathos>=0.2.3 

 The main run files are (in either the verifcation or Exploration/Size Explore folders):

 	1. Run the test module -- run_distro_test.py
 	2. Run the distro module -- run_distro.py
 	3. Run the sequential module -- run.py


 At this time DS Mesa is only able to porvide modest improvements. The below graphs show improvements over tun time and breaks down the magement cost and the step costfor models run on two processors and models run on four processors. 

 ![Run time: agent population by run time](https://github.com/tpike3/Distributed-Sugarscape/blob/master/pictures/overhead%20and%20per%20step.png)


 ![Breakdown: Break down of step time and management time](https://github.com/tpike3/Distributed-Sugarscape/blob/master/pictures/size%20and%20run%20time.png)
