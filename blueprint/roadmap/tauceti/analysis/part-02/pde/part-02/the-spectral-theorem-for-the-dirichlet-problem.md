---
declaration: theorem
origin: cited
lean: TauCeti.PDE.orthogonalComplement_iSup_eigenspaces_dirichletSolutionOperator_eq_bot
statement: formalized
proof: formalized
---

# The spectral theorem for the Dirichlet problem

on a bounded domain and for a symmetric
energy form, the eigenvectors of the solution operator span a dense subspace of `L²(Ω)`.

```lean
TauCeti.PDE.orthogonalComplement_iSup_eigenspaces_dirichletSolutionOperator_eq_bot.{u_1}
  {ι : Type u_1} [Fintype ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {c : EuclideanSpace ℝ ι → ℝ}
  (hcoeff :
    MeasureTheory.MemLp (fun x => TauCeti.PDE.energyIntegrand (a x) (b x) (c x)) ⊤
      (mu.restrict ↑Omega))
  (hcoercive : IsCoercive (TauCeti.PDE.energyFormH1L0 hcoeff)) (hOmega : Bornology.IsBounded ↑Omega)
  (hsymm :
    ∀ (u v : ↥(TauCeti.W1p0 mu Omega 2)),
      TauCeti.PDE.energyFormH1 a b c ↑u ↑v = TauCeti.PDE.energyFormH1 a b c ↑v ↑u) :
  (⨆ nu, Module.End.eigenspace (↑(TauCeti.PDE.dirichletSolutionOperator hcoeff hcoercive)) nu)ᗮ = ⊥
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Fréchet--Kolmogorov criterion for a family vanishing almost everywhere off a fixed bounded set, the form that Rellich--Kondrachov for `W^{1,p}_0(Ω)` consumes](../../../../measure-theory/function/the-frechet-kolmogorov-criterion-for-a-family-va.md)
- [Hölder's inequality for Young's exponents](../../../../measure-theory/euclidean-isoperimetry-sharp-inequalities-and-ri/part-02/holders-inequality-for-youngs-exponents.md)
- [The spectral theorem for the solution operator](../../inner-product-space/part-02/the-spectral-theorem-for-the-solution-operator.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.orthogonalComplement_iSup_eigenspaces_dirichletSolutionOperator_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Spectrum/Basic.html#TauCeti.PDE.orthogonalComplement_iSup_eigenspaces_dirichletSolutionOperator_eq_bot).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.orthogonalComplement_iSup_eigenspaces_dirichletSolutionOperator_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Spectrum/Basic.html#TauCeti.PDE.orthogonalComplement_iSup_eigenspaces_dirichletSolutionOperator_eq_bot)
- [Source of `TauCeti.PDE.orthogonalComplement_iSup_eigenspaces_dirichletSolutionOperator_eq_bot` in TauCeti/Analysis/PDE/Spectrum/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Spectrum/Basic.lean#L519)
