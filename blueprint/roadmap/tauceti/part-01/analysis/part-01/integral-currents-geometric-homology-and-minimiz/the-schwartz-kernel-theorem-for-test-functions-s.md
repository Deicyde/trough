---
declaration: theorem
origin: cited
lean: LinearMap.exists_schwartzKernel_supportedIn
statement: formalized
proof: formalized
---

# The Schwartz kernel theorem for test functions supported in compact sets

Let `K₁'` and
`K₂'` be compact sets meeting none of their translates by nonzero integer vectors, and let `B` be
a bilinear map on `𝓓_{K₁'}(ℝ^a, ℂ) × 𝓓_{K₂'}(ℝ^b, ℂ)` bounded by a product of `C^k` seminorms.
For compact sets `K₁`, `K₂` in the interiors of `K₁'`, `K₂'` there is a continuous linear map `T`
on `𝓓_{K₁ × K₂}(ℝ^a × ℝ^b, ℂ)` with `T (φ ⊗ ψ) = B φ ψ`, and every continuous linear map `T'` on
`𝓓_{K₁' × K₂'}(ℝ^a × ℝ^b, ℂ)` with `T' (φ ⊗ ψ) = B φ ψ` restricts to `T`.

```lean
LinearMap.exists_schwartzKernel_supportedIn.{u_1, u_2, u_3} {a : Type u_1} {b : Type u_2}
  [Fintype a] [Fintype b] {F : Type u_3} [NormedAddCommGroup F] [NormedSpace ℂ F] [CompleteSpace F]
  {K₁ K₁' : TopologicalSpace.Compacts (a → ℝ)} {K₂ K₂' : TopologicalSpace.Compacts (b → ℝ)}
  (B : ContDiffMapSupportedIn (a → ℝ) ℂ ⊤ K₁' →ₗ[ℂ] ContDiffMapSupportedIn (b → ℝ) ℂ ⊤ K₂' →ₗ[ℂ] F)
  (hB :
    ∃ C k,
      ∀ (φ : ContDiffMapSupportedIn (a → ℝ) ℂ ⊤ K₁') (ψ : ContDiffMapSupportedIn (b → ℝ) ℂ ⊤ K₂'),
        ‖(B φ) ψ‖ ≤
          C * (ContDiffMapSupportedIn.supSeminorm ℂ (a → ℝ) ℂ ⊤ K₁' k) φ *
            (ContDiffMapSupportedIn.supSeminorm ℂ (b → ℝ) ℂ ⊤ K₂' k) ψ)
  (hK₁' : ∀ x ∈ K₁', ∀ (ℓ : a → ℤ), (x + fun i => ↑(ℓ i)) ∈ K₁' → ℓ = 0)
  (hK₂' : ∀ y ∈ K₂', ∀ (ℓ : b → ℤ), (y + fun i => ↑(ℓ i)) ∈ K₂' → ℓ = 0) (hK₁ : ↑K₁ ⊆ interior ↑K₁')
  (hK₂ : ↑K₂ ⊆ interior ↑K₂') :
  ∃ T,
    (∀ (φ : ContDiffMapSupportedIn (a → ℝ) ℂ ⊤ K₁) (ψ : ContDiffMapSupportedIn (b → ℝ) ℂ ⊤ K₂),
        T (φ.tensor ψ) =
          (B ((ContDiffMapSupportedIn.monoCLM ℂ) φ)) ((ContDiffMapSupportedIn.monoCLM ℂ) ψ)) ∧
      ∀ (T' : ContDiffMapSupportedIn ((a → ℝ) × (b → ℝ)) ℂ ⊤ (K₁' ×ˢ K₂') →L[ℂ] F),
        (∀ (φ : ContDiffMapSupportedIn (a → ℝ) ℂ ⊤ K₁')
            (ψ : ContDiffMapSupportedIn (b → ℝ) ℂ ⊤ K₂'), T' (φ.tensor ψ) = (B φ) ψ) →
          ∀ (Φ : ContDiffMapSupportedIn ((a → ℝ) × (b → ℝ)) ℂ ⊤ (K₁ ×ˢ K₂)),
            T' ((ContDiffMapSupportedIn.monoCLM ℂ) Φ) = T Φ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The kernel theorem](../../part-02/fourier/the-kernel-theorem.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.exists_schwartzKernel_supportedIn`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/SchwartzKernel.html#LinearMap.exists_schwartzKernel_supportedIn).

## Sources

- [Tau Ceti documentation: `LinearMap.exists_schwartzKernel_supportedIn`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/SchwartzKernel.html#LinearMap.exists_schwartzKernel_supportedIn)
- [Source of `LinearMap.exists_schwartzKernel_supportedIn` in TauCeti/Analysis/Distribution/TestFunction/SchwartzKernel.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Distribution/TestFunction/SchwartzKernel.lean#L332)
