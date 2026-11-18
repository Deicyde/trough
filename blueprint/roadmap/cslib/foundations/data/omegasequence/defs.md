---
catalog: module
lean: Cslib.ωSequence, Cslib.ωSequence.head, Cslib.ωSequence.tail, Cslib.ωSequence.drop, Cslib.ωSequence.take, Cslib.ωSequence.extract, Cslib.ωSequence.cons, Cslib.ωSequence.appendωSequence, Cslib.ωSequence.const, Cslib.ωSequence.map, Cslib.ωSequence.zip, Cslib.ωSequence.iterate
statement: formalized
proof: formalized
---

# Definition of `ωSequence` and functions on infinite sequences

`Cslib.Foundations.Data.OmegaSequence.Defs`, in [Cslib/Foundations/Data/OmegaSequence/Defs.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Defs.lean), by Ching-Tsun Chou, Fabrizio Montesi.

> An `ωSequence α` is an infinite sequence of elements of `α`.  It is basically
> a wrapper around the type `ℕ → α` which supports the dot-notation and
> the analogues of many familiar API functions of `List α`.  In particular,
> the element at position `n : ℕ` of `s : ωSequence α` is obtained using the
> function application notation `s n`.
>
> In this file we define `ωSequence` and its API functions.
> Most code below is adapted from Mathlib.Data.Stream.Defs.

`Cslib.ωSequence` (structure, [line 34](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Defs.lean#L34))

> An `ωSequence α` is an infinite sequence of elements of `α`.

```lean
structure ωSequence (α : Type u) where
  /-- The function that defines this infinite sequence. -/
  get : ℕ → α
```

`Cslib.ωSequence.head` (abbreviation, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Defs.lean#L49))

> Head of an ω-sequence: `ωSequence.head s = ωSequence s 0`.

```lean
abbrev head (s : ωSequence α) : α
```

`Cslib.ωSequence.tail` (definition, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Defs.lean#L52))

> Tail of an ω-sequence: `ωSequence.tail (h :: t) = t`.

```lean
def tail (s : ωSequence α) : ωSequence α
```

`Cslib.ωSequence.drop` (definition, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Defs.lean#L55))

> Drop first `n` elements of an ω-sequence.

```lean
def drop (n : ℕ) (s : ωSequence α) : ωSequence α
```

`Cslib.ωSequence.take` (definition, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Defs.lean#L58))

> `take n s` returns a list of the `n` first elements of ω-sequence `s`

```lean
def take : ℕ → ωSequence α → List α
```

`Cslib.ωSequence.extract` (definition, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Defs.lean#L63))

> Get the list containing the elements of `xs` from position `m` to `n - 1`.

```lean
def extract (xs : ωSequence α) (m n : ℕ) : List α
```

`Cslib.ωSequence.cons` (definition, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Defs.lean#L67))

> Prepend an element to an ω-sequence.

```lean
def cons (a : α) (s : ωSequence α) : ωSequence α
```

`Cslib.ωSequence.appendωSequence` (definition, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Defs.lean#L74))

> Append an ω-sequence to a list.

```lean
def appendωSequence : List α → ωSequence α → ωSequence α
```

`Cslib.ωSequence.const` (definition, [line 81](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Defs.lean#L81))

> The constant ω-sequence: `ωSequence n (ωSequence.const a) = a`.

```lean
def const (a : α) : ωSequence α
```

`Cslib.ωSequence.map` (definition, [line 84](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Defs.lean#L84))

> Apply a function `f` to all elements of an ω-sequence `s`.

```lean
def map (f : α → β) (s : ωSequence α) : ωSequence β
```

`Cslib.ωSequence.zip` (definition, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Defs.lean#L88))

> Zip two ω-sequences using a binary operation:
> `ωSequence n (ωSequence.zip f s₁ s₂) = f (ωSequence s₁) (ωSequence s₂)`.

```lean
def zip (f : α → β → δ) (s₁ : ωSequence α) (s₂ : ωSequence β) : ωSequence δ
```

`Cslib.ωSequence.iterate` (definition, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Defs.lean#L92))

> Iterates of a function as an ω-sequence.

```lean
def iterate (f : α → α) (a : α) : ωSequence α
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Data/OmegaSequence/Defs.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Defs.lean)
