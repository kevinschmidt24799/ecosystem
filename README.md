# Ecosystem
## Overview
My goal going into this project was to create a simple game to train a neural network to play. I ended up creating a simple ecosystem consisting of some three different types of creatures (red, green, blue) which counter each other in a rock-paper-scissors cycle. When a creature contacts a member of its prey species, it will convert it to the same type as itself. 

To get some idea of how the game would work, I ran various games with creatures moving randomly, then with various simple strategies. Experimenting with different strategies, starting distributions, density, and grid sizes, I found there were 3 broad outcomes that could occur. 

The balanced distribution would occur in almost every case. Whenever any species became too populous, its predator would then easily grow, and so on. With various mirrored strategies I would sometimes find the creatures would settle into some arrangement they were all satisfied with, remaining in a static state seemingly forever. 

The most surprising result though, was that when a strategy was too "smart", paired against randomness, it would almost always create an unstable state. Surprisingly though, it was consistently not one that it won. It would quickly hunt its prey to extinction, and then with just it, and its predator remaining, slowly die out. This gave me apprehensions about what it looked like to properly play the game, as being too efficient of a predator would most often lose you the game. 

#### Balanced distribution (almost all cases)

<img src="Demo%20Images/Balanced%20Distribution.png" alt="drawing" width="500"/>

#### Static state in which all species prefer inactivity

<img src="Demo%20Images/Static%20Stable%20Distribution.png" alt="drawing" width="500"/>

#### Unstable state wherein yellow was "too predatory"

<img src="Demo%20Images/Unstable%20Distribution.png" alt="drawing" width="500"/>

## Machine Learning Approach with TensorFlow
My initial desire was to have different neural nets play complete games against random or semi-intelligent opponents to train. I was interested in learning to use Keras dataframes which are insistent on having both input data and labels (which tell what it expects of the data). I briefly contemplated a hacky solution in which I feed in dummy data for labels, and then use a custom evaluation function that ran the trial using the current iteration of a model, returning a loss based on performance and ignoring the labels. However, in the spirit of learning Keras properly, I decided otherwise. 

I ended thinking of a reasonably clean solution: running 100 random games, for each move, recording the creature's field of vision, decided move, and whether that creature won or lost. Then, treating the FoV as data, and the move, as well as result as labels, I trained the network. With only 100 games of random moves as training data, I was more than doubtful of the strength of the model. After all, the correlation between any single move with winning or losing is strenuously small. Shockingly though, the neural net ended up significantly outperforming random and simple creatures, winning virtually every game. The neural net plays strangely, with no discernible strategy. Seemingly by magic though, its predator will suddenly die out. 


<img src="Demo%20Images/Neural%20Net%20Strategy.png" alt="drawing" width="500"/>

This image is of a game in which the neural net (red) has effectively won, because it beats the only remaining creatures (green). As you can see, it forms a bizarre formation, and will slowly and patiently finish off the green. A video of how the neural net plays is uploaded at: https://youtu.be/PNqL7vxpSmE
