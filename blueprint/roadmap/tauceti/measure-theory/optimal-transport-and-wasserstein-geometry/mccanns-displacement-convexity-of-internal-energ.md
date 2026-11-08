---
declaration: theorem
origin: cited
lean: TauCeti.internalEnergy_map_smul_add_smul_gradient_le
statement: formalized
proof: formalized
---

# McCann's displacement convexity of internal energies

Let `E` be a real inner product space
of finite dimension `n ≥ 1` with an additive Haar measure `ρ`, and let `U : ℝ → ℝ` satisfy
`U 0 = 0` and McCann's condition: `s ↦ sⁿ U(s⁻ⁿ)` is convex and nonincreasing on `(0, ∞)`. Let
`f : E → EReal` be convex (convex real epigraph, never `⊥`), with real representative `F`, and let
`μ` be a σ-finite measure, absolutely continuous with respect to `ρ` and carried by the interior of
the effective domain of `f`. Then the internal energy is convex along the interpolation
`μₜ = (Tₜ)₊ μ`, `Tₜ x = (1 - t) • x + t • ∇F x`:
`𝓤(μₜ) ≤ (1 - t) 𝓤(μ) + t 𝓤((∇F)₊ μ)` for `t ∈ [0, 1]`, provided neither endpoint has energy `⊥`.
The endpoint `(∇F)₊ μ` need not be absolutely continuous; its singular part is charged at the
recession constant `U'(∞)`.

```lean
TauCeti.internalEnergy_map_smul_add_smul_gradient_le.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  (ρ : MeasureTheory.Measure E) [ρ.IsAddHaarMeasure] {f : E → EReal} {U : ℝ → ℝ} [Nontrivial E]
  (hU0 : U 0 = 0)
  (hc : ConvexOn ℝ (Set.Ioi 0) fun s => s ^ Module.finrank ℝ E * U (s ^ Module.finrank ℝ E)⁻¹)
  (ha : AntitoneOn (fun s => s ^ Module.finrank ℝ E * U (s ^ Module.finrank ℝ E)⁻¹) (Set.Ioi 0))
  (hf : Convex ℝ {p | f p.1 ≤ ↑p.2}) (hbot : ∀ (x : E), f x ≠ ⊥) {μ : MeasureTheory.Measure E}
  [MeasureTheory.SigmaFinite μ] (hμ : μ.AbsolutelyContinuous ρ)
  (hμD : ∀ᵐ (x : E) ∂μ, x ∈ interior {x | f x ≠ ⊤}) (h₀ : TauCeti.internalEnergy U ρ μ ≠ ⊥)
  (h₁ :
    TauCeti.internalEnergy U ρ (MeasureTheory.Measure.map (gradient fun x' => (f x').toReal) μ) ≠ ⊥)
  {t : ℝ} (ht : t ∈ Set.Icc 0 1) :
  TauCeti.internalEnergy U ρ
      (MeasureTheory.Measure.map (fun x => (1 - t) • x + t • gradient (fun x' => (f x').toReal) x)
        μ) ≤
    ↑(1 - t) * TauCeti.internalEnergy U ρ μ +
      ↑t *
        TauCeti.internalEnergy U ρ (MeasureTheory.Measure.map (gradient fun x' => (f x').toReal) μ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Fenchel–Young inequality](../../analysis/part-02/convex/the-fenchel-young-inequality.md)
- [Lebesgue decomposition of the Monge–Ampère measure](../../analysis/part-02/convex/lebesgue-decomposition-of-the-monge-ampere-measu.md)
- [Minkowski's determinant inequality](../../analysis/part-02/matrix/minkowskis-determinant-inequality.md)
- [Rademacher's theorem for extended-real convex functions](../../analysis/part-02/convex/rademachers-theorem-for-extended-real-convex-fun.md)
- [Rademacher's theorem for locally Lipschitz functions](../../analysis/part-02/calculus/part-01/rademachers-theorem-for-locally-lipschitz-functi.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.internalEnergy_map_smul_add_smul_gradient_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/InternalEnergy/DisplacementConvexity.html#TauCeti.internalEnergy_map_smul_add_smul_gradient_le).

## Sources

- [Tau Ceti documentation: `TauCeti.internalEnergy_map_smul_add_smul_gradient_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/InternalEnergy/DisplacementConvexity.html#TauCeti.internalEnergy_map_smul_add_smul_gradient_le)
- [Source of `TauCeti.internalEnergy_map_smul_add_smul_gradient_le` in TauCeti/MeasureTheory/OptimalTransport/Wasserstein/InternalEnergy/DisplacementConvexity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/InternalEnergy/DisplacementConvexity.lean#L344)
- [Tau Ceti roadmap status: Optimal transport and Wasserstein geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OptimalTransport/STATUS.md)
