---
declaration: def
origin: cited
lean: Distribution.IsNormal
statement: formalized
---

# Distribution.IsNormal

A current `T` on the test `k`-forms on `Ω` is *normal* if both `T` and its boundary
`∂T = T ∘ d` have finite mass. The boundary of a `0`-current is zero, so in degree zero this is
finiteness of the mass of `T`. No support condition is imposed.

```lean
Distribution.IsNormal.{u_1, u_2, u_3} {E : Type u_1} {F : Type u_2} {V : Type u_3}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  [NormedAddCommGroup V] [NormedSpace ℝ V] {Ω : TopologicalSpace.Opens E} {k : ℕ} :
  (TestFunction Ω (E [⋀^Fin k]→L[ℝ] F) ⊤ →L[ℝ] V) → Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Distribution.IsNormal`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Mass/Normal.html#Distribution.IsNormal).

## Sources

- [Tau Ceti documentation: `Distribution.IsNormal`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Mass/Normal.html#Distribution.IsNormal)
- [Source of `Distribution.IsNormal` in TauCeti/Analysis/Distribution/Mass/Normal.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Distribution/Mass/Normal.lean#L77)
- [Tau Ceti roadmap status: Integral currents, geometric homology and minimizing hypersurfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricCurrents/STATUS.md)
