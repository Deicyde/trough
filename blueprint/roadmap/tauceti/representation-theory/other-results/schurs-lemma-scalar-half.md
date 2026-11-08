---
declaration: theorem
origin: cited
lean: ContRepresentation.exists_eq_smul_one_of_isIrreducible, Representation.exists_forall_apply_eq_mul_apply, Representation.eq_zero_of_isEmpty_equiv, Representation.IsIrreducible.exists_forall_apply_eq_smul, ContRepresentation.eq_zero_of_isEmpty_equiv
statement: formalized
proof: formalized
---

# Schur's lemma, scalar half

Every continuous self-intertwiner of an irreducible
finite-dimensional representation over an algebraically closed field is a scalar multiple of the
identity.

```lean
ContRepresentation.exists_eq_smul_one_of_isIrreducible.{u_1, u_2, u_3} {𝕜 : Type u_1} {G : Type u_2}
  {V : Type u_3} [Field 𝕜] [IsAlgClosed 𝕜] [Monoid G] [AddCommGroup V] [_root_.Module 𝕜 V]
  [TopologicalSpace V] [IsTopologicalAddGroup V] [ContinuousConstSMul 𝕜 V] [FiniteDimensional 𝕜 V]
  (π : ContRepresentation 𝕜 G V)
  (hirr : (ContRepresentation.toRepresentation 𝕜 G V π).IsIrreducible)
  (f : ContIntertwiningMap π π) : ∃ c, f = c • 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContRepresentation.exists_eq_smul_one_of_isIrreducible`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Continuous/Schur.html#ContRepresentation.exists_eq_smul_one_of_isIrreducible).

## Other forms

**Schur's lemma for contravariant forms.** Formalized in Tau Ceti as [`Representation.exists_forall_apply_eq_mul_apply`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ContravariantForm.html#Representation.exists_forall_apply_eq_mul_apply).

```lean
Representation.exists_forall_apply_eq_mul_apply.{u_1, u_2, u_4} {𝕜 : Type u_1} {V : Type u_2}
  [Field 𝕜] [StarRing 𝕜] [AddCommGroup V] [_root_.Module 𝕜 V] {G : Type u_4} [Monoid G] [StarMul G]
  (ρ : Representation 𝕜 G V) [IsAlgClosed 𝕜] [FiniteDimensional 𝕜 V] [ρ.IsIrreducible]
  {B : V →ₗ⋆[𝕜] V →ₗ[𝕜] 𝕜} (hB : B.SeparatingRight)
  (hρ : ∀ (g : G) (x y : V), (B ((ρ g) x)) y = (B x) ((ρ (star g)) y)) {S : V →ₗ⋆[𝕜] V →ₗ[𝕜] 𝕜}
  (hS : ∀ (g : G) (x y : V), (S ((ρ g) x)) y = (S x) ((ρ (star g)) y)) :
  ∃ c, ∀ (x y : V), (S x) y = c * (B x) y
```

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

**Schur's lemma, scalar form.** Formalized in Tau Ceti as [`Representation.IsIrreducible.exists_forall_apply_eq_smul`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Irreducible.html#Representation.IsIrreducible.exists_forall_apply_eq_smul).

```lean
Representation.IsIrreducible.exists_forall_apply_eq_smul.{u_1, u_2, u_3} {k : Type u_1}
  {G : Type u_2} {V : Type u_3} [Field k] [Monoid G] [AddCommGroup V] [_root_.Module k V]
  [IsAlgClosed k] [FiniteDimensional k V] {ρ : Representation k G V} [ρ.IsIrreducible]
  (f : V →ₗ[k] V) (hf : ∀ (g : G) (v : V), f ((ρ g) v) = (ρ g) (f v)) : ∃ c, ∀ (v : V), f v = c • v
```

**Schur's lemma, vanishing half.** Formalized in Tau Ceti as [`ContRepresentation.eq_zero_of_isEmpty_equiv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Continuous/Schur.html#ContRepresentation.eq_zero_of_isEmpty_equiv).

```lean
ContRepresentation.eq_zero_of_isEmpty_equiv.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} {G : Type u_2}
  {V : Type u_3} {W : Type u_4} [NontriviallyNormedField 𝕜] [CompleteSpace 𝕜] [Monoid G]
  [AddCommGroup V] [_root_.Module 𝕜 V] [TopologicalSpace V] [IsTopologicalAddGroup V]
  [ContinuousSMul 𝕜 V] [T2Space V] [FiniteDimensional 𝕜 V] [AddCommGroup W] [_root_.Module 𝕜 W]
  [TopologicalSpace W] [IsTopologicalAddGroup W] [ContinuousSMul 𝕜 W] [T2Space W]
  {π : ContRepresentation 𝕜 G V} {ρ : ContRepresentation 𝕜 G W}
  (hπ : (ContRepresentation.toRepresentation 𝕜 G V π).IsIrreducible)
  (hρ : (ContRepresentation.toRepresentation 𝕜 G W ρ).IsIrreducible) (hne : IsEmpty (π.Equiv ρ))
  (f : ContIntertwiningMap π ρ) : f = 0
```

## Sources

- [Tau Ceti documentation: `ContRepresentation.exists_eq_smul_one_of_isIrreducible`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Continuous/Schur.html#ContRepresentation.exists_eq_smul_one_of_isIrreducible)
- [Source of `ContRepresentation.exists_eq_smul_one_of_isIrreducible` in TauCeti/RepresentationTheory/Continuous/Schur.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Continuous/Schur.lean#L83)
