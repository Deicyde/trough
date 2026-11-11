---
declaration: theorem
origin: cited
lean: TauCeti.mongeAmpereMeasure_eq_singularPart_add_withDensity, TauCeti.exists_mongeAmpereMeasure_eq_singularPart_add_withDensity, TauCeti.mongeAmpereMeasure_withDensity_eq_singularPart_add_withDensity
statement: formalized
proof: formalized
---

# Lebesgue decomposition of the Monge–Ampère measure

Let `f : E → EReal` be convex
(convex real epigraph, never `⊥`) with `D` the interior of its effective domain, and let `H x` be,
for almost every `x ∈ D`, a first-order expansion of the subdifferential of `f` at `x` (the
Alexandrov Hessian, see `rnDeriv_mongeAmpereMeasure_ae_eq`). Then for every additive Haar measure
`μ`, the Aleksandrov Monge–Ampère measure splits as `MA_f = (MA_f)ˢ + det (H x) dx` on `D`, where
`(MA_f)ˢ` is the part singular with respect to `μ`. So the Alexandrov Hessian determines exactly
the absolutely continuous part of `MA_f`. This is the case `g = 1` of
`mongeAmpereMeasure_withDensity_eq_singularPart_add_withDensity`.

```lean
TauCeti.mongeAmpereMeasure_eq_singularPart_add_withDensity.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {f : E → EReal}
  [MeasurableSpace E] [BorelSpace E] (μ : MeasureTheory.Measure E) [μ.IsAddHaarMeasure]
  (hf : Convex ℝ {p | f p.1 ≤ ↑p.2}) (hbot : ∀ (x : E), f x ≠ ⊥) {H : E → E →L[ℝ] E}
  (hH :
    ∀ᵐ (x : E) ∂μ,
      x ∈ interior {x | f x ≠ ⊤} →
        ∃ y,
          ∀ ε > 0,
            ∀ᶠ (x' : E) in nhds x,
              ∀ y' ∈ TauCeti.subdifferential (innerₗ E) f x',
                ‖y' - y - (H x) (x' - x)‖ ≤ ε * ‖x' - x‖) :
  TauCeti.mongeAmpereMeasure μ f =
    (TauCeti.mongeAmpereMeasure μ f).singularPart μ +
      (μ.restrict (interior {x | f x ≠ ⊤})).withDensity fun x => ENNReal.ofReal (H x).det
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Alexandrov's theorem](alexandrovs-theorem.md)
- [The Fenchel–Young inequality](the-fenchel-young-inequality.md)
- [Rademacher's theorem for extended-real convex functions](rademachers-theorem-for-extended-real-convex-fun.md)
- [Rademacher's theorem for locally Lipschitz functions](../calculus/part-02/rademachers-theorem-for-locally-lipschitz-functi.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mongeAmpereMeasure_eq_singularPart_add_withDensity`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/MongeAmpere/Decomposition.html#TauCeti.mongeAmpereMeasure_eq_singularPart_add_withDensity).

## Other forms

**Lebesgue decomposition of the Monge–Ampère measure, with the Alexandrov Hessian.** Formalized in Tau Ceti as [`TauCeti.exists_mongeAmpereMeasure_eq_singularPart_add_withDensity`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/MongeAmpere/Decomposition.html#TauCeti.exists_mongeAmpereMeasure_eq_singularPart_add_withDensity).

```lean
TauCeti.exists_mongeAmpereMeasure_eq_singularPart_add_withDensity.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {f : E → EReal}
  [MeasurableSpace E] [BorelSpace E] (μ : MeasureTheory.Measure E) [μ.IsAddHaarMeasure]
  (hf : Convex ℝ {p | f p.1 ≤ ↑p.2}) (hbot : ∀ (x : E), f x ≠ ⊥) :
  ∃ H,
    (∀ᵐ (x : E) ∂μ,
        f x ≠ ⊤ →
          (H x).IsPositive ∧
            ∀ ε > 0,
              ∀ᶠ (x' : E) in nhds x,
                ∀ y' ∈ TauCeti.subdifferential (innerₗ E) f x',
                  ‖y' - gradient (fun x' => (f x').toReal) x - (H x) (x' - x)‖ ≤ ε * ‖x' - x‖) ∧
      TauCeti.mongeAmpereMeasure μ f =
        (TauCeti.mongeAmpereMeasure μ f).singularPart μ +
          (μ.restrict (interior {x | f x ≠ ⊤})).withDensity fun x => ENNReal.ofReal (H x).det
```

**Lebesgue decomposition of the weighted Monge–Ampère measure.** Formalized in Tau Ceti as [`TauCeti.mongeAmpereMeasure_withDensity_eq_singularPart_add_withDensity`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/MongeAmpere/Decomposition.html#TauCeti.mongeAmpereMeasure_withDensity_eq_singularPart_add_withDensity).

```lean
TauCeti.mongeAmpereMeasure_withDensity_eq_singularPart_add_withDensity.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {f : E → EReal}
  [MeasurableSpace E] [BorelSpace E] (μ : MeasureTheory.Measure E) [μ.IsAddHaarMeasure]
  (hf : Convex ℝ {p | f p.1 ≤ ↑p.2}) (hbot : ∀ (x : E), f x ≠ ⊥) {H : E → E →L[ℝ] E}
  (hH :
    ∀ᵐ (x : E) ∂μ,
      x ∈ interior {x | f x ≠ ⊤} →
        ∃ y,
          ∀ ε > 0,
            ∀ᶠ (x' : E) in nhds x,
              ∀ y' ∈ TauCeti.subdifferential (innerₗ E) f x',
                ‖y' - y - (H x) (x' - x)‖ ≤ ε * ‖x' - x‖)
  {g : E → ENNReal} (hg : Measurable g) :
  TauCeti.mongeAmpereMeasure (μ.withDensity g) f =
    (TauCeti.mongeAmpereMeasure (μ.withDensity g) f).singularPart μ +
      (μ.restrict (interior {x | f x ≠ ⊤})).withDensity fun x =>
        ENNReal.ofReal (H x).det * g (gradient (fun x' => (f x').toReal) x)
```

## Sources

- [Tau Ceti documentation: `TauCeti.mongeAmpereMeasure_eq_singularPart_add_withDensity`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/MongeAmpere/Decomposition.html#TauCeti.mongeAmpereMeasure_eq_singularPart_add_withDensity)
- [Source of `TauCeti.mongeAmpereMeasure_eq_singularPart_add_withDensity` in TauCeti/Analysis/Convex/MongeAmpere/Decomposition.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Convex/MongeAmpere/Decomposition.lean#L469)
