---
declaration: theorem
origin: cited
lean: TauCeti.mongeAmpereMeasure_withDensity_eq_singularPart_add_withDensity
statement: formalized
proof: formalized
---

# Lebesgue decomposition of the weighted Monge–Ampère measure

Let `f : E → EReal` be convex
(convex real epigraph, never `⊥`) with `D` the interior of its effective domain and real
representative `F`, and let `H x` be, for almost every `x ∈ D`, a first-order expansion of the
subdifferential of `f` at `x` (the Alexandrov Hessian, see
`rnDeriv_mongeAmpereMeasure_withDensity_ae_eq`). Then for every additive Haar measure `μ` and
measurable `g`, the Monge–Ampère measure weighted by `g μ` splits as
`MA_{f, g μ} = (MA_{f, g μ})ˢ + det (H x) g (∇F x) dx` on `D`, where `(MA_{f, g μ})ˢ` is the part
singular with respect to `μ`.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Fenchel–Young inequality, in the form that holds with no hypothesis](the-fenchel-young-inequality-in-the-form-that-ho.md)
- [Rademacher's theorem for locally Lipschitz functions](../../part-01/calculus/part-01/rademachers-theorem-for-locally-lipschitz-functi.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mongeAmpereMeasure_withDensity_eq_singularPart_add_withDensity`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/MongeAmpere/Decomposition.html#TauCeti.mongeAmpereMeasure_withDensity_eq_singularPart_add_withDensity).

## Sources

- [Tau Ceti documentation: `TauCeti.mongeAmpereMeasure_withDensity_eq_singularPart_add_withDensity`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/MongeAmpere/Decomposition.html#TauCeti.mongeAmpereMeasure_withDensity_eq_singularPart_add_withDensity)
- [Source of `TauCeti.mongeAmpereMeasure_withDensity_eq_singularPart_add_withDensity` in TauCeti/Analysis/Convex/MongeAmpere/Decomposition.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Convex/MongeAmpere/Decomposition.lean#L466)
