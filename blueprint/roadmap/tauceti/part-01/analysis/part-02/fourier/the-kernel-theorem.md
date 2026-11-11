---
declaration: theorem
origin: cited
lean: LinearMap.schwartzKernel_tensor
statement: formalized
proof: formalized
---

# The kernel theorem

The kernel of `B` represents `B` on tensor products:
`K (f ⊗ g) = B f g`.

```lean
LinearMap.schwartzKernel_tensor.{u_1, u_2, u_3} {a : Type u_1} {b : Type u_2} [Fintype a]
  [Fintype b] {F : Type u_3} [NormedAddCommGroup F] [NormedSpace ℂ F] [CompleteSpace F]
  (B :
    ↥(TauCeti.UnitAddTorus.smoothFunctions a) →ₗ[ℂ]
      ↥(TauCeti.UnitAddTorus.smoothFunctions b) →ₗ[ℂ] F)
  (hB :
    ∃ C N,
      ∀ (f : ↥(TauCeti.UnitAddTorus.smoothFunctions a))
        (g : ↥(TauCeti.UnitAddTorus.smoothFunctions b)) (M₁ M₂ : ℝ),
        TauCeti.UnitAddTorus.DerivBound N M₁ ↑f →
          TauCeti.UnitAddTorus.DerivBound N M₂ ↑g → ‖(B f) g‖ ≤ C * M₁ * M₂)
  (f : ↥(TauCeti.UnitAddTorus.smoothFunctions a)) (g : ↥(TauCeti.UnitAddTorus.smoothFunctions b)) :
  (B.schwartzKernel hB) ⟨UnitAddTorus.tensor ↑f ↑g, ⋯⟩ = (B f) g
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.schwartzKernel_tensor`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Torus/Kernel.html#LinearMap.schwartzKernel_tensor).

## Sources

- [Tau Ceti documentation: `LinearMap.schwartzKernel_tensor`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Torus/Kernel.html#LinearMap.schwartzKernel_tensor)
- [Source of `LinearMap.schwartzKernel_tensor` in TauCeti/Analysis/Fourier/Torus/Kernel.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Fourier/Torus/Kernel.lean#L283)
