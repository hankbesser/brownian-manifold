
# brownian-manifold

The most basic algorithms for approximating Brownian motion entail realizations of the Wiener process (the name for the mathematical construct of the Brownian motion) on  n-dimensional Euclidian spaces that can scale to large n. However, the methods used to simulate the most basic continuous time Markov process on Euclidian space are not directly suited for simulations on more general Riemannian manifolds.

Why is it important to explore Brownian motion on Riemannian manifolds?

Well, in terms of stochastic analysis to explore the probabilistic formulations of ergodic theory, the applications are plentiful. In particular, in the context of Brownian motion on a compact manifold, Birkhoff's ergodic theorem tells us that: for any for any real-valued measurable function $f$ and measure-preserving map
$\mathcal{M} \rightarrow \mathbb{R}$
, after a sufficient amount, the time average of $f$ along the trajectories is related to the space average. Therefore, after a long time, the system no longer "remembers" its initial state and the probability of finding all initial points for the Brownian path on the manifold is the same.

Some other application of ergodic theory are related to Markov chains, entropy of dynamical systems, and information theory.  


To improve upon the numerical methods for examining Birkhoff's ergodic theorem we have created ```brownian-manifold```: a collection of Python tools to make simulations and visualizations of Brownian motion on manifolds easy and reproducible.

Currently, ```brownian-manifold``` comes with two classes:
- ```Manifold``` helps you simulate brownian motion on a 2-sphere or a finite cylinder. Also, helps you plot organized and visually informative manifolds/simulation data with many user-changeable parameters for each callable method.  
- ```Diffusion``` still in the works at the present-time: uses the the ```Manifold``` objects in constructing Brownian motion as a diffusion process. The object used for the simulations/visualizations features two 2-spheres connected by a cylinder manifold with boundary.

```brownian-manifold``` provides efficient and convenient methods to gather the data and examine ergodicity properties on special systems.

![](https://github.com/hankbesser/brownian-manifold/blob/master/notebook_examples/figures/2sphere_manifold_4subp_400000.png)

### Notebooks
Checkout the notebooks for a guide on how to use browian-manifold and/or to the see implementation of the various methods;

#### How to use ```Manifold```?

go to:

- [manifold_example.ipynb](https://github.com/hankbesser/brownian-manifold/blob/master/notebook_examples/manifold_example.ipynb)
### Installation


The three dependencies needed for ```brownian-manifold``` are distributed with [Anaconda](https://www.continuum.io/downloads) and [Canopy](https://www.enthought.com/products/canopy/), but can also be installed through other means.
- ```NumPy``` >= 1.6.1
- ```SciPy``` >= 0.14
- ```Matplotlib``` >= 1.5

### Previous Work

For our initial motivations in creating ```brownian-manifold``` check out our [poster](http://mcl.math.uic.edu/wp-content/uploads/2016/08/F16-BMM-poster.pdf)   
- gives a brief explanation Birkhoff's ergodic theorem in relation to Brownian motion on manifolds and also our algorithmic approaches. Many of approaches have changed and can be inspected in ```brownian-manifold``` itself.

To view some interactive plots check out of [plot.ly page](https://plot.ly/~besser2/) (just click out the blue box when asked to login)
- some nice looking Brownian motion on 2-sphere plots that were used for initial presentations and poster. However, using ```Matplotlib``` for ```brownian-manifold``` provided much of the same visualization tools, although the user-interface camera functions are not as sophisticated as ```plot.ly```'s. Using the powers of  ```Matplotlib```  made plotting large amounts of data easy and run locally. If you interested in how these ```plot.ly```  plots were contructed let us know.  

### Installation

You can Clone the repository.

```bash
$ git clone https://github.com/hankbesser/brownian-manifold
```

### Authors

* [Henry (Hank) Besser](https://github.com/hankbesser)
* Branden Carrier


### Acknowledgments
* [UIC Mathematical Computing Laboratory (MCL)](http://mcl.math.uic.edu/fall-2016-projects/): funding and support
* [Cheng Ouyang](http://homepages.math.uic.edu/~couyang/)
* [Alexander Cameron](http://homepages.math.uic.edu/~acamer4/teaching.html)
