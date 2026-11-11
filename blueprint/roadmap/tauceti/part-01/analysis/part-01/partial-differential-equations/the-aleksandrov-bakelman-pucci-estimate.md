---
declaration: theorem
origin: cited
lean: TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow, TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow_of_wkp, TauCeti.PDE.volume_ball_le_setLIntegral_upperContactSet_of_wkp, TauCeti.PDE.volume_ball_le_setLIntegral_upperContactSet
statement: formalized
proof: formalized
---

# The Aleksandrov–Bakelman–Pucci estimate

**The Aleksandrov–Bakelman–Pucci estimate** (Gilbarg–Trudinger, Lemma 9.3 and Theorem 9.1
without drift). Let `Ω ⊆ ℝⁿ`, `n ≥ 1`, be bounded and open, let `u` be continuous on `closure Ω`
and `C²` in `Ω`, and let `m` bound `u` on `frontier Ω`. Suppose that on the upper contact set
`Γ⁺` the matrices `a y` are positive definite and `f y ≤ ∑ᵢⱼ aⁱʲ(y) ∂ᵢ∂ⱼu(y)`, and that
`f⁻ / D*`, with `D* = (det a)^{1/n}`, lies in `Lⁿ(Γ⁺)`. Then on `Ω`,
`u ≤ m + diam Ω / (n ωₙ^{1/n}) ‖f⁻ / D*‖_{Lⁿ(Γ⁺)}`, where `ωₙ` is the volume of the unit ball.

```lean
TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow.{u_1} {ι : Type u_1} [Fintype ι] [DecidableEq ι]
  {Ω : Set (EuclideanSpace ℝ ι)} {u f : EuclideanSpace ℝ ι → ℝ}
  {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {m : ℝ} {x : EuclideanSpace ℝ ι} [Nonempty ι]
  (hΩb : Bornology.IsBounded Ω) (hΩ : IsOpen Ω) (hcont : ContinuousOn u (closure Ω))
  (hu : ContDiffOn ℝ 2 u Ω) (ha : ∀ y ∈ TauCeti.PDE.upperContactSet u Ω, (a y).PosDef)
  (hf :
    ∀ y ∈ TauCeti.PDE.upperContactSet u Ω,
      f y ≤
        ∑ i,
          ∑ j,
            a y i j *
              ((fderiv ℝ (fderiv ℝ u) y) (EuclideanSpace.single i 1)) (EuclideanSpace.single j 1))
  (hg :
    MeasureTheory.MemLp (fun y => (f y)⁻ / (a y).det ^ (↑(Fintype.card ι))⁻¹) (↑(Fintype.card ι))
      (MeasureTheory.volume.restrict (TauCeti.PDE.upperContactSet u Ω)))
  (hm : ∀ z ∈ frontier Ω, u z ≤ m) (hx : x ∈ Ω) :
  u x ≤
    m +
      Metric.diam Ω /
          (↑(Fintype.card ι) *
            (MeasureTheory.volume (Metric.ball 0 1)).toReal ^ (↑(Fintype.card ι))⁻¹) *
        (MeasureTheory.eLpNorm (fun y => (f y)⁻ / (a y).det ^ (↑(Fintype.card ι))⁻¹)
            (↑(Fintype.card ι))
            (MeasureTheory.volume.restrict (TauCeti.PDE.upperContactSet u Ω))).toReal
```

## Depends on

- [TauCeti.Wkp](tauceti-wkp.md)

## Proof depends on

- [The Aleksandrov measure estimate (Gilbarg–Trudinger, Lemma 9.2)](../../part-03/pde/part-01/the-aleksandrov-measure-estimate-gilbarg-truding.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/AleksandrovBakelmanPucci/Basic.html#TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow).

## Other forms

**The Aleksandrov–Bakelman–Pucci estimate for strong subsolutions.** Formalized in Tau Ceti as [`TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow_of_wkp`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/AleksandrovBakelmanPucci/Sobolev.html#TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow_of_wkp).

```lean
TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow_of_wkp.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] {Ω : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {ū f : EuclideanSpace ℝ ι → ℝ}
  {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {m : ℝ} {x : EuclideanSpace ℝ ι} {p : ENNReal}
  [Fact (1 ≤ p)] (hΩb : Bornology.IsBounded ↑Ω) (hp : p = ↑(Fintype.card ι))
  (u : TauCeti.Wkp MeasureTheory.volume Ω p 2) (hcont : ContinuousOn ū (closure ↑Ω))
  (hū : ↑↑(TauCeti.Wkp.value 2 u) =ᵐ[MeasureTheory.volume.restrict ↑Ω] ū)
  (ha :
    ∀ᵐ (y : EuclideanSpace ℝ ι) ∂MeasureTheory.volume.restrict (TauCeti.PDE.upperContactSet ū ↑Ω),
      (a y).PosDef)
  (hf :
    ∀ᵐ (y : EuclideanSpace ℝ ι) ∂MeasureTheory.volume.restrict (TauCeti.PDE.upperContactSet ū ↑Ω),
      f y ≤
        ∑ i,
          ∑ j,
            a y i j * ((↑↑(TauCeti.Wkp.iteratedGradient 1 u) y) (EuclideanSpace.single j 1)).ofLp i)
  (hg :
    MeasureTheory.MemLp (fun y => (f y)⁻ / (a y).det ^ (↑(Fintype.card ι))⁻¹) (↑(Fintype.card ι))
      (MeasureTheory.volume.restrict (TauCeti.PDE.upperContactSet ū ↑Ω)))
  (hm : ∀ z ∈ frontier ↑Ω, ū z ≤ m) (hx : x ∈ Ω) :
  ū x ≤
    m +
      Metric.diam ↑Ω /
          (↑(Fintype.card ι) *
            (MeasureTheory.volume (Metric.ball 0 1)).toReal ^ (↑(Fintype.card ι))⁻¹) *
        (MeasureTheory.eLpNorm (fun y => (f y)⁻ / (a y).det ^ (↑(Fintype.card ι))⁻¹)
            (↑(Fintype.card ι))
            (MeasureTheory.volume.restrict (TauCeti.PDE.upperContactSet ū ↑Ω))).toReal
```

**The Aleksandrov–Bakelman–Pucci estimate for strong subsolutions, measure form.** Formalized in Tau Ceti as [`TauCeti.PDE.volume_ball_le_setLIntegral_upperContactSet_of_wkp`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/AleksandrovBakelmanPucci/Sobolev.html#TauCeti.PDE.volume_ball_le_setLIntegral_upperContactSet_of_wkp).

```lean
TauCeti.PDE.volume_ball_le_setLIntegral_upperContactSet_of_wkp.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] {Ω : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {ū f : EuclideanSpace ℝ ι → ℝ}
  {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {m : ℝ} {x : EuclideanSpace ℝ ι} {p : ENNReal}
  [Fact (1 ≤ p)] (hΩb : Bornology.IsBounded ↑Ω) (hp : p = ↑(Fintype.card ι))
  (u : TauCeti.Wkp MeasureTheory.volume Ω p 2) (hcont : ContinuousOn ū (closure ↑Ω))
  (hū : ↑↑(TauCeti.Wkp.value 2 u) =ᵐ[MeasureTheory.volume.restrict ↑Ω] ū)
  (ha :
    ∀ᵐ (y : EuclideanSpace ℝ ι) ∂MeasureTheory.volume.restrict (TauCeti.PDE.upperContactSet ū ↑Ω),
      (a y).PosDef)
  (hf :
    ∀ᵐ (y : EuclideanSpace ℝ ι) ∂MeasureTheory.volume.restrict (TauCeti.PDE.upperContactSet ū ↑Ω),
      f y ≤
        ∑ i,
          ∑ j,
            a y i j * ((↑↑(TauCeti.Wkp.iteratedGradient 1 u) y) (EuclideanSpace.single j 1)).ofLp i)
  (hm : ∀ z ∈ frontier ↑Ω, ū z ≤ m) (hx : x ∈ Ω) :
  MeasureTheory.volume (Metric.ball 0 ((ū x - m) / Metric.diam ↑Ω)) ≤
    ∫⁻ (y : EuclideanSpace ℝ ι) in TauCeti.PDE.upperContactSet ū ↑Ω,
      ENNReal.ofReal (((f y)⁻ / ↑(Fintype.card ι)) ^ Fintype.card ι / (a y).det)
```

**The Aleksandrov–Bakelman–Pucci estimate, measure form (Gilbarg–Trudinger, Lemma 9.3 without drift).** Formalized in Tau Ceti as [`TauCeti.PDE.volume_ball_le_setLIntegral_upperContactSet`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/AleksandrovBakelmanPucci/Basic.html#TauCeti.PDE.volume_ball_le_setLIntegral_upperContactSet).

```lean
TauCeti.PDE.volume_ball_le_setLIntegral_upperContactSet.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] {Ω : Set (EuclideanSpace ℝ ι)} {u f : EuclideanSpace ℝ ι → ℝ}
  {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {m : ℝ} {x : EuclideanSpace ℝ ι}
  (hΩb : Bornology.IsBounded Ω) (hΩ : IsOpen Ω) (hcont : ContinuousOn u (closure Ω))
  (hu : ContDiffOn ℝ 2 u Ω) (ha : ∀ y ∈ TauCeti.PDE.upperContactSet u Ω, (a y).PosDef)
  (hf :
    ∀ y ∈ TauCeti.PDE.upperContactSet u Ω,
      f y ≤
        ∑ i,
          ∑ j,
            a y i j *
              ((fderiv ℝ (fderiv ℝ u) y) (EuclideanSpace.single i 1)) (EuclideanSpace.single j 1))
  (hm : ∀ z ∈ frontier Ω, u z ≤ m) (hx : x ∈ Ω) :
  MeasureTheory.volume (Metric.ball 0 ((u x - m) / Metric.diam Ω)) ≤
    ∫⁻ (y : EuclideanSpace ℝ ι) in TauCeti.PDE.upperContactSet u Ω,
      ENNReal.ofReal (((f y)⁻ / ↑(Fintype.card ι)) ^ Fintype.card ι / (a y).det)
```

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/AleksandrovBakelmanPucci/Basic.html#TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow)
- [Source of `TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow` in TauCeti/Analysis/PDE/MaximumPrinciple/AleksandrovBakelmanPucci/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/MaximumPrinciple/AleksandrovBakelmanPucci/Basic.lean#L300)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PDE/STATUS.md)
