---
catalog: module
lean: Relation.ofSMul, Relation.ofSMul_diamond, Relation.ofSMul_preserves_iff, Relation.ofSMul_preserves_mem, Relation.ofSMul_mem_of_mem, Cslib.Logic.Modal.Proposition.ofSMul_diamond_denotation, Cslib.Logic.Modal.Proposition.ofSMul_diamond_and_equiv
statement: formalized
proof: formalized
---

# Modal Logic for scalar multiplication (SMul)

`Cslib.Logics.Modal.Unimodal.Lean.SMul`, in [Cslib/Logics/Modal/Unimodal/Lean/SMul.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Lean/SMul.lean), by Fabrizio Montesi.

> Any scalar multiplication operation `•` induces an accessibility relation where two elements are
> related if the latter is the result of applying a scalar multiplication to the former.
>
> Properties of the operator translate to properties of the relation, for example a semigroup action
> on a commutative semigroup yields a relation with the `Diamond` property. This bridge allows for
> studying properties of the operation using modal logic.

`Relation.ofSMul` (definition, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Lean/SMul.lean#L28))

> The accessibility relation induced by a scalar multiplication operation: `x` is related to `y`
> when there exists `m` such that `m • x = y`.

```lean
def ofSMul (M α : Type*) [SMul M α] (x y : α) : Prop
```

`Relation.ofSMul_diamond` (theorem, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Lean/SMul.lean#L61))

> The relation induced by an action commuting with itself has the diamond property.

```lean
theorem ofSMul_diamond [SMul M α] [SMulCommClass M M α] : Diamond (ofSMul M α)
```

`Relation.ofSMul_preserves_iff` (theorem, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Lean/SMul.lean#L67))

> Preservation by an action-induced relation is exactly closure under the action.

```lean
theorem ofSMul_preserves_iff [SMul M α] {P : α → Prop} :
    Preserves (ofSMul M α) P ↔ ∀ m : M, ∀ x, P x → P (m • x)
```

`Relation.ofSMul_preserves_mem` (theorem, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Lean/SMul.lean#L80))

> Membership in a type closed under a scalar action is preserved by the relation induced by the
> action.

```lean
theorem ofSMul_preserves_mem [SMul M α] [SetLike S α] [SMulMemClass S M α]
    (s : S) : Preserves (ofSMul M α) (· ∈ s)
```

`Relation.ofSMul_mem_of_mem` (theorem, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Lean/SMul.lean#L86))

```lean
theorem ofSMul_mem_of_mem [SMul M α] [SetLike S α] [SMulMemClass S M α]
    {p : S} {a b : α} (hab : Relation.ofSMul M α a b) (ha : a ∈ p) : b ∈ p
```

`Cslib.Logic.Modal.Proposition.ofSMul_diamond_denotation` (theorem, [line 99](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Lean/SMul.lean#L99))

> Characterisation of the denotation of a `◇p` under `ofSMul`.

```lean
theorem ofSMul_diamond_denotation [SMul M α] [Membership α β] (p : β) :
    (◇p : Proposition τ β).denotation
      (Model.ofContainers (Frame.ofRelation (Relation.ofSMul M α))) =
      {x | ∃ m : M, m • x ∈ p}
```

`Cslib.Logic.Modal.Proposition.ofSMul_diamond_and_equiv` (theorem, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Lean/SMul.lean#L113))

> For `SetLike` objects closed under a commutative semigroup action, simultaneous reachability is
> equivalent to separate reachability.

```lean
theorem ofSMul_diamond_and_equiv [CommSemigroup M] [SemigroupAction M α] [SetLike S α]
    [SMulMemClass S M α] (p q : S) :
    ◇(p ∧ q : Proposition τ S) ≡[Equiv.OfContainers
      (Frame.ofRelation (τ := τ) (Relation.ofSMul M α))
    ] (◇p ∧ ◇q)
```

## Depends on

- [Modal Logic for Lean](../../lean/basic.md)
- [Basic Modal Logic](../basic.md)

## Proof depends on

- [Relations: preservation of properties](../../../../foundations/relation/preserves.md)

## Sources

- [Cslib/Logics/Modal/Unimodal/Lean/SMul.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Lean/SMul.lean)
