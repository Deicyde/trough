---
declaration: structure
origin: cited
lean: TauCeti.ProjValMeasure
statement: formalized
---

# TauCeti.ProjValMeasure

A **projection-valued measure** on the measurable sets of `X`, acting on a
complex Hilbert space `H`.

The diagonal scalar measures `diag ξ` are supplied as finite measures,
related to the projections by `inner_proj`. This follows the donor's carrier
representation, in which the diagonal measures are uniquely determined by
`proj`. Idempotence, self-adjointness,
positivity, finite additivity, contraction, and strong countable additivity
follow from these laws.

```lean
TauCeti.ProjValMeasure.{u_3, u_4} (X : Type u_3) [MeasurableSpace X] (H : Type u_4)
  [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H] : Type (max u_3 u_4)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ProjValMeasure`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/ProjValMeasure/Basic.html#TauCeti.ProjValMeasure).

## Sources

- [Tau Ceti documentation: `TauCeti.ProjValMeasure`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/ProjValMeasure/Basic.html#TauCeti.ProjValMeasure)
- [Source of `TauCeti.ProjValMeasure` in TauCeti/Analysis/InnerProductSpace/ProjValMeasure/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/ProjValMeasure/Basic.lean#L83)
- [Tau Ceti roadmap status: Operator theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OperatorTheory/STATUS.md)
