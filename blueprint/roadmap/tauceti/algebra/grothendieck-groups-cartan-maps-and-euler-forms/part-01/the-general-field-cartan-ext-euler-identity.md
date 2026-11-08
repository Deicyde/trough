---
declaration: theorem
origin: cited
lean: TauCeti.cartanMatrix_transpose_mul_extEulerMatrix_eq_diagonal
statement: formalized
proof: formalized
---

# The general-field Cartan/Ext-Euler identity

Let `P i ⟶ S i` be projective covers of
simple modules. If every pair of finitely generated modules is Euler-admissible, then
`Cᵀ * E = diagonal (fun i ↦ dim_k End_A(S i))`, where `C i j = [P j : S i]` is the Cartan
matrix and `E` is the Ext-Euler matrix in the simple-class basis.

```lean
TauCeti.cartanMatrix_transpose_mul_extEulerMatrix_eq_diagonal.{u, v, u_1} {k : Type u_1} [Field k]
  {A : Type u} [Ring A] [Algebra k A] [IsArtinianRing A] {I : Type v} [Fintype I] [DecidableEq I]
  (P : I → (TauCeti.finiteProjectiveModules A).FullSubcategory) (S : I → FGModuleCat A)
  [hS : ∀ (i : I), IsSimpleModule A ↑(S i)]
  (hind : ∀ (i : I), TauCeti.IsIndecomposableModule A ↑(P i).obj)
  (hPnoniso : Pairwise fun i j => IsEmpty (↑(P i).obj ≃ₗ[A] ↑(P j).obj))
  (hPexhaustive : TauCeti.IsExhaustiveIndecomposableProjectiveFamily P)
  (hSnoniso : Pairwise fun i j => IsEmpty (↑(S i) ≃ₗ[A] ↑(S j)))
  (hSexhaustive : TauCeti.IsExhaustiveSimpleFamily S) {f : (i : I) → ↑(P i).obj →ₗ[A] ↑(S i).obj}
  (hf : ∀ (i : I), TauCeti.IsProjectiveCover (f i))
  (hadm : TauCeti.IsEulerAdmissibleOn k (ModuleCat.isFG A) (ModuleCat.isFG A)) :
  (TauCeti.cartanMatrix P S hind hPnoniso hPexhaustive hSnoniso hSexhaustive).transpose *
      TauCeti.extEulerMatrix (ModuleCat.isFG A) (ModuleCat.isFG A) ⋯ ⋯ hadm
        ((TauCeti.simpleClassBasis S hSnoniso hSexhaustive).map
          (TauCeti.finiteModulesExactK0Equiv A).toIntLinearEquiv)
        ((TauCeti.simpleClassBasis S hSnoniso hSexhaustive).map
          (TauCeti.finiteModulesExactK0Equiv A).toIntLinearEquiv) =
    Matrix.diagonal fun i => ↑(Module.finrank k (Module.End A ↑(S i).obj))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Krull-Schmidt theorem](../../../ring-theory/krull-schmidt/the-krull-schmidt-theorem.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)
- [Schur's lemma, vanishing form](../../../quantum-groups/quantum-groups-compact-reconstruction-and-generi/schurs-lemma-vanishing-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.cartanMatrix_transpose_mul_extEulerMatrix_eq_diagonal`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/GrothendieckGroup/ExtEulerMatrix.html#TauCeti.cartanMatrix_transpose_mul_extEulerMatrix_eq_diagonal).

## Sources

- [Tau Ceti documentation: `TauCeti.cartanMatrix_transpose_mul_extEulerMatrix_eq_diagonal`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/GrothendieckGroup/ExtEulerMatrix.html#TauCeti.cartanMatrix_transpose_mul_extEulerMatrix_eq_diagonal)
- [Source of `TauCeti.cartanMatrix_transpose_mul_extEulerMatrix_eq_diagonal` in TauCeti/RepresentationTheory/GrothendieckGroup/ExtEulerMatrix.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/GrothendieckGroup/ExtEulerMatrix.lean#L84)
