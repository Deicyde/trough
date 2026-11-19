# Projective family of Gaussian measures

We build a projective family of Gaussian measures indexed by $\mathbb{R}_+$. In order to do so, we need to define specific Gaussian measures on finite index sets $\{t_1, \ldots, t_n\}$. We want to build a multivariate Gaussian measure on $\mathbb{R}^n$ with mean $0$ and covariance matrix $C_{ij} = \min(t_i, t_j)$ for $1 \leq i,j \leq n$.

We prove that the matrix $C_{ij} = \min(t_i, t_j)$ is positive semidefinite, which means that there exists a Gaussian distribution with mean 0 and covariance matrix $C$.

- [Gram matrix](def-grammatrix.md)
- [posSemidef_gramMatrix](lem-possemidef-grammatrix.md)
- [posSemidef_brownianCov](lem-possemidef-browniancov.md)

Definition of the projective family and extension

- [Projective family of the Brownian motion](def-gaussianprojectivefamily.md)
- [isProjectiveMeasureFamily_gaussianProjectiveFamily](lem-isprojectivemeasurefamily-gaussianprojective.md)
- [gaussianLimit](def-gaussianlimit.md)
