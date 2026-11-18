---
declaration: module
origin: cited
lean: ProbabilisticTheory.PosCone, ProbabilisticTheory.PosCone.instModule, ProbabilisticTheory.PosCone.isClosed, ProbabilisticTheory.PosCone.instOne, ProbabilisticTheory.PosCone.coe_one
statement: formalized
proof: formalized
---

# Ordered positive cones

The module `Physlib.ProbabilisticTheory.OrderUnit.Cone`, [Physlib/ProbabilisticTheory/OrderUnit/Cone.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Cone.lean): 5 declarations, 4 with a docstring.

## i. Overview

> `PosCone E` collects the positive elements of `E`. In quantum mechanics, `E` is the real vector
> space of self-adjoint matrices, whose spectra are real. Its positive cone consists exactly of
> those matrices whose spectra are nonnegative.
> These elements form a cone: they are closed under addition and scaling by nonnegative reals.

## ii. Key results

> - `PosCone` : the cone of positive observables, `PointedCone.positive ℝ E`. Its carrier is exactly
>   `{A | 0 ≤ A}` (`PointedCone.mem_positive`) and it is convex (`PointedCone.convex`).
> - `PosCone.isClosed` : the positive cone is closed in the order-unit-norm topology of an
>   Archimedean order-unit space.

## A. The positive cone

**`ProbabilisticTheory.PosCone`**, an abbrev, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Cone.lean#L49).

> The positive pointed cone of an ordered real module.

```lean
abbrev PosCone (E : Type*) [OrderedVectorSpace E] : PointedCone ℝ E
```

**`ProbabilisticTheory.PosCone.instModule`**, an instance, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Cone.lean#L59).

> The positive cone carries a nonnegative-real scalar action.

```lean
instance instModule : Module ℝ≥0 (PosCone E)
```

## B. Topological closedness

**`ProbabilisticTheory.PosCone.isClosed`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Cone.lean#L77).

> The positive cone is closed in the topology induced by the order-unit norm.

```lean
lemma isClosed : IsClosed (PosCone E : Set E)
```

## C. The order unit

**`ProbabilisticTheory.PosCone.instOne`**, an instance, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Cone.lean#L94).

> The order unit, regarded as a point of the positive cone.

```lean
instance instOne : One (PosCone E)
```

**`ProbabilisticTheory.PosCone.coe_one`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Cone.lean#L97).

```lean
lemma coe_one : ((1 : PosCone E) : E) = (1 : E)
```

## Depends on

- [Archimedean order-unit spaces](archimedean.md)

## Sources

- [Physlib/ProbabilisticTheory/OrderUnit/Cone.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Cone.lean)
