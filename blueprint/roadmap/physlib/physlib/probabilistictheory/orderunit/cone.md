---
declaration: module
origin: cited
lean: ProbabilisticTheory.PosCone, ProbabilisticTheory.PosCone.instModule, ProbabilisticTheory.PosCone.isClosed, ProbabilisticTheory.PosCone.coe_nnreal_smul, ProbabilisticTheory.PosCone.instOne, ProbabilisticTheory.PosCone.coe_one, ProbabilisticTheory.PosCone.exists_sub
statement: formalized
proof: formalized
---

# Ordered positive cones (Physlib)

The module `Physlib.ProbabilisticTheory.OrderUnit.Cone`, [Physlib/ProbabilisticTheory/OrderUnit/Cone.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Cone.lean): 7 declarations, 5 with a docstring.

## i. Overview

> `PosCone P` collects the positive observables of `P`. In quantum mechanics, `P.Observables` is
> the real vector space of self-adjoint matrices, whose spectra are real. Its positive cone
> consists exactly of those matrices whose spectra are nonnegative.
> These elements form a cone: they are closed under addition and scaling by nonnegative reals.

## ii. Key results

> - `PosCone` : the cone of positive observables, `PointedCone.positive ℝ P.Observables`. Its
>   carrier is exactly `{A | 0 ≤ A}` (`PointedCone.mem_positive`) and it is convex
>   (`PointedCone.convex`).
> - `PosCone.isClosed` : the positive cone is closed in the order-unit-norm topology of an
>   Archimedean order-unit space.
> - `PosCone.exists_sub` : every observable is a difference of two positive observables.

## A. The positive cone

**`ProbabilisticTheory.PosCone`**, an abbrev, [line 51](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Cone.lean#L51).

> The positive pointed cone of an ordered real module.

```lean
abbrev ProbabilisticTheory.PosCone (P : ProbabilisticTheory) : PointedCone ℝ P.Observables
```

**`ProbabilisticTheory.PosCone.instModule`**, an instance, [line 59](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Cone.lean#L59).

> The positive cone carries a nonnegative-real scalar action.

```lean
instance instModule : Module ℝ≥0 (PosCone P)
```

## B. Topological closedness

**`ProbabilisticTheory.PosCone.isClosed`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Cone.lean#L69).

> The positive cone is closed in the topology induced by the order-unit norm.

```lean
lemma isClosed : IsClosed (PosCone P : Set P.Observables)
```

## C. The order unit

**`ProbabilisticTheory.PosCone.coe_nnreal_smul`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Cone.lean#L78).

```lean
lemma coe_nnreal_smul (t : ℝ≥0) (p : PosCone P) :
    ((t • p : PosCone P) : P.Observables) = (t : ℝ) • (p : P.Observables)
```

**`ProbabilisticTheory.PosCone.instOne`**, an instance, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Cone.lean#L83).

> The order unit, regarded as a point of the positive cone.

```lean
instance instOne : One (PosCone P)
```

**`ProbabilisticTheory.PosCone.coe_one`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Cone.lean#L86).

```lean
lemma coe_one : ((1 : PosCone P) : P.Observables) = (1 : P.Observables)
```

**`ProbabilisticTheory.PosCone.exists_sub`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Cone.lean#L89).

> Every observable is a difference `(A + n • 1) - n • 1` of two positive observables.

```lean
lemma exists_sub (A : P.Observables) : ∃ p q : PosCone P, (p : P.Observables) - q = A
```

## Depends on

- [Archimedean order-unit spaces (Physlib)](archimedean.md)
- [Ordered vector spaces and order units (Physlib)](basic.md)

## Sources

- [Physlib/ProbabilisticTheory/OrderUnit/Cone.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Cone.lean)
