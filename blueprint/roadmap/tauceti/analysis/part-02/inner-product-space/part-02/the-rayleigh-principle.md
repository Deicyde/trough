---
declaration: theorem
origin: cited
lean: IsCoercive.isLeast_rayleighQuotient, TauCeti.PDE.isLeast_rayleighQuotient_firstDirichletEigenvalue
statement: formalized
proof: formalized
---

# The Rayleigh principle

the least variational eigenvalue `‖S‖⁻¹` is the *minimum* of the
Rayleigh quotient `B v v / ‖J v‖²` over the vectors with `J v ≠ 0`.  The minimum is attained at
an eigenfunction, which is why compactness of `J` is assumed.

```lean
IsCoercive.isLeast_rayleighQuotient.{u_3, u_4} {V : Type u_3} {H : Type u_4} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [CompleteSpace V] [NormedAddCommGroup H] [InnerProductSpace ℝ H]
  {B : V →L[ℝ] V →L[ℝ] ℝ} (hB : IsCoercive B) {J : V →L[ℝ] H} (hJ : IsCompactOperator ⇑J)
  (hsymm : ∀ (u v : V), (B u) v = (B v) u) (hJne : J ≠ 0) :
  IsLeast {r | ∃ v, J v ≠ 0 ∧ (B v) v / ‖J v‖ ^ 2 = r} ‖hB.formSolutionOperator J‖⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Fréchet--Kolmogorov criterion for a family vanishing almost everywhere off a fixed bounded set, the form that Rellich--Kondrachov for `W^{1,p}_0(Ω)` consumes](../../../../measure-theory/function/the-frechet-kolmogorov-criterion-for-a-family-va.md)
- [Hölder's inequality for Young's exponents](../../../../measure-theory/euclidean-isoperimetry-sharp-inequalities-and-ri/part-02/holders-inequality-for-youngs-exponents.md)
- [The Rayleigh lower bound](the-rayleigh-lower-bound.md)

## Lean

Formalized in Tau Ceti as [`IsCoercive.isLeast_rayleighQuotient`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Variational/Rayleigh.html#IsCoercive.isLeast_rayleighQuotient).

## Other forms

**The Rayleigh principle for the Dirichlet problem.** Formalized in Tau Ceti as [`TauCeti.PDE.isLeast_rayleighQuotient_firstDirichletEigenvalue`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Spectrum/Basic.html#TauCeti.PDE.isLeast_rayleighQuotient_firstDirichletEigenvalue).

```lean
TauCeti.PDE.isLeast_rayleighQuotient_firstDirichletEigenvalue.{u_1} {ι : Type u_1} [Fintype ι]
  {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {c : EuclideanSpace ℝ ι → ℝ}
  (hcoeff :
    MeasureTheory.MemLp (fun x => TauCeti.PDE.energyIntegrand (a x) (b x) (c x)) ⊤
      (mu.restrict ↑Omega))
  (hcoercive : IsCoercive (TauCeti.PDE.energyFormH1L0 hcoeff)) (hOmega : Bornology.IsBounded ↑Omega)
  (hsymm :
    ∀ (u v : ↥(TauCeti.W1p0 mu Omega 2)),
      TauCeti.PDE.energyFormH1 a b c ↑u ↑v = TauCeti.PDE.energyFormH1 a b c ↑v ↑u)
  (hOmega_nonempty : (↑Omega).Nonempty) :
  IsLeast
    {r |
      ∃ u,
        TauCeti.W1p.value ↑u ≠ 0 ∧
          TauCeti.PDE.energyFormH1 a b c ↑u ↑u / ‖TauCeti.W1p.value ↑u‖ ^ 2 = r}
    (TauCeti.PDE.firstDirichletEigenvalue hcoeff hcoercive)
```

## Sources

- [Tau Ceti documentation: `IsCoercive.isLeast_rayleighQuotient`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Variational/Rayleigh.html#IsCoercive.isLeast_rayleighQuotient)
- [Source of `IsCoercive.isLeast_rayleighQuotient` in TauCeti/Analysis/InnerProductSpace/Variational/Rayleigh.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/Variational/Rayleigh.lean#L131)
