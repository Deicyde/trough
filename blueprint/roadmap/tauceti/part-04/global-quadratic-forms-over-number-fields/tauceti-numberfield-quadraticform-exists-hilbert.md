---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.QuadraticForm.exists_hilbertSymbol_eq_ite
statement: formalized
proof: formalized
---

# TauCeti.NumberField.QuadraticForm.exists_hilbertSymbol_eq_ite

**Hilbert sign prescription** (O'Meara 71:19a). Let `S` be a finite set of finite places at
which `b ∈ Kˣ` is a nonsquare and `T` a finite set of real places at which `b` is negative, with
`#S + #T` even. Then some `a ∈ Kˣ` has Hilbert symbol `(a, b)_v = -1` at the places of `S` and of
`T`, and `1` at every other finite and real place.

```lean
TauCeti.NumberField.QuadraticForm.exists_hilbertSymbol_eq_ite.{u_1} {K : Type u_1} [Field K]
  [NumberField K] (b : Kˣ)
  (S : Finset (IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)))
  (T : Finset { w // w.IsReal }) (hS : ∀ v ∈ S, ¬IsSquare (v.unitAtFinitePlace b))
  (hT : ∀ w ∈ T, (NumberField.InfinitePlace.embedding_of_isReal ⋯) ↑b < 0)
  (hST : Even (S.card + T.card)) :
  ∃ a,
    (∀ (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)),
        TauCeti.hilbertSymbol (v.unitAtFinitePlace a) (v.unitAtFinitePlace b) =
          if v ∈ S then -1 else 1) ∧
      ∀ (w : { w // w.IsReal }),
        TauCeti.hilbertSymbol ((TauCeti.unitAtRealPlace w) a) ((TauCeti.unitAtRealPlace w) b) =
          if w ∈ T then -1 else 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The kernel of the idele Hilbert character](the-kernel-of-the-idele-hilbert-character.md)
- [The local class formation](../../part-01/class-field-theory/the-local-class-formation.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.ClassFormation.tateIso](../../part-01/class-field-theory/tauceti-classfieldtheory-classformation-tateiso.md)
- [TauCeti.QuaternionAlgebra.nonempty_algEquiv_matrix_tfae](../../part-06/quadratic-forms-and-cohomological-invariants/tauceti-quaternionalgebra-nonempty-algequiv-matr.md)
- [TauCeti.relDiscr](../../part-05/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)
- [TauCeti.semilocalEquiv](../../part-05/number-fields-ramification-frobenius-and-the-lmf/tauceti-semilocalequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.QuadraticForm.exists_hilbertSymbol_eq_ite`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/SignPrescription.html#TauCeti.NumberField.QuadraticForm.exists_hilbertSymbol_eq_ite).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.QuadraticForm.exists_hilbertSymbol_eq_ite`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/SignPrescription.html#TauCeti.NumberField.QuadraticForm.exists_hilbertSymbol_eq_ite)
- [Source of `TauCeti.NumberField.QuadraticForm.exists_hilbertSymbol_eq_ite` in TauCeti/NumberTheory/QuadraticForm/Global/SignPrescription.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/QuadraticForm/Global/SignPrescription.lean#L188)
- [Tau Ceti roadmap status: Global quadratic forms over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GlobalQuadraticForms/STATUS.md)
