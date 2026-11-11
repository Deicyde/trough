---
declaration: theorem
origin: cited
lean: TauCeti.W1p.sub_mul_measureReal_mul_measureReal_le_of_convex, TauCeti.W1p.sub_mul_measureReal_mul_measureReal_le_of_eq_ball, TauCeti.W1p.sub_mul_measureReal_mul_measureReal_le_of_ball_subset, TauCeti.W1p.sq_sub_mul_measureReal_mul_measureReal_le_of_ball_subset
statement: formalized
proof: formalized
---

# De Giorgi's isoperimetric inequality

Let `Ω` be a bounded convex open set in a
finite-dimensional real inner product space of dimension `n`, let `u ∈ W^{1,p}(Ω)` with
`1 ≤ p ≤ ∞`, and let `k < l`.  Then, all sets being taken inside `Ω`,

`(l - k) · |{u ≥ l}| · |{u ≤ k}| ≤ μ(B(0, 1)) · (diam Ω) ^ (n + 1) · ∫_{k < u < l} |∇u|`.

A function that is both `≤ k` and `≥ l` on sets of positive measure must have a weak gradient
of definite `L¹` mass on the strip `{k < u < l}`.

```lean
TauCeti.W1p.sub_mul_measureReal_mul_measureReal_le_of_convex.{u_1} {E : Type u_1}
  [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [BorelSpace E] {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens E} {p : ENNReal} [Fact (1 ≤ p)] (hconv : Convex ℝ ↑Omega)
  (hb : Bornology.IsBounded ↑Omega) (u : ↥(TauCeti.W1p mu Omega p)) {k l : ℝ} (hkl : k < l) :
  (l - k) * (mu.restrict ↑Omega).real {x | l ≤ ↑↑(TauCeti.W1p.value u) x} *
      (mu.restrict ↑Omega).real {x | ↑↑(TauCeti.W1p.value u) x ≤ k} ≤
    mu.real (Metric.ball 0 1) * Metric.diam ↑Omega ^ (Module.finrank ℝ E + 1) *
      ∫ (x : E) in {x | k < ↑↑(TauCeti.W1p.value u) x ∧ ↑↑(TauCeti.W1p.value u) x < l},
        ‖↑↑(TauCeti.W1p.gradient u) x‖ ∂mu.restrict ↑Omega
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Poincaré–Wirtinger inequality on a ball](../part-02/the-poincare-wirtinger-inequality-on-a-ball.md)
- [TauCeti.Wkp](../../../part-01/partial-differential-equations/tauceti-wkp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.W1p.sub_mul_measureReal_mul_measureReal_le_of_convex`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/DeGiorgi.html#TauCeti.W1p.sub_mul_measureReal_mul_measureReal_le_of_convex).

## Other forms

**De Giorgi's isoperimetric inequality on a ball.** Formalized in Tau Ceti as [`TauCeti.W1p.sub_mul_measureReal_mul_measureReal_le_of_eq_ball`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/DeGiorgi.html#TauCeti.W1p.sub_mul_measureReal_mul_measureReal_le_of_eq_ball).

```lean
TauCeti.W1p.sub_mul_measureReal_mul_measureReal_le_of_eq_ball.{u_1} {E : Type u_1}
  [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [BorelSpace E] {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens E} {p : ENNReal} [Fact (1 ≤ p)] {c : E} {R : ℝ} (hR : 0 ≤ R)
  (hOmega : ↑Omega = Metric.ball c R) (u : ↥(TauCeti.W1p mu Omega p)) {k l : ℝ} (hkl : k < l) :
  (l - k) * (mu.restrict ↑Omega).real {x | l ≤ ↑↑(TauCeti.W1p.value u) x} *
      (mu.restrict ↑Omega).real {x | ↑↑(TauCeti.W1p.value u) x ≤ k} ≤
    mu.real (Metric.ball 0 1) * (2 * R) ^ (Module.finrank ℝ E + 1) *
      ∫ (x : E) in {x | k < ↑↑(TauCeti.W1p.value u) x ∧ ↑↑(TauCeti.W1p.value u) x < l},
        ‖↑↑(TauCeti.W1p.gradient u) x‖ ∂mu.restrict ↑Omega
```

**De Giorgi's isoperimetric inequality on a ball contained in the Sobolev domain.** Formalized in Tau Ceti as [`TauCeti.W1p.sub_mul_measureReal_mul_measureReal_le_of_ball_subset`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/DeGiorgi.html#TauCeti.W1p.sub_mul_measureReal_mul_measureReal_le_of_ball_subset).

```lean
TauCeti.W1p.sub_mul_measureReal_mul_measureReal_le_of_ball_subset.{u_1} {E : Type u_1}
  [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [BorelSpace E] {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens E} {p : ENNReal} [Fact (1 ≤ p)] {c : E} {R : ℝ} (hR : 0 ≤ R)
  (hball : Metric.ball c R ⊆ ↑Omega) (u : ↥(TauCeti.W1p mu Omega p)) {k l : ℝ} (hkl : k < l) :
  (l - k) * (mu.restrict (Metric.ball c R)).real {x | l ≤ ↑↑(TauCeti.W1p.value u) x} *
      (mu.restrict (Metric.ball c R)).real {x | ↑↑(TauCeti.W1p.value u) x ≤ k} ≤
    mu.real (Metric.ball 0 1) * (2 * R) ^ (Module.finrank ℝ E + 1) *
      ∫ (x : E) in {x | k < ↑↑(TauCeti.W1p.value u) x ∧ ↑↑(TauCeti.W1p.value u) x < l},
        ‖↑↑(TauCeti.W1p.gradient u) x‖ ∂mu.restrict (Metric.ball c R)
```

**De Giorgi's isoperimetric inequality, squared form.** Formalized in Tau Ceti as [`TauCeti.W1p.sq_sub_mul_measureReal_mul_measureReal_le_of_ball_subset`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/DeGiorgi.html#TauCeti.W1p.sq_sub_mul_measureReal_mul_measureReal_le_of_ball_subset).

```lean
TauCeti.W1p.sq_sub_mul_measureReal_mul_measureReal_le_of_ball_subset.{u_1} {E : Type u_1}
  [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [BorelSpace E] {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens E} {c : E} {R : ℝ} (hR : 0 ≤ R) (hball : Metric.ball c R ⊆ ↑Omega)
  (u : ↥(TauCeti.W1p mu Omega 2)) {k l : ℝ} (hkl : k < l)
  (hwLp :
    MeasureTheory.MemLp (fun x => max (↑↑(TauCeti.W1p.value u) x - k) 0) 2 (mu.restrict ↑Omega)) :
  ((l - k) * (mu.restrict (Metric.ball c R)).real {x | l ≤ ↑↑(TauCeti.W1p.value u) x} *
        (mu.restrict (Metric.ball c R)).real {x | ↑↑(TauCeti.W1p.value u) x ≤ k}) ^
      2 ≤
    (mu.real (Metric.ball 0 1) * (2 * R) ^ (Module.finrank ℝ E + 1)) ^ 2 *
        (mu.restrict (Metric.ball c R)).real
          {x | k < ↑↑(TauCeti.W1p.value u) x ∧ ↑↑(TauCeti.W1p.value u) x < l} *
      ∫ (x : E) in Metric.ball c R,
        ‖↑↑(TauCeti.W1p.gradient
                    (TauCeti.W1p.posPartAboveOfMemLp
                      TauCeti.W1p.sq_sub_mul_measureReal_mul_measureReal_le_of_ball_subset._proof_1
                      k u hwLp))
              x‖ ^
          2 ∂mu
```

## Sources

- [Tau Ceti documentation: `TauCeti.W1p.sub_mul_measureReal_mul_measureReal_le_of_convex`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/DeGiorgi.html#TauCeti.W1p.sub_mul_measureReal_mul_measureReal_le_of_convex)
- [Source of `TauCeti.W1p.sub_mul_measureReal_mul_measureReal_le_of_convex` in TauCeti/Analysis/Sobolev/Poincare/Wirtinger/DeGiorgi.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/DeGiorgi.lean#L148)
