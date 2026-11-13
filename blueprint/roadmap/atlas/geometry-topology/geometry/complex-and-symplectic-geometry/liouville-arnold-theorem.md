---
declaration: section
origin: cited
lean: MathlibExt.Geometry.LiouvilleArnoldWanted.Geometry.LiouvilleArnold.E, MathlibExt.Geometry.LiouvilleArnoldWanted.Geometry.LiouvilleArnold.idxP, MathlibExt.Geometry.LiouvilleArnoldWanted.Geometry.LiouvilleArnold.idxQ, MathlibExt.Geometry.LiouvilleArnoldWanted.Geometry.LiouvilleArnold.poissonBracket, MathlibExt.Geometry.LiouvilleArnoldWanted.Geometry.LiouvilleArnold.IsLiouvilleIntegrable, MathlibExt.Geometry.LiouvilleArnoldWanted.Geometry.LiouvilleArnold.levelSet, MathlibExt.Geometry.LiouvilleArnoldWanted.Geometry.LiouvilleArnold.liouville_arnold
statement: formalized
---

# Liouville–Arnold theorem

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/liouville-arnold-theorem/index.html).

## The model space $\mathbb{R}^{2n}$ of the Liouville–Arnold theorem

For a natural number
$n$, $E_n$ is the Euclidean space $\mathbb{R}^{2n}$, with coordinates indexed by
$0, \dots, 2n-1$ and the standard inner product.

Formalized by `MathlibExt.Geometry.LiouvilleArnoldWanted.Geometry.LiouvilleArnold.E`, an abbreviation declared in [WantedExt/Geometry/LiouvilleArnoldWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LiouvilleArnoldWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/liouville-arnold-theorem/index.html#e).

## Liouville–Arnold coordinates: index of $p_i$

For $i \in \{0, \dots, n-1\}$, the
coordinate $p_i$ of $\mathbb{R}^{2n}$ is coordinate number $i$: this map sends $i$ to the same
number $i$, regarded as an index in $\{0, \dots, 2n-1\}$.

Formalized by `MathlibExt.Geometry.LiouvilleArnoldWanted.Geometry.LiouvilleArnold.idxP`, a definition declared in [WantedExt/Geometry/LiouvilleArnoldWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LiouvilleArnoldWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/liouville-arnold-theorem/index.html#idx-p).

## Liouville–Arnold coordinates: index of $q_i$

For $i \in \{0, \dots, n-1\}$, the
coordinate $q_i$ of $\mathbb{R}^{2n}$ is coordinate number $n + i$: this map sends $i$ to
$n + i \in \{0, \dots, 2n-1\}$.

Formalized by `MathlibExt.Geometry.LiouvilleArnoldWanted.Geometry.LiouvilleArnold.idxQ`, a definition declared in [WantedExt/Geometry/LiouvilleArnoldWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LiouvilleArnoldWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/liouville-arnold-theorem/index.html#idx-q).

## Standard Poisson bracket on $\mathbb{R}^{2n}$

Write the coordinates of a point
$x \in \mathbb{R}^{2n}$ as $p_i = x_i$ and $q_i = x_{n+i}$ for $i = 0, \dots, n-1$. For functions
$F, G \colon \mathbb{R}^{2n} \to \mathbb{R}$, the Poisson bracket for the symplectic form
$\omega_0 = \sum_i dp_i \wedge dq_i$ is the function

$$
\{F, G\}(x) = \sum_{i=0}^{n-1} \left( \frac{\partial F}{\partial p_i}(x)
\frac{\partial G}{\partial q_i}(x) - \frac{\partial F}{\partial q_i}(x)
\frac{\partial G}{\partial p_i}(x) \right).
$$

Partial derivatives are read off the Fréchet derivative, which is taken to be zero at points
where the function is not differentiable.

Formalized by `MathlibExt.Geometry.LiouvilleArnoldWanted.Geometry.LiouvilleArnold.poissonBracket`, a definition declared in [WantedExt/Geometry/LiouvilleArnoldWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LiouvilleArnoldWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/liouville-arnold-theorem/index.html#poisson-bracket).

## Liouville integrable system on a subset of $\mathbb{R}^{2n}$

Functions
$F_0, \dots, F_{n-1} \colon \mathbb{R}^{2n} \to \mathbb{R}$ are Liouville integrable on a set
$U \subseteq \mathbb{R}^{2n}$ if each $F_i$ is $C^\infty$ on $U$, the Poisson brackets
$\{F_i, F_j\}$ vanish at every point of $U$ for all $i, j$, and at every $x \in U$ the
Fréchet derivatives $dF_0(x), \dots, dF_{n-1}(x)$ are linearly independent over $\mathbb{R}$.

The set $U$ is not required to be open; the Liouville–Arnold theorem assumes this separately.

Formalized by `MathlibExt.Geometry.LiouvilleArnoldWanted.Geometry.LiouvilleArnold.IsLiouvilleIntegrable`, a definition declared in [WantedExt/Geometry/LiouvilleArnoldWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LiouvilleArnoldWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/liouville-arnold-theorem/index.html#is-liouville-integrable).

## Common level set of $n$ functions on $\mathbb{R}^{2n}$

For functions
$F_0, \dots, F_{n-1} \colon \mathbb{R}^{2n} \to \mathbb{R}$ and values
$c_0, \dots, c_{n-1} \in \mathbb{R}$, the common level set is
$\{x \in \mathbb{R}^{2n} : F_i(x) = c_i \text{ for all } i\}$.

Formalized by `MathlibExt.Geometry.LiouvilleArnoldWanted.Geometry.LiouvilleArnold.levelSet`, a definition declared in [WantedExt/Geometry/LiouvilleArnoldWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LiouvilleArnoldWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/liouville-arnold-theorem/index.html#level-set).

## Liouville–Arnold theorem

Let $U \subseteq \mathbb{R}^{2n}$ be open and let
$F_0, \dots, F_{n-1} \colon \mathbb{R}^{2n} \to \mathbb{R}$ be Liouville integrable on $U$. For
$c = (c_0, \dots, c_{n-1}) \in \mathbb{R}^n$, let
$M_c = \{x \in \mathbb{R}^{2n} : F_i(x) = c_i \text{ for all } i\}$ be the common level set. If
$M_c \subseteq U$ and $M_c$ is compact and connected (in particular nonempty), then $M_c$ is
homeomorphic to the $n$-torus $(\mathbb{R}/\mathbb{Z})^n$.

The hypotheses *compact* and *connected* on the level set, and its
containment in the open set where the derivatives are independent,
restore standard regularity assumptions that Knill elides; without them
the conclusion fails.

## Sources

- V. I. Arnold, *Mathematical Methods of Classical Mechanics* (2nd ed., 1989), Theorem 49.A.1 (the standard modern reference). The result is due to Liouville (1855) for the local existence of action-angle coordinates and Arnold (1963) for the compact-connected-component topology. Listed as §45 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `liouville_arnold` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.LiouvilleArnoldWanted.Geometry.LiouvilleArnold.liouville_arnold` is written with `theorem_wanted` in [WantedExt/Geometry/LiouvilleArnoldWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LiouvilleArnoldWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/liouville-arnold-theorem/index.html#liouville-arnold).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Liouville–Arnold theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/liouville-arnold-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/complex-and-symplectic-geometry/liouville-arnold-theorem)
