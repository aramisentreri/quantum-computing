# Quantum Computing 
This repo is meant to create a simple quantum computer simulator based on classical implementations of a few bits and 
Quantum gates.

Ideally some simple algorithms can be implemented in this simulation, and then confirmed in actual quantum computers by 
using for example the API of IBM's qiskit (or any other available cloud service).  

## Usage
Right now you can just run 
```python qbit.py```
and it will run 1000 measurements of a randomly generated qbit and print out the probability of finding the qbit in 
state |0>

## Qbit class 
You can initialize a Qbit by calling from the Qbit class
```
from qbit import Qbit

# specify state coefficients x, y in the standard 
# basis |0>, |1>:  state = x|0> + y|1>
qbit_0 = Qbit(state = np.array([x,y]))

# or initialize it in random state
qbit_1 = Qbit()
```
To measure the qbit, simply use the ```measure()``` method:
``` 
qbit_0.measure()
```
The outcome of the measurement will be |0> with probability |x|^2, or 
|1> with probability $|y|^2$, and the qbit state will now be the new state.