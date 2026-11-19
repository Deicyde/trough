---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsAdmissible.exists_globalForm
statement: formalized
proof: formalized
---

# Realization of admissible systems

Every admissible system of local invariants over a
number field is the system of a regular global form on `Fin I.rank → K`.

```lean
TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsAdmissible.exists_globalForm.{u_1}
  {K : Type u_1} [Field K] [NumberField K]
  {I : TauCeti.NumberField.QuadraticForm.GlobalFormInvariants K} (hI : I.IsAdmissible) :
  ∃ Q, ∃ (hQ : QuadraticMap.Nondegenerate), Q.globalInvariants hQ = I
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Hasse product formula](the-hasse-product-formula.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [Hilbert sign prescription (O'Meara 71:19a)](hilbert-sign-prescription-omeara-71-19a.md)
- [Hilbert's product formula](../../part-02/quadratic-forms-and-cohomological-invariants/hilberts-product-formula.md)
- [The local square theorem bounds the defect of a unit](../../part-02/local-field/the-local-square-theorem-bounds-the-defect-of-a.md)
- [The splitting criterion for quaternion algebras](../../part-02/quadratic-forms-and-cohomological-invariants/the-splitting-criterion-for-quaternion-algebras.md)
- [TauCeti.multiplicativeSquareClassEquiv](../../../linear-algebra/part-01/orthogonal-and-spin-groups/tauceti-multiplicativesquareclassequiv.md)
- [Wedderburn-Artin for central simple algebras](../../../algebra/part-02/central-simple/wedderburn-artin-for-central-simple-algebras.md)
- [Witt decomposition](../../../linear-algebra/part-01/quadratic-form/witt-decomposition.md)
- [Witt's chain theorem in its nontrivial range](../../../linear-algebra/part-01/quadratic-form/witts-chain-theorem-in-its-nontrivial-range.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsAdmissible.exists_globalForm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/Realization.html#TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsAdmissible.exists_globalForm).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsAdmissible.exists_globalForm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/Realization.html#TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsAdmissible.exists_globalForm)
- [Source of `TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsAdmissible.exists_globalForm` in TauCeti/NumberTheory/QuadraticForm/Global/Realization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/QuadraticForm/Global/Realization.lean#L286)
- [Tau Ceti roadmap status: Global quadratic forms over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GlobalQuadraticForms/STATUS.md)
