---
declaration: def
origin: cited
lean: LieAlgebra.LoopAlgebra.toHahnModule
statement: formalized
---

# LieAlgebra.LoopAlgebra.toHahnModule

The embedding of polynomial loops into `L`-valued Hahn series, sending `t ^ a ⊗ x` to the
monomial `x t ^ a`.

```lean
LieAlgebra.LoopAlgebra.toHahnModule.{u_1, u_2, u_3} (R : Type u_1) (Γ : Type u_2) (L : Type u_3)
  [CommRing R] [AddCommMonoid Γ] [PartialOrder Γ] [IsOrderedCancelAddMonoid Γ] [LieRing L]
  [LieAlgebra R L] : LieAlgebra.loopAlgebra R Γ L →ₗ⁅R⁆ HahnModule Γ R L
```

## Depends on

- [HahnModule.instLieRing](hahnmodule-instliering.md)

## Lean

Formalized in Tau Ceti as [`LieAlgebra.LoopAlgebra.toHahnModule`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Loop/HahnModule.html#LieAlgebra.LoopAlgebra.toHahnModule).

## Sources

- [Tau Ceti documentation: `LieAlgebra.LoopAlgebra.toHahnModule`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Loop/HahnModule.html#LieAlgebra.LoopAlgebra.toHahnModule)
- [Source of `LieAlgebra.LoopAlgebra.toHahnModule` in TauCeti/Algebra/Lie/Loop/HahnModule.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/Loop/HahnModule.lean#L40)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
