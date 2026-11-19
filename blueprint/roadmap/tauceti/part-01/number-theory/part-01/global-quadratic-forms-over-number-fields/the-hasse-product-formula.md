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

- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [Hilbert's product formula](../../part-02/quadratic-forms-and-cohomological-invariants/hilberts-product-formula.md)
- [The local square theorem bounds the defect of a unit](../../part-02/local-field/the-local-square-theorem-bounds-the-defect-of-a.md)
- [The splitting criterion for quaternion algebras](../../part-02/quadratic-forms-and-cohomological-invariants/the-splitting-criterion-for-quaternion-algebras.md)
- [TauCeti.multiplicativeSquareClassEquiv](../../../linear-algebra/part-01/orthogonal-and-spin-groups/tauceti-multiplicativesquareclassequiv.md)
- [Witt's chain theorem in its nontrivial range](../../../linear-algebra/part-01/quadratic-form/witts-chain-theorem-in-its-nontrivial-range.md)

## Lean

Formalized in Tau Ceti as [`QuadraticForm.globalInvariants_hasseProduct_eq_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.html#QuadraticForm.globalInvariants_hasseProduct_eq_one).

## Sources

- [Tau Ceti documentation: `QuadraticForm.globalInvariants_hasseProduct_eq_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.html#QuadraticForm.globalInvariants_hasseProduct_eq_one)
- [Source of `QuadraticForm.globalInvariants_hasseProduct_eq_one` in TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.lean#L128)
- [Tau Ceti roadmap status: Global quadratic forms over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GlobalQuadraticForms/STATUS.md)
