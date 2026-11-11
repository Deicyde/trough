---
declaration: theorem
origin: cited
lean: CliffordAlgebra.endValuedTensorEquiv_ι_mem_invariants_iff
statement: formalized
proof: formalized
---

# Clifford multiplication is an invariant tensor exactly when the Clifford action is equivariant

For a group acting on `V` by isometries `ρ g` of `Q` and on a Clifford module `E`
by `μ`, the tensor of Clifford multiplication `v ↦ π (ι Q v)` is fixed by the tensor product
representation `(ρ_A)* ⊗ (μ* ⊗ μ)` if and only if `π (map (ρ g) a) = μ g ∘ π a ∘ μ g⁻¹` for every
group element `g` and every Clifford element `a`.

```lean
CliffordAlgebra.endValuedTensorEquiv_ι_mem_invariants_iff.{u_1, u_2, u_3, u_4, u_5} {R : Type u_1}
  {A : Type u_2} {V : Type u_3} {E : Type u_4} {G : Type u_5} [CommRing R] [CommRing A]
  [Algebra R A] [AddCommGroup V] [_root_.Module R V] [Module.Finite R V] [Module.Projective R V]
  [AddCommGroup E] [_root_.Module A E] [Module.Finite A E] [Module.Projective A E]
  [_root_.Module R E] [IsScalarTower R A E] [Group G] {Q : QuadraticForm R V}
  (ρ : Representation R G V) (hρ : ∀ (g : G) (v : V), Q ((ρ g) v) = Q v) (μ : Representation A G E)
  (π : CliffordAlgebra Q →ₐ[R] Module.End A E) :
  (TauCeti.endValuedTensorEquiv R A V E) (π.toLinearMap ∘ₗ CliffordAlgebra.ι Q) ∈
      ((Representation.baseChange A ρ).dual.tprod (μ.dual.tprod μ)).invariants ↔
    ∀ (g : G) (a : CliffordAlgebra Q),
      π ((CliffordAlgebra.map { toLinearMap := ρ g, map_app' := ⋯ }) a) = μ g ∘ₗ π a ∘ₗ μ g⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.endValuedTensorEquiv_ι_mem_invariants_iff`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/EquivariantModule.html#CliffordAlgebra.endValuedTensorEquiv_%CE%B9_mem_invariants_iff).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.endValuedTensorEquiv_ι_mem_invariants_iff`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/EquivariantModule.html#CliffordAlgebra.endValuedTensorEquiv_%CE%B9_mem_invariants_iff)
- [Source of `CliffordAlgebra.endValuedTensorEquiv_ι_mem_invariants_iff` in TauCeti/LinearAlgebra/CliffordAlgebra/EquivariantModule.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/CliffordAlgebra/EquivariantModule.lean#L55)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpinGeometry/STATUS.md)
