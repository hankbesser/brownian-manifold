
# brownian-manifold

The most basic algorithms for approximating Brownian motion entail realizations of the Wiener process (the name for the mathematical construct of the Brownian motion) on n-dimensional Euclidean spaces that can scale to large n. However, the methods used to simulate the basic continuous-time stochastic process on a Euclidean space are not directly suited for simulations on a more general Riemannian manifold.

In the context of Brownian motion on special manifolds: given a sequence of random trajectories on the manifold, the current state of the Brownian path captures relevant historical information, but, once known, is *independent* of the past (i.e. a Markov process, where the current state characterizes the process). Also, Birkhoff's ergodic theorem tells us that after a sufficient amount of time, the system evolves to where it has no memory of its initial state. The Brownian motion visits *all* parts of the manifold *without any* systematic period.  Thus, the time-*average* of the Brownian motion’s trajectory equals the space-*average* almost everywhere (i.e. Ergodic) and the probability of finding all initial points on the manifold are expected to be the same on the unit interval (i.e. uniform coverage on the manifold).

To introduce numerical methods used for understanding properties of Brownian motion on manifolds we have created ```brownian-manifold```: a collection of Python tools that make simulations and visualizations easy and reproducible.

Currently, ```brownian-manifold``` comes with two classes:
- ```Manifold``` helps you simulate Brownian motion on a 2-sphere or a finite cylinder. Also, helps you plot organized and visually informative manifolds/simulation data with many user-changeable parameters for each callable method.  
- ```Diffusion``` still in the works at present-time: uses the ```Manifold``` objects in generating Brownian motion as a diffusion process--a Markov process with continuous sample paths. The object used for this representation features a compact manifold with two 2-spheres connected by a cylinder manifold with boundary.

![](https://github.com/hankbesser/brownian-manifold/blob/master/poster_and_figures/2_sphere_400000.png)

### Notebooks

Checkout the notebooks for a guide on how to use brownian-manifold and/or to the see implementation of the various methods;

#### How to use ```Manifold```?

go to:
- [manifold_example.ipynb](https://github.com/hankbesser/brownian-manifold/blob/master/notebook_examples/manifold_example.ipynb)

### Dependencies

The three dependencies needed for ```brownian-manifold``` are distributed with [Anaconda](https://www.continuum.io/downloads) and [Canopy](https://www.enthought.com/products/canopy/), but can also be installed through other means.
- ```NumPy``` >= 1.6.1
- ```SciPy``` >= 0.14
- ```Matplotlib``` >= 1.5
- ```Pandas``` (optional)

### Posters and more visuals

* For the updated poster [click here](https://github.com/hankbesser/brownian-manifold/blob/master/poster_and_figures/new_poster_hank.pdf)

* For our initial motivations in creating ```brownian-manifold``` check out our [poster](http://mcl.math.uic.edu/wp-content/uploads/2016/08/F16-BMM-poster.pdf)   

* To view some interactive plots check out of [plot.ly page](https://plot.ly/~besser2/) (just click out the blue box when asked to login)
  - If you interested in how these ```plot.ly```  plots were constructed let us know.  

Details of the code can be inspected in the comments of the ```brownian-manifold``` modules.

### Installation

You can Clone the repository.

```bash
$ git clone https://github.com/hankbesser/brownian-manifold
```

### Authors

* [Henry (Hank) Besser](https://github.com/hankbesser)
* Branden Carrier


### Acknowledgments
* [UIC Mathematical Computing Laboratory (MCL)](http://mcl.math.uic.edu/fall-2016-projects/)
* [Cheng Ouyang](http://homepages.math.uic.edu/~couyang/)
* [Alexander Cameron](http://homepages.math.uic.edu/~acamer4/teaching.html)
