---
declaration: theorem
origin: cited
lean: TauCeti.PDE.dirichletEigenvalue_eq_of_hilbertBasis
statement: formalized
proof: formalized
---

# The Courant–Fischer min–max principle for the Dirichlet eigenvalues

Let the energy form
`a` be symmetric and nonnegative on `H¹₀(Ω)`, and let `κ₀ ≤ κ₁ ≤ ⋯` be eigenvalues with
eigenfunctions `uⱼ ∈ H¹₀(Ω)`, `a(uⱼ, v) = κⱼ ⟪uⱼ, v⟫_{L²}` for every `v ∈ H¹₀(Ω)`, whose values
form an orthonormal basis of `L²(Ω)`. Then `κₖ` is the `k`-th Dirichlet eigenvalue `λₖ(Ω)`. In
particular any two such listings agree.

```lean
TauCeti.PDE.dirichletEigenvalue_eq_of_hilbertBasis.{u_1} {ι : Type u_1} [Fintype ι]
  {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {c : EuclideanSpace ℝ ι → ℝ}
  (hcoeff :
    MeasureTheory.MemLp (fun x => TauCeti.PDE.energyIntegrand (a x) (b x) (c x)) ⊤
      (mu.restrict ↑Omega))
  (hsymm :
    ∀ (u v : ↥(TauCeti.W1p0 mu Omega 2)),
      TauCeti.PDE.energyFormH1 a b c ↑u ↑v = TauCeti.PDE.energyFormH1 a b c ↑v ↑u)
  (hnonneg : ∀ (v : ↥(TauCeti.W1p0 mu Omega 2)), 0 ≤ TauCeti.PDE.energyFormH1 a b c ↑v ↑v)
  (basis : HilbertBasis ℕ ℝ ↥(MeasureTheory.Lp ℝ 2 (mu.restrict ↑Omega))) {kappa : ℕ → ℝ}
  (hkappa : Monotone kappa) {u : ℕ → ↥(TauCeti.W1p0 mu Omega 2)}
  (hvalue : ∀ (j : ℕ), TauCeti.W1p.value ↑(u j) = basis j)
  (heq :
    ∀ (j : ℕ) (v : ↥(TauCeti.W1p0 mu Omega 2)),
      TauCeti.PDE.energyFormH1 a b c ↑(u j) ↑v =
        kappa j * inner ℝ (TauCeti.W1p.value ↑(u j)) (TauCeti.W1p.value ↑v))
  (k : ℕ) : TauCeti.PDE.dirichletEigenvalue mu Omega a b c k = kappa k
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Courant–Fischer min–max principle](../../../part-03/inner-product-space/part-01/the-courant-fischer-min-max-principle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.dirichletEigenvalue_eq_of_hilbertBasis`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Spectrum/MinMax.html#TauCeti.PDE.dirichletEigenvalue_eq_of_hilbertBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.dirichletEigenvalue_eq_of_hilbertBasis`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Spectrum/MinMax.html#TauCeti.PDE.dirichletEigenvalue_eq_of_hilbertBasis)
- [Source of `TauCeti.PDE.dirichletEigenvalue_eq_of_hilbertBasis` in TauCeti/Analysis/PDE/Spectrum/MinMax.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Spectrum/MinMax.lean#L146)
