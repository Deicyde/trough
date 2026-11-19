# Testing, Estimation, Risk

In the estimation problem, we are given a family of measures and we want to estimate an unknown parameter for the measure from which we observe samples. Let $\mathcal X$ be the measurable space on which the measures are defined. The measure family is described by a kernel $P : \Theta \rightsquigarrow \mathcal X$. We write $P_\theta$ for $P(\theta)$. In *parametric* problems, $\Theta$ is a low-dimensional space. In *nonparametric* problems $\Theta$ is large, for example $\Theta = \mathcal M (\mathcal X)$ or $\Theta = \mathcal P(\mathcal X)$.

The goal of the estimation task is to find, given the observation of samples of $P_\theta$ for an unknown $\theta$, the value of a function $y : \Theta \to \mathcal Y$ , which maps the parameter $\theta$ to the quantity we are interested in. For example, $y(\theta)$ might be the expected value of the distribution $P_\theta$.

An estimator is a Markov kernel $\hat{y} : \mathcal X \rightsquigarrow \mathcal Z$, where most often $\mathcal Z = \mathcal Y$. Note that, while $y$ is a function of a parameter in $\Theta$, $\hat{y}$ has domain $\mathcal X$ as the estimation is done based on a sample of the measure, while the measure itself and its parameter remain unknown. In general this is a randomized estimator, but often deterministic estimators (corresponding to deterministic kernels) are enough to attain optimal performance. The quality of the estimation is quantified by a loss $\ell' : \mathcal Y \times \mathcal Z \to \mathbb{R}_{+, \infty}$. We write $\ell$ for a loss on $\mathcal Y \times \mathcal Y$ and $\ell'$ in the heterogeneous case.

In short, an estimation problem is specified by the data $(P, y, \ell')$.

Example: simple binary hypothesis testing (SBHT)

We say that an estimation problem is a testing problem if $\mathcal Y = \mathcal Z$ is discrete and the loss takes values in $\{0, 1\}$. A test is said to be binary if $\mathcal Y$ has two elements. A test is simple if $\{\theta \mid y(\theta) = y_0\}$ is a singleton for all $y_0 \in \mathcal Y$, i.e. $y$ is bijective.

In summary, in simple binary hypothesis testing, $\Theta = \mathcal Y = \mathcal Z = \{0,1\}$, $y(0) = 0$, $y(1) = 1$ (that is, $y$ is the identity). For $y_0, z \in \{0,1\}$, $\ell(y_0, z) = \mathbb{I}\{y_0 \ne z\}$.

- [Risk](risk/README.md)
- [Simple binary hypothesis testing](simple-binary-hypothesis-testing/README.md)
- [Reduction to testing](reduction-to-testing/README.md)
