---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_norm_intervalRepresentativeL_le_and_holderWith
statement: formalized
proof: formalized
---

# Global Hölder estimate on an interval

Let `x₀ < x₁`, `0 < λ` and `1 ≤ s ≤ ∞`. There is a
constant `C > 0`, depending only on `x₀`, `x₁`, `λ`, `M` and `s`, with the following property. Let
`a` be measurable with `λ ≤ a ≤ M`, let `f ∈ L¹(x₀, x₁)` and `F ∈ Lˢ(x₀, x₁)`, and let
`u ∈ W^{1,p}(x₀, x₁)` solve `-(a u')' = f + F'` in the sense of distributions. Then the continuous
representative `ū ∈ C([x₀, x₁])` of `u` satisfies

`‖ū‖_∞ ≤ C B` and `|ū y - ū z| ≤ C B |y - z| ^ (1 - 1 / s)`,

where `B = |ū x₀| + |ū x₁| + ‖f‖₁ + ‖F‖ₛ`. So the solution is `(1 - 1 / s)`-Hölder up to the
boundary, with norm controlled by its boundary values and the data; at `s = ∞` it is Lipschitz.

```lean
TauCeti.PDE.exists_norm_intervalRepresentativeL_le_and_holderWith {x₀ x₁ : ℝ} {p : ENNReal}
  [Fact (1 ≤ p)] (hx : x₀ < x₁) {lam M : ℝ} (hlam : 0 < lam) {s : ENNReal} (hs : 1 ≤ s) :
  ∃ C,
    0 < C ∧
      ∀ {a f F : ℝ → ℝ}
        {u : ↥(TauCeti.W1p MeasureTheory.volume { carrier := Set.Ioo x₀ x₁, is_open' := ⋯ } p)},
        MeasureTheory.AEStronglyMeasurable a (MeasureTheory.volume.restrict (Set.Ioo x₀ x₁)) →
          (∀ᵐ (t : ℝ) ∂MeasureTheory.volume.restrict (Set.Ioo x₀ x₁), lam ≤ a t ∧ a t ≤ M) →
            MeasureTheory.IntegrableOn f (Set.Ioo x₀ x₁) MeasureTheory.volume →
              MeasureTheory.MemLp F s (MeasureTheory.volume.restrict (Set.Ioo x₀ x₁)) →
                (∀ (φ : TestFunction { carrier := Set.Ioo x₀ x₁, is_open' := ⋯ } ℝ ⊤),
                    ∫ (t : ℝ) in Set.Ioo x₀ x₁, a t * ↑↑(TauCeti.W1p.gradient u) t * deriv (⇑φ) t =
                      (∫ (t : ℝ) in Set.Ioo x₀ x₁, f t * φ t) -
                        ∫ (t : ℝ) in Set.Ioo x₀ x₁, F t * deriv (⇑φ) t) →
                  ‖(TauCeti.W1p.intervalRepresentativeL hx) u‖ ≤
                      C *
                        ((|((TauCeti.W1p.intervalTraceL hx) u).1| +
                              |((TauCeti.W1p.intervalTraceL hx) u).2| +
                            ∫ (t : ℝ) in Set.Ioo x₀ x₁, |f t|) +
                          (MeasureTheory.eLpNorm F s
                              (MeasureTheory.volume.restrict (Set.Ioo x₀ x₁))).toReal) ∧
                    HolderWith
                      (C *
                          ((|((TauCeti.W1p.intervalTraceL hx) u).1| +
                                |((TauCeti.W1p.intervalTraceL hx) u).2| +
                              ∫ (t : ℝ) in Set.Ioo x₀ x₁, |f t|) +
                            (MeasureTheory.eLpNorm F s
                                (MeasureTheory.volume.restrict (Set.Ioo x₀ x₁))).toReal)).toNNReal
                      (1 - s.toNNReal⁻¹) ⇑((TauCeti.W1p.intervalRepresentativeL hx) u)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The fundamental theorem of calculus for a continuous representative](../../part-03/sobolev/part-01/the-fundamental-theorem-of-calculus-for-a-contin.md)
- [The fundamental theorem of calculus for weak derivatives](../../part-03/sobolev/part-01/the-fundamental-theorem-of-calculus-for-weak-der.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_norm_intervalRepresentativeL_le_and_holderWith`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Interval.html#TauCeti.PDE.exists_norm_intervalRepresentativeL_le_and_holderWith).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_norm_intervalRepresentativeL_le_and_holderWith`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Interval.html#TauCeti.PDE.exists_norm_intervalRepresentativeL_le_and_holderWith)
- [Source of `TauCeti.PDE.exists_norm_intervalRepresentativeL_le_and_holderWith` in TauCeti/Analysis/PDE/Regularity/Interval.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Regularity/Interval.lean#L394)
