---
declaration: theorem
origin: cited
lean: TauCeti.PDE.existsUnique_isWeakSolutionDirichlet_sub_const_of_not_isDirichletEigenvalue, TauCeti.PDE.fredholmAlternative_isWeakSolutionDirichlet_sub_const
statement: formalized
proof: formalized
---

# The Fredholm alternative in eigenvalue language

On a bounded domain, if `κ` is not a
Dirichlet eigenvalue then `L u - κ u = f` in `Ω`, `u = 0` on `∂Ω`, has exactly one weak solution
for every `f ∈ L²(Ω)`.

```lean
TauCeti.PDE.existsUnique_isWeakSolutionDirichlet_sub_const_of_not_isDirichletEigenvalue.{u_1}
  {ι : Type u_1} [Fintype ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {c : EuclideanSpace ℝ ι → ℝ}
  (hcoeff :
    MeasureTheory.MemLp (fun x => TauCeti.PDE.energyIntegrand (a x) (b x) (c x)) ⊤
      (mu.restrict ↑Omega))
  (hcoercive : IsCoercive (TauCeti.PDE.energyFormH1L0 hcoeff)) (hOmega : Bornology.IsBounded ↑Omega)
  {kappa : ℝ} (hkappa : ¬TauCeti.PDE.IsDirichletEigenvalue mu Omega a b c kappa)
  (f : ↥(MeasureTheory.Lp ℝ 2 (mu.restrict ↑Omega))) :
  ∃! u, TauCeti.PDE.IsWeakSolutionDirichlet a b (fun x => c x - kappa) f u
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Fréchet--Kolmogorov criterion for a family vanishing almost everywhere off a fixed bounded set, the form that Rellich--Kondrachov for `W^{1,p}_0(Ω)` consumes](../../../../measure-theory/function/the-frechet-kolmogorov-criterion-for-a-family-va.md)
- [Hölder's inequality for Young's exponents](../../../../measure-theory/euclidean-isoperimetry-sharp-inequalities-and-ri/part-02/holders-inequality-for-youngs-exponents.md)
- [The variational Fredholm alternative](../../inner-product-space/part-02/the-variational-fredholm-alternative.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.existsUnique_isWeakSolutionDirichlet_sub_const_of_not_isDirichletEigenvalue`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Spectrum/Basic.html#TauCeti.PDE.existsUnique_isWeakSolutionDirichlet_sub_const_of_not_isDirichletEigenvalue).

## Other forms

**The Fredholm alternative for the mass-shifted Dirichlet problem.** Formalized in Tau Ceti as [`TauCeti.PDE.fredholmAlternative_isWeakSolutionDirichlet_sub_const`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/FredholmAlternative.html#TauCeti.PDE.fredholmAlternative_isWeakSolutionDirichlet_sub_const).

```lean
TauCeti.PDE.fredholmAlternative_isWeakSolutionDirichlet_sub_const.{u_1} {ι : Type u_1} [Fintype ι]
  {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {c : EuclideanSpace ℝ ι → ℝ}
  (hcoeff :
    MeasureTheory.MemLp (fun x => TauCeti.PDE.energyIntegrand (a x) (b x) (c x)) ⊤
      (mu.restrict ↑Omega))
  (hcoercive : IsCoercive (TauCeti.PDE.energyFormH1L0 hcoeff)) (hOmega : Bornology.IsBounded ↑Omega)
  (kappa : ℝ) :
  (∃ u, u ≠ 0 ∧ TauCeti.PDE.IsWeakSolutionDirichlet a b (fun x => c x - kappa) 0 u) ∨
    ∀ (f : ↥(MeasureTheory.Lp ℝ 2 (mu.restrict ↑Omega))),
      ∃! u, TauCeti.PDE.IsWeakSolutionDirichlet a b (fun x => c x - kappa) f u
```

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.existsUnique_isWeakSolutionDirichlet_sub_const_of_not_isDirichletEigenvalue`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Spectrum/Basic.html#TauCeti.PDE.existsUnique_isWeakSolutionDirichlet_sub_const_of_not_isDirichletEigenvalue)
- [Source of `TauCeti.PDE.existsUnique_isWeakSolutionDirichlet_sub_const_of_not_isDirichletEigenvalue` in TauCeti/Analysis/PDE/Spectrum/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Spectrum/Basic.lean#L592)
