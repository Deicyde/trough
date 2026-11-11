---
declaration: theorem
origin: cited
lean: LieAlgebra.LoopAlgebra.residuePairing_toHahnModule
statement: formalized
proof: formalized
---

# LieAlgebra.LoopAlgebra.residuePairing_toHahnModule

The residue pairing `(x, y) ↦ Res Φ(x, D y) dt` of formal loops restricts along the embedding
of polynomial loops to Mathlib's residue pairing of polynomial loops.

```lean
LieAlgebra.LoopAlgebra.residuePairing_toHahnModule.{u_1, u_2} {R : Type u_1} {L : Type u_2}
  [CommRing R] [LieRing L] [LieAlgebra R L] (Φ : LinearMap.BilinForm R L)
  (p q : LieAlgebra.loopAlgebra R ℤ L) :
  ((HahnModule.residuePairing R Φ) ((LieAlgebra.LoopAlgebra.toHahnModule R ℤ L) p))
      ((LieAlgebra.LoopAlgebra.toHahnModule R ℤ L) q) =
    ((LieAlgebra.LoopAlgebra.residuePairing R ℤ L Φ) p) q
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LieAlgebra.LoopAlgebra.residuePairing_toHahnModule`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Loop/Derivative.html#LieAlgebra.LoopAlgebra.residuePairing_toHahnModule).

## Sources

- [Tau Ceti documentation: `LieAlgebra.LoopAlgebra.residuePairing_toHahnModule`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Loop/Derivative.html#LieAlgebra.LoopAlgebra.residuePairing_toHahnModule)
- [Source of `LieAlgebra.LoopAlgebra.residuePairing_toHahnModule` in TauCeti/Algebra/Lie/Loop/Derivative.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/Loop/Derivative.lean#L123)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
