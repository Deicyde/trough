---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_holderOnWith_preciseRepresentative
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

- [TauCeti.Wkp](tauceti-wkp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_preciseRepresentative`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/HolderContinuity.html#TauCeti.PDE.exists_holderOnWith_preciseRepresentative).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_holderOnWith_preciseRepresentative`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/HolderContinuity.html#TauCeti.PDE.exists_holderOnWith_preciseRepresentative)
- [Source of `TauCeti.PDE.exists_holderOnWith_preciseRepresentative` in TauCeti/Analysis/PDE/Regularity/HolderContinuity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Regularity/HolderContinuity.lean#L172)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PDE/STATUS.md)
