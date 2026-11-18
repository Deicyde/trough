---
catalog: module
lean: Cslib.BitString.flipBlock, Cslib.BitString.flipBlock_eq_piecewise, Cslib.BitString.flipBlock_apply_of_mem, Cslib.BitString.flipBlock_apply_of_notMem, Cslib.BitString.flipBlock_empty, Cslib.BitString.flipBlock_flipBlock, Cslib.BitString.flipBlock_involutive, Cslib.BitString.flipBlock_singleton, Cslib.BitString.flipBlock_erase, Cslib.QueryComplexity.Block, Cslib.QueryComplexity.PartialAssignment, Cslib.QueryComplexity.support, Cslib.QueryComplexity.mem_support, Cslib.QueryComplexity.size, Cslib.QueryComplexity.Agrees, Cslib.QueryComplexity.ofBitString, Cslib.QueryComplexity.agrees_ofBitString_iff, Cslib.QueryComplexity.size_ofBitString, Cslib.QueryComplexity.restrict, Cslib.QueryComplexity.agrees_restrict_iff, Cslib.QueryComplexity.support_restrict, Cslib.QueryComplexity.eq_restrict_support
statement: formalized
proof: formalized
---

# Boolean functions on the hypercube

`Cslib.Computability.QueryComplexity.Defs`, in [Cslib/Computability/QueryComplexity/Defs.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean), by Vignesh Karri.

> A Boolean function is a map `{0,1}ⁿ → {0,1}`, shared across the library as
> `Cslib.BooleanFunction` on `Cslib.BitString n`. This file sets up block flips, which are the moves
> of sensitivity and block sensitivity, and partial assignments. The complexity measures are built in
> `Measures.lean`.
>
> ## Main definitions
>
> - `BitString.flipBlock B x`: `x` with every coordinate of `B` flipped.
> - `Block n`: a set of coordinates.
> - `PartialAssignment n`: a partial assignment, fixing some coordinates and leaving others free.
> - `restrict x S`: the partial assignment reading off `x` on the coordinates in `S`.
> - `Agrees`: An input is consistent with a partial assignment.
>
> ## References
>
> * [S. Arora, B. Barak, *Computational Complexity: A Modern Approach*][AroraBarak09],
>   Chapter 12 (Decision Trees); the notions defined here underpin Sections 12.2 and 12.5.1.
> * [H. Buhrman, R. de Wolf, *Complexity measures and decision tree complexity:
>   a survey*][BuhrmanDeWolf2002]

> ## Flipping blocks of bits

`Cslib.BitString.flipBlock` (definition, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L49))

> `x` with every coordinate of `B` flipped.

```lean
def flipBlock (B : Finset (Fin n)) (x : BitString n) : BitString n
```

`Cslib.BitString.flipBlock_eq_piecewise` (theorem, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L53))

> Flipping `B` splices the negation of `x` into `x` on `B`.

```lean
theorem flipBlock_eq_piecewise (B : Finset (Fin n)) (x : BitString n) :
    flipBlock B x = B.piecewise (fun j => !(x j)) x
```

`Cslib.BitString.flipBlock_apply_of_mem` (theorem, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L58))

```lean
theorem flipBlock_apply_of_mem {B : Finset (Fin n)} {x : BitString n} {j : Fin n} (h : j ∈ B) :
    flipBlock B x j = !(x j)
```

`Cslib.BitString.flipBlock_apply_of_notMem` (theorem, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L63))

```lean
theorem flipBlock_apply_of_notMem {B : Finset (Fin n)} {x : BitString n} {j : Fin n} (h : j ∉ B) :
    flipBlock B x j = x j
```

`Cslib.BitString.flipBlock_empty` (theorem, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L69))

> Flipping no coordinates does nothing.

```lean
theorem flipBlock_empty (x : BitString n) : flipBlock ∅ x = x
```

`Cslib.BitString.flipBlock_flipBlock` (theorem, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L74))

> Flipping the same block twice does nothing.

```lean
theorem flipBlock_flipBlock (B : Finset (Fin n)) (x : BitString n) :
    flipBlock B (flipBlock B x) = x
```

`Cslib.BitString.flipBlock_involutive` (theorem, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L79))

> Flipping a block is an involution.

```lean
theorem flipBlock_involutive (B : Finset (Fin n)) : Function.Involutive (flipBlock B)
```

`Cslib.BitString.flipBlock_singleton` (theorem, [line 84](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L84))

> Flipping the block `{i}` is flipping the single bit `i`.

```lean
theorem flipBlock_singleton (i : Fin n) (x : BitString n) :
    flipBlock {i} x = Function.update x i (!x i)
```

`Cslib.BitString.flipBlock_erase` (theorem, [line 89](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L89))

> Flipping `B \ {i}` is flipping `B` and then restoring bit `i ∈ B`.

```lean
theorem flipBlock_erase {B : Finset (Fin n)} {i : Fin n} (hi : i ∈ B) (x : BitString n) :
    flipBlock (B.erase i) x = Function.update (flipBlock B x) i (x i)
```

`Cslib.QueryComplexity.Block` (abbreviation, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L101))

> A block: a set of coordinates.

```lean
abbrev Block (n : ℕ) : Type
```

> ## Partial assignments

`Cslib.QueryComplexity.PartialAssignment` (abbreviation, [line 106](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L106))

> `C i = some b` fixes coordinate `i` to `b`; `C i = none` leaves it free.

```lean
abbrev PartialAssignment (n : ℕ) : Type
```

`Cslib.QueryComplexity.support` (definition, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L109))

> The coordinates the partial assignment fixes.

```lean
def support (C : PartialAssignment n) : Finset (Fin n)
```

`Cslib.QueryComplexity.mem_support` (lemma, [line 114](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L114))

> A coordinate lies in the support if and only if the partial assignment fixes it.

```lean
lemma mem_support {C : PartialAssignment n} {i : Fin n} :
    i ∈ support C ↔ (C i).isSome
```

`Cslib.QueryComplexity.size` (definition, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L118))

> How many coordinates the partial assignment fixes.

```lean
def size (C : PartialAssignment n) : ℕ
```

`Cslib.QueryComplexity.Agrees` (definition, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L121))

> `x` agrees with `C` when it matches `C` on every fixed coordinate.

```lean
def Agrees (C : PartialAssignment n) (x : BitString n) : Prop
```

`Cslib.QueryComplexity.ofBitString` (definition, [line 127](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L127))

> The total assignment reading off every coordinate of `x`.

```lean
def ofBitString (x : BitString n) : PartialAssignment n
```

`Cslib.QueryComplexity.agrees_ofBitString_iff` (theorem, [line 131](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L131))

> A total assignment read off `x` is agreed with by `x` alone.

```lean
theorem agrees_ofBitString_iff {x y : BitString n} : Agrees (ofBitString x) y ↔ y = x
```

`Cslib.QueryComplexity.size_ofBitString` (theorem, [line 138](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L138))

> Reading off the whole input fixes all `n` coordinates.

```lean
theorem size_ofBitString (x : BitString n) : size (ofBitString x) = n
```

`Cslib.QueryComplexity.restrict` (definition, [line 142](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L142))

> The partial assignment reading off `x` on the coordinates only in `S`.

```lean
def restrict (x : BitString n) (S : Finset (Fin n)) : PartialAssignment n
```

`Cslib.QueryComplexity.agrees_restrict_iff` (theorem, [line 147](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L147))

> An input agrees with `restrict x S` if and only if it matches `x` on `S`.

```lean
theorem agrees_restrict_iff {x y : BitString n} {S : Finset (Fin n)} :
    Agrees (restrict x S) y ↔ ∀ i ∈ S, y i = x i
```

`Cslib.QueryComplexity.support_restrict` (theorem, [line 157](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L157))

> `restrict x S` fixes exactly the coordinates in `S`.

```lean
theorem support_restrict (x : BitString n) (S : Finset (Fin n)) : support (restrict x S) = S
```

`Cslib.QueryComplexity.eq_restrict_support` (theorem, [line 162](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean#L162))

> A partial assignment consistent with `x` is `x` restricted to its support.

```lean
theorem eq_restrict_support {C : PartialAssignment n} {x : BitString n} (h : Agrees C x) :
    C = restrict x (support C)
```

## Depends on

- [Fixed-length bit strings and Boolean functions](../../foundations/data/bitstring.md)

## Sources

- [Cslib/Computability/QueryComplexity/Defs.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Defs.lean)
