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
- [Source of `LieAlgebra.LoopAlgebra.residuePairing_toHahnModule` in TauCeti/Algebra/Lie/Loop/Derivative.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Lie/Loop/Derivative.lean#L123)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
