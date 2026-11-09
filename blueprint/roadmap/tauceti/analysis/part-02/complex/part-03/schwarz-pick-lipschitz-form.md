---
declaration: theorem
origin: cited
lean: TauCeti.PoincareDisc.lipschitzWith_one, TauCeti.hyperbolicLength_comp_le, TauCeti.hyperbolicDist_map_le, TauCeti.PoincareDisc.dist_map_le
statement: formalized
proof: formalized
---

# Schwarz–Pick, Lipschitz form

A holomorphic self-map of the unit disc is a nonexpanding
map of the metric space `TauCeti.PoincareDisc`.

Together with
`TauCeti.PoincareDisc.isometry_iff_exists_eq_unitDiscStandardAutomorphismIsometryEquiv` this says
that a holomorphic self-map of the Poincaré disc is nonexpanding, and is an isometry precisely
when it is a disc automorphism.

```lean
TauCeti.PoincareDisc.lipschitzWith_one {F : TauCeti.PoincareDisc → TauCeti.PoincareDisc} {f : ℂ → ℂ}
  (hf : DifferentiableOn ℂ f (Metric.ball 0 1))
  (hrep :
    ∀ (z : TauCeti.PoincareDisc),
      ↑(TauCeti.PoincareDisc.toUnitDisc (F z)) = f ↑(TauCeti.PoincareDisc.toUnitDisc z)) :
  LipschitzWith 1 F
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The infinitesimal Schwarz--Pick inequality](../part-02/the-infinitesimal-schwarz-pick-inequality.md)
- [Poincaré defect identity (norm form)](../../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-02/poincare-defect-identity-norm-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PoincareDisc.lipschitzWith_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Poincare/SchwarzPick.html#TauCeti.PoincareDisc.lipschitzWith_one).

## Other forms

**Schwarz--Pick for the Poincaré length.** Formalized in Tau Ceti as [`TauCeti.hyperbolicLength_comp_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Hyperbolic/Length.html#TauCeti.hyperbolicLength_comp_le).

```lean
TauCeti.hyperbolicLength_comp_le {γ γ' : ℝ → ℂ} {a b : ℝ} {f : ℂ → ℂ}
  (hf : DifferentiableOn ℂ f (Metric.ball 0 1))
  (hmaps : Set.MapsTo f (Metric.ball 0 1) (Metric.ball 0 1)) (hγ : ContinuousOn γ (Set.uIcc a b))
  (hderiv : ∀ t ∈ Set.uIoo a b, HasDerivAt γ (γ' t) t) (hγ' : ContinuousOn γ' (Set.uIcc a b))
  (hmem : ∀ t ∈ Set.uIcc a b, ‖γ t‖ < 1) :
  TauCeti.hyperbolicLength (f ∘ γ) a b ≤ TauCeti.hyperbolicLength γ a b
```

**Schwarz--Pick, distance form.** Formalized in Tau Ceti as [`TauCeti.hyperbolicDist_map_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Hyperbolic/Distance.html#TauCeti.hyperbolicDist_map_le).

```lean
TauCeti.hyperbolicDist_map_le {f : ℂ → ℂ} (hf : DifferentiableOn ℂ f (Metric.ball 0 1))
  (hmaps : Set.MapsTo f (Metric.ball 0 1) (Metric.ball 0 1)) {z w : ℂ} (hz : z ∈ Metric.ball 0 1)
  (hw : w ∈ Metric.ball 0 1) : TauCeti.hyperbolicDist (f z) (f w) ≤ TauCeti.hyperbolicDist z w
```

**Schwarz–Pick for the Poincaré metric.** Formalized in Tau Ceti as [`TauCeti.PoincareDisc.dist_map_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Poincare/SchwarzPick.html#TauCeti.PoincareDisc.dist_map_le).

```lean
TauCeti.PoincareDisc.dist_map_le {F : TauCeti.PoincareDisc → TauCeti.PoincareDisc} {f : ℂ → ℂ}
  (hf : DifferentiableOn ℂ f (Metric.ball 0 1))
  (hrep :
    ∀ (z : TauCeti.PoincareDisc),
      ↑(TauCeti.PoincareDisc.toUnitDisc (F z)) = f ↑(TauCeti.PoincareDisc.toUnitDisc z))
  (z w : TauCeti.PoincareDisc) : dist (F z) (F w) ≤ dist z w
```

## Sources

- [Tau Ceti documentation: `TauCeti.PoincareDisc.lipschitzWith_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Poincare/SchwarzPick.html#TauCeti.PoincareDisc.lipschitzWith_one)
- [Source of `TauCeti.PoincareDisc.lipschitzWith_one` in TauCeti/Analysis/Complex/Conformal/Poincare/SchwarzPick.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/Poincare/SchwarzPick.lean#L124)
