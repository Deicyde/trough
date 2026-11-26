---
declaration: module
origin: cited
lean: PhyslibAlpha.ProbabilisticTheory.Effect.binaryAtom, PhyslibAlpha.ProbabilisticTheory.Effect.sum_binaryAtom, PhyslibAlpha.ProbabilisticTheory.Effect.binaryMeasurement, PhyslibAlpha.ProbabilisticTheory.Effect.binaryMeasurement_true, PhyslibAlpha.ProbabilisticTheory.Effect.binaryMeasurement_false
statement: formalized
proof: formalized
---

# Binary measurements

The module `PhyslibAlpha.ProbabilisticTheory.Measurement.Binary`, [PhyslibAlpha/ProbabilisticTheory/Measurement/Binary.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Measurement/Binary.lean): 5 declarations, 2 with a docstring.

> The yes/no measurement defined by an effect of an Archimedean system.

## i. Overview

> Every effect of an Archimedean system defines a yes/no measurement: the outcome `true` has the
> effect itself, the outcome `false` its complement.

## ii. Key results

> - `Effect.binaryMeasurement` : the binary measurement associated to an effect.

## iv. References

> * None.

## A. Binary measurements

**`PhyslibAlpha.ProbabilisticTheory.Effect.binaryAtom`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Measurement/Binary.lean#L46).

> The effect of each outcome of the binary measurement of `e`: `e` for `true`, its complement
> for `false`.

```lean
def binaryAtom (e : Effect E) (b : Bool) : Effect E
```

**`PhyslibAlpha.ProbabilisticTheory.Effect.sum_binaryAtom`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Measurement/Binary.lean#L49).

```lean
lemma sum_binaryAtom (e : Effect E) : ∑ b, (binaryAtom e b : E) = 1
```

**`PhyslibAlpha.ProbabilisticTheory.Effect.binaryMeasurement`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Measurement/Binary.lean#L55).

> The two-outcome measurement whose `true` effect is `e` and whose `false` effect is `1 - e`.

```lean
noncomputable def binaryMeasurement (e : Effect F) : Measurement Bool F
```

**`PhyslibAlpha.ProbabilisticTheory.Effect.binaryMeasurement_true`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Measurement/Binary.lean#L59).

```lean
lemma binaryMeasurement_true (e : Effect F) (h : MeasurableSet {true}) :
    binaryMeasurement e {true} h = e
```

**`PhyslibAlpha.ProbabilisticTheory.Effect.binaryMeasurement_false`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Measurement/Binary.lean#L64).

```lean
lemma binaryMeasurement_false (e : Effect F) (h : MeasurableSet {false}) :
    binaryMeasurement e {false} h = complement e
```

## Depends on

- [Complementary effects (PhyslibAlpha)](../effect/complement.md)
- [Measurements with finitely many outcomes](finite.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Measurement/Binary.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Measurement/Binary.lean)
