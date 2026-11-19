---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.comp_homotopyPullbackCLM_comp_extDerivCLM
statement: formalized
proof: formalized
---

# The homotopy formula

for a `(k + 1)`-current `T` on `Ω`,
`∂ H_# ([[0, 1]] × T) = H₁# T - H₀# T - H_# ([[0, 1]] × ∂ T)`, where
`H_# ([[0, 1]] × T) = T ∘ K` for the homotopy operator `K`, `Hₜ# T = T ∘ Hₜ^*` and `∂ T = T ∘ d`.

```lean
ContinuousLinearMap.comp_homotopyPullbackCLM_comp_extDerivCLM.{u_1, u_2, u_3, u_4} {E : Type u_1}
  {E' : Type u_2} {F : Type u_3} {G : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [NormedAddCommGroup E'] [NormedSpace ℝ E'] [NormedAddCommGroup F] [NormedSpace ℝ F]
  [CompleteSpace F] [AddCommGroup G] [_root_.Module ℝ G] [TopologicalSpace G]
  [IsTopologicalAddGroup G] {Ω : TopologicalSpace.Opens E} {Ω' : TopologicalSpace.Opens E'}
  {H : E × ℝ → E'} {k : ℕ} {hH : ∀ p ∈ ↑Ω ×ˢ Set.Icc 0 1, ContDiffAt ℝ (↑⊤) H p}
  {hHp : ∀ (K : Set E'), IsCompact K → K ⊆ ↑Ω' → IsCompact (↑Ω ×ˢ Set.Icc 0 1 ∩ H ⁻¹' K)}
  (T : TestFunction Ω (E [⋀^Fin (k + 1)]→L[ℝ] F) ⊤ →L[ℝ] G) :
  (T ∘SL TestFunction.homotopyPullbackCLM hH hHp) ∘SL TestFunction.extDerivCLM =
    T ∘SL TestFunction.pullbackCLM (fun x => H (x, 1)) ⋯ ⋯ -
        T ∘SL TestFunction.pullbackCLM (fun x => H (x, 0)) ⋯ ⋯ -
      (T ∘SL TestFunction.extDerivCLM) ∘SL TestFunction.homotopyPullbackCLM hH hHp
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.comp_homotopyPullbackCLM_comp_extDerivCLM`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/Homotopy.html#ContinuousLinearMap.comp_homotopyPullbackCLM_comp_extDerivCLM).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.comp_homotopyPullbackCLM_comp_extDerivCLM`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/Homotopy.html#ContinuousLinearMap.comp_homotopyPullbackCLM_comp_extDerivCLM)
- [Source of `ContinuousLinearMap.comp_homotopyPullbackCLM_comp_extDerivCLM` in TauCeti/Analysis/Distribution/TestFunction/Homotopy.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Distribution/TestFunction/Homotopy.lean#L416)
- [Tau Ceti roadmap status: Integral currents, geometric homology and minimizing hypersurfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricCurrents/STATUS.md)
