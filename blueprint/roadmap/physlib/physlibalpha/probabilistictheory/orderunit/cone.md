---
declaration: module
origin: cited
lean: PhyslibAlpha.ProbabilisticTheory.PosCone, PhyslibAlpha.ProbabilisticTheory.PosCone.instModule, PhyslibAlpha.ProbabilisticTheory.PosCone.isClosed, PhyslibAlpha.ProbabilisticTheory.PosCone.instOne, PhyslibAlpha.ProbabilisticTheory.PosCone.coe_one
statement: formalized
proof: formalized
---

# Ordered positive cones (PhyslibAlpha)

The module `PhyslibAlpha.ProbabilisticTheory.OrderUnit.Cone`, [PhyslibAlpha/ProbabilisticTheory/OrderUnit/Cone.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Cone.lean): 5 declarations, 4 with a docstring.

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

## iv. References

## A. The positive cone

**`PhyslibAlpha.ProbabilisticTheory.PosCone`**, an abbrev, [line 51](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Cone.lean#L51).

> The positive pointed cone of an ordered real module.

```lean
abbrev PosCone (E : Type*) [OrderedVectorSpace E] : PointedCone ℝ E
```

**`PhyslibAlpha.ProbabilisticTheory.PosCone.instModule`**, an instance, [line 61](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Cone.lean#L61).

> The positive cone carries a nonnegative-real scalar action.

```lean
instance instModule : Module ℝ≥0 (PosCone E)
```

## B. Topological closedness

**`PhyslibAlpha.ProbabilisticTheory.PosCone.isClosed`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Cone.lean#L79).

> The positive cone is closed in the topology induced by the order-unit norm.

```lean
lemma isClosed : IsClosed (PosCone E : Set E)
```

## C. The order unit

**`PhyslibAlpha.ProbabilisticTheory.PosCone.instOne`**, an instance, [line 96](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Cone.lean#L96).

> The order unit, regarded as a point of the positive cone.

```lean
instance instOne : One (PosCone E)
```

**`PhyslibAlpha.ProbabilisticTheory.PosCone.coe_one`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Cone.lean#L99).

```lean
lemma coe_one : ((1 : PosCone E) : E) = (1 : E)
```

## Depends on

- [Archimedean order-unit spaces (PhyslibAlpha)](archimedean.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/OrderUnit/Cone.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Cone.lean)
