---
declaration: section
origin: cited
lean: Cslib.MachineLearning.LeastSquares.rss, Cslib.MachineLearning.LeastSquares.rss_add, Cslib.MachineLearning.LeastSquares.rss_eq_of_normal, Cslib.MachineLearning.LeastSquares.rss_le_iff_normal, Cslib.MachineLearning.LeastSquares.exists_normal, Cslib.MachineLearning.LeastSquares.normal_inv, Cslib.MachineLearning.LeastSquares.convexOn_rss, Cslib.MachineLearning.LeastSquares.gaussLikelihood
statement: formalized
proof: formalized
---

# Least squares, ridge and lasso regression

29 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html).

## Residual sum of squares

For a real design matrix $X$ with $m$ rows and columns indexed
by a finite type $\iota$, responses $y \in \mathbb{R}^m$ and $\theta \in \mathbb{R}^\iota$, the
residual sum of squares is
$S(\theta) = (y - X\theta) \cdot (y - X\theta) = \sum_{k=1}^{m} (y_k - (X\theta)_k)^2$.

Formalized by `Cslib.MachineLearning.LeastSquares.rss`, a definition declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#rss).

## Expansion of the residual sum of squares

Let $X$ be a real design matrix with $m$ rows
and columns indexed by a finite type $\iota$, let $y \in \mathbb{R}^m$, and write
$S(\theta) = (y - X\theta) \cdot (y - X\theta)$ for the residual sum of squares. Then for all
$\theta, v \in \mathbb{R}^\iota$,

$$S(\theta + v) = S(\theta) - 2\, v \cdot \bigl(X^\top (y - X\theta)\bigr) + (Xv) \cdot (Xv).$$

Formalized by `Cslib.MachineLearning.LeastSquares.rss_add`, a theorem declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#rss-add).

## Pythagoras for least squares

Let $X$ be a real design matrix with $m$ rows and columns
indexed by a finite type $\iota$, let $y \in \mathbb{R}^m$, write $S$ for the residual sum of
squares, and let $\theta_0 \in \mathbb{R}^\iota$ solve the normal equations
$X^\top X \theta_0 = X^\top y$. Then for every $\theta \in \mathbb{R}^\iota$,

$$S(\theta) = S(\theta_0) + (X(\theta - \theta_0)) \cdot (X(\theta - \theta_0)).$$

Formalized by `Cslib.MachineLearning.LeastSquares.rss_eq_of_normal`, a theorem declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#rss-eq-of-normal).

## Least squares and the normal equations

Let $X$ be a real design matrix with $m$ rows and
columns indexed by a finite type $\iota$, let $y \in \mathbb{R}^m$, and write $S$ for the residual
sum of squares. A vector $\theta_0 \in \mathbb{R}^\iota$ satisfies $S(\theta_0) \le S(\theta)$ for
every $\theta \in \mathbb{R}^\iota$ if and only if $X^\top X \theta_0 = X^\top y$.

Formalized by `Cslib.MachineLearning.LeastSquares.rss_le_iff_normal`, a theorem declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#rss-le-iff-normal).

## Least-squares estimates exist

Let $X$ be a real matrix with $m$ rows and columns indexed
by a finite set $\iota$, and let $y \in \mathbb{R}^m$. Then there is $\theta \in \mathbb{R}^\iota$
with $X^\top X \theta = X^\top y$: the normal equations always have a solution, whatever the rank
of $X$.

The reason is that the range of $X^\top X$ is contained in that of $X^\top$ and the two matrices
have the same rank, so their ranges coincide.

Formalized by `Cslib.MachineLearning.LeastSquares.exists_normal`, a theorem declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#exists-normal).

## Closed-form solution of the normal equations

Let $X$ be a real matrix with $m$ rows and
columns indexed by a finite set $\iota$ such that $X^\top X$ is invertible, and let
$y \in \mathbb{R}^m$. Then $\hat\theta = (X^\top X)^{-1} X^\top y$ solves the normal equations
$X^\top X \hat\theta = X^\top y$.

Formalized by `Cslib.MachineLearning.LeastSquares.normal_inv`, a theorem declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#normal-inv).

## Convexity of the residual sum of squares

Let $X$ be a real matrix with $m$ rows and
columns indexed by a finite set $\iota$, and let $y \in \mathbb{R}^m$. Then the residual sum of
squares $\theta \mapsto \sum_k (y_k - (X\theta)_k)^2$ is a convex function on all of
$\mathbb{R}^\iota$.

Formalized by `Cslib.MachineLearning.LeastSquares.convexOn_rss`, a theorem declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#convex-on-rss).

## Gaussian likelihood of linear regression

Let $X$ be a real matrix with $m$ rows and
columns indexed by a finite set $\iota$, let $y \in \mathbb{R}^m$ and let $v \ge 0$. The Gaussian
likelihood with noise variance $v$ is the function of $\theta \in \mathbb{R}^\iota$ given by

$$
L(\theta) = \prod_{k=1}^{m} \frac{1}{\sqrt{2 \pi v}}
\exp\left(-\frac{(y_k - (X\theta)_k)^2}{2 v}\right).
$$

This is the likelihood of $y$ when $y_k = (X\theta)_k + \varepsilon_k$ with independent
$\varepsilon_k \sim N(0, v)$.

For $v = 0$ each factor is the zero function (with the convention $1/0 = 0$), not a Dirac kernel;
the results about this likelihood assume $v \neq 0$.

Formalized by `Cslib.MachineLearning.LeastSquares.gaussLikelihood`, a definition declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#gauss-likelihood).

## The Gaussian likelihood decreases with the residual sum of squares

Let $X$ be a real
matrix with $m$ rows and columns indexed by a finite set $\iota$, let $y \in \mathbb{R}^m$ and
$v > 0$, let $L$ be the Gaussian likelihood of linear regression with noise variance $v$, and let
$\mathrm{RSS}(\theta) = \sum_k (y_k - (X\theta)_k)^2$ be the residual sum of squares. Then for all
$\theta, \theta' \in \mathbb{R}^\iota$, $L(\theta) \le L(\theta')$ if and only if
$\mathrm{RSS}(\theta') \le \mathrm{RSS}(\theta)$.

Formalized by `Cslib.MachineLearning.LeastSquares.gaussLikelihood_le_iff`, a theorem declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#gauss-likelihood-le-iff).

## Least squares is maximum likelihood

Let $X$ be a real matrix with $m$ rows and columns
indexed by a finite set $\iota$, let $y \in \mathbb{R}^m$ and $v > 0$, and let $L$ be the Gaussian
likelihood of linear regression with noise variance $v$. Then $\theta_0 \in \mathbb{R}^\iota$
maximizes $L$ over $\mathbb{R}^\iota$ if and only if it solves the normal equations
$X^\top X \theta_0 = X^\top y$.

Formalized by `Cslib.MachineLearning.LeastSquares.isMaxOn_gaussLikelihood_iff`, a theorem declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#is-max-on-gauss-likelihood-iff).

## Existence of the Gaussian maximum likelihood estimate

Let $X$ be a real matrix with $m$
rows and columns indexed by a finite set $\iota$, let $y \in \mathbb{R}^m$ and $v > 0$, and let $L$
be the Gaussian likelihood of linear regression with noise variance $v$. Then $L$ attains its
maximum on $\mathbb{R}^\iota$: there is $\theta_0 \in \mathbb{R}^\iota$ with
$L(\theta) \le L(\theta_0)$ for every $\theta \in \mathbb{R}^\iota$.

Formalized by `Cslib.MachineLearning.LeastSquares.exists_isMaxOn_gaussLikelihood`, a theorem declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#exists-is-max-on-gauss-likelihood).

## Ridge objective

For a real design matrix $X$ with $m$ rows and columns indexed by a
finite type $\iota$, responses $y \in \mathbb{R}^m$, a real number $\lambda$ and
$\theta \in \mathbb{R}^\iota$, let $S(\theta) = \sum_{k=1}^{m} (y_k - (X\theta)_k)^2$ be the
residual sum of squares. The ridge objective is $S(\theta) + \lambda \sum_{i} \theta_i^2$.

Formalized by `Cslib.MachineLearning.LeastSquares.ridge`, a definition declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#ridge).

## Expansion of the ridge objective around a solution of its normal equations

Let $X$ be a
real matrix with $m$ rows and columns indexed by a finite set $\iota$, let $y \in \mathbb{R}^m$
and $\lambda \in \mathbb{R}$, and write $\|\cdot\|$ for the Euclidean norm and
$R(\theta) = \|y - X\theta\|^2 + \lambda \|\theta\|^2$ for the ridge objective. If
$\theta_0 \in \mathbb{R}^\iota$ satisfies $(X^\top X + \lambda I)\theta_0 = X^\top y$, then for
every $\theta \in \mathbb{R}^\iota$,
$R(\theta) = R(\theta_0) + \|X(\theta - \theta_0)\|^2 + \lambda \|\theta - \theta_0\|^2$.

Formalized by `Cslib.MachineLearning.LeastSquares.ridge_eq_of_normal`, a theorem declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#ridge-eq-of-normal).

## Solutions of the ridge normal equations minimize the ridge objective

Let $X$ be a real
matrix with $m$ rows and columns indexed by a finite set $\iota$, let $y \in \mathbb{R}^m$ and
$\lambda \ge 0$, and write $\|\cdot\|$ for the Euclidean norm. If $\theta_0 \in \mathbb{R}^\iota$
satisfies $(X^\top X + \lambda I)\theta_0 = X^\top y$, then for every $\theta \in \mathbb{R}^\iota$,
$\|y - X\theta_0\|^2 + \lambda \|\theta_0\|^2 \le \|y - X\theta\|^2 + \lambda \|\theta\|^2$.

Formalized by `Cslib.MachineLearning.LeastSquares.ridge_le_of_normal`, a theorem declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#ridge-le-of-normal).

## The ridge matrix is positive definite

For every real matrix $X$ with $m$ rows and columns
indexed by a finite set $\iota$ and every real $\lambda > 0$, the matrix $X^\top X + \lambda I$ is
positive definite.

Formalized by `Cslib.MachineLearning.LeastSquares.posDef_ridge`, a theorem declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#pos-def-ridge).

## Ridge estimate

For a real matrix $X$ with $m$ rows and columns indexed by a finite set
$\iota$, responses $y \in \mathbb{R}^m$ and a real number $\lambda$, the ridge estimate is
$(X^\top X + \lambda I)^{-1} X^\top y \in \mathbb{R}^\iota$.

The inverse of a singular matrix is taken to be $0$; for $\lambda > 0$ the matrix
$X^\top X + \lambda I$ is always invertible.

Formalized by `Cslib.MachineLearning.LeastSquares.ridgeEstimate`, a definition declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#ridge-estimate).

## Closed form of ridge regression

Let $X$ be a real matrix with $m$ rows and columns indexed
by a finite set $\iota$, let $y \in \mathbb{R}^m$ and $\lambda > 0$, and write $\|\cdot\|$ for the
Euclidean norm. The ridge estimate $\hat\theta = (X^\top X + \lambda I)^{-1} X^\top y$ minimizes
the ridge objective: for every $\theta \in \mathbb{R}^\iota$,
$\|y - X\hat\theta\|^2 + \lambda \|\hat\theta\|^2 \le \|y - X\theta\|^2 + \lambda \|\theta\|^2$.

Formalized by `Cslib.MachineLearning.LeastSquares.ridge_le_ridgeEstimate`, a theorem declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#ridge-le-ridge-estimate).

## Density of independent centred Gaussian coordinates

For a finite set $\iota$, a variance
$\tau \ge 0$ and $\theta \in \mathbb{R}^\iota$, the product over $i \in \iota$ of the densities of
the normal distribution $N(0, \tau)$ at $\theta_i$ equals
$\left(\frac{1}{\sqrt{2\pi\tau}}\right)^{|\iota|} \exp\left(-\frac{1}{2\tau}
\sum_{i \in \iota} \theta_i^2\right)$.

This also holds at $\tau = 0$, where the normal density is the zero function, with the
convention $1/0 = 0$.

Formalized by `Cslib.MachineLearning.LeastSquares.prod_gaussianPDFReal_zero`, a theorem declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#prod-gaussian-pdfreal-zero).

## Posterior kernel of ridge regression

For $s \ge 0$ let $\varphi_s$ be the density of
$N(0, s)$, $\varphi_s(x) = (2 \pi s)^{-1/2} e^{-x^2 / (2 s)}$, with $\varphi_0$ the zero function.
For a real design matrix $X$ with $m$ rows and columns indexed by a finite type $\iota$, responses
$y \in \mathbb{R}^m$, variances $v, \tau \ge 0$ and $\theta \in \mathbb{R}^\iota$, the posterior
kernel is the Gaussian likelihood of $y$ times the prior density of $\theta$:

$$p(\theta) = \prod_{k=1}^{m} \varphi_v(y_k - (X\theta)_k) \prod_{i} \varphi_\tau(\theta_i).$$

This is the posterior kernel of linear regression with Gaussian noise of variance $v$ and
independent $N(0, \tau)$ priors on the coordinates of $\theta$; it is meaningful for
$v, \tau > 0$.

Formalized by `Cslib.MachineLearning.LeastSquares.ridgePosterior`, a definition declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#ridge-posterior).

## Ridge regression is MAP estimation

Let $X$ be a real design matrix with $m$ rows and
columns indexed by a finite type $\iota$, let $y \in \mathbb{R}^m$, and let $v$ and $\tau$ be
positive reals. Let $p$ be the posterior kernel of linear regression with Gaussian noise of
variance $v$ and independent $N(0, \tau)$ priors on the coordinates of the parameter, and let $R$
be the ridge objective with $\lambda = v / \tau$. Then for all
$\theta, \theta' \in \mathbb{R}^\iota$ we have $p(\theta) \le p(\theta')$ if and only if
$R(\theta') \le R(\theta)$.

So the posterior kernel is a decreasing function of the ridge objective.

Formalized by `Cslib.MachineLearning.LeastSquares.ridgePosterior_le_iff`, a theorem declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#ridge-posterior-le-iff).

## The ridge estimate maximizes the ridge posterior

Let $X$ be a real design matrix with $m$
rows and columns indexed by a finite type $\iota$, let $y \in \mathbb{R}^m$, and let $v$ and $\tau$
be positive reals. Let $p$ be the posterior kernel of linear regression with Gaussian noise of
variance $v$ and independent $N(0, \tau)$ priors on the coordinates of the parameter, and let
$\hat\theta = (X^\top X + \lambda I)^{-1} X^\top y$ be the ridge estimate with $\lambda = v / \tau$.
Then $\hat\theta$ maximizes $p$: for every $\theta \in \mathbb{R}^\iota$ we have
$p(\theta) \le p(\hat\theta)$.

Formalized by `Cslib.MachineLearning.LeastSquares.isMaxOn_ridgePosterior`, a theorem declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#is-max-on-ridge-posterior).

## Lasso objective

For a real matrix $X$ with $m$ rows and columns indexed by a finite set
$\iota$, responses $y \in \mathbb{R}^m$ and a real number $\lambda$, the lasso objective at
$\theta \in \mathbb{R}^\iota$ is
$\sum_{k=1}^m (y_k - (X\theta)_k)^2 + \lambda \sum_{i \in \iota} |\theta_i|$, the residual sum of
squares plus $\lambda$ times the $\ell^1$ norm of $\theta$.

Formalized by `Cslib.MachineLearning.LeastSquares.lasso`, a definition declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#lasso).

## Laplace density

For a scale $b \ge 0$, the density of the Laplace distribution with
location $0$ and scale $b$ is the function on $\mathbb{R}$

$$
f_b(x) = \frac{1}{2b} \exp\left(-\frac{|x|}{b}\right).
$$

For $b = 0$ this is read with the convention $1/0 = 0$ and gives the zero function; the results
about this density assume $b \neq 0$.

Formalized by `Cslib.MachineLearning.LeastSquares.laplacePDF`, a definition declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#laplace-pdf).

## Lasso posterior kernel

Let $X$ be a real matrix with $m$ rows and columns indexed by a
finite set $\iota$, let $y \in \mathbb{R}^m$, and let $v \ge 0$ and $b \ge 0$. The lasso posterior
kernel at $\theta \in \mathbb{R}^\iota$ is

$$\prod_{k=1}^{m} \varphi_v\bigl(y_k - (X\theta)_k\bigr) \cdot \prod_{i \in \iota} p_b(\theta_i),$$

where $\varphi_v(x) = e^{-x^2/(2v)} / \sqrt{2\pi v}$ is the density of the normal distribution with
mean $0$ and variance $v$ and $p_b(x) = e^{-|x|/b} / (2b)$ is the density of the Laplace
distribution with location $0$ and scale $b$: the Gaussian likelihood of $y$ with noise variance
$v$ times the Laplace prior density of $\theta$.

It is a meaningful kernel for $v \ne 0$ and $b \ne 0$; for $v = 0$ (respectively $b = 0$) the
normal (respectively Laplace) density is the zero function.

Formalized by `Cslib.MachineLearning.LeastSquares.lassoPosterior`, a definition declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#lasso-posterior).

## Lasso is MAP estimation

Let $X$ be a real matrix with $m$ rows and columns indexed by a
finite set $\iota$, let $y \in \mathbb{R}^m$, and let $v > 0$ and $b > 0$. Let $P$ be the
posterior kernel of linear regression with Gaussian noise of variance $v$ and the Laplace prior
with scale $b$ on each coordinate, and let $\ell$ be the lasso objective with $\lambda = 2v/b$,
$\ell(\theta) = \sum_k (y_k - (X\theta)_k)^2 + \lambda \sum_{i \in \iota} |\theta_i|$. Then for all
$\theta, \theta' \in \mathbb{R}^\iota$, $P(\theta) \le P(\theta')$ if and only if
$\ell(\theta') \le \ell(\theta)$.

Formalized by `Cslib.MachineLearning.LeastSquares.lassoPosterior_le_iff`, a theorem declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#lasso-posterior-le-iff).

## Convexity of the lasso objective

Let $X$ be a real matrix with $m$ rows and columns
indexed by a finite set $\iota$, let $y \in \mathbb{R}^m$ and let $\lambda \ge 0$. Then the lasso
objective $\theta \mapsto \sum_k (y_k - (X\theta)_k)^2 + \lambda \sum_{i \in \iota} |\theta_i|$
is a convex function on all of $\mathbb{R}^\iota$.

Formalized by `Cslib.MachineLearning.LeastSquares.convexOn_lasso`, a theorem declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#convex-on-lasso).

## Soft thresholding

For real numbers $t$ and $z$, the soft thresholding of $z$ at $t$ is
$S_t(z) = z - t$ if $z > t$; otherwise $S_t(z) = z + t$ if $z < -t$; and $S_t(z) = 0$ in the
remaining case.

For $t \ge 0$ this shrinks $z$ towards $0$ by $t$ and sets it to $0$ when $|z| \le t$.

Formalized by `Cslib.MachineLearning.LeastSquares.softThreshold`, a definition declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 442](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L442). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#soft-threshold).

## Soft thresholding solves the one-dimensional lasso

Let $t \ge 0$ and $z \in \mathbb{R}$,
and let $S_t(z)$ be the soft thresholding of $z$ at $t$. Then for every $s \in \mathbb{R}$,

$$(z - S_t(z))^2 + 2t\,|S_t(z)| \le (z - s)^2 + 2t\,|s|,$$

so $S_t(z)$ minimizes $(z - s)^2 + 2t\,|s|$ over $s \in \mathbb{R}$.

Formalized by `Cslib.MachineLearning.LeastSquares.softThreshold_le`, a theorem declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 447](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L447). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#soft-threshold-le).

## Lasso with an orthonormal design

Let $X$ be a real matrix with $m$ rows and columns indexed
by a finite set $\iota$ such that $X^\top X = I$, let $y \in \mathbb{R}^m$ and let $\lambda \ge 0$.
Let $\hat\theta \in \mathbb{R}^\iota$ be given by $\hat\theta_i = S_{\lambda/2}((X^\top y)_i)$,
where $S_t$ is soft thresholding at $t$. Then $\hat\theta$ minimizes the lasso objective: for every
$\theta \in \mathbb{R}^\iota$,
$\sum_{k=1}^m (y_k - (X\hat\theta)_k)^2 + \lambda \sum_{i \in \iota} |\hat\theta_i| \le
\sum_{k=1}^m (y_k - (X\theta)_k)^2 + \lambda \sum_{i \in \iota} |\theta_i|$.

Formalized by `Cslib.MachineLearning.LeastSquares.lasso_softThreshold_le`, a theorem declared in [CSLibExt/MachineLearning/Regression/LeastSquares.lean, line 466](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/LeastSquares.lean#L466). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html#lasso-soft-threshold-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Least squares, ridge and lasso regression](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/machine-learning/supervised-learning/least-squares-ridge-and-lasso-regression)
