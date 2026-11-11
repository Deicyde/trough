---
declaration: theorem
origin: cited
lean: TauCeti.ContinuousLinearMapUltraweak.isInducing_restrict_toWOT
statement: formalized
proof: formalized
---

# Bounded-set agreement with the weak operator topology

On a norm-bounded set of
operators, the ultraweak topology is the subspace topology of the weak operator topology.

```lean
TauCeti.ContinuousLinearMapUltraweak.isInducing_restrict_toWOT.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [CompleteSpace F]
  {s : Set (TauCeti.ContinuousLinearMapUltraweak 𝕜 E F)} {C : ℝ} (hs : ∀ A ∈ s, ‖A.toCLM‖ ≤ C) :
  Topology.IsInducing (s.domRestrict fun A => ContinuousLinearMapWOT.ofCLM A.toCLM)
```

## Depends on

- [TauCeti.ContinuousLinearMapUltraweak](tauceti-continuouslinearmapultraweak.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ContinuousLinearMapUltraweak.isInducing_restrict_toWOT`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UltraweakTopology.html#TauCeti.ContinuousLinearMapUltraweak.isInducing_restrict_toWOT).

## Sources

- [Tau Ceti documentation: `TauCeti.ContinuousLinearMapUltraweak.isInducing_restrict_toWOT`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UltraweakTopology.html#TauCeti.ContinuousLinearMapUltraweak.isInducing_restrict_toWOT)
- [Source of `TauCeti.ContinuousLinearMapUltraweak.isInducing_restrict_toWOT` in TauCeti/Analysis/InnerProductSpace/UltraweakTopology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/UltraweakTopology.lean#L355)
- [Tau Ceti roadmap status: Von Neumann algebras, factors, and modular theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/VonNeumannAlgebras/STATUS.md)
