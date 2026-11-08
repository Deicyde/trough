---
declaration: def
origin: cited
lean: QuadraticForm.globalInvariants
statement: formalized
---

# The system of local invariants of a regular quadratic form `Q` over a number field

its
rank, its plain discriminant `d(Q) ∈ Kˣ/(Kˣ)²`, its Hasse sign at every finite place and its
positive index at every real place.

```lean
QuadraticForm.globalInvariants.{u, v} {K : Type u} [Field K] [NumberField K] {V : Type v}
  [AddCommGroup V] [_root_.Module K V] [FiniteDimensional K V] (Q : QuadraticForm K V)
  (hQ : QuadraticMap.Nondegenerate) : TauCeti.NumberField.QuadraticForm.GlobalFormInvariants K
```

## Depends on

- [A system of local invariants of a quadratic form over a number field `K`](a-system-of-local-invariants-of-a-quadratic-form.md)

## Proof depends on

- [The splitting criterion for quaternion algebras](../quadratic-forms-and-cohomological-invariants/the-splitting-criterion-for-quaternion-algebras.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [Witt's chain theorem in its nontrivial range](../../../linear-algebra/quadratic-form/witts-chain-theorem-in-its-nontrivial-range.md)

## Lean

Formalized in Tau Ceti as [`QuadraticForm.globalInvariants`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/FormInvariants.html#QuadraticForm.globalInvariants).

## Sources

- [Tau Ceti documentation: `QuadraticForm.globalInvariants`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/FormInvariants.html#QuadraticForm.globalInvariants)
- [Source of `QuadraticForm.globalInvariants` in TauCeti/NumberTheory/QuadraticForm/Global/FormInvariants.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/QuadraticForm/Global/FormInvariants.lean#L74)
- [Tau Ceti roadmap status: Global quadratic forms over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GlobalQuadraticForms/STATUS.md)
