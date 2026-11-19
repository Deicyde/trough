---
declaration: theorem
origin: cited
lean: TauCeti.exists_strictMono_tendstoLocallyUniformlyOn_fderiv
statement: formalized
proof: formalized
---

# Arzelà–Ascoli in `C¹`

Let `uₙ` be differentiable on an open subset `Ω` of a
finite-dimensional space, with values in a finite-dimensional space, and converge pointwise on
`Ω` to `v`. If the derivatives `Duₙ` are equicontinuous on `Ω` and bounded at each point, then
`v` is `C¹` on `Ω` and, along a subsequence, `Duₙ → Dv` locally uniformly on `Ω`.

```lean
TauCeti.exists_strictMono_tendstoLocallyUniformlyOn_fderiv.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [ProperSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  {Ω : Set E} [FiniteDimensional ℝ E] [FiniteDimensional ℝ F] {u : ℕ → E → F} {v : E → F}
  (hΩ : IsOpen Ω) (hu : ∀ (n : ℕ), DifferentiableOn ℝ (u n) Ω)
  (hequi : EquicontinuousOn (fun n => fderiv ℝ (u n)) Ω)
  (hbd : ∀ x ∈ Ω, ∃ M, ∀ (n : ℕ), ‖fderiv ℝ (u n) x‖ ≤ M)
  (hlim : ∀ x ∈ Ω, Filter.Tendsto (fun n => u n x) Filter.atTop (nhds (v x))) :
  ∃ φ,
    StrictMono φ ∧
      ContDiffOn ℝ 1 v Ω ∧
        TendstoLocallyUniformlyOn (fun n => fderiv ℝ (u (φ n))) (fderiv ℝ v) Filter.atTop Ω
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Arzelà–Ascoli along exhausting bands](../../../../../part-02/topology/other-results/arzela-ascoli-along-exhausting-bands.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_strictMono_tendstoLocallyUniformlyOn_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Equicontinuity.html#TauCeti.exists_strictMono_tendstoLocallyUniformlyOn_fderiv).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_strictMono_tendstoLocallyUniformlyOn_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Equicontinuity.html#TauCeti.exists_strictMono_tendstoLocallyUniformlyOn_fderiv)
- [Source of `TauCeti.exists_strictMono_tendstoLocallyUniformlyOn_fderiv` in TauCeti/Analysis/Calculus/Equicontinuity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Calculus/Equicontinuity.lean#L75)
