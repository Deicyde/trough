---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.BrowderKirkWanted.browderGoehdeKirk_fixedPoint, MathlibExt.Topology.KirkNormalStructureWanted.Topology.KirkNormalStructure.metricDiameter, MathlibExt.Topology.KirkNormalStructureWanted.Topology.KirkNormalStructure.pointRadiusIn, MathlibExt.Topology.KirkNormalStructureWanted.Topology.KirkNormalStructure.IsDiametralPoint, MathlibExt.Topology.KirkNormalStructureWanted.Topology.KirkNormalStructure.HasNormalStructure, MathlibExt.Topology.KirkNormalStructureWanted.Topology.KirkNormalStructure.IsNonexpansiveSelfMap, MathlibExt.Topology.KirkNormalStructureWanted.Topology.KirkNormalStructure.kirk_normal_structure
statement: formalized
---

# Browder–Göhde–Kirk fixed-point theorem

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/fixed-point-theory/browder-g-hde-kirk-fixed-point-theorem/index.html).

## Browder–Göhde–Kirk fixed point theorem

Let $E$ be a uniformly convex real Banach space and
let $K \subseteq E$ be a nonempty, closed, bounded, convex set. If a map $f : E \to E$ sends $K$
into $K$ and is nonexpansive on $K$, that is, $\|f(x) - f(y)\| \le \|x - y\|$ for all
$x, y \in K$, then $f$ has a fixed point in $K$: there is $y \in K$ with $f(y) = y$.

## Sources

- F. Browder, Proc. Nat. Acad. Sci. USA 1965, D. Göhde, Math. Ann. 1965, and W. Kirk, Amer. Math. Monthly 1965-66, fixed-point theorem for nonexpansive mappings in uniformly convex Banach spaces; textbook Goebel and Kirk, 1990; Lean states complete uniformly convex real case with `Bornology.IsBounded` convex set.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.BrowderKirkWanted.browderGoehdeKirk_fixedPoint`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/BrowderKirk.lean, line 647](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/BrowderKirk.lean#L647). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/fixed-point-theory/browder-g-hde-kirk-fixed-point-theorem/index.html#browder-goehde-kirk-fixed-point).

## Diameter of a set

The diameter of a set $s$ in a real normed space is the supremum in
$\mathbb{R}$ of the distances $\operatorname{dist}(x, y)$ over all $x, y \in s$; by the convention
for real suprema it is $0$ when $s$ is empty or these distances are unbounded.

Formalized by `MathlibExt.Topology.KirkNormalStructureWanted.Topology.KirkNormalStructure.metricDiameter`, a definition declared in [WantedExt/Topology/KirkNormalStructureWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/KirkNormalStructureWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/fixed-point-theory/browder-g-hde-kirk-fixed-point-theorem/index.html#metric-diameter).

## Radius of a point in a set

The radius of a point $x$ in a set $s$ of a real normed space
is the supremum in $\mathbb{R}$ of the distances $\operatorname{dist}(x, y)$ over all $y \in s$; by
the convention for real suprema it is $0$ when $s$ is empty or these distances are unbounded.

Formalized by `MathlibExt.Topology.KirkNormalStructureWanted.Topology.KirkNormalStructure.pointRadiusIn`, a definition declared in [WantedExt/Topology/KirkNormalStructureWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/KirkNormalStructureWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/fixed-point-theory/browder-g-hde-kirk-fixed-point-theorem/index.html#point-radius-in).

## Diametral point

A point $x$ of a real normed space is diametral in a set $s$
if $x \in s$ and the radius of $x$ in $s$ equals the diameter of $s$.

Formalized by `MathlibExt.Topology.KirkNormalStructureWanted.Topology.KirkNormalStructure.IsDiametralPoint`, a definition declared in [WantedExt/Topology/KirkNormalStructureWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/KirkNormalStructureWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/fixed-point-theory/browder-g-hde-kirk-fixed-point-theorem/index.html#is-diametral-point).

## Normal structure

A set $K$ in a real normed space has normal structure if every convex
subset $H \subseteq K$ with at least two points contains a point that is not diametral in $H$.

Formalized by `MathlibExt.Topology.KirkNormalStructureWanted.Topology.KirkNormalStructure.HasNormalStructure`, a definition declared in [WantedExt/Topology/KirkNormalStructureWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/KirkNormalStructureWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/fixed-point-theory/browder-g-hde-kirk-fixed-point-theorem/index.html#has-normal-structure).

## Nonexpansive self-map

A map $T : K \to K$ from a subset $K$ of a real normed space to
itself is nonexpansive if $\|T(x) - T(y)\| \le \|x - y\|$ for all $x, y \in K$, that is, if $T$
is $1$-Lipschitz for the distance inherited from the space.

Formalized by `MathlibExt.Topology.KirkNormalStructureWanted.Topology.KirkNormalStructure.IsNonexpansiveSelfMap`, a definition declared in [WantedExt/Topology/KirkNormalStructureWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/KirkNormalStructureWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/fixed-point-theory/browder-g-hde-kirk-fixed-point-theorem/index.html#is-nonexpansive-self-map).

## Kirk's fixed-point theorem for sets with normal structure

Let $E$ be a reflexive real
Banach space, meaning that the canonical embedding of $E$ into its double dual is surjective, and
let $K \subseteq E$ be a nonempty, closed, bounded, convex set with normal structure. Then every
nonexpansive self-map $T : K \to K$ has a fixed point.

## Sources

- W. A. Kirk, A fixed point theorem for mappings which do not increase distances, Amer. Math. Monthly 72 (1965). Listed as §228 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Knill, §228. Problem `kirk_normal_structure` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.KirkNormalStructureWanted.Topology.KirkNormalStructure.kirk_normal_structure` is written with `theorem_wanted` in [WantedExt/Topology/KirkNormalStructureWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/KirkNormalStructureWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/fixed-point-theory/browder-g-hde-kirk-fixed-point-theorem/index.html#kirk-normal-structure).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Browder–Göhde–Kirk fixed-point theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/fixed-point-theory/browder-g-hde-kirk-fixed-point-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/fixed-point-theory/browder-g-hde-kirk-fixed-point-theorem)
