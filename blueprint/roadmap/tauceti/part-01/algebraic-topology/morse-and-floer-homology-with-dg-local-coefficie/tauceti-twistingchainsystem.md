---
declaration: structure
origin: cited
lean: TauCeti.TwistingChainSystem
statement: formalized
---

# TauCeti.TwistingChainSystem

A **twisting chain system** for the composition maps `ι`: chains `s x y` of `M x y`, of
cohomological degree `ind y - ind x + 1`, satisfying the twisting equation
`∂ s x y = Σ_z (-1) ^ (ind x - ind z) • ι_* (s x z × s z y)`.

```lean
TauCeti.TwistingChainSystem.{u_1, u_2, u_3} {P : Type u_1} [Fintype P] (ind : P → ℤ)
  {M : P → P → Type u_2} [(x y : P) → TopologicalSpace (M x y)]
  (ι : (x y z : P) → C(M x y × M y z, M x z)) (R : Type u_3) [CommRing R] :
  Type (max (max u_1 u_2) u_3)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TwistingChainSystem`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/MonoidAlgebra/TwistingChainSystem.html#TauCeti.TwistingChainSystem).

## Sources

- [Tau Ceti documentation: `TauCeti.TwistingChainSystem`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/MonoidAlgebra/TwistingChainSystem.html#TauCeti.TwistingChainSystem)
- [Source of `TauCeti.TwistingChainSystem` in TauCeti/AlgebraicTopology/Singular/Cubical/MonoidAlgebra/TwistingChainSystem.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Singular/Cubical/MonoidAlgebra/TwistingChainSystem.lean#L96)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DGFloer/STATUS.md)
