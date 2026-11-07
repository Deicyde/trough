---
declaration: theorem
origin: cited
lean: TauCeti.PDE.UniformlyEllipticOn.existsUnique_isWeakSolutionDirichlet_of_mass_nonneg
statement: formalized
proof: formalized
---

# Existence and uniqueness for the Dirichlet problem with `c ≥ 0`

Let `Ω ⊆ ℝⁿ`, `n ≥ 1`,
be a bounded open set, and let `L u = -∂ᵢ(aⁱʲ ∂ⱼu) + bⁱ ∂ᵢu + c u` have measurable, uniformly
elliptic `a`, measurable `b` with `‖b‖ ≤ β` and measurable `c` with `0 ≤ c ≤ γ`. Then for every
`f ∈ L²(Ω)` there is exactly one `u ∈ H¹₀(Ω)` with `a(u, v) = ∫_Ω f v` for all `v ∈ H¹₀(Ω)`.
Since `β` is arbitrary, the energy form of `L` need not be coercive.

```lean
TauCeti.PDE.UniformlyEllipticOn.existsUnique_isWeakSolutionDirichlet_of_mass_nonneg.{u_1}
  {ι : Type u_1} [Fintype ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {c : EuclideanSpace ℝ ι → ℝ}
  {lam Lam beta gamma : ℝ} [DecidableEq ι] [Nonempty ι]
  (h : TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega))
  (hb : MeasureTheory.AEStronglyMeasurable b (mu.restrict ↑Omega))
  (hc : MeasureTheory.AEStronglyMeasurable c (mu.restrict ↑Omega))
  (hb_bound : ∀ x ∈ Omega, ‖b x‖ ≤ beta) (hc_bound : ∀ x ∈ Omega, ‖c x‖ ≤ gamma)
  (hc_nonneg : ∀ x ∈ Omega, 0 ≤ c x) (hOmega : Bornology.IsBounded ↑Omega)
  (f : ↥(MeasureTheory.Lp ℝ 2 (mu.restrict ↑Omega))) :
  ∃! u, TauCeti.PDE.IsWeakSolutionDirichlet a b c f u
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.Wkp](tauceti-wkp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.UniformlyEllipticOn.existsUnique_isWeakSolutionDirichlet_of_mass_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/Drift.html#TauCeti.PDE.UniformlyEllipticOn.existsUnique_isWeakSolutionDirichlet_of_mass_nonneg).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.UniformlyEllipticOn.existsUnique_isWeakSolutionDirichlet_of_mass_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/Drift.html#TauCeti.PDE.UniformlyEllipticOn.existsUnique_isWeakSolutionDirichlet_of_mass_nonneg)
- [Source of `TauCeti.PDE.UniformlyEllipticOn.existsUnique_isWeakSolutionDirichlet_of_mass_nonneg` in TauCeti/Analysis/PDE/MaximumPrinciple/Drift.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/MaximumPrinciple/Drift.lean#L441)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PDE/STATUS.md)
