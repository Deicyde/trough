---
declaration: module
origin: cited
lean: IsStableUnder, IsFixedBy, isStableUnder_iff_map, IsFixedBy.isStableUnder, IsFixedBy.sup, isStableUnder_bot, IsStableUnder.sup, isStableUnder_iSup
statement: formalized
proof: formalized
---

# Reducing invariants modulo a stable submodule

The module `PhyslibAlpha.Mathematics.InvariantReduction`, [PhyslibAlpha/Mathematics/InvariantReduction.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean): 43 declarations, 43 with a docstring.

> Classifying the invariants of a family of linear maps one stable submodule at a time.

## i. Overview

> Let `σ : G → B →ₗ[R] B` be a family of linear maps, indexed by an arbitrary type. No group or
> representation law is assumed. An element `x` is invariant when `σ g x = x` for every `g`, and
> a submodule is stable when every `σ g` carries it into itself.
>
> The relation `ReducesInvariantsTo σ V W` says: for every stable submodule `S`, every invariant
> of `V ⊔ S` lies in `W ⊔ S`. It is transitive, antitone in the source, monotone in the target
> and, for stable sources and a stable target, closed under joins of the source. Since an element
> of a join lies in a join over finitely many summands, the index type need not be finite:
> `ReducesInvariantsTo.iSup_of_biSup`, and with it `ReducesInvariantsTo.iSup`. A classification
> of the invariants of a family can therefore be applied one family at a time, the other families
> being kept in the stable remainder `S`. A submodule on which one map of the family acts by a
> scalar other than `1` reduces to `⊥`: `reducesInvariantsTo_bot_of_apply_eq_smul`.
>
> Such a reduction is usually proved in the quotient `B ⧸ S`. If every invariant of the image of
> `V` in `B ⧸ S` lies in the image of `W`, then every invariant of `V ⊔ S` lies in `W ⊔ S`, and
> when `W` is pointwise fixed the remainder in `S` is itself invariant:
> `IsStableUnder.exists_add_of_quotient`. The quotient hypothesis is not implied by a
> classification of the invariants of `V` alone, since the invariants of `B ⧸ S` are the classes
> `x` with `σ g x - x ∈ S`. For a pointwise-fixed `W ≤ V` a reduction describes the invariants
> of `V ⊔ S` exactly, as the elements of `W` plus an invariant element of `S`:
> `ReducesInvariantsTo.mem_sup_and_forall_eq_self_iff`.
>
> `InvariantReductionToSpan σ V` packages a reduction of `V` to the span of one fixed vector,
> the form in which the classification theorems are applied.
>
> A representation of a group `H` and a representation of `SL(2,ℂ)` on the same module are read as
> one family, `gaugeLorentzMaps`, indexed by `H ⊕ SL(2,ℂ)`. Its invariants and stable submodules
> are those of both groups, and a reduction for either group alone is a reduction for the family.

## ii. Key results

> - `ReducesInvariantsTo.iSup_of_biSup` : a reduction of every join over a finite set of indices is a
>   reduction of the join over the whole index type, which may be infinite: an element of the join
>   lies in the join over finitely many of the summands
> - `ReducesInvariantsTo.iSup` : reductions of stable submodules to a common stable target combine
>   over any index type, finite or not: `biSup` combines them over every finite set of indices, and
>   `iSup_of_biSup` passes to the whole join
> - `reducesInvariantsTo_bot_of_apply_eq_smul` : a submodule on which one map of the family acts by a
>   scalar `μ ≠ 1` reduces to `⊥`
> - `ReducesInvariantsTo.mem_sup_and_forall_eq_self_iff` : for a pointwise-fixed target inside the
>   source, the invariants of `V ⊔ S` are the elements of `W` plus an invariant element of `S`
> - `IsStableUnder.exists_add_of_quotient` : quotient to remainder: when every invariant of the image
>   of `V` in `B ⧸ S` lies in the image of a pointwise-fixed `W`, an invariant of `V ⊔ S` is an
>   element of `W` plus an invariant element of `S`
> - `ReducesInvariantsTo.mem_sup_and_gauge_lorentz_invariant_iff` : the classification endpoint for
>   a group `H` and the Lorentz group together, with the two invariances stated separately

## iv. References

> * None.

## A. Stable and fixed submodules

**`IsStableUnder`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L92).

> A submodule carried into itself by every map of the family `σ`.

```lean
def IsStableUnder (σ : G → B →ₗ[R] B) (V : Submodule R B) : Prop
```

**`IsFixedBy`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L96).

> A submodule fixed pointwise by every map of the family `σ`.

```lean
def IsFixedBy (σ : G → B →ₗ[R] B) (V : Submodule R B) : Prop
```

**`isStableUnder_iff_map`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L102).

> Stability as an inclusion of images.

```lean
lemma isStableUnder_iff_map {V : Submodule R B} :
    IsStableUnder σ V ↔ ∀ g, Submodule.map (σ g) V ≤ V
```

**`IsFixedBy.isStableUnder`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L110).

> A pointwise-fixed submodule is stable.

```lean
lemma IsFixedBy.isStableUnder {V : Submodule R B} (hV : IsFixedBy σ V) : IsStableUnder σ V
```

**`IsFixedBy.sup`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L114).

> A join of two pointwise-fixed submodules is pointwise fixed.

```lean
lemma IsFixedBy.sup {V V' : Submodule R B} (hV : IsFixedBy σ V) (hV' : IsFixedBy σ V') :
    IsFixedBy σ (V ⊔ V')
```

**`isStableUnder_bot`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L121).

> The zero submodule is stable.

```lean
lemma isStableUnder_bot : IsStableUnder σ (⊥ : Submodule R B)
```

**`IsStableUnder.sup`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L127).

> A join of two stable submodules is stable.

```lean
lemma IsStableUnder.sup {V V' : Submodule R B} (hV : IsStableUnder σ V)
    (hV' : IsStableUnder σ V') : IsStableUnder σ (V ⊔ V')
```

**`isStableUnder_iSup`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L135).

> An indexed join of stable submodules is stable. The index is a `Sort`, so this covers
> the bounded join `⨆ i ∈ s, V i`.

```lean
lemma isStableUnder_iSup {ι : Sort*} {V : ι → Submodule R B}
    (hV : ∀ i, IsStableUnder σ (V i)) : IsStableUnder σ (⨆ i, V i)
```

**`isFixedBy_span_singleton`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L142).

> The span of a fixed vector is pointwise fixed.

```lean
lemma isFixedBy_span_singleton {b : B} (hb : ∀ g, σ g b = b) : IsFixedBy σ (R ∙ b)
```

**`isFixedBy_iSup`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L148).

> An indexed join of pointwise-fixed submodules is pointwise fixed.

```lean
lemma isFixedBy_iSup {ι : Sort*} {V : ι → Submodule R B} (hV : ∀ i, IsFixedBy σ (V i)) :
    IsFixedBy σ (⨆ i, V i)
```

**`isFixedBy_span_range`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L155).

> The span of a family of fixed vectors is pointwise fixed.

```lean
lemma isFixedBy_span_range {ι : Sort*} {T : ι → B} (hT : ∀ i g, σ g (T i) = T i) :
    IsFixedBy σ (Submodule.span R (Set.range T))
```

**`isStableUnder_span_range`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L161).

> The span of a family is stable when each map sends each member into the span.

```lean
lemma isStableUnder_span_range {ι : Sort*} {T : ι → B}
    (hT : ∀ g i, σ g (T i) ∈ Submodule.span R (Set.range T)) :
    IsStableUnder σ (Submodule.span R (Set.range T))
```

**`isStableUnder_span_range_of_sum`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L170).

> The span of a finite family is stable when each map sends each member to a combination
> of the family.

```lean
lemma isStableUnder_span_range_of_sum {ι : Type*} [Fintype ι] {T : ι → B}
    (hT : ∀ g i, ∃ c : ι → R, σ g (T i) = ∑ a, c a • T a) :
    IsStableUnder σ (Submodule.span R (Set.range T))
```

**`IsStableUnder.mul`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L179).

> A product of two stable submodules of an algebra is stable under maps respecting
> multiplication.

```lean
lemma IsStableUnder.mul {R A : Type*} [CommSemiring R] [Semiring A] [Algebra R A]
    {σ : G → A →ₗ[R] A} (hσ : ∀ g (a b : A), σ g (a * b) = σ g a * σ g b)
    {V V' : Submodule R A} (hV : IsStableUnder σ V) (hV' : IsStableUnder σ V') :
    IsStableUnder σ (V * V')
```

## B. Reducing invariants

> To reduce `V₁ ⊔ V₂` to `W`, the summand `V₂` is first moved into the remainder, which needs `V₂`
> stable; the result lies in `W ⊔ (V₂ ⊔ S)`, and reducing `V₂` from there needs `W` stable.

**`ReducesInvariantsTo`**, a def, [line 206](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L206).

> Every invariant of `V ⊔ S`, for `S` a `σ`-stable submodule, lies in `W ⊔ S`.

```lean
def ReducesInvariantsTo (σ : G → B →ₗ[R] B) (V W : Submodule R B) : Prop
```

**`reducesInvariantsTo_of_le`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L210).

> A submodule reduces to any submodule containing it.

```lean
lemma reducesInvariantsTo_of_le {V W : Submodule R B} (hVW : V ≤ W) :
    ReducesInvariantsTo σ V W
```

**`ReducesInvariantsTo.mono_left`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L215).

> A reduction restricts to a smaller source.

```lean
lemma ReducesInvariantsTo.mono_left {V V' W : Submodule R B} (hP : ReducesInvariantsTo σ V' W)
    (hV : V ≤ V') : ReducesInvariantsTo σ V W
```

**`ReducesInvariantsTo.mono_right`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L220).

> A reduction extends to a larger target.

```lean
lemma ReducesInvariantsTo.mono_right {V W W' : Submodule R B}
    (hP : ReducesInvariantsTo σ V W') (hW : W' ≤ W) : ReducesInvariantsTo σ V W
```

**`ReducesInvariantsTo.trans`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L225).

> Successive reductions compose.

```lean
lemma ReducesInvariantsTo.trans {V W W' : Submodule R B} (hP : ReducesInvariantsTo σ V W)
    (hQ : ReducesInvariantsTo σ W W') : ReducesInvariantsTo σ V W'
```

**`ReducesInvariantsTo.sup`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L231).

> Reductions of `V` and of a stable `V'` to a common stable target combine to a reduction of
> `V ⊔ V'`.

```lean
lemma ReducesInvariantsTo.sup {V V' W : Submodule R B} (hP : ReducesInvariantsTo σ V W)
    (hQ : ReducesInvariantsTo σ V' W) (hV' : IsStableUnder σ V') (hW : IsStableUnder σ W) :
    ReducesInvariantsTo σ (V ⊔ V') W
```

**`ReducesInvariantsTo.biSup`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L241).

> Reductions of stable submodules to a common stable target combine over a finite set.

```lean
lemma ReducesInvariantsTo.biSup {ι : Type*} [DecidableEq ι] {V : ι → Submodule R B}
    {W : Submodule R B} (hP : ∀ i, ReducesInvariantsTo σ (V i) W)
    (hV : ∀ i, IsStableUnder σ (V i)) (hW : IsStableUnder σ W) (s : Finset ι) :
    ReducesInvariantsTo σ (⨆ i ∈ s, V i) W
```

**`ReducesInvariantsTo.iSup_of_biSup`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L255).

> A reduction of every join over a finite set of indices is a reduction of the join over the
> whole index type, which may be infinite. An element of the join lies in the join over finitely
> many of the summands. No stability is assumed of the summands or of the target; the remainder
> is stable, as in every reduction.

```lean
lemma ReducesInvariantsTo.iSup_of_biSup {ι : Type*} {V : ι → Submodule R B} {W : Submodule R B}
    (hP : ∀ s : Finset ι, ReducesInvariantsTo σ (⨆ i ∈ s, V i) W) :
    ReducesInvariantsTo σ (⨆ i, V i) W
```

**`ReducesInvariantsTo.iSup`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L266).

> Reductions of stable submodules to a common stable target combine over any index type,
> finite or not. `biSup` combines them over every finite set of indices, and
> `iSup_of_biSup` passes to the whole join.

```lean
lemma ReducesInvariantsTo.iSup {ι : Type*} {V : ι → Submodule R B} {W : Submodule R B}
    (hP : ∀ i, ReducesInvariantsTo σ (V i) W) (hV : ∀ i, IsStableUnder σ (V i))
    (hW : IsStableUnder σ W) : ReducesInvariantsTo σ (⨆ i, V i) W
```

**`ReducesInvariantsTo.comp`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L274).

> A reduction for the subfamily `σ ∘ ι` is a reduction for `σ`. An invariant of `σ` is an
> invariant of the subfamily, and a `σ`-stable submodule is stable under the subfamily.

```lean
lemma ReducesInvariantsTo.comp {G' : Type*} (ι : G' → G) {V W : Submodule R B}
    (hP : ReducesInvariantsTo (fun g' => σ (ι g')) V W) : ReducesInvariantsTo σ V W
```

**`reducesInvariantsTo_bot_of_apply_eq_smul`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L287).

> A submodule on which one map of the family acts by a scalar `μ ≠ 1` reduces to `⊥`. An
> invariant `v + s` of `V ⊔ S` has `(μ - 1) • v = s - σ g s`, which lies in `S`, and so does
> `v`. Of the stability of `S` only stability under `σ g` is used.

```lean
lemma reducesInvariantsTo_bot_of_apply_eq_smul (g : G) {μ : K} (hμ : μ ≠ 1)
    {V : Submodule K B} (hV : ∀ v ∈ V, σ g v = μ • v) : ReducesInvariantsTo σ V ⊥
```

## C. Reduction through a quotient

> For a `σ`-stable `S`, the maps `S.mapQ S (σ g) _` act on `B ⧸ S`. The hypotheses below classify
> invariants of that action on the image of the source, which is where a classification valid in
> every module is applied.

**`IsStableUnder.mem_sup_of_quotient`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L319).

> An invariant of `V ⊔ S` lies in `W ⊔ S` when every invariant of the image of `V` in
> `B ⧸ S` lies in the image of `W`.

```lean
lemma IsStableUnder.mem_sup_of_quotient (hS : IsStableUnder σ S)
    (hclass : ∀ x ∈ V.map S.mkQ, (∀ g, S.mapQ S (σ g) (hS g) x = x) → x ∈ W.map S.mkQ)
    {x : B} (hx : x ∈ V ⊔ S) (hinv : ∀ g, σ g x = x) : x ∈ W ⊔ S
```

**`reducesInvariantsTo_of_quotient`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L327).

> `V` reduces to `W` when, for every stable `S`, every invariant of the image of `V` in
> `B ⧸ S` lies in the image of `W`.

```lean
lemma reducesInvariantsTo_of_quotient
    (hclass : ∀ S : Submodule R B, ∀ hS : IsStableUnder σ S, ∀ x ∈ V.map S.mkQ,
      (∀ g, S.mapQ S (σ g) (hS g) x = x) → x ∈ W.map S.mkQ) :
    ReducesInvariantsTo σ V W
```

**`IsFixedBy.exists_add_of_mem_sup`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L335).

> An invariant of `W ⊔ S`, for `W` pointwise fixed, is an element of `W` plus an invariant
> element of `S`.

```lean
lemma IsFixedBy.exists_add_of_mem_sup (hW : IsFixedBy σ W) {x : B} (hx : x ∈ W ⊔ S)
    (hinv : ∀ g, σ g x = x) : ∃ w ∈ W, ∃ y ∈ S, x = w + y ∧ ∀ g, σ g y = y
```

**`ReducesInvariantsTo.mem_sup_and_forall_eq_self_iff`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L345).

> A reduction of `V` to a pointwise-fixed `W ≤ V` describes the invariants of `V ⊔ S`, for
> `S` stable, exactly. They are the elements of `W` plus an invariant element of `S`. This is
> the form in which a classification is stated.

```lean
lemma ReducesInvariantsTo.mem_sup_and_forall_eq_self_iff (hP : ReducesInvariantsTo σ V W)
    (hWV : W ≤ V) (hW : IsFixedBy σ W) (hS : IsStableUnder σ S) (x : B) :
    (x ∈ V ⊔ S ∧ ∀ g, σ g x = x) ↔ ∃ y ∈ S, (∀ g, σ g y = y) ∧ x - y ∈ W
```

**`IsStableUnder.exists_add_of_quotient`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L359).

> Quotient to remainder. When every invariant of the image of `V` in `B ⧸ S` lies in the
> image of a pointwise-fixed `W`, an invariant of `V ⊔ S` is an element of `W` plus an
> invariant element of `S`.

```lean
lemma IsStableUnder.exists_add_of_quotient (hS : IsStableUnder σ S) (hW : IsFixedBy σ W)
    (hclass : ∀ x ∈ V.map S.mkQ, (∀ g, S.mapQ S (σ g) (hS g) x = x) → x ∈ W.map S.mkQ)
    {x : B} (hx : x ∈ V ⊔ S) (hinv : ∀ g, σ g x = x) :
    ∃ w ∈ W, ∃ y ∈ S, x = w + y ∧ ∀ g, σ g y = y
```

## D. Reduction to the span of one vector

**`InvariantReductionToSpan`**, a structure, [line 380](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L380).

> A stable submodule `V` together with a fixed vector such that, for every stable `S`, every
> invariant of `V ⊔ S` is a multiple of that vector plus an element of `S`. The vector need not
> be nonzero or lie in `V`.

```lean
structure InvariantReductionToSpan (σ : G → B →ₗ[R] B) (V : Submodule R B) where
  /-- The vector whose span receives the invariants of `V`. -/
  spanningVector : B
  /-- The submodule is stable. -/
  stable : IsStableUnder σ V
  /-- The spanning vector is invariant. -/
  spanningVector_fixed : ∀ g, σ g spanningVector = spanningVector
  /-- An invariant of `V ⊔ S`, for `S` stable, is a multiple of the spanning vector plus an
    element of `S`. -/
  reduce : ∀ S : Submodule R B, IsStableUnder σ S → ∀ x ∈ V ⊔ S, (∀ g, σ g x = x) →
    ∃ c : R, ∃ y ∈ S, x = c • spanningVector + y
```

**`InvariantReductionToSpan.reducesInvariantsTo`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L397).

> The submodule reduces to the span of the spanning vector.

```lean
lemma reducesInvariantsTo (r : InvariantReductionToSpan σ V) :
    ReducesInvariantsTo σ V (R ∙ r.spanningVector)
```

**`InvariantReductionToSpan.reducesInvariantsTo_iSup`**, a lemma, [line 405](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L405).

> A family of reductions to spans, over any index type, reduces the join of the submodules to
> the span of the spanning vectors.

```lean
lemma reducesInvariantsTo_iSup {κ : Type*} {V : κ → Submodule R B}
    (r : ∀ k, InvariantReductionToSpan σ (V k)) :
    ReducesInvariantsTo σ (⨆ k, V k)
      (Submodule.span R (Set.range fun k => (r k).spanningVector))
```

**`InvariantReductionToSpan.ofFixed`**, a def, [line 416](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L416).

> The span of a fixed vector reduces to itself.

```lean
def ofFixed (b : B) (hb : ∀ g, σ g b = b) :
    InvariantReductionToSpan σ (R ∙ b)
```

**`InvariantReductionToSpan.ofFixedFamily`**, a def, [line 428](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L428).

> The span of a nonempty family whose members all equal one fixed vector reduces to the
> span of that vector.

```lean
def ofFixedFamily {ι : Type*} [Nonempty ι] {T : ι → B} (b : B)
    (hTb : ∀ i, T i = b) (hb : ∀ g, σ g b = b) :
    InvariantReductionToSpan σ (Submodule.span R (Set.range T))
```

## E. A group together with the Lorentz group

> A representation of a group `H` and a representation of `SL(2,ℂ)` on the same module are read
> as a single family of linear maps, `gaugeLorentzMaps`, indexed by the disjoint union
> `H ⊕ SL(2,ℂ)`. Its invariants are the elements fixed by both groups, and its stable submodules
> are those stable under both. A reduction for `H` or for the Lorentz group alone is a reduction
> for the family by `ReducesInvariantsTo.comp`.

**`gaugeLorentzMaps`**, a def, [line 463](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L463).

> A representation of `H` and one of `SL(2,ℂ)` on the same module, read as a single family of
> linear maps indexed by the disjoint union of the two groups.

```lean
def gaugeLorentzMaps : H ⊕ SL(2,ℂ) → B →ₗ[ℂ] B
```

**`isStableUnder_gaugeLorentzMaps_iff`**, a lemma, [line 470](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L470).

> A submodule stable under both groups is stable under the combined family, and
> conversely.

```lean
lemma isStableUnder_gaugeLorentzMaps_iff {V : Submodule ℂ B} :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) V
      ↔ (∀ g : H, ∀ y ∈ V, repGauge g y ∈ V) ∧ ∀ Λ : SL(2,ℂ), ∀ y ∈ V, repLorentz Λ y ∈ V
```

**`forall_gaugeLorentzMaps_eq_self_iff`**, a lemma, [line 480](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L480).

> An element fixed by both groups is fixed by the combined family, and conversely.

```lean
lemma forall_gaugeLorentzMaps_eq_self_iff {x : B} :
    (∀ p, gaugeLorentzMaps repGauge repLorentz p x = x)
      ↔ (∀ g : H, repGauge g x = x) ∧ ∀ Λ : SL(2,ℂ), repLorentz Λ x = x
```

**`isFixedBy_gaugeLorentzMaps_iff`**, a lemma, [line 491](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L491).

> A submodule fixed pointwise by both groups is fixed pointwise by the combined family, and
> conversely.

```lean
lemma isFixedBy_gaugeLorentzMaps_iff {V : Submodule ℂ B} :
    IsFixedBy (gaugeLorentzMaps repGauge repLorentz) V
      ↔ (∀ g : H, ∀ y ∈ V, repGauge g y = y) ∧ ∀ Λ : SL(2,ℂ), ∀ y ∈ V, repLorentz Λ y = y
```

**`ReducesInvariantsTo.mem_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 502](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L502).

> The endpoint `ReducesInvariantsTo.mem_sup_and_forall_eq_self_iff` for the two groups
> together, with the two invariances and the two stabilities stated separately.

```lean
lemma ReducesInvariantsTo.mem_sup_and_gauge_lorentz_invariant_iff {V W S : Submodule ℂ B}
    (hP : ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) V W) (hWV : W ≤ V)
    (hW : IsFixedBy (gaugeLorentzMaps repGauge repLorentz) W)
    (hS : ∀ g : H, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ Λ : SL(2,ℂ), ∀ y ∈ S, repLorentz Λ y ∈ S) (x : B) :
    (x ∈ V ⊔ S ∧ (∀ g : H, repGauge g x = x) ∧ ∀ Λ : SL(2,ℂ), repLorentz Λ x = x)
      ↔ ∃ y ∈ S, (∀ g : H, repGauge g y = y)
          ∧ (∀ Λ : SL(2,ℂ), repLorentz Λ y = y) ∧ x - y ∈ W
```

**`ReducesInvariantsTo.ofGauge`**, a lemma, [line 514](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L514).

> A reduction for `H` is a reduction for the two groups together.

```lean
lemma ReducesInvariantsTo.ofGauge {V W : Submodule ℂ B}
    (hP : ReducesInvariantsTo (fun g : H => repGauge g) V W) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) V W
```

**`ReducesInvariantsTo.ofLorentz`**, a lemma, [line 520](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L520).

> A Lorentz reduction is a reduction for the two groups together.

```lean
lemma ReducesInvariantsTo.ofLorentz {V W : Submodule ℂ B}
    (hP : ReducesInvariantsTo (fun Λ : SL(2,ℂ) => repLorentz Λ) V W) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) V W
```

**`gaugeLorentzMaps_mul`**, a lemma, [line 536](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean#L536).

> The two groups read as one family of maps respect multiplication, each of the two
> representations doing so.

```lean
lemma gaugeLorentzMaps_mul
    (hG : ∀ (g : H) (b₁ b₂ : B), repGauge g (b₁ * b₂) = repGauge g b₁ * repGauge g b₂)
    (hL : ∀ (Λ : SL(2,ℂ)) (b₁ b₂ : B),
      repLorentz Λ (b₁ * b₂) = repLorentz Λ b₁ * repLorentz Λ b₂)
    (p : H ⊕ SL(2,ℂ)) (a b : B) :
    gaugeLorentzMaps repGauge repLorentz p (a * b)
      = gaugeLorentzMaps repGauge repLorentz p a * gaugeLorentzMaps repGauge repLorentz p b
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/InvariantReduction.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/InvariantReduction.lean)
