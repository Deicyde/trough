---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsLocalRealization.exists_locallyRepresents_prod
statement: formalized
proof: formalized
---

# O'Meara 72:1 up to one global representation

Let `U_v` and `R_w` be local forms realizing
an admissible system `I`. Then there are a regular global form `W` of rank `I.rank` and
`α, β ∈ Kˣ` such that `⟨α, -αβ⟩` is represented by `⟨1, -β⟩ ⊥ W` at every finite and real place,
and such that, if `⟨α, -αβ⟩` is represented by `⟨1, -β⟩ ⊥ W` over `K`, some regular global form on
`K ^ I.rank` has `I` as its system of local invariants.

```lean
TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsLocalRealization.exists_locallyRepresents_prod.{u_1}
  {K : Type u_1} [Field K] [NumberField K]
  {I : TauCeti.NumberField.QuadraticForm.GlobalFormInvariants K}
  {U :
    (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)) →
      QuadraticForm (IsDedekindDomain.HeightOneSpectrum.adicCompletion K v)
        (Fin I.rank → IsDedekindDomain.HeightOneSpectrum.adicCompletion K v)}
  {R : { w // w.IsReal } → QuadraticForm ℝ (Fin I.rank → ℝ)} (hI : I.IsAdmissible)
  (hL : I.IsLocalRealization U R) :
  ∃ W,
    ∃ (_ : QuadraticMap.Nondegenerate),
      ∃ a b,
        QuadraticForm.LocallyRepresents (QuadraticMap.weightedSumSquares K ![↑a, -(↑a * ↑b)])
            ((QuadraticMap.weightedSumSquares K ![1, -↑b]).prod W) ∧
          ((QuadraticMap.weightedSumSquares K ![↑a, -(↑a * ↑b)]).IsRepresentedBy
              ((QuadraticMap.weightedSumSquares K ![1, -↑b]).prod W) →
            ∃ Q, ∃ (hQ : QuadraticMap.Nondegenerate), Q.globalInvariants hQ = I)
```

## Depends on

- [A system of local invariants of a quadratic form over a number field `K`](a-system-of-local-invariants-of-a-quadratic-form.md)
- [The system of local invariants of a regular quadratic form `Q` over a number field](the-system-of-local-invariants-of-a-regular-quad.md)

## Proof depends on

- [The Hasse product formula](the-hasse-product-formula.md)
- [Hensel's lemma with an estimate over a Henselian discrete valuation ring](../counting-totally-ramified-extensions-of-a-local/part-01/hensels-lemma-with-an-estimate-over-a-henselian.md)
- [Hilbert sign prescription (O'Meara 71:19a)](hilbert-sign-prescription-omeara-71-19a.md)
- [The splitting criterion for quaternion algebras (Lam III.2.7 and III.4.2, Serre III.1, Gille-Szamuely 1.1.9)](../quadratic-forms-and-cohomological-invariants/the-splitting-criterion-for-quaternion-algebras.md)
- [Sylvester's law of inertia for regular forms](../../../linear-algebra/quadratic-form/sylvesters-law-of-inertia-for-regular-forms.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [Witt's chain theorem in its nontrivial range](../../../linear-algebra/quadratic-form/witts-chain-theorem-in-its-nontrivial-range.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsLocalRealization.exists_locallyRepresents_prod`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/PrescribedLocalForms.html#TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsLocalRealization.exists_locallyRepresents_prod).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsLocalRealization.exists_locallyRepresents_prod`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/PrescribedLocalForms.html#TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsLocalRealization.exists_locallyRepresents_prod)
- [Source of `TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsLocalRealization.exists_locallyRepresents_prod` in TauCeti/NumberTheory/QuadraticForm/Global/PrescribedLocalForms.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/QuadraticForm/Global/PrescribedLocalForms.lean#L135)
- [Tau Ceti roadmap status: Global quadratic forms over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GlobalQuadraticForms/STATUS.md)
