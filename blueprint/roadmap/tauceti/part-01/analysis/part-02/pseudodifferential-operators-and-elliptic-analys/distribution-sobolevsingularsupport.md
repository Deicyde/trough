---
declaration: def
origin: cited
lean: Distribution.sobolevSingularSupport
statement: formalized
---

# Distribution.sobolevSingularSupport

The **`H^s` singular support** of a complex distribution `T` on `Ω`: the points of `Ω` near
which `T` is not `H^s`.

```lean
Distribution.sobolevSingularSupport.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {Ω : TopologicalSpace.Opens E} (s : ℝ) (T : Distribution Ω ℂ ⊤) : Set E
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Distribution.sobolevSingularSupport`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/WaveFrontSet/Sobolev/SingularSupport.html#Distribution.sobolevSingularSupport).

## Sources

- [Tau Ceti documentation: `Distribution.sobolevSingularSupport`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/WaveFrontSet/Sobolev/SingularSupport.html#Distribution.sobolevSingularSupport)
- [Source of `Distribution.sobolevSingularSupport` in TauCeti/Analysis/Distribution/WaveFrontSet/Sobolev/SingularSupport.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Distribution/WaveFrontSet/Sobolev/SingularSupport.lean#L271)
- [Tau Ceti roadmap status: Pseudodifferential operators and elliptic analysis on bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PseudodifferentialOperators/STATUS.md)
