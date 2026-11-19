---
declaration: module
origin: cited
lean: Ray
statement: formalized
proof: formalized
---

# Rendering

[girving/ray](https://github.com/girving/ray) at commit [53f17081](https://github.com/girving/ray/tree/53f17081c44a88a16e0d2e1876451beb38653bed), 2026-10-18.

> The goal of this repository is to formalize standard results about the Mandelbrot set in Lean. The main result is that [the Mandelbrot set and its complement are connected](http://github.com/girving/ray/blob/main/Ray/Dynamics/Mandelbrot.lean#L37), by exhibiting the analytic Böttcher homeomorphism from the exterior of the Mandelbrot set to the exterior of the closed unit disk. But I'm also using it to learn Lean generally, which means detours along the way.

*Quoted from [README.md](https://github.com/girving/ray/blob/53f17081c44a88a16e0d2e1876451beb38653bed/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Radius of convergence](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/radius-of-convergence.md)
- [Complex roots of unity](../../../undergraduate/group-theory/abelian-group/complex-roots-of-unity.md)
- [Weierstrass trigonometric approximation theorem](../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/weierstrass-trigonometric-approximation-theorem.md)
- [Stream](../../data-structures/list-like-structures/stream.md)
- [Derivative of a composition of functions (Single Variable Real Analysis)](../../../undergraduate/single-variable-real-analysis/differentiability/derivative-of-a-composition-of-functions.md)
- [Schwarz lemma](../../analysis/complex-analysis/schwarz-lemma.md)
- [Change of variables formula](../../analysis/measures-and-integral-calculus/part-02/change-of-variables-formula.md)
- [Cluster point](../../topology/general-topology/part-01/cluster-point.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`Ray`](https://github.com/girving/ray/blob/53f17081c44a88a16e0d2e1876451beb38653bed/Ray.lean): the root of a Lean library its lakefile builds, not a theorem. No file it imports, directly or not (107 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 111 .lean files; its Lean libraries `Ray` hold 111, declaring 2,186 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/girving/ray/blob/53f17081c44a88a16e0d2e1876451beb38653bed/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).

## Placement

Of its imports of Mathlib modules in an overview area, 60 of 564 are in Geometry, 4.5 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Geometry (60 of 564 imports, 4.5×), Analysis (376 of 564 imports, 2.5×). *Proof depends on* names 8 of the 73 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [girving/ray at 53f17081](https://github.com/girving/ray/tree/53f17081c44a88a16e0d2e1876451beb38653bed)
