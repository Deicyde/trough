---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_holderOnWith_preciseRepresentative_sub_compHyperplaneReflectionL, TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_isUniformlyEllipticAE, TauCeti.PDE.exists_holderOnWith_preciseRepresentative_jumpCoefficient, TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_isCompact, TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_isCompact_drift, TauCeti.PDE.exists_holderOnWith_preciseRepresentative_sub_compHyperplaneReflectionL_drift, TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_memLp, TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_memLp_add_divergence, TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_memLp_divergence, TauCeti.PDE.exists_holderOnWith_preciseRepresentative_sub_compHyperplaneReflectionL_of_memLp
statement: formalized
proof: formalized
---

# De Giorgi's theorem up to a flat boundary

Let `n ≥ 1` be the dimension. There are
`α ∈ (0, 1]` and `C > 0`, depending only on `λ`, `Λ`, the dimension and the normalization of the
additive Haar measure `mu`, such that the following holds. Let `H = {x | c₀ < ⟪x, ν⟫}` with
`ν ≠ 0`, let `ρ` be the reflection in the hyperplane `∂H` and let `U` be open with `ρ U ⊆ U`. Let
`a` be measurable on `U ∩ H` and uniformly elliptic with constants `λ, Λ` on the part of `U` in
the closed half-space `{x | c₀ ≤ ⟪x, ν⟫}`. Let `u ∈ H¹(U)` vanish on `U ∖ H` and let its
restriction to `U ∩ H` be a weak solution of `-∂ᵢ(aⁱʲ ∂ⱼu) = 0`. If the closed `R`-thickening of
a set `K` lies in `U`, then the precise representative of the odd reflection `w = u - u ∘ ρ`,
which agrees with `u` on `U ∩ H`, is Hölder continuous on `K` with exponent `α` and constant
`C R^(-α - n/2) ‖w‖_{L²(U)}`. This is the case `b = 0` of
`TauCeti.PDE.exists_holderOnWith_preciseRepresentative_sub_compHyperplaneReflectionL_drift`.

```lean
TauCeti.PDE.exists_holderOnWith_preciseRepresentative_sub_compHyperplaneReflectionL.{u_1}
  {ι : Type u_1} [Fintype ι] [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  [mu.IsAddHaarMeasure] {lam Lam : ℝ} [Nonempty ι] :
  ∃ α C,
    0 < α ∧
      α ≤ 1 ∧
        0 < C ∧
          ∀ {U H : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {ν : EuclideanSpace ℝ ι} {c₀ : ℝ}
            {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {u : ↥(TauCeti.W1p mu U 2)}
            {K : Set (EuclideanSpace ℝ ι)} {R : ℝ},
            ν ≠ 0 →
              (∀ (x : EuclideanSpace ℝ ι), x ∈ H ↔ c₀ < inner ℝ x ν) →
                ∀ (hU : Set.MapsTo ⇑(TauCeti.hyperplaneReflection ν c₀) ↑U ↑U),
                  TauCeti.PDE.UniformlyEllipticOn {x | x ∈ U ∧ c₀ ≤ inner ℝ x ν} a lam Lam →
                    MeasureTheory.AEStronglyMeasurable a (mu.restrict (↑U ∩ ↑H)) →
                      (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑U,
                          x ∉ H → ↑↑(TauCeti.W1p.value u) x = 0) →
                        (∀ (v : ↥(TauCeti.W1p0 mu (U ⊓ H) 2)),
                            TauCeti.PDE.energyFormH1 a 0 0 ((TauCeti.W1p.restrictL ⋯) u) ↑v = 0) →
                          0 < R →
                            Metric.cthickening R K ⊆ ↑U →
                              HolderOnWith
                                (C * R ^ (-↑α) *
                                    (R ^ (-↑(Fintype.card ι) / 2) *
                                      √(∫ (y : EuclideanSpace ℝ ι) in ↑U,
                                          ↑↑(TauCeti.W1p.value
                                                    (u -
                                                      (TauCeti.W1p.compHyperplaneReflectionL ⋯ ν c₀
                                                          hU)
                                                        u))
                                              y ^
                                            2 ∂mu))).toNNReal
                                α
                                (TauCeti.MeasureTheory.preciseRepresentative mu
                                  ↑↑(TauCeti.W1p.value
                                        (u - (TauCeti.W1p.compHyperplaneReflectionL ⋯ ν c₀ hU) u)))
                                K
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The `L²` Leibniz estimate](../../part-04/sobolev/part-01/the-l2-leibniz-estimate.md)
- [The analytic content of the extension theorem](../../part-04/sobolev/part-01/the-analytic-content-of-the-extension-theorem.md)
- [Chebyshev's inequality for truncations](../../../measure-theory/integral/part-01/chebyshevs-inequality-for-truncations.md)
- [De Giorgi's interior oscillation estimate](../../part-04/pde/part-01/de-giorgis-interior-oscillation-estimate.md)
- [De Giorgi's theorem: Hölder continuity of weak solutions](de-giorgis-theorem-holder-continuity-of-weak-sol.md)
- [Gårding's inequality on `H¹(Ω)`](../../part-04/pde/part-02/gardings-inequality-on-h1.md)
- [Hölder's inequality with a bounded weight](../../../measure-theory/integral/part-02/holders-inequality-with-a-bounded-weight.md)
- [Meyers–Serrin: `H = W` in `W^{k,p}(Ω)`](../../part-04/sobolev/part-02/meyers-serrin-h-w-in-w-k-p.md)
- [The Poincaré inequality on a ball](../../part-04/sobolev/part-02/the-poincare-inequality-on-a-ball.md)
- [The Sobolev inequality on `W^{1,p}_0` of a ball](../../part-04/sobolev/part-02/the-sobolev-inequality-on-w-1-p-0-of-a-ball.md)
- [Stampacchia's bound on a ball](../../part-04/pde/part-03/stampacchias-bound-on-a-ball.md)
- [Stampacchia's global bound](../../part-04/pde/part-03/stampacchias-global-bound.md)
- [The zero-forcing Caccioppoli inequality for a positive truncation of a weak subsolution](../../part-04/pde/part-04/the-zero-forcing-caccioppoli-inequality-for-a-po.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_preciseRepresentative_sub_compHyperplaneReflectionL`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Boundary/Holder.html#TauCeti.PDE.exists_holderOnWith_preciseRepresentative_sub_compHyperplaneReflectionL).

## Other forms

**De Giorgi's theorem on a ball.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_isUniformlyEllipticAE`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/InverseCoercive.html#TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_isUniformlyEllipticAE).

```lean
TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_isUniformlyEllipticAE.{u_1} {ι : Type u_1}
  [Fintype ι] [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  [mu.IsAddHaarMeasure] (ratio : ℝ) :
  ∃ α C,
    0 < α ∧
      α ≤ 1 ∧
        0 < C ∧
          ∀ {lam Lam : ℝ} {x₀ : EuclideanSpace ℝ ι} {r : ℝ} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
            {u : ↥(TauCeti.W1p mu { carrier := Metric.ball x₀ (2 * r), is_open' := ⋯ } 2)},
            TauCeti.PDE.IsUniformlyEllipticAE mu (Metric.ball x₀ (2 * r)) a lam Lam →
              Lam ≤ ratio * lam →
                MeasureTheory.AEStronglyMeasurable a (mu.restrict (Metric.ball x₀ (2 * r))) →
                  (∀
                      (v :
                        ↥(TauCeti.W1p0 mu { carrier := Metric.ball x₀ (2 * r), is_open' := ⋯ } 2)),
                      TauCeti.PDE.energyFormH1 a 0 0 u ↑v = 0) →
                    HolderOnWith
                      (C * r ^ (-↑α) *
                          (r ^ (-↑(Fintype.card ι) / 2) *
                            √(∫ (y : EuclideanSpace ℝ ι) in Metric.ball x₀ (2 * r),
                                ↑↑(TauCeti.W1p.value u) y ^ 2 ∂mu))).toNNReal
                      α (TauCeti.MeasureTheory.preciseRepresentative mu ↑↑(TauCeti.W1p.value u))
                      (Metric.ball x₀ r)
```

**De Giorgi's theorem on an equation with a discontinuous coefficient.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_preciseRepresentative_jumpCoefficient`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/JumpCoefficient.html#TauCeti.PDE.exists_holderOnWith_preciseRepresentative_jumpCoefficient).

```lean
TauCeti.PDE.exists_holderOnWith_preciseRepresentative_jumpCoefficient (n : ℕ) :
  ∃ α,
    0 < α ∧
      α ≤ 1 ∧
        ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ (Fin (n + 1)))},
          Bornology.IsBounded ↑Omega →
            (↑Omega).Nonempty →
              ∃ g,
                (↑↑(TauCeti.W1p.value g) =ᵐ[MeasureTheory.volume.restrict ↑Omega] fun x =>
                    x.ofLp 0) ∧
                  (∃! u,
                      u - g ∈ TauCeti.w1p0Submodule MeasureTheory.volume Omega 2 ∧
                        ∀ (v : ↥(TauCeti.W1p0 MeasureTheory.volume Omega 2)),
                          TauCeti.PDE.energyFormH1 (TauCeti.PDE.jumpCoefficient n) 0 0 u ↑v = 0) ∧
                    ∀ (u : ↥(TauCeti.W1p MeasureTheory.volume Omega 2)),
                      (u - g ∈ TauCeti.w1p0Submodule MeasureTheory.volume Omega 2 ∧
                          ∀ (v : ↥(TauCeti.W1p0 MeasureTheory.volume Omega 2)),
                            TauCeti.PDE.energyFormH1 (TauCeti.PDE.jumpCoefficient n) 0 0 u ↑v = 0) →
                        (¬∃ c,
                              ↑↑(TauCeti.W1p.value u) =ᵐ[MeasureTheory.volume.restrict ↑Omega]
                                fun x => c) ∧
                          ∀ (K : Set (EuclideanSpace ℝ (Fin (n + 1)))),
                            IsCompact K →
                              K ⊆ ↑Omega →
                                ∃ C,
                                  HolderOnWith C α
                                    (TauCeti.MeasureTheory.preciseRepresentative
                                      MeasureTheory.volume ↑↑(TauCeti.W1p.value u))
                                    K
```

**De Giorgi's theorem on compact sets.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_isCompact`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/HolderContinuity.html#TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_isCompact).

```lean
TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_isCompact.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {lam Lam : ℝ} :
  ∃ α,
    0 < α ∧
      α ≤ 1 ∧
        ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
          {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {u : ↥(TauCeti.W1p mu Omega 2)}
          {K : Set (EuclideanSpace ℝ ι)},
          TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
            MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
              (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)), TauCeti.PDE.energyFormH1 a 0 0 u ↑v = 0) →
                IsCompact K →
                  K ⊆ ↑Omega →
                    ∃ C,
                      HolderOnWith C α
                        (TauCeti.MeasureTheory.preciseRepresentative mu ↑↑(TauCeti.W1p.value u)) K
```

**De Giorgi's theorem with a drift on compact sets.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_isCompact_drift`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/HolderContinuity.html#TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_isCompact_drift).

```lean
TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_isCompact_drift.{u_1} {ι : Type u_1}
  [Fintype ι] [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  [mu.IsAddHaarMeasure] {lam Lam : ℝ} :
  ∃ α,
    0 < α ∧
      α ≤ 1 ∧
        ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
          {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι}
          {beta : ℝ} {u : ↥(TauCeti.W1p mu Omega 2)} {K : Set (EuclideanSpace ℝ ι)},
          TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
            MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
              MeasureTheory.AEStronglyMeasurable b (mu.restrict ↑Omega) →
                (∀ x ∈ ↑Omega, ‖b x‖ ≤ beta) →
                  (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)), TauCeti.PDE.energyFormH1 a b 0 u ↑v = 0) →
                    IsCompact K →
                      K ⊆ ↑Omega →
                        ∃ C,
                          HolderOnWith C α
                            (TauCeti.MeasureTheory.preciseRepresentative mu ↑↑(TauCeti.W1p.value u))
                            K
```

**De Giorgi's theorem with a drift up to a flat boundary.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_preciseRepresentative_sub_compHyperplaneReflectionL_drift`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Boundary/Holder.html#TauCeti.PDE.exists_holderOnWith_preciseRepresentative_sub_compHyperplaneReflectionL_drift).

```lean
TauCeti.PDE.exists_holderOnWith_preciseRepresentative_sub_compHyperplaneReflectionL_drift.{u_1}
  {ι : Type u_1} [Fintype ι] [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  [mu.IsAddHaarMeasure] {lam Lam : ℝ} [Nonempty ι] (σ : ℝ) :
  ∃ α C,
    0 < α ∧
      α ≤ 1 ∧
        0 < C ∧
          ∀ {U H : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {ν : EuclideanSpace ℝ ι} {c₀ : ℝ}
            {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι}
            {beta : ℝ} {u : ↥(TauCeti.W1p mu U 2)} {K : Set (EuclideanSpace ℝ ι)} {R : ℝ},
            ν ≠ 0 →
              (∀ (x : EuclideanSpace ℝ ι), x ∈ H ↔ c₀ < inner ℝ x ν) →
                ∀ (hU : Set.MapsTo ⇑(TauCeti.hyperplaneReflection ν c₀) ↑U ↑U),
                  TauCeti.PDE.UniformlyEllipticOn {x | x ∈ U ∧ c₀ ≤ inner ℝ x ν} a lam Lam →
                    MeasureTheory.AEStronglyMeasurable a (mu.restrict (↑U ∩ ↑H)) →
                      MeasureTheory.AEStronglyMeasurable b (mu.restrict (↑U ∩ ↑H)) →
                        (∀ x ∈ {x | x ∈ U ∧ c₀ ≤ inner ℝ x ν}, ‖b x‖ ≤ beta) →
                          (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑U,
                              x ∉ H → ↑↑(TauCeti.W1p.value u) x = 0) →
                            (∀ (v : ↥(TauCeti.W1p0 mu (U ⊓ H) 2)),
                                TauCeti.PDE.energyFormH1 a b 0 ((TauCeti.W1p.restrictL ⋯) u) ↑v =
                                  0) →
                              0 < R →
                                Metric.cthickening R K ⊆ ↑U →
                                  beta * R ≤ σ * lam →
                                    HolderOnWith
                                      (C * R ^ (-↑α) *
                                          (R ^ (-↑(Fintype.card ι) / 2) *
                                            √(∫ (y : EuclideanSpace ℝ ι) in ↑U,
                                                ↑↑(TauCeti.W1p.value
                                                          (u -
                                                            (TauCeti.W1p.compHyperplaneReflectionL ⋯
                                                                ν c₀ hU)
                                                              u))
                                                    y ^
                                                  2 ∂mu))).toNNReal
                                      α
                                      (TauCeti.MeasureTheory.preciseRepresentative mu
                                        ↑↑(TauCeti.W1p.value
                                              (u -
                                                (TauCeti.W1p.compHyperplaneReflectionL ⋯ ν c₀ hU)
                                                  u)))
                                      K
```

**De Giorgi's theorem with a right-hand side.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_memLp`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Inhomogeneous.html#TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_memLp).

```lean
TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_memLp.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  [Nonempty ι] {lam Lam : ℝ} {r : NNReal} (hr : 1 < r) (hrn : ↑(Fintype.card ι) < 2 * ↑r) :
  ∃ α C,
    0 < α ∧
      α ≤ 1 ∧
        0 < C ∧
          ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
            {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {f : EuclideanSpace ℝ ι → ℝ}
            {u : ↥(TauCeti.W1p mu Omega 2)} {K : Set (EuclideanSpace ℝ ι)} {R : ℝ},
            TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
              MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
                MeasureTheory.MemLp f (↑r) (mu.restrict ↑Omega) →
                  (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
                      TauCeti.PDE.energyFormH1 a 0 0 u ↑v =
                        ∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
                          f x * ↑↑(TauCeti.W1p.value ↑v) x ∂mu) →
                    0 < R →
                      Metric.cthickening R K ⊆ ↑Omega →
                        HolderOnWith
                          (C * R ^ (-↑α) *
                              (R ^ (-↑(Fintype.card ι) / 2) *
                                  √(∫ (y : EuclideanSpace ℝ ι) in ↑Omega,
                                      ↑↑(TauCeti.W1p.value u) y ^ 2 ∂mu) +
                                R ^ (2 - ↑(Fintype.card ι) / ↑r) *
                                    (MeasureTheory.eLpNorm f (↑r) (mu.restrict ↑Omega)).toReal /
                                  lam)).toNNReal
                          α (TauCeti.MeasureTheory.preciseRepresentative mu ↑↑(TauCeti.W1p.value u))
                          K
```

**De Giorgi's theorem with a right-hand side `f + ∂ᵢFⁱ`.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_memLp_add_divergence`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Inhomogeneous.html#TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_memLp_add_divergence).

```lean
TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_memLp_add_divergence.{u_1} {ι : Type u_1}
  [Fintype ι] [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  [mu.IsAddHaarMeasure] [Nonempty ι] {lam Lam : ℝ} {r q : NNReal} (hr : 1 < r)
  (hrn : ↑(Fintype.card ι) < 2 * ↑r) (hq : 2 < ↑q) (hqn : ↑(Fintype.card ι) < ↑q) :
  ∃ α C,
    0 < α ∧
      α ≤ 1 ∧
        0 < C ∧
          ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
            {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {f : EuclideanSpace ℝ ι → ℝ}
            {F : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {u : ↥(TauCeti.W1p mu Omega 2)}
            {K : Set (EuclideanSpace ℝ ι)} {R : ℝ},
            TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
              MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
                MeasureTheory.MemLp f (↑r) (mu.restrict ↑Omega) →
                  MeasureTheory.MemLp F (↑q) (mu.restrict ↑Omega) →
                    (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
                        TauCeti.PDE.energyFormH1 a 0 0 u ↑v =
                          ∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
                              f x * ↑↑(TauCeti.W1p.value ↑v) x ∂mu -
                            ∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
                              inner ℝ (F x) (↑↑(TauCeti.W1p.gradient ↑v) x) ∂mu) →
                      0 < R →
                        Metric.cthickening R K ⊆ ↑Omega →
                          HolderOnWith
                            (C * R ^ (-↑α) *
                                (R ^ (-↑(Fintype.card ι) / 2) *
                                    √(∫ (y : EuclideanSpace ℝ ι) in ↑Omega,
                                        ↑↑(TauCeti.W1p.value u) y ^ 2 ∂mu) +
                                  (R ^ (2 - ↑(Fintype.card ι) / ↑r) *
                                        (MeasureTheory.eLpNorm f (↑r) (mu.restrict ↑Omega)).toReal +
                                      R ^ (1 - ↑(Fintype.card ι) / ↑q) *
                                        (MeasureTheory.eLpNorm F (↑q)
                                            (mu.restrict ↑Omega)).toReal) /
                                    lam)).toNNReal
                            α
                            (TauCeti.MeasureTheory.preciseRepresentative mu ↑↑(TauCeti.W1p.value u))
                            K
```

**De Giorgi's theorem with a right-hand side in divergence form.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_memLp_divergence`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Inhomogeneous.html#TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_memLp_divergence).

```lean
TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_memLp_divergence.{u_1} {ι : Type u_1}
  [Fintype ι] [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  [mu.IsAddHaarMeasure] [Nonempty ι] {lam Lam : ℝ} {q : NNReal} (hq : 2 < ↑q)
  (hqn : ↑(Fintype.card ι) < ↑q) :
  ∃ α C,
    0 < α ∧
      α ≤ 1 ∧
        0 < C ∧
          ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
            {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {F : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι}
            {u : ↥(TauCeti.W1p mu Omega 2)} {K : Set (EuclideanSpace ℝ ι)} {R : ℝ},
            TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
              MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
                MeasureTheory.MemLp F (↑q) (mu.restrict ↑Omega) →
                  (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
                      TauCeti.PDE.energyFormH1 a 0 0 u ↑v =
                        -∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
                            inner ℝ (F x) (↑↑(TauCeti.W1p.gradient ↑v) x) ∂mu) →
                    0 < R →
                      Metric.cthickening R K ⊆ ↑Omega →
                        HolderOnWith
                          (C * R ^ (-↑α) *
                              (R ^ (-↑(Fintype.card ι) / 2) *
                                  √(∫ (y : EuclideanSpace ℝ ι) in ↑Omega,
                                      ↑↑(TauCeti.W1p.value u) y ^ 2 ∂mu) +
                                R ^ (1 - ↑(Fintype.card ι) / ↑q) *
                                    (MeasureTheory.eLpNorm F (↑q) (mu.restrict ↑Omega)).toReal /
                                  lam)).toNNReal
                          α (TauCeti.MeasureTheory.preciseRepresentative mu ↑↑(TauCeti.W1p.value u))
                          K
```

**De Giorgi's theorem with a right-hand side up to a flat boundary.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_preciseRepresentative_sub_compHyperplaneReflectionL_of_memLp`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Boundary/Holder.html#TauCeti.PDE.exists_holderOnWith_preciseRepresentative_sub_compHyperplaneReflectionL_of_memLp).

```lean
TauCeti.PDE.exists_holderOnWith_preciseRepresentative_sub_compHyperplaneReflectionL_of_memLp.{u_1}
  {ι : Type u_1} [Fintype ι] [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  [mu.IsAddHaarMeasure] [Nonempty ι] {lam Lam : ℝ} {r : NNReal} (hr : 1 < r)
  (hrn : ↑(Fintype.card ι) < 2 * ↑r) :
  ∃ α C,
    0 < α ∧
      α ≤ 1 ∧
        0 < C ∧
          ∀ {U H : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {ν : EuclideanSpace ℝ ι} {c₀ : ℝ}
            {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {f : EuclideanSpace ℝ ι → ℝ}
            {u : ↥(TauCeti.W1p mu U 2)} {K : Set (EuclideanSpace ℝ ι)} {R : ℝ},
            ν ≠ 0 →
              (∀ (x : EuclideanSpace ℝ ι), x ∈ H ↔ c₀ < inner ℝ x ν) →
                ∀ (hU : Set.MapsTo ⇑(TauCeti.hyperplaneReflection ν c₀) ↑U ↑U),
                  TauCeti.PDE.UniformlyEllipticOn {x | x ∈ U ∧ c₀ ≤ inner ℝ x ν} a lam Lam →
                    MeasureTheory.AEStronglyMeasurable a (mu.restrict (↑U ∩ ↑H)) →
                      MeasureTheory.MemLp f 2 (mu.restrict (↑U ∩ ↑H)) →
                        MeasureTheory.MemLp f (↑r) (mu.restrict (↑U ∩ ↑H)) →
                          (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑U,
                              x ∉ H → ↑↑(TauCeti.W1p.value u) x = 0) →
                            (∀ (v : ↥(TauCeti.W1p0 mu (U ⊓ H) 2)),
                                TauCeti.PDE.energyFormH1 a 0 0 ((TauCeti.W1p.restrictL ⋯) u) ↑v =
                                  ∫ (x : EuclideanSpace ℝ ι) in ↑U ∩ ↑H,
                                    f x * ↑↑(TauCeti.W1p.value ↑v) x ∂mu) →
                              0 < R →
                                Metric.cthickening R K ⊆ ↑U →
                                  HolderOnWith
                                    (C * R ^ (-↑α) *
                                        (R ^ (-↑(Fintype.card ι) / 2) *
                                            √(∫ (y : EuclideanSpace ℝ ι) in ↑U,
                                                ↑↑(TauCeti.W1p.value
                                                          (u -
                                                            (TauCeti.W1p.compHyperplaneReflectionL ⋯
                                                                ν c₀ hU)
                                                              u))
                                                    y ^
                                                  2 ∂mu) +
                                          R ^ (2 - ↑(Fintype.card ι) / ↑r) *
                                              (MeasureTheory.eLpNorm f (↑r)
                                                  (mu.restrict (↑U ∩ ↑H))).toReal /
                                            lam)).toNNReal
                                    α
                                    (TauCeti.MeasureTheory.preciseRepresentative mu
                                      ↑↑(TauCeti.W1p.value
                                            (u -
                                              (TauCeti.W1p.compHyperplaneReflectionL ⋯ ν c₀ hU) u)))
                                    K
```

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_holderOnWith_preciseRepresentative_sub_compHyperplaneReflectionL`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Boundary/Holder.html#TauCeti.PDE.exists_holderOnWith_preciseRepresentative_sub_compHyperplaneReflectionL)
- [Source of `TauCeti.PDE.exists_holderOnWith_preciseRepresentative_sub_compHyperplaneReflectionL` in TauCeti/Analysis/PDE/Regularity/Boundary/Holder.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Regularity/Boundary/Holder.lean#L130)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PDE/STATUS.md)
