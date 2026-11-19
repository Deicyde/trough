---
declaration: theorem
origin: cited
lean: LinearMap.upperSemicontinuous_finrank_fiber_homology
statement: formalized
proof: formalized
---

# LinearMap.upperSemicontinuous_finrank_fiber_homology

For a complex `M₁ → M₂ → M₃` of `R`-modules with `M₂` finite and `M₃` projective, the
dimension of the homology of the fibre `κ(p) ⊗ M₁ → κ(p) ⊗ M₂ → κ(p) ⊗ M₃` is an upper
semicontinuous function of `p ∈ Spec R`. The homology is written as the image of the cycles
`ker (κ(p) ⊗ g)` in the cokernel of `κ(p) ⊗ f`.

```lean
LinearMap.upperSemicontinuous_finrank_fiber_homology.{u_1, u_2, u_3, u_4} {R : Type u_1}
  {M₁ : Type u_2} {M₂ : Type u_3} {M₃ : Type u_4} [CommRing R] [AddCommGroup M₁]
  [_root_.Module R M₁] [AddCommGroup M₂] [_root_.Module R M₂] [AddCommGroup M₃] [_root_.Module R M₃]
  [Module.Finite R M₂] [Module.Projective R M₃] (f : M₁ →ₗ[R] M₂) (g : M₂ →ₗ[R] M₃)
  (hfg : g ∘ₗ f = 0) :
  UpperSemicontinuous fun p =>
    Module.finrank p.asIdeal.ResidueField
      ↥(Submodule.map (LinearMap.baseChange p.asIdeal.ResidueField f).range.mkQ
          (LinearMap.baseChange p.asIdeal.ResidueField g).ker)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.upperSemicontinuous_finrank_fiber_homology`](https://taucetiproject.org/docs/TauCeti/RingTheory/Spectrum/Prime/Semicontinuity.html#LinearMap.upperSemicontinuous_finrank_fiber_homology).

## Sources

- [Tau Ceti documentation: `LinearMap.upperSemicontinuous_finrank_fiber_homology`](https://taucetiproject.org/docs/TauCeti/RingTheory/Spectrum/Prime/Semicontinuity.html#LinearMap.upperSemicontinuous_finrank_fiber_homology)
- [Source of `LinearMap.upperSemicontinuous_finrank_fiber_homology` in TauCeti/RingTheory/Spectrum/Prime/Semicontinuity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Spectrum/Prime/Semicontinuity.lean#L113)
- [Tau Ceti roadmap status: The Jacobian challenge](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/JacobianChallenge/STATUS.md)
