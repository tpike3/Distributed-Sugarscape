# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:29:59 2019

@author: ymamo
"""

from NetScape import NetScape
import recorder
import pickle
import time






def step_finish(agent, pos, bus, buffer_pos):
        
            
        this_cell = agent.model.grid.get_cell_list_contents(pos)
        agent_on = False
        for i in this_cell: 
            if i.type == 'agent':
                agent_on = True
        
        if agent_on == True:
            agent.history.append(("step_finish_bus", agent.model.step_num))
            agent.model.grid.place_agent(agent, pos)
            boundary = agent.resolve_move()
            if boundary == 'boundary': 
                return
            agent.eat()
            agent.die()
            if agent.status == 'dead':
                return
            agent.trade()
            agent.debug += 1
            
        else:         
            agent.history.append(("step_finish_only", agent.model.step_num))
            agent.model.grid.place_agent(agent, pos)
            agent.eat()
            agent.die()
            if agent.status == 'dead':
                return
            agent.trade()
            agent.debug += 1




        
#############################################################################################
        
        
#data to save
survivors = []
step_time = []
price_df = {}
total_time = []



if __name__ == '__main__':
    for run in range(1):   
        print ("Run: " + str(run))
        start_run = time.time()
        #create an instance of the model
        test = NetScape(height = 50, width = 50, initial_population =200, regrow = 1,\
                        Moore = False)
        
       
        from distributedspace_mesa.space_distribute import Space_Distribute    
        #create an instance of the pool process, parameter to pass in is
        #the model object
        d_mesa = Space_Distribute(test, step_finish,\
                            split = 2)#, resolver = resolver) 
    
        #run the program, pass in the steps
        results = d_mesa.distro_geo(10)
                    
        #print (results[1].schedule.get_breed_count('agent'))
        df = results[1].datacollector.get_table_dataframe("Time") 
        price_df["Run"+str(run)] = results[1].price_record
        agents = recorder.survivors(results[1])
        survivors.append(agents)
        step_time.append(df["Time Per Step"].sum())
        run_time = time.time() - start_run
        total_time.append(run_time)
    

print (survivors)
print (total_time)
#pickle.dump(price_df, open("multi_total_price_2.p", "wb"))
#pickle.dump(survivors, open( "multi_sur_2.p", "wb" ))
#pickle.dump(step_time, open("multi_step_time_2.p", "wb")) 
#pickle.dump(total_time, open("multi_total_time_2.p", "wb")) 
