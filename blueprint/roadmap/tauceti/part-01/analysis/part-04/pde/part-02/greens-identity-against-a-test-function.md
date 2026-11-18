---
declaration: theorem
origin: cited
lean: TauCeti.PDE.energyFormH1_one_zero_zero_ofTestFunctionₗ_eq_neg_integral_laplacian_smul
statement: formalized
proof: formalized
---

# Green's identity against a test function

Let `u ∈ H¹(Ω)` agree almost everywhere on `Ω`
with a function `w`. For a test function `φ` on `Ω`, the energy form of `-Δ` is
`∫_Ω ∇φ · ∇u = -∫ Δφ w`. No boundary condition is imposed on `u`.

```lean
TauCeti.PDE.energyFormH1_one_zero_zero_ofTestFunctionₗ_eq_neg_integral_laplacian_smul.{u_1}
  {ι : Type u_1} [Fintype ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {w : EuclideanSpace ℝ ι → ℝ} [DecidableEq ι]
  {u : ↥(TauCeti.W1p mu Omega 2)} (hu : ↑↑(TauCeti.W1p.value u) =ᵐ[mu.restrict ↑Omega] w)
  (φ : TestFunction Omega ℝ ⊤) :
  TauCeti.PDE.energyFormH1 (fun x => 1) 0 0 u ((TauCeti.W1p.ofTestFunctionₗ mu Omega 2) φ) =
    -∫ (x : EuclideanSpace ℝ ι), Laplacian.laplacian (⇑φ) x • w x ∂mu
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.energyFormH1_one_zero_zero_ofTestFunctionₗ_eq_neg_integral_laplacian_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/WeakLaplacian.html#TauCeti.PDE.energyFormH1_one_zero_zero_ofTestFunction%E2%82%97_eq_neg_integral_laplacian_smul).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.energyFormH1_one_zero_zero_ofTestFunctionₗ_eq_neg_integral_laplacian_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/WeakLaplacian.html#TauCeti.PDE.energyFormH1_one_zero_zero_ofTestFunction%E2%82%97_eq_neg_integral_laplacian_smul)
- [Source of `TauCeti.PDE.energyFormH1_one_zero_zero_ofTestFunctionₗ_eq_neg_integral_laplacian_smul` in TauCeti/Analysis/PDE/WeakLaplacian.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/WeakLaplacian.lean#L54)
