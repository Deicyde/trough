---
declaration: theorem
origin: cited
lean: TauCeti.exists_forall_apply_eq_smul, TauCeti.LieModule.finrank_lieModuleHom, TauCeti.LieModule.bijective_of_ne_zero
statement: formalized
proof: formalized
---

# Schur's lemma for Lie modules

Over an algebraically closed field, a morphism of a
finite-dimensional irreducible `L`-module to itself is multiplication by a scalar: an eigenvalue
exists, and the corresponding eigenspace is a nonzero Lie submodule, hence everything.

```lean
TauCeti.exists_forall_apply_eq_smul.{u, v, w} (K : Type u) [Field K] (L : Type v) [LieRing L]
  [LieAlgebra K L] (M : Type w) [AddCommGroup M] [_root_.Module K M] [LieRingModule L M]
  [LieModule K L M] [LieModule.IsIrreducible K L M] [IsAlgClosed K] [FiniteDimensional K M]
  (f : M →ₗ⁅K,L⁆ M) : ∃ c, ∀ (m : M), f m = c • m
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_forall_apply_eq_smul`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Weights/Central.html#TauCeti.exists_forall_apply_eq_smul).

## Other forms

**Schur's lemma for finite-dimensional irreducible Lie modules over an algebraically closed field, in its dimension form.** Formalized in Tau Ceti as [`TauCeti.LieModule.finrank_lieModuleHom`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Schur.html#TauCeti.LieModule.finrank_lieModuleHom).

```lean
TauCeti.LieModule.finrank_lieModuleHom.{u, v, w, w₁} (K : Type u) (L : Type v) {M : Type w}
  {N : Type w₁} [Field K] [IsAlgClosed K] [LieRing L] [LieAlgebra K L] [AddCommGroup M]
  [_root_.Module K M] [LieRingModule L M] [LieModule K L M] [AddCommGroup N] [_root_.Module K N]
  [LieRingModule L N] [LieModule K L N] [FiniteDimensional K M] [LieModule.IsIrreducible K L M]
  [LieModule.IsIrreducible K L N] :
  Module.finrank K (M →ₗ⁅K,L⁆ N) = if Nonempty (M ≃ₗ⁅K,L⁆ N) then 1 else 0
```

**Schur's lemma for Lie modules, in its bijectivity form.** Formalized in Tau Ceti as [`TauCeti.LieModule.bijective_of_ne_zero`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Schur.html#TauCeti.LieModule.bijective_of_ne_zero).

```lean
TauCeti.LieModule.bijective_of_ne_zero.{u, v, w, w₁} {R : Type u} {L : Type v} {M : Type w}
  {N : Type w₁} [CommRing R] [LieRing L] [AddCommGroup M] [_root_.Module R M] [LieRingModule L M]
  [AddCommGroup N] [_root_.Module R N] [LieRingModule L N] [LieModule.IsIrreducible R L M]
  [LieModule.IsIrreducible R L N] {f : M →ₗ⁅R,L⁆ N} (hf : f ≠ 0) : Function.Bijective ⇑f
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_forall_apply_eq_smul`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Weights/Central.html#TauCeti.exists_forall_apply_eq_smul)
- [Source of `TauCeti.exists_forall_apply_eq_smul` in TauCeti/Algebra/Lie/Weights/Central.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/Weights/Central.lean#L137)
