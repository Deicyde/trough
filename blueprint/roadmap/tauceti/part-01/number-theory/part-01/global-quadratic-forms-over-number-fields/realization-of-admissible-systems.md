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
TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsAdmissible.exists_globalForm {K : Type}
  [Field K] [NumberField K] {I : TauCeti.NumberField.QuadraticForm.GlobalFormInvariants K}
  (hI : I.IsAdmissible) : ∃ Q, ∃ (hQ : QuadraticMap.Nondegenerate), Q.globalInvariants hQ = I
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Hasse product formula](the-hasse-product-formula.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [Hilbert sign prescription (O'Meara 71:19a)](hilbert-sign-prescription-omeara-71-19a.md)
- [Hilbert's product formula](../../part-02/quadratic-forms-and-cohomological-invariants/hilberts-product-formula.md)
- [The splitting criterion for quaternion algebras](../../part-02/quadratic-forms-and-cohomological-invariants/the-splitting-criterion-for-quaternion-algebras.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [Wedderburn-Artin for central simple algebras](../../../algebra/part-02/central-simple/wedderburn-artin-for-central-simple-algebras.md)
- [Witt decomposition](../../../linear-algebra/quadratic-form/witt-decomposition.md)
- [Witt's chain theorem in its nontrivial range](../../../linear-algebra/quadratic-form/witts-chain-theorem-in-its-nontrivial-range.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsAdmissible.exists_globalForm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/Realization.html#TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsAdmissible.exists_globalForm).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsAdmissible.exists_globalForm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/Realization.html#TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsAdmissible.exists_globalForm)
- [Source of `TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.IsAdmissible.exists_globalForm` in TauCeti/NumberTheory/QuadraticForm/Global/Realization.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/QuadraticForm/Global/Realization.lean#L286)
- [Tau Ceti roadmap status: Global quadratic forms over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GlobalQuadraticForms/STATUS.md)
