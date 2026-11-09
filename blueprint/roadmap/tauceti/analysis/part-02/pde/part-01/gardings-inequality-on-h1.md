---
declaration: theorem
origin: cited
lean: TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self, TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self_norm_of_norm_le, TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self_norm
statement: formalized
proof: formalized
---

# Gårding's inequality on `H¹(Ω)`

For a uniformly elliptic principal coefficient with
lower constant `λ`, a drift bounded by `β` and a nonnegative mass coefficient,

`(λ/2)‖∇u‖²_{L²} - (β²/2λ)‖u‖²_{L²} ≤ a(u, u)`

for every `u ∈ H¹(Ω)`. The drift is absorbed by Young's inequality at the cost of half of the
ellipticity floor, which is where the negative `L²` term comes from. Under the stated general
assumption `c ≥ 0`, either a Poincaré inequality or a sufficiently positive mass lower bound is
needed to eliminate that term.

```lean
TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self.{u_1} {ι : Type u_1} [Fintype ι]
  {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {c : EuclideanSpace ℝ ι → ℝ}
  {lam Lam beta gamma : ℝ} [mu.IsAddHaarMeasure] [DecidableEq ι]
  (h : TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega))
  (hb : MeasureTheory.AEStronglyMeasurable b (mu.restrict ↑Omega))
  (hc : MeasureTheory.AEStronglyMeasurable c (mu.restrict ↑Omega))
  (hb_bound : ∀ x ∈ ↑Omega, ‖b x‖ ≤ beta) (hc_bound : ∀ x ∈ ↑Omega, ‖c x‖ ≤ gamma)
  (hc_nonneg : ∀ x ∈ ↑Omega, 0 ≤ c x) (u : ↥(TauCeti.W1p mu Omega 2)) :
  lam / 2 * ‖TauCeti.W1p.gradient u‖ ^ 2 - beta ^ 2 / (2 * lam) * ‖TauCeti.W1p.value u‖ ^ 2 ≤
    TauCeti.PDE.energyFormH1 a b c u u
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/EnergyForm/Sobolev.html#TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self).

## Other forms

**Gårding's inequality in `H¹`-norm form, without a sign condition on `c`.** Formalized in Tau Ceti as [`TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self_norm_of_norm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/EnergyForm/Sobolev.html#TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self_norm_of_norm_le).

```lean
TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self_norm_of_norm_le.{u_1} {ι : Type u_1}
  [Fintype ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {c : EuclideanSpace ℝ ι → ℝ}
  {lam Lam beta gamma : ℝ} [mu.IsAddHaarMeasure] [DecidableEq ι]
  (h : TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega))
  (hb : MeasureTheory.AEStronglyMeasurable b (mu.restrict ↑Omega))
  (hc : MeasureTheory.AEStronglyMeasurable c (mu.restrict ↑Omega))
  (hb_bound : ∀ x ∈ ↑Omega, ‖b x‖ ≤ beta) (hc_bound : ∀ x ∈ ↑Omega, ‖c x‖ ≤ gamma)
  (u : ↥(TauCeti.W1p mu Omega 2)) :
  lam / 2 * ‖u‖ ^ 2 - (lam / 2 + gamma + beta ^ 2 / (2 * lam)) * ‖TauCeti.W1p.value u‖ ^ 2 ≤
    TauCeti.PDE.energyFormH1 a b c u u
```

**Gårding's inequality in the roadmap's `H¹`-norm form.** Formalized in Tau Ceti as [`TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/EnergyForm/Sobolev.html#TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self_norm).

```lean
TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self_norm.{u_1} {ι : Type u_1} [Fintype ι]
  {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {c : EuclideanSpace ℝ ι → ℝ}
  {lam Lam beta gamma : ℝ} [mu.IsAddHaarMeasure] [DecidableEq ι]
  (h : TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega))
  (hb : MeasureTheory.AEStronglyMeasurable b (mu.restrict ↑Omega))
  (hc : MeasureTheory.AEStronglyMeasurable c (mu.restrict ↑Omega))
  (hb_bound : ∀ x ∈ ↑Omega, ‖b x‖ ≤ beta) (hc_bound : ∀ x ∈ ↑Omega, ‖c x‖ ≤ gamma)
  (hc_nonneg : ∀ x ∈ ↑Omega, 0 ≤ c x) (u : ↥(TauCeti.W1p mu Omega 2)) :
  lam / 2 * ‖u‖ ^ 2 - (lam / 2 + beta ^ 2 / (2 * lam)) * ‖TauCeti.W1p.value u‖ ^ 2 ≤
    TauCeti.PDE.energyFormH1 a b c u u
```

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/EnergyForm/Sobolev.html#TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self)
- [Source of `TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self` in TauCeti/Analysis/PDE/EnergyForm/Sobolev.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/EnergyForm/Sobolev.lean#L948)
