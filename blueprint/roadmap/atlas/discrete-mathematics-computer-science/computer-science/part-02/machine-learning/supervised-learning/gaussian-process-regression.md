---
declaration: section
origin: cited
lean: Cslib.MachineLearning.GaussianProcessRegression.kernelMatrix, Cslib.MachineLearning.GaussianProcessRegression.jointCov, Cslib.MachineLearning.GaussianProcessRegression.testPart, Cslib.MachineLearning.GaussianProcessRegression.targetPart, Cslib.MachineLearning.GaussianProcessRegression.isUnit_det_kernelMatrix_add, Cslib.MachineLearning.GaussianProcessRegression.jointCov_eq_add, Cslib.MachineLearning.GaussianProcessRegression.jointCov_posSemidef, Cslib.MachineLearning.GaussianProcessRegression.kernelMatrix_posSemidef_train
statement: formalized
proof: formalized
---

# Gaussian process regression

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/gaussian-process-regression/index.html).

## Kernel matrix

For a kernel $k : X \times X \to \mathbb{R}$ and two families of inputs
$a = (a_i)_{i \in \alpha}$ and $b = (b_j)_{j \in \beta}$ in $X$, the kernel (Gram) matrix
$K(a, b)$ is the $\alpha \times \beta$ real matrix with entries $K(a, b)_{ij} = k(a_i, b_j)$.

Formalized by `Cslib.MachineLearning.GaussianProcessRegression.kernelMatrix`, a definition declared in [CSLibExt/MachineLearning/GaussianProcessRegression.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GaussianProcessRegression.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/gaussian-process-regression/index.html#kernel-matrix).

## Joint prior covariance in Gaussian-process regression

The joint prior covariance of the test values `f(x*)` and the noisy training targets
`y = f(x) + ε`, `ε ~ N(0, σ² I)`: `[[K(x*, x*), K(x*, x)], [K(x, x*), K(x, x) + σ² I]]`.

Formalized by `Cslib.MachineLearning.GaussianProcessRegression.jointCov`, a definition declared in [CSLibExt/MachineLearning/GaussianProcessRegression.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GaussianProcessRegression.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/gaussian-process-regression/index.html#joint-cov).

## Test-value projection

For finite index sets $\tau$ (test inputs) and $\nu$ (training
inputs), the test-value projection is the $\tau \times (\tau \sqcup \nu)$ real matrix with the
identity matrix on the columns indexed by $\tau$ and a zero block on the columns indexed by $\nu$.
It sends a joint vector $(u, y)$ with $u \in \mathbb{R}^{\tau}$ and $y \in \mathbb{R}^{\nu}$ to its
block of test values $u$.

Formalized by `Cslib.MachineLearning.GaussianProcessRegression.testPart`, a definition declared in [CSLibExt/MachineLearning/GaussianProcessRegression.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GaussianProcessRegression.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/gaussian-process-regression/index.html#test-part).

## Training-target projection

For finite index sets $\tau$ (test inputs) and $\nu$
(training inputs), the training-target projection is the $\nu \times (\tau \sqcup \nu)$ real
matrix with a zero block on the columns indexed by $\tau$ and the identity matrix on the columns
indexed by $\nu$. It sends a joint vector $(u, y)$ with $u \in \mathbb{R}^{\tau}$ and
$y \in \mathbb{R}^{\nu}$ to its block of training targets $y$.

Formalized by `Cslib.MachineLearning.GaussianProcessRegression.targetPart`, a definition declared in [CSLibExt/MachineLearning/GaussianProcessRegression.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GaussianProcessRegression.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/gaussian-process-regression/index.html#target-part).

## Regularized kernel matrices are invertible

Let $k : X \times X \to \mathbb{R}$ be a kernel
and $x = (x_j)_{j \in \nu}$ a finite family of inputs whose kernel matrix
$K = (k(x_i, x_j))_{i, j \in \nu}$ is positive semidefinite. Then for every $\sigma^2 > 0$ the
matrix $K + \sigma^2 I$ has nonzero determinant, so it is invertible.

Formalized by `Cslib.MachineLearning.GaussianProcessRegression.isUnit_det_kernelMatrix_add`, a theorem declared in [CSLibExt/MachineLearning/GaussianProcessRegression.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GaussianProcessRegression.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/gaussian-process-regression/index.html#is-unit-det-kernel-matrix-add).

## The joint covariance as a kernel matrix plus noise

For a kernel
$k : X \times X \to \mathbb{R}$, a real number $\sigma^2$, test inputs $x^* = (x^*_i)_{i \in \tau}$
and training inputs $x = (x_j)_{j \in \nu}$, the joint covariance of $k$, $\sigma^2$, $x^*$ and $x$
equals $K + D$, where $K$ is the kernel matrix of the combined family $(x^*, x)$ indexed by
$\tau \sqcup \nu$ and $D$ is the diagonal matrix with entry $0$ at each test index and $\sigma^2$
at each training index.

Formalized by `Cslib.MachineLearning.GaussianProcessRegression.jointCov_eq_add`, a theorem declared in [CSLibExt/MachineLearning/GaussianProcessRegression.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GaussianProcessRegression.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/gaussian-process-regression/index.html#joint-cov-eq-add).

## The joint covariance is positive semidefinite

Let $k : X \times X \to \mathbb{R}$ be a
kernel, let $x^* = (x^*_i)_{i \in \tau}$ and $x = (x_j)_{j \in \nu}$ be families of test and
training inputs, and let $\sigma^2 \ge 0$. If the kernel matrix of the combined family $(x^*, x)$,
indexed by $\tau \sqcup \nu$, is positive semidefinite, then the joint covariance of $k$,
$\sigma^2$, $x^*$ and $x$ is positive semidefinite.

Formalized by `Cslib.MachineLearning.GaussianProcessRegression.jointCov_posSemidef`, a theorem declared in [CSLibExt/MachineLearning/GaussianProcessRegression.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GaussianProcessRegression.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/gaussian-process-regression/index.html#joint-cov-pos-semidef).

## Training blocks of positive semidefinite kernel matrices

Let
$k : X \times X \to \mathbb{R}$ be a kernel and let $x^* = (x^*_i)_{i \in \tau}$ and
$x = (x_j)_{j \in \nu}$ be families of inputs. If the kernel matrix of the combined family
$(x^*, x)$, indexed by $\tau \sqcup \nu$, is positive semidefinite, then so is the kernel matrix
$(k(x_i, x_j))_{i, j \in \nu}$ of $x$.

Formalized by `Cslib.MachineLearning.GaussianProcessRegression.kernelMatrix_posSemidef_train`, a theorem declared in [CSLibExt/MachineLearning/GaussianProcessRegression.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GaussianProcessRegression.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/gaussian-process-regression/index.html#kernel-matrix-pos-semidef-train).

## The Gaussian-process posterior

Let $k : X \times X \to \mathbb{R}$ be a kernel, let
$x^* = (x^*_i)_{i \in \tau}$ (test inputs) and $x = (x_j)_{j \in \nu}$ (training inputs) be
finite families in $X$, and write $K(a, b)$ for the kernel matrix $(k(a_i, b_j))_{i, j}$. Assume
that the kernel matrix of the combined family $(x^*, x)$, indexed by $\tau \sqcup \nu$, is
positive semidefinite, and let $\sigma^2 > 0$. Let $V$ be a measurable random vector in
$\mathbb{R}^{\tau \sqcup \nu}$ on a probability space whose law is the Gaussian $N(0, \Sigma)$,
where $\Sigma$ is the joint covariance of $k$, $\sigma^2$, $x^*$ and $x$, and let $F$ (the test
values) and $Y$ (the training targets), random vectors in $\mathbb{R}^{\tau}$ and
$\mathbb{R}^{\nu}$, be the test and training blocks of $V$. Then for almost every $y$ with respect
to the law of $Y$, the conditional distribution of $F$ given $Y = y$ is the Gaussian with mean
$K(x^*, x) (K(x, x) + \sigma^2 I)^{-1} y$ and covariance
$K(x^*, x^*) - K(x^*, x) (K(x, x) + \sigma^2 I)^{-1} K(x, x^*)$.

Formalized by `Cslib.MachineLearning.GaussianProcessRegression.condDistrib_test_given_targets`, a theorem declared in [CSLibExt/MachineLearning/GaussianProcessRegression.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GaussianProcessRegression.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/gaussian-process-regression/index.html#cond-distrib-test-given-targets).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gaussian process regression](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/gaussian-process-regression/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/machine-learning/supervised-learning/gaussian-process-regression)
