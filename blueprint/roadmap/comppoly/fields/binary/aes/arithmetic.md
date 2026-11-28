---
catalog: module
lean: AesField.params, AesField, AesField.ofBitVec, AesField.toBitVec, AesField.coeff_ofBitVec, AesField.getLsbD_toBitVec, AesField.toBitVec_ofBitVec, AesField.ofBitVec_toBitVec, AesField.equivBitVec, AesField.toBitVec_injective, AesField.gen, AesField.gen_eq_ofBitVec, AesField.toBitVec_gen
statement: formalized
proof: formalized
---

# AES polynomial-basis coordinates and arithmetic

`CompPoly.Fields.Binary.Aes.Arithmetic`, in [CompPoly/Fields/Binary/Aes/Arithmetic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Aes/Arithmetic.lean), by CompPoly Contributors.

> `AesField` reuses the nominal monic-extension carrier with coefficients in `ZMod 2` and
> modulus `X^8 + X^4 + X^3 + X + 1`. Its explicit byte maps identify bit `i` with the
> coefficient of `X^i`, including the constant term at bit zero. Arithmetic uses the existing
> extension implementation; no raw-word coercion or separate byte multiplication is installed.
>
> This module contains executable operations and coordinate proofs. Irreducibility, certified
> field laws and quotient correspondence are supplied by `Aes.Basic`.
>
> ## References
>
> * NIST, *Advanced Encryption Standard (AES)*, FIPS 197, updated May 9, 2023, Sections 3.2
>   and 4. https://doi.org/10.6028/NIST.FIPS.197-upd1

`AesField.params` (definition, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Aes/Arithmetic.lean#L35))

> Degree-eight parameters with lower coefficients of `X^4 + X^3 + X + 1` over `GF(2)`.

```lean
def params : ExtensionParams (ZMod 2)
```

`AesField` (abbreviation, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Aes/Arithmetic.lean#L44))

> The AES polynomial presentation, with eight coefficients in ascending degree order.

```lean
abbrev AesField : Type
```

`AesField.ofBitVec` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Aes/Arithmetic.lean#L49))

> Interpret the bits of a byte as polynomial coefficients, least significant bit first.

```lean
def ofBitVec (a : BitVec 8) : AesField
```

`AesField.toBitVec` (definition, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Aes/Arithmetic.lean#L52))

> Recover the byte whose bit `i` is the coefficient of `X^i`.

```lean
def toBitVec (a : AesField) : BitVec 8
```

`AesField.coeff_ofBitVec` (theorem, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Aes/Arithmetic.lean#L57))

> The coefficient at index `i` is the corresponding input bit, valued in `GF(2)`.

```lean
theorem coeff_ofBitVec (a : BitVec 8) (i : Fin 8) :
    Ext.coeff (ofBitVec a) i = if a.getLsbD i then 1 else 0
```

`AesField.getLsbD_toBitVec` (theorem, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Aes/Arithmetic.lean#L61))

> Decoding tests each coefficient against one in `GF(2)`.

```lean
theorem getLsbD_toBitVec (a : AesField) (i : Fin 8) :
    (toBitVec a).getLsbD i = decide (Ext.coeff a i = 1)
```

`AesField.toBitVec_ofBitVec` (theorem, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Aes/Arithmetic.lean#L67))

> Decoding an encoded byte recovers every input bit.

```lean
theorem toBitVec_ofBitVec (a : BitVec 8) : toBitVec (ofBitVec a) = a
```

`AesField.ofBitVec_toBitVec` (theorem, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Aes/Arithmetic.lean#L74))

> Encoding the decoded byte recovers every coefficient.

```lean
theorem ofBitVec_toBitVec (a : AesField) : ofBitVec (toBitVec a) = a
```

`AesField.equivBitVec` (definition, [line 82](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Aes/Arithmetic.lean#L82))

> The coordinate equivalence between AES elements and bytes.

```lean
def equivBitVec : AesField ≃ BitVec 8
```

`AesField.toBitVec_injective` (theorem, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Aes/Arithmetic.lean#L89))

> Equal byte encodings identify equal field elements.

```lean
theorem toBitVec_injective : Function.Injective toBitVec
```

`AesField.gen` (definition, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Aes/Arithmetic.lean#L92))

> The polynomial generator with coefficient one at `X` and zero elsewhere.

```lean
def gen : AesField
```

`AesField.gen_eq_ofBitVec` (theorem, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Aes/Arithmetic.lean#L95))

> The polynomial generator is the explicit coordinate byte two.

```lean
theorem gen_eq_ofBitVec : gen = ofBitVec (2#8)
```

`AesField.toBitVec_gen` (theorem, [line 106](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Aes/Arithmetic.lean#L106))

> The polynomial generator has only bit one set in its byte encoding.

```lean
theorem toBitVec_gen : toBitVec gen = 2#8
```

## Depends on

- [Computable arithmetic for monic quotient presentations](../../extension/arithmetic.md)

## Sources

- [CompPoly/Fields/Binary/Aes/Arithmetic.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Aes/Arithmetic.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.Aes.Arithmetic.json)
