---
declaration: theorem
origin: cited
lean: TauCeti.Comodule.matrixCoefficientSubmodule_eq_iff
statement: formalized
proof: formalized
---

# Coefficient spaces label simple comodules

Two simple comodules which are projective
over the ground ring, for instance any two simple comodules over a field, have the same
coefficient space exactly when there is a nonzero morphism between them, that is, exactly when
they are isomorphic.

```lean
TauCeti.Comodule.matrixCoefficientSubmodule_eq_iff.{u_1, u_2, u_3, u_4} {R : Type u_1}
  {C : Type u_2} {M : Type u_3} {N : Type u_4} [CommRing R] [AddCommGroup C] [_root_.Module R C]
  [Coalgebra R C] [Module.Projective R C] [AddCommGroup M] [_root_.Module R M]
  [TauCeti.Comodule R C M] [AddCommGroup N] [_root_.Module R N] [TauCeti.Comodule R C N]
  [Module.Projective R M] [IsSimpleOrder (TauCeti.Subcomodule R C M)]
  [IsSimpleOrder (TauCeti.Subcomodule R C N)] :
  TauCeti.Comodule.matrixCoefficientSubmodule = TauCeti.Comodule.matrixCoefficientSubmodule ↔
    ∃ f, f ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Comodule.matrixCoefficientSubmodule_eq_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Coalgebra/Comodule/MatrixCoefficient/Isotypic.html#TauCeti.Comodule.matrixCoefficientSubmodule_eq_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Comodule.matrixCoefficientSubmodule_eq_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Coalgebra/Comodule/MatrixCoefficient/Isotypic.html#TauCeti.Comodule.matrixCoefficientSubmodule_eq_iff)
- [Source of `TauCeti.Comodule.matrixCoefficientSubmodule_eq_iff` in TauCeti/Algebra/Coalgebra/Comodule/MatrixCoefficient/Isotypic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Coalgebra/Comodule/MatrixCoefficient/Isotypic.lean#L154)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ReductiveGroups/STATUS.md)
