---
declaration: module
origin: cited
lean: TensorSpecies.Tensor, TensorSpecies.Tensor.Pure, TensorSpecies.Tensor.Pure.congr_right, TensorSpecies.Tensor.Pure.congr_mid, TensorSpecies.Tensor.Pure.map_mid_move_left, TensorSpecies.Tensor.Pure.toTensor, TensorSpecies.Tensor.Pure.toTensor_apply, TensorSpecies.Tensor.Pure.update
statement: formalized
proof: formalized
---

# Tensors

The module `Physlib.Relativity.Tensors.Basic`, [Physlib/Relativity/Tensors/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean): 86 declarations (6 instances with no name), 18 with a docstring.

> This module sets up the tensors used for index notation in Physlib.
>
> Physics picture:
> - Choose a symmetry group `G` (for example, the Lorentz group).
> - Give each index kind a name called a *color* (encoded by a type `C`).
>   In Lorentzian notation, a typical choice is two colors: `up` and `down`.
> - For each color, choose a representation of `G`.
> - Fix a basis for each color. This determines which values that index can take and
>   lets us speak about tensor components explicitly.
> - Specify a dual color for each color, telling us which index pairs can contract.
> - For dual pairs, provide the contraction/unit/metric data used for contraction and
>   for raising/lowering indices.
>
> All of this structure is packaged as a `TensorSpecies`.
>
> For `S : TensorSpecies` and a list of index colors `c : Fin n → C`:
> - `Tensor S c` is the type of tensors with those indices.
> - `Pure S c` is the type of pure tensors, i.e. tensors of the form
>   `v₀ ⊗ₜ v₁ ⊗ₜ v₂ …`.
> - `ComponentIdx S c` is the type of allowed component labels for those indices.
>
> This file realizes `Tensor S c` as a `PiTensorProduct`, relates pure tensors to
> their components, constructs the component basis, and supplies the inherited
> finite-dimensional and module-topology instances. It also defines the natural
> action of `G` on pure tensors and tensors, the associated permutation maps, and
> the map from rank-zero tensors to the scalars `k`.
>
> From this setup we get the usual index-notation operations in a uniform way:
> contraction, raising/lowering, and permutation of indices.

**`TensorSpecies.Tensor`**, an abbrev, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L64).

> The tensors associated with a list of indices of a given color
> `c : Fin n → C`.

```lean
noncomputable abbrev Tensor {n : ℕ} (S : TensorSpecies k C G V basisIdx rep b)
  (c : Fin n → C) : Type
```

## Components of tensors

## Pure tensors

**`TensorSpecies.Tensor.Pure`**, an abbrev, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L87).

> The type of pure tensors associated to a list of indices `c : OverColor C`.
> A pure tensor is a tensor which can be written in the form `v1 ⊗ₜ v2 ⊗ₜ v3 …`.

```lean
abbrev Pure (S : TensorSpecies k C G V basisIdx rep b) (c : Fin n → C) : Type
```

**`TensorSpecies.Tensor.Pure.congr_right`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L92).

```lean
lemma congr_right {n : ℕ} {c : Fin n → C} (p : Pure S c)
    (i j : Fin n) (h : i = j) : LinearEquiv.cast (R := k) (by rw [h]) (p j) = p i
```

**`TensorSpecies.Tensor.Pure.congr_mid`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L97).

```lean
lemma congr_mid {n : ℕ} {c : Fin n → C} (c' : C) (p : Pure S c)
    (i j : Fin n) (h : i = j) (hi : c i = c') (hj : c j = c') :
    LinearEquiv.cast (R := k) (by rw [hi] : c i = c') (p i) =
    LinearEquiv.cast (R := k) (by rw [hj] : c j = c') (p j)
```

**`TensorSpecies.Tensor.Pure.map_mid_move_left`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L104).

```lean
lemma map_mid_move_left {n n1 : ℕ} {c : Fin n → C} {c1 : Fin n1 → C} (p : Pure S c)
    (p' : Pure S c1) {c' : C}
    (i : Fin n) (j : Fin n1) (hi : c i = c') (hj : c1 j = c') :
    LinearEquiv.cast (R := k) (by rw [hi] : c i = c') (p i) =
    LinearEquiv.cast (R := k) (by rw [hj] : c1 j = c') (p' j)
    ↔ LinearEquiv.cast (R := k) (by rw [hi, hj] : c i = c1 j) (p i) =
    (p' j)
```

**`TensorSpecies.Tensor.Pure.toTensor`**, a def, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L115).

> The tensor corresponding to a pure tensor.

```lean
noncomputable def toTensor {n : ℕ} {c : Fin n → C} (p : Pure S c) : S.Tensor c
```

**`TensorSpecies.Tensor.Pure.toTensor_apply`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L118).

```lean
lemma toTensor_apply {n : ℕ} (c : Fin n → C) (p : Pure S c) :
    toTensor p = PiTensorProduct.tprod k p
```

**`TensorSpecies.Tensor.Pure.update`**, a def, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L126).

> Given a list of indices `c` of `n` indices, a pure tensor `p`, an element `i : Fin n` and
> a `x` in `V (c i)` then `update p i x` corresponds to `p` where
> the `i`th part of `p` is replaced with `x`.
>
> E.g. if `n = 2` and `p = v₀ ⊗ₜ v₁` then `update p 0 x = x ⊗ₜ v₁`.

```lean
def update {n : ℕ} {c : Fin n → C} [inst : DecidableEq (Fin n)] (p : Pure S c) (i : Fin n)
    (x : V (c i)) : Pure S c
```

**`TensorSpecies.Tensor.Pure.update_eq_function_update`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L129).

```lean
lemma update_eq_function_update {n : ℕ} {c : Fin n → C} [inst : DecidableEq (Fin n)]
    (p : Pure S c) (i : Fin n)
    (x : V (c i)) : update p i x = Function.update p i x
```

**`TensorSpecies.Tensor.Pure.update_same`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L134).

```lean
lemma update_same {n : ℕ} {c : Fin n → C} [inst : DecidableEq (Fin n)] (p : Pure S c) (i : Fin n)
    (x : V (c i)) : (update p i x) i = x
```

**`TensorSpecies.Tensor.Pure.update_diff`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L138).

```lean
lemma update_diff {n : ℕ} {c : Fin n → C} [inst : DecidableEq (Fin n)] (p : Pure S c) (i j : Fin n)
    (x : V (c i)) (hij : i ≠ j) : (update p i x) j = p j
```

**`TensorSpecies.Tensor.Pure.update_succAbove_apply`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L143).

```lean
lemma update_succAbove_apply {n : ℕ} {c : Fin (n + 1) → C} [inst : DecidableEq (Fin (n + 1))]
    (p : Pure S c) (i : Fin (n + 1)) (j : Fin n) (x : V (c (i.succAbove j))) :
    update p (i.succAbove j) x i = p i
```

**`TensorSpecies.Tensor.Pure.toTensor_update_add`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L149).

```lean
lemma toTensor_update_add {n : ℕ} {c : Fin n → C} [inst : DecidableEq (Fin n)] (p : Pure S c)
    (i : Fin n) (x y : V (c i)) :
    (update p i (x + y)).toTensor = (update p i x).toTensor + (update p i y).toTensor
```

**`TensorSpecies.Tensor.Pure.toTensor_update_smul`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L155).

```lean
lemma toTensor_update_smul {n : ℕ} {c : Fin n → C} [inst : DecidableEq (Fin n)] (p : Pure S c)
    (i : Fin n) (r : k) (y : V (c i)) :
    (update p i (r • y)).toTensor = r • (update p i y).toTensor
```

**`TensorSpecies.Tensor.Pure.drop`**, a def, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L164).

> Given a list of indices `c` of length `n + 1`, a pure tensor `p` and an `i : Fin (n + 1)`, then
> `drop p i` is the tensor `p` with it's `i`th part dropped.
>
> For example, if `n = 2` and `p = v₀ ⊗ₜ v₁ ⊗ₜ v₂` then `drop p 1 = v₀ ⊗ₜ v₂`.

```lean
def drop {n : ℕ} {c : Fin (n + 1) → C} (p : Pure S c) (i : Fin (n + 1)) :
    Pure S (c ∘ i.succAbove)
```

**`TensorSpecies.Tensor.Pure.update_succAbove_drop`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L169).

```lean
lemma update_succAbove_drop {n : ℕ} {c : Fin (n + 1) → C} [inst : DecidableEq (Fin (n + 1))]
    (p : Pure S c) (i : Fin (n + 1)) (k : Fin n) (x : V (c (i.succAbove k))) :
    (update p (i.succAbove k) x).drop i = (p.drop i).update k x
```

**`TensorSpecies.Tensor.Pure.update_drop_self`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L175).

```lean
lemma update_drop_self {n : ℕ} {c : Fin (n + 1) → C} [inst : DecidableEq (Fin (n + 1))]
    (p : Pure S c) (i : Fin (n + 1)) (x : V (c i)) :
    (update p i x).drop i = p.drop i
```

## Components

**`TensorSpecies.Tensor.Pure.component`**, a def, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L192).

> Given an element `b` of `ComponentIdx c` and a pure tensor `p` then
> `component p b` is the element of the ring `k` corresponding to
> the component of `p` in the direction `b`.
>
> For example, if `p = v ⊗ₜ w` and `b = ⟨0, 1⟩` then `component p b = v⁰ ⊗ₜ w¹`.

```lean
noncomputable def component {n : ℕ} {c : Fin n → C} (p : Pure S c)
    (φ : ComponentIdx (S := S) c) : k
```

**`TensorSpecies.Tensor.Pure.component_eq`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L196).

```lean
lemma component_eq {n : ℕ} {c : Fin n → C} (p : Pure S c) (φ : ComponentIdx c) :
    p.component φ = ∏ i, (b (c i)).repr (p i) (φ i)
```

**`TensorSpecies.Tensor.Pure.component_eq_drop`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L199).

```lean
lemma component_eq_drop {n : ℕ} {c : Fin (n + 1) → C} (p : Pure S c) (i : Fin (n + 1))
    (φ : ComponentIdx c) :
    p.component φ = ((b (c i)).repr (p i) (φ i)) *
    ((drop p i).component (fun j => φ (i.succAbove j)))
```

**`TensorSpecies.Tensor.Pure.component_update_add`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L206).

```lean
lemma component_update_add {n : ℕ} [inst : DecidableEq (Fin n)]
    {c : Fin n → C} (p : Pure S c) (i : Fin n)
    (x y :V (c i)) (b : ComponentIdx c) :
    (update p i (x + y)).component b = (update p i x).component b +
    (update p i y).component b
```

**`TensorSpecies.Tensor.Pure.component_update_smul`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L216).

```lean
lemma component_update_smul {n : ℕ} [inst : DecidableEq (Fin n)]
    {c : Fin n → C} (p : Pure S c) (i : Fin n)
    (x : k) (y : V (c i)) (b : ComponentIdx c) :
    (update p i (x • y)).component b = x * (update p i y).component b
```

**`TensorSpecies.Tensor.Pure.componentMap`**, a def, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L226).

> The multilinear map taking pure tensors `p` to a map `ComponentIdx c → k` which when
> evaluated returns the components of `p`.

```lean
noncomputable def componentMap {n : ℕ} (c : Fin n → C) :
    MultilinearMap k (fun i => V (c i)) (ComponentIdx (S := S) c → k)
```

**`TensorSpecies.Tensor.Pure.componentMap_apply`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L240).

```lean
lemma componentMap_apply {n : ℕ} (c : Fin n → C)
    (p : Pure S c) : componentMap c p = p.component
```

**`TensorSpecies.Tensor.Pure.basisVector`**, a def, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L246).

> Given an component idx `b` in `ComponentIdx c`, `basisVector c b` is the pure tensor
> formed by `S.basis (c i) (b i)`.

```lean
noncomputable def basisVector {n : ℕ} (c : Fin n → C) (φ : ComponentIdx (S := S) c) : Pure S c
```

**`TensorSpecies.Tensor.Pure.component_basisVector`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L250).

```lean
lemma component_basisVector {n : ℕ} (c : Fin n → C) (b1 b2 : ComponentIdx (S := S) c) :
    (basisVector c b1).component b2 = if b1 = b2 then 1 else 0
```

**`TensorSpecies.Tensor.induction_on_pure`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L256).

```lean
lemma induction_on_pure {n : ℕ} {c : Fin n → C} {P : S.Tensor c → Prop}
    (h : ∀ (p : Pure S c), P p.toTensor)
    (hsmul : ∀ (r : k) t, P t → P (r • t))
    (hadd : ∀ t1 t2, P t1 → P t2 → P (t1 + t2)) (t : S.Tensor c) : P t
```

## The basis

**`TensorSpecies.Tensor.componentMap`**, a def, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L273).

> The linear map from tensors to its components.

```lean
def componentMap {n : ℕ} (c : Fin n → C) : S.Tensor c →ₗ[k] (ComponentIdx (S := S) c → k)
```

**`TensorSpecies.Tensor.componentMap_pure`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L277).

```lean
lemma componentMap_pure {n : ℕ} (c : Fin n → C)
    (p : Pure S c) : componentMap c (p.toTensor) = Pure.componentMap c p
```

**`TensorSpecies.Tensor.ofComponents`**, a def, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L282).

> The tensor created from it's components.

```lean
def ofComponents {n : ℕ} (c : Fin n → C) :
    (ComponentIdx (S := S) c → k) →ₗ[k] S.Tensor c
```

**`TensorSpecies.Tensor.componentMap_ofComponents`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L291).

```lean
lemma componentMap_ofComponents {n : ℕ} (c : Fin n → C) (f : ComponentIdx c → k) :
    componentMap c (ofComponents (S := S) c f) = f
```

**`TensorSpecies.Tensor.ofComponents_componentMap`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L297).

```lean
lemma ofComponents_componentMap {n : ℕ} (c : Fin n → C) (t : S.Tensor c) :
    ofComponents c (componentMap c t) = t
```

**`TensorSpecies.Tensor.basis`**, a def, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L313).

> The basis of tensors.

```lean
def basis {n : ℕ} (c : Fin n → C) : Basis (ComponentIdx (S := S) c) k (S.Tensor c)
```

**`TensorSpecies.Tensor.basis_apply`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L318).

```lean
lemma basis_apply {n : ℕ} (c : Fin n → C) (φ : ComponentIdx (S := S) c) :
    basis c φ = (Pure.basisVector c φ).toTensor
```

**`TensorSpecies.Tensor.basis_repr_pure`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L324).

```lean
lemma basis_repr_pure {n : ℕ} (c : Fin n → C)
    (p : Pure S c) :
    (basis c).repr p.toTensor = p.component
```

**`TensorSpecies.Tensor.induction_on_basis`**, a lemma, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L331).

```lean
lemma induction_on_basis {n : ℕ} {c : Fin n → C} {P : S.Tensor c → Prop}
    (h : ∀ b, P (basis c b)) (hzero : P 0)
    (hsmul : ∀ (r : k) t, P t → P (r • t))
    (hadd : ∀ t1 t2, P t1 → P t2 → P (t1 + t2)) (t : S.Tensor c) : P t
```

**`TensorSpecies.Tensor.componentMap_eq_repr`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L342).

> `componentMap` is the basis representation `(basis c).repr` definitionally; this bridges the two
> notations wherever a component computation meets a `repr` rewrite.

```lean
lemma componentMap_eq_repr {n : ℕ} (c : Fin n → C) (t : S.Tensor c)
    (ψ : ComponentIdx (S := S) c) : componentMap c t ψ = (basis c).repr t ψ
```

**`TensorSpecies.Tensor.componentMap_ext`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L346).

> Two tensors with the same colour sequence are equal when all their components agree.

```lean
lemma componentMap_ext {n : ℕ} {c : Fin n → C} {t₁ t₂ : S.Tensor c}
    (h : ∀ b, componentMap c t₁ b = componentMap c t₂ b) : t₁ = t₂
```

## The rank

**An instance with no name**, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L358).

```lean
instance {k : Type} [Field k] {C : Type} {G : Type} [Group G]
    {V : C → Type} [∀ c, AddCommGroup (V c)] [∀ c, Module k (V c)]
    {basisIdx : C → Type} [∀ c, Fintype (basisIdx c)] [∀ c, DecidableEq (basisIdx c)]
    {rep : (c : C) → Representation k G (V c)} {b : (c : C) → Basis (basisIdx c) k (V c)}
    (S : TensorSpecies k C G V basisIdx rep b)
    {c : Fin n → C} : FiniteDimensional k (S.Tensor c)
```

**An instance with no name**, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L366).

```lean
noncomputable instance {k : Type} [RCLike k] {C : Type} {G : Type} [Group G]
    {V : C → Type} [∀ c, AddCommGroup (V c)] [∀ c, Module k (V c)]
    {basisIdx : C → Type} [∀ c, Fintype (basisIdx c)] [∀ c, DecidableEq (basisIdx c)]
    {rep : (c : C) → Representation k G (V c)} {b : (c : C) → Basis (basisIdx c) k (V c)}
    (S : TensorSpecies k C G V basisIdx rep b)
    {c : Fin n → C} : TopologicalSpace (S.Tensor c)
```

**An instance with no name**, [line 374](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L374).

```lean
instance {k : Type} [RCLike k] {C : Type} {G : Type} [Group G]
    {V : C → Type} [∀ c, AddCommGroup (V c)] [∀ c, Module k (V c)]
    {basisIdx : C → Type} [∀ c, Fintype (basisIdx c)] [∀ c, DecidableEq (basisIdx c)]
    {rep : (c : C) → Representation k G (V c)} {b : (c : C) → Basis (basisIdx c) k (V c)}
    (S : TensorSpecies k C G V basisIdx rep b)
    {c : Fin n → C} : IsTopologicalAddGroup (S.Tensor c)
```

## The action

**`TensorSpecies.Tensor.Pure.actionP`**, an instance, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L389).

```lean
noncomputable instance actionP : MulAction G (Pure S c)
```

**`TensorSpecies.Tensor.Pure.actionP_eq`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L400).

```lean
lemma actionP_eq {g : G} {p : Pure S c} : g • p = fun i => rep (c i) g (p i)
```

**`TensorSpecies.Tensor.Pure.rep_cast`**, a lemma, [line 402](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L402).

```lean
lemma rep_cast {g : G} {c c1 : C} (p : V c) (h : c = c1) :
    LinearEquiv.cast (R := k) h (rep c g p) = rep c1 g (LinearEquiv.cast (R := k) h p)
```

**`TensorSpecies.Tensor.Pure.actionP_cast`**, a lemma, [line 407](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L407).

```lean
lemma actionP_cast {g : G} {p : Pure S c} (h : c = c1) :
    LinearEquiv.cast (R := k) h (g • p) = g • LinearEquiv.cast (R := k) h p
```

**`TensorSpecies.Tensor.Pure.drop_actionP`**, a lemma, [line 413](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L413).

```lean
lemma drop_actionP {n : ℕ} {c : Fin (n + 1) → C} {i : Fin (n + 1)} {p : Pure S c} (g : G) :
    (g • p).drop i = g • (p.drop i)
```

## The action on tensors

**`TensorSpecies.Tensor.instSMul`**, an instance, [line 431](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L431).

```lean
noncomputable instance (priority := high + 1) instSMul : SMul G (S.Tensor c)
```

**`TensorSpecies.Tensor.actionT_eq`**, a lemma, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L434).

```lean
lemma actionT_eq {g : G} {t : S.Tensor c} : g • t =
    PiTensorProduct.map (fun i => rep (c i) g) t
```

**`TensorSpecies.Tensor.actionT`**, an instance, [line 437](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L437).

```lean
noncomputable instance (priority := high + 1) actionT : MulAction G (S.Tensor c)
```

**`TensorSpecies.Tensor.actionT_pure`**, a lemma, [line 447](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L447).

```lean
lemma actionT_pure {g : G} {p : Pure S c} :
    g • p.toTensor = Pure.toTensor (g • p)
```

**`TensorSpecies.Tensor.actionT_add`**, a lemma, [line 451](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L451).

```lean
lemma actionT_add {g : G} {t1 t2 : S.Tensor c} :
    g • (t1 + t2) = g • t1 + g • t2
```

**`TensorSpecies.Tensor.actionT_smul`**, a lemma, [line 456](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L456).

```lean
lemma actionT_smul {g : G} {r : k} {t : S.Tensor c} :
    g • (r • t) = r • (g • t)
```

**`TensorSpecies.Tensor.actionT_zero`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L460).

```lean
lemma actionT_zero {g : G} : g • (0 : S.Tensor c) = 0
```

**`TensorSpecies.Tensor.actionT_neg`**, a lemma, [line 463](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L463).

```lean
lemma actionT_neg {g : G} {t : S.Tensor c} :
    g • (-t) = -(g • t)
```

**An instance with no name**, [line 469](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L469).

```lean
noncomputable instance (priority := high + 1) : DistribMulAction G (S.Tensor c)
```

**An instance with no name**, [line 473](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L473).

```lean
instance : SMulCommClass k G (S.Tensor c)
```

**An instance with no name**, [line 477](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L477).

```lean
instance : SMulCommClass G k (S.Tensor c)
```

## Permutations

**`TensorSpecies.Tensor.Pure.permP`**, a def, [line 491](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L491).

> Given a permutation `σ : Fin m → Fin n` of indices satisfying `IsReindexing` through `h`,
> and a pure tensor `p`, `permP σ h p` is the pure tensor permuted according to `σ`.
>
> For example if `m = n = 2` and `σ = ![1, 0]`, and `p = v ⊗ₜ w` then
> `permP σ _ p = w ⊗ₜ v`.

```lean
def Pure.permP {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    (σ : Fin m → Fin n) (h : IsReindexing c c1 σ) (p : Pure S c) : Pure S c1
```

**`TensorSpecies.Tensor.Pure.permP_basisVector`**, a lemma, [line 496](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L496).

```lean
lemma Pure.permP_basisVector {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    (σ : Fin m → Fin n) (h : IsReindexing c c1 σ) (φ : ComponentIdx (S := S) c) :
    Pure.permP σ h (Pure.basisVector c φ) =
    Pure.basisVector c1 (fun i => basisIdxCongr (by simp [h.preserve_color]) (φ (σ i)))
```

**`TensorSpecies.Tensor.Pure.permP_equivariant`**, a lemma, [line 504](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L504).

```lean
lemma Pure.permP_equivariant {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    {σ : Fin m → Fin n} (h : IsReindexing c c1 σ) (g : G) (p : Pure S c) :
    Pure.permP σ h (g • p) = g • Pure.permP σ h p
```

**`TensorSpecies.Tensor.permT`**, a def, [line 513](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L513).

> The reindexing of a tensor based on a map `σ : Fin m → Fin n` of indices
> satisfying `IsReindexing`.

```lean
noncomputable def permT {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    (σ : Fin m → Fin n) (h : IsReindexing c c1 σ) : S.Tensor c →ₗ[k] S.Tensor c1
```

**`TensorSpecies.Tensor.permT_pure`**, a lemma, [line 519](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L519).

```lean
lemma permT_pure {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    {σ : Fin m → Fin n} (h : IsReindexing c c1 σ) (p : Pure S c) :
    permT σ h p.toTensor = (p.permP σ h).toTensor
```

**`TensorSpecies.Tensor.Pure.permP_id_self`**, a lemma, [line 527](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L527).

```lean
lemma Pure.permP_id_self {n : ℕ} {c : Fin n → C} (p : Pure S c) :
    Pure.permP (id : Fin n → Fin n) (by simp : IsReindexing c c id) p = p
```

**`TensorSpecies.Tensor.permT_id_self`**, a lemma, [line 533](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L533).

```lean
lemma permT_id_self {n : ℕ} {c : Fin n → C} (t : S.Tensor c) :
    permT (id : Fin n → Fin n) (by simp : IsReindexing c c id) t = t
```

**`TensorSpecies.Tensor.permT_congr_eq_id`**, a lemma, [line 540](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L540).

```lean
lemma permT_congr_eq_id {n : ℕ} {c : Fin n → C} (t : S.Tensor c)
    (σ : Fin n → Fin n) (hσ : IsReindexing c c σ) (h : σ = id) :
    permT σ (hσ) t = t
```

**`TensorSpecies.Tensor.permT_congr_eq_id'`**, a lemma, [line 546](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L546).

```lean
lemma permT_congr_eq_id' {n : ℕ} {c : Fin n → C} (t t1 : S.Tensor c)
    (σ : Fin n → Fin n) (hσ : IsReindexing c c σ) (h : σ = id) (ht : t = t1) :
    permT σ (hσ) t = t1
```

**`TensorSpecies.Tensor.permT_equivariant`**, a lemma, [line 553](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L553).

```lean
lemma permT_equivariant {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    {σ : Fin m → Fin n} (h : IsReindexing c c1 σ) (g : G) (t : S.Tensor c) :
    permT σ h (g • t) = g • permT σ h t
```

**`TensorSpecies.Tensor.Pure.permP_congr`**, a lemma, [line 562](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L562).

```lean
lemma Pure.permP_congr {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    {σ σ1 : Fin m → Fin n} {h : IsReindexing c c1 σ} {h1 : IsReindexing c c1 σ1}
    {p p1 : Pure S c} (hmap : σ = σ1) (hpure : p = p1) :
    Pure.permP σ h p = Pure.permP σ1 h1 p1
```

**`TensorSpecies.Tensor.permT_congr`**, a lemma, [line 570](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L570).

```lean
lemma permT_congr {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    {σ σ1 : Fin m → Fin n} {h : IsReindexing c c1 σ} {h1 : IsReindexing c c1 σ1}
    (hmap : σ = σ1) {t t1: S.Tensor c} (htensor : t = t1) :
    permT σ h t = permT σ1 h1 t1
```

**`TensorSpecies.Tensor.Pure.permP_permP`**, a lemma, [line 578](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L578).

```lean
lemma Pure.permP_permP {n m1 m2 : ℕ} {c : Fin n → C} {c1 : Fin m1 → C} {c2 : Fin m2 → C}
    {σ : Fin m1 → Fin n} {σ2 : Fin m2 → Fin m1} (h : IsReindexing c c1 σ)
    (h2 : IsReindexing c1 c2 σ2) (p : Pure S c) :
    Pure.permP σ2 h2 (Pure.permP σ h p) = Pure.permP (σ ∘ σ2) (h.comp h2) p
```

**`TensorSpecies.Tensor.permT_permT`**, a lemma, [line 586](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L586).

```lean
lemma permT_permT {n m1 m2 : ℕ} {c : Fin n → C} {c1 : Fin m1 → C} {c2 : Fin m2 → C}
    {σ : Fin m1 → Fin n} {σ2 : Fin m2 → Fin m1} (h : IsReindexing c c1 σ)
    (h2 : IsReindexing c1 c2 σ2) (t : S.Tensor c) :
    permT σ2 h2 (permT σ h t) = permT (σ ∘ σ2) (h.comp h2) t
```

**`TensorSpecies.Tensor.permT_basis_repr_symm_apply`**, a lemma, [line 596](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L596).

```lean
lemma permT_basis_repr_symm_apply {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    {σ : Fin m → Fin n} (h : IsReindexing c c1 σ) (t : S.Tensor c)
    (φ : ComponentIdx c1) :
    (basis c1).repr (permT σ h t) φ =
    (basis c).repr t (fun i =>
      basisIdxCongr (by simp [IsReindexing.inv_perserve_color]) (φ (h.inv σ i)))
```

**`TensorSpecies.Tensor.permT_basis_repr_of_id`**, a lemma, [line 622](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L622).

> A reindexing whose slot map is pointwise the identity only transports the labels.

```lean
lemma permT_basis_repr_of_id {n : ℕ} {c c1 : Fin n → C} {σ : Fin n → Fin n}
    (hσ : ∀ i, σ i = i) (h : IsReindexing c c1 σ) (t : S.Tensor c)
    (φ : ComponentIdx (S := S) c1) :
    (basis c1).repr (permT σ h t) φ =
    (basis c).repr t (fun i => basisIdxCongr (by rw [← h.2 i, hσ]) (φ i))
```

**`TensorSpecies.Tensor.permT_basis`**, a lemma, [line 632](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L632).

```lean
lemma permT_basis {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    {σ : Fin m → Fin n} (h : IsReindexing c c1 σ)
    (b : ComponentIdx c) :
    (permT σ h) (basis (S := S) c b) = basis c1 (fun i =>
      basisIdxCongr (by simp [h.2]) (b (σ i)))
```

**`TensorSpecies.Tensor.permT_eq_zero_iff`**, a lemma, [line 639](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L639).

```lean
lemma permT_eq_zero_iff {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    {σ : Fin m → Fin n} (h : IsReindexing c c1 σ) (t : S.Tensor c) :
    permT σ h t = 0 ↔ t = 0
```

**`TensorSpecies.Tensor.permT_injective`**, a lemma, [line 649](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L649).

> `permT` is injective.

```lean
lemma permT_injective {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    {σ : Fin m → Fin n} (h : IsReindexing c c1 σ) :
    Function.Injective (permT (S := S) σ h)
```

## Rank-zero tensors as scalars

**`TensorSpecies.Tensor.toScalar`**, a def, [line 660](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L660).

> The linear map between tensors with zero indices and the underlying scalars
> `k`.

```lean
noncomputable def toScalar {c : Fin 0 → C} : S.Tensor c →ₗ[k] k
```

**`TensorSpecies.Tensor.toScalar_default`**, a lemma, [line 663](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L663).

```lean
lemma toScalar_default {c : Fin 0 → C} :
    toScalar (Pure.toTensor default : S.Tensor c) = 1
```

**`TensorSpecies.Tensor.toScalar_injective`**, a lemma, [line 667](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L667).

```lean
lemma toScalar_injective {c : Fin 0 → C} :
    Function.Injective (toScalar : S.Tensor c → k)
```

**`TensorSpecies.Tensor.toScalar_pure`**, a lemma, [line 672](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L672).

```lean
lemma toScalar_pure {c : Fin 0 → C} (p : Pure S c) :
    toScalar (p.toTensor : S.Tensor c) = 1
```

**`TensorSpecies.Tensor.toScalar_permT`**, a lemma, [line 676](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L676).

```lean
lemma toScalar_permT {c c1 : Fin 0 → C} (σ : Fin 0 → Fin 0)
    (h : IsReindexing c c1 σ) (t : S.Tensor c) :
    toScalar (permT σ h t) = toScalar t
```

**`TensorSpecies.Tensor.toScalar_basis_default`**, a lemma, [line 686](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L686).

```lean
lemma toScalar_basis_default {c : Fin 0 → C} :
    toScalar (basis c (@default (ComponentIdx (S := S) c) Unique.instInhabited)) = 1
```

**`TensorSpecies.Tensor.toScalar_basis`**, a lemma, [line 690](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L690).

```lean
lemma toScalar_basis {c : Fin 0 → C} (b : ComponentIdx (S := S) c) :
    toScalar (basis c b) = 1
```

**`TensorSpecies.Tensor.toScalar_eq_repr`**, a lemma, [line 694](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L694).

```lean
lemma toScalar_eq_repr {c : Fin 0 → C} (t : Tensor S c) :
    t.toScalar = (basis c).repr t (fun j => Fin.elim0 j)
```

**`TensorSpecies.Tensor.toScalar_equivariant`**, a lemma, [line 702](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L702).

```lean
lemma toScalar_equivariant {c : Fin 0 → C} (g : G) (t : Tensor S c) :
    toScalar (g • t) = toScalar t
```

**`TensorSpecies.Tensor.eq_smul_toScalar`**, a lemma, [line 709](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean#L709).

```lean
lemma eq_smul_toScalar {c : Fin 0 → C} (t : Tensor S c) :
    t = toScalar t • (basis c (@default (ComponentIdx (S := S) c) Unique.instInhabited))
```

## Depends on

- [Component indices](../part-02/componentidx-basic.md)
- [Reindexing of tensor components](reindexing.md)

## Sources

- [Physlib/Relativity/Tensors/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Basic.lean)
