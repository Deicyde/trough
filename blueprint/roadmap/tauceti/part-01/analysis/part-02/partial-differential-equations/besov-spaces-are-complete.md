---
declaration: theorem
origin: cited
lean: TauCeti.BesovSpace.instCompleteSpace
statement: formalized
proof: formalized
---

# Besov spaces are complete

For `1 ≤ q`, the Besov space `B^s_{p,q}` is a Banach space.

```lean
TauCeti.BesovSpace.instCompleteSpace.{u_1, u_2} {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  [NormedAddCommGroup F] [NormedSpace ℂ F] [CompleteSpace F] {φ : ContDiffBump 0} {s : ℝ}
  {p q : ENNReal} [Fact (1 ≤ p)] [Fact (1 ≤ q)] : CompleteSpace (TauCeti.BesovSpace F φ s p q)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Plancherel's theorem for the inverse Fourier transform of Schwartz functions](../../part-03/distribution/plancherels-theorem-for-the-inverse-fourier-tran.md)
- [The weighted Plancherel bound](../../part-03/distribution/the-weighted-plancherel-bound.md)
- [Young's convolution inequality](../../part-03/convolution/youngs-convolution-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BesovSpace.instCompleteSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/FunctionalSpaces/BesovSpace/Basic.html#TauCeti.BesovSpace.instCompleteSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.BesovSpace.instCompleteSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/FunctionalSpaces/BesovSpace/Basic.html#TauCeti.BesovSpace.instCompleteSpace)
- [Source of `TauCeti.BesovSpace.instCompleteSpace` in TauCeti/Analysis/FunctionalSpaces/BesovSpace/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/FunctionalSpaces/BesovSpace/Basic.lean#L809)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PDE/STATUS.md)
