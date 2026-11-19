---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_uniformlyEllipticOn_energyFormH1_eq_zero_tendsto_div
statement: formalized
proof: formalized
---

# Hopf's lemma fails for measurable divergence-form coefficients

Let `Λ > 1` and let
`Ω ⊆ ℝ²` be a bounded open set in the half-plane `0 < x₀`, for instance the half disc, whose
boundary point `0` has an interior disc with inward normal `e₀`. Then there is a strongly
measurable coefficient field `a`, uniformly elliptic on `Ω` with constants `1` and `Λ`, and a
weak solution `u ∈ H¹(Ω)` of `div(a ∇u) = 0` on `Ω` with a continuous representative `ū` that is
positive on `Ω` and vanishes at `0`, such that the inward difference quotients `ū(t e₀) / t`
tend to `0` as `t → 0⁺`. So the conclusion of Hopf's lemma, a positive lower bound for these
quotients, fails. The field is Meyers' coefficient with `s = √Λ`
(`TauCeti.PDE.meyersCoefficient`), which has no limit at `0` within the half-plane
(`TauCeti.PDE.not_exists_tendsto_meyersCoefficient`).

```lean
TauCeti.PDE.exists_uniformlyEllipticOn_energyFormH1_eq_zero_tendsto_div {Λ : ℝ} (hΛ : 1 < Λ)
  {Ω : TopologicalSpace.Opens (EuclideanSpace ℝ (Fin 2))} (hb : Bornology.IsBounded ↑Ω)
  (hΩ : ↑Ω ⊆ {x | 0 < x.ofLp 0}) :
  ∃ a,
    MeasureTheory.StronglyMeasurable a ∧
      TauCeti.PDE.UniformlyEllipticOn (↑Ω) a 1 Λ ∧
        ∃ u ū,
          ↑↑(TauCeti.W1p.value u) =ᵐ[MeasureTheory.volume.restrict ↑Ω] ū ∧
            (∀ (v : ↥(TauCeti.W1p0 MeasureTheory.volume Ω 2)),
                TauCeti.PDE.energyFormH1 a 0 0 u ↑v = 0) ∧
              Continuous ū ∧
                ū 0 = 0 ∧
                  (∀ x ∈ ↑Ω, 0 < ū x) ∧
                    Filter.Tendsto (fun t => ū (t • EuclideanSpace.single 0 1) / t)
                      (nhdsWithin 0 (Set.Ioi 0)) (nhds 0)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_uniformlyEllipticOn_energyFormH1_eq_zero_tendsto_div`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/HalfDisk.html#TauCeti.PDE.exists_uniformlyEllipticOn_energyFormH1_eq_zero_tendsto_div).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_uniformlyEllipticOn_energyFormH1_eq_zero_tendsto_div`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/HalfDisk.html#TauCeti.PDE.exists_uniformlyEllipticOn_energyFormH1_eq_zero_tendsto_div)
- [Source of `TauCeti.PDE.exists_uniformlyEllipticOn_energyFormH1_eq_zero_tendsto_div` in TauCeti/Analysis/PDE/MaximumPrinciple/HalfDisk.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/MaximumPrinciple/HalfDisk.lean#L89)
