---
declaration: def
origin: cited
lean: TauCeti.HasUniformJetBoundsOn
statement: formalized
---

# TauCeti.HasUniformJetBoundsOn

Each derivative through order `n` has a bound shared by the family on `s`.

```lean
TauCeti.HasUniformJetBoundsOn.{u_1, u_2, u_3, u_5} {ι : Type u_1} {E : Type u_2} {F : Type u_3}
  [NormedAddCommGroup E] [NormedAddCommGroup F] (𝕜 : Type u_5) [NontriviallyNormedField 𝕜]
  [NormedSpace 𝕜 E] [NormedSpace 𝕜 F] (n : ℕ) (s : Set E) (f : ι → E → F) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HasUniformJetBoundsOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/UniformJets.html#TauCeti.HasUniformJetBoundsOn).

## Sources

- [Tau Ceti documentation: `TauCeti.HasUniformJetBoundsOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/UniformJets.html#TauCeti.HasUniformJetBoundsOn)
- [Source of `TauCeti.HasUniformJetBoundsOn` in TauCeti/Analysis/Calculus/UniformJets.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Calculus/UniformJets.lean#L35)
- [Tau Ceti roadmap status: Three-dimensional Poincaré through Ricci flow with surgery](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Poincare3D/STATUS.md)
