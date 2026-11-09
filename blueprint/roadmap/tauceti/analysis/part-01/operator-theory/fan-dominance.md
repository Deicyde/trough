---
declaration: theorem
origin: cited
lean: TauCeti.UnitarilyInvariantSeminorm.map_le_of_kyFanSum_le
statement: formalized
proof: formalized
---

# Fan dominance

If every Ky Fan sum of `A` is at most the corresponding Ky Fan sum of `C`,
then `N A ≤ N C` for every unitarily invariant seminorm `N`.

```lean
TauCeti.UnitarilyInvariantSeminorm.map_le_of_kyFanSum_le.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [FiniteDimensional 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [FiniteDimensional 𝕜 F]
  (N : TauCeti.UnitarilyInvariantSeminorm 𝕜 E F) {A C : E →ₗ[𝕜] F}
  (h : ∀ (k : ℕ), A.kyFanSum k ≤ C.kyFanSum k) : N A ≤ N C
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Courant–Fischer, lower direction](../../part-02/inner-product-space/part-01/courant-fischer-lower-direction.md)
- [Ky Fan's maximum principle, attainment](../../part-02/inner-product-space/part-02/ky-fans-maximum-principle-attainment.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UnitarilyInvariantSeminorm.map_le_of_kyFanSum_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/FanDominance.html#TauCeti.UnitarilyInvariantSeminorm.map_le_of_kyFanSum_le).

## Sources

- [Tau Ceti documentation: `TauCeti.UnitarilyInvariantSeminorm.map_le_of_kyFanSum_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/FanDominance.html#TauCeti.UnitarilyInvariantSeminorm.map_le_of_kyFanSum_le)
- [Source of `TauCeti.UnitarilyInvariantSeminorm.map_le_of_kyFanSum_le` in TauCeti/Analysis/InnerProductSpace/FanDominance.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/FanDominance.lean#L149)
- [Tau Ceti roadmap status: Operator theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OperatorTheory/STATUS.md)
