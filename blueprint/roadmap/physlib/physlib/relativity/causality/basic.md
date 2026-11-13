---
declaration: module
origin: cited
lean: Lorentz.Vector.CausalCharacter, Lorentz.Vector.causalCharacter, Lorentz.Vector.causalCharacter_invariant, Lorentz.Vector.spaceLike_iff_norm_sq_neg, Lorentz.Vector.neg_causalCharacter_eq_self, Lorentz.Vector.interiorFutureLightCone, Lorentz.Vector.interiorPastLightCone, Lorentz.Vector.lightConeBoundary
statement: formalized
proof: formalized
---

# Physlib.Relativity.Causality.Basic

The module `Physlib.Relativity.Causality.Basic`, [Physlib/Relativity/Causality/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/Basic.lean): 18 declarations, 17 with a docstring.

## Causality of Lorentz vectors

**`Lorentz.Vector.CausalCharacter`**, an inductive, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/Basic.lean#L26).

> Classification of lorentz vectors based on their causal character.

```lean
inductive CausalCharacter
  | timeLike
  | lightLike
  | spaceLike
```

**`Lorentz.Vector.causalCharacter`**, a def, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/Basic.lean#L39).

> A Lorentz vector `p` is
> - `lightLike` if `⟪p, p⟫ₘ = 0`.
> - `timeLike` if `0 < ⟪p, p⟫ₘ`.
> - `spaceLike` if `⟪p, p⟫ₘ < 0`.
> Note that `⟪p, p⟫ₘ` is defined in the +--- convention.

```lean
def causalCharacter {d : ℕ} (p : Vector d) : CausalCharacter
```

**`Lorentz.Vector.causalCharacter_invariant`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/Basic.lean#L46).

> `causalCharacter` are invariant under an action of the Lorentz group.

```lean
lemma causalCharacter_invariant {d : ℕ} (p : Vector d) (Λ : LorentzGroup d) :
    causalCharacter (Λ • p) = causalCharacter p
```

**`Lorentz.Vector.spaceLike_iff_norm_sq_neg`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/Basic.lean#L51).

```lean
lemma spaceLike_iff_norm_sq_neg {d : ℕ} (p : Vector d) :
    causalCharacter p = CausalCharacter.spaceLike ↔ ⟪p, p⟫ₘ < 0
```

**`Lorentz.Vector.neg_causalCharacter_eq_self`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/Basic.lean#L68).

> The Lorentz vector `p` and `-p` have the same causalCharacter

```lean
lemma neg_causalCharacter_eq_self {d : ℕ} (p : Vector d) :
    causalCharacter (-p) = causalCharacter p
```

**`Lorentz.Vector.interiorFutureLightCone`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/Basic.lean#L79).

> The future light cone of a Lorentz vector `p` is defined as those
>   vectors `q` such that
> - `causalCharacter (q - p)` is `timeLike` and
> - `(q - p) (Sum.inl 0)` is positive.

```lean
def interiorFutureLightCone {d : ℕ} (p : Vector d) : Set (Vector d)
```

**`Lorentz.Vector.interiorPastLightCone`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/Basic.lean#L86).

> The backward light cone of a Lorentz vector `p` is defined as those
>   vectors `q` such that
> - `causalCharacter (q - p)` is `timeLike` and
> - `(q - p) (Sum.inl 0)` is negative.

```lean
def interiorPastLightCone {d : ℕ} (p : Vector d) : Set (Vector d)
```

**`Lorentz.Vector.lightConeBoundary`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/Basic.lean#L90).

> The light cone boundary (null surface) of a spacetime point `p`.

```lean
def lightConeBoundary {d : ℕ} (p : Vector d) : Set (Vector d)
```

**`Lorentz.Vector.futureLightConeBoundary`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/Basic.lean#L94).

> The future light cone boundary (null surface) of a spacetime point `p`.

```lean
def futureLightConeBoundary {d : ℕ} (p : Vector d) : Set (Vector d)
```

**`Lorentz.Vector.pastLightConeBoundary`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/Basic.lean#L98).

> The past light cone boundary (null surface) of a spacetime point `p`.

```lean
def pastLightConeBoundary {d : ℕ} (p : Vector d) : Set (Vector d)
```

**`Lorentz.Vector.self_mem_lightConeBoundary`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/Basic.lean#L103).

> Any point `p` lies on its own light cone boundary, as `p - p = 0` has
> zero Minkowski norm squared.

```lean
lemma self_mem_lightConeBoundary {d : ℕ} (p : Vector d) : p ∈ lightConeBoundary p
```

**`Lorentz.Vector.causallyFollows`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/Basic.lean#L107).

> A proposition which is true if `q` is in the causal future of event `p`.

```lean
def causallyFollows {d : ℕ} (p q : Vector d) : Prop
```

**`Lorentz.Vector.causallyPrecedes`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/Basic.lean#L111).

> A proposition which is true if `q` is in the causal past of event `p`.

```lean
def causallyPrecedes {d : ℕ} (p q : Vector d) : Prop
```

**`Lorentz.Vector.causallyRelated`**, a def, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/Basic.lean#L115).

> Events `p` and `q` are causally related.

```lean
def causallyRelated {d : ℕ} (p q : Vector d) : Prop
```

**`Lorentz.Vector.causallyUnrelated`**, a def, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/Basic.lean#L119).

> Events p and q are causally unrelated (spacelike separated).

```lean
def causallyUnrelated {d : ℕ} (p q : Vector d) : Prop
```

**`Lorentz.Vector.causalDiamond`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/Basic.lean#L123).

> The causal diamond between events p and q, where p is assumed to causally precede q.

```lean
def causalDiamond {d : ℕ} (p q : Vector d) : Set (Vector d)
```

**`Lorentz.Vector.isFutureDirected`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/Basic.lean#L128).

> In Minkowski spacetime with (+---) signature, we can define future-directed vectors
> as having positive time components (by convention)

```lean
def isFutureDirected {d : ℕ} (v : Vector d) : Prop
```

**`Lorentz.Vector.isPastDirected`**, a def, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/Basic.lean#L133).

> In Minkowski spacetime with (+---) signature, we can define past-directed vectors
> as having negative time components (by convention)

```lean
def isPastDirected {d : ℕ} (v : Vector d) : Prop
```

## Depends on

- [Minkowski product on Lorentz vectors](../tensors/part-03/realtensor-vector-minkowskiproduct.md)

## Sources

- [Physlib/Relativity/Causality/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/Basic.lean)
