---
declaration: theorem
origin: cited
lean: LinearMap.existsUnique_schwartzKernel
statement: formalized
proof: formalized
---

# The Schwartz kernel theorem on the torus

A bilinear map on smooth functions on two tori
which is continuous for the `C^N` norms has a unique kernel: a linear map on smooth functions on
the product torus, continuous for some `C^N'` norm, which agrees with it on tensor products.

```lean
LinearMap.existsUnique_schwartzKernel.{u_1, u_2, u_3} {a : Type u_1} {b : Type u_2} [Fintype a]
  [Fintype b] {F : Type u_3} [NormedAddCommGroup F] [NormedSpace ℂ F] [CompleteSpace F]
  (B :
    ↥(TauCeti.UnitAddTorus.smoothFunctions a) →ₗ[ℂ]
      ↥(TauCeti.UnitAddTorus.smoothFunctions b) →ₗ[ℂ] F)
  (hB :
    ∃ C N,
      ∀ (f : ↥(TauCeti.UnitAddTorus.smoothFunctions a))
        (g : ↥(TauCeti.UnitAddTorus.smoothFunctions b)) (M₁ M₂ : ℝ),
        TauCeti.UnitAddTorus.DerivBound N M₁ ↑f →
          TauCeti.UnitAddTorus.DerivBound N M₂ ↑g → ‖(B f) g‖ ≤ C * M₁ * M₂) :
  ∃! K,
    (∃ C N,
        ∀ (h : ↥(TauCeti.UnitAddTorus.smoothFunctions (a ⊕ b))) (M : ℝ),
          TauCeti.UnitAddTorus.DerivBound N M ↑h → ‖K h‖ ≤ C * M) ∧
      ∀ (f : ↥(TauCeti.UnitAddTorus.smoothFunctions a))
        (g : ↥(TauCeti.UnitAddTorus.smoothFunctions b)), K ⟨UnitAddTorus.tensor ↑f ↑g, ⋯⟩ = (B f) g
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The kernel theorem](the-kernel-theorem.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.existsUnique_schwartzKernel`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Torus/Kernel.html#LinearMap.existsUnique_schwartzKernel).

## Sources

- [Tau Ceti documentation: `LinearMap.existsUnique_schwartzKernel`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Torus/Kernel.html#LinearMap.existsUnique_schwartzKernel)
- [Source of `LinearMap.existsUnique_schwartzKernel` in TauCeti/Analysis/Fourier/Torus/Kernel.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Fourier/Torus/Kernel.lean#L343)
