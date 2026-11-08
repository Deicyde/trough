---
declaration: theorem
origin: cited
lean: TauCeti.PDE.isLeast_rayleighQuotient_firstDirichletEigenvalue
statement: formalized
proof: formalized
---

# The Rayleigh principle for the Dirichlet problem

On a nonempty bounded domain with a
symmetric energy form, the first Dirichlet eigenvalue is the *minimum* of the Rayleigh quotient

`a(u, u) / ‖u‖²_{L²(Ω)}`

over the `u ∈ H¹₀(Ω)` with nonzero `L²` value; the minimum is attained at an eigenfunction.
Boundedness of `Ω` enters only through the attainment, by way of Rellich--Kondrachov: the
inequality alone is `TauCeti.PDE.firstDirichletEigenvalue_mul_norm_value_sq_le`.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Rayleigh principle](../../inner-product-space/part-02/the-rayleigh-principle.md)
- [Rellich–Kondrachov on bounded Lipschitz domains](../../sobolev/part-02/rellich-kondrachov-on-bounded-lipschitz-domains.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.isLeast_rayleighQuotient_firstDirichletEigenvalue`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Spectrum/Basic.html#TauCeti.PDE.isLeast_rayleighQuotient_firstDirichletEigenvalue).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.isLeast_rayleighQuotient_firstDirichletEigenvalue`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Spectrum/Basic.html#TauCeti.PDE.isLeast_rayleighQuotient_firstDirichletEigenvalue)
- [Source of `TauCeti.PDE.isLeast_rayleighQuotient_firstDirichletEigenvalue` in TauCeti/Analysis/PDE/Spectrum/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Spectrum/Basic.lean#L450)
