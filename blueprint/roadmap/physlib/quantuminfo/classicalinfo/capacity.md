---
declaration: module
origin: cited
lean: Code, FixedLengthCode
statement: formalized
proof: formalized
---

# QuantumInfo.ClassicalInfo.Capacity

The module `QuantumInfo.ClassicalInfo.Capacity`, [QuantumInfo/ClassicalInfo/Capacity.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Capacity.lean): 2 declarations, 2 with a docstring.

**`Code`**, a structure, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Capacity.lean#L26).

> Here we define a *Code* by an encdoder and a decoder. The encoder is a function that takes
> strings (`List`s) of any length over an alphabet `A`, and returns strings over `I`;
> the decoder takes `O` and gives back strings over `A`. The idea is that a channel
> would map from strings of `I` to `O`. Important special cases are where `I=O` (the channel doesn't
> change the symbol set), and `FixedLengthCode` where the output lengths only depend on input
> lengths.

```lean
structure Code where
  encoder : List A → List I
  decoder : List O → List A
```

**`FixedLengthCode`**, a structure, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Capacity.lean#L32).

> A `FixedLengthCode` is a `Code` whose output lengths don't depend on the input content, only
> the input length.

```lean
structure FixedLengthCode extends Code A I O where
  enc_length : ℕ → ℕ
  enc_maps_length : ∀ as, (encoder as).length = enc_length (as.length)
  dec_length : ℕ → ℕ
  dec_maps_length : ∀ is, (decoder is).length = dec_length (is.length)
```

## Depends on

- [Physlib.Meta.Informal.Basic](../../physlib/meta/informal/basic.md)

## Sources

- [QuantumInfo/ClassicalInfo/Capacity.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Capacity.lean)
