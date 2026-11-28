---
catalog: module
lean: BinaryField.B128, BinaryField.B256, BinaryField.to256, BinaryField.to256_toNat, BinaryField.zeroExtendTo, BinaryField.toNat_zeroExtendTo, BinaryField.to256_eq_zeroExtendTo, BinaryField.carryLessMul, BinaryField.clMul, BinaryField.clMul_eq_carryLessMul, BinaryField.clSq, BinaryField.fold_range_xor_eq_foldl
statement: formalized
proof: formalized
---

# Binary polynomial word arithmetic

`CompPoly.Fields.Binary.Common.Arithmetic`, in [CompPoly/Fields/Binary/Common/Arithmetic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Common/Arithmetic.lean), by Chung Thai Nguyen, Quang Dao, Derek Sorensen, Dimitris Mitsios.

> A word's bit `i` represents the coefficient of `X^i`. Changing word width
> zero-extends or truncates the coefficient vector. Carry-less multiplication
> accumulates shifted words using XOR and truncates at the chosen result width.
> A width at least twice the operand width preserves the full polynomial product.
> The 128-bit specialization returns a 256-bit product.
>
> Polynomial interpretation and its correspondence proofs are available through
> `CompPoly.Fields.Binary.Common`.

`BinaryField.B128` (abbreviation, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Common/Arithmetic.lean#L32))

```lean
abbrev B128
```

`BinaryField.B256` (abbreviation, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Common/Arithmetic.lean#L33))

```lean
abbrev B256
```

`BinaryField.to256` (definition, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Common/Arithmetic.lean#L36))

```lean
def to256 (v : B128) : B256
```

`BinaryField.to256_toNat` (lemma, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Common/Arithmetic.lean#L38))

```lean
lemma to256_toNat (v : B128) : (to256 v).toNat = v.toNat
```

`BinaryField.zeroExtendTo` (definition, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Common/Arithmetic.lean#L65))

> Resize a bit vector by zero extension or truncation to the target width.

```lean
def zeroExtendTo {v w : ℕ} (a : BitVec v) : BitVec w
```

`BinaryField.toNat_zeroExtendTo` (theorem, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Common/Arithmetic.lean#L67))

```lean
theorem toNat_zeroExtendTo {v w : ℕ} (a : BitVec v) (h : v ≤ w) :
    (zeroExtendTo (w := w) a).toNat = a.toNat
```

`BinaryField.to256_eq_zeroExtendTo` (theorem, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Common/Arithmetic.lean#L74))

> `to256` is the 128-to-256 instance of `zeroExtendTo`.

```lean
theorem to256_eq_zeroExtendTo (v : B128) : to256 v = zeroExtendTo v
```

`BinaryField.carryLessMul` (definition, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Common/Arithmetic.lean#L78))

> Multiply binary polynomial coefficients using XOR and shifts, retaining the lowest `w`
> bits. If `v + v ≤ w`, every coefficient of the full product is retained.

```lean
def carryLessMul {v w : ℕ} (a b : BitVec v) : BitVec w
```

`BinaryField.clMul` (definition, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Common/Arithmetic.lean#L84))

> The full carry-less product of two 128-bit polynomial coefficient vectors.

```lean
def clMul (a b : B128) : B256
```

`BinaryField.clMul_eq_carryLessMul` (theorem, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Common/Arithmetic.lean#L86))

```lean
theorem clMul_eq_carryLessMul (a b : B128) : clMul a b = carryLessMul (w := 256) a b
```

`BinaryField.clSq` (definition, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Common/Arithmetic.lean#L89))

> Carry-less squaring of a 128-bit vector.

```lean
def clSq (a : B128) : B256
```

`BinaryField.fold_range_xor_eq_foldl` (lemma, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Common/Arithmetic.lean#L92))

```lean
lemma fold_range_xor_eq_foldl {w : Nat} (n : Nat) (f : Nat → BitVec w) :
    (Finset.range n).fold BitVec.xor 0 f =
    Fin.foldl n (fun acc i => acc ^^^ (f i)) 0
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Fields/Binary/Common/Arithmetic.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Common/Arithmetic.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.Common.Arithmetic.json)
