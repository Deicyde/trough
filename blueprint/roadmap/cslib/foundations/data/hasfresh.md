---
catalog: module
lean: Cslib.HasFresh, Cslib.HasFresh.fresh_exists, Cslib.HasFresh.to_infinite, Cslib.HasFresh.ofNatEmbed, Cslib.HasFresh.ofSucc, Cslib.FreeUnionConfig, Cslib.HasFresh.freeUnion
statement: formalized
proof: formalized
---

# HasFresh

`Cslib.Foundations.Data.HasFresh`, in [Cslib/Foundations/Data/HasFresh.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/HasFresh.lean), by Fabrizio Montesi, Kenny Lau.

> Computable chacterization of infinite types.

`Cslib.HasFresh` (class, [line 22](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/HasFresh.lean#L22))

> A type `α` has a computable `fresh` function if it is always possible, for any finite set
> of `α`, to compute a fresh element not in the set.

```lean
class HasFresh (α : Type u) where
  /-- Given a finite set, returns an element not in the set. -/
  fresh : Finset α → α
  /-- Proof that `fresh` returns a fresh element for its input set. -/
  fresh_notMem (s : Finset α) : fresh s ∉ s
```

`Cslib.HasFresh.fresh_exists` (theorem, [line 32](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/HasFresh.lean#L32))

> An existential version of the `HasFresh` typeclass. This is useful for the sake of brevity
> in proofs.

```lean
theorem HasFresh.fresh_exists {α : Type u} [HasFresh α] (s : Finset α) : ∃ a, a ∉ s
```

`Cslib.HasFresh.to_infinite` (instance, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/HasFresh.lean#L38))

> `HasFresh α` implies a computably infinite type.

```lean
instance HasFresh.to_infinite (α : Type u) [HasFresh α] : Infinite α
```

`Cslib.HasFresh.ofNatEmbed` (definition, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/HasFresh.lean#L52))

> Construct a fresh element from an embedding of `ℕ` using `Nat.find`.

```lean
def HasFresh.ofNatEmbed {α : Type u} [DecidableEq α] (e : ℕ ↪ α) : HasFresh α
```

`Cslib.HasFresh.ofSucc` (definition, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/HasFresh.lean#L59))

> Construct a fresh element given a function `f` with `x < f x`.

```lean
def HasFresh.ofSucc {α : Type u} [Inhabited α] [SemilatticeSup α] (f : α → α) (hf : ∀ x, x < f x) :
    HasFresh α
```

`Cslib.FreeUnionConfig` (structure, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/HasFresh.lean#L97))

> Configuration for the `free_union` term elaborator.

```lean
structure FreeUnionConfig where
  /-- For `free_union Var`, include all `x : Var`. Defaults to true. -/
  singleton : Bool := true
  /-- For `free_union Var`, include all `xs : Finset Var`. Defaults to true. -/
  finset : Bool := true
```

`Cslib.HasFresh.freeUnion` (definition, [line 143](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/HasFresh.lean#L143))

> Elaborator for `free_union`.

```lean
def HasFresh.freeUnion : TermElab
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Data/HasFresh.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/HasFresh.lean)
