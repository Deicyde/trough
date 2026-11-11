---
declaration: section
origin: cited
lean: MathlibExt.Topology.Continuum.HahnMazurkiewiczWanted.hahnMazurkiewicz, MathlibExt.Topology.Continuum.PeanoCurveWanted.peano_curve_exists, MathlibExt.Topology.ScottishBook46Wanted.sphere_in_banach_space_is_unicoherent
statement: formalized
---

# Continuum theory and infinite-dimensional topology: its own results

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/index.html).

Compact connected spaces, Peano continua and space-filling curves, absolute retracts, hyperspaces, the Hilbert cube and fixed-point properties.

## Hahn–Mazurkiewicz theorem

Let $X$ be a nonempty topological space that is compact,
connected, locally connected, Hausdorff and second countable. Then there is a continuous
surjection from the closed unit interval $[0,1]$ onto $X$.

## Sources

- H. Hahn, Jahresber. DMV 23 (1914); S. Mazurkiewicz, Fund. Math. 1 (1920) (announcement 1913); Willard, General Topology; Munkres, Topology 2nd ed., second-countable Hausdorff compact formulation.

Formalized by `MathlibExt.Topology.Continuum.HahnMazurkiewiczWanted.hahnMazurkiewicz`, a theorem declared in [MathlibExt/Topology/Continuum/HahnMazurkiewicz.lean, line 1279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Continuum/HahnMazurkiewicz.lean#L1279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/index.html#hahn-mazurkiewicz).

## Peano's space-filling curve

There exists a continuous surjection from the closed unit interval to its square.

## Sources

- G. Peano, "Sur une courbe, qui remplit toute une aire plane", Mathematische Annalen 36 (1890), 157-160.

Formalized by `MathlibExt.Topology.Continuum.PeanoCurveWanted.peano_curve_exists`, a theorem declared in [MathlibExt/Topology/Continuum/PeanoCurve.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Continuum/PeanoCurve.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/index.html#peano-curve-exists).

## Unit spheres of infinite-dimensional Banach spaces are unicoherent

Let $E$ be a real
Banach space that is not finite-dimensional, and let $S = \{x \in E : \|x\| = 1\}$ be its unit
sphere. If $A$ and $B$ are closed connected subsets of $S$ with $A \cup B = S$, then $A \cap B$ is
connected. Here connected sets are nonempty by definition.

This answers Banach's Problem 46 of the Scottish Book: is the sphere in a space of type (B)
uni-coherent, that is, whenever it is the union of two continua $A$ and $B$, is $A \cap B$
connected? Continua are read as closed connected sets, the meaning of uni-coherence for
non-compact spaces: in infinite dimensions the sphere is not compact, so two compact sets could
not cover it. The statement is restricted to infinite-dimensional spaces; in dimension $1$ the
sphere is two points and in dimension $2$ it is a circle, and neither is uni-coherent (two
semicircles cover the circle and meet in two points). In infinite dimensions the sphere is an
absolute retract, and the affirmative answer follows from the theorems of Borsuk and Eilenberg
recorded in the addendum.

## Sources

- S. Banach, Problem 46 of the Scottish Book; addendum in the Scottish Book citing Borsuk and Eilenberg, Fund. Math. 26, p. 61; see the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015).

Stated but not proved: `MathlibExt.Topology.ScottishBook46Wanted.sphere_in_banach_space_is_unicoherent` is written with `theorem_wanted` in [WantedExt/Topology/ScottishBook46Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ScottishBook46Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/index.html#sphere-in-banach-space-is-unicoherent).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Continuum theory and infinite-dimensional topology](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Topology/continua-infinite-dimensional)
