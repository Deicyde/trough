---
declaration: theorem
origin: cited
lean: TauCeti.FredholmDetLine.vectorBundle
statement: formalized
proof: formalized
---

# The determinant line bundle

The determinant lines of the Fredholm operators from `E` to
`F` form a vector bundle of rank one over the space of Fredholm operators.

```lean
TauCeti.FredholmDetLine.vectorBundle.{u_1, u_2, u_3} (𝕜 : Type u_1) (E : Type u_2) (F : Type u_3)
  [NontriviallyNormedField 𝕜] [CompleteSpace 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [CompleteSpace E] [NormedAddCommGroup F] [NormedSpace 𝕜 F] [CompleteSpace F] :
  VectorBundle 𝕜 𝕜 (TauCeti.FredholmDetLine 𝕜 E F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FredholmDetLine.vectorBundle`](https://taucetiproject.org/docs/TauCeti/Analysis/Fredholm/DeterminantLine/Bundle.html#TauCeti.FredholmDetLine.vectorBundle).

## Sources

- [Tau Ceti documentation: `TauCeti.FredholmDetLine.vectorBundle`](https://taucetiproject.org/docs/TauCeti/Analysis/Fredholm/DeterminantLine/Bundle.html#TauCeti.FredholmDetLine.vectorBundle)
- [Source of `TauCeti.FredholmDetLine.vectorBundle` in TauCeti/Analysis/Fredholm/DeterminantLine/Bundle.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Fredholm/DeterminantLine/Bundle.lean#L328)
- [Tau Ceti roadmap status: Analytic Heegaard Floer homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HeegaardFloer/STATUS.md)
