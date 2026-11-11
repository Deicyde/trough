---
declaration: theorem
origin: cited
lean: Distribution.waveFrontSet_ofFun_one_map_subtype
statement: formalized
proof: formalized
---

# The wave front set of the surface measure of a subspace is its conormal set

The surface
measure of a subspace `V`, that is, Lebesgue measure of `V` pushed forward to `E`, is singular
exactly at the points of `V` in `Ω`, and there exactly in the nonzero directions orthogonal to
`V`. For `V = ⊤` the measure is Lebesgue measure and the wave front set is empty; for `V = ⊥` it
is the point mass at the origin, singular in every direction.

```lean
Distribution.waveFrontSet_ofFun_one_map_subtype.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] {Ω : TopologicalSpace.Opens E} [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] (V : Submodule ℝ E) :
  (Distribution.ofFun Ω 1 (MeasureTheory.Measure.map Subtype.val MeasureTheory.volume)
        ⊤).waveFrontSet =
    (↑Ω ∩ ↑V) ×ˢ (↑Vᗮ \ {0})
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Distribution.waveFrontSet_ofFun_one_map_subtype`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/WaveFrontSet/Basic.html#Distribution.waveFrontSet_ofFun_one_map_subtype).

## Sources

- [Tau Ceti documentation: `Distribution.waveFrontSet_ofFun_one_map_subtype`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/WaveFrontSet/Basic.html#Distribution.waveFrontSet_ofFun_one_map_subtype)
- [Source of `Distribution.waveFrontSet_ofFun_one_map_subtype` in TauCeti/Analysis/Distribution/WaveFrontSet/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Distribution/WaveFrontSet/Basic.lean#L595)
- [Tau Ceti roadmap status: Pseudodifferential operators and elliptic analysis on bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PseudodifferentialOperators/STATUS.md)
