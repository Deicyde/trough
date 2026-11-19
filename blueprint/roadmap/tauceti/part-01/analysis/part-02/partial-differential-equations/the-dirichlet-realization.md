---
declaration: def
origin: cited
lean: TauCeti.PDE.dirichletOperator
statement: formalized
---

# The Dirichlet realization

**The Dirichlet realization** of `L u = -∂ᵢ(aⁱʲ ∂ⱼu) + bⁱ ∂ᵢu + c u` on `L²(Ω)`, for an energy
form that is coercive on `H¹₀(Ω)`. It is the inverse of the solution operator
`S = TauCeti.PDE.dirichletSolutionOperator`, which is injective. Its domain consists of the
values of the `u ∈ H¹₀(Ω)` with `L u ∈ L²(Ω)` weakly, and it sends such a `u` to `L u`: `(u, f)`
lies on its graph exactly when `a(u, v) = ∫_Ω f v` for every `v ∈ H¹₀(Ω)`
(`TauCeti.PDE.mem_graph_dirichletOperator_iff`).

```lean
TauCeti.PDE.dirichletOperator.{u_1} {ι : Type u_1} [Fintype ι]
  {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {c : EuclideanSpace ℝ ι → ℝ}
  (hcoeff :
    MeasureTheory.MemLp (fun x => TauCeti.PDE.energyIntegrand (a x) (b x) (c x)) ⊤
      (mu.restrict ↑Omega))
  (hcoercive : IsCoercive (TauCeti.PDE.energyFormH1L0 hcoeff)) :
  ↥(MeasureTheory.Lp ℝ 2 (mu.restrict ↑Omega)) →ₗ.[ℝ] ↥(MeasureTheory.Lp ℝ 2 (mu.restrict ↑Omega))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.dirichletOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Spectrum/Operator.html#TauCeti.PDE.dirichletOperator).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.dirichletOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Spectrum/Operator.html#TauCeti.PDE.dirichletOperator)
- [Source of `TauCeti.PDE.dirichletOperator` in TauCeti/Analysis/PDE/Spectrum/Operator.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Spectrum/Operator.lean#L102)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PDE/STATUS.md)
