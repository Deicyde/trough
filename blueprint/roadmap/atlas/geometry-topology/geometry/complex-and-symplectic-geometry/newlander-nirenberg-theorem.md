---
declaration: section
origin: cited
lean: MathlibExt.Geometry.NewlanderNirenbergWanted.Geometry.NewlanderNirenberg.E, MathlibExt.Geometry.NewlanderNirenbergWanted.Geometry.NewlanderNirenberg.nijenhuis, MathlibExt.Geometry.NewlanderNirenbergWanted.Geometry.NewlanderNirenberg.IsAlmostComplexOn, MathlibExt.Geometry.NewlanderNirenbergWanted.Geometry.NewlanderNirenberg.NijenhuisVanishesOn, MathlibExt.Geometry.NewlanderNirenbergWanted.Geometry.NewlanderNirenberg.newlander_nirenberg
statement: formalized
---

# Newlander–Nirenberg theorem

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/newlander-nirenberg-theorem/index.html).

## Model space $\mathbb{R}^{2n}$ for the Newlander–Nirenberg theorem

For a natural number
$n$, $E_n$ is the Euclidean space $\mathbb{R}^{2n}$, the model space carrying the almost complex
structure.

Formalized by `MathlibExt.Geometry.NewlanderNirenbergWanted.Geometry.NewlanderNirenberg.E`, an abbreviation declared in [WantedExt/Geometry/NewlanderNirenbergWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/NewlanderNirenbergWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/newlander-nirenberg-theorem/index.html#e).

## Nijenhuis tensor

Let $n$ be a natural number, let $J$ assign to each point
$y \in \mathbb{R}^{2n}$ a real linear map $J(y) : \mathbb{R}^{2n} \to \mathbb{R}^{2n}$, and let
$V, W : \mathbb{R}^{2n} \to \mathbb{R}^{2n}$ be vector fields. Write $JV$ for the vector field
$y \mapsto J(y)V(y)$ and $[V, W]$ for the Lie bracket of vector fields. The Nijenhuis tensor of
$J$ at a point $x \in \mathbb{R}^{2n}$ is

$$N(V, W)(x) = [JV, JW](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/complex-and-symplectic-geometry/newlander-nirenberg-theorem/x) - J(x)[JV, W](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/complex-and-symplectic-geometry/newlander-nirenberg-theorem/x) - J(x)[V, JW](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/complex-and-symplectic-geometry/newlander-nirenberg-theorem/x) - [V, W](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/complex-and-symplectic-geometry/newlander-nirenberg-theorem/x).$$

For an almost complex structure the last term is $J^2[V, W]$, so this is the usual torsion of
$J$. When $J$ is an almost complex structure on an open set $U \subseteq \mathbb{R}^{2n}$, the
expression is $C^\infty(U)$-bilinear in $V$ and $W$ on $U$: the terms involving the derivatives
of $V$ and $W$ cancel using $J^2 = -1$, so the value at a point $x$ of $U$ depends only on
$V(x)$, $W(x)$ and the derivative of $J$ there.

Formalized by `MathlibExt.Geometry.NewlanderNirenbergWanted.Geometry.NewlanderNirenberg.nijenhuis`, a definition declared in [WantedExt/Geometry/NewlanderNirenbergWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/NewlanderNirenbergWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/newlander-nirenberg-theorem/index.html#nijenhuis).

## Almost complex structure on a subset of $\mathbb{R}^{2n}$

Let $n$ be a natural number,
let $U \subseteq \mathbb{R}^{2n}$ and let $J$ assign to each point $y \in \mathbb{R}^{2n}$ a real
linear map $J(y) : \mathbb{R}^{2n} \to \mathbb{R}^{2n}$. Then $J$ is an almost complex structure
on $U$ if $J$ is $C^\infty$ on $U$ and $J(x)(J(x)v) = -v$ for every $x \in U$ and every
$v \in \mathbb{R}^{2n}$.

Formalized by `MathlibExt.Geometry.NewlanderNirenbergWanted.Geometry.NewlanderNirenberg.IsAlmostComplexOn`, a definition declared in [WantedExt/Geometry/NewlanderNirenbergWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/NewlanderNirenbergWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/newlander-nirenberg-theorem/index.html#is-almost-complex-on).

## Vanishing of the Nijenhuis tensor on a set

Let $n$ be a natural number, let
$U \subseteq \mathbb{R}^{2n}$, let $J$ assign to each point $y \in \mathbb{R}^{2n}$ a real linear
map $J(y) : \mathbb{R}^{2n} \to \mathbb{R}^{2n}$, and write $N$ for the Nijenhuis tensor of $J$.
The Nijenhuis tensor of $J$ vanishes on $U$ if $N(V, W)(x) = 0$ for all $C^\infty$ vector fields
$V, W : \mathbb{R}^{2n} \to \mathbb{R}^{2n}$ and every $x \in U$.

The vector fields range over globally smooth fields, which is the textbook hypothesis. Whenever
$U$ is open and $J$ is an almost complex structure on $U$ this is equivalent to the pointwise
condition: the tensor is bilinear over functions, and constant vector fields already realize
every pair of tangent vectors.

Formalized by `MathlibExt.Geometry.NewlanderNirenbergWanted.Geometry.NewlanderNirenberg.NijenhuisVanishesOn`, a definition declared in [WantedExt/Geometry/NewlanderNirenbergWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/NewlanderNirenbergWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/newlander-nirenberg-theorem/index.html#nijenhuis-vanishes-on).

## Newlander–Nirenberg theorem

Let $n$ be a natural number, let $U \subseteq \mathbb{R}^{2n}$
be open and let $J$ be an almost complex structure on $U$ whose Nijenhuis tensor vanishes on $U$.
Then every $x \in U$ has holomorphic coordinates for $J$: there are open sets
$S \subseteq \mathbb{R}^{2n}$ and $T \subseteq \mathbb{C}^n$ with $x \in S \subseteq U$ and a
homeomorphism $\varphi : S \to T$ such that $\varphi$ is $C^\infty$ on $S$, $\varphi^{-1}$ is
$C^\infty$ on $T$ (both as maps of real vector spaces), and for every $y \in S$ and every
$v \in \mathbb{R}^{2n}$ the real derivative of $\varphi$ satisfies
$D\varphi(y)(J(y)v) = i \, D\varphi(y)v$.

## Sources

- A. Newlander and L. Nirenberg, `Complex analytic coordinates in almost complex manifolds`, Annals of Math, 65 (3) 1957, 391-404. Problem `newlander_nirenberg` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.NewlanderNirenbergWanted.Geometry.NewlanderNirenberg.newlander_nirenberg` is written with `theorem_wanted` in [WantedExt/Geometry/NewlanderNirenbergWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/NewlanderNirenbergWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/newlander-nirenberg-theorem/index.html#newlander-nirenberg).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Newlander–Nirenberg theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/newlander-nirenberg-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/complex-and-symplectic-geometry/newlander-nirenberg-theorem)
