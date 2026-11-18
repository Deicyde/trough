---
declaration: module
origin: cited
lean: IsStableUnder, IsFixedBy, isStableUnder_iff_map, IsFixedBy.isStableUnder, IsFixedBy.sup, isStableUnder_bot, IsStableUnder.sup, isStableUnder_iSup
statement: formalized
proof: formalized
---

# Reducing invariants modulo a stable submodule

The module `PhyslibAlpha.Mathematics.InvariantReduction`, [PhyslibAlpha/Mathematics/InvariantReduction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean): 41 declarations, 41 with a docstring.

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
> For a finite family moved by matrices, `σ g (T l) = ∑ a, M g a l • T a`, the quotient
> hypothesis reduces to a finite problem about coefficient vectors: the law holds again for the
> classes of the members in `B ⧸ S`, so an invariant there is the combination of a coefficient
> vector fixed by every `M g`, and any classification of the fixed coefficient vectors gives a
> reduction, `reducesInvariantsTo_of_mulVec_eq`.

## ii. Key results

> - `ReducesInvariantsTo.iSup_of_biSup` : a reduction of every join over a finite set of indices is a
>   reduction of the join over the whole index type, which may be infinite: an element of the join
>   lies in the join over finitely many of the summands
> - `ReducesInvariantsTo.iSup` : reductions of stable submodules to a common stable target combine
>   over any index type, finite or not: `biSup` combines them over every finite set of indices, and
>   `iSup_of_biSup` passes to the whole join
> - `reducesInvariantsTo_bot_of_apply_eq_smul` : a submodule on which one map of the family acts by a
>   scalar `μ ≠ 1` reduces to `⊥`
> - `ReducesInvariantsTo.mem_sup_and_forall_eq_self_iff`
> - `IsStableUnder.exists_add_of_quotient` : quotient to remainder: when every invariant of the image
>   of `V` in `B ⧸ S` lies in the image of a pointwise-fixed `W`, an invariant of `V ⊔ S` is an
>   element of `W` plus an invariant element of `S`
> - `reducesInvariantsTo_of_mulVec_eq` : a family moved by matrices whose conjugate transposes are
>   among them reduces to the combinations of any submodule `E` of coefficient vectors containing
>   every vector fixed by all the matrices

## iv. References

> * None.

## A. Stable and fixed submodules

**`IsStableUnder`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L90).

> A submodule carried into itself by every map of the family `σ`.

```lean
def IsStableUnder (σ : G → B →ₗ[R] B) (V : Submodule R B) : Prop
```

**`IsFixedBy`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L94).

> A submodule fixed pointwise by every map of the family `σ`.

```lean
def IsFixedBy (σ : G → B →ₗ[R] B) (V : Submodule R B) : Prop
```

**`isStableUnder_iff_map`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L100).

> Stability as an inclusion of images.

```lean
lemma isStableUnder_iff_map {V : Submodule R B} :
    IsStableUnder σ V ↔ ∀ g, Submodule.map (σ g) V ≤ V
```

**`IsFixedBy.isStableUnder`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L108).

> A pointwise-fixed submodule is stable.

```lean
lemma IsFixedBy.isStableUnder {V : Submodule R B} (hV : IsFixedBy σ V) : IsStableUnder σ V
```

**`IsFixedBy.sup`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L112).

> A join of two pointwise-fixed submodules is pointwise fixed.

```lean
lemma IsFixedBy.sup {V V' : Submodule R B} (hV : IsFixedBy σ V) (hV' : IsFixedBy σ V') :
    IsFixedBy σ (V ⊔ V')
```

**`isStableUnder_bot`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L119).

> The zero submodule is stable.

```lean
lemma isStableUnder_bot : IsStableUnder σ (⊥ : Submodule R B)
```

**`IsStableUnder.sup`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L125).

> A join of two stable submodules is stable.

```lean
lemma IsStableUnder.sup {V V' : Submodule R B} (hV : IsStableUnder σ V)
    (hV' : IsStableUnder σ V') : IsStableUnder σ (V ⊔ V')
```

**`isStableUnder_iSup`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L133).

> An indexed join of stable submodules is stable. The index is a `Sort`, so this covers
> the bounded join `⨆ i ∈ s, V i`.

```lean
lemma isStableUnder_iSup {ι : Sort*} {V : ι → Submodule R B}
    (hV : ∀ i, IsStableUnder σ (V i)) : IsStableUnder σ (⨆ i, V i)
```

**`isFixedBy_span_singleton`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L140).

> The span of a fixed vector is pointwise fixed.

```lean
lemma isFixedBy_span_singleton {b : B} (hb : ∀ g, σ g b = b) : IsFixedBy σ (R ∙ b)
```

**`isFixedBy_iSup`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L146).

> An indexed join of pointwise-fixed submodules is pointwise fixed.

```lean
lemma isFixedBy_iSup {ι : Sort*} {V : ι → Submodule R B} (hV : ∀ i, IsFixedBy σ (V i)) :
    IsFixedBy σ (⨆ i, V i)
```

**`isFixedBy_span_range`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L153).

> The span of a family of fixed vectors is pointwise fixed.

```lean
lemma isFixedBy_span_range {ι : Sort*} {T : ι → B} (hT : ∀ i g, σ g (T i) = T i) :
    IsFixedBy σ (Submodule.span R (Set.range T))
```

**`isStableUnder_span_range`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L159).

> The span of a family is stable when each map sends each member into the span.

```lean
lemma isStableUnder_span_range {ι : Sort*} {T : ι → B}
    (hT : ∀ g i, σ g (T i) ∈ Submodule.span R (Set.range T)) :
    IsStableUnder σ (Submodule.span R (Set.range T))
```

**`isStableUnder_span_range_of_sum`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L168).

> The span of a finite family is stable when each map sends each member to a combination
> of the family.

```lean
lemma isStableUnder_span_range_of_sum {ι : Type*} [Fintype ι] {T : ι → B}
    (hT : ∀ g i, ∃ c : ι → R, σ g (T i) = ∑ a, c a • T a) :
    IsStableUnder σ (Submodule.span R (Set.range T))
```

**`IsStableUnder.mul`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L177).

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

**`ReducesInvariantsTo`**, a def, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L204).

> Every invariant of `V ⊔ S`, for `S` a `σ`-stable submodule, lies in `W ⊔ S`.

```lean
def ReducesInvariantsTo (σ : G → B →ₗ[R] B) (V W : Submodule R B) : Prop
```

**`reducesInvariantsTo_of_le`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L208).

> A submodule reduces to any submodule containing it.

```lean
lemma reducesInvariantsTo_of_le {V W : Submodule R B} (hVW : V ≤ W) :
    ReducesInvariantsTo σ V W
```

**`ReducesInvariantsTo.mono_left`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L213).

> A reduction restricts to a smaller source.

```lean
lemma ReducesInvariantsTo.mono_left {V V' W : Submodule R B} (hP : ReducesInvariantsTo σ V' W)
    (hV : V ≤ V') : ReducesInvariantsTo σ V W
```

**`ReducesInvariantsTo.mono_right`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L218).

> A reduction extends to a larger target.

```lean
lemma ReducesInvariantsTo.mono_right {V W W' : Submodule R B}
    (hP : ReducesInvariantsTo σ V W') (hW : W' ≤ W) : ReducesInvariantsTo σ V W
```

**`ReducesInvariantsTo.trans`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L223).

> Successive reductions compose.

```lean
lemma ReducesInvariantsTo.trans {V W W' : Submodule R B} (hP : ReducesInvariantsTo σ V W)
    (hQ : ReducesInvariantsTo σ W W') : ReducesInvariantsTo σ V W'
```

**`ReducesInvariantsTo.sup`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L229).

> Reductions of `V` and of a stable `V'` to a common stable target combine to a reduction of
> `V ⊔ V'`.

```lean
lemma ReducesInvariantsTo.sup {V V' W : Submodule R B} (hP : ReducesInvariantsTo σ V W)
    (hQ : ReducesInvariantsTo σ V' W) (hV' : IsStableUnder σ V') (hW : IsStableUnder σ W) :
    ReducesInvariantsTo σ (V ⊔ V') W
```

**`ReducesInvariantsTo.biSup`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L239).

> Reductions of stable submodules to a common stable target combine over a finite set.

```lean
lemma ReducesInvariantsTo.biSup {ι : Type*} [DecidableEq ι] {V : ι → Submodule R B}
    {W : Submodule R B} (hP : ∀ i, ReducesInvariantsTo σ (V i) W)
    (hV : ∀ i, IsStableUnder σ (V i)) (hW : IsStableUnder σ W) (s : Finset ι) :
    ReducesInvariantsTo σ (⨆ i ∈ s, V i) W
```

**`ReducesInvariantsTo.iSup_of_biSup`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L253).

> A reduction of every join over a finite set of indices is a reduction of the join over the
> whole index type, which may be infinite: an element of the join lies in the join over finitely
> many of the summands. No stability is assumed of the summands or of the target; the remainder
> is stable, as in every reduction.

```lean
lemma ReducesInvariantsTo.iSup_of_biSup {ι : Type*} {V : ι → Submodule R B} {W : Submodule R B}
    (hP : ∀ s : Finset ι, ReducesInvariantsTo σ (⨆ i ∈ s, V i) W) :
    ReducesInvariantsTo σ (⨆ i, V i) W
```

**`ReducesInvariantsTo.iSup`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L264).

> Reductions of stable submodules to a common stable target combine over any index type,
> finite or not: `biSup` combines them over every finite set of indices, and
> `iSup_of_biSup` passes to the whole join.

```lean
lemma ReducesInvariantsTo.iSup {ι : Type*} {V : ι → Submodule R B} {W : Submodule R B}
    (hP : ∀ i, ReducesInvariantsTo σ (V i) W) (hV : ∀ i, IsStableUnder σ (V i))
    (hW : IsStableUnder σ W) : ReducesInvariantsTo σ (⨆ i, V i) W
```

**`ReducesInvariantsTo.comp`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L272).

> A reduction for the subfamily `σ ∘ ι` is a reduction for `σ`: an invariant of `σ` is an
> invariant of the subfamily, and a `σ`-stable submodule is stable under the subfamily.

```lean
lemma ReducesInvariantsTo.comp {G' : Type*} (ι : G' → G) {V W : Submodule R B}
    (hP : ReducesInvariantsTo (fun g' => σ (ι g')) V W) : ReducesInvariantsTo σ V W
```

**`reducesInvariantsTo_bot_of_apply_eq_smul`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L285).

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

**`IsStableUnder.mem_sup_of_quotient`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L317).

> An invariant of `V ⊔ S` lies in `W ⊔ S` when every invariant of the image of `V` in
> `B ⧸ S` lies in the image of `W`.

```lean
lemma IsStableUnder.mem_sup_of_quotient (hS : IsStableUnder σ S)
    (hclass : ∀ x ∈ V.map S.mkQ, (∀ g, S.mapQ S (σ g) (hS g) x = x) → x ∈ W.map S.mkQ)
    {x : B} (hx : x ∈ V ⊔ S) (hinv : ∀ g, σ g x = x) : x ∈ W ⊔ S
```

**`reducesInvariantsTo_of_quotient`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L325).

> `V` reduces to `W` when, for every stable `S`, every invariant of the image of `V` in
> `B ⧸ S` lies in the image of `W`.

```lean
lemma reducesInvariantsTo_of_quotient
    (hclass : ∀ S : Submodule R B, ∀ hS : IsStableUnder σ S, ∀ x ∈ V.map S.mkQ,
      (∀ g, S.mapQ S (σ g) (hS g) x = x) → x ∈ W.map S.mkQ) :
    ReducesInvariantsTo σ V W
```

**`IsFixedBy.exists_add_of_mem_sup`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L333).

> An invariant of `W ⊔ S`, for `W` pointwise fixed, is an element of `W` plus an invariant
> element of `S`.

```lean
lemma IsFixedBy.exists_add_of_mem_sup (hW : IsFixedBy σ W) {x : B} (hx : x ∈ W ⊔ S)
    (hinv : ∀ g, σ g x = x) : ∃ w ∈ W, ∃ y ∈ S, x = w + y ∧ ∀ g, σ g y = y
```

**`ReducesInvariantsTo.mem_sup_and_forall_eq_self_iff`**, a lemma, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L343).

> A reduction of `V` to a pointwise-fixed `W ≤ V` describes the invariants of `V ⊔ S`, for
> `S` stable, exactly: they are the elements of `W` plus an invariant element of `S`. This is
> the form in which a classification is stated.

```lean
lemma ReducesInvariantsTo.mem_sup_and_forall_eq_self_iff (hP : ReducesInvariantsTo σ V W)
    (hWV : W ≤ V) (hW : IsFixedBy σ W) (hS : IsStableUnder σ S) (x : B) :
    (x ∈ V ⊔ S ∧ ∀ g, σ g x = x) ↔ ∃ y ∈ S, (∀ g, σ g y = y) ∧ x - y ∈ W
```

**`IsStableUnder.exists_add_of_quotient`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L357).

> Quotient to remainder: when every invariant of the image of `V` in `B ⧸ S` lies in the
> image of a pointwise-fixed `W`, an invariant of `V ⊔ S` is an element of `W` plus an
> invariant element of `S`.

```lean
lemma IsStableUnder.exists_add_of_quotient (hS : IsStableUnder σ S) (hW : IsFixedBy σ W)
    (hclass : ∀ x ∈ V.map S.mkQ, (∀ g, S.mapQ S (σ g) (hS g) x = x) → x ∈ W.map S.mkQ)
    {x : B} (hx : x ∈ V ⊔ S) (hinv : ∀ g, σ g x = x) :
    ∃ w ∈ W, ∃ y ∈ S, x = w + y ∧ ∀ g, σ g y = y
```

**`IsStableUnder.exists_smul_add_of_quotient`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L366).

> Quotient to remainder for a single fixed vector `v`: when every invariant of the image of
> `V` in `B ⧸ S` is a multiple of the class of `v`, an invariant of `V ⊔ S` is a multiple of
> `v` plus an invariant element of `S`.

```lean
lemma IsStableUnder.exists_smul_add_of_quotient (hS : IsStableUnder σ S) {v : B}
    (hv : ∀ g, σ g v = v)
    (hclass : ∀ x ∈ V.map S.mkQ, (∀ g, S.mapQ S (σ g) (hS g) x = x) → ∃ c : R, x = c • S.mkQ v)
    {x : B} (hx : x ∈ V ⊔ S) (hinv : ∀ g, σ g x = x) :
    ∃ c : R, ∃ y ∈ S, x = c • v + y ∧ ∀ g, σ g y = y
```

## D. Reduction to the span of one vector

**`InvariantReductionToSpan`**, a structure, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L394).

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

**`InvariantReductionToSpan.reducesInvariantsTo`**, a lemma, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L411).

> The submodule reduces to the span of the spanning vector.

```lean
lemma reducesInvariantsTo (r : InvariantReductionToSpan σ V) :
    ReducesInvariantsTo σ V (R ∙ r.spanningVector)
```

**`InvariantReductionToSpan.reducesInvariantsTo_iSup`**, a lemma, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L419).

> A family of reductions to spans, over any index type, reduces the join of the submodules to
> the span of the spanning vectors.

```lean
lemma reducesInvariantsTo_iSup {κ : Type*} {V : κ → Submodule R B}
    (r : ∀ k, InvariantReductionToSpan σ (V k)) :
    ReducesInvariantsTo σ (⨆ k, V k)
      (Submodule.span R (Set.range fun k => (r k).spanningVector))
```

**`InvariantReductionToSpan.ofReducesInvariantsTo`**, a def, [line 430](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L430).

> The reduction of a stable submodule to the span of a fixed vector.

```lean
def ofReducesInvariantsTo (hV : IsStableUnder σ V) (v : B) (hv : ∀ g, σ g v = v)
    (h : ReducesInvariantsTo σ V (R ∙ v)) : InvariantReductionToSpan σ V
```

**`InvariantReductionToSpan.ofFixed`**, a def, [line 441](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L441).

> The span of a fixed vector reduces to itself.

```lean
def ofFixed (b : B) (hb : ∀ g, σ g b = b) :
    InvariantReductionToSpan σ (R ∙ b)
```

**`InvariantReductionToSpan.ofFixedFamily`**, a def, [line 453](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L453).

> The span of a nonempty family whose members all equal one fixed vector reduces to the
> span of that vector.

```lean
def ofFixedFamily {ι : Type*} [Nonempty ι] {T : ι → B} (b : B)
    (hTb : ∀ i, T i = b) (hb : ∀ g, σ g b = b) :
    InvariantReductionToSpan σ (Submodule.span R (Set.range T))
```

## E. Families moved by matrices

> A finite family `T : ι → B` is moved by matrices when `σ g (T l) = ∑ a, M g a l • T a`, the
> summed index in the row slot. For a stable `S` the classes of the members in `B ⧸ S` obey the
> same law (`Submodule.mapQ_mkQ_eq_sum_smul`), and that law is all that
> `Fintype.exists_mulVec_eq_of_conjTranspose_mem` needs: an invariant of the image of the span in
> `B ⧸ S` is the combination of a coefficient vector fixed by every `M g`. A description of the
> fixed coefficient vectors, a submodule `E` containing them all, therefore reduces the span to
> the combinations of `E`. What is classified is coefficient vectors, which do not depend on `S`;
> no classification of invariants of `B` is assumed to descend to `B ⧸ S`.

**`Submodule.mapQ_mkQ_eq_sum_smul`**, a lemma, [line 488](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L488).

> A map moving each member of a family by a matrix moves their classes modulo a submodule
> that it preserves by the same matrix.

```lean
lemma Submodule.mapQ_mkQ_eq_sum_smul {R B ι : Type*} [Ring R] [AddCommGroup B] [Module R B]
    [Fintype ι] (S : Submodule R B) {f : B →ₗ[R] B} (hS : ∀ y ∈ S, f y ∈ S) {T : ι → B}
    {M : Matrix ι ι R} {l : ι} (hf : f (T l) = ∑ a, M a l • T a) :
    S.mapQ S f hS (S.mkQ (T l)) = ∑ a, M a l • S.mkQ (T a)
```

**`reducesInvariantsTo_of_mulVec_eq`**, a lemma, [line 500](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L500).

> A family moved by matrices whose conjugate transposes are among them reduces to the
> combinations of any submodule `E` of coefficient vectors containing every vector fixed by
> all the matrices.

```lean
lemma reducesInvariantsTo_of_mulVec_eq (T : ι → B) (M : G → Matrix ι ι ℂ)
    (hT : ∀ g l, σ g (T l) = ∑ a, M g a l • T a) (hM : ∀ g, ∃ g', M g' = (M g)ᴴ)
    (E : Submodule ℂ (ι → ℂ)) (hE : ∀ c, (∀ g, M g *ᵥ c = c) → c ∈ E) :
    ReducesInvariantsTo σ (Submodule.span ℂ (Set.range T))
      (E.map (Fintype.linearCombination ℂ T))
```

**`reducesInvariantsTo_bot_of_mulVec_eq`**, a lemma, [line 517](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L517).

> The form of `reducesInvariantsTo_of_mulVec_eq` when no nonzero coefficient vector is
> fixed: the span reduces to `⊥`.

```lean
lemma reducesInvariantsTo_bot_of_mulVec_eq (T : ι → B) (M : G → Matrix ι ι ℂ)
    (hT : ∀ g l, σ g (T l) = ∑ a, M g a l • T a) (hM : ∀ g, ∃ g', M g' = (M g)ᴴ)
    (hE : ∀ c, (∀ g, M g *ᵥ c = c) → c = 0) :
    ReducesInvariantsTo σ (Submodule.span ℂ (Set.range T)) ⊥
```

**`reducesInvariantsTo_span_singleton_of_mulVec_eq`**, a lemma, [line 526](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean#L526).

> The form of `reducesInvariantsTo_of_mulVec_eq` when every fixed coefficient vector is a
> multiple of `e`: the span reduces to the span of the combination with coefficients `e`.

```lean
lemma reducesInvariantsTo_span_singleton_of_mulVec_eq (T : ι → B) (M : G → Matrix ι ι ℂ)
    (hT : ∀ g l, σ g (T l) = ∑ a, M g a l • T a) (hM : ∀ g, ∃ g', M g' = (M g)ᴴ)
    (e : ι → ℂ) (hE : ∀ c, (∀ g, M g *ᵥ c = c) → ∃ z : ℂ, c = z • e) :
    ReducesInvariantsTo σ (Submodule.span ℂ (Set.range T)) (ℂ ∙ ∑ i, e i • T i)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [Finite linear combinations under a linear map](linearcombination.md)

## Sources

- [PhyslibAlpha/Mathematics/InvariantReduction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/InvariantReduction.lean)
