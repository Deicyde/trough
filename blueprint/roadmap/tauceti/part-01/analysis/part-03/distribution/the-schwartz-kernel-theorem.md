---
declaration: theorem
origin: cited
lean: LinearMap.existsUnique_kernelOperator_eq, ContinuousLinearMap.existsUnique_kernelOperator_eq, LinearMap.existsUnique_schwartzKernel_distribution, LinearMap.exists_schwartzKernel_supportedIn, LinearMap.existsUnique_schwartzKernel_testFunction, LinearMap.existsUnique_schwartzKernel_prodSMulCLM
statement: formalized
proof: formalized
---

# The Schwartz kernel theorem

Let `Ω ⊆ ℝ^a` and `O ⊆ ℝ^b` be open sets and let
`A : 𝓓(O, ℝ) → 𝓓'(Ω, ℂ)` be a linear map which is continuous for the weak topology of
distributions: `ψ ↦ ⟨A ψ, φ⟩` is continuous for every test function `φ` on `Ω`. Then there is a
unique distribution `K` on `V = Ω × O`, the Schwartz kernel of `A`, with `⟨A ψ, φ⟩ = K (φ ⊗ ψ)`,
that is, `A = kernelOperator hV K`.

```lean
LinearMap.existsUnique_kernelOperator_eq.{u_1, u_2} {a : Type u_1} {b : Type u_2} [Fintype a]
  [Fintype b] {Ω : TopologicalSpace.Opens (a → ℝ)} {O : TopologicalSpace.Opens (b → ℝ)}
  {V : TopologicalSpace.Opens ((a → ℝ) × (b → ℝ))} (A : TestFunction O ℝ ⊤ →ₗ[ℝ] Distribution Ω ℂ ⊤)
  (hA : ∀ (φ : TestFunction Ω ℝ ⊤), Continuous fun ψ => (A ψ) φ) (hV : ↑V = ↑Ω ×ˢ ↑O) :
  ∃! K, (Distribution.kernelOperator ⋯) K = A
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The kernel theorem](../fourier/part-01/the-kernel-theorem.md)
- [TauCeti.Complexification](../../part-02/one-parameter-semigroups-completely-monotone-and/tauceti-complexification.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.existsUnique_kernelOperator_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/SchwartzKernel.html#LinearMap.existsUnique_kernelOperator_eq).

## Other forms

**The Schwartz kernel theorem for continuous operators.** Formalized in Tau Ceti as [`ContinuousLinearMap.existsUnique_kernelOperator_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/SchwartzKernel.html#ContinuousLinearMap.existsUnique_kernelOperator_eq).

```lean
ContinuousLinearMap.existsUnique_kernelOperator_eq.{u_1, u_2} {a : Type u_1} {b : Type u_2}
  [Fintype a] [Fintype b] {Ω : TopologicalSpace.Opens (a → ℝ)} {O : TopologicalSpace.Opens (b → ℝ)}
  {V : TopologicalSpace.Opens ((a → ℝ) × (b → ℝ))} (A : TestFunction O ℝ ⊤ →L[ℝ] Distribution Ω ℂ ⊤)
  (hV : ↑V = ↑Ω ×ˢ ↑O) : ∃! K, (Distribution.kernelOperator ⋯) K = ↑A
```

**The Schwartz kernel theorem for distributions on open sets.** Formalized in Tau Ceti as [`LinearMap.existsUnique_schwartzKernel_distribution`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/SchwartzKernel.html#LinearMap.existsUnique_schwartzKernel_distribution).

```lean
LinearMap.existsUnique_schwartzKernel_distribution.{u_1, u_2} {a : Type u_1} {b : Type u_2}
  [Fintype a] [Fintype b] {Ω : TopologicalSpace.Opens (a → ℝ)} {O : TopologicalSpace.Opens (b → ℝ)}
  (B : TestFunction Ω ℂ ⊤ →ₗ[ℂ] TestFunction O ℂ ⊤ →ₗ[ℂ] ℂ)
  (hB :
    ∀ (K₁ : TopologicalSpace.Compacts (a → ℝ)) (K₂ : TopologicalSpace.Compacts (b → ℝ))
      (hK₁ : ↑K₁ ⊆ ↑Ω) (hK₂ : ↑K₂ ⊆ ↑O),
      ∃ C k,
        ∀ (φ : ContDiffMapSupportedIn (a → ℝ) ℂ ⊤ K₁) (ψ : ContDiffMapSupportedIn (b → ℝ) ℂ ⊤ K₂),
          ‖(B (TestFunction.ofSupportedIn hK₁ φ)) (TestFunction.ofSupportedIn hK₂ ψ)‖ ≤
            C * (ContDiffMapSupportedIn.supSeminorm ℂ (a → ℝ) ℂ ⊤ K₁ k) φ *
              (ContDiffMapSupportedIn.supSeminorm ℂ (b → ℝ) ℂ ⊤ K₂ k) ψ)
  {V : TopologicalSpace.Opens ((a → ℝ) × (b → ℝ))} (hV : ↑V = ↑Ω ×ˢ ↑O) :
  ∃! K,
    ∀ (φ : TestFunction Ω ℂ ⊤) (ψ : TestFunction O ℂ ⊤), K.complexPairing (φ.tensor ψ ⋯) = (B φ) ψ
```

**The Schwartz kernel theorem for test functions supported in compact sets.** Formalized in Tau Ceti as [`LinearMap.exists_schwartzKernel_supportedIn`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/SchwartzKernel.html#LinearMap.exists_schwartzKernel_supportedIn).

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

**The Schwartz kernel theorem on open sets.** Formalized in Tau Ceti as [`LinearMap.existsUnique_schwartzKernel_testFunction`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/SchwartzKernel.html#LinearMap.existsUnique_schwartzKernel_testFunction).

```lean
LinearMap.existsUnique_schwartzKernel_testFunction.{u_1, u_2, u_3} {a : Type u_1} {b : Type u_2}
  [Fintype a] [Fintype b] {F : Type u_3} [NormedAddCommGroup F] [NormedSpace ℂ F] [CompleteSpace F]
  {Ω : TopologicalSpace.Opens (a → ℝ)} {O : TopologicalSpace.Opens (b → ℝ)}
  (B : TestFunction Ω ℂ ⊤ →ₗ[ℂ] TestFunction O ℂ ⊤ →ₗ[ℂ] F)
  (hB :
    ∀ (K₁ : TopologicalSpace.Compacts (a → ℝ)) (K₂ : TopologicalSpace.Compacts (b → ℝ))
      (hK₁ : ↑K₁ ⊆ ↑Ω) (hK₂ : ↑K₂ ⊆ ↑O),
      ∃ C k,
        ∀ (φ : ContDiffMapSupportedIn (a → ℝ) ℂ ⊤ K₁) (ψ : ContDiffMapSupportedIn (b → ℝ) ℂ ⊤ K₂),
          ‖(B (TestFunction.ofSupportedIn hK₁ φ)) (TestFunction.ofSupportedIn hK₂ ψ)‖ ≤
            C * (ContDiffMapSupportedIn.supSeminorm ℂ (a → ℝ) ℂ ⊤ K₁ k) φ *
              (ContDiffMapSupportedIn.supSeminorm ℂ (b → ℝ) ℂ ⊤ K₂ k) ψ)
  {V : TopologicalSpace.Opens ((a → ℝ) × (b → ℝ))} (hV : ↑V = ↑Ω ×ˢ ↑O) :
  ∃! T, ∀ (φ : TestFunction Ω ℂ ⊤) (ψ : TestFunction O ℂ ⊤), T (φ.tensor ψ ⋯) = (B φ) ψ
```

**The Schwartz kernel theorem on open sets, for real test functions.** Formalized in Tau Ceti as [`LinearMap.existsUnique_schwartzKernel_prodSMulCLM`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/SchwartzKernel.html#LinearMap.existsUnique_schwartzKernel_prodSMulCLM).

```lean
LinearMap.existsUnique_schwartzKernel_prodSMulCLM.{u_1, u_2, u_4} {a : Type u_1} {b : Type u_2}
  [Fintype a] [Fintype b] {Ω : TopologicalSpace.Opens (a → ℝ)} {O : TopologicalSpace.Opens (b → ℝ)}
  {G : Type u_4} [NormedAddCommGroup G] [NormedSpace ℝ G] [CompleteSpace G]
  (B : TestFunction Ω ℝ ⊤ →ₗ[ℝ] TestFunction O ℝ ⊤ →ₗ[ℝ] G)
  (hB :
    ∀ (K₁ : TopologicalSpace.Compacts (a → ℝ)) (K₂ : TopologicalSpace.Compacts (b → ℝ))
      (hK₁ : ↑K₁ ⊆ ↑Ω) (hK₂ : ↑K₂ ⊆ ↑O),
      ∃ C k,
        ∀ (φ : ContDiffMapSupportedIn (a → ℝ) ℝ ⊤ K₁) (ψ : ContDiffMapSupportedIn (b → ℝ) ℝ ⊤ K₂),
          ‖(B (TestFunction.ofSupportedIn hK₁ φ)) (TestFunction.ofSupportedIn hK₂ ψ)‖ ≤
            C * (ContDiffMapSupportedIn.supSeminorm ℝ (a → ℝ) ℝ ⊤ K₁ k) φ *
              (ContDiffMapSupportedIn.supSeminorm ℝ (b → ℝ) ℝ ⊤ K₂ k) ψ)
  {V : TopologicalSpace.Opens ((a → ℝ) × (b → ℝ))} (hV : ↑V = ↑Ω ×ˢ ↑O) :
  ∃! T, ∀ (φ : TestFunction Ω ℝ ⊤) (ψ : TestFunction O ℝ ⊤), T ((ψ.prodSMulCLM ⋯) φ) = (B φ) ψ
```

## Sources

- [Tau Ceti documentation: `LinearMap.existsUnique_kernelOperator_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/SchwartzKernel.html#LinearMap.existsUnique_kernelOperator_eq)
- [Source of `LinearMap.existsUnique_kernelOperator_eq` in TauCeti/Analysis/Distribution/SchwartzKernel.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Distribution/SchwartzKernel.lean#L581)
