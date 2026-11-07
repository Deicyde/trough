---
declaration: theorem
origin: cited
lean: TauCeti.exists_map_IccExtend_eq_lintegral_curveAction_eq
statement: formalized
proof: formalized
---

# TauCeti.exists\_map\_IccExtend\_eq\_lintegral\_curveAction\_eq

**Lisini's superposition principle** in a complete separable metric space. Let `1 < p < ∞`
and let `μ` be a curve in `P_p(X)`, absolutely continuous on `[a, b]` with finite `p`-action,
where `a < b`. There is a probability measure `η` on `C([a, b], X)`, concentrated on absolutely
continuous paths, whose law at each time `t ∈ [a, b]` is `μ t`, whose expected `p`-action is the
`p`-action of `μ`, and whose averaged speed is the metric speed of `μ`:
`|μ'|(t) ^ p = ∫ |γ'|(t) ^ p dη` at almost every `t ∈ [a, b]`.

```lean
TauCeti.exists_map_IccExtend_eq_lintegral_curveAction_eq.{u_1} {X : Type u_1} [MetricSpace X]
  [MeasurableSpace X] [BorelSpace X] [SecondCountableTopology X] [CompleteSpace X] {p : ENNReal}
  [Fact (1 ≤ p)] (hp1 : 1 < p) (hp : p ≠ ⊤) {μ : ℝ → TauCeti.WassersteinSpace p X} {a b : ℝ}
  (hab : a < b) (hμ : AbsolutelyContinuousOnInterval μ a b)
  (hA : TauCeti.curveAction p.toReal μ a b ≠ ⊤) :
  ∃ η,
    MeasureTheory.IsProbabilityMeasure η ∧
      (∀ᵐ (γ : C(↑(Set.Icc a b), X)) ∂η, AbsolutelyContinuousOnInterval (Set.IccExtend ⋯ ⇑γ) a b) ∧
        (∀ t ∈ Set.Icc a b,
            MeasureTheory.Measure.map (fun γ => Set.IccExtend ⋯ (⇑γ) t) η = ↑↑(μ t)) ∧
          ∫⁻ (γ : C(↑(Set.Icc a b), X)), TauCeti.curveAction p.toReal (Set.IccExtend ⋯ ⇑γ) a b ∂η =
              TauCeti.curveAction p.toReal μ a b ∧
            ∀ᵐ (t : ℝ),
              t ∈ Set.Icc a b →
                TauCeti.metricDerivative μ t ^ p.toReal =
                  ∫⁻ (γ : C(↑(Set.Icc a b), X)),
                    TauCeti.metricDerivative (Set.IccExtend ⋯ ⇑γ) t ^ p.toReal ∂η
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_map_IccExtend_eq_lintegral_curveAction_eq`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Superposition.html#TauCeti.exists_map_IccExtend_eq_lintegral_curveAction_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_map_IccExtend_eq_lintegral_curveAction_eq`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Superposition.html#TauCeti.exists_map_IccExtend_eq_lintegral_curveAction_eq)
- [Source of `TauCeti.exists_map_IccExtend_eq_lintegral_curveAction_eq` in TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Superposition.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Superposition.lean#L188)
- [Tau Ceti roadmap status: Optimal transport and Wasserstein geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OptimalTransport/STATUS.md)
