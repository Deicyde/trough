---
declaration: def
origin: cited
lean: TauCeti.HomologicalOrientation.dualityMap
statement: formalized
---

# The duality map

**The duality map** `D_M : Hᵖ_c(M; L) ⟶ H_q(M; L)` of an oriented manifold, `p + q = n`: on a
class supported in a compact set `K`, the cap product with the fundamental class `μ_K` along `K`.

```lean
TauCeti.HomologicalOrientation.dualityMap {M E : Type} [TopologicalSpace M] [T2Space M]
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [ChartedSpace E M] {n : ℕ}
  (o : TauCeti.HomologicalOrientation M E n) (hn : Module.finrank ℝ E = n) (L : ModuleCat ℤ)
  (p q : ℕ) (h : p + q = n) :
  (↧M).compactSupportCohomology ↧(ULift.{0, 0} ℤ) ℤ L p ⟶
    ((AlgebraicTopology.singularHomologyFunctor (ModuleCat ℤ) q).obj L).obj ↧M
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mayer–Vietoris isomorphism of a sphere](../singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../singular/the-relative-small-chain-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HomologicalOrientation.dualityMap`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/CompactSupport/Duality.html#TauCeti.HomologicalOrientation.dualityMap).

## Sources

- [Tau Ceti documentation: `TauCeti.HomologicalOrientation.dualityMap`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/CompactSupport/Duality.html#TauCeti.HomologicalOrientation.dualityMap)
- [Source of `TauCeti.HomologicalOrientation.dualityMap` in TauCeti/AlgebraicTopology/Cohomology/CompactSupport/Duality.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Cohomology/CompactSupport/Duality.lean#L164)
- [Tau Ceti roadmap status: Algebraic topology of spaces and manifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AlgebraicTopology/STATUS.md)
