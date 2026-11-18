---
catalog: module
lean: Cslib.Circuits.Line.instFinite, Cslib.Circuits.Program.instFinite, Cslib.Circuits.Line.card, Cslib.Circuits.Line.card_le, Cslib.Circuits.Program.card_zero, Cslib.Circuits.Program.card_succ, Cslib.Circuits.Program.card, Cslib.Circuits.FullOp.equiv, Cslib.Circuits.FullOp.card, Cslib.Circuits.Line.card_full
statement: formalized
proof: formalized
---

# Finite circuit syntax

`Cslib.Computability.Circuit.Finite`, in [Cslib/Computability/Circuit/Finite.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Finite.lean), by Samuel Schlesinger.

> A finite signature gives finitely many lines and programs of each fixed size.
> Their cardinalities count syntax and are independent of any interpretation or carrier.
> `Line.card_le` bounds the number of lines when all operation arities are bounded.
> For the full basis on a carrier of size `q`, there are `q ^ (q ^ k)` operation tables
> and `q` constants. `Line.card_full` counts their possible arguments separately.

`Cslib.Circuits.Line.instFinite` (instance, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Finite.lean#L33))

```lean
instance Line.instFinite (n g : ℕ) : Finite (Line σ n g)
```

`Cslib.Circuits.Program.instFinite` (instance, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Finite.lean#L36))

```lean
instance Program.instFinite (n : ℕ) : (g : ℕ) → Finite (Program σ n g)
```

`Cslib.Circuits.Line.card` (theorem, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Finite.lean#L43))

> For each operation, choose one wire for each of its arguments.

```lean
theorem Line.card (n g : ℕ) :
    Nat.card (Line σ n g) = ∑ᶠ op : σ.Op, (n + g) ^ σ.Arity op
```

`Cslib.Circuits.Line.card_le` (theorem, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Finite.lean#L51))

> A uniform arity bound gives a uniform bound on the number of lines, including when
> there are no available wires.

```lean
theorem Line.card_le (n g r : ℕ) (arity_le : ∀ op, σ.Arity op ≤ r) :
    Nat.card (Line σ n g) ≤ Nat.card σ.Op * (n + g + 1) ^ r
```

`Cslib.Circuits.Program.card_zero` (theorem, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Finite.lean#L65))

> There is one empty program, regardless of the signature or number of inputs.

```lean
theorem Program.card_zero (n : ℕ) : Nat.card (Program σ n 0) = 1
```

`Cslib.Circuits.Program.card_succ` (theorem, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Finite.lean#L71))

> Choose a prefix program and then its last line.

```lean
theorem Program.card_succ (n g : ℕ) :
    Nat.card (Program σ n (g + 1)) =
      Nat.card (Program σ n g) * Nat.card (Line σ n g)
```

`Cslib.Circuits.Program.card` (theorem, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Finite.lean#L77))

> The line at each position may refer to the inputs and all preceding gates.

```lean
theorem Program.card (n g : ℕ) :
    Nat.card (Program σ n g) =
      ∏ j ∈ Finset.range g, ∑ᶠ op : σ.Op, (n + j) ^ σ.Arity op
```

`Cslib.Circuits.FullOp.equiv` (definition, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Finite.lean#L87))

> A full-basis operation is either a `k`-ary function or a constant.

```lean
def equiv (k : ℕ) (U : Type*) : FullOp k U ≃ (((Fin k → U) → U) ⊕ U)
```

`Cslib.Circuits.FullOp.card` (theorem, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Finite.lean#L101))

> Full-basis operations consist of all function tables and all constants.

```lean
theorem card (k : ℕ) (U : Type*) [Finite U] :
    Nat.card (FullOp k U) = Nat.card U ^ (Nat.card U ^ k) + Nat.card U
```

`Cslib.Circuits.Line.card_full` (theorem, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Finite.lean#L111))

> A function table takes `k` wire arguments; a constant takes none.

```lean
theorem Line.card_full (k n g : ℕ) (U : Type*) [Finite U] :
    Nat.card (Line (fullSignature k U) n g) =
      Nat.card U ^ (Nat.card U ^ k) * (n + g) ^ k + Nat.card U
```

## Depends on

- [Straight-line programs](program.md)

## Sources

- [Cslib/Computability/Circuit/Finite.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Finite.lean)
