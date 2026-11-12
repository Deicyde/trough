---
catalog: module
lean: Cslib.Turing.BiTape, Cslib.Turing.BiTape.nil, Cslib.Turing.BiTape.empty_eq_nil, Cslib.Turing.BiTape.mk₁, Cslib.Turing.BiTape.moveLeft, Cslib.Turing.BiTape.moveRight, Cslib.Turing.BiTape.move, Cslib.Turing.BiTape.optionMove, Cslib.Turing.BiTape.moveLeft_moveRight, Cslib.Turing.BiTape.moveRight_moveLeft, Cslib.Turing.BiTape.write, Cslib.Turing.BiTape.spaceUsed, Cslib.Turing.BiTape.spaceUsed_write, Cslib.Turing.BiTape.spaceUsed_mk₁, Cslib.Turing.BiTape.spaceUsed_move
statement: formalized
proof: formalized
---

# BiTape: Bidirectionally infinite TM tape representation using StackTape

`Cslib.Foundations.Data.BiTape`, in [Cslib/Foundations/Data/BiTape.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/BiTape.lean), by Bolton Bailey.

> This file defines `BiTape`, a tape representation for Turing machines
> in the form of an `List` of `Option` values,
> with the additional property that the list cannot end with `none`.
>
> ## Design
>
> Note that Mathlib has a `Tape` type, but it requires the alphabet type to be inhabited,
> and considers the ends of the tape to be filled with default values.
>
> This design requires the tape elements to be `Option` values, and ensures that
> `List`s of the base alphabet, rendered directly onto the tape by mapping over `some`,
> will not collide.
>
> ## Main definitions
>
> * `BiTape`: A tape with a head symbol and left/right contents stored as `StackTape`
> * `BiTape.move`: Move the tape head left or right
> * `BiTape.write`: Write a symbol at the current head position
> * `BiTape.spaceUsed`: The space used by the tape

`Cslib.Turing.BiTape` (structure, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/BiTape.lean#L47))

> A structure for bidirectionally-infinite Turing machine tapes
> that eventually take on blank `none` values

```lean
structure BiTape (Symbol : Type*) where
  /-- The symbol currently under the tape head -/
  head : Option Symbol
  /-- The contents to the left of the head -/
  left : StackTape Symbol
  /-- The contents to the right of the head -/
  right : StackTape Symbol
```

`Cslib.Turing.BiTape.nil` (definition, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/BiTape.lean#L60))

> The empty `BiTape`

```lean
def nil : BiTape Symbol
```

`Cslib.Turing.BiTape.empty_eq_nil` (lemma, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/BiTape.lean#L69))

```lean
lemma empty_eq_nil : (∅ : BiTape Symbol) = nil
```

`Cslib.Turing.BiTape.mk₁` (definition, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/BiTape.lean#L76))

> Given a `List` of `Symbol`s, construct a `BiTape` by mapping the list to `some` elements
> and laying them out to the right side,
> with the head under the first element of the list if it exists.

```lean
def mk₁ (l : List Symbol) : BiTape Symbol
```

`Cslib.Turing.BiTape.moveLeft` (definition, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/BiTape.lean#L86))

> Move the head left by shifting the left StackTape under the head.

```lean
def moveLeft (t : BiTape Symbol) : BiTape Symbol
```

`Cslib.Turing.BiTape.moveRight` (definition, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/BiTape.lean#L92))

> Move the head right by shifting the right StackTape under the head.

```lean
def moveRight (t : BiTape Symbol) : BiTape Symbol
```

`Cslib.Turing.BiTape.move` (definition, [line 100](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/BiTape.lean#L100))

> Move the head to the left or right, shifting the tape underneath it.

```lean
def move (t : BiTape Symbol) : Dir → BiTape Symbol
```

`Cslib.Turing.BiTape.optionMove` (definition, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/BiTape.lean#L107))

> Optionally perform a `move`, or do nothing if `none`.

```lean
def optionMove : BiTape Symbol → Option Turing.Dir → BiTape Symbol
```

`Cslib.Turing.BiTape.moveLeft_moveRight` (lemma, [line 112](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/BiTape.lean#L112))

```lean
lemma moveLeft_moveRight (t : BiTape Symbol) : t.moveLeft.moveRight = t
```

`Cslib.Turing.BiTape.moveRight_moveLeft` (lemma, [line 116](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/BiTape.lean#L116))

```lean
lemma moveRight_moveLeft (t : BiTape Symbol) : t.moveRight.moveLeft = t
```

`Cslib.Turing.BiTape.write` (definition, [line 124](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/BiTape.lean#L124))

> Write a value under the head of the `BiTape`.

```lean
def write (t : BiTape Symbol) (a : Option Symbol) : BiTape Symbol
```

`Cslib.Turing.BiTape.spaceUsed` (definition, [line 130](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/BiTape.lean#L130))

> The space used by a `BiTape` is the number of symbols
> between and including the head, and leftmost and rightmost non-blank symbols on the `BiTape`.

```lean
def spaceUsed (t : BiTape Symbol) : ℕ
```

`Cslib.Turing.BiTape.spaceUsed_write` (lemma, [line 133](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/BiTape.lean#L133))

```lean
lemma spaceUsed_write (t : BiTape Symbol) (a : Option Symbol) :
    (t.write a).spaceUsed = t.spaceUsed
```

`Cslib.Turing.BiTape.spaceUsed_mk₁` (lemma, [line 136](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/BiTape.lean#L136))

```lean
lemma spaceUsed_mk₁ (l : List Symbol) :
    (mk₁ l).spaceUsed = max 1 l.length
```

`Cslib.Turing.BiTape.spaceUsed_move` (lemma, [line 142](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/BiTape.lean#L142))

```lean
lemma spaceUsed_move (t : BiTape Symbol) (d : Turing.Dir) :
    (t.move d).spaceUsed ≤ t.spaceUsed + 1
```

## Depends on

- [StackTape: Infinite, eventually-`none` lists of `Option`s](stacktape.md)

## Sources

- [Cslib/Foundations/Data/BiTape.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/BiTape.lean)
