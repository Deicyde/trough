---
declaration: theorem
origin: cited
lean: TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_of_nonpos, TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_lowerOrder_of_nonpos
statement: formalized
proof: formalized
---

# The zero-forcing Caccioppoli inequality for a positive truncation of a weak subsolution

This is the specialization of
`UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_of_memLp` to
`-∂ᵢ(aⁱʲ ∂ⱼu) ≤ 0`.

```lean
TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_of_nonpos.{u_1}
  {ι : Type u_1} [Fintype ι] [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  [mu.IsAddHaarMeasure] {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
  {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {lam Lam : ℝ}
  (h : TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega)) {u : ↥(TauCeti.W1p mu Omega 2)}
  (hu :
    ∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
      (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, 0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
        TauCeti.PDE.energyFormH1 a 0 0 u ↑v ≤ 0)
  {k : ℝ}
  (hwLp :
    MeasureTheory.MemLp (fun x => max (↑↑(TauCeti.W1p.value u) x - k) 0) 2 (mu.restrict ↑Omega))
  {ψ : EuclideanSpace ℝ ι → ℝ} (hψ : ContDiff ℝ (↑⊤) ψ) (hcpt : HasCompactSupport ψ)
  (hts : tsupport ψ ⊆ ↑Omega) :
  have w :=
    TauCeti.W1p.posPartAboveOfMemLp
      TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_of_memLp._proof_1
      k u hwLp;
  ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ψ x ^ 2 * ‖↑↑(TauCeti.W1p.gradient w) x‖ ^ 2 ∂mu ≤
    (2 * Lam / lam) ^ 2 *
      ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ‖gradient ψ x‖ ^ 2 * ↑↑(TauCeti.W1p.value w) x ^ 2 ∂mu
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.Wkp](../../../part-01/partial-differential-equations/tauceti-wkp.md)

## Informally uses

- [The Caccioppoli inequality](../part-01/the-caccioppoli-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_of_nonpos`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Caccioppoli/Truncation.html#TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_of_nonpos).

## Other forms

**The zero-forcing Caccioppoli inequality for a nonnegative-level truncation with lower-order terms.** Formalized in Tau Ceti as [`TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_lowerOrder_of_nonpos`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Caccioppoli/LowerOrder.html#TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_lowerOrder_of_nonpos).

```lean
TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_lowerOrder_of_nonpos.{u_1}
  {ι : Type u_1} [Fintype ι] [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  [mu.IsAddHaarMeasure] {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
  {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι}
  {c : EuclideanSpace ℝ ι → ℝ} {lam Lam beta gamma : ℝ}
  (h : TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega))
  (hb : MeasureTheory.AEStronglyMeasurable b (mu.restrict ↑Omega))
  (hc : MeasureTheory.AEStronglyMeasurable c (mu.restrict ↑Omega))
  (hb_bound : ∀ x ∈ ↑Omega, ‖b x‖ ≤ beta) (hc_bound : ∀ x ∈ ↑Omega, ‖c x‖ ≤ gamma)
  (hc_nonneg : ∀ x ∈ ↑Omega, 0 ≤ c x) {u : ↥(TauCeti.W1p mu Omega 2)}
  (hu :
    ∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
      (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, 0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
        TauCeti.PDE.energyFormH1 a b c u ↑v ≤ 0)
  {k : ℝ} (hk : 0 ≤ k) {ψ : EuclideanSpace ℝ ι → ℝ} (hψ : ContDiff ℝ (↑⊤) ψ)
  (hcpt : HasCompactSupport ψ) (hts : tsupport ψ ⊆ ↑Omega) :
  have w :=
    TauCeti.W1p.posPartAbove
      TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_lowerOrder_of_memLp._proof_1
      hk u;
  ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ψ x ^ 2 * ‖↑↑(TauCeti.W1p.gradient w) x‖ ^ 2 ∂mu ≤
    2 * (2 * Lam / lam) ^ 2 *
        ∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
          ‖gradient ψ x‖ ^ 2 * ↑↑(TauCeti.W1p.value w) x ^ 2 ∂mu +
      (2 * beta / lam) ^ 2 *
        ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ψ x ^ 2 * ↑↑(TauCeti.W1p.value w) x ^ 2 ∂mu
```

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_of_nonpos`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Caccioppoli/Truncation.html#TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_of_nonpos)
- [Source of `TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_of_nonpos` in TauCeti/Analysis/PDE/Caccioppoli/Truncation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Caccioppoli/Truncation.lean#L178)
