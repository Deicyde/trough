---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.InvariantRingPoincareSeriesKourovka12Problem36Wanted.linSubst, MathlibExt.GroupTheory.InvariantRingPoincareSeriesKourovka12Problem36Wanted.invariantComponent, MathlibExt.GroupTheory.InvariantRingPoincareSeriesKourovka12Problem36Wanted.poincareSeries, MathlibExt.GroupTheory.InvariantRingPoincareSeriesKourovka12Problem36Wanted.pointwiseStabilizer, MathlibExt.GroupTheory.InvariantRingPoincareSeriesKourovka12Problem36Wanted.hyperplaneTerm, MathlibExt.GroupTheory.InvariantRingPoincareSeriesKourovka12Problem36Wanted.hyperplaneSum, MathlibExt.GroupTheory.InvariantRingPoincareSeriesKourovka12Problem36Wanted.poincareSeriesSecondCoefficient, MathlibExt.GroupTheory.InvariantRingPoincareSeriesKourovka12Problem36Wanted.poincareSeriesSecondCoefficient_holds
statement: formalized
---

# Poincaré series of modular invariant rings

8 results, 7 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/invariant-theory/poincar-series-of-modular-invariant-rings/index.html).

## Linear substitution by a matrix

For natural numbers $p$ and $n$ and an $n \times n$ matrix
$g$ over $\mathbb{Z}/p\mathbb{Z}$, the linear substitution by $g$ is the
$\mathbb{Z}/p\mathbb{Z}$-algebra endomorphism of the polynomial ring
$(\mathbb{Z}/p\mathbb{Z})[x_0, \dots, x_{n-1}]$ that sends each variable $x_i$ to
$\sum_j g_{ij} x_j$. Viewing polynomials as functions on $V = (\mathbb{Z}/p\mathbb{Z})^n$, it sends
$f$ to the function $x \mapsto f(gx)$.

Formalized by `MathlibExt.GroupTheory.InvariantRingPoincareSeriesKourovka12Problem36Wanted.linSubst`, a definition declared in [WantedExt/GroupTheory/InvariantRingPoincareSeriesKourovka12Problem36Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/InvariantRingPoincareSeriesKourovka12Problem36Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/invariant-theory/poincar-series-of-modular-invariant-rings/index.html#lin-subst).

## Homogeneous component of the invariant ring

For natural numbers $p$ and $n$, a subgroup
$G$ of $\mathrm{GL}_n(\mathbb{Z}/p\mathbb{Z})$ and $m \in \mathbb{N}$, the degree-$m$ component
$T_m$ of the invariant ring $T$ of $G$ is the $\mathbb{Z}/p\mathbb{Z}$-submodule of the polynomial
ring $(\mathbb{Z}/p\mathbb{Z})[x_0, \dots, x_{n-1}]$ consisting of the homogeneous polynomials $f$
of degree $m$ that are fixed by the linear substitution $x_i \mapsto \sum_j g_{ij} x_j$ of every
$g \in G$, that is, with $f(gx) = f(x)$ as polynomials for all $g \in G$, where
$x = (x_0, \dots, x_{n-1})$ is the column vector of variables.

Formalized by `MathlibExt.GroupTheory.InvariantRingPoincareSeriesKourovka12Problem36Wanted.invariantComponent`, a definition declared in [WantedExt/GroupTheory/InvariantRingPoincareSeriesKourovka12Problem36Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/InvariantRingPoincareSeriesKourovka12Problem36Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/invariant-theory/poincar-series-of-modular-invariant-rings/index.html#invariant-component).

## Poincaré series of the invariant ring

For natural numbers $p$ and $n$ and a subgroup $G$
of $\mathrm{GL}_n(\mathbb{Z}/p\mathbb{Z})$, the Poincaré series of the invariant ring $T$ of $G$
is the formal power series $P(t) = \sum_{m \ge 0} b_m t^m$ over $\mathbb{Q}$, where $b_m$ is the
rank over $\mathbb{Z}/p\mathbb{Z}$ (the dimension, when $p$ is prime) of the degree-$m$
homogeneous component $T_m$ of $T$.

Formalized by `MathlibExt.GroupTheory.InvariantRingPoincareSeriesKourovka12Problem36Wanted.poincareSeries`, a definition declared in [WantedExt/GroupTheory/InvariantRingPoincareSeriesKourovka12Problem36Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/InvariantRingPoincareSeriesKourovka12Problem36Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/invariant-theory/poincar-series-of-modular-invariant-rings/index.html#poincare-series).

## Pointwise stabilizer

For natural numbers $p$ and $n$, a subgroup $G$ of
$\mathrm{GL}_n(\mathbb{Z}/p\mathbb{Z})$ and a submodule $W$ of $V = (\mathbb{Z}/p\mathbb{Z})^n$,
the pointwise stabilizer $G_W$ of $W$ in $G$ is the set of all $g \in G$ with $g w = w$ for every
$w \in W$, where $g$ acts on column vectors by matrix multiplication.

Formalized by `MathlibExt.GroupTheory.InvariantRingPoincareSeriesKourovka12Problem36Wanted.pointwiseStabilizer`, a definition declared in [WantedExt/GroupTheory/InvariantRingPoincareSeriesKourovka12Problem36Wanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/InvariantRingPoincareSeriesKourovka12Problem36Wanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/invariant-theory/poincar-series-of-modular-invariant-rings/index.html#pointwise-stabilizer).

## Hyperplane term

For natural numbers $p$ and $n$, a subgroup $G$ of
$\mathrm{GL}_n(\mathbb{Z}/p\mathbb{Z})$ and a submodule $W$ of $V = (\mathbb{Z}/p\mathbb{Z})^n$, let
$N$ be the number of elements of the pointwise stabilizer $G_W$ of $W$ in $G$ (taken to be $0$
if $G_W$ is infinite), let $\alpha_W$ be the exponent of $p$ in the prime factorization of $N$
(which is $0$ unless $p$ is prime and $N \ne 0$), and let $s_W = N / p^{\alpha_W}$, so that
$N = p^{\alpha_W} s_W$ and $p \nmid s_W$ when $p$ is prime and $N \ne 0$. The hyperplane term of
$W$ is the rational number $(p - 1) \alpha_W + s_W - 1$.

Formalized by `MathlibExt.GroupTheory.InvariantRingPoincareSeriesKourovka12Problem36Wanted.hyperplaneTerm`, a definition declared in [WantedExt/GroupTheory/InvariantRingPoincareSeriesKourovka12Problem36Wanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/InvariantRingPoincareSeriesKourovka12Problem36Wanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/invariant-theory/poincar-series-of-modular-invariant-rings/index.html#hyperplane-term).

## Hyperplane sum

For natural numbers $p$ and $n$ and a subgroup $G$ of
$\mathrm{GL}_n(\mathbb{Z}/p\mathbb{Z})$, the hyperplane sum of $G$ is the rational number
$r = \sum_W ((p - 1) \alpha_W + s_W - 1)$, where $W$ runs over the maximal proper submodules
of $V = (\mathbb{Z}/p\mathbb{Z})^n$ (the hyperplanes of $V$ when $p$ is prime) and
$(p - 1) \alpha_W + s_W - 1$ is the hyperplane term of $W$: here $N_W$ is the number of elements
of the pointwise stabilizer $G_W$ of $W$ in $G$ (taken to be $0$ if $G_W$ is infinite),
$\alpha_W$ is the exponent of $p$ in the prime factorization of $N_W$ (which is $0$ unless $p$
is prime and $N_W \ne 0$), and $s_W = N_W / p^{\alpha_W}$, so that $N_W = p^{\alpha_W} s_W$.
The sum is defined to be $0$ if infinitely many of its terms are nonzero, which can happen only
for $p = 0$.

Formalized by `MathlibExt.GroupTheory.InvariantRingPoincareSeriesKourovka12Problem36Wanted.hyperplaneSum`, a definition declared in [WantedExt/GroupTheory/InvariantRingPoincareSeriesKourovka12Problem36Wanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/InvariantRingPoincareSeriesKourovka12Problem36Wanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/invariant-theory/poincar-series-of-modular-invariant-rings/index.html#hyperplane-sum).

## Carlisle–Kropholler conjecture on the second Laurent coefficient (Kourovka 12.36)

The
statement that for every prime $p$, every $n \in \mathbb{N}$ and every subgroup $G$ of
$\mathrm{GL}_n(\mathbb{F}_p)$, with $P(t)$ the Poincaré series of the invariant ring of $G$ and
$r$ the hyperplane sum of $G$, there are polynomials $A, B \in \mathbb{Q}[t]$ with $B(1) \ne 0$
and $B(t) (1 - t)^n P(t) = A(t)$ in $\mathbb{Q}[[t]]$ such that

$$\frac{A(1) B'(1) - A'(1) B(1)}{B(1)^2} = \frac{r}{2 |G|}.$$

Here $(1 - t)^n P(t) = A(t) / B(t) = a_{-n} + a_{-n+1} (1 - t) + \cdots$, where
$P(t) = \sum_{i \ge -n} a_i (1 - t)^i$ is the Laurent expansion of $P$ at $t = 1$, so the left
side is $a_{-n+1} = -(A / B)'(1)$, and the conjecture says $a_{-n+1} = r / (2 |G|)$.

Formalized by `MathlibExt.GroupTheory.InvariantRingPoincareSeriesKourovka12Problem36Wanted.poincareSeriesSecondCoefficient`, a definition declared in [WantedExt/GroupTheory/InvariantRingPoincareSeriesKourovka12Problem36Wanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/InvariantRingPoincareSeriesKourovka12Problem36Wanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/invariant-theory/poincar-series-of-modular-invariant-rings/index.html#poincare-series-second-coefficient).

## Benson–Crawley-Boevey hyperplane formula (Kourovka 12.36)

For every prime $p$, every
$n \in \mathbb{N}$ and every subgroup $G$ of $\mathrm{GL}_n(\mathbb{F}_p)$, with $P(t)$ the
Poincaré series of the invariant ring of $G$ and $r$ the hyperplane sum of $G$, there are
polynomials $A, B \in \mathbb{Q}[t]$ with $B(1) \ne 0$ and $B(t) (1 - t)^n P(t) = A(t)$ in
$\mathbb{Q}[[t]]$ such that

$$\frac{A(1) B'(1) - A'(1) B(1)}{B(1)^2} = \frac{r}{2 |G|}.$$

That is, the Carlisle–Kropholler conjecture on the second Laurent coefficient holds: the
coefficient $a_{-n+1}$ in the expansion $P(t) = \sum_{i \ge -n} a_i (1 - t)^i$ equals
$r / (2 |G|)$.

Resolved true: the Kourovka Archive records the conjecture as proved by Benson and Crawley-Boevey
(Bull. London Math. Soc. 27 (1995)), with a second proof by Neeman (Comment. Math. Helv. 70 (1995))
based on the Grothendieck-Riemann-Roch theorem. Source: E. I. Khukhro and V. D. Mazurov (eds.),
Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026),
Archive of Solved Problems, Problem 12.36 (D. Carlisle, P. H. Kropholler); resolution: D. J. Benson
and W. W. Crawley-Boevey, Bull. London Math. Soc. 27 (1995), no. 5, 435-440; A. Neeman, Comment.
Math. Helv. 70 (1995), no. 3, 339-349, Kourovka Archive, Problem 12.36: the conjecture is proved.

Stated but not proved: `MathlibExt.GroupTheory.InvariantRingPoincareSeriesKourovka12Problem36Wanted.poincareSeriesSecondCoefficient_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/InvariantRingPoincareSeriesKourovka12Problem36Wanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/InvariantRingPoincareSeriesKourovka12Problem36Wanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/invariant-theory/poincar-series-of-modular-invariant-rings/index.html#poincare-series-second-coefficient-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Poincaré series of modular invariant rings](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/invariant-theory/poincar-series-of-modular-invariant-rings/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/invariant-theory/poincar-series-of-modular-invariant-rings)
