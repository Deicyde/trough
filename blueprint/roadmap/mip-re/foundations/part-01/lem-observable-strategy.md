---
declaration: lemma
origin: cited
lean: MIPRE.LCS.ObservableStrategy.toProjectorStrategy, MIPRE.LCS.ObservableStrategy.isMeasurementSystem_aliceMeasurement, MIPRE.LCS.ObservableStrategy.aliceMeasurement_commute_bobMeasurement
statement: formalized
proof: formalized
---

# From an observable strategy to a projective strategy

A strategy given by commuting observables, one per variable of an LCS instance, yields a strategy given by genuine projective measurements: for a question consisting of several variables the joint measurement is the product of the corresponding binary projectors, which is projective because the observables commute, and the two players' measurements commute with each other.

## Depends on

- [Binary observables](def-observable.md)
- [Observables and projective measurements correspond](lem-observable-projector.md)
- [LCS instance](def-lcs-instance.md)

## Proof

The joint family over an equation's support is a product of commuting binary projectors, so it is a projective measurement and sums to $1$ over the outcomes; commutation across players is inherited from commutation of the underlying observables.

## Lean

Formalized as [`MIPRE.LCS.ObservableStrategy.toProjectorStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.ObservableStrategy.toProjectorStrategy), [`MIPRE.LCS.ObservableStrategy.isMeasurementSystem_aliceMeasurement`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.ObservableStrategy.isMeasurementSystem_aliceMeasurement), [`MIPRE.LCS.ObservableStrategy.aliceMeasurement_commute_bobMeasurement`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.ObservableStrategy.aliceMeasurement_commute_bobMeasurement).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 407](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L407)
