---
declaration: theorem
origin: cited
lean: TauCeti.PDE.UniformlyEllipticOn.ae_value_le_add_of_forall_eLpNorm_le, TauCeti.PDE.exists_ae_value_le_add_mul_div_mul_rpow
statement: formalized
proof: formalized
---

# Stampacchia's global bound

Let `Ω` have finite measure, let `a` be measurable and
uniformly elliptic on `Ω` with constants `0 < λ ≤ Λ`, and let `c` be bounded, measurable and
nonnegative. Suppose that `W^{1,2}_0(Ω)` satisfies a Sobolev inequality `‖v‖_{Lˢ} ≤ S ‖∇v‖_{L²}`,
and let `f ∈ Lʳ(Ω)` with `s (1 - 1/r) > 2`. If `u ∈ H¹(Ω)` is a weak subsolution of

`-∂ᵢ(aⁱʲ ∂ⱼu) + c u ≤ f` in `Ω`,

that is `a(u, v) ≤ ∫_Ω f v` for every nonnegative `v ∈ H¹₀(Ω)`, and `u ≤ k` on `∂Ω` for a level
`k ≥ 0`, in the sense that `(u - k)⁺ ∈ H¹₀(Ω)`, then almost everywhere in `Ω`

`u ≤ k + 2 ^ (β / (β - 1)) S² ‖f‖_{Lʳ} / λ · |Ω| ^ (1 - 1/r - 2/s)`, where `β = s (1 - 1/r) - 1`.

No regularity of `∂Ω` or of the coefficients beyond measurability is needed.

```lean
TauCeti.PDE.UniformlyEllipticOn.ae_value_le_add_of_forall_eLpNorm_le.{u_1} {ι : Type u_1}
  [Fintype ι] [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  [mu.IsAddHaarMeasure] {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
  {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {c : EuclideanSpace ℝ ι → ℝ} {lam Lam gamma : ℝ}
  (h : TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega))
  (hc : MeasureTheory.AEStronglyMeasurable c (mu.restrict ↑Omega))
  (hc_bound : ∀ x ∈ ↑Omega, ‖c x‖ ≤ gamma) (hc_nonneg : ∀ x ∈ ↑Omega, 0 ≤ c x)
  (hOmega : mu ↑Omega ≠ ⊤) {r s S : NNReal} (hr : 0 < r) (hrs : 2 < ↑s * (1 - (↑r)⁻¹))
  (hS :
    ∀ v ∈ TauCeti.w1p0Submodule mu Omega 2,
      MeasureTheory.eLpNorm (↑↑(TauCeti.W1p.value v)) (↑s) (mu.restrict ↑Omega) ≤
        ↑S * ‖TauCeti.W1p.gradient v‖ₑ)
  {f : EuclideanSpace ℝ ι → ℝ} (hf : MeasureTheory.MemLp f (↑r) (mu.restrict ↑Omega))
  {u : ↥(TauCeti.W1p mu Omega 2)}
  (hu :
    ∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
      (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, 0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
        TauCeti.PDE.energyFormH1 a 0 c u ↑v ≤
          ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, f x * ↑↑(TauCeti.W1p.value ↑v) x ∂mu)
  {k : ℝ} (hk : 0 ≤ k)
  (hboundary :
    TauCeti.W1p.posPartAbove
        TauCeti.PDE.UniformlyEllipticOn.ae_value_le_add_of_forall_eLpNorm_le._proof_1 hk u ∈
      TauCeti.w1p0Submodule mu Omega 2) :
  ∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega,
    ↑↑(TauCeti.W1p.value u) x ≤
      k +
        2 ^ ((↑s * (1 - (↑r)⁻¹) - 1) / (↑s * (1 - (↑r)⁻¹) - 2)) * ↑S ^ 2 *
              (MeasureTheory.eLpNorm f (↑r) (mu.restrict ↑Omega)).toReal /
            lam *
          mu.real ↑Omega ^ (1 - (↑r)⁻¹ - 2 / ↑s)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's inequality for Young's exponents](../../../../measure-theory/integral/part-01/holders-inequality-for-youngs-exponents.md)
- [The Sobolev inequality on `W^{1,p}_0` of a ball](../../sobolev/part-02/the-sobolev-inequality-on-w-1-p-0-of-a-ball.md)
- [Stampacchia's lemma](../../other-results/stampacchias-lemma.md)
- [TauCeti.Wkp](../../../part-01/partial-differential-equations/tauceti-wkp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.UniformlyEllipticOn.ae_value_le_add_of_forall_eLpNorm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/GlobalBoundedness.html#TauCeti.PDE.UniformlyEllipticOn.ae_value_le_add_of_forall_eLpNorm_le).

## Other forms

**Stampacchia's global bound, in every dimension.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_ae_value_le_add_mul_div_mul_rpow`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/GlobalBoundedness.html#TauCeti.PDE.exists_ae_value_le_add_mul_div_mul_rpow).

```lean
TauCeti.PDE.exists_ae_value_le_add_mul_div_mul_rpow.{u_1} {ι : Type u_1} [Fintype ι] [DecidableEq ι]
  {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure] [Nonempty ι] {r : NNReal}
  (hr : 1 < r) (hrn : ↑(Fintype.card ι) < 2 * ↑r) :
  ∃ C,
    0 < C ∧
      ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
        {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {c : EuclideanSpace ℝ ι → ℝ} {lam Lam gamma : ℝ}
        {f : EuclideanSpace ℝ ι → ℝ} {u : ↥(TauCeti.W1p mu Omega 2)} {k : ℝ} (hk : 0 ≤ k),
        mu ↑Omega ≠ ⊤ →
          TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
            MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
              MeasureTheory.AEStronglyMeasurable c (mu.restrict ↑Omega) →
                (∀ x ∈ ↑Omega, ‖c x‖ ≤ gamma) →
                  (∀ x ∈ ↑Omega, 0 ≤ c x) →
                    MeasureTheory.MemLp f (↑r) (mu.restrict ↑Omega) →
                      (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
                          (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega,
                              0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
                            TauCeti.PDE.energyFormH1 a 0 c u ↑v ≤
                              ∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
                                f x * ↑↑(TauCeti.W1p.value ↑v) x ∂mu) →
                        TauCeti.W1p.posPartAbove
                              TauCeti.PDE.UniformlyEllipticOn.ae_value_le_add_of_forall_eLpNorm_le._proof_1
                              hk u ∈
                            TauCeti.w1p0Submodule mu Omega 2 →
                          ∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega,
                            ↑↑(TauCeti.W1p.value u) x ≤
                              k +
                                C * (MeasureTheory.eLpNorm f (↑r) (mu.restrict ↑Omega)).toReal /
                                    lam *
                                  mu.real ↑Omega ^ (2 / ↑(Fintype.card ι) - (↑r)⁻¹)
```

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.UniformlyEllipticOn.ae_value_le_add_of_forall_eLpNorm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/GlobalBoundedness.html#TauCeti.PDE.UniformlyEllipticOn.ae_value_le_add_of_forall_eLpNorm_le)
- [Source of `TauCeti.PDE.UniformlyEllipticOn.ae_value_le_add_of_forall_eLpNorm_le` in TauCeti/Analysis/PDE/MaximumPrinciple/GlobalBoundedness.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/MaximumPrinciple/GlobalBoundedness.lean#L331)
