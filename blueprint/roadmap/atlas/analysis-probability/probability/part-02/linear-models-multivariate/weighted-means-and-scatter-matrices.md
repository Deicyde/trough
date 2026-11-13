---
declaration: section
origin: cited
lean: MetaMathlibExt.weightedMean, MetaMathlibExt.weightedScatter, MetaMathlibExt.sum_smul_sub_weightedMean, MetaMathlibExt.sum_mul_quad_sub_eq, MetaMathlibExt.sum_mul_quad_eq_trace, MetaMathlibExt.dotProduct_weightedScatter_mulVec, MetaMathlibExt.weightedScatter_posDef
statement: formalized
proof: formalized
---

# Weighted means and scatter matrices

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/weighted-means-and-scatter-matrices/index.html).

## Weighted mean

Let $I$ be a finite set and $J$ an index set, and let
$x_i \in \mathbb{R}^J$ ($i \in I$) be points with real weights $w_i$. Their weighted mean is the
point $\big(\sum_{i \in I} w_i\big)^{-1} \sum_{i \in I} w_i x_i$ of $\mathbb{R}^J$, that is
$\sum_i w_i x_i / \sum_i w_i$, with the convention $0^{-1} = 0$ when the weights sum to $0$.

Formalized by `MetaMathlibExt.weightedMean`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/WeightedScatter.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/WeightedScatter.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/weighted-means-and-scatter-matrices/index.html#weighted-mean).

## Weighted scatter matrix

Let $I$ be a finite set and $J$ an index set, let
$x_i \in \mathbb{R}^J$ ($i \in I$) be points with real weights $w_i$, and let
$\mu \in \mathbb{R}^J$. The weighted scatter matrix of the $x_i$ about $\mu$ is the real
$J \times J$ matrix

$$
C = \Big(\sum_{i \in I} w_i\Big)^{-1} \sum_{i \in I} w_i \, (x_i - \mu)(x_i - \mu)^{\mathsf T},
$$

with the convention $0^{-1} = 0$ when the weights sum to $0$. When $\mu$ is the weighted mean of
the $x_i$, it is the weighted sample covariance.

Formalized by `MetaMathlibExt.weightedScatter`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/WeightedScatter.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/WeightedScatter.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/weighted-means-and-scatter-matrices/index.html#weighted-scatter).

## Weighted residuals sum to zero

Let $I$ be a finite set and $J$ any index set, let
$x_i \in \mathbb{R}^J$ ($i \in I$) be points with real weights $w_i$ such that $\sum_i w_i \ne 0$,
and let $m$ be their weighted mean. Then $\sum_{i \in I} w_i (x_i - m) = 0$.

Formalized by `MetaMathlibExt.sum_smul_sub_weightedMean`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/WeightedScatter.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/WeightedScatter.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/weighted-means-and-scatter-matrices/index.html#sum-smul-sub-weighted-mean).

## The bias-variance split of a weighted quadratic form

Let $I$ and $J$ be finite sets, let
$x_i \in \mathbb{R}^J$ ($i \in I$) be points with real weights $w_i$ such that $\sum_i w_i \ne 0$,
let $m$ be their weighted mean, let $A$ be a symmetric real $J \times J$ matrix, and let
$\mu \in \mathbb{R}^J$. Then

$$
\sum_{i \in I} w_i \, (x_i - \mu)^{\mathsf T} A \, (x_i - \mu) =
\sum_{i \in I} w_i \, (x_i - m)^{\mathsf T} A \, (x_i - m) +
\Big(\sum_{i \in I} w_i\Big) (m - \mu)^{\mathsf T} A \, (m - \mu).
$$

Formalized by `MetaMathlibExt.sum_mul_quad_sub_eq`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/WeightedScatter.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/WeightedScatter.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/weighted-means-and-scatter-matrices/index.html#sum-mul-quad-sub-eq).

## Weighted quadratic forms as traces against the scatter matrix

Let $I$ and $J$ be finite
sets, let $x_i \in \mathbb{R}^J$ ($i \in I$) be points with real weights $w_i$ such that
$\sum_i w_i \ne 0$, let $A$ be a real $J \times J$ matrix, let $\mu \in \mathbb{R}^J$, and let $C$
be the weighted scatter matrix of the $x_i$ about $\mu$. Then

$$
\sum_{i \in I} w_i \, (x_i - \mu)^{\mathsf T} A \, (x_i - \mu) =
\Big(\sum_{i \in I} w_i\Big) \operatorname{tr}(A C).
$$

Formalized by `MetaMathlibExt.sum_mul_quad_eq_trace`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/WeightedScatter.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/WeightedScatter.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/weighted-means-and-scatter-matrices/index.html#sum-mul-quad-eq-trace).

## Quadratic form of a weighted scatter matrix

Let $I$ and $J$ be finite sets, let
$x_i \in \mathbb{R}^J$ ($i \in I$) be points with real weights $w_i$, let $\mu \in \mathbb{R}^J$,
and let $C$ be the weighted scatter matrix of the $x_i$ about $\mu$. Then for every
$u \in \mathbb{R}^J$,

$$
u^{\mathsf T} C u =
\Big(\sum_{i \in I} w_i\Big)^{-1} \sum_{i \in I} w_i \big(u \cdot (x_i - \mu)\big)^2,
$$

with the convention $0^{-1} = 0$.

Formalized by `MetaMathlibExt.dotProduct_weightedScatter_mulVec`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/WeightedScatter.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/WeightedScatter.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/weighted-means-and-scatter-matrices/index.html#dot-product-weighted-scatter-mul-vec).

## Weighted scatter matrices of points in general position are positive definite

Let $I$
and $J$ be finite sets and let $x_i \in \mathbb{R}^J$ ($i \in I$) be points with positive weights
$w_i > 0$ that do not all lie in an affine hyperplane: for every nonzero $v \in \mathbb{R}^J$
there are $i, j \in I$ with $\langle v, x_i \rangle \ne \langle v, x_j \rangle$. Then for every
$\mu \in \mathbb{R}^J$ the weighted scatter matrix of the $x_i$ about $\mu$ is positive definite.

Formalized by `MetaMathlibExt.weightedScatter_posDef`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/WeightedScatter.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/WeightedScatter.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/weighted-means-and-scatter-matrices/index.html#weighted-scatter-pos-def).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weighted means and scatter matrices](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/weighted-means-and-scatter-matrices/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/linear-models-multivariate/weighted-means-and-scatter-matrices)
