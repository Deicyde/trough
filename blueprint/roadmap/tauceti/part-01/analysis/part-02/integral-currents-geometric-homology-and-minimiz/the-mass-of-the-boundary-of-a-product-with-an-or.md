---
declaration: theorem
origin: cited
lean: Distribution.mass_comp_intervalCylinderHomotopyCLM_comp_extDerivCLM_le
statement: formalized
proof: formalized
---

# The mass of the boundary of a product with an oriented interval

`M(∂ ([[a, b]] × T)) ≤ 2 M(T) + |b - a| M(∂ T)` for a `(k + 1)`-current `T` on `Ω`, where
`[[a, b]] × T = T ∘ h_{a,b}` and `∂ T = T ∘ d`, for the sup norm on `E × ℝ`.

```lean
Distribution.mass_comp_intervalCylinderHomotopyCLM_comp_extDerivCLM_le.{u_1, u_2, u_3}
  {E : Type u_1} {F : Type u_2} {V : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] [NormedAddCommGroup V]
  [NormedSpace ℝ V] {Ω : TopologicalSpace.Opens E} {W : TopologicalSpace.Opens (E × ℝ)} {k : ℕ}
  {a b : ℝ} {hW : ∀ p ∈ W, p.2 ∈ Set.uIcc a b → p.1 ∈ Ω}
  (T : TestFunction Ω (E [⋀^Fin (k + 1)]→L[ℝ] F) ⊤ →L[ℝ] V) :
  Distribution.mass
      ⇑((T ∘SL TestFunction.intervalCylinderHomotopyCLM a b hW) ∘SL TestFunction.extDerivCLM) ≤
    2 * Distribution.mass ⇑T + ‖b - a‖ₑ * Distribution.mass ⇑(T ∘SL TestFunction.extDerivCLM)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Distribution.mass_comp_intervalCylinderHomotopyCLM_comp_extDerivCLM_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/CylinderHomotopy.html#Distribution.mass_comp_intervalCylinderHomotopyCLM_comp_extDerivCLM_le).

## Sources

- [Tau Ceti documentation: `Distribution.mass_comp_intervalCylinderHomotopyCLM_comp_extDerivCLM_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/CylinderHomotopy.html#Distribution.mass_comp_intervalCylinderHomotopyCLM_comp_extDerivCLM_le)
- [Source of `Distribution.mass_comp_intervalCylinderHomotopyCLM_comp_extDerivCLM_le` in TauCeti/Analysis/Distribution/TestFunction/CylinderHomotopy.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Distribution/TestFunction/CylinderHomotopy.lean#L707)
- [Tau Ceti roadmap status: Integral currents, geometric homology and minimizing hypersurfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricCurrents/STATUS.md)
