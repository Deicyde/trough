---
declaration: section
origin: cited
lean: MetaMathlibExt.noiseKernel, MetaMathlibExt.condDistrib_add_of_indepFun, MetaMathlibExt.condDistrib_of_hasGaussianLaw, MetaMathlibExt.map_toEuclideanLin_multivariateGaussian, MetaMathlibExt.map_add_multivariateGaussian, MetaMathlibExt.blockRow, MetaMathlibExt.covariance_inner_of_map_eq, MetaMathlibExt.condDistrib_multivariateGaussian
statement: formalized
proof: formalized
---

# Gaussian conditioning

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/gaussian-conditioning/index.html).

## The additive-noise kernel

Let $E$ be an additive commutative group with a measurable
structure for which addition $E \times E \to E$ is measurable, let $F$ be a measurable space, let
$f \colon F \to E$ be a measurable map and let $\nu$ be a measure on $E$. If $\nu$ is s-finite,
the additive-noise kernel from $F$ to $E$ sends $y \in F$ to the image of the product measure
$\delta_{f(y)} \otimes \nu$ (where $\delta_{f(y)}$ is the Dirac measure at $f(y)$) under addition
$(a, z) \mapsto a + z$, that is, to the image of $\nu$ under $z \mapsto f(y) + z$. If $\nu$ is not
s-finite, it is the zero kernel.

When $\nu$ is a probability measure, the kernel sends $y$ to the law of $f(y) + Z$ for a random
variable $Z$ with law $\nu$.

Formalized by `MetaMathlibExt.noiseKernel`, a definition declared in [MathlibExt/Probability/Distributions/GaussianConditioning.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/GaussianConditioning.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/gaussian-conditioning/index.html#noise-kernel).

## Conditioning on a signal observed in independent additive noise

Let $E$ be a nonempty
standard Borel space that is an abelian group with measurable addition, let $F$ be a measurable
space, and let $Y \colon \Omega \to F$ and $Z \colon \Omega \to E$ be independent measurable random
variables on a probability space. For every measurable $f \colon F \to E$ and almost every $y$
with respect to the law of $Y$, the conditional distribution of $f(Y) + Z$ given $Y = y$ is the
law of $f(y) + Z$.

Formalized by `MetaMathlibExt.condDistrib_add_of_indepFun`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianConditioning.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/GaussianConditioning.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/gaussian-conditioning/index.html#cond-distrib-add-of-indep-fun).

## Gaussian conditioning

Let $E$ and $F$ be finite-dimensional real inner product spaces,
and let $X$ and $Y$ be measurable random vectors in $E$ and $F$ on a probability space such that
$(X, Y)$ is jointly Gaussian. Let $A \colon F \to E$ be a linear map whose residual $X - A Y$ is
uncorrelated with $Y$ (the normal equations): for all $u \in E$ and $w \in F$,
$\operatorname{Cov}(\langle u, X - A Y \rangle, \langle w, Y \rangle) = 0$. Then $X - A Y$ is
Gaussian and independent of $Y$, and for almost every $y$ with respect to the law of $Y$, the
conditional distribution of $X$ given $Y = y$ is the law of $A y + (X - A Y)$.

Formalized by `MetaMathlibExt.condDistrib_of_hasGaussianLaw`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianConditioning.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/GaussianConditioning.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/gaussian-conditioning/index.html#cond-distrib-of-has-gaussian-law).

## Linear images of multivariate Gaussians

Write $\mathcal{N}(a, \Sigma)$ for the
multivariate Gaussian distribution with mean $a$ and covariance matrix $\Sigma$. Let $\iota$ and
$\kappa$ be finite index sets, let $M$ be a real $\iota \times \kappa$ matrix, let
$\mu \in \mathbb{R}^\kappa$ and let $S$ be a positive semidefinite real $\kappa \times \kappa$
matrix. Then the image of $\mathcal{N}(\mu, S)$ under the linear map $z \mapsto M z$ is
$\mathcal{N}(M \mu, M S M^\top)$.

Formalized by `MetaMathlibExt.map_toEuclideanLin_multivariateGaussian`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianConditioning.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/GaussianConditioning.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/gaussian-conditioning/index.html#map-to-euclidean-lin-multivariate-gaussi).

## Translating a multivariate Gaussian

Let $\iota$ be a finite index set. For all
$c, \mu \in \mathbb{R}^\iota$ and every real $\iota \times \iota$ matrix $S$, the pushforward of
$N(\mu, S)$ under the translation $x \mapsto c + x$ is $N(c + \mu, S)$.

No positive semidefiniteness is assumed: when $S$ is not positive semidefinite, $N(\mu, S)$ is
taken to be the point mass at $\mu$.

Formalized by `MetaMathlibExt.map_add_multivariateGaussian`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianConditioning.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/GaussianConditioning.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/gaussian-conditioning/index.html#map-add-multivariate-gaussian).

## Horizontal block matrix

Let $\rho$, $\iota$ and $\kappa$ be index sets with $\iota$ and
$\kappa$ finite. For real matrices $P$ with rows indexed by $\rho$ and columns by $\iota$, and $Q$
with rows indexed by $\rho$ and columns by $\kappa$, the block row $[P\ Q]$ is the real matrix with
rows indexed by $\rho$ and columns indexed by the disjoint union $\iota \sqcup \kappa$, whose
entry in row $r$ is $P_{ri}$ in the column of $i \in \iota$ and $Q_{rk}$ in the column of
$k \in \kappa$.

Formalized by `MetaMathlibExt.blockRow`, a definition declared in [MathlibExt/Probability/Distributions/GaussianConditioning.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/GaussianConditioning.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/gaussian-conditioning/index.html#block-row).

## Covariances of linear functionals of a Gaussian vector

Let $\nu$ be a finite index set
and let $V$ be a measurable random vector in $\mathbb{R}^\nu$ on a probability space with law
$N(\mu, S)$, where $S$ is positive semidefinite. Then for all $a, b \in \mathbb{R}^\nu$,
$\operatorname{Cov}(\langle a, V \rangle, \langle b, V \rangle) = a^\top S b$.

Formalized by `MetaMathlibExt.covariance_inner_of_map_eq`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianConditioning.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/GaussianConditioning.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/gaussian-conditioning/index.html#covariance-inner-of-map-eq).

## Gaussian conditioning (Schur complement)

Let $\iota$ and $\kappa$ be finite index sets
and let $V$ be a measurable random vector in $\mathbb{R}^{\iota \sqcup \kappa}$ on a probability
space, with blocks $X \in \mathbb{R}^\iota$ and $Y \in \mathbb{R}^\kappa$. Suppose $V$ has law
$N(\mu, S)$ with $S$ positive semidefinite, write $\mu_X, \mu_Y$ for the blocks of $\mu$ and
$S_{11}, S_{12}, S_{21}, S_{22}$ for the blocks of $S$ indexed by $\iota \times \iota$,
$\iota \times \kappa$, $\kappa \times \iota$ and $\kappa \times \kappa$, and suppose $S_{22}$ is
invertible. Then for almost every $y$ with respect to the law of $Y$, the conditional
distribution of $X$ given $Y = y$ is
$N(\mu_X + S_{12} S_{22}^{-1} (y - \mu_Y), S_{11} - S_{12} S_{22}^{-1} S_{21})$.

Formalized by `MetaMathlibExt.condDistrib_multivariateGaussian`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianConditioning.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/GaussianConditioning.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/gaussian-conditioning/index.html#cond-distrib-multivariate-gaussian).

## Block-diagonal matrices with positive semidefinite blocks

Let $\iota$ and $\kappa$ be
finite index sets and let $S$ and $R$ be positive semidefinite real matrices indexed by $\iota$
and by $\kappa$. Then the block-diagonal matrix $\begin{pmatrix} S & 0 \\ 0 & R \end{pmatrix}$,
indexed by $\iota \sqcup \kappa$, is positive semidefinite.

Formalized by `MetaMathlibExt.posSemidef_fromBlocks_zero`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianConditioning.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/GaussianConditioning.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/gaussian-conditioning/index.html#pos-semidef-from-blocks-zero).

## The inner product splits over blocks

Let $\iota$ and $\kappa$ be finite index sets. For
$p_1 \in \mathbb{R}^\iota$, $p_2 \in \mathbb{R}^\kappa$ and $t \in \mathbb{R}^{\iota \sqcup \kappa}$
with blocks $t_\iota \in \mathbb{R}^\iota$ and $t_\kappa \in \mathbb{R}^\kappa$, the inner product
of the concatenation of $p_1$ and $p_2$ with $t$ is
$\langle p_1, t_\iota \rangle + \langle p_2, t_\kappa \rangle$.

Formalized by `MetaMathlibExt.inner_sumEquivProd_symm`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianConditioning.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/GaussianConditioning.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/gaussian-conditioning/index.html#inner-sum-equiv-prod-symm).

## Characteristic function of a product of blocks

Let $\iota$ and $\kappa$ be finite index
sets, let $\mu$ and $\nu$ be finite measures on $\mathbb{R}^\iota$ and $\mathbb{R}^\kappa$, and let
$\pi$ be the pushforward of the product measure $\mu \otimes \nu$ to
$\mathbb{R}^{\iota \sqcup \kappa}$ under concatenation of the two blocks. Write $\varphi_\rho$ for
the characteristic function of a measure $\rho$. Then for every
$t \in \mathbb{R}^{\iota \sqcup \kappa}$ with blocks $t_\iota \in \mathbb{R}^\iota$ and
$t_\kappa \in \mathbb{R}^\kappa$, we have
$\varphi_\pi(t) = \varphi_\mu(t_\iota) \, \varphi_\nu(t_\kappa)$.

Formalized by `MetaMathlibExt.charFun_map_sumEquivProd_symm_prod`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianConditioning.lean, line 347](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/GaussianConditioning.lean#L347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/gaussian-conditioning/index.html#char-fun-map-sum-equiv-prod-symm-prod).

## Independent Gaussian blocks

Write $\mathcal{N}(a, \Sigma)$ for the multivariate
Gaussian distribution with mean $a$ and covariance matrix $\Sigma$. Let $\iota$ and $\kappa$ be
finite index sets, let $m \in \mathbb{R}^\iota$ and $m' \in \mathbb{R}^\kappa$, and let $S$ and
$R$ be positive semidefinite real matrices indexed by $\iota$ and by $\kappa$. Then the image of
the product measure $\mathcal{N}(m, S) \otimes \mathcal{N}(m', R)$ under the concatenation map
$\mathbb{R}^\iota \times \mathbb{R}^\kappa \to \mathbb{R}^{\iota \sqcup \kappa}$ is
$\mathcal{N}\left((m, m'), \begin{pmatrix} S & 0 \\ 0 & R \end{pmatrix}\right)$.

Formalized by `MetaMathlibExt.map_sumEquivProd_symm_prod_multivariateGaussian`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianConditioning.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/GaussianConditioning.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/gaussian-conditioning/index.html#map-sum-equiv-prod-symm-prod-multivariat).

## Concatenation of independent Gaussian random vectors

Write $\mathcal{N}(a, \Sigma)$ for
the multivariate Gaussian distribution with mean $a$ and covariance matrix $\Sigma$. Let $\iota$
and $\kappa$ be finite index sets, and let $x$ and $v$ be independent measurable random vectors in
$\mathbb{R}^\iota$ and $\mathbb{R}^\kappa$ on a probability space, with laws $\mathcal{N}(m, S)$
and $\mathcal{N}(m', R)$ for positive semidefinite real matrices $S$ and $R$. Then the
concatenated random vector $(x, v)$ in $\mathbb{R}^{\iota \sqcup \kappa}$ has law
$\mathcal{N}\left((m, m'), \begin{pmatrix} S & 0 \\ 0 & R \end{pmatrix}\right)$.

Formalized by `MetaMathlibExt.map_sumEquivProd_symm_of_indepFun`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianConditioning.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/GaussianConditioning.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/gaussian-conditioning/index.html#map-sum-equiv-prod-symm-of-indep-fun).

## Block-triangular congruence of a block-diagonal matrix

Let $n$ and $p$ be finite index
sets and let $S$, $R$ and $H$ be real matrices of sizes $n \times n$, $p \times p$ and
$p \times n$. Let $M$ be the block matrix with block rows $(I_n, 0)$ and $(H, I_p)$, and let $D$
be the block-diagonal matrix with diagonal blocks $S$ and $R$. Then $M D M^\top$ is the block
matrix with block rows $(S, S H^\top)$ and $(H S, H S H^\top + R)$.

When $x$ and $v$ are independent random vectors with covariances $S$ and $R$, this is the joint
covariance of $(x, H x + v)$.

Formalized by `MetaMathlibExt.fromBlocks_one_zero_mul_mul_transpose`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianConditioning.lean, line 452](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/GaussianConditioning.lean#L452). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/gaussian-conditioning/index.html#from-blocks-one-zero-mul-mul-transpose).

## The joint covariance of a linear-Gaussian model is positive semidefinite

Let $n$ and $p$
be finite index sets, let $S$ and $R$ be positive semidefinite real matrices indexed by $n$ and by
$p$, and let $H$ be a real $p \times n$ matrix. Then the block matrix
$\begin{pmatrix} S & S H^\top \\ H S & H S H^\top + R \end{pmatrix}$, indexed by $n \sqcup p$, is
positive semidefinite.

Formalized by `MetaMathlibExt.posSemidef_fromBlocks_linear`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianConditioning.lean, line 460](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/GaussianConditioning.lean#L460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/gaussian-conditioning/index.html#pos-semidef-from-blocks-linear).

## The posterior covariance is positive semidefinite

Let $n$ and $p$ be finite index sets,
let $S$ be a positive semidefinite real $n \times n$ matrix, let $R$ be a positive definite real
$p \times p$ matrix and let $H$ be a real $p \times n$ matrix. Then
$S - S H^\top (H S H^\top + R)^{-1} H S$ is positive semidefinite.

This matrix is the Schur complement of the lower-right block in the joint covariance
$\begin{pmatrix} S & S H^\top \\ H S & H S H^\top + R \end{pmatrix}$ of a linear-Gaussian model.

Formalized by `MetaMathlibExt.posSemidef_sub_mul_inv_mul`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianConditioning.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/GaussianConditioning.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/gaussian-conditioning/index.html#pos-semidef-sub-mul-inv-mul).

## The marginal of a linear-Gaussian model

Write $\mathcal{N}(a, \Sigma)$ for the
multivariate Gaussian distribution with mean $a$ and covariance matrix $\Sigma$. Let $n$ and $p$
be finite index sets, and let $x$ and $w$ be independent measurable random vectors in
$\mathbb{R}^n$ and $\mathbb{R}^p$ on a probability space, where $x$ has law
$\mathcal{N}(m, S)$ and $w$ has law $\mathcal{N}(c, Q)$ for positive semidefinite real matrices
$S$ and $Q$. Then for every real $p \times n$ matrix $F$, the random vector $F x + w$ has law
$\mathcal{N}(F m + c, F S F^\top + Q)$.

Formalized by `MetaMathlibExt.map_linear_add_of_indepFun`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianConditioning.lean, line 499](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/GaussianConditioning.lean#L499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/gaussian-conditioning/index.html#map-linear-add-of-indep-fun).

## Bayes' theorem for a linear-Gaussian observation

Let $n$ and $p$ be finite index sets,
and let $x$ and $v$ be independent measurable random vectors in $\mathbb{R}^n$ and $\mathbb{R}^p$
on a probability space, with $x \sim N(m, S)$ and $v \sim N(0, R)$ for positive semidefinite
matrices $S$ and $R$. Let $H$ be a real $p \times n$ matrix such that $H S H^\top + R$ is
invertible, and let $Y = H x + v$. Then for almost every $y$ with respect to the law of $Y$, the
conditional distribution of $x$ given $Y = y$ is the Gaussian with mean
$m + S H^\top (H S H^\top + R)^{-1} (y - H m)$ and covariance
$S - S H^\top (H S H^\top + R)^{-1} H S$.

Formalized by `MetaMathlibExt.condDistrib_linear_add_of_indepFun`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianConditioning.lean, line 523](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/GaussianConditioning.lean#L523). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/gaussian-conditioning/index.html#cond-distrib-linear-add-of-indep-fun).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gaussian conditioning](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/gaussian-conditioning/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/distributions/continuous/gaussian-conditioning)
