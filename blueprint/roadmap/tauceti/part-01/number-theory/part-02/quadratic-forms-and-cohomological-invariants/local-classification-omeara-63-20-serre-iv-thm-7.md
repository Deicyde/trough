---
declaration: theorem
origin: cited
lean: TauCeti.RegularFormClass.localInvariants_injective
statement: formalized
proof: formalized
---

# Local classification (O'Meara 63:20, Serre IV Thm 7)

A regular-form class over a
nonarchimedean local field is determined by its rank, discriminant and local Hasse invariant.

```lean
TauCeti.RegularFormClass.localInvariants_injective.{u_1} {K : Type u_1} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] [Invertible 2] :
  Function.Injective TauCeti.RegularFormClass.localInvariants
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [The local square theorem bounds the defect of a unit](../local-field/the-local-square-theorem-bounds-the-defect-of-a.md)
- [The splitting criterion for quaternion algebras](the-splitting-criterion-for-quaternion-algebras.md)
- [TauCeti.multiplicativeSquareClassEquiv](../../../linear-algebra/part-01/orthogonal-and-spin-groups/tauceti-multiplicativesquareclassequiv.md)
- [Witt's chain theorem in its nontrivial range](../../../linear-algebra/part-01/quadratic-form/witts-chain-theorem-in-its-nontrivial-range.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RegularFormClass.localInvariants_injective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/Invariants.html#TauCeti.RegularFormClass.localInvariants_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.RegularFormClass.localInvariants_injective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/Invariants.html#TauCeti.RegularFormClass.localInvariants_injective)
- [Source of `TauCeti.RegularFormClass.localInvariants_injective` in TauCeti/NumberTheory/LocalField/QuadraticForm/Invariants.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LocalField/QuadraticForm/Invariants.lean#L140)
