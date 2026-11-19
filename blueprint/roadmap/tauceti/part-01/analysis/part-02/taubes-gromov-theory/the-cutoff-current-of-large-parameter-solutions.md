---
declaration: theorem
origin: cited
lean: TauCeti.SeibergWitten.exists_mass_integral_wedge_le_of_inner_ιMulti_eq
statement: formalized
proof: formalized
---

# The cutoff current of large-parameter solutions has `r`-independent mass

Work on an
open set `Ω` of finite volume in an oriented four-dimensional inner product space with a constant
unitary frame `e`, `J e₀ = e₁`, `J e₂ = e₃`. Fix constants `C, N ≥ 0` and a cutoff `χ` with
values in `[0, 1]` and `0 ≤ χ' ≤ M`. There are `A` and `r₀` such that for every `r ≥ r₀` and
every solution of the large-parameter curvature equation
`F + ⋆F = (r / 4) ω - q(√r (φ + β)) - η` on `Ω` satisfying the coarse bounds of
`TauCeti.SeibergWitten.norm_le_mul_max_one_sub_add_of_inner_ιMulti_eq` and
`r ∫_Ω |1 - |φ|² - |β|²| ≤ C`, the current `ζ ↦ ∫ Θ ∧ ζ` of the cutoff current `Θ` on test
two-forms on `Ω` has mass at most `A`. The top-degree coefficients are taken on a basis `b` and
integrated against its Haar measure. Unlike
`TauCeti.SeibergWitten.exists_mass_integral_wedge_le_of_add_hodgeStar_eq`, only the coarse
anti-self-dual bound is assumed.

```lean
TauCeti.SeibergWitten.exists_mass_integral_wedge_le_of_inner_ιMulti_eq.{u_4, u_5} {V : Type u_4}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [Fact (Module.finrank ℝ V = 4)]
  {Q : QuadraticForm ℝ V} {o : Orientation ℝ V (Fin 4)} {W : Type u_5} [NormedAddCommGroup W]
  [InnerProductSpace ℂ W] [FiniteDimensional ℂ W] {ρ : CliffordAlgebra Q →ₐ[ℝ] Module.End ℂ W}
  {e : OrthonormalBasis (Fin 4) ℝ V} {J : TauCeti.AlmostComplexStructure V}
  (h₀ : J.toLinearMap (e 0) = e 1) (h₂₃ : J.toLinearMap (e 2) = e 3)
  (hQ : ∀ (v : V), Q v = -‖v‖ ^ 2) (hkl : 2 + 2 = Module.finrank ℝ V)
  (he : e.toBasis.orientation = o)
  (hρ : ∀ (v : V), LinearMap.adjoint (ρ ((CliffordAlgebra.ι Q) v)) = -ρ ((CliffordAlgebra.ι Q) v))
  (h₂ : Module.finrank ℂ ↥(CliffordAlgebra.positiveHalfSpinors o ρ) = 2) {χ : ℝ → ℝ} {C M N : ℝ}
  [MeasurableSpace V] [BorelSpace V] (b : Module.Basis (Fin (2 + 2)) ℝ V)
  {Ω : TopologicalSpace.Opens V} (hΩ : b.addHaar ↑Ω ≠ ⊤) (hC : 0 ≤ C) (hN : 0 ≤ N)
  (hχ : ∀ (s : ℝ), χ s ∈ Set.Icc 0 1) (hχ' : ∀ (s : ℝ), deriv χ s ∈ Set.Icc 0 M) :
  ∃ A r₀,
    ∀ ⦃r : ℝ⦄ ⦃F η Θ : V → ↥(⋀[ℝ]^2 V)⦄ ⦃φ β : V → ↥(CliffordAlgebra.positiveHalfSpinors o ρ)⦄
      ⦃Dα : V → V →L[ℝ] ℂ⦄,
      r₀ ≤ r →
        MeasureTheory.AEStronglyMeasurable Θ (b.addHaar.restrict ↑Ω) →
          MeasureTheory.IntegrableOn (fun x => 1 - ‖φ x‖ ^ 2 - ‖β x‖ ^ 2) (↑Ω) b.addHaar →
            r * ∫ (x : V) in ↑Ω, |1 - ‖φ x‖ ^ 2 - ‖β x‖ ^ 2| ∂b.addHaar ≤ C →
              (∀ x ∈ Ω, (TauCeti.SeibergWitten.cliffordProjection o ρ J.kahlerForm) (φ x) = φ x) →
                (∀ x ∈ Ω, (TauCeti.SeibergWitten.cliffordProjection o ρ J.kahlerForm) (β x) = 0) →
                  (∀ x ∈ Ω,
                      F x + (o.hodgeStar hkl) (F x) =
                        (r / 4) • J.kahlerForm -
                            ↑(TauCeti.SeibergWitten.quadraticTwoForm o ρ hkl (↑√r • (φ x + β x))) -
                          η x) →
                    (∀ x ∈ Ω, ‖η x‖ ≤ N) →
                      (∀ x ∈ Ω,
                          ‖2⁻¹ • (F x - (o.hodgeStar hkl) (F x))‖ ≤
                            r / (4 * √2) * (1 + C / √r) * max (1 - ‖φ x‖ ^ 2) 0 + C) →
                        (∀ x ∈ Ω,
                            ∀ (u w : V),
                              inner ℝ (Θ x) ((exteriorPower.ιMulti ℝ 2) ![u, w]) =
                                (1 - χ (‖φ x‖ ^ 2)) *
                                    inner ℝ (F x) ((exteriorPower.ιMulti ℝ 2) ![u, w]) +
                                  2 * deriv χ (‖φ x‖ ^ 2) *
                                    ((starRingEnd ℂ) ((Dα x) u) * (Dα x) w).im) →
                          (∀ x ∈ Ω, ‖φ x‖ ^ 2 + ‖β x‖ ^ 2 ≤ 1 + C / r) →
                            (∀ x ∈ Ω, ‖β x‖ ^ 2 ≤ C / r * max (1 - ‖φ x‖ ^ 2) 0 + C / r ^ 2) →
                              (∀ x ∈ Ω, ‖Dα x‖ ^ 2 ≤ C * r * max (1 - ‖φ x‖ ^ 2) 0 + C) →
                                ∀ (m : ℕ∞),
                                  (Distribution.mass fun ζ =>
                                      ∫ (x : V),
                                        (((TauCeti.alternatingFormEquiv V 2) (Θ x)).wedge (ζ x))
                                          ⇑b ∂b.addHaar) ≤
                                    ENNReal.ofReal A
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hadamard's inequality](../../../number-theory/part-02/successive-minima-and-minkowskis-theorems/hadamards-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SeibergWitten.exists_mass_integral_wedge_le_of_inner_ιMulti_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/CurrentMass.html#TauCeti.SeibergWitten.exists_mass_integral_wedge_le_of_inner_%CE%B9Multi_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.SeibergWitten.exists_mass_integral_wedge_le_of_inner_ιMulti_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/CurrentMass.html#TauCeti.SeibergWitten.exists_mass_integral_wedge_le_of_inner_%CE%B9Multi_eq)
- [Source of `TauCeti.SeibergWitten.exists_mass_integral_wedge_le_of_inner_ιMulti_eq` in TauCeti/Analysis/PDE/SeibergWitten/CurrentMass.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/SeibergWitten/CurrentMass.lean#L429)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TaubesGromov/STATUS.md)
