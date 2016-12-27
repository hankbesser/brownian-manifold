
# brownian-manifold

The most basic algorithms for approximating Brownian motion entail realizations of the Wiener process (the name for the mathematical construct of the Brownian motion) on  n-dimensional Euclidian spaces that can scale to large n. However, the methods used to simulate a basic continuous-time Markov process on Euclidian space are not directly suited for simulations on more general Riemannian manifolds.

In the context of Brownian motion on special manifolds, Birkhoff's ergodic theorem tells us that: after a long time, the system no longer "remembers" its initial state and the probability of finding all initial points on the manifold are expected to be the same (i.e. uniformly distributed).

To introduce numerical methods used for understanding properties of Brownian motion on manifolds we have created ```brownian-manifold```: a collection of Python tools that make simulations and visualizations easy and reproducible.

Currently, ```brownian-manifold``` comes with two classes:
- ```Manifold``` helps you simulate Brownian motion on a 2-sphere or a finite cylinder. Also, helps you plot organized and visually informative manifolds/simulation data with many user-changeable parameters for each callable method.  
- ```Diffusion``` still in the works at present-time: uses the the ```Manifold``` objects in constructing Brownian motion as a diffusion process. The object used for the simulations/visualizations features two 2-spheres connected by a cylinder manifold with boundary.

![](https://github.com/hankbesser/brownian-manifold/blob/master/notebook_examples/figures/2sphere_manifold_4subp_400000.png)

### Notebooks

Checkout the notebooks for a guide on how to use browian-manifold and/or to the see implementation of the various methods;

#### How to use ```Manifold```?

go to:
- [manifold_example.ipynb](https://github.com/hankbesser/brownian-manifold/blob/master/notebook_examples/manifold_example.ipynb)

### Dependencies

The three dependencies needed for ```brownian-manifold``` are distributed with [Anaconda](https://www.continuum.io/downloads) and [Canopy](https://www.enthought.com/products/canopy/), but can also be installed through other means.
- ```NumPy``` >= 1.6.1
- ```SciPy``` >= 0.14
- ```Matplotlib``` >= 1.5

### Previous Work

For our initial motivations in creating ```brownian-manifold``` check out our [poster](http://mcl.math.uic.edu/wp-content/uploads/2016/08/F16-BMM-poster.pdf)   
- Gives a brief explanation Birkhoff's ergodic theorem in relation to Brownian motion on manifolds and also our algorithmic approaches. Many of approaches have changed and can be inspected in ```brownian-manifold``` modules themselves.

To view some interactive plots check out of [plot.ly page](https://plot.ly/~besser2/) (just click out the blue box when asked to login)
- Some nice looking Brownian motion on 2-sphere plots that were used for initial presentations and poster. For ```brownian-manifold``` only ```matplotlib``` was used. The powers of ```matplotlib``` made local plotting of large data sets easy and effective.
- If you interested in how these ```plot.ly```  plots were contructed let us know.  

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
