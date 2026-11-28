---
catalog: module
lean: Cslib.Encoding.undelimitOr, Cslib.Encoding.undelimitOr_nil_left, Cslib.Encoding.undelimitOr_delimit_append, Cslib.Encoding.undelimitAll, Cslib.Encoding.undelimitAll_delimit_append, Cslib.Encoding.length_undelimitOr_le, Cslib.Encoding.length_undelimitAll_le, Turing.MultiTapeTM.computableInTimeAndSpace_delimit, Turing.MultiTapeTM.computableInTimeAndSpace_undelimitOr, Turing.MultiTapeTM.computableInTimeAndSpace_undelimit, Turing.MultiTapeTM.computableInTimeAndSpace_dropDelimited, Turing.MultiTapeTM.computableInTimeAndSpace_undelimitAll
statement: formalized
proof: formalized
---

# Complexity of operations on delimited Boolean words

`Cslib.Computability.Machines.Turing.MultiTape.Encodings.Delimit`, in [Cslib/Computability/Machines/Turing/MultiTape/Encodings/Delimit.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Encodings/Delimit.lean), by Christian Reitwiessner.

> The functions `delimit`, `undelimit`, `undelimitOr`, `dropDelimited` and `undelimitAll` are
> computable by multitape Turing machines in linear time and zero work space.
> The constructions use subsequential transducers for `delimit` and `undelimitOr`.
> Taking the empty default gives `undelimit`. Sequential transducers suffice for `dropDelimited`
> and `undelimitAll`.
>
> ## Main definitions
>
> * `Cslib.Encoding.undelimitOr` decodes the first word like `Cslib.Encoding.undelimit` and
>   supplies a default on empty input.
> * `Cslib.Encoding.undelimitAll` concatenates all decoded words.
>
> ## Main results
>
> * `Cslib.Encoding.undelimitAll_delimit_append` decodes a leading codeword and continues
>   decoding the suffix.
> * `Turing.MultiTapeTM.computableInTimeAndSpace_delimit` bounds the cost of writing a codeword.
> * `Turing.MultiTapeTM.computableInTimeAndSpace_undelimit` and
>   `Turing.MultiTapeTM.computableInTimeAndSpace_undelimitOr` bound the cost of decoding the first
>   word, with a configurable default on empty input for `undelimitOr`.
> * `Turing.MultiTapeTM.computableInTimeAndSpace_dropDelimited` bounds the cost of copying the
>   suffix after the first codeword.
> * `Turing.MultiTapeTM.computableInTimeAndSpace_undelimitAll` bounds the cost of decoding all
>   codewords and concatenating their contents.

`Cslib.Encoding.undelimitOr` (definition, [line 48](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Encodings/Delimit.lean#L48))

> Decode the first word with `undelimit`, and use `e` when the input is empty.

```lean
def undelimitOr (e : List Bool) : List Bool → List Bool
```

`Cslib.Encoding.undelimitOr_nil_left` (theorem, [line 55](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Encodings/Delimit.lean#L55))

```lean
theorem undelimitOr_nil_left : undelimitOr [] = undelimit
```

`Cslib.Encoding.undelimitOr_delimit_append` (theorem, [line 60](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Encodings/Delimit.lean#L60))

```lean
theorem undelimitOr_delimit_append (e w u : List Bool) :
    undelimitOr e (delimit w ++ u) = w
```

`Cslib.Encoding.undelimitAll` (definition, [line 67](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Encodings/Delimit.lean#L67))

> The concatenation of the words whose delimited codes make up `w`: removes all tags and
> delimiters. A trailing tag `true` without a data bit is ignored.

```lean
def undelimitAll : List Bool → List Bool
```

`Cslib.Encoding.undelimitAll_delimit_append` (theorem, [line 73](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Encodings/Delimit.lean#L73))

```lean
theorem undelimitAll_delimit_append (w u : List Bool) :
    undelimitAll (delimit w ++ u) = w ++ undelimitAll u
```

`Cslib.Encoding.length_undelimitOr_le` (theorem, [line 78](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Encodings/Delimit.lean#L78))

> Decoding with a default adds at most the length of the default.

```lean
theorem length_undelimitOr_le (e w : List Bool) :
    (undelimitOr e w).length ≤ w.length + e.length
```

`Cslib.Encoding.length_undelimitAll_le` (theorem, [line 83](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Encodings/Delimit.lean#L83))

> Decoding all codewords does not make a word longer.

```lean
theorem length_undelimitAll_le (w : List Bool) : (undelimitAll w).length ≤ w.length
```

> ### Writing a delimited word

`Turing.MultiTapeTM.computableInTimeAndSpace_delimit` (theorem, [line 104](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Encodings/Delimit.lean#L104))

> Writing a delimited code is computable in linear time and zero work space.

```lean
theorem computableInTimeAndSpace_delimit :
    ComputableInTimeAndSpace delimit encBits encBits (fun w => 3 * w.length + 2) (fun _ => 0)
```

> ### The word whose delimited code starts the input

`Turing.MultiTapeTM.computableInTimeAndSpace_undelimitOr` (theorem, [line 152](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Encodings/Delimit.lean#L152))

> `undelimitOr e` is computable in linear time and zero space.

```lean
theorem computableInTimeAndSpace_undelimitOr (e : List Bool) :
    ComputableInTimeAndSpace (undelimitOr e) encBits encBits
      (fun w => 2 * w.length + e.length + 1) (fun _ => 0)
```

`Turing.MultiTapeTM.computableInTimeAndSpace_undelimit` (theorem, [line 160](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Encodings/Delimit.lean#L160))

> `undelimit` is computable in linear time and zero space.

```lean
theorem computableInTimeAndSpace_undelimit :
    ComputableInTimeAndSpace undelimit encBits encBits (fun w => 2 * w.length + 1)
      (fun _ => 0)
```

> ### What follows the first delimited code

`Turing.MultiTapeTM.computableInTimeAndSpace_dropDelimited` (theorem, [line 200](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Encodings/Delimit.lean#L200))

> `dropDelimited` is computable in linear time and zero space.

```lean
theorem computableInTimeAndSpace_dropDelimited :
    ComputableInTimeAndSpace dropDelimited encBits encBits (fun w => 2 * w.length + 1)
      (fun _ => 0)
```

> ### All delimited codes

`Turing.MultiTapeTM.computableInTimeAndSpace_undelimitAll` (theorem, [line 229](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Encodings/Delimit.lean#L229))

> `undelimitAll` is computable in linear time and zero space.

```lean
theorem computableInTimeAndSpace_undelimitAll :
    ComputableInTimeAndSpace undelimitAll encBits encBits (fun w => 2 * w.length + 1)
      (fun _ => 0)
```

## Depends on

- [Default encodings](../../../../encoding/basic.md)
- [Deterministic Multi-Tape Turing Machines](../deterministic.md)

## Proof depends on

- [Turing machine simulation of finite sequential and subsequential transducers](../transducer.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Encodings/Delimit.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Encodings/Delimit.lean)
- [Declaration ledger](../../../../../../../sources/cslib/Cslib.Computability.Machines.Turing.MultiTape.Encodings.Delimit.json)
