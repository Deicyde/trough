# Brownian motion

**Overview**

This part of the blueprint is a guide to the formalization of a standard Brownian motion in Lean using Mathlib. There are two main parts to this formalization:

- a development of the theory of Gaussian distributions, the construction of a projective family of Gaussian distributions and its projective limit by the Kolmogorov extension theorem,
- a proof of a Kolmogorov-Chentsov continuity theorem, following (kratschmer2023kolmogorov).

Putting the two sides together, we then build a stochastic process that fits the definition of a Brownian motion on the real line.

**Status** The formalization is complete.

**Blueprint authors** Rémy Degenne, Peter Pfaffelhuber.

**Formalization authors** Rémy Degenne, Markus Himmel, David Ledvinka, Etienne Marion, Peter Pfaffelhuber.

With additional contributions from Jonas Bayer, Lorenzo Loccioli, Pietro Monticone, Alessio Rondelli and Jérémy Scanvic.

- [Characteristic function and covariance](characteristic-function-and-covariance/README.md)
- [Stochastic processes](stochastic-processes/README.md)
- [Gaussian distributions](gaussian-distributions/README.md)
- [Projective family of the Brownian motion](projective-family-of-the-brownian-motion/README.md)
- [Kolmogorov-Chentsov Theorem](kolmogorov-chentsov-theorem/README.md)
- [Brownian motion](brownian-motion/README.md)
