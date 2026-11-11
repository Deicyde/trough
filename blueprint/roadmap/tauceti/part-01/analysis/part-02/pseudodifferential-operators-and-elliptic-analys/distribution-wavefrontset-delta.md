---
declaration: theorem
origin: cited
lean: Distribution.waveFrontSet_delta
statement: formalized
proof: formalized
---

# Distribution.waveFrontSet_delta

The point mass at `x₀ ∈ Ω` has wave front set `{x₀} × (E \ {0})`: it is singular at `x₀` in
every direction.

```lean
Distribution.waveFrontSet_delta.{u_1} {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  {Ω : TopologicalSpace.Opens E} [FiniteDimensional ℝ E] {x₀ : E} (hx₀ : x₀ ∈ Ω) :
  ((Distribution.mapCLM Complex.ofRealCLM) (Distribution.delta x₀)).waveFrontSet = {x₀} ×ˢ {0}ᶜ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Distribution.waveFrontSet_delta`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/WaveFrontSet/Basic.html#Distribution.waveFrontSet_delta).

## Sources

- [Tau Ceti documentation: `Distribution.waveFrontSet_delta`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/WaveFrontSet/Basic.html#Distribution.waveFrontSet_delta)
- [Source of `Distribution.waveFrontSet_delta` in TauCeti/Analysis/Distribution/WaveFrontSet/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Distribution/WaveFrontSet/Basic.lean#L391)
- [Tau Ceti roadmap status: Pseudodifferential operators and elliptic analysis on bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PseudodifferentialOperators/STATUS.md)
