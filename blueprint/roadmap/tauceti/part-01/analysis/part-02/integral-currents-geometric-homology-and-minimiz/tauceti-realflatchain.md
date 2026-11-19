---
declaration: abbrev
origin: cited
lean: TauCeti.RealFlatChain
statement: formalized
---

# TauCeti.RealFlatChain

The real normal flat completion, using the native uniform-space completion.
This is not the integral-decomposition flat completion.

```lean
TauCeti.RealFlatChain.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  (Ω : TopologicalSpace.Opens E) (k : ℕ) : Type u_1
```

## Depends on

- [Distribution.IsNormal](distribution-isnormal.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RealFlatChain`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Flat/Completion.html#TauCeti.RealFlatChain).

## Sources

- [Tau Ceti documentation: `TauCeti.RealFlatChain`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Flat/Completion.html#TauCeti.RealFlatChain)
- [Source of `TauCeti.RealFlatChain` in TauCeti/Analysis/Distribution/Flat/Completion.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Distribution/Flat/Completion.lean#L164)
- [Tau Ceti roadmap status: Integral currents, geometric homology and minimizing hypersurfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricCurrents/STATUS.md)
