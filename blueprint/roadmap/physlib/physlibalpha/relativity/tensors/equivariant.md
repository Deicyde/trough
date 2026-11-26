---
declaration: module
origin: cited
lean: TensorSpecies.IsEquivariant, TensorSpecies.smul_basis_eq_sum, TensorSpecies.basis_repr_smul, TensorSpecies.tensorRep, TensorSpecies.tensorRep_apply, TensorSpecies.tensorRep_eq_prod_smul, TensorSpecies.invariants_tensorRep_eq_span_singleton, TensorSpecies.invariants_tensorRep_eq_bot
statement: formalized
proof: formalized
---

# Equivariant maps out of the tensors of a species

The module `PhyslibAlpha.Relativity.Tensors.Equivariant`, [PhyslibAlpha/Relativity/Tensors/Equivariant.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean): 76 declarations, 71 with a docstring.

> Families of vectors carrying tensor indices, and how their invariants come from invariant tensors.

## i. Overview

> A family of vectors in a representation `ρ` of the group `G` of a tensor species `S`, carrying
> indices of colors `c`, is packaged as a linear map `f : S.Tensor c →ₗ[k] B`, and
> `S.IsEquivariant c ρ f` says that `f` intertwines the action of `G` on tensors with `ρ`. The action
> on `S.Tensor c` is a representation `S.tensorRep c`, so the invariant tensors are the Mathlib
> submodule `(S.tensorRep c).invariants` (A). Every classification of invariant tensors is stated as
> `(S.tensorRep c).invariants = ℂ ∙ t₀`, `= Submodule.span ℂ s` or `= ⊥`.
>
> Over `ℂ`, the invariants in the range of such a map come from invariant tensors (C): every
> invariant of `LinearMap.range f ⊔ W`, for `W` a `G`-stable submodule, is `f t + y` with `t` an
> invariant tensor and `y ∈ W`. This holds whenever the tensors have a Reynolds element,
> `HasReynolds` (B): an element of the group algebra with coefficients summing to one which maps
> every tensor to an invariant one. Applied to any preimage of an invariant `f t`, it gives an
> invariant tensor with the same image. The Reynolds elements of a group are produced from the
> continuity of its action, which `continuousMatrixCoeff_top_comp` reads off the matrix entries of
> the colors. A classification of the invariant tensors thereby classifies the invariants in the
> range of `f`, `IsEquivariant.invariantReductionToSpan`, and the invariants in the range of an
> intertwining map out of the tensors, `HasReynolds.invariants_inf_range_eq_span`.
>
> A family `T` of vectors indexed by the component indices of `S.Tensor c` is the map
> `liftComponents T`, sending each basis tensor to the matching component, and it is equivariant
> exactly when the components obey the transformation law of the components of a tensor in the
> basis of the species, `isEquivariant_liftComponents_iff` (D). A family indexed by other labels is
> first relabelled by an equivalence `e` with the component indices, as `liftComponents (T ∘ e)`.
>
> A tensor with two indices is `fromPairT` of exactly one element of the tensor product of the two
> representations, and `fromPairTEquiv` intertwines the two actions, so the invariant tensors with
> two indices are the image of the invariants of that tensor product; likewise for three indices and
> `fromTripleTEquiv` (E). A classification of the invariants of a tensor product of
> representations is thereby one of the invariant tensors. A family with two indices `T x y`,
> relabelled by `pairIdx`, gives an equivariant map when each index moves by the matrix of its
> colour, `isEquivariant_liftComponents_pair`.
>
> Reindexing and dualising an index carry the invariant tensors of one colour list onto those of
> the other, so a classification is stated only for the canonical order of the colours, undualised.
> A classification of the coefficient functions fixed by the matrices of the group, one factor per
> index, is one of the invariant tensors, `invariants_tensorRep_eq_map_componentEquiv` (F).
>
> The group of a species can be changed along a homomorphism for each colour, the same for a colour
> and its dual, keeping the tensors, `restrict` (G).

## ii. Key results

> - `TensorSpecies.IsEquivariant` : equivariant linear maps out of `S.Tensor c`.
> - `TensorSpecies.tensorRep` : the action on tensors as a representation.
> - `TensorSpecies.HasReynolds` : the tensors have a Reynolds element.
> - `TensorSpecies.continuousMatrixCoeff_top_comp` : continuity of the action on the tensors from
>   that of the colors.
> - `TensorSpecies.IsEquivariant.exists_invariant_add_of_mem_sup` : invariants of the range come from
>   invariant tensors.
> - `TensorSpecies.IsEquivariant.reducesInvariantsTo_span`,
>   `TensorSpecies.IsEquivariant.reducesInvariantsTo_bot` : the reductions given by the invariant
>   tensors.
> - `TensorSpecies.IsEquivariant.invariantReductionToSpan` : the reduction to one invariant tensor.
> - `TensorSpecies.HasReynolds.invariants_inf_range_eq_map` : the invariants in the range of an
>   intertwining map out of the tensors are the image of the invariant tensors.
> - `TensorSpecies.liftComponents` : a family lifted to the linear map out of the tensors sending
>   each basis tensor to the matching member of the family.
> - `TensorSpecies.isEquivariant_liftComponents_iff` : the map of a family is equivariant exactly when
>   the family obeys the transformation law of the components.
> - `TensorSpecies.invariants_tensorRep_pair_eq_span`,
>   `TensorSpecies.invariants_tensorRep_triple_eq_span` : invariant tensors with two or three
>   indices from the invariants of the tensor product of the representations.
> - `TensorSpecies.invariants_tensorRep_eq_map_permT`,
>   `TensorSpecies.invariants_tensorRep_update_eq_map_toDualMapAtIndex` : the invariant tensors
>   transported along a reindexing and along the dualisation of an index.
> - `TensorSpecies.invariants_tensorRep_eq_map_componentEquiv` : the invariant tensors from the
>   invariant coefficient functions.
> - `TensorSpecies.restrict` : a species restricted along a homomorphism of groups for each colour.

## iv. References

> * None.

## A. Equivariant maps and the tensors as a representation

**`TensorSpecies.IsEquivariant`**, a structure, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L131).

> A linear map `f` from the tensors of the species `S` with index colors `c` to a
> representation `ρ` of the group of the species, which is equivariant, that is, it intertwines
> the action of the group on tensors with `ρ`.

```lean
structure IsEquivariant (S : TensorSpecies k C G V basisIdx rep b) {n : ℕ} (c : Fin n → C)
    {B : Type*} [AddCommMonoid B] [Module k B] (ρ : Representation k G B)
    (f : S.Tensor c →ₗ[k] B) : Prop where
  equivariant : ∀ (g : G) (t : S.Tensor c), f (g • t) = ρ g (f t)
```

**`TensorSpecies.smul_basis_eq_sum`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L140).

> The action of `g` on a basis tensor. The coefficient of `e_ψ` in `g • e_φ` is the product over
> the indices of the matrix entries of `g` in the color of that index.

```lean
lemma smul_basis_eq_sum {n : ℕ} (c : Fin n → C) (g : G) (φ : ComponentIdx (S := S) c) :
    g • Tensor.basis (S := S) c φ
      = ∑ ψ : ComponentIdx (S := S) c,
        (∏ i, LinearMap.toMatrix (b (c i)) (b (c i)) (rep (c i) g) (ψ i) (φ i)) •
        Tensor.basis (S := S) c ψ
```

**`TensorSpecies.basis_repr_smul`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L161).

> The components of `g • t`, the matrix of products of the matrix entries of `g`, one factor
> per index, applied to the components of `t`.

```lean
lemma basis_repr_smul {n : ℕ} (c : Fin n → C) (g : G) (t : S.Tensor c)
    (φ : ComponentIdx (S := S) c) :
    (Tensor.basis c).repr (g • t) φ
      = ∑ ψ, (∏ i, LinearMap.toMatrix (b (c i)) (b (c i)) (rep (c i) g) (φ i) (ψ i)) *
        (Tensor.basis c).repr t ψ
```

**`TensorSpecies.tensorRep`**, a def, [line 178](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L178).

> The action of the group on the tensors with index colors `c`, as a representation.

```lean
noncomputable def tensorRep {n : ℕ} (c : Fin n → C) : Representation k G (S.Tensor c)
```

**`TensorSpecies.tensorRep_apply`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L184).

```lean
lemma tensorRep_apply {n : ℕ} {c : Fin n → C} (g : G) (t : S.Tensor c) :
    S.tensorRep c g t = g • t
```

**`TensorSpecies.tensorRep_eq_prod_smul`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L189).

> When `g` acts on the representation of each colour `a` by a scalar `s a`, it acts on the
> tensors with colours `c` by the product of the scalars of their colours.

```lean
lemma tensorRep_eq_prod_smul {g : G} {s : C → k} (hs : ∀ (a : C) (v : V a), rep a g v = s a • v)
    {n : ℕ} (c : Fin n → C) : S.tensorRep c g = (∏ i, s (c i)) • LinearMap.id
```

**`TensorSpecies.invariants_tensorRep_eq_span_singleton`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L204).

> The invariant tensors are the line through an invariant tensor `t₀` when every invariant
> tensor is a multiple of it.

```lean
lemma invariants_tensorRep_eq_span_singleton {n : ℕ} {c : Fin n → C} {t₀ : S.Tensor c}
    (ht₀ : ∀ g : G, g • t₀ = t₀)
    (h : ∀ t : S.Tensor c, (∀ g : G, g • t = t) → ∃ a : k, t = a • t₀) :
    (S.tensorRep c).invariants = k ∙ t₀
```

**`TensorSpecies.invariants_tensorRep_eq_bot`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L213).

> There are no invariant tensors but zero when every invariant tensor vanishes.

```lean
lemma invariants_tensorRep_eq_bot {n : ℕ} {c : Fin n → C}
    (h : ∀ t : S.Tensor c, (∀ g : G, g • t = t) → t = 0) : (S.tensorRep c).invariants = ⊥
```

**`TensorSpecies.IsEquivariant.isStableUnder_range`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L224).

> The range of an equivariant map is stable under the group.

```lean
lemma isStableUnder_range : IsStableUnder (fun g : G => ρ g) (LinearMap.range f)
```

**`TensorSpecies.IsEquivariant.rep_map_of_invariant`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L230).

> The image of an invariant tensor under an equivariant map is invariant.

```lean
lemma rep_map_of_invariant {t : S.Tensor c} (ht : ∀ g : G, g • t = t) (g : G) :
    ρ g (f t) = f t
```

**`TensorSpecies.IsEquivariant.sum`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L235).

> A sum of equivariant maps is equivariant.

```lean
lemma sum {ι : Type*} (s : Finset ι) {F : ι → S.Tensor c →ₗ[k] B}
    (hF : ∀ i ∈ s, S.IsEquivariant c ρ (F i)) : S.IsEquivariant c ρ (∑ i ∈ s, F i)
```

**`TensorSpecies.IsEquivariant.comp`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L243).

> Composing with a linear map that intertwines `ρ` with `ρ'` keeps a map equivariant.

```lean
lemma comp {B' : Type*} [AddCommGroup B'] [Module k B'] {ρ' : Representation k G B'}
    (σ : B →ₗ[k] B') (hσ : ∀ (g : G) (y : B), σ (ρ g y) = ρ' g (σ y)) :
    S.IsEquivariant c ρ' (σ ∘ₗ f)
```

**`TensorSpecies.IsEquivariant.sub`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L251).

> A difference of equivariant maps is equivariant.

```lean
lemma sub {f' : S.Tensor c →ₗ[k] B} (hf' : S.IsEquivariant c ρ f') :
    S.IsEquivariant c ρ (f - f')
```

## B. Reynolds elements for the tensors

**`TensorSpecies.HasReynolds`**, a def, [line 275](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L275).

> The tensors of `S` with index colors `c` have a Reynolds element: an element of the group
> algebra, with coefficients summing to one, which maps every tensor to an invariant tensor.

```lean
def HasReynolds (S : TensorSpecies ℂ C G V basisIdx rep b) {n : ℕ} (c : Fin n → C) : Prop
```

**`TensorSpecies.HasReynolds.of_comp`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L282).

> The tensors have a Reynolds element when they have one for the action restricted along a
> surjective homomorphism `φ` onto the group of the species.

```lean
lemma HasReynolds.of_comp {H : Type*} [Group H] {φ : H →* G} (hφ : Function.Surjective φ)
    (h : ∃ r, Representation.IsReynolds ((S.tensorRep c).comp φ) ⊤ r) : S.HasReynolds c
```

**`TensorSpecies.continuousMatrixCoeff_top_comp`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L288).

> The action on the tensors, restricted along `φ : H →* G`, has continuous matrix coefficients
> when the matrix entries of every color are continuous on `H`.

```lean
lemma continuousMatrixCoeff_top_comp {H : Type*} [Group H] [TopologicalSpace H] (φ : H →* G)
    (hφ : ∀ (k : C) (x y : basisIdx k),
      Continuous fun h => LinearMap.toMatrix (b k) (b k) (rep k (φ h)) x y) :
    Representation.ContinuousMatrixCoeff (⊤ : Subrepresentation ((S.tensorRep c).comp φ))
```

## C. Invariants in the range come from invariant tensors

**`TensorSpecies.IsEquivariant.exists_invariant_eq_of_mem_range`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L313).

> An invariant in the range of `f` is the image of an invariant tensor, the Reynolds element
> applied to any preimage.

```lean
lemma exists_invariant_eq_of_mem_range (hc : S.HasReynolds c) {x : B}
    (hx : x ∈ LinearMap.range f) (hinv : ∀ g : G, ρ g x = x) :
    ∃ t : S.Tensor c, (∀ g : G, g • t = t) ∧ f t = x
```

**`TensorSpecies.IsEquivariant.exists_invariant_add_of_mem_sup`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L325).

> An invariant of `LinearMap.range f ⊔ W`, for `W` a stable submodule, is the image of an
> invariant tensor plus an element of `W`.

```lean
lemma exists_invariant_add_of_mem_sup (hc : S.HasReynolds c) (W : Submodule ℂ B)
    (hW : ∀ g : G, ∀ y ∈ W, ρ g y ∈ W) {x : B} (hx : x ∈ LinearMap.range f ⊔ W)
    (hinv : ∀ g : G, ρ g x = x) :
    ∃ t : S.Tensor c, (∀ g : G, g • t = t) ∧ ∃ y ∈ W, x = f t + y
```

**`TensorSpecies.IsEquivariant.reducesInvariantsTo_map`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L346).

> When every invariant tensor of `S.Tensor c` lies in `I`, the invariants of the range of `f`
> reduce to the image of `I`.

```lean
lemma reducesInvariantsTo_map (hc : S.HasReynolds c) {I : Submodule ℂ (S.Tensor c)}
    (hI : (S.tensorRep c).invariants ≤ I) :
    ReducesInvariantsTo (fun g : G => ρ g) (LinearMap.range f) (I.map f)
```

**`TensorSpecies.IsEquivariant.reducesInvariantsTo_span`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L356).

> When the invariant tensors are the span of `s`, the invariants of the range of `f` reduce to
> the span of the image of `s`.

```lean
lemma reducesInvariantsTo_span (hc : S.HasReynolds c) {s : Set (S.Tensor c)}
    (h : (S.tensorRep c).invariants = Submodule.span ℂ s) :
    ReducesInvariantsTo (fun g : G => ρ g) (LinearMap.range f) (Submodule.span ℂ (f '' s))
```

**`TensorSpecies.IsEquivariant.reducesInvariantsTo_bot`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L364).

> When the only invariant tensor of `S.Tensor c` is zero, the range of `f` reduces to `⊥`.

```lean
lemma reducesInvariantsTo_bot (hc : S.HasReynolds c) (h : (S.tensorRep c).invariants = ⊥) :
    ReducesInvariantsTo (fun g : G => ρ g) (LinearMap.range f) ⊥
```

**`TensorSpecies.IsEquivariant.eq_zero_of_invariant`**, a lemma, [line 372](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L372).

> When the only invariant tensor of `S.Tensor c` is zero, so is every invariant in the range
> of `f`.

```lean
lemma eq_zero_of_invariant (hc : S.HasReynolds c) (h : (S.tensorRep c).invariants = ⊥)
    {x : B} (hx : x ∈ LinearMap.range f) (hinv : ∀ g : G, ρ g x = x) : x = 0
```

**`TensorSpecies.IsEquivariant.invariantReductionToSpan`**, a def, [line 380](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L380).

> When the invariant tensors of `S.Tensor c` are the line through `t₀`, the invariants of the
> range of `f` reduce to the span of `f t₀`.

```lean
noncomputable def invariantReductionToSpan (hc : S.HasReynolds c) {t₀ : S.Tensor c}
    (h : (S.tensorRep c).invariants = ℂ ∙ t₀) :
    InvariantReductionToSpan (fun g : G => ρ g) (LinearMap.range f)
```

**`TensorSpecies.IsEquivariant.invariantReductionToSpanOfEq`**, a def, [line 394](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L394).

> The reduction of `invariantReductionToSpan`, stated for a submodule `V` equal to the range of
> `f` and with the spanning vector given by any expression `v` for `f t₀`.

```lean
noncomputable def invariantReductionToSpanOfEq (hc : S.HasReynolds c) {t₀ : S.Tensor c}
    (h : (S.tensorRep c).invariants = ℂ ∙ t₀) {V : Submodule ℂ B}
    (hV : LinearMap.range f = V) (v : B) (hv : f t₀ = v) :
    InvariantReductionToSpan (fun g : G => ρ g) V
```

**`TensorSpecies.HasReynolds.invariants_inf_range_eq_map`**, a lemma, [line 411](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L411).

> With a Reynolds element, the invariants in the range of an intertwining map `f` out of the
> tensors are the images of the invariant tensors.

```lean
lemma HasReynolds.invariants_inf_range_eq_map (hc : S.HasReynolds c)
    (f : (S.tensorRep c).IntertwiningMap ρ) :
    ρ.invariants ⊓ f.range.toSubmodule = (S.tensorRep c).invariants.map f.toLinearMap
```

**`TensorSpecies.HasReynolds.invariants_inf_range_eq_span`**, a lemma, [line 418](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L418).

> The invariants in the range of an intertwining map `f` out of the tensors are the line through
> `f t₀` when the invariant tensors are the line through `t₀`.

```lean
lemma HasReynolds.invariants_inf_range_eq_span (hc : S.HasReynolds c) {t₀ : S.Tensor c}
    (h : (S.tensorRep c).invariants = ℂ ∙ t₀) (f : (S.tensorRep c).IntertwiningMap ρ) :
    ρ.invariants ⊓ f.range.toSubmodule = ℂ ∙ f t₀
```

**`TensorSpecies.HasReynolds.invariants_inf_range_eq_bot`**, a lemma, [line 426](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L426).

> The invariants in the range of an intertwining map `f` out of the tensors are zero when there
> are no invariant tensors but zero.

```lean
lemma HasReynolds.invariants_inf_range_eq_bot (hc : S.HasReynolds c)
    (h : (S.tensorRep c).invariants = ⊥) (f : (S.tensorRep c).IntertwiningMap ρ) :
    ρ.invariants ⊓ f.range.toSubmodule = ⊥
```

## D. Maps from components

**`TensorSpecies.liftComponents`**, a def, [line 451](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L451).

> A family `T` indexed by the component indices, lifted along the tensor basis to the linear map
> out of `S.Tensor c` sending each basis tensor to the matching component `T φ`.

```lean
noncomputable def liftComponents (T : ComponentIdx (S := S) c → B) : S.Tensor c →ₗ[k] B
```

**`TensorSpecies.liftComponents_basis`**, a lemma, [line 455](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L455).

```lean
lemma liftComponents_basis (T : ComponentIdx (S := S) c → B) (φ : ComponentIdx (S := S) c) :
    liftComponents T (Tensor.basis c φ) = T φ
```

**`TensorSpecies.range_liftComponents`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L460).

> The range of `liftComponents T` is the span of the components.

```lean
lemma range_liftComponents (T : ComponentIdx (S := S) c → B) :
    LinearMap.range (liftComponents T) = Submodule.span k (Set.range T)
```

**`TensorSpecies.range_liftComponents_comp`**, a lemma, [line 466](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L466).

> The range of the map of a family relabelled by an equivalence `e` is the span of the
> family.

```lean
lemma range_liftComponents_comp {ι : Type*} (e : ComponentIdx (S := S) c ≃ ι) (T : ι → B) :
    LinearMap.range (liftComponents (T ∘ e)) = Submodule.span k (Set.range T)
```

**`TensorSpecies.liftComponents_mem`**, a lemma, [line 471](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L471).

> The image of `liftComponents T` lies in every submodule containing the components.

```lean
lemma liftComponents_mem (T : ComponentIdx (S := S) c → B) {M : Submodule k B}
    (hT : ∀ φ, T φ ∈ M) (t : S.Tensor c) : liftComponents T t ∈ M
```

**`TensorSpecies.liftComponents_comp_mem_span`**, a lemma, [line 481](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L481).

> The image of the map of a family relabelled by an equivalence `e` lies in the span of the
> family.

```lean
lemma liftComponents_comp_mem_span {ι : Type*} (e : ComponentIdx (S := S) c ≃ ι) (T : ι → B)
    (t : S.Tensor c) : liftComponents (T ∘ e) t ∈ Submodule.span k (Set.range T)
```

**`TensorSpecies.liftComponents_comp_mem`**, a lemma, [line 488](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L488).

> The image of the map of a relabelled family lies in every submodule containing the
> family.

```lean
lemma liftComponents_comp_mem {ι : Type*} (e : ComponentIdx (S := S) c ≃ ι) (T : ι → B)
    {M : Submodule k B} (hT : ∀ l, T l ∈ M) (t : S.Tensor c) : liftComponents (T ∘ e) t ∈ M
```

**`TensorSpecies.liftComponents_sum`**, a lemma, [line 493](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L493).

> `liftComponents` of a sum of families is the sum of the maps.

```lean
lemma liftComponents_sum {α : Type*} (s : Finset α) (T : α → ComponentIdx (S := S) c → B) :
    liftComponents (fun φ => ∑ i ∈ s, T i φ) = ∑ i ∈ s, liftComponents (T i)
```

**`TensorSpecies.liftComponents_sub`**, a lemma, [line 498](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L498).

> `liftComponents` of a difference of families is the difference of the maps.

```lean
lemma liftComponents_sub (T T' : ComponentIdx (S := S) c → B) :
    liftComponents (fun φ => T φ - T' φ) = liftComponents T - liftComponents T'
```

**`TensorSpecies.comp_liftComponents`**, a lemma, [line 504](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L504).

> A linear map applied after `liftComponents T` is `liftComponents` of its values on the
> components.

```lean
lemma comp_liftComponents {B' : Type*} [AddCommGroup B'] [Module k B'] (σ : B →ₗ[k] B')
    (T : ComponentIdx (S := S) c → B) :
    σ ∘ₗ liftComponents T = liftComponents fun φ => σ (T φ)
```

**`TensorSpecies.map_liftComponents`**, a lemma, [line 511](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L511).

> A linear map applied to `liftComponents T t` is `liftComponents` of its values on the
> components, applied to `t`.

```lean
lemma map_liftComponents {B' : Type*} [AddCommGroup B'] [Module k B'] (σ : B →ₗ[k] B')
    (T : ComponentIdx (S := S) c → B) (t : S.Tensor c) :
    σ (liftComponents T t) = liftComponents (fun φ => σ (T φ)) t
```

**`TensorSpecies.liftComponents_comp_sum`**, a lemma, [line 517](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L517).

> `liftComponents` of a sum of relabelled families is the sum of the maps.

```lean
lemma liftComponents_comp_sum {ι α : Type*} (e : ComponentIdx (S := S) c ≃ ι) (s : Finset α)
    (T : α → ι → B) :
    liftComponents ((fun l => ∑ i ∈ s, T i l) ∘ e) = ∑ i ∈ s, liftComponents (T i ∘ e)
```

**`TensorSpecies.liftComponents_comp_sub`**, a lemma, [line 523](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L523).

> `liftComponents` of a difference of relabelled families is the difference of the maps.

```lean
lemma liftComponents_comp_sub {ι : Type*} (e : ComponentIdx (S := S) c ≃ ι) (T T' : ι → B) :
    liftComponents ((fun l => T l - T' l) ∘ e) = liftComponents (T ∘ e) - liftComponents (T' ∘ e)
```

**`TensorSpecies.map_liftComponents_comp`**, a lemma, [line 529](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L529).

> A linear map applied to the map of a relabelled family is the map of its values on the
> family.

```lean
lemma map_liftComponents_comp {ι : Type*} {B' : Type*} [AddCommGroup B'] [Module k B']
    (σ : B →ₗ[k] B') (e : ComponentIdx (S := S) c ≃ ι) (T : ι → B) (t : S.Tensor c) :
    σ (liftComponents (T ∘ e) t) = liftComponents ((fun l => σ (T l)) ∘ e) t
```

**`TensorSpecies.liftComponents_smul_of_law`**, a lemma, [line 536](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L536).

> A linear map moving the components as `g` moves the basis tensors intertwines
> `liftComponents T` with the action of `g`.

```lean
lemma liftComponents_smul_of_law (T : ComponentIdx (S := S) c → B) {σ : B →ₗ[k] B} (g : G)
    (hσ : ∀ φ, σ (T φ)
      = ∑ ψ, (∏ i, LinearMap.toMatrix (b (c i)) (b (c i)) (rep (c i) g) (ψ i) (φ i)) • T ψ)
    (t : S.Tensor c) :
    σ (liftComponents T t) = liftComponents T (g • t)
```

**`TensorSpecies.isEquivariant_liftComponents_iff`**, a lemma, [line 552](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L552).

> The map of a family is equivariant exactly when the components are moved as the basis
> tensors are, with one matrix entry of `g` per index and the summed index first in each
> factor.

```lean
lemma isEquivariant_liftComponents_iff {ρ : Representation k G B}
    (T : ComponentIdx (S := S) c → B) :
    S.IsEquivariant c ρ (liftComponents T) ↔ ∀ (g : G) (φ : ComponentIdx (S := S) c), ρ g (T φ)
      = ∑ ψ, (∏ i, LinearMap.toMatrix (b (c i)) (b (c i)) (rep (c i) g) (ψ i) (φ i)) • T ψ
```

**`TensorSpecies.isEquivariant_liftComponents_sum`**, a lemma, [line 564](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L564).

> The map of a finite sum of families is equivariant when the map of each family is.

```lean
lemma isEquivariant_liftComponents_sum {ρ : Representation k G B} {α : Type*} (s : Finset α)
    {T : α → ComponentIdx (S := S) c → B}
    (hT : ∀ i ∈ s, S.IsEquivariant c ρ (liftComponents (T i))) :
    S.IsEquivariant c ρ (liftComponents fun φ => ∑ i ∈ s, T i φ)
```

## E. Invariant tensors with two and three indices

**`TensorSpecies.Tensor.fromPairT_injective`**, a lemma, [line 590](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L590).

> A tensor with two indices determines the element of `V c1 ⊗ V c2` it comes from.

```lean
lemma fromPairT_injective {c1 c2 : C} :
    Function.Injective (fromPairT (S := S) (c1 := c1) (c2 := c2))
```

**`TensorSpecies.Tensor.fromPairT_surjective`**, a lemma, [line 599](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L599).

> Every tensor with two indices comes from `V c1 ⊗ V c2`, since the basis tensors do.

```lean
lemma fromPairT_surjective {c1 c2 : C} :
    Function.Surjective (fromPairT (S := S) (c1 := c1) (c2 := c2))
```

**`TensorSpecies.Tensor.fromTripleT_injective`**, a lemma, [line 611](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L611).

> A tensor with three indices determines the element of `V c1 ⊗ (V c2 ⊗ V c3)` it comes
> from.

```lean
lemma fromTripleT_injective {c1 c2 c3 : C} :
    Function.Injective (fromTripleT (S := S) (c1 := c1) (c2 := c2) (c3 := c3))
```

**`TensorSpecies.Tensor.fromTripleT_surjective`**, a lemma, [line 622](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L622).

> Every tensor with three indices comes from `V c1 ⊗ (V c2 ⊗ V c3)`, since the basis tensors
> do.

```lean
lemma fromTripleT_surjective {c1 c2 c3 : C} :
    Function.Surjective (fromTripleT (S := S) (c1 := c1) (c2 := c2) (c3 := c3))
```

**`TensorSpecies.invariants_eq_map_of_equiv`**, a lemma, [line 646](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L646).

> For a linear equivalence `e` onto the tensors intertwining `σ` with the action on tensors, the
> invariants of `σ` are the images of the invariant tensors under `e⁻¹`.

```lean
lemma invariants_eq_map_of_equiv {W : Type*} [AddCommGroup W] [Module k W]
    {σ : Representation k G W} (e : W ≃ₗ[k] S.Tensor c)
    (he : ∀ (g : G) (w : W), e (σ g w) = g • e w) :
    σ.invariants = (S.tensorRep c).invariants.map (e.symm : S.Tensor c →ₗ[k] W)
```

**`TensorSpecies.invariants_tensorRep_eq_map_of_equiv`**, a lemma, [line 660](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L660).

> For a linear equivalence `e` onto the tensors intertwining `σ` with the action on tensors, the
> invariant tensors are the images under `e` of the invariants of `σ`.

```lean
lemma invariants_tensorRep_eq_map_of_equiv {W : Type*} [AddCommGroup W] [Module k W]
    {σ : Representation k G W} (e : W ≃ₗ[k] S.Tensor c)
    (he : ∀ (g : G) (w : W), e (σ g w) = g • e w) :
    (S.tensorRep c).invariants = σ.invariants.map (e : W →ₗ[k] S.Tensor c)
```

**`TensorSpecies.fromPairTEquiv`**, a def, [line 675](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L675).

> The tensors with two indices as the tensor product of the two representations.

```lean
noncomputable def fromPairTEquiv {c1 c2 : C} : V c1 ⊗[k] V c2 ≃ₗ[k] S.Tensor ![c1, c2]
```

**`TensorSpecies.fromPairTEquiv_apply`**, a lemma, [line 679](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L679).

```lean
lemma fromPairTEquiv_apply {c1 c2 : C} (x : V c1 ⊗[k] V c2) :
    fromPairTEquiv (S := S) x = Tensor.fromPairT x
```

**`TensorSpecies.fromPairTEquiv_tprod`**, a lemma, [line 684](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L684).

> `fromPairTEquiv` intertwines the tensor product of the two representations with the action on
> tensors.

```lean
lemma fromPairTEquiv_tprod {c1 c2 : C} (g : G) (x : V c1 ⊗[k] V c2) :
    fromPairTEquiv (S := S) (((rep c1).tprod (rep c2)) g x) = g • fromPairTEquiv x
```

**`TensorSpecies.invariants_tprod_eq_span_singleton`**, a lemma, [line 690](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L690).

> The invariants of the tensor product of two representations are the line through `v` when the
> invariant tensors with two indices are the line through `fromPairT v`.

```lean
lemma invariants_tprod_eq_span_singleton {c1 c2 : C} {v : V c1 ⊗[k] V c2}
    (h : (S.tensorRep ![c1, c2]).invariants = k ∙ Tensor.fromPairT v) :
    ((rep c1).tprod (rep c2)).invariants = k ∙ v
```

**`TensorSpecies.fromTripleTEquiv`**, a def, [line 698](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L698).

> The tensors with three indices as the tensor product of the three representations.

```lean
noncomputable def fromTripleTEquiv {c1 c2 c3 : C} :
    V c1 ⊗[k] (V c2 ⊗[k] V c3) ≃ₗ[k] S.Tensor ![c1, c2, c3]
```

**`TensorSpecies.fromTripleTEquiv_apply`**, a lemma, [line 704](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L704).

```lean
lemma fromTripleTEquiv_apply {c1 c2 c3 : C} (x : V c1 ⊗[k] (V c2 ⊗[k] V c3)) :
    fromTripleTEquiv (S := S) x = Tensor.fromTripleT x
```

**`TensorSpecies.fromTripleTEquiv_tprod`**, a lemma, [line 709](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L709).

> `fromTripleTEquiv` intertwines the tensor product of the three representations with the action
> on tensors.

```lean
lemma fromTripleTEquiv_tprod {c1 c2 c3 : C} (g : G) (x : V c1 ⊗[k] (V c2 ⊗[k] V c3)) :
    fromTripleTEquiv (S := S) (((rep c1).tprod ((rep c2).tprod (rep c3))) g x)
      = g • fromTripleTEquiv x
```

**`TensorSpecies.pairIdx`**, a def, [line 715](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L715).

> The component indices of a tensor with two indices, as the pair of their labels.

```lean
def pairIdx {c1 c2 : C} : ComponentIdx (S := S) ![c1, c2] ≃ basisIdx c1 × basisIdx c2
```

**`TensorSpecies.isEquivariant_liftComponents_pair`**, a lemma, [line 725](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L725).

> The map of a family `T x y` with two indices is equivariant when each index is moved by the
> matrix of `g` in its colour, the summed index first in each factor.

```lean
lemma isEquivariant_liftComponents_pair {c1 c2 : C} {B : Type*} [AddCommGroup B] [Module k B]
    {ρ : Representation k G B} (T : basisIdx c1 → basisIdx c2 → B)
    (hT : ∀ (g : G) x y, ρ g (T x y) = ∑ x', ∑ y',
      (LinearMap.toMatrix (b c1) (b c1) (rep c1 g) x' x *
        LinearMap.toMatrix (b c2) (b c2) (rep c2 g) y' y) • T x' y') :
    S.IsEquivariant ![c1, c2] ρ (liftComponents ((fun p => T p.1 p.2) ∘ pairIdx))
```

**`TensorSpecies.range_liftComponents_pair`**, a lemma, [line 737](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L737).

> The range of the map of a family `T x y` with two indices is the span of its members.

```lean
lemma range_liftComponents_pair {c1 c2 : C} {B : Type*} [AddCommGroup B] [Module k B]
    (T : basisIdx c1 → basisIdx c2 → B) :
    LinearMap.range (liftComponents (S := S) ((fun p => T p.1 p.2) ∘ pairIdx))
      = Submodule.span k (Set.range fun m : basisIdx c1 × basisIdx c2 => T m.1 m.2)
```

**`TensorSpecies.invariants_tensorRep_pair_eq_span`**, a lemma, [line 745](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L745).

> The invariant tensors with two indices are the line through `fromPairT v` when the invariants
> of the tensor product of the two representations are the line through `v`.

```lean
lemma invariants_tensorRep_pair_eq_span {c1 c2 : C} {v : V c1 ⊗[k] V c2}
    (h : ((rep c1).tprod (rep c2)).invariants = k ∙ v) :
    (S.tensorRep ![c1, c2]).invariants = k ∙ Tensor.fromPairT v
```

**`TensorSpecies.invariants_tensorRep_pair_eq_bot`**, a lemma, [line 754](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L754).

> There are no invariant tensors with two indices but zero when the tensor product of the two
> representations has none.

```lean
lemma invariants_tensorRep_pair_eq_bot {c1 c2 : C} (h : ((rep c1).tprod (rep c2)).invariants = ⊥) :
    (S.tensorRep ![c1, c2]).invariants = ⊥
```

**`TensorSpecies.invariants_tensorRep_triple_eq_span`**, a lemma, [line 761](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L761).

> The invariant tensors with three indices are the line through `fromTripleT v` when the
> invariants of the tensor product of the three representations are the line through `v`.

```lean
lemma invariants_tensorRep_triple_eq_span {c1 c2 c3 : C} {v : V c1 ⊗[k] (V c2 ⊗[k] V c3)}
    (h : ((rep c1).tprod ((rep c2).tprod (rep c3))).invariants = k ∙ v) :
    (S.tensorRep ![c1, c2, c3]).invariants = k ∙ Tensor.fromTripleT v
```

## F. Transport of the invariant tensors

> A classification of the invariant tensors is stated once, for the colours in their canonical order
> and undualised. A reindexing `permT σ h` (F.1) and the dualisation `toDualMapAtIndex i` of an index
> (F.3) are linear equivalences commuting with the group, so they carry the invariant tensors of one
> colour list onto those of the other. A tensor is also determined by its components, and the
> components of `g • t` are the components of `t` moved by the products of the matrix entries of `g`,
> one factor per index (F.2). A classification of the coefficient functions fixed by these
> products is thereby one of the invariant tensors.

### F.1. Reindexing

**`TensorSpecies.isReindexing_append_three`**, a lemma, [line 800](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L800).

> The colours `Fin.append ![c1] (Fin.append ![c2] ![c3])` of the tensors of a product of three
> tensorial types are the plain list `![c1, c2, c3]`.

```lean
lemma isReindexing_append_three (c1 c2 c3 : C) :
    IsReindexing (Fin.append ![c1] (Fin.append ![c2] ![c3])) ![c1, c2, c3] id
```

**`TensorSpecies.permTEquiv`**, a def, [line 805](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L805).

> The reindexing `permT σ h` as a linear equivalence.

```lean
noncomputable def permTEquiv {m : ℕ} {c1 : Fin m → C} {σ : Fin m → Fin n}
    (h : IsReindexing c c1 σ) : S.Tensor c ≃ₗ[k] S.Tensor c1
```

**`TensorSpecies.invariants_tensorRep_eq_map_permT`**, a lemma, [line 813](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L813).

> Reindexing carries the invariant tensors onto the invariant tensors.

```lean
lemma invariants_tensorRep_eq_map_permT {m : ℕ} {c1 : Fin m → C} {σ : Fin m → Fin n}
    (h : IsReindexing c c1 σ) :
    (S.tensorRep c1).invariants = (S.tensorRep c).invariants.map (Tensor.permT σ h)
```

**`TensorSpecies.invariants_tensorRep_eq_span_of_permT`**, a lemma, [line 821](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L821).

> A spanning set of the invariant tensors is carried by a reindexing to one of the reindexed
> invariant tensors.

```lean
lemma invariants_tensorRep_eq_span_of_permT {m : ℕ} {c1 : Fin m → C} {σ : Fin m → Fin n}
    (h : IsReindexing c c1 σ) {s : Set (S.Tensor c)}
    (hs : (S.tensorRep c).invariants = Submodule.span k s) :
    (S.tensorRep c1).invariants = Submodule.span k (Tensor.permT σ h '' s)
```

**`TensorSpecies.invariants_tensorRep_eq_bot_of_permT`**, a lemma, [line 828](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L828).

> A reindexing of colours with no invariant tensors but zero has none either.

```lean
lemma invariants_tensorRep_eq_bot_of_permT {m : ℕ} {c1 : Fin m → C} {σ : Fin m → Fin n}
    (h : IsReindexing c c1 σ) (hb : (S.tensorRep c).invariants = ⊥) :
    (S.tensorRep c1).invariants = ⊥
```

### F.2. Components

**`TensorSpecies.componentEquiv`**, a def, [line 842](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L842).

> The components of a tensor, as a function of labels `ι` matched with the component indices
> by `e`.

```lean
noncomputable def componentEquiv {ι : Type*} (e : ComponentIdx (S := S) c ≃ ι) :
    S.Tensor c ≃ₗ[k] (ι → k)
```

**`TensorSpecies.componentEquiv_apply`**, a lemma, [line 846](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L846).

```lean
lemma componentEquiv_apply {ι : Type*} (e : ComponentIdx (S := S) c ≃ ι) (t : S.Tensor c)
    (a : ι) : componentEquiv e t a = (Tensor.basis c).repr t (e.symm a)
```

**`TensorSpecies.componentEquiv_smul`**, a lemma, [line 851](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L851).

> The components of `g • t` are those of `t` moved by `A g`, when `A g` is the product of the
> matrix entries of `g`, one factor per index.

```lean
lemma componentEquiv_smul {ι : Type*} [Fintype ι] (e : ComponentIdx (S := S) c ≃ ι)
    {A : G → ι → ι → k} (hA : ∀ g φ ψ, A g (e φ) (e ψ)
      = ∏ i, LinearMap.toMatrix (b (c i)) (b (c i)) (rep (c i) g) (φ i) (ψ i))
    (g : G) (t : S.Tensor c) :
    componentEquiv e (g • t) = fun a => ∑ a', componentEquiv e t a' * A g a a'
```

**`TensorSpecies.invariants_tensorRep_eq_map_componentEquiv`**, a lemma, [line 864](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L864).

> The invariant tensors are the images of the coefficient functions fixed by every `A g`, for
> `A g` the matrix of `g` on the components. A classification of these coefficient functions,
> as the members of a submodule `K`, is thereby one of the invariant tensors.

```lean
lemma invariants_tensorRep_eq_map_componentEquiv {ι : Type*} [Fintype ι]
    (e : ComponentIdx (S := S) c ≃ ι) {A : G → ι → ι → k}
    (hA : ∀ g φ ψ, A g (e φ) (e ψ)
      = ∏ i, LinearMap.toMatrix (b (c i)) (b (c i)) (rep (c i) g) (φ i) (ψ i))
    {K : Submodule k (ι → k)}
    (hK : ∀ x : ι → k, (∀ g, (fun a => ∑ a', x a' * A g a a') = x) ↔ x ∈ K) :
    (S.tensorRep c).invariants = K.map ((componentEquiv e).symm : (ι → k) →ₗ[k] S.Tensor c)
```

### F.3. Dualisation

**`TensorSpecies.invariants_tensorRep_update_eq_map_toDualMapAtIndex`**, a lemma, [line 895](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L895).

> Dualising the index `i` carries the invariant tensors onto those with the colour of `i`
> dualised.

```lean
lemma invariants_tensorRep_update_eq_map_toDualMapAtIndex (i : Fin n) :
    (S.tensorRep (Function.update c i (S.τ (c i)))).invariants
      = Submodule.map (Tensor.toDualMapAtIndex (S := S) (c := c) i)
        (S.tensorRep c).invariants
```

**`TensorSpecies.invariants_tensorRep_eq_bot_of_dual`**, a lemma, [line 909](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L909).

> Dualising an index of colours with no invariant tensors but zero leaves none, the colours
> of the result given up to pointwise equality as `c'`.

```lean
lemma invariants_tensorRep_eq_bot_of_dual {c' : Fin n → C} (i : Fin n)
    (hb : (S.tensorRep c).invariants = ⊥) (hc : ∀ j, Function.update c i (S.τ (c i)) j = c' j) :
    (S.tensorRep c').invariants = ⊥
```

## G. Restricting the group

> A homomorphism `φ c : H →* G` for each colour, agreeing on a colour and its dual, turns the species
> `S` into one for the group `H`, `S.restrict φ hφ`: the colour `c` carries the representation of
> `G` pulled back along `φ c`, and the contractions and units are those of `S`, which stay
> equivariant because a colour and its dual are pulled back along the same homomorphism. The
> tensors, their bases and their components are those of `S`, and `h` acts on the index `i` of a
> tensor with colours `c` as `φ (c i) h` does in `S`.

**`TensorSpecies.restrict`**, a def, [line 939](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L939).

> The species `S` for the group `H`, with the representation of each colour `c` pulled back
> along a homomorphism `φ c : H →* G`, the same for a colour and its dual.

```lean
def restrict (S : TensorSpecies k C G V basisIdx rep b) {H : Type} [Group H] (φ : C → H →* G)
    (hφ : ∀ c, φ (S.τ c) = φ c) :
    TensorSpecies k C H V basisIdx (fun c => (rep c).comp (φ c)) b
```

**`TensorSpecies.restrict_tensorRep_apply`**, a lemma, [line 958](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean#L958).

> An element `h` acts on the tensors of the restricted species as `φ (c i) h` acts on the index
> `i` in `S`.

```lean
lemma restrict_tensorRep_apply (S : TensorSpecies k C G V basisIdx rep b) {H : Type} [Group H]
    {φ : C → H →* G} {hφ : ∀ c, φ (S.τ c) = φ c} {n : ℕ} (c : Fin n → C) (h : H) :
    (S.restrict φ hφ).tensorRep c h = PiTensorProduct.map fun i => rep (c i) (φ (c i) h)
```

## Depends on

- [Dual tensors](../../../physlib/relativity/tensors/part-01/dual.md)
- [Reducing invariants modulo a stable submodule](../../mathematics/part-01/invariantreduction.md)
- [Reynolds elements for compact groups](../../mathematics/part-02/representationtheory/reynolds-compact.md)

## Proof depends on

- [Invariants and intertwining maps out of the trivial representation](../../mathematics/part-02/representationtheory/invariants.md)

## Sources

- [PhyslibAlpha/Relativity/Tensors/Equivariant.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/Equivariant.lean)
