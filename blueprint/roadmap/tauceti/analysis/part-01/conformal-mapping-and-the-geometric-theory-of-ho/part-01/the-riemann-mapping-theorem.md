---
declaration: theorem
origin: cited
lean: TauCeti.riemannMapping, TauCeti.exists_bijOn_ball_differentiableOn_invFunOn, TauCeti.riemannMapping_openPartialHomeomorph, TauCeti.riemannMapping_homeomorph, TauCeti.riemannMapping_of_hasHolomorphicSquareRoots, TauCeti.riemannMapping_normalized
statement: formalized
proof: formalized
---

# The Riemann mapping theorem

A simply connected open proper subset `Ω` of `ℂ` admits a
holomorphic bijection onto the open unit disc, with nonvanishing derivative throughout `Ω`.

Existence only: the map is not asserted to be unique, and no normalization is imposed.

```lean
TauCeti.riemannMapping {Ω : Set ℂ} (hΩo : IsOpen Ω) (hΩc : IsSimplyConnected Ω)
  (hΩ : Ω ≠ Set.univ) :
  ∃ f, Set.BijOn f Ω (Metric.ball 0 1) ∧ DifferentiableOn ℂ f Ω ∧ ∀ z ∈ Ω, deriv f z ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy estimate](../../../part-02/complex/part-01/cauchy-estimate.md)
- [Hurwitz's theorem](hurwitzs-theorem.md)
- [Montel's selection theorem](../../../part-02/complex/part-02/montels-selection-theorem.md)
- [Rouché's theorem for a disc, classical form](../part-02/rouches-theorem-for-a-disc-classical-form.md)
- [Strict Schwarz lemma](../part-02/strict-schwarz-lemma.md)
- [Uniqueness in the Riemann mapping theorem, up to a disc automorphism](../part-02/uniqueness-in-the-riemann-mapping-theorem-up-to.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.riemannMapping`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/RiemannMapping/Existence.html#TauCeti.riemannMapping).

## Other forms

**The Riemann mapping theorem as a biholomorphism.** Formalized in Tau Ceti as [`TauCeti.exists_bijOn_ball_differentiableOn_invFunOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/RiemannMapping/Existence.html#TauCeti.exists_bijOn_ball_differentiableOn_invFunOn).

```lean
TauCeti.exists_bijOn_ball_differentiableOn_invFunOn {Ω : Set ℂ} (hΩo : IsOpen Ω)
  (hΩc : IsSimplyConnected Ω) (hΩ : Ω ≠ Set.univ) :
  ∃ f,
    Set.BijOn f Ω (Metric.ball 0 1) ∧
      DifferentiableOn ℂ f Ω ∧
        DifferentiableOn ℂ (Function.invFunOn f Ω) (Metric.ball 0 1) ∧
          Set.LeftInvOn (Function.invFunOn f Ω) f Ω ∧
            Set.RightInvOn (Function.invFunOn f Ω) f (Metric.ball 0 1)
```

**The Riemann mapping theorem as a conformal open partial homeomorphism.** Formalized in Tau Ceti as [`TauCeti.riemannMapping_openPartialHomeomorph`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/RiemannMapping/Conformal.html#TauCeti.riemannMapping_openPartialHomeomorph).

```lean
TauCeti.riemannMapping_openPartialHomeomorph {Ω : Set ℂ} (hΩo : IsOpen Ω)
  (hΩc : IsSimplyConnected Ω) (hΩ : Ω ≠ Set.univ) :
  ∃ e,
    e.source = Ω ∧
      e.target = Metric.ball 0 1 ∧
        DifferentiableOn ℂ (↑e) Ω ∧
          DifferentiableOn ℂ (↑e.symm) (Metric.ball 0 1) ∧
            (∀ z ∈ Ω, ConformalAt (↑e) z) ∧ ∀ w ∈ Metric.ball 0 1, ConformalAt (↑e.symm) w
```

**The Riemann mapping theorem as a homeomorphism.** Formalized in Tau Ceti as [`TauCeti.riemannMapping_homeomorph`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/RiemannMapping/Conformal.html#TauCeti.riemannMapping_homeomorph).

```lean
TauCeti.riemannMapping_homeomorph {Ω : Set ℂ} (hΩo : IsOpen Ω) (hΩc : IsSimplyConnected Ω)
  (hΩ : Ω ≠ Set.univ) : Nonempty (↑Ω ≃ₜ Complex.UnitDisc)
```

**The Riemann mapping theorem for domains with holomorphic square roots.** Formalized in Tau Ceti as [`TauCeti.riemannMapping_of_hasHolomorphicSquareRoots`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/RiemannMapping/Existence.html#TauCeti.riemannMapping_of_hasHolomorphicSquareRoots).

```lean
TauCeti.riemannMapping_of_hasHolomorphicSquareRoots {Ω : Set ℂ} (hΩo : IsOpen Ω)
  (hΩc : IsConnected Ω) (hΩs : TauCeti.HasHolomorphicSquareRoots Ω) (hΩ : Ω ≠ Set.univ) :
  ∃ f, Set.BijOn f Ω (Metric.ball 0 1) ∧ DifferentiableOn ℂ f Ω ∧ ∀ z ∈ Ω, deriv f z ≠ 0
```

**The Riemann mapping theorem, normalized.** Formalized in Tau Ceti as [`TauCeti.riemannMapping_normalized`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/RiemannMapping/Normalization.html#TauCeti.riemannMapping_normalized).

```lean
TauCeti.riemannMapping_normalized {Ω : Set ℂ} {z₀ : ℂ} (hΩo : IsOpen Ω) (hΩc : IsSimplyConnected Ω)
  (hΩ : Ω ≠ Set.univ) (hz₀ : z₀ ∈ Ω) :
  ∃ f,
    TauCeti.IsNormalizedRiemannMapOn f Ω z₀ ∧
      ∀ (g : ℂ → ℂ), TauCeti.IsNormalizedRiemannMapOn g Ω z₀ → Set.EqOn g f Ω
```

## Sources

- [Tau Ceti documentation: `TauCeti.riemannMapping`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/RiemannMapping/Existence.html#TauCeti.riemannMapping)
- [Source of `TauCeti.riemannMapping` in TauCeti/Analysis/Complex/Conformal/RiemannMapping/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/RiemannMapping/Existence.lean#L84)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ConformalMapping/STATUS.md)
