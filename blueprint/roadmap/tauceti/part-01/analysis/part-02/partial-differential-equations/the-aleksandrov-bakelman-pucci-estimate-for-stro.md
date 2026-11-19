---
declaration: theorem
origin: cited
lean: TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow_of_wkp, TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow, TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow_of_wkpLoc, TauCeti.PDE.volume_ball_le_setLIntegral_upperContactSet_of_wkpLoc, TauCeti.PDE.volume_ball_le_setLIntegral_upperContactSet_of_wkp, TauCeti.PDE.volume_ball_le_setLIntegral_upperContactSet
statement: formalized
proof: formalized
---

# The Aleksandrov–Bakelman–Pucci estimate for strong subsolutions

**The Aleksandrov–Bakelman–Pucci estimate for strong subsolutions** (Gilbarg–Trudinger,
Lemma 9.3 and Theorem 9.1 without drift, for `W^{2,n}` functions). Let `Ω ⊆ ℝⁿ`, `n ≥ 1`, be
bounded and open, let `u ∈ W^{2,n}(Ω)` have a representative `ū` continuous on `closure Ω`, and let
`m` bound `ū` on `frontier Ω`. Suppose that almost everywhere on the upper contact set `Γ⁺` of `ū`
the matrices `a y` are positive definite and `f y ≤ ∑ᵢⱼ aⁱʲ(y) ∂ᵢ∂ⱼu(y)` with the weak Hessian,
and that `f⁻ / D*`, with `D* = (det a)^{1/n}`, lies in `Lⁿ(Γ⁺)`. Then on `Ω`,
`ū ≤ m + diam Ω / (n ωₙ^{1/n}) ‖f⁻ / D*‖_{Lⁿ(Γ⁺)}`, where `ωₙ` is the volume of the unit ball.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Aleksandrov measure estimate for bounded slopes](../../part-04/pde/part-01/the-aleksandrov-measure-estimate-for-bounded-slo.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow_of_wkp`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/AleksandrovBakelmanPucci/Sobolev.html#TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow_of_wkp).

## Other forms

**The Aleksandrov–Bakelman–Pucci estimate.** Formalized in Tau Ceti as [`TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/AleksandrovBakelmanPucci/Basic.html#TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow).

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

**The Aleksandrov–Bakelman–Pucci estimate for local strong subsolutions.** Formalized in Tau Ceti as [`TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow_of_wkpLoc`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/AleksandrovBakelmanPucci/Sobolev.html#TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow_of_wkpLoc).

```lean
TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow_of_wkpLoc.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] {Ω : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {ū f : EuclideanSpace ℝ ι → ℝ}
  {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {m : ℝ} {x : EuclideanSpace ℝ ι} {p : ENNReal}
  [Fact (1 ≤ p)] (hΩb : Bornology.IsBounded ↑Ω) (hp : p = ↑(Fintype.card ι))
  (hcont : ContinuousOn ū (closure ↑Ω))
  (hloc :
    ∀ K ⊆ ↑Ω,
      IsCompact K →
        ∃ V v,
          K ⊆ ↑V ∧
            ↑↑(TauCeti.Wkp.value 2 v) =ᵐ[MeasureTheory.volume.restrict ↑V] ū ∧
              ∀ᵐ (y :
                EuclideanSpace ℝ
                  ι) ∂MeasureTheory.volume.restrict (TauCeti.PDE.upperContactSet ū ↑Ω ∩ ↑V),
                f y ≤
                  ∑ i,
                    ∑ j,
                      a y i j *
                        ((↑↑(TauCeti.Wkp.iteratedGradient 1 v) y) (EuclideanSpace.single j 1)).ofLp
                          i)
  (ha :
    ∀ᵐ (y : EuclideanSpace ℝ ι) ∂MeasureTheory.volume.restrict (TauCeti.PDE.upperContactSet ū ↑Ω),
      (a y).PosDef)
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

**The Aleksandrov–Bakelman–Pucci estimate for local strong subsolutions, measure form.** Formalized in Tau Ceti as [`TauCeti.PDE.volume_ball_le_setLIntegral_upperContactSet_of_wkpLoc`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/AleksandrovBakelmanPucci/Sobolev.html#TauCeti.PDE.volume_ball_le_setLIntegral_upperContactSet_of_wkpLoc).

```lean
TauCeti.PDE.volume_ball_le_setLIntegral_upperContactSet_of_wkpLoc.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] {Ω : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {ū f : EuclideanSpace ℝ ι → ℝ}
  {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {m : ℝ} {x : EuclideanSpace ℝ ι} {p : ENNReal}
  [Fact (1 ≤ p)] (hΩb : Bornology.IsBounded ↑Ω) (hp : p = ↑(Fintype.card ι))
  (hcont : ContinuousOn ū (closure ↑Ω))
  (hloc :
    ∀ K ⊆ ↑Ω,
      IsCompact K →
        ∃ V v,
          K ⊆ ↑V ∧
            ↑↑(TauCeti.Wkp.value 2 v) =ᵐ[MeasureTheory.volume.restrict ↑V] ū ∧
              ∀ᵐ (y :
                EuclideanSpace ℝ
                  ι) ∂MeasureTheory.volume.restrict (TauCeti.PDE.upperContactSet ū ↑Ω ∩ ↑V),
                f y ≤
                  ∑ i,
                    ∑ j,
                      a y i j *
                        ((↑↑(TauCeti.Wkp.iteratedGradient 1 v) y) (EuclideanSpace.single j 1)).ofLp
                          i)
  (ha :
    ∀ᵐ (y : EuclideanSpace ℝ ι) ∂MeasureTheory.volume.restrict (TauCeti.PDE.upperContactSet ū ↑Ω),
      (a y).PosDef)
  (hm : ∀ z ∈ frontier ↑Ω, ū z ≤ m) (hx : x ∈ Ω) :
  MeasureTheory.volume (Metric.ball 0 ((ū x - m) / Metric.diam ↑Ω)) ≤
    ∫⁻ (y : EuclideanSpace ℝ ι) in TauCeti.PDE.upperContactSet ū ↑Ω,
      ENNReal.ofReal (((f y)⁻ / ↑(Fintype.card ι)) ^ Fintype.card ι / (a y).det)
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

- [Tau Ceti documentation: `TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow_of_wkp`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/AleksandrovBakelmanPucci/Sobolev.html#TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow_of_wkp)
- [Source of `TauCeti.PDE.le_add_mul_eLpNorm_negPart_div_det_rpow_of_wkp` in TauCeti/Analysis/PDE/MaximumPrinciple/AleksandrovBakelmanPucci/Sobolev.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/MaximumPrinciple/AleksandrovBakelmanPucci/Sobolev.lean#L586)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PDE/STATUS.md)
