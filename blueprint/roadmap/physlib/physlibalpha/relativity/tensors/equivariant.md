---
declaration: module
origin: cited
lean: TensorSpecies.IsEquivariant, TensorSpecies.smul_basis_eq_sum, TensorSpecies.basis_repr_smul, TensorSpecies.IsEquivariant.isStableUnder_range, TensorSpecies.IsEquivariant.rep_map_of_invariant, TensorSpecies.IsEquivariant.sum, TensorSpecies.IsEquivariant.comp, TensorSpecies.IsEquivariant.sub
statement: formalized
proof: formalized
---

# Equivariant maps out of the tensors of a species

The module `PhyslibAlpha.Relativity.Tensors.Equivariant`, [PhyslibAlpha/Relativity/Tensors/Equivariant.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean): 26 declarations, 25 with a docstring.

## i. Overview

> A family of vectors in a representation `ρ` of the group `G` of a tensor species `S`, carrying
> indices of colors `c`, is packaged as a linear map `f : S.Tensor c →ₗ[k] B`, and
> `S.IsEquivariant c ρ f` says that `f` intertwines the action of `G` on tensors with `ρ` (A).
>
> Over `ℂ`, the invariants in the range of such a map come from invariant tensors (C): every
> invariant of `LinearMap.range f ⊔ W`, for `W` a `G`-stable submodule, is `f t + y` with `t` an
> invariant tensor and `y ∈ W`. This holds whenever the colors are closed under adjoints (B): for
> every `g` some `g'` acts on each color by the conjugate transpose of the matrix of `g`. The
> classification of the invariants in the range of `f` is thereby reduced to that of the invariant
> tensors of `S.Tensor c`, `IsEquivariant.invariantReductionToSpan`.
>
> A map is specified by its values on the basis tensors with `Basis.constr`, and
> `isEquivariant_constr` turns a transformation law of those values into equivariance (D). With
> the component indices relabelled by `e`, the map of a family `T` is `familyMap e T`, and it is
> equivariant exactly when `T` obeys that law, `isEquivariant_familyMap_iff`.

## ii. Key results

> - `TensorSpecies.IsEquivariant` : equivariant linear maps out of `S.Tensor c`.
> - `TensorSpecies.smul_basis_eq_sum` : the action on the basis tensors.
> - `TensorSpecies.IsAdjointClosed` : the colors are closed under conjugate transposition.
> - `TensorSpecies.IsEquivariant.exists_invariant_add_of_mem_sup` : invariants of the range come from
>   invariant tensors.
> - `TensorSpecies.IsEquivariant.reducesInvariantsTo_map` : the reduction to the image of a
>   submodule containing the invariant tensors.
> - `TensorSpecies.IsEquivariant.invariantReductionToSpan` : the reduction to one invariant tensor.
> - `TensorSpecies.isEquivariant_familyMap_iff` : the map of a family is equivariant exactly when
>   the family obeys the transformation law of the components.

## iv. References

> * None.

## A. Equivariant maps and the action on basis tensors

**`TensorSpecies.IsEquivariant`**, a structure, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L79).

> A linear map `f` from the tensors of the species `S` with index colors `c` to a
> representation `ρ` of the group of the species, which is equivariant: it intertwines the action
> of the group on tensors with `ρ`.

```lean
structure IsEquivariant (S : TensorSpecies k C G V basisIdx rep b) {n : ℕ} (c : Fin n → C)
    {B : Type*} [AddCommMonoid B] [Module k B] (ρ : Representation k G B)
    (f : S.Tensor c →ₗ[k] B) : Prop where
  equivariant : ∀ (g : G) (t : S.Tensor c), f (g • t) = ρ g (f t)
```

**`TensorSpecies.smul_basis_eq_sum`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L88).

> The action of `g` on a basis tensor: the coefficient of `e_ψ` in `g • e_φ` is the product over
> the indices of the matrix entries of `g` in the color of that index.

```lean
lemma smul_basis_eq_sum {n : ℕ} (c : Fin n → C) (g : G) (φ : ComponentIdx (S := S) c) :
    g • Tensor.basis (S := S) c φ
      = ∑ ψ : ComponentIdx (S := S) c,
        (∏ i, LinearMap.toMatrix (b (c i)) (b (c i)) (rep (c i) g) (ψ i) (φ i)) •
        Tensor.basis (S := S) c ψ
```

**`TensorSpecies.basis_repr_smul`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L109).

> The components of `g • t`: the matrix of products of the matrix entries of `g`, one factor
> per index, applied to the components of `t`.

```lean
lemma basis_repr_smul {n : ℕ} (c : Fin n → C) (g : G) (t : S.Tensor c)
    (φ : ComponentIdx (S := S) c) :
    (Tensor.basis c).repr (g • t) φ
      = ∑ ψ, (∏ i, LinearMap.toMatrix (b (c i)) (b (c i)) (rep (c i) g) (φ i) (ψ i)) *
        (Tensor.basis c).repr t ψ
```

**`TensorSpecies.IsEquivariant.isStableUnder_range`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L131).

> The range of an equivariant map is stable under the group.

```lean
lemma isStableUnder_range : IsStableUnder (fun g : G => ρ g) (LinearMap.range f)
```

**`TensorSpecies.IsEquivariant.rep_map_of_invariant`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L137).

> The image of an invariant tensor under an equivariant map is invariant.

```lean
lemma rep_map_of_invariant {t : S.Tensor c} (ht : ∀ g : G, g • t = t) (g : G) :
    ρ g (f t) = f t
```

**`TensorSpecies.IsEquivariant.sum`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L142).

> A sum of equivariant maps is equivariant.

```lean
lemma sum {ι : Type*} (s : Finset ι) {F : ι → S.Tensor c →ₗ[k] B}
    (hF : ∀ i ∈ s, S.IsEquivariant c ρ (F i)) : S.IsEquivariant c ρ (∑ i ∈ s, F i)
```

**`TensorSpecies.IsEquivariant.comp`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L150).

> Composing with a linear map that intertwines `ρ` with `ρ'` keeps a map equivariant.

```lean
lemma comp {B' : Type*} [AddCommGroup B'] [Module k B'] {ρ' : Representation k G B'}
    (σ : B →ₗ[k] B') (hσ : ∀ (g : G) (y : B), σ (ρ g y) = ρ' g (σ y)) :
    S.IsEquivariant c ρ' (σ ∘ₗ f)
```

**`TensorSpecies.IsEquivariant.sub`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L158).

> A difference of equivariant maps is equivariant.

```lean
lemma sub {f' : S.Tensor c →ₗ[k] B} (hf' : S.IsEquivariant c ρ f') :
    S.IsEquivariant c ρ (f - f')
```

## B. Colors closed under adjoints

**`TensorSpecies.IsAdjointClosed`**, a def, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L185).

> The colors `c` of a complex species are closed under adjoints when for every `g` some `g'`
> acts on each of them by the conjugate transpose of the matrix of `g`. For a unitary group
> `g' = g⁻¹` and orthonormal bases; for `SL(2,ℂ)` on the Weyl colors, `g' = g†`.

```lean
def IsAdjointClosed (S : TensorSpecies ℂ C G V basisIdx rep b) {n : ℕ} (c : Fin n → C) :
    Prop
```

## C. Invariants in the range come from invariant tensors

**`TensorSpecies.IsEquivariant.exists_invariant_eq_of_mem_range`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L206).

> An invariant in the range of `f` is the image of an invariant tensor, when the colors are
> closed under adjoints: the adjoint of the action of `g` on the coefficients is that of `g'`.

```lean
lemma exists_invariant_eq_of_mem_range (hc : S.IsAdjointClosed c) {x : B}
    (hx : x ∈ LinearMap.range f) (hinv : ∀ g : G, ρ g x = x) :
    ∃ t : S.Tensor c, (∀ g : G, g • t = t) ∧ f t = x
```

**`TensorSpecies.IsEquivariant.exists_invariant_add_of_mem_sup`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L232).

> An invariant of `LinearMap.range f ⊔ W`, for `W` a stable submodule, is the image of an
> invariant tensor plus an element of `W`.

```lean
lemma exists_invariant_add_of_mem_sup (hc : S.IsAdjointClosed c) (W : Submodule ℂ B)
    (hW : ∀ g : G, ∀ y ∈ W, ρ g y ∈ W) {x : B} (hx : x ∈ LinearMap.range f ⊔ W)
    (hinv : ∀ g : G, ρ g x = x) :
    ∃ t : S.Tensor c, (∀ g : G, g • t = t) ∧ ∃ y ∈ W, x = f t + y
```

**`TensorSpecies.IsEquivariant.reducesInvariantsTo_map`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L253).

> When every invariant tensor of `S.Tensor c` lies in `I`, the invariants of the range of `f`
> reduce to the image of `I`.

```lean
lemma reducesInvariantsTo_map (hc : S.IsAdjointClosed c) (I : Submodule ℂ (S.Tensor c))
    (hI : ∀ t : S.Tensor c, (∀ g : G, g • t = t) → t ∈ I) :
    ReducesInvariantsTo (fun g : G => ρ g) (LinearMap.range f) (I.map f)
```

**`TensorSpecies.IsEquivariant.reducesInvariantsTo_bot`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L262).

> When the only invariant tensor of `S.Tensor c` is zero, the range of `f` reduces to `⊥`.

```lean
lemma reducesInvariantsTo_bot (hc : S.IsAdjointClosed c)
    (hI : ∀ t : S.Tensor c, (∀ g : G, g • t = t) → t = 0) :
    ReducesInvariantsTo (fun g : G => ρ g) (LinearMap.range f) ⊥
```

**`TensorSpecies.IsEquivariant.eq_zero_of_invariant`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L271).

> When the only invariant tensor of `S.Tensor c` is zero, so is every invariant in the range
> of `f`.

```lean
lemma eq_zero_of_invariant (hc : S.IsAdjointClosed c)
    (hI : ∀ t : S.Tensor c, (∀ g : G, g • t = t) → t = 0) {x : B}
    (hx : x ∈ LinearMap.range f) (hinv : ∀ g : G, ρ g x = x) : x = 0
```

**`TensorSpecies.IsEquivariant.invariantReductionToSpan`**, a def, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L280).

> When the invariant tensors of `S.Tensor c` are the multiples of one tensor `t₀`, the
> invariants of the range of `f` reduce to the span of `f t₀`.

```lean
noncomputable def invariantReductionToSpan (hc : S.IsAdjointClosed c) (t₀ : S.Tensor c)
    (ht₀ : ∀ g : G, g • t₀ = t₀)
    (hclass : ∀ t : S.Tensor c, (∀ g : G, g • t = t) → ∃ a : ℂ, t = a • t₀) :
    InvariantReductionToSpan (fun g : G => ρ g) (LinearMap.range f)
```

**`TensorSpecies.IsEquivariant.invariantReductionToSpanOfEq`**, a def, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L295).

> The reduction of `invariantReductionToSpan`, stated for a submodule `V` equal to the range of
> `f` and with the spanning vector given by any expression `v` for `f t₀`.

```lean
noncomputable def invariantReductionToSpanOfEq (hc : S.IsAdjointClosed c) (t₀ : S.Tensor c)
    (ht₀ : ∀ g : G, g • t₀ = t₀)
    (hclass : ∀ t : S.Tensor c, (∀ g : G, g • t = t) → ∃ a : ℂ, t = a • t₀)
    {V : Submodule ℂ B} (hV : LinearMap.range f = V) (v : B) (hv : f t₀ = v) :
    InvariantReductionToSpan (fun g : G => ρ g) V
```

## D. Building equivariant maps

**`TensorSpecies.isEquivariant_constr`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L327).

> The linear map with prescribed values `T ψ` on the basis tensors is equivariant when the
> values are moved by `ρ` as the basis tensors are moved by the group.

```lean
lemma isEquivariant_constr {n : ℕ} {c : Fin n → C} {B : Type*} [AddCommGroup B] [Module k B]
    {ρ : Representation k G B} (T : ComponentIdx (S := S) c → B)
    (hT : ∀ (g : G) φ, ρ g (T φ)
      = ∑ ψ, (∏ i, LinearMap.toMatrix (b (c i)) (b (c i)) (rep (c i) g) (ψ i) (φ i)) • T ψ) :
    S.IsEquivariant c ρ ((Tensor.basis c).constr k T)
```

**`TensorSpecies.familyMap`**, a def, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L345).

> The linear map out of `S.Tensor c` sending the basis tensor with components `e.symm l` to
> `T l`, for a relabelling `e` of the component indices by `ι`.

```lean
noncomputable def familyMap (e : ComponentIdx (S := S) c ≃ ι) (T : ι → B) :
    S.Tensor c →ₗ[k] B
```

**`TensorSpecies.familyMap_basis`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L350).

```lean
lemma familyMap_basis (e : ComponentIdx (S := S) c ≃ ι) (T : ι → B) (l : ι) :
    familyMap e T (Tensor.basis c (e.symm l)) = T l
```

**`TensorSpecies.range_familyMap`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L355).

> The range of `familyMap e T` is the span of the vectors `T l`.

```lean
lemma range_familyMap (e : ComponentIdx (S := S) c ≃ ι) (T : ι → B) :
    LinearMap.range (familyMap e T) = Submodule.span k (Set.range T)
```

**`TensorSpecies.familyMap_mem_span`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L361).

> The image of `familyMap e T` lies in the span of the vectors `T l`.

```lean
lemma familyMap_mem_span (e : ComponentIdx (S := S) c ≃ ι) (T : ι → B) (t : S.Tensor c) :
    familyMap e T t ∈ Submodule.span k (Set.range T)
```

**`TensorSpecies.familyMap_sum`**, a lemma, [line 367](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L367).

> `familyMap` of a sum of families is the sum of the maps.

```lean
lemma familyMap_sum (e : ComponentIdx (S := S) c ≃ ι) {α : Type*} (s : Finset α)
    (T : α → ι → B) :
    familyMap e (fun l => ∑ i ∈ s, T i l) = ∑ i ∈ s, familyMap e (T i)
```

**`TensorSpecies.familyMap_sub`**, a lemma, [line 373](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L373).

> `familyMap` of a difference of families is the difference of the maps.

```lean
lemma familyMap_sub (e : ComponentIdx (S := S) c ≃ ι) (T T' : ι → B) :
    familyMap e (fun l => T l - T' l) = familyMap e T - familyMap e T'
```

**`TensorSpecies.comp_familyMap`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L379).

> A linear map applied after `familyMap e T` is `familyMap` of its values on the
> components.

```lean
lemma comp_familyMap (e : ComponentIdx (S := S) c ≃ ι) {B' : Type*} [AddCommGroup B']
    [Module k B'] (σ : B →ₗ[k] B') (T : ι → B) :
    σ ∘ₗ familyMap e T = familyMap e fun l => σ (T l)
```

**`TensorSpecies.familyMap_smul_of_law`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L386).

> A linear map moving a family as `g` moves the basis tensors intertwines the map of the family
> with the action of `g`.

```lean
lemma familyMap_smul_of_law (e : ComponentIdx (S := S) c ≃ ι) [Fintype ι] (T : ι → B)
    {σ : B →ₗ[k] B} (g : G)
    (hσ : ∀ l : ι, σ (T l) = ∑ a, (∏ i, LinearMap.toMatrix (b (c i)) (b (c i)) (rep (c i) g)
      (e.symm a i) (e.symm l i)) • T a) (t : S.Tensor c) :
    σ (familyMap e T t) = familyMap e T (g • t)
```

**`TensorSpecies.isEquivariant_familyMap_iff`**, a lemma, [line 402](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L402).

> The map of a family is equivariant exactly when the family is moved as the basis tensors
> are: one matrix entry of `g` per index, the summed index first in each factor.

```lean
lemma isEquivariant_familyMap_iff (e : ComponentIdx (S := S) c ≃ ι) [Fintype ι]
    {ρ : Representation k G B} (T : ι → B) :
    S.IsEquivariant c ρ (familyMap e T) ↔ ∀ (g : G) (l : ι), ρ g (T l)
      = ∑ a, (∏ i, LinearMap.toMatrix (b (c i)) (b (c i)) (rep (c i) g)
        (e.symm a i) (e.symm l i)) • T a
```

## Depends on

- [Tensors](../../../physlib/relativity/tensors/part-01/basic.md)
- [Reducing invariants modulo a stable submodule](../../mathematics/part-01/invariantreduction.md)

## Sources

- [PhyslibAlpha/Relativity/Tensors/Equivariant.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/Equivariant.lean)
