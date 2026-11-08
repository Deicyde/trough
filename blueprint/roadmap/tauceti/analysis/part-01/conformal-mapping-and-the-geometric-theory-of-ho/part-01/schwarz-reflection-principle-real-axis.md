---
declaration: theorem
origin: cited
lean: TauCeti.differentiableOn_schwarzReflection_of_symmetric, TauCeti.WeaklyHarmonicOn.exists_harmonicOnNhd_ae_eq_of_inf_normalHalfSpace, TauCeti.exists_differentiableOn_eqOn_conj_of_symmetric, TauCeti.differentiableOn_circleSchwarzReflection_of_symmetric, TauCeti.exists_differentiableOn_eqOn_lineReflection_of_symmetric, TauCeti.differentiableOn_lineSchwarzReflection_of_symmetric, TauCeti.WeaklyHarmonicOn.sub_comp_normalReflection
statement: formalized
proof: formalized
---

# Schwarz reflection principle (real axis)

On a conjugation-symmetric open set `Ω`, if `f`
is continuous on the closed upper part, holomorphic on the open upper part, and real-valued on
the real axis of `Ω`, then the explicit reflection extension `schwarzReflection f` is holomorphic
on all of `Ω` — in particular across the real axis.

The gluing calculus (continuity everywhere, holomorphy off the axis, the conjugation symmetry) is
`Reflection/Basic.lean`; the missing holomorphy at the axis is Painlevé removability,
`differentiableOn_of_continuousOn_of_differentiableOn_im_ne_zero`.

```lean
TauCeti.differentiableOn_schwarzReflection_of_symmetric {f : ℂ → ℂ} {Ω : Set ℂ} (hΩopen : IsOpen Ω)
  (hΩ : Set.MapsTo (⇑(starRingEnd ℂ)) Ω Ω) (hcont : ContinuousOn f (Ω ∩ {z | 0 ≤ z.im}))
  (hholo : DifferentiableOn ℂ f (Ω ∩ {z | 0 < z.im})) (hreal : ∀ z ∈ Ω, z.im = 0 → (f z).im = 0) :
  DifferentiableOn ℂ (TauCeti.schwarzReflection f) Ω
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Rademacher's theorem for locally Lipschitz functions](../../calculus/part-01/rademachers-theorem-for-locally-lipschitz-functi.md)
- [Weyl's lemma for `\bar∂`](../../../part-02/complex/part-02/weyls-lemma-for-bar.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.differentiableOn_schwarzReflection_of_symmetric`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Reflection/Principle.html#TauCeti.differentiableOn_schwarzReflection_of_symmetric).

## Other forms

**The Schwarz reflection principle.** Formalized in Tau Ceti as [`TauCeti.WeaklyHarmonicOn.exists_harmonicOnNhd_ae_eq_of_inf_normalHalfSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Harmonic/Reflection.html#TauCeti.WeaklyHarmonicOn.exists_harmonicOnNhd_ae_eq_of_inf_normalHalfSpace).

```lean
TauCeti.WeaklyHarmonicOn.exists_harmonicOnNhd_ae_eq_of_inf_normalHalfSpace.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {a : ℝ} {U : TopologicalSpace.Opens (WithLp 2 (ℝ × E))} {w : WithLp 2 (ℝ × E) → ℝ}
  {G : WithLp 2 (ℝ × E) → WithLp 2 (ℝ × E)}
  (hharm : TauCeti.WeaklyHarmonicOn MeasureTheory.volume (U ⊓ TauCeti.normalHalfSpace a) w)
  (hU : Set.MapsTo ⇑(TauCeti.normalReflection E a) ↑U ↑U)
  (hw : TauCeti.HasWeakFDerivOn MeasureTheory.volume U w fun x => (innerSL ℝ) (G x))
  (hG0 :
    ∀ᵐ (x : WithLp 2 (ℝ × E)) ∂MeasureTheory.volume.restrict ↑U,
      x ∉ TauCeti.normalHalfSpace a → G x = 0)
  (hw0 :
    ∀ᵐ (x : WithLp 2 (ℝ × E)) ∂MeasureTheory.volume.restrict ↑U,
      x ∉ TauCeti.normalHalfSpace a → w x = 0) :
  ∃ h,
    InnerProductSpace.HarmonicOnNhd h ↑U ∧
      (∀ x ∈ U, h ((TauCeti.normalReflection E a) x) = -h x) ∧
        w =ᵐ[MeasureTheory.volume.restrict ↑(U ⊓ TauCeti.normalHalfSpace a)] h ∧
          (fun x => gradient h x) =ᵐ[MeasureTheory.volume.restrict ↑(U ⊓ TauCeti.normalHalfSpace a)]
            G
```

**Schwarz reflection principle, packaged existential form.** Formalized in Tau Ceti as [`TauCeti.exists_differentiableOn_eqOn_conj_of_symmetric`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Reflection/Principle.html#TauCeti.exists_differentiableOn_eqOn_conj_of_symmetric).

```lean
TauCeti.exists_differentiableOn_eqOn_conj_of_symmetric {f : ℂ → ℂ} {Ω : Set ℂ} (hΩopen : IsOpen Ω)
  (hΩ : Set.MapsTo (⇑(starRingEnd ℂ)) Ω Ω) (hcont : ContinuousOn f (Ω ∩ {z | 0 ≤ z.im}))
  (hholo : DifferentiableOn ℂ f (Ω ∩ {z | 0 < z.im})) (hreal : ∀ z ∈ Ω, z.im = 0 → (f z).im = 0) :
  ∃ F,
    DifferentiableOn ℂ F Ω ∧
      Set.EqOn F f (Ω ∩ {z | 0 ≤ z.im}) ∧ ∀ z ∈ Ω, F ((starRingEnd ℂ) z) = (starRingEnd ℂ) (F z)
```

**Schwarz reflection principle across a circle.** Formalized in Tau Ceti as [`TauCeti.differentiableOn_circleSchwarzReflection_of_symmetric`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Reflection/Circle/Principle.html#TauCeti.differentiableOn_circleSchwarzReflection_of_symmetric).

```lean
TauCeti.differentiableOn_circleSchwarzReflection_of_symmetric {Ω : Set ℂ} {c d : ℂ} {r s : ℝ}
  {f : ℂ → ℂ} (hr : 0 < r) (hs : 0 < s) (hΩ : IsOpen Ω)
  (hsymm : Set.MapsTo (EuclideanGeometry.inversion c r) Ω Ω)
  (hcont : ContinuousOn f (Ω ∩ Metric.closedBall c r))
  (hholo : DifferentiableOn ℂ f (Ω ∩ Metric.ball c r))
  (hboundary : Set.MapsTo f (Ω ∩ Metric.sphere c r) (Metric.sphere d s))
  (havoid : ∀ z ∈ Ω ∩ Metric.ball c r, z ≠ c → f z ≠ d) :
  DifferentiableOn ℂ (TauCeti.circleSchwarzReflection c r d s f) Ω
```

**Schwarz reflection principle across affine source and target lines, packaged form.** Formalized in Tau Ceti as [`TauCeti.exists_differentiableOn_eqOn_lineReflection_of_symmetric`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Reflection/Line.html#TauCeti.exists_differentiableOn_eqOn_lineReflection_of_symmetric).

```lean
TauCeti.exists_differentiableOn_eqOn_lineReflection_of_symmetric {Ω : Set ℂ} {p a q b : ℂ}
  {f : ℂ → ℂ} (ha : a ≠ 0) (hb : b ≠ 0) (hΩopen : IsOpen Ω)
  (hΩ : Set.MapsTo (fun z => p + a * (starRingEnd ℂ) ((z - p) / a)) Ω Ω)
  (hcont : ContinuousOn f (Ω ∩ {z | 0 ≤ ((z - p) / a).im}))
  (hholo : DifferentiableOn ℂ f (Ω ∩ {z | 0 < ((z - p) / a).im}))
  (hline : ∀ z ∈ Ω, ((z - p) / a).im = 0 → ((f z - q) / b).im = 0) :
  ∃ F,
    DifferentiableOn ℂ F Ω ∧
      Set.EqOn F f (Ω ∩ {z | 0 ≤ ((z - p) / a).im}) ∧
        ∀ z ∈ Ω, F (p + a * (starRingEnd ℂ) ((z - p) / a)) = q + b * (starRingEnd ℂ) ((F z - q) / b)
```

**Schwarz reflection principle across an affine line, holomorphy form.** Formalized in Tau Ceti as [`TauCeti.differentiableOn_lineSchwarzReflection_of_symmetric`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Reflection/Line.html#TauCeti.differentiableOn_lineSchwarzReflection_of_symmetric).

```lean
TauCeti.differentiableOn_lineSchwarzReflection_of_symmetric {Ω : Set ℂ} {p a q b : ℂ} {f : ℂ → ℂ}
  (ha : a ≠ 0) (hΩopen : IsOpen Ω)
  (hΩ : Set.MapsTo (fun z => p + a * (starRingEnd ℂ) ((z - p) / a)) Ω Ω)
  (hcont : ContinuousOn f (Ω ∩ {z | 0 ≤ ((z - p) / a).im}))
  (hholo : DifferentiableOn ℂ f (Ω ∩ {z | 0 < ((z - p) / a).im}))
  (hline : ∀ z ∈ Ω, ((z - p) / a).im = 0 → ((f z - q) / b).im = 0) :
  DifferentiableOn ℂ (TauCeti.lineSchwarzReflection p a q b f) Ω
```

**The Schwarz reflection principle, weak form.** Formalized in Tau Ceti as [`TauCeti.WeaklyHarmonicOn.sub_comp_normalReflection`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Harmonic/Reflection.html#TauCeti.WeaklyHarmonicOn.sub_comp_normalReflection).

```lean
TauCeti.WeaklyHarmonicOn.sub_comp_normalReflection.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] {a : ℝ}
  {U : TopologicalSpace.Opens (WithLp 2 (ℝ × E))} {w : WithLp 2 (ℝ × E) → ℝ}
  {G : WithLp 2 (ℝ × E) → WithLp 2 (ℝ × E)}
  (hharm : TauCeti.WeaklyHarmonicOn MeasureTheory.volume (U ⊓ TauCeti.normalHalfSpace a) w)
  (hU : Set.MapsTo ⇑(TauCeti.normalReflection E a) ↑U ↑U)
  (hw : TauCeti.HasWeakFDerivOn MeasureTheory.volume U w fun x => (innerSL ℝ) (G x))
  (hG0 :
    ∀ᵐ (x : WithLp 2 (ℝ × E)) ∂MeasureTheory.volume.restrict ↑U,
      x ∉ TauCeti.normalHalfSpace a → G x = 0) :
  TauCeti.WeaklyHarmonicOn MeasureTheory.volume U fun x =>
    w x - w ((TauCeti.normalReflection E a) x)
```

## Sources

- [Tau Ceti documentation: `TauCeti.differentiableOn_schwarzReflection_of_symmetric`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Reflection/Principle.html#TauCeti.differentiableOn_schwarzReflection_of_symmetric)
- [Source of `TauCeti.differentiableOn_schwarzReflection_of_symmetric` in TauCeti/Analysis/Complex/Conformal/Reflection/Principle.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/Reflection/Principle.lean#L54)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ConformalMapping/STATUS.md)
