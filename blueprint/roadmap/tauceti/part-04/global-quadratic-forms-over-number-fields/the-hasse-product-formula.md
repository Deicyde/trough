---
declaration: theorem
origin: cited
lean: QuadraticForm.globalInvariants_hasseProduct_eq_one
statement: formalized
proof: formalized
---

# The Hasse product formula

For every regular form `Q` over a number field `K`, the
product of the finite Hasse signs and of the real Hasse signs of `Q` is `1`.

```lean
QuadraticForm.globalInvariants_hasseProduct_eq_one.{u_1, u_2} {K : Type u_1} [Field K]
  [NumberField K] {V : Type u_2} [AddCommGroup V] [_root_.Module K V] [FiniteDimensional K V]
  (Q : QuadraticForm K V) (hQ : QuadraticMap.Nondegenerate) :
  (Q.globalInvariants hQ).hasseProduct = 1
```

## Depends on

- [A system of local invariants of a quadratic form over a number field `K`](a-system-of-local-invariants-of-a-quadratic-form.md)
- [The system of local invariants of a regular quadratic form](the-system-of-local-invariants-of-a-regular-quad.md)

## Proof depends on

- [Hilbert's product formula](../../part-06/quadratic-forms-and-cohomological-invariants/hilberts-product-formula.md)
- [The splitting criterion for quaternion algebras](../../part-06/quadratic-forms-and-cohomological-invariants/the-splitting-criterion-for-quaternion-algebras.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`QuadraticForm.globalInvariants_hasseProduct_eq_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.html#QuadraticForm.globalInvariants_hasseProduct_eq_one).

## Sources

- [Tau Ceti documentation: `QuadraticForm.globalInvariants_hasseProduct_eq_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.html#QuadraticForm.globalInvariants_hasseProduct_eq_one)
- [Source of `QuadraticForm.globalInvariants_hasseProduct_eq_one` in TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.lean#L128)
- [Tau Ceti roadmap status: Global quadratic forms over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GlobalQuadraticForms/STATUS.md)
