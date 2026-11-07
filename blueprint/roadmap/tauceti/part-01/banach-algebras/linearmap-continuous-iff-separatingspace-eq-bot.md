---
declaration: theorem
origin: cited
lean: LinearMap.continuous_iff_separatingSpace_eq_bot
statement: formalized
proof: formalized
---

# LinearMap.continuous\_iff\_separatingSpace\_eq\_bot

A linear map between Banach spaces is continuous if and only if its separating space is
trivial.

```lean
LinearMap.continuous_iff_separatingSpace_eq_bot.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] (T : E →ₗ[𝕜] F) [CompleteSpace E] [CompleteSpace F] :
  Continuous ⇑T ↔ T.separatingSpace = ⊥
```

## Depends on

- [LinearMap.separatingSpace](linearmap-separatingspace.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.continuous_iff_separatingSpace_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/SeparatingSpace.html#LinearMap.continuous_iff_separatingSpace_eq_bot).

## Sources

- [Tau Ceti documentation: `LinearMap.continuous_iff_separatingSpace_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/SeparatingSpace.html#LinearMap.continuous_iff_separatingSpace_eq_bot)
- [Source of `LinearMap.continuous_iff_separatingSpace_eq_bot` in TauCeti/Analysis/Normed/Operator/SeparatingSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/SeparatingSpace.lean#L251)
- [Tau Ceti roadmap status: Banach algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BanachAlgebras/STATUS.md)
