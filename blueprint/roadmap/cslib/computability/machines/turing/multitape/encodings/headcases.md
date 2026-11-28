---
catalog: module
lean: Cslib.Encoding.headCases, Cslib.Encoding.length_headCases_le, Turing.MultiTapeTM.computableInTimeAndSpace_headCases
statement: formalized
proof: formalized
---

# Complexity of operations on the first bit of a Boolean word

`Cslib.Computability.Machines.Turing.MultiTape.Encodings.HeadCases`, in [Cslib/Computability/Machines/Turing/MultiTape/Encodings/HeadCases.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Encodings/HeadCases.lean), by Christian Reitwiessner.

> A multitape Turing machine computes `headCases e g keep` in linear time and zero work space.
> This function is useful when reading a sum tag or the least significant bit of a number.
> The construction uses a subsequential transducer that reads the first bit to decide whether to copy
> or discard the tail.
>
> ## Main definitions
>
> * `Cslib.Encoding.headCases` replaces the first bit with a word and uses that bit to decide
>   whether to copy the remaining input. It returns a supplied default on empty input.
>
> ## Main results
>
> * `Cslib.Encoding.length_headCases_le` bounds the output length by the input length plus the
>   maximum length of the default and the two replacement words.
> * `Turing.MultiTapeTM.computableInTimeAndSpace_headCases` bounds the running time by twice the
>   input length plus a constant depending on `e` and `g`, using zero work space.

`Cslib.Encoding.headCases` (definition, [line 41](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Encodings/HeadCases.lean#L41))

> Return `e` on empty input. Otherwise replace the first bit `b` with `g b` and
> copy the tail if `keep b` is true.

```lean
def headCases (e : List Bool) (g : Bool → List Bool) (keep : Bool → Bool) : List Bool → List Bool
```

`Cslib.Encoding.length_headCases_le` (theorem, [line 51](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Encodings/HeadCases.lean#L51))

> The output is at most as long as the input plus the longest of `e`, `g false` and
> `g true`.

```lean
theorem length_headCases_le (w : List Bool) :
    (headCases e g keep w).length ≤
      w.length + max e.length (max (g false).length (g true).length)
```

`Turing.MultiTapeTM.computableInTimeAndSpace_headCases` (theorem, [line 94](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Encodings/HeadCases.lean#L94))

> `headCases e g keep` is computable in linear time and zero space.

```lean
theorem computableInTimeAndSpace_headCases (e : List Bool) (g : Bool → List Bool)
    (keep : Bool → Bool) :
    ComputableInTimeAndSpace (headCases e g keep) encBits encBits
      (fun w => 2 * w.length + max e.length (max (g false).length (g true).length) + 1)
      (fun _ => 0)
```

## Depends on

- [Default encodings](../../../../encoding/basic.md)
- [Deterministic Multi-Tape Turing Machines](../deterministic.md)

## Proof depends on

- [Turing machine simulation of finite sequential and subsequential transducers](../transducer.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Encodings/HeadCases.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Encodings/HeadCases.lean)
- [Declaration ledger](../../../../../../../sources/cslib/Cslib.Computability.Machines.Turing.MultiTape.Encodings.HeadCases.json)
