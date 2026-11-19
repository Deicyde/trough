---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_holderOnWith_preciseRepresentative, TauCeti.PDE.exists_holderOnWith_preciseRepresentative_drift
statement: formalized
proof: formalized
---

# De Giorgi's theorem: Hölder continuity of weak solutions

Let `n` be the
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
  {lam Lam : ℝ} :
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

- [The `L²` Leibniz estimate](../../part-04/sobolev/part-01/the-l2-leibniz-estimate.md)
- [Chebyshev's inequality for truncations](../../../measure-theory/integral/part-01/chebyshevs-inequality-for-truncations.md)
- [De Giorgi's interior oscillation estimate](../../part-04/pde/part-01/de-giorgis-interior-oscillation-estimate.md)
- [The Sobolev inequality on `W^{1,p}_0` of a ball](../../part-04/sobolev/part-02/the-sobolev-inequality-on-w-1-p-0-of-a-ball.md)
- [The zero-forcing Caccioppoli inequality for a positive truncation of a weak subsolution](../../part-04/pde/part-04/the-zero-forcing-caccioppoli-inequality-for-a-po.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_preciseRepresentative`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/HolderContinuity.html#TauCeti.PDE.exists_holderOnWith_preciseRepresentative).

## Other forms

**De Giorgi's theorem with a drift: Hölder continuity of weak solutions.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_preciseRepresentative_drift`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/HolderContinuity.html#TauCeti.PDE.exists_holderOnWith_preciseRepresentative_drift).

```lean
TauCeti.PDE.exists_holderOnWith_preciseRepresentative_drift.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {lam Lam : ℝ} (σ : ℝ) :
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

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_holderOnWith_preciseRepresentative`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/HolderContinuity.html#TauCeti.PDE.exists_holderOnWith_preciseRepresentative)
- [Source of `TauCeti.PDE.exists_holderOnWith_preciseRepresentative` in TauCeti/Analysis/PDE/Regularity/HolderContinuity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Regularity/HolderContinuity.lean#L159)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PDE/STATUS.md)
