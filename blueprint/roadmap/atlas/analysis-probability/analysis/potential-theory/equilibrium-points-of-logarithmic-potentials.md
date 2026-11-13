---
declaration: section
origin: cited
lean: MathlibExt.Analysis.LogarithmicPotentialEquilibriumFreeWanted.ChargeSeq, MathlibExt.Analysis.LogarithmicPotentialEquilibriumFreeWanted.PointsDistinct, MathlibExt.Analysis.LogarithmicPotentialEquilibriumFreeWanted.IsSummable, MathlibExt.Analysis.LogarithmicPotentialEquilibriumFreeWanted.FieldSum, MathlibExt.Analysis.LogarithmicPotentialEquilibriumFreeWanted.conjecture, MathlibExt.Analysis.LogarithmicPotentialEquilibriumFreeWanted.conjecture_refuted
statement: formalized
---

# Equilibrium points of logarithmic potentials

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/equilibrium-points-of-logarithmic-potentials/index.html).

## Charge sequences

A charge sequence is an arbitrary sequence $(z_n)_{n \in \mathbb{N}}$ of
complex numbers, read as the positions of the charges.

Formalized by `MathlibExt.Analysis.LogarithmicPotentialEquilibriumFreeWanted.ChargeSeq`, an abbreviation declared in [WantedExt/Analysis/LogarithmicPotentialEquilibriumFreeWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/LogarithmicPotentialEquilibriumFreeWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/equilibrium-points-of-logarithmic-potentials/index.html#charge-seq).

## Distinct charge positions

A charge sequence $(z_n)$ has distinct positions when its terms
are pairwise distinct: $z_m \neq z_n$ whenever $m \neq n$.

Formalized by `MathlibExt.Analysis.LogarithmicPotentialEquilibriumFreeWanted.PointsDistinct`, a definition declared in [WantedExt/Analysis/LogarithmicPotentialEquilibriumFreeWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/LogarithmicPotentialEquilibriumFreeWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/equilibrium-points-of-logarithmic-potentials/index.html#points-distinct).

## Summable charge sequences

A charge sequence $(z_n)$ is summable when $z_n \neq 0$ for every
$n$ and $\sum_n 1/|z_n| < \infty$.

Formalized by `MathlibExt.Analysis.LogarithmicPotentialEquilibriumFreeWanted.IsSummable`, a definition declared in [WantedExt/Analysis/LogarithmicPotentialEquilibriumFreeWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/LogarithmicPotentialEquilibriumFreeWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/equilibrium-points-of-logarithmic-potentials/index.html#is-summable).

## Field of a charge sequence

For a charge sequence $(z_n)$ and a point $z \in \mathbb{C}$,
the field at $z$ is the sum $\sum_n 1/(z - z_n)$, where a term with $z_n = z$ counts as $0$ and the
sum is taken to be $0$ when the family $\bigl(1/(z - z_n)\bigr)_n$ is not summable.

The sum converges absolutely when $z_n \neq 0$ for every $n$ and $\sum_n 1/|z_n| < \infty$.

Formalized by `MathlibExt.Analysis.LogarithmicPotentialEquilibriumFreeWanted.FieldSum`, a definition declared in [WantedExt/Analysis/LogarithmicPotentialEquilibriumFreeWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/LogarithmicPotentialEquilibriumFreeWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/equilibrium-points-of-logarithmic-potentials/index.html#field-sum).

## Equilibrium-free logarithmic potential conjecture

The conjecture states that there exists
a charge sequence $(z_n)$ whose positions are pairwise distinct, which is summable ($z_n \neq 0$
for every $n$ and $\sum_n 1/|z_n| < \infty$), and whose field $\sum_n 1/(z - z_n)$ is nonzero at
every point $z \in \mathbb{C}$ that is not one of the $z_n$.

## Sources

- record AMR-022-7078 (Problem 7.78, Rubel).

Formalized by `MathlibExt.Analysis.LogarithmicPotentialEquilibriumFreeWanted.conjecture`, a definition declared in [WantedExt/Analysis/LogarithmicPotentialEquilibriumFreeWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/LogarithmicPotentialEquilibriumFreeWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/equilibrium-points-of-logarithmic-potentials/index.html#conjecture).

## The equilibrium-free logarithmic potential conjecture is false

There is no charge sequence
$(z_n)$ whose positions are pairwise distinct, which is summable ($z_n \neq 0$ for every $n$ and
$\sum_n 1/|z_n| < \infty$), and whose field $\sum_n 1/(z - z_n)$ is nonzero at every point
$z \in \mathbb{C}$ that is not one of the $z_n$.

Clunie, Eremenko and Rossi proved more: under these hypotheses the field has infinitely many
zeros.

## Sources

- J. Clunie, A. Eremenko and J. Rossi, On equilibrium points of logarithmic and Newtonian potentials, J. London Math. Soc. (2) 47 (1993), 309-320.

Stated but not proved: `MathlibExt.Analysis.LogarithmicPotentialEquilibriumFreeWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/LogarithmicPotentialEquilibriumFreeWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/LogarithmicPotentialEquilibriumFreeWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/equilibrium-points-of-logarithmic-potentials/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Equilibrium points of logarithmic potentials](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/equilibrium-points-of-logarithmic-potentials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/potential-theory/equilibrium-points-of-logarithmic-potentials)
