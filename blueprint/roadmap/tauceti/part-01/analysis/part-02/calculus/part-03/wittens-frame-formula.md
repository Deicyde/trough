---
declaration: theorem
origin: cited
lean: TauCeti.euclideanWittenLaplacian_apply
statement: formalized
proof: formalized
---

# Witten's frame formula

For a function `f` and a form `φ` on `ℝ^ι` that are `C²` at `x`,
the Witten Laplacian at `x` is

`Δ_t φ = -∑ᵢ ∂ᵢ² φ + t² |df|² φ + t ∑_{i,j} Hess f(∂ᵢ, ∂ⱼ) ⁅εᵢ, ιⱼ⁆ φ`,

with `⁅εᵢ, ιⱼ⁆ = εᵢ ιⱼ - ιⱼ εᵢ` the commutator of exterior multiplication by `dx^i` and contraction
with `∂ⱼ`.

```lean
TauCeti.euclideanWittenLaplacian_apply.{u_1} {ι : Type u_1} [Fintype ι] [LinearOrder ι]
  {f : (ι → ℝ) → ℝ} {φ : (ι → ℝ) → Finset ι → ℝ} {x : ι → ℝ} (hf : ContDiffAt ℝ 2 f x)
  (hφ : ContDiffAt ℝ 2 φ x) (t : ℝ) :
  TauCeti.euclideanWittenLaplacian f t φ x =
    ∑ i,
        (-((fderiv ℝ (fderiv ℝ φ) x) (Pi.single i 1)) (Pi.single i 1) +
          (t ^ 2 * (fderiv ℝ f x) (Pi.single i 1) ^ 2) • φ x) +
      t •
        ∑ i,
          ∑ j,
            ((fderiv ℝ (fderiv ℝ f) x) (Pi.single i 1)) (Pi.single j 1) •
              ⁅(Pi.basisFun ℝ ι).exteriorCreation i, (Pi.basisFun ℝ ι).exteriorContraction j⁆ (φ x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.euclideanWittenLaplacian_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/WittenLaplacian/Basic.html#TauCeti.euclideanWittenLaplacian_apply).

## Sources

- [Tau Ceti documentation: `TauCeti.euclideanWittenLaplacian_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/WittenLaplacian/Basic.html#TauCeti.euclideanWittenLaplacian_apply)
- [Source of `TauCeti.euclideanWittenLaplacian_apply` in TauCeti/Analysis/Calculus/WittenLaplacian/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/WittenLaplacian/Basic.lean#L327)
