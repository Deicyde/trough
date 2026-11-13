---
declaration: section
origin: cited
lean: Set.HasHausdorffCodimAtLeast, Set.hasHausdorffCodimAtLeast_empty, Set.HasHausdorffCodimAtLeast.mono, Set.HasHausdorffCodimAtLeast.eq_empty_of_lt, Set.hasHausdorffCodimAtLeast_of_dimH_le, Set.hasHausdorffCodimAtLeast_iff
statement: formalized
proof: formalized
---

# Hausdorff codimension

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/hausdorff-codimension/index.html).

## Lower bound on Hausdorff codimension

Let $S$ be a subset of an extended metric space
and let $n, c$ be natural numbers. The set $S$ has Hausdorff codimension at least $c$ in
dimension $n$ if $S$ is empty or its Hausdorff dimension satisfies $\dim_H S + c \le n$, the
inequality being taken in $[0, \infty]$.

The empty-set case plays the role of the convention $\dim_H \emptyset = -\infty$.

Formalized by `Set.HasHausdorffCodimAtLeast`, a definition declared in [MathlibExt/Topology/MetricSpace/HausdorffCodimension.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/MetricSpace/HausdorffCodimension.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/hausdorff-codimension/index.html#has-hausdorff-codim-at-least).

## The empty set has every codimension

In an extended metric space, the empty set has
Hausdorff codimension at least $c$ in dimension $n$ for all natural numbers $n$ and $c$.

Formalized by `Set.hasHausdorffCodimAtLeast_empty`, a theorem declared in [MathlibExt/Topology/MetricSpace/HausdorffCodimension.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/MetricSpace/HausdorffCodimension.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/hausdorff-codimension/index.html#has-hausdorff-codim-at-least-empty).

## Subsets inherit a codimension bound

Let $T \subseteq S$ be subsets of an extended
metric space and let $n, c$ be natural numbers. If $S$ has Hausdorff codimension at least $c$
in dimension $n$, then so does $T$.

Formalized by `Set.HasHausdorffCodimAtLeast.mono`, a theorem declared in [MathlibExt/Topology/MetricSpace/HausdorffCodimension.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/MetricSpace/HausdorffCodimension.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/hausdorff-codimension/index.html#mono).

## Sets of codimension larger than the dimension are empty

Let $S$ be a subset of an
extended metric space and let $n < c$ be natural numbers. If $S$ has Hausdorff codimension at
least $c$ in dimension $n$, then $S$ is empty.

Formalized by `Set.HasHausdorffCodimAtLeast.eq_empty_of_lt`, a theorem declared in [MathlibExt/Topology/MetricSpace/HausdorffCodimension.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/MetricSpace/HausdorffCodimension.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/hausdorff-codimension/index.html#eq-empty-of-lt).

## A dimension bound gives a codimension bound

Let $S$ be a subset of an extended metric
space and let $c \le n$ be natural numbers. If the Hausdorff dimension of $S$ satisfies
$\dim_H S \le n - c$, then $S$ has Hausdorff codimension at least $c$ in dimension $n$.

Formalized by `Set.hasHausdorffCodimAtLeast_of_dimH_le`, a theorem declared in [MathlibExt/Topology/MetricSpace/HausdorffCodimension.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/MetricSpace/HausdorffCodimension.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/hausdorff-codimension/index.html#has-hausdorff-codim-at-least-of-dim-h-le).

## Characterization of Hausdorff codimension

Let $S$ be a subset of an extended metric
space and let $n, c$ be natural numbers. Then $S$ has Hausdorff codimension at least $c$ in
dimension $n$ if and only if either $S$ is empty, or both $c \le n$ and the Hausdorff
dimension of $S$ satisfies $\dim_H S \le n - c$.

Formalized by `Set.hasHausdorffCodimAtLeast_iff`, a theorem declared in [MathlibExt/Topology/MetricSpace/HausdorffCodimension.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/MetricSpace/HausdorffCodimension.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/hausdorff-codimension/index.html#has-hausdorff-codim-at-least-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hausdorff codimension](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/hausdorff-codimension/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/MeasureTheory/geometric-measure-theory/hausdorff-codimension)
