---
declaration: theorem
origin: cited
lean: Representation.exists_forall_apply_eq_mul_apply, Representation.eq_zero_of_isEmpty_equiv
statement: formalized
proof: formalized
---

# Schur's lemma for contravariant forms

Over an algebraically closed field, a contravariant
form on a finite-dimensional irreducible representation is a scalar multiple of any separating
contravariant form.

```lean
Representation.exists_forall_apply_eq_mul_apply.{u_1, u_2, u_4} {𝕜 : Type u_1} {V : Type u_2}
  [Field 𝕜] [StarRing 𝕜] [AddCommGroup V] [_root_.Module 𝕜 V] {G : Type u_4} [Monoid G] [StarMul G]
  (ρ : Representation 𝕜 G V) [IsAlgClosed 𝕜] [FiniteDimensional 𝕜 V] [ρ.IsIrreducible]
  {B : V →ₗ⋆[𝕜] V →ₗ[𝕜] 𝕜} (hB : B.SeparatingRight)
  (hρ : ∀ (g : G) (x y : V), (B ((ρ g) x)) y = (B x) ((ρ (star g)) y)) {S : V →ₗ⋆[𝕜] V →ₗ[𝕜] 𝕜}
  (hS : ∀ (g : G) (x y : V), (S ((ρ g) x)) y = (S x) ((ρ (star g)) y)) :
  ∃ c, ∀ (x y : V), (S x) y = c * (B x) y
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Representation.exists_forall_apply_eq_mul_apply`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ContravariantForm.html#Representation.exists_forall_apply_eq_mul_apply).

## Other forms

**Schur's lemma for pairings of nonisomorphic representations.** Formalized in Tau Ceti as [`Representation.eq_zero_of_isEmpty_equiv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ContravariantForm.html#Representation.eq_zero_of_isEmpty_equiv).

```lean
Representation.eq_zero_of_isEmpty_equiv.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} {V : Type u_2}
  {W : Type u_3} [Field 𝕜] [StarRing 𝕜] [AddCommGroup V] [_root_.Module 𝕜 V] [AddCommGroup W]
  [_root_.Module 𝕜 W] {G : Type u_4} [Monoid G] [StarMul G] (ρ : Representation 𝕜 G V)
  (σ : Representation 𝕜 G W) [FiniteDimensional 𝕜 V] [ρ.IsIrreducible] [σ.IsIrreducible]
  {B : V →ₗ⋆[𝕜] V →ₗ[𝕜] 𝕜} (hB : B.SeparatingRight)
  (hρ : ∀ (g : G) (x y : V), (B ((ρ g) x)) y = (B x) ((ρ (star g)) y)) {S : V →ₗ⋆[𝕜] W →ₗ[𝕜] 𝕜}
  (hS : ∀ (g : G) (x : V) (y : W), (S ((ρ g) x)) y = (S x) ((σ (star g)) y))
  (hne : IsEmpty (σ.Equiv ρ)) : S = 0
```

## Sources

- [Tau Ceti documentation: `Representation.exists_forall_apply_eq_mul_apply`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ContravariantForm.html#Representation.exists_forall_apply_eq_mul_apply)
- [Source of `Representation.exists_forall_apply_eq_mul_apply` in TauCeti/RepresentationTheory/ContravariantForm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/ContravariantForm.lean#L79)
