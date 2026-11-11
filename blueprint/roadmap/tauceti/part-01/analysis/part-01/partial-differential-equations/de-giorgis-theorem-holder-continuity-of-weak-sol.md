---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_holderOnWith_preciseRepresentative, TauCeti.PDE.exists_holderOnWith_preciseRepresentative_jumpCoefficient, TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_isCompact, TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_isCompact_drift, TauCeti.PDE.exists_holderOnWith_preciseRepresentative_drift, TauCeti.PDE.exists_holderOnWith_preciseRepresentative_of_memLp
statement: formalized
proof: formalized
---

# De Giorgi's theorem: Hölder continuity of weak solutions

Let `n ≥ 1` be the
dimension. There are `α ∈ (0, 1]` and `C > 0`, depending only on `λ`, `Λ`, the dimension and the
normalization of the additive Haar measure `mu`, such that the following holds. Let `a` be
measurable and uniformly elliptic on `Ω` with constants `λ, Λ`, and let `u ∈ H¹(Ω)` be a weak
solution of `-∂ᵢ(aⁱʲ ∂ⱼu) = 0`. If the closed `R`-thickening of a set `K` lies in `Ω`, then the
precise representative of `u` is Hölder continuous on `K` with exponent `α` and constant
`C R^(-α - n/2) ‖u‖_{L²(Ω)}`.

The precise representative agrees with `u` almost everywhere on `Ω`
(`TauCeti.W1p.ae_eq_preciseRepresentative`). No regularity of the coefficients
beyond measurability is assumed. This is the case `b = 0` of
`TauCeti.PDE.exists_holderOnWith_preciseRepresentative_drift`.

```lean
TauCeti.PDE.exists_holderOnWith_preciseRepresentative.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {lam Lam : ℝ} [Nonempty ι] :
  ∃ α C,
    0 < α ∧
      α ≤ 1 ∧
        0 < C ∧
          ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
            {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {u : ↥(TauCeti.W1p mu Omega 2)}
            {K : Set (EuclideanSpace ℝ ι)} {R : ℝ},
            TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
              MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
                (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)), TauCeti.PDE.energyFormH1 a 0 0 u ↑v = 0) →
                  0 < R →
                    Metric.cthickening R K ⊆ ↑Omega →
                      HolderOnWith
                        (C * R ^ (-↑α) *
                            (R ^ (-↑(Fintype.card ι) / 2) *
                              √(∫ (y : EuclideanSpace ℝ ι) in ↑Omega,
                                  ↑↑(TauCeti.W1p.value u) y ^ 2 ∂mu))).toNNReal
                        α (TauCeti.MeasureTheory.preciseRepresentative mu ↑↑(TauCeti.W1p.value u)) K
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The `L²` Leibniz estimate](../../part-03/sobolev/part-01/the-l2-leibniz-estimate.md)
- [The analytic content of the extension theorem](../../part-03/sobolev/part-01/the-analytic-content-of-the-extension-theorem.md)
- [Chebyshev's inequality for truncations](../../../measure-theory/integral/part-01/chebyshevs-inequality-for-truncations.md)
- [De Giorgi's interior oscillation estimate](de-giorgis-interior-oscillation-estimate.md)
- [Gårding's inequality on `H¹(Ω)`](../../part-03/pde/part-01/gardings-inequality-on-h1.md)
- [Hölder's inequality for Young's exponents](../../../measure-theory/integral/part-01/holders-inequality-for-youngs-exponents.md)
- [The Poincaré inequality on a ball](../../part-03/sobolev/part-02/the-poincare-inequality-on-a-ball.md)
- [The Sobolev inequality on `W^{1,p}_0` of a ball](../../part-03/sobolev/part-02/the-sobolev-inequality-on-w-1-p-0-of-a-ball.md)
- [Stampacchia's global bound](../../part-03/pde/part-02/stampacchias-global-bound.md)
- [TauCeti.Wkp](tauceti-wkp.md)
- [The zero-forcing Caccioppoli inequality for a positive truncation of a weak subsolution](../../part-03/pde/part-03/the-zero-forcing-caccioppoli-inequality-for-a-po.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_preciseRepresentative`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/HolderContinuity.html#TauCeti.PDE.exists_holderOnWith_preciseRepresentative).

## Other forms

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
  [mu.IsAddHaarMeasure] {lam Lam : ℝ} [Nonempty ι] :
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

**De Giorgi's theorem with a drift: Hölder continuity of weak solutions.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_preciseRepresentative_drift`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/HolderContinuity.html#TauCeti.PDE.exists_holderOnWith_preciseRepresentative_drift).

```lean
TauCeti.PDE.exists_holderOnWith_preciseRepresentative_drift.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {lam Lam : ℝ} [Nonempty ι] (σ : ℝ) :
  ∃ α C,
    0 < α ∧
      α ≤ 1 ∧
        0 < C ∧
          ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
            {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι}
            {beta : ℝ} {u : ↥(TauCeti.W1p mu Omega 2)} {K : Set (EuclideanSpace ℝ ι)} {R : ℝ},
            TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
              MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
                MeasureTheory.AEStronglyMeasurable b (mu.restrict ↑Omega) →
                  (∀ x ∈ ↑Omega, ‖b x‖ ≤ beta) →
                    (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)), TauCeti.PDE.energyFormH1 a b 0 u ↑v = 0) →
                      0 < R →
                        Metric.cthickening R K ⊆ ↑Omega →
                          beta * R ≤ σ * lam →
                            HolderOnWith
                              (C * R ^ (-↑α) *
                                  (R ^ (-↑(Fintype.card ι) / 2) *
                                    √(∫ (y : EuclideanSpace ℝ ι) in ↑Omega,
                                        ↑↑(TauCeti.W1p.value u) y ^ 2 ∂mu))).toNNReal
                              α
                              (TauCeti.MeasureTheory.preciseRepresentative mu
                                ↑↑(TauCeti.W1p.value u))
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

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_holderOnWith_preciseRepresentative`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/HolderContinuity.html#TauCeti.PDE.exists_holderOnWith_preciseRepresentative)
- [Source of `TauCeti.PDE.exists_holderOnWith_preciseRepresentative` in TauCeti/Analysis/PDE/Regularity/HolderContinuity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Regularity/HolderContinuity.lean#L155)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PDE/STATUS.md)
