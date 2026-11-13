---
declaration: section
origin: cited
lean: MathlibExt.Dynamics.OrnsteinWeissWanted.Dynamics.IsFreeAction, MathlibExt.Dynamics.OrnsteinWeissWanted.Dynamics.boxShape, MathlibExt.Dynamics.OrnsteinWeissWanted.Dynamics.ornstein_weiss_rokhlin, MathlibExt.Dynamics.RokhlinLemmaWanted.Dynamics.IsAperiodic, MathlibExt.Dynamics.RokhlinLemmaWanted.Dynamics.towerFloor, MathlibExt.Dynamics.RokhlinLemmaWanted.Dynamics.towerUnion, MathlibExt.Dynamics.RokhlinLemmaWanted.Dynamics.IsRokhlinTower, MathlibExt.Dynamics.RokhlinLemmaWanted.Dynamics.rokhlin_lemma
statement: formalized
---

# Rokhlin lemma

8 results, 6 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/rokhlin-lemma/index.html).

## Free $\mathbb{Z}^d$-action

Let $d$ be a natural number, let $\mu$ be a measure on a
measurable space $\Omega$, and let $T$ assign to each $v \in \mathbb{Z}^d$ a map
$T_v \colon \Omega \to \Omega$. Then $T$ is free (in the Ornstein–Weiss sense) with respect to
$\mu$ if, for every nonzero $v \in \mathbb{Z}^d$, the set of points $x \in \Omega$ with
$T_v(x) = x$ has $\mu$-measure zero.

Formalized by `MathlibExt.Dynamics.OrnsteinWeissWanted.Dynamics.IsFreeAction`, a definition declared in [WantedExt/Dynamics/OrnsteinWeissWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/OrnsteinWeissWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/rokhlin-lemma/index.html#is-free-action).

## Integer box

For natural numbers $d$ and $N$, the integer box $[0, N)^d$ is the finite set
of vectors $v \in \mathbb{Z}^d$ with $0 \le v_i < N$ for every coordinate $i$.

Formalized by `MathlibExt.Dynamics.OrnsteinWeissWanted.Dynamics.boxShape`, a definition declared in [WantedExt/Dynamics/OrnsteinWeissWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/OrnsteinWeissWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/rokhlin-lemma/index.html#box-shape).

## Ornstein–Weiss Rokhlin lemma for $\mathbb{Z}^d$-actions

Let $d \ge 1$, let $\Omega$ be a
standard Borel space with a probability measure $\mu$, and let $T$ assign to each
$v \in \mathbb{Z}^d$ a map $T_v \colon \Omega \to \Omega$ such that $T_0$ is the identity,
$T_{u + v} = T_u \circ T_v$ for all $u, v \in \mathbb{Z}^d$, every $T_v$ is measure preserving
for $\mu$, and the action is free (for every $v \ne 0$ the set of fixed points of $T_v$ has
$\mu$-measure zero). Then for every integer $N \ge 1$ and every $\varepsilon \in (0, \infty]$
there is a measurable set $B \subseteq \Omega$ such that the images $T_v(B)$, for $v$ in the
integer box $[0, N)^d$, are pairwise disjoint and their union has measure at least
$1 - \varepsilon$.

## Sources

- D. S. Ornstein and B. Weiss, *Entropy and isomorphism theorems for actions of amenable groups*, J. Anal. Math. 48 (1987), 1-141 — Theorem 5.2 establishes the multidimensional (and amenable-group) Rokhlin lemma. Listed as §109 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). No formalization found in any major prover. Problem `ornstein_weiss_rokhlin` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Dynamics.OrnsteinWeissWanted.Dynamics.ornstein_weiss_rokhlin` is written with `theorem_wanted` in [WantedExt/Dynamics/OrnsteinWeissWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/OrnsteinWeissWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/rokhlin-lemma/index.html#ornstein-weiss-rokhlin).

## Aperiodic transformation

Let $\mu$ be a measure on a measurable space $\Omega$. A map
$T : \Omega \to \Omega$ is aperiodic with respect to $\mu$ if the set of periodic points of $T$,
the points $x$ with $T^k(x) = x$ for some $k \ge 1$, where $T^k$ is the $k$-fold iterate of $T$,
has (outer) $\mu$-measure zero. Equivalently, for $\mu$-almost every $x$, no positive iterate of
$T$ fixes $x$.

Formalized by `MathlibExt.Dynamics.RokhlinLemmaWanted.Dynamics.IsAperiodic`, a definition declared in [WantedExt/Dynamics/RokhlinLemmaWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/RokhlinLemmaWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/rokhlin-lemma/index.html#is-aperiodic).

## Floor of a Rokhlin tower

For a map $T : \Omega \to \Omega$, a set
$B \subseteq \Omega$ and $k \in \mathbb{N}$, the level-$k$ floor with base $B$ is the image
$T^k(B)$ of $B$ under the $k$-fold iterate $T^k$ of $T$; the level-$0$ floor is $B$.

Formalized by `MathlibExt.Dynamics.RokhlinLemmaWanted.Dynamics.towerFloor`, a definition declared in [WantedExt/Dynamics/RokhlinLemmaWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/RokhlinLemmaWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/rokhlin-lemma/index.html#tower-floor).

## Union of a Rokhlin tower

For a map $T : \Omega \to \Omega$, a set
$B \subseteq \Omega$ and $n \in \mathbb{N}$, the union of the tower with base $B$ and height $n$
is the set $\bigcup_{k=0}^{n-1} T^k(B)$ of its floors $B, T(B), \dots, T^{n-1}(B)$, where
$T^k(B)$ is the image of $B$ under the $k$-fold iterate of $T$. It is empty when $n = 0$, and
no disjointness of the floors is required.

Formalized by `MathlibExt.Dynamics.RokhlinLemmaWanted.Dynamics.towerUnion`, a definition declared in [WantedExt/Dynamics/RokhlinLemmaWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/RokhlinLemmaWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/rokhlin-lemma/index.html#tower-union).

## Rokhlin tower

Let $\Omega$ be a measurable space, $T : \Omega \to \Omega$ a map and
$n \in \mathbb{N}$. A set $B \subseteq \Omega$ is the base of a Rokhlin tower of height $n$
for $T$ if $B$ is measurable and the floors $B, T(B), \dots, T^{n-1}(B)$ are pairwise
disjoint, that is, $T^i(B) \cap T^j(B) = \emptyset$ for all $i \ne j$ with $i, j < n$; here
$T^k(B)$ is the image of $B$ under the $k$-fold iterate of $T$.

Only the base is required to be measurable. For a non-invertible $T$, the floors need not be
measurable, so evaluating a measure on their union uses its outer measure.

Formalized by `MathlibExt.Dynamics.RokhlinLemmaWanted.Dynamics.IsRokhlinTower`, a definition declared in [WantedExt/Dynamics/RokhlinLemmaWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/RokhlinLemmaWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/rokhlin-lemma/index.html#is-rokhlin-tower).

## Rokhlin lemma for non-invertible maps

Let $\Omega$ be a standard Borel space with a
probability measure $\mu$, and let $T : \Omega \to \Omega$ be a measure-preserving map that is
aperiodic with respect to $\mu$. Then for every integer $n \ge 1$ and every
$\varepsilon \in (0, \infty]$ there is a measurable set $B \subseteq \Omega$ such that the
floors $B, T(B), \dots, T^{n-1}(B)$ are pairwise disjoint, where $T^k(B)$ is the image of $B$
under the $k$-fold iterate of $T$, and their union $\bigcup_{k=0}^{n-1} T^k(B)$ has outer
$\mu$-measure at least $1 - \varepsilon$ (truncated subtraction, so the bound is $0$ when
$\varepsilon \ge 1$). No invertibility of $T$ is assumed.

## Sources

- V. A. Rokhlin, *A general measure-preserving transformation is not mixing*, Doklady Akademii Nauk SSSR 60 (1948), 349-351 (original Russian; English translation later); S. Kakutani, *Induced measure-preserving transformations*, Proc. Imp. Acad. Tokyo 19 (1943), 635-641 (independent discovery); S.-M. Heinemann and O. Schmitt, *Rokhlin's lemma for non-invertible maps*, Dynam. Systems Appl. 10 (2001), no. 2, 201-213. The classical form is listed as §109 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `rokhlin_lemma` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Dynamics.RokhlinLemmaWanted.Dynamics.rokhlin_lemma` is written with `theorem_wanted` in [WantedExt/Dynamics/RokhlinLemmaWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/RokhlinLemmaWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/rokhlin-lemma/index.html#rokhlin-lemma).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rokhlin lemma](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/rokhlin-lemma/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Dynamics/ergodic-theory/rokhlin-lemma)
