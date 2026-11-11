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

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hilbert's product formula](../../part-02/quadratic-forms-and-cohomological-invariants/hilberts-product-formula.md)
- [The splitting criterion for quaternion algebras](../../part-02/quadratic-forms-and-cohomological-invariants/the-splitting-criterion-for-quaternion-algebras.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [Witt's chain theorem in its nontrivial range](../../../linear-algebra/quadratic-form/witts-chain-theorem-in-its-nontrivial-range.md)

## Lean

Formalized in Tau Ceti as [`QuadraticForm.globalInvariants_hasseProduct_eq_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.html#QuadraticForm.globalInvariants_hasseProduct_eq_one).

## Sources

- [Tau Ceti documentation: `QuadraticForm.globalInvariants_hasseProduct_eq_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.html#QuadraticForm.globalInvariants_hasseProduct_eq_one)
- [Source of `QuadraticForm.globalInvariants_hasseProduct_eq_one` in TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.lean#L128)
- [Tau Ceti roadmap status: Global quadratic forms over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GlobalQuadraticForms/STATUS.md)
