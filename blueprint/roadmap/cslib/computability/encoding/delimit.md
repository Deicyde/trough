---
catalog: module
lean: Cslib.Encoding.delimit, Cslib.Encoding.undelimit, Cslib.Encoding.dropDelimited, Cslib.Encoding.delimit_nil, Cslib.Encoding.delimit_cons, Cslib.Encoding.length_delimit, Cslib.Encoding.delimit_ne_nil, Cslib.Encoding.undelimit_nil, Cslib.Encoding.undelimit_false_cons, Cslib.Encoding.undelimit_true_nil, Cslib.Encoding.undelimit_true_cons_cons, Cslib.Encoding.dropDelimited_nil, Cslib.Encoding.dropDelimited_false_cons, Cslib.Encoding.dropDelimited_true_nil, Cslib.Encoding.dropDelimited_true_cons_cons, Cslib.Encoding.undelimit_delimit_append, Cslib.Encoding.undelimit_delimit, Cslib.Encoding.dropDelimited_delimit_append, Cslib.Encoding.delimit_append_inj, Cslib.Encoding.delimit_append_inj_iff, Cslib.Encoding.delimit_injective, Cslib.Encoding.delimit_inj, Cslib.Encoding.delimit_prefix_delimit, Cslib.Encoding.length_undelimit_le, Cslib.Encoding.length_dropDelimited_le
statement: formalized
proof: formalized
---

# Delimited Boolean words

`Cslib.Computability.Encoding.Delimit`, in [Cslib/Computability/Encoding/Delimit.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean), by Christian Reitwiessner.

> Defines `delimit` which turns arbitrary Boolean words into a self-delimiting, prefix-free code.
> The input words may be empty, contain any bit pattern, or be prefixes of one another.
>
> `delimit` writes each data bit `b` as `[true, b]` and ends the codeword with `[false]`. This means
> that `true` introduces one data bit and `false` terminates the word, which makes the boundary
> recognizable in one left-to-right pass, even when arbitrary data follows it. A word of length `n`
> has a delimited code of length `2 * n + 1`.
>
> The guarantee concerns individual delimited words. A variable-length list of concatenated
> codewords needs its own delimiter if the entire list encoding is to be prefix-free.
>
> ## Main definitions
>
> * `Cslib.Encoding.delimit` encodes a word. `Cslib.Encoding.undelimit` reads the first encoded
>   word, and `Cslib.Encoding.dropDelimited` skips it.
>
> ## Main results
>
> * `Cslib.Encoding.delimit_prefix_delimit` states that one codeword is a prefix of another
>   exactly when the original words are equal.
> * `Cslib.Encoding.undelimit_delimit_append` and `Cslib.Encoding.dropDelimited_delimit_append`
>   recover the original word and the suffix following its codeword, respectively.

> ### Delimited words

`Cslib.Encoding.delimit` (definition, [line 45](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L45))

> Each symbol `b` of `w` as `[true, b]`, followed by `[false]`.

```lean
def delimit (w : List Bool) : List Bool
```

`Cslib.Encoding.undelimit` (definition, [line 50](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L50))

> Read complete tagged bits until the delimiter or end of input. An incomplete trailing tag
> is ignored.

```lean
def undelimit : List Bool → List Bool
```

`Cslib.Encoding.dropDelimited` (definition, [line 55](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L55))

> The suffix after the first delimiter, or `[]` if the input ends before a delimiter.

```lean
def dropDelimited : List Bool → List Bool
```

`Cslib.Encoding.delimit_nil` (theorem, [line 61](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L61))

```lean
theorem delimit_nil : delimit [] = [false]
```

`Cslib.Encoding.delimit_cons` (theorem, [line 64](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L64))

```lean
theorem delimit_cons (b : Bool) (w : List Bool) : delimit (b :: w) =
    true :: b :: delimit w
```

`Cslib.Encoding.length_delimit` (theorem, [line 68](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L68))

```lean
theorem length_delimit (w : List Bool) : (delimit w).length = 2 * w.length + 1
```

`Cslib.Encoding.delimit_ne_nil` (theorem, [line 72](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L72))

```lean
theorem delimit_ne_nil (w : List Bool) : delimit w ≠ []
```

> Equation lemmas for `undelimit` and `dropDelimited`. These are needed by `simp` because
> `delimit_cons` rewrites `delimit (b :: w)` before the round-trip lemmas below can apply.

`Cslib.Encoding.undelimit_nil` (theorem, [line 77](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L77))

```lean
theorem undelimit_nil : undelimit [] = []
```

`Cslib.Encoding.undelimit_false_cons` (theorem, [line 79](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L79))

```lean
theorem undelimit_false_cons (v : List Bool) : undelimit (false :: v) = []
```

`Cslib.Encoding.undelimit_true_nil` (theorem, [line 81](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L81))

```lean
theorem undelimit_true_nil : undelimit [true] = []
```

`Cslib.Encoding.undelimit_true_cons_cons` (theorem, [line 83](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L83))

```lean
theorem undelimit_true_cons_cons (b : Bool) (v : List Bool) :
    undelimit (true :: b :: v) = b :: undelimit v
```

`Cslib.Encoding.dropDelimited_nil` (theorem, [line 86](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L86))

```lean
theorem dropDelimited_nil : dropDelimited [] = []
```

`Cslib.Encoding.dropDelimited_false_cons` (theorem, [line 88](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L88))

```lean
theorem dropDelimited_false_cons (v : List Bool) : dropDelimited (false :: v) = v
```

`Cslib.Encoding.dropDelimited_true_nil` (theorem, [line 90](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L90))

```lean
theorem dropDelimited_true_nil : dropDelimited [true] = []
```

`Cslib.Encoding.dropDelimited_true_cons_cons` (theorem, [line 92](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L92))

```lean
theorem dropDelimited_true_cons_cons (b : Bool) (v : List Bool) :
    dropDelimited (true :: b :: v) = dropDelimited v
```

`Cslib.Encoding.undelimit_delimit_append` (theorem, [line 96](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L96))

```lean
theorem undelimit_delimit_append (w u : List Bool) : undelimit (delimit w ++ u) = w
```

`Cslib.Encoding.undelimit_delimit` (theorem, [line 100](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L100))

```lean
theorem undelimit_delimit (w : List Bool) : undelimit (delimit w) = w
```

`Cslib.Encoding.dropDelimited_delimit_append` (theorem, [line 104](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L104))

```lean
theorem dropDelimited_delimit_append (w u : List Bool) :
    dropDelimited (delimit w ++ u) = u
```

`Cslib.Encoding.delimit_append_inj` (theorem, [line 110](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L110))

> A delimited word followed by another word determines both.

```lean
theorem delimit_append_inj {w w' u u' : List Bool} (h : delimit w ++ u = delimit w' ++ u') :
    w = w' ∧ u = u'
```

`Cslib.Encoding.delimit_append_inj_iff` (theorem, [line 115](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L115))

```lean
theorem delimit_append_inj_iff {w w' u u' : List Bool} :
    delimit w ++ u = delimit w' ++ u' ↔ w = w' ∧ u = u'
```

`Cslib.Encoding.delimit_injective` (theorem, [line 121](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L121))

> Delimiting is injective.

```lean
theorem delimit_injective : Function.Injective delimit
```

`Cslib.Encoding.delimit_inj` (theorem, [line 125](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L125))

```lean
theorem delimit_inj {w w' : List Bool} : delimit w = delimit w' ↔ w = w'
```

`Cslib.Encoding.delimit_prefix_delimit` (theorem, [line 130](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L130))

> The image of `delimit` is prefix-free, independently of the input words.

```lean
theorem delimit_prefix_delimit {w v : List Bool} :
    delimit w <+: delimit v ↔ w = v
```

> ### Lengths

`Cslib.Encoding.length_undelimit_le` (theorem, [line 141](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L141))

> Decoding does not make a word longer.

```lean
theorem length_undelimit_le (w : List Bool) : (undelimit w).length ≤ w.length
```

`Cslib.Encoding.length_dropDelimited_le` (theorem, [line 145](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean#L145))

> Skipping the first codeword does not make a word longer.

```lean
theorem length_dropDelimited_le (w : List Bool) : (dropDelimited w).length ≤ w.length
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Computability/Encoding/Delimit.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Delimit.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Computability.Encoding.Delimit.json)
