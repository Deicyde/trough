---
declaration: theorem
origin: cited
lean: Distribution.fst_image_waveFrontSet
statement: formalized
proof: formalized
---

# The projection of the wave front set is the singular support (Hörmander I, Proposition 8.1.3)

```lean
Distribution.fst_image_waveFrontSet.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {Ω : TopologicalSpace.Opens E} (T : Distribution Ω ℂ ⊤) :
  Prod.fst '' T.waveFrontSet = T.singularSupport
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Poisson's summation formula](../../part-03/fourier/part-01/poissons-summation-formula.md)

## Lean

Formalized in Tau Ceti as [`Distribution.fst_image_waveFrontSet`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/WaveFrontSet/SingularSupport.html#Distribution.fst_image_waveFrontSet).

## Sources

- [Tau Ceti documentation: `Distribution.fst_image_waveFrontSet`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/WaveFrontSet/SingularSupport.html#Distribution.fst_image_waveFrontSet)
- [Source of `Distribution.fst_image_waveFrontSet` in TauCeti/Analysis/Distribution/WaveFrontSet/SingularSupport.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Distribution/WaveFrontSet/SingularSupport.lean#L228)
- [Tau Ceti roadmap status: Pseudodifferential operators and elliptic analysis on bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PseudodifferentialOperators/STATUS.md)
