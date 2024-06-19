#define neural network in this file

#could make neural networks depending on positions,
#or i can base my neural network off every feature this way
#there would be an evenly ranked output

#input: data after preprocessing (columns, target%)

#output: unique values  
#
#or if i implement the other way, based off position
#it would output unique values based off the number of wrs
#in the league

#based off position

#will have to create classes based off of positional
#characteristics and will get ranks based off of the number
#of positions in a class instead of based on the whole
#data

#based off fantasy value

#would have to prerank players by fantasy value from last
#year (points scored) so that when they go into the nn
#the output is remembered since it has to be put back into
#the network (convolutional idrk) because the positions(WR1)
#will gain weights attached to them to give an accurate 
#output based off of other outputs (actually would it have
#to have the weights put back in since its trained on
#previous years stats and fantasy values)