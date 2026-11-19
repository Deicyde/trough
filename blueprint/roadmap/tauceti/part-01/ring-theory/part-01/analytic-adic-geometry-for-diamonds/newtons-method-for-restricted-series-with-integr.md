---
declaration: theorem
origin: cited
lean: TauCeti.Huber.existsUnique_weightedEval_eq_zero
statement: formalized
proof: formalized
---

# Newton's method for restricted series with integral coefficients

Let `C` be Hausdorff,
let `ϖ ∈ A₀` be a pseudouniformiser, and let `M` be an integral matrix with `M J(t) = ϖᵏ`, where
`J(t) = (∂ⱼFᵢ(t))` is the Jacobian matrix of `F` at `t ∈ A₀^N`. If `F(t) ∈ ϖ^(2k + 1) A₀^N`, then
`F` has exactly one zero `u ∈ A₀^N` with `u ≡ t mod ϖ^(k + 1)`.

```lean
TauCeti.Huber.existsUnique_weightedEval_eq_zero.{u_1} {C : Type u_1} [CommRing C] [UniformSpace C]
  [IsUniformAddGroup C] [IsTopologicalRing C] [CompleteSpace C]
  (P : TauCeti.Huber.PairOfDefinition C) {N : ℕ} {ϖ : ↥P.ringOfDefinition}
  {F : Fin N → MvPowerSeries (Fin N) C} [T0Space C] (hϖ : TauCeti.Huber.IsPseudoUniformizer ↑ϖ)
  (hF : ∀ (i : Fin N), TauCeti.Huber.IsWeightedRestricted (fun x => {1}) (F i))
  (hF₀ : ∀ (i : Fin N) (ν : Fin N →₀ ℕ), (MvPowerSeries.coeff ν) (F i) ∈ P.ringOfDefinition)
  (t : Fin N → ↥P.ringOfDefinition) {k : ℕ} {M : Matrix (Fin N) (Fin N) ↥P.ringOfDefinition}
  (hM :
    (M.map Subtype.val *
        Matrix.of fun i j =>
          TauCeti.Huber.weightedEval (RingHom.id C) (fun l => ↑(t l))
            ((MvPowerSeries.pderiv j) (F i))) =
      ↑ϖ ^ k • 1)
  (ht :
    ∀ (i : Fin N),
      TauCeti.Huber.weightedEval (RingHom.id C) (fun l => ↑(t l)) (F i) ∈
        ↑ϖ ^ (2 * k + 1) • ↑P.ringOfDefinition) :
  ∃! u,
    (∀ (i : Fin N), ϖ ^ (k + 1) ∣ u i - t i) ∧
      ∀ (i : Fin N), TauCeti.Huber.weightedEval (RingHom.id C) (fun l => ↑(u l)) (F i) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Taylor's estimate for restricted series with integral coefficients](taylors-estimate-for-restricted-series-with-inte.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.existsUnique_weightedEval_eq_zero`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/WeightedEval/Newton.html#TauCeti.Huber.existsUnique_weightedEval_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.existsUnique_weightedEval_eq_zero`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/WeightedEval/Newton.html#TauCeti.Huber.existsUnique_weightedEval_eq_zero)
- [Source of `TauCeti.Huber.existsUnique_weightedEval_eq_zero` in TauCeti/RingTheory/Huber/WeightedEval/Newton.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Huber/WeightedEval/Newton.lean#L206)
- [Tau Ceti roadmap status: Analytic adic geometry for diamonds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicEtaleGeometry/STATUS.md)
