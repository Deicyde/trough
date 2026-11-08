---
declaration: theorem
origin: cited
lean: QuadraticForm.locallyEquivalent_iff_finrank_eq_and_discr_eq_and_finiteHasse_eq_and_realPositiveIndex_eq
statement: formalized
proof: formalized
---

# Local equivalence by invariants

Two regular forms over a number field are isometric at
every finite and every real place exactly when they have the same rank, the images of their global
discriminants agree at every finite place, and they have the same Hasse sign at every finite place
and the same positive index at every real place.

```lean
QuadraticForm.locallyEquivalent_iff_finrank_eq_and_discr_eq_and_finiteHasse_eq_and_realPositiveIndex_eq.{u,
    v, w}
  {K : Type u} [Field K] [NumberField K] {V : Type v} [AddCommGroup V] [_root_.Module K V]
  [FiniteDimensional K V] {W : Type w} [AddCommGroup W] [_root_.Module K W] [FiniteDimensional K W]
  {Q : QuadraticForm K V} {R : QuadraticForm K W} (hQ : QuadraticMap.Nondegenerate)
  (hR : QuadraticMap.Nondegenerate) :
  Q.LocallyEquivalent R ↔
    Module.finrank K V = Module.finrank K W ∧
      (∀ (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)),
          (algebraMap K (IsDedekindDomain.HeightOneSpectrum.adicCompletion K v)).squareClassMap
              (TauCeti.formClass Q hQ).discr =
            (algebraMap K (IsDedekindDomain.HeightOneSpectrum.adicCompletion K v)).squareClassMap
              (TauCeti.formClass R hR).discr) ∧
        Q.finiteHasse hQ = R.finiteHasse hR ∧ Q.realPositiveIndex = R.realPositiveIndex
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hensel's lemma with an estimate over a Henselian discrete valuation ring](../counting-totally-ramified-extensions-of-a-local/part-01/hensels-lemma-with-an-estimate-over-a-henselian.md)
- [The splitting criterion for quaternion algebras (Lam III.2.7 and III.4.2, Serre III.1, Gille-Szamuely 1.1.9)](../quadratic-forms-and-cohomological-invariants/the-splitting-criterion-for-quaternion-algebras.md)
- [Sylvester's law of inertia at a real place](../../part-02/other-results/sylvesters-law-of-inertia-at-a-real-place.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [Witt's chain theorem in its nontrivial range](../../../linear-algebra/quadratic-form/witts-chain-theorem-in-its-nontrivial-range.md)

## Lean

Formalized in Tau Ceti as [`QuadraticForm.locallyEquivalent_iff_finrank_eq_and_discr_eq_and_finiteHasse_eq_and_realPositiveIndex_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/Classification.html#QuadraticForm.locallyEquivalent_iff_finrank_eq_and_discr_eq_and_finiteHasse_eq_and_realPositiveIndex_eq).

## Sources

- [Tau Ceti documentation: `QuadraticForm.locallyEquivalent_iff_finrank_eq_and_discr_eq_and_finiteHasse_eq_and_realPositiveIndex_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/Classification.html#QuadraticForm.locallyEquivalent_iff_finrank_eq_and_discr_eq_and_finiteHasse_eq_and_realPositiveIndex_eq)
- [Source of `QuadraticForm.locallyEquivalent_iff_finrank_eq_and_discr_eq_and_finiteHasse_eq_and_realPositiveIndex_eq` in TauCeti/NumberTheory/QuadraticForm/Global/Classification.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/QuadraticForm/Global/Classification.lean#L131)
- [Tau Ceti roadmap status: Global quadratic forms over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GlobalQuadraticForms/STATUS.md)
