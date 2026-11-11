---
declaration: theorem
origin: cited
lean: TauCeti.PDE.energyFormH1_one_zero_zero_eq_setIntegral_neg_laplacian_mul
statement: formalized
proof: formalized
---

# Green's first identity against `H¹₀(Ω)`

Let `u ∈ H¹(Ω)` agree almost everywhere on `Ω`
with a function `w` of class `C²` on `Ω` whose Laplacian lies in `L²(Ω)`. Then
`∫_Ω ∇v · ∇u = -∫_Ω Δw v` for every `v ∈ H¹₀(Ω)`: `u` solves `-Δu = -Δw` weakly. No boundary
condition is imposed on `u`.

```lean
TauCeti.PDE.energyFormH1_one_zero_zero_eq_setIntegral_neg_laplacian_mul.{u_1} {ι : Type u_1}
  [Fintype ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {w : EuclideanSpace ℝ ι → ℝ} [DecidableEq ι]
  {u : ↥(TauCeti.W1p mu Omega 2)} (hw : ContDiffOn ℝ 2 w ↑Omega)
  (hu : ↑↑(TauCeti.W1p.value u) =ᵐ[mu.restrict ↑Omega] w)
  (hΔ : MeasureTheory.MemLp (Laplacian.laplacian w) 2 (mu.restrict ↑Omega))
  (v : ↥(TauCeti.W1p0 mu Omega 2)) :
  TauCeti.PDE.energyFormH1 (fun x => 1) 0 0 u ↑v =
    ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, -Laplacian.laplacian w x * ↑↑(TauCeti.W1p.value ↑v) x ∂mu
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Green's second identity against a test function](../../sobolev/part-01/greens-second-identity-against-a-test-function.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.energyFormH1_one_zero_zero_eq_setIntegral_neg_laplacian_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/ClassicalSolution.html#TauCeti.PDE.energyFormH1_one_zero_zero_eq_setIntegral_neg_laplacian_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.energyFormH1_one_zero_zero_eq_setIntegral_neg_laplacian_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/ClassicalSolution.html#TauCeti.PDE.energyFormH1_one_zero_zero_eq_setIntegral_neg_laplacian_mul)
- [Source of `TauCeti.PDE.energyFormH1_one_zero_zero_eq_setIntegral_neg_laplacian_mul` in TauCeti/Analysis/PDE/ClassicalSolution.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/ClassicalSolution.lean#L74)
