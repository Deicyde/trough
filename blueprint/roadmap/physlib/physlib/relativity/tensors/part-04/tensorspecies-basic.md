---
declaration: module
origin: cited
lean: TensorSpecies, TensorSpecies.basisIdxCongr, TensorSpecies.basisIdxCongr_rfl, TensorSpecies.basisIdxCongr_symm, TensorSpecies.basisIdxCongr_apply_apply, TensorSpecies.basisIdxCongr_heq_arg, TensorSpecies.basisIdxCongr_heq, TensorSpecies.basisIdxCongr_const
statement: formalized
proof: formalized
---

# Tensor species (Basic)

The module `Physlib.Relativity.Tensors.TensorSpecies.Basic`, [Physlib/Relativity/Tensors/TensorSpecies/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/Basic.lean): 17 declarations, 11 with a docstring.

> - A tensor species is a structure including all of the ingredients needed to define a type of
>   tensor.
> - Examples of tensor species will include real Lorentz tensors, complex Lorentz tensors, and
>   Einstein tensors.
> - Tensor species are built upon symmetric monoidal categories.

**`TensorSpecies`**, a structure, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/Basic.lean#L34).

> The structure `TensorSpecies` contains the necessary structure needed to define
> a system of tensors with index notation. Examples of `TensorSpecies` include real Lorentz tensors,
> complex Lorentz tensors, and ordinary Euclidean tensors.

```lean
structure TensorSpecies (k : Type) [CommRing k] (C : Type) (G : Type) [Group G]
    (V : C → Type) [∀ c, AddCommGroup (V c)] [∀ c, Module k (V c)]
    (basisIdx : C → Type) [∀ c, Fintype (basisIdx c)] [∀ c, DecidableEq (basisIdx c)]
    (rep : (c : C) → Representation k G (V c)) (basis : (c : C) → Basis (basisIdx c) k (V c)) where
  /-- A map from `C` to `C`. An involution. -/
  τ : C → C
  /-- The condition that `τ` is an involution. -/
  τ_involution : Function.Involutive τ
  /-- The contraction of vectors with dual colors. -/
  contr : (c : C) → ((rep c).tprod (rep (τ c))).IntertwiningMap (Representation.trivial k G k)
  /-- The invariant unit tensor for a given color. -/
  unit : (c : C) → ((Representation.trivial k G k)).IntertwiningMap ((rep (τ c)).tprod (rep c))
  /-- Contraction is symmetric with respect to duals. -/
  contr_tmul_symm : ∀ c (x : V c) (y : V (τ c)),
      contr c (x ⊗ₜ[k] y) = contr (τ c) (y ⊗ₜ Equiv.cast (congrArg V (τ_involution c).symm) x)
  /-- The unit is symmetric. -/
  unit_symm : ∀ c, unit c (1 : k) =
      LinearMap.lTensor _ (LinearEquiv.cast (τ_involution c)).toLinearMap
      (TensorProduct.comm k _ _ (unit (τ c) (1 : k)))
  /-- Contraction with unit leaves invariant. -/
  contr_unit : ∀ c (x : V c),
    (TensorProduct.lid k _ <|
    (contr c).toLinearMap.rTensor _ <|
    (TensorProduct.assoc k (V c) (V (τ c)) (V c)).symm <|
    x ⊗ₜ[k] (unit c (1 : k))) = x
```

## Properties of the basis

**`TensorSpecies.basisIdxCongr`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/Basic.lean#L73).

> The casting between `basisIdx c` and `basisIdx c1`.

```lean
def basisIdxCongr {c c1 : C} (h : c = c1) :
    basisIdx c ≃ basisIdx c1
```

**`TensorSpecies.basisIdxCongr_rfl`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/Basic.lean#L77).

```lean
lemma basisIdxCongr_rfl (c : C) (i : basisIdx c) :
    basisIdxCongr (Eq.refl c) i = i
```

**`TensorSpecies.basisIdxCongr_symm`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/Basic.lean#L80).

```lean
lemma basisIdxCongr_symm {c c1 : C} (h : c = c1) (i : basisIdx c1) :
    (basisIdxCongr h).symm i = basisIdxCongr h.symm i
```

**`TensorSpecies.basisIdxCongr_apply_apply`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/Basic.lean#L86).

```lean
lemma basisIdxCongr_apply_apply {c c1 c2 : C} (h1 : c = c1) (h2 : c1 = c2) (i : basisIdx c) :
    basisIdxCongr h2 (basisIdxCongr h1 i) = basisIdxCongr (by simp [h1, h2]) i
```

**`TensorSpecies.basisIdxCongr_heq_arg`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/Basic.lean#L92).

> `basisIdxCongr` only depends on its endpoints up to `HEq` of the arguments: equal target
> colours and heterogeneously equal labels give equal casts.

```lean
lemma basisIdxCongr_heq_arg {c1 c2 d : C} (h1 : c1 = d) (h2 : c2 = d)
    {x : basisIdx c1} {y : basisIdx c2} (hxy : HEq x y) :
    basisIdxCongr h1 x = basisIdxCongr h2 y
```

**`TensorSpecies.basisIdxCongr_heq`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/Basic.lean#L98).

> A transported label is heterogeneously equal to the original.

```lean
lemma basisIdxCongr_heq {c c1 : C} (h : c = c1) (x : basisIdx c) : basisIdxCongr h x ≍ x
```

**`TensorSpecies.basisIdxCongr_const`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/Basic.lean#L105).

> For a species whose every colour carries the same label type `I`, a label transport is the
> identity.

```lean
lemma basisIdxCongr_const {I : Type} {c c1 : C} (h : c = c1) :
    basisIdxCongr (basisIdx := fun _ : C => I) h = Equiv.refl I
```

**`TensorSpecies.τ_τ_apply`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/Basic.lean#L118).

```lean
lemma τ_τ_apply (c : C) : S.τ (S.τ c) = c
```

**`TensorSpecies.basis_congr`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/Basic.lean#L121).

```lean
lemma basis_congr {c c1 : C} (h : c = c1) (i : basisIdx c) :
    basis c i = LinearEquiv.cast (R := k) h.symm (basis c1 (basisIdxCongr h i))
```

**`TensorSpecies.map_basis_eq`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/Basic.lean#L127).

```lean
lemma map_basis_eq {c c1 : C} (h : c = c1) (i : basisIdx c) :
    LinearEquiv.cast (R := k) h (basis c i) = basis c1 (basisIdxCongr h i)
```

**`TensorSpecies.contr_basis_congr`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/Basic.lean#L134).

> The contraction of two basis vectors does not change when their colour is transported along an
> equality and their labels with it.

```lean
lemma contr_basis_congr {a a' : C} (h : a = a') (x : basisIdx a) (y : basisIdx (S.τ a)) :
    S.contr a (basis a x ⊗ₜ[k] basis (S.τ a) y) =
      S.contr a' (basis a' (basisIdxCongr h x) ⊗ₜ[k]
        basis (S.τ a') (basisIdxCongr (congrArg S.τ h) y))
```

**`TensorSpecies.equivCast_basis`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/Basic.lean#L144).

> `map_basis_eq` with the cast spelled `Equiv.cast`, the form `contr_tmul_symm` applies to its
> first vector.

```lean
lemma equivCast_basis {c c1 : C} (h : c = c1) (i : basisIdx c) :
    Equiv.cast (congrArg V h) (basis c i) = basis c1 (basisIdxCongr h i)
```

**`TensorSpecies.numIndices`**, a def, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/Basic.lean#L151).

> The number of indices `n` from a tensor.

```lean
def numIndices {S : TensorSpecies k C G V basisIdx rep basis} {n : ℕ} {c : Fin n → C}
    (_ : PiTensorProduct k (fun i => V (c i))) : ℕ
```

## Metric

**`TensorSpecies.WithMetric`**, a class, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/Basic.lean#L164).

> Instance of a metric on a tensor species. For each color `c` an invariant tensor
> in `V c ⊗ V c`, whose contraction against the metric of the dual color `τ c` is the unit.
> Not every species has one: it requires every color to be self-dual,
> which fails for the fundamental of `SU(N)`, `3 ≤ N`.

```lean
class WithMetric {k : Type} [CommRing k] {C : Type} {G : Type} [Group G]
    {V : C → Type} [∀ c, AddCommGroup (V c)] [∀ c, Module k (V c)]
    {basisIdx : C → Type} [∀ c, Fintype (basisIdx c)] [∀ c, DecidableEq (basisIdx c)]
    {rep : (c : C) → Representation k G (V c)} {basis : (c : C) → Basis (basisIdx c) k (V c)}
    (S : TensorSpecies k C G V basisIdx rep basis) where
  /-- The invariant metric tensor for a given color. -/
  metric : (c : C) → ((Representation.trivial k G k)).IntertwiningMap ((rep c).tprod (rep c))
  /-- On contracting metrics we get the unit. -/
  contr_metric : ∀ c,
    (TensorProduct.comm k _ _ <|
      (TensorProduct.lid k _).lTensor _ <|
      ((S.contr c).toLinearMap.rTensor (V (S.τ c))).lTensor (V c) <|
      (TensorProduct.assoc k (V c) (V (S.τ c)) (V (S.τ c))).symm.toLinearMap.lTensor (V c) <|
      TensorProduct.assoc k (V c) (V c) (V (S.τ c) ⊗[k] V (S.τ c)) <|
      (metric c 1) ⊗ₜ[k] (metric (S.τ c) 1)) = S.unit c (1 : k)
```

**`TensorSpecies.metric`**, an abbrev, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/Basic.lean#L181).

> The metric of a species with a metric, at the color `c`.

```lean
abbrev metric [S.WithMetric] (c : C) :
    ((Representation.trivial k G k)).IntertwiningMap ((rep c).tprod (rep c))
```

**`TensorSpecies.contr_metric`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/Basic.lean#L186).

> On contracting metrics we get the unit.

```lean
lemma contr_metric [S.WithMetric] (c : C) :
    (TensorProduct.comm k _ _ <|
      (TensorProduct.lid k _).lTensor _ <|
      ((S.contr c).toLinearMap.rTensor (V (S.τ c))).lTensor (V c) <|
      (TensorProduct.assoc k (V c) (V (S.τ c)) (V (S.τ c))).symm.toLinearMap.lTensor (V c) <|
      TensorProduct.assoc k (V c) (V c) (V (S.τ c) ⊗[k] V (S.τ c)) <|
      (S.metric c 1) ⊗ₜ[k] (S.metric (S.τ c) 1)) = S.unit c (1 : k)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Relativity/Tensors/TensorSpecies/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/TensorSpecies/Basic.lean)
