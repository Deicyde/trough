---
declaration: theorem
origin: cited
lean: LinearMap.IsSymmetric.le_sum_sq_eigenvalues_sub
statement: formalized
proof: formalized
---

# Davis's eigenvalue-change lower bound

Let `T` and `S` be symmetric, let `(vᵢ)` be the
eigenbasis of `T`, and suppose the eigenvalues `μᵢ` of `S` are pairwise at distance at least
`γ ≥ 0`. If the diagonal entries `hᵢ = Re⟪vᵢ, (S - T) vᵢ⟫` of the perturbation satisfy
`∑ᵢ hᵢ² ≤ (γ / √2)²`, then the sorted spectra satisfy

`∑ᵢ hᵢ² - (∑ᵢ μᵢ² - ∑ᵢ Re⟪vᵢ, S vᵢ⟫²) ≤ ∑ᵢ (μᵢ - λᵢ)²`,

where `λᵢ` are the eigenvalues of `T`. Here `∑ᵢ μᵢ² - ∑ᵢ Re⟪vᵢ, S vᵢ⟫²` is the squared Frobenius
norm of the off-diagonal part of `S - T` in the basis `(vᵢ)`.

```lean
LinearMap.IsSymmetric.le_sum_sq_eigenvalues_sub.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E] {T S : E →ₗ[𝕜] E} {n : ℕ}
  (hT : T.IsSymmetric) (hS : S.IsSymmetric) (hn : Module.finrank 𝕜 E = n) {γ : ℝ} (hγ : 0 ≤ γ)
  (hsep : Pairwise fun i j => γ ≤ |hS.eigenvalues hn i - hS.eigenvalues hn j|)
  (hH :
    ∑ i,
        RCLike.re (inner 𝕜 ((hT.eigenvectorBasis hn) i) ((S - T) ((hT.eigenvectorBasis hn) i))) ^
          2 ≤
      (γ / √2) ^ 2) :
  ∑ i, RCLike.re (inner 𝕜 ((hT.eigenvectorBasis hn) i) ((S - T) ((hT.eigenvectorBasis hn) i))) ^ 2 -
      (∑ i, hS.eigenvalues hn i ^ 2 -
        ∑ i,
          RCLike.re (inner 𝕜 ((hT.eigenvectorBasis hn) i) (S ((hT.eigenvectorBasis hn) i))) ^ 2) ≤
    ∑ i, (hS.eigenvalues hn i - hT.eigenvalues hn i) ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.IsSymmetric.le_sum_sq_eigenvalues_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/DavisEigenvalueChange.html#LinearMap.IsSymmetric.le_sum_sq_eigenvalues_sub).

## Sources

- [Tau Ceti documentation: `LinearMap.IsSymmetric.le_sum_sq_eigenvalues_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/DavisEigenvalueChange.html#LinearMap.IsSymmetric.le_sum_sq_eigenvalues_sub)
- [Source of `LinearMap.IsSymmetric.le_sum_sq_eigenvalues_sub` in TauCeti/Analysis/InnerProductSpace/DavisEigenvalueChange.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/DavisEigenvalueChange.lean#L57)
