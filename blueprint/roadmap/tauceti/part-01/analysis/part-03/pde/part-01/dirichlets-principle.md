---
declaration: theorem
origin: cited
lean: TauCeti.PDE.energyFormH1_self_div_two_le_of_forall_energyFormH1_eq
statement: formalized
proof: formalized
---

# Dirichlet's principle

Let the energy form be symmetric on `H¹(Ω)` and nonnegative on
`H¹₀(Ω)`, and let `u` solve `a(u, v) = ℓ v` for every `v ∈ H¹₀(Ω)`. Then for every
`w ∈ H¹₀(Ω)`,

`a(u, u) / 2 ≤ a(u + w, u + w) / 2 - ℓ w`.

If `u - g ∈ H¹₀(Ω)`, the functions `u + w` run over the affine space `g + H¹₀(Ω)` and
`ℓ ((u + w) - g) = ℓ (u - g) + ℓ w`, so this says that `u` minimizes the Dirichlet energy
`J(v) = a(v, v) / 2 - ℓ (v - g)` over `g + H¹₀(Ω)`. With no drift and an almost everywhere
symmetric principal coefficient the symmetry hypothesis is
`TauCeti.PDE.energyFormH1_comm_of_isSymm_ae`, and coercivity gives the nonnegativity.

```lean
TauCeti.PDE.energyFormH1_self_div_two_le_of_forall_energyFormH1_eq.{u_1} {ι : Type u_1} [Fintype ι]
  {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {c : EuclideanSpace ℝ ι → ℝ}
  (hcoeff :
    MeasureTheory.MemLp (fun x => TauCeti.PDE.energyIntegrand (a x) (b x) (c x)) ⊤
      (mu.restrict ↑Omega))
  (hsymm :
    ∀ (v w : ↥(TauCeti.W1p mu Omega 2)),
      TauCeti.PDE.energyFormH1 a b c v w = TauCeti.PDE.energyFormH1 a b c w v)
  (hnonneg : ∀ (w : ↥(TauCeti.W1p0 mu Omega 2)), 0 ≤ TauCeti.PDE.energyFormH1 a b c ↑w ↑w)
  {ℓ : StrongDual ℝ ↥(TauCeti.W1p0 mu Omega 2)} {u : ↥(TauCeti.W1p mu Omega 2)}
  (hu : ∀ (v : ↥(TauCeti.W1p0 mu Omega 2)), TauCeti.PDE.energyFormH1 a b c u ↑v = ℓ v)
  (w : ↥(TauCeti.W1p0 mu Omega 2)) :
  TauCeti.PDE.energyFormH1 a b c u u / 2 ≤
    TauCeti.PDE.energyFormH1 a b c (u + ↑w) (u + ↑w) / 2 - ℓ w
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.energyFormH1_self_div_two_le_of_forall_energyFormH1_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/DirichletProblem.html#TauCeti.PDE.energyFormH1_self_div_two_le_of_forall_energyFormH1_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.energyFormH1_self_div_two_le_of_forall_energyFormH1_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/DirichletProblem.html#TauCeti.PDE.energyFormH1_self_div_two_le_of_forall_energyFormH1_eq)
- [Source of `TauCeti.PDE.energyFormH1_self_div_two_le_of_forall_energyFormH1_eq` in TauCeti/Analysis/PDE/DirichletProblem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/DirichletProblem.lean#L455)
