---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsAdmissible.exists_globalForm_equivalent_at_places
statement: formalized
proof: formalized
---

# Existence with prescribed local behavior for admissible systems

An admissible system
has a regular global realization on `Fin I.rank → K` that is isometric at every finite and real
place to any prescribed local realization of the system.

```lean
TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsAdmissible.exists_globalForm_equivalent_at_places.{u_1}
  {K : Type u_1} [Field K] [NumberField K]
  {I : TauCeti.NumberField.QuadraticForm.GlobalFormInvariants K} (hI : I.IsAdmissible)
  {U :
    (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)) →
      QuadraticForm (IsDedekindDomain.HeightOneSpectrum.adicCompletion K v)
        (Fin I.rank → IsDedekindDomain.HeightOneSpectrum.adicCompletion K v)}
  {R : { w // w.IsReal } → QuadraticForm ℝ (Fin I.rank → ℝ)} (hL : I.IsLocalRealization U R) :
  ∃ Q,
    ∃ (hQ : QuadraticMap.Nondegenerate),
      Q.globalInvariants hQ = I ∧
        (∀ (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)),
            QuadraticMap.Equivalent (Q.atFinitePlace v) (U v)) ∧
          ∀ (w : { w // w.IsReal }), QuadraticMap.Equivalent (Q.atRealPlace w) (R w)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [The local square theorem bounds the defect of a unit](../../part-02/local-field/the-local-square-theorem-bounds-the-defect-of-a.md)
- [Realization of admissible systems](realization-of-admissible-systems.md)
- [The splitting criterion for quaternion algebras](../../part-02/quadratic-forms-and-cohomological-invariants/the-splitting-criterion-for-quaternion-algebras.md)
- [Sylvester's law of inertia for regular forms](../../../linear-algebra/part-01/quadratic-form/sylvesters-law-of-inertia-for-regular-forms.md)
- [TauCeti.multiplicativeSquareClassEquiv](../../../linear-algebra/part-01/orthogonal-and-spin-groups/tauceti-multiplicativesquareclassequiv.md)
- [Witt's chain theorem in its nontrivial range](../../../linear-algebra/part-01/quadratic-form/witts-chain-theorem-in-its-nontrivial-range.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsAdmissible.exists_globalForm_equivalent_at_places`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/Realization.html#TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsAdmissible.exists_globalForm_equivalent_at_places).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsAdmissible.exists_globalForm_equivalent_at_places`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/Realization.html#TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsAdmissible.exists_globalForm_equivalent_at_places)
- [Source of `TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsAdmissible.exists_globalForm_equivalent_at_places` in TauCeti/NumberTheory/QuadraticForm/Global/Realization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/QuadraticForm/Global/Realization.lean#L314)
- [Tau Ceti roadmap status: Global quadratic forms over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GlobalQuadraticForms/STATUS.md)
