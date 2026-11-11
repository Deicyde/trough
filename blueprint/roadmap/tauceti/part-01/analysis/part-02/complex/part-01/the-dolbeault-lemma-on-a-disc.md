---
declaration: theorem
origin: cited
lean: TauCeti.exists_contDiffOn_conjWirtingerDeriv_apply_one_eq_of_eball, TauCeti.exists_contDiffOn_conjWirtingerDeriv_apply_one_eq_of_ball, TauCeti.exists_contDiff_conjWirtingerDeriv_apply_one_eq
statement: formalized
proof: formalized
---

# The Dolbeault lemma on a disc

Let `f` be `Cⁿ`, `n ≥ 1`, on the open disc `eball c R`
of radius `R ≤ ∞`. Then there is a function `g`, `Cⁿ` on the disc, with `\bar∂ g = f` on the
disc.

```lean
TauCeti.exists_contDiffOn_conjWirtingerDeriv_apply_one_eq_of_eball.{u_1} {W : Type u_1}
  [NormedAddCommGroup W] [NormedSpace ℂ W] [CompleteSpace W] {n : ℕ∞} {f : ℂ → W} {c : ℂ}
  {R : ENNReal} (hn : 1 ≤ n) (hf : ContDiffOn ℝ (↑n) f (Metric.eball c R)) :
  ∃ g,
    ContDiffOn ℝ (↑n) g (Metric.eball c R) ∧
      ∀ z ∈ Metric.eball c R, (TauCeti.conjWirtingerDeriv g z) 1 = f z
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cauchy–Pompeiu formula for a compactly supported `C¹` map `u : ℂ → F`](../../../part-01/elliptic-analysis-of-pseudoholomorphic-curves/the-cauchy-pompeiu-formula-for-a-compactly-suppo.md)
- [TauCeti.cauchyTransform](../../../part-01/elliptic-analysis-of-pseudoholomorphic-curves/tauceti-cauchytransform.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_contDiffOn_conjWirtingerDeriv_apply_one_eq_of_eball`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/DolbeaultLemma.html#TauCeti.exists_contDiffOn_conjWirtingerDeriv_apply_one_eq_of_eball).

## Other forms

**The Dolbeault lemma on a disc of real radius.** Formalized in Tau Ceti as [`TauCeti.exists_contDiffOn_conjWirtingerDeriv_apply_one_eq_of_ball`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/DolbeaultLemma.html#TauCeti.exists_contDiffOn_conjWirtingerDeriv_apply_one_eq_of_ball).

```lean
TauCeti.exists_contDiffOn_conjWirtingerDeriv_apply_one_eq_of_ball.{u_1} {W : Type u_1}
  [NormedAddCommGroup W] [NormedSpace ℂ W] [CompleteSpace W] {n : ℕ∞} {f : ℂ → W} {c : ℂ} {R : ℝ}
  (hn : 1 ≤ n) (hf : ContDiffOn ℝ (↑n) f (Metric.ball c R)) :
  ∃ g,
    ContDiffOn ℝ (↑n) g (Metric.ball c R) ∧
      ∀ z ∈ Metric.ball c R, (TauCeti.conjWirtingerDeriv g z) 1 = f z
```

**The Dolbeault lemma on the plane.** Formalized in Tau Ceti as [`TauCeti.exists_contDiff_conjWirtingerDeriv_apply_one_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/DolbeaultLemma.html#TauCeti.exists_contDiff_conjWirtingerDeriv_apply_one_eq).

```lean
TauCeti.exists_contDiff_conjWirtingerDeriv_apply_one_eq.{u_1} {W : Type u_1} [NormedAddCommGroup W]
  [NormedSpace ℂ W] [CompleteSpace W] {n : ℕ∞} {f : ℂ → W} (hn : 1 ≤ n) (hf : ContDiff ℝ (↑n) f) :
  ∃ g, ContDiff ℝ (↑n) g ∧ ∀ (z : ℂ), (TauCeti.conjWirtingerDeriv g z) 1 = f z
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_contDiffOn_conjWirtingerDeriv_apply_one_eq_of_eball`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/DolbeaultLemma.html#TauCeti.exists_contDiffOn_conjWirtingerDeriv_apply_one_eq_of_eball)
- [Source of `TauCeti.exists_contDiffOn_conjWirtingerDeriv_apply_one_eq_of_eball` in TauCeti/Analysis/Complex/Wirtinger/DolbeaultLemma.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Wirtinger/DolbeaultLemma.lean#L117)
