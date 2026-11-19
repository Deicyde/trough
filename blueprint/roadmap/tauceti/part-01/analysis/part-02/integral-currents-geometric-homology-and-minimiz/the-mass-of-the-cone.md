---
declaration: theorem
origin: cited
lean: Distribution.mass_cone_le
statement: formalized
proof: formalized
---

# The mass of the cone

if the support of a `k`-current `T` of finite mass lies in the closed
ball of radius `r` about `p`, then `M(δ_p × T) ≤ r M(T) / (k + 1)`.

```lean
Distribution.mass_cone_le.{u_1, u_2, u_4} {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F]
  {Ω : TopologicalSpace.Opens E} {k : ℕ} {p : E} [FiniteDimensional ℝ E] {V : Type u_4}
  [NormedAddCommGroup V] [NormedSpace ℝ V] (T : TestFunction Ω (E [⋀^Fin k]→L[ℝ] F) ⊤ →L[ℝ] V)
  {r : NNReal} (hr : Distribution.dsupport ⇑T ⊆ Metric.closedBall p ↑r)
  (hT : Distribution.mass ⇑T ≠ ⊤) :
  Distribution.mass ⇑(Distribution.cone p T) ≤ ↑(r / (↑k + 1)) * Distribution.mass ⇑T
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Distribution.mass_cone_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/Cone.html#Distribution.mass_cone_le).

## Sources

- [Tau Ceti documentation: `Distribution.mass_cone_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/Cone.html#Distribution.mass_cone_le)
- [Source of `Distribution.mass_cone_le` in TauCeti/Analysis/Distribution/TestFunction/Cone.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Distribution/TestFunction/Cone.lean#L803)
- [Tau Ceti roadmap status: Integral currents, geometric homology and minimizing hypersurfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricCurrents/STATUS.md)
