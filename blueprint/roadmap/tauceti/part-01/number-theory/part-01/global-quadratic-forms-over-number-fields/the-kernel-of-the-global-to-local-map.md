---
declaration: theorem
origin: cited
lean: TauCeti.WittRing.globalToLocal_eq_zero_iff
statement: formalized
proof: formalized
---

# The kernel of the global-to-local map

A Witt class of a number field `K` vanishes at
every finite and every real place exactly when it has even dimension, its signed discriminant
becomes a square in every completion `K_v`, its Clifford invariant splits over every `K_v`, and
its signature vanishes at every real place.

```lean
TauCeti.WittRing.globalToLocal_eq_zero_iff.{u} {K : Type u} [Field K] [NumberField K]
  (x : TauCeti.WittRing K) :
  (TauCeti.WittRing.globalToLocal K) x = 0 ↔
    TauCeti.WittRing.dimMod2 x = 0 ∧
      (∀ (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)),
          (algebraMap K (IsDedekindDomain.HeightOneSpectrum.adicCompletion K v)).squareClassMap
              x.signedDiscr =
            0) ∧
        (∀ (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)),
            (TauCeti.BrauerGroup.baseChange K
                  (IsDedekindDomain.HeightOneSpectrum.adicCompletion K v))
                x.cliffordInvariant =
              1) ∧
          ∀ (w : { w // w.IsReal }),
            TauCeti.WittRing.signature ((TauCeti.WittRing.atRealPlace w) x) = 0
```

## Depends on

- [The global-to-local map of Witt rings](the-global-to-local-map-of-witt-rings.md)

## Proof depends on

- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [The splitting criterion for quaternion algebras](../../part-02/quadratic-forms-and-cohomological-invariants/the-splitting-criterion-for-quaternion-algebras.md)
- [The structure theorem in operator form](../../../representation-theory/spin/the-structure-theorem-in-operator-form.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [Wedderburn-Artin for central simple algebras](../../../algebra/part-02/central-simple/wedderburn-artin-for-central-simple-algebras.md)
- [Witt decomposition](../../../linear-algebra/quadratic-form/witt-decomposition.md)
- [Witt's chain theorem in its nontrivial range](../../../linear-algebra/quadratic-form/witts-chain-theorem-in-its-nontrivial-range.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.WittRing.globalToLocal_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/WittLocalization.html#TauCeti.WittRing.globalToLocal_eq_zero_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.WittRing.globalToLocal_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/WittLocalization.html#TauCeti.WittRing.globalToLocal_eq_zero_iff)
- [Source of `TauCeti.WittRing.globalToLocal_eq_zero_iff` in TauCeti/NumberTheory/QuadraticForm/Global/WittLocalization.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/QuadraticForm/Global/WittLocalization.lean#L199)
- [Tau Ceti roadmap status: Global quadratic forms over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GlobalQuadraticForms/STATUS.md)
