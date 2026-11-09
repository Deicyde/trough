---
declaration: theorem
origin: cited
lean: TauCeti.exists_norm_eq_one_forall_eq_of_pseudoHyperbolicExpr_map_eq
statement: formalized
proof: formalized
---

# Rigidity in the Schwarz--Pick theorem

If a holomorphic self-map `f` of the open unit disc
preserves the pseudo-hyperbolic expression at one pair of distinct points `z ≠ w`, then on the
whole disc `f` is the Moebius conjugate of a rotation: there is a unimodular `C` with

`(f ζ - f w) / (1 - conj (f w) * f ζ) = C * ((ζ - w) / (1 - conj w * ζ))`.

```lean
TauCeti.exists_norm_eq_one_forall_eq_of_pseudoHyperbolicExpr_map_eq {f : ℂ → ℂ} {z w : ℂ}
  (hf : DifferentiableOn ℂ f (Metric.ball 0 1))
  (hmaps : Set.MapsTo f (Metric.ball 0 1) (Metric.ball 0 1)) (hz : z ∈ Metric.ball 0 1)
  (hw : w ∈ Metric.ball 0 1) (hne : z ≠ w)
  (heq : TauCeti.pseudoHyperbolicExpr (f z) (f w) = TauCeti.pseudoHyperbolicExpr z w) :
  ∃ C,
    ‖C‖ = 1 ∧
      ∀ ζ ∈ Metric.ball 0 1,
        (f ζ - f w) / (1 - (starRingEnd ℂ) (f w) * f ζ) =
          C * ((ζ - w) / (1 - (starRingEnd ℂ) w * ζ))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_norm_eq_one_forall_eq_of_pseudoHyperbolicExpr_map_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzPick/Rigidity.html#TauCeti.exists_norm_eq_one_forall_eq_of_pseudoHyperbolicExpr_map_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_norm_eq_one_forall_eq_of_pseudoHyperbolicExpr_map_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzPick/Rigidity.html#TauCeti.exists_norm_eq_one_forall_eq_of_pseudoHyperbolicExpr_map_eq)
- [Source of `TauCeti.exists_norm_eq_one_forall_eq_of_pseudoHyperbolicExpr_map_eq` in TauCeti/Analysis/Complex/Conformal/SchwarzPick/Rigidity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/SchwarzPick/Rigidity.lean#L91)
