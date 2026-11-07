---
declaration: def
origin: cited
lean: ContinuousLinearMap.unitizationAction
statement: formalized
---

# ContinuousLinearMap.unitizationAction

The unital action on `E` of the `ℓ¹` unitization of `A` extending the left action `L`.

```lean
ContinuousLinearMap.unitizationAction.{u_1, u_2, u_3} {𝕜 : Type u_1} {A : Type u_2} {E : Type u_3}
  [NontriviallyNormedField 𝕜] [NonUnitalNormedRing A] [NormedSpace 𝕜 A] [IsScalarTower 𝕜 A A]
  [SMulCommClass 𝕜 A A] [NormedAddCommGroup E] [NormedSpace 𝕜 E] (L : A →L[𝕜] E →L[𝕜] E)
  (hL : ∀ (a b : A) (z : E), (L (a * b)) z = (L a) ((L b) z)) :
  WithLp 1 (Unitization 𝕜 A) →ₐ[𝕜] E →L[𝕜] E
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.unitizationAction`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Unitization/Basic.html#ContinuousLinearMap.unitizationAction).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.unitizationAction`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Unitization/Basic.html#ContinuousLinearMap.unitizationAction)
- [Source of `ContinuousLinearMap.unitizationAction` in TauCeti/Analysis/Normed/Module/Unitization/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Module/Unitization/Basic.lean#L123)
- [Tau Ceti roadmap status: Banach algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BanachAlgebras/STATUS.md)
