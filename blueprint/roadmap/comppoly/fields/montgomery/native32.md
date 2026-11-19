---
catalog: module
lean: Montgomery.Native32.reduceRaw, Montgomery.Native32.reduceQuotient, Montgomery.Native32.conditionalSubtract, Montgomery.Native32.reduceRaw_eq_conditionalSubtract, Montgomery.Native32.reduceQuotient_toNat, Montgomery.Native32.conditionalSubtract_toNat, Montgomery.Native32.reduceRaw_toNat, Montgomery.Native32.conditionalSubtract_lt, Montgomery.Native32.conditionalSubtract_cast, Montgomery.Native32.reduceRaw_lt, Montgomery.Native32.reduceRaw_cast
statement: formalized
proof: formalized
---

# Native 32-bit Montgomery Reduction

`CompPoly.Fields.Montgomery.Native32`, in [CompPoly/Fields/Montgomery/Native32.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32.lean), by Valerii Huhnin, Georgios Raikos.

> Raw word operations for Montgomery reduction with radix `2 ^ 32`.

`Montgomery.Native32.reduceRaw` (definition, [line 23](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32.lean#L23))

> Montgomery reduction.

```lean
def reduceRaw (p32 : UInt32) (p64 : UInt64) (negInv : UInt32) (x : UInt64) : UInt32
```

`Montgomery.Native32.reduceQuotient` (definition, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32.lean#L29))

> The native pre-subtraction quotient in 32-bit Montgomery reduction.

```lean
def reduceQuotient (negInv : UInt32) (p x : UInt64) : UInt32
```

`Montgomery.Native32.conditionalSubtract` (definition, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32.lean#L34))

> Conditional subtraction of the modulus in 32-bit Montgomery reduction.

```lean
def conditionalSubtract (p32 : UInt32) (u : UInt32) : UInt32
```

`Montgomery.Native32.reduceRaw_eq_conditionalSubtract` (theorem, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32.lean#L39))

```lean
theorem reduceRaw_eq_conditionalSubtract :
    reduceRaw p32 p64 negInv x =
      conditionalSubtract p32 (reduceQuotient negInv p64 x)
```

`Montgomery.Native32.reduceQuotient_toNat` (theorem, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32.lean#L44))

> The native quotient agrees with the `Nat`-level Montgomery quotient.

```lean
theorem reduceQuotient_toNat (hp_pos : 0 < p64.toNat) (hbound : p64.toNat < 2 ^ 31)
    (h : x.toNat < p64.toNat * 2 ^ 32) :
    (reduceQuotient negInv p64 x).toNat =
      reduceNatQuotient (2 ^ 32) p64.toNat negInv.toNat x.toNat
```

`Montgomery.Native32.conditionalSubtract_toNat` (theorem, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32.lean#L70))

```lean
theorem conditionalSubtract_toNat :
    (conditionalSubtract p32 u).toNat =
      if u.toNat < p32.toNat then u.toNat else u.toNat - p32.toNat
```

`Montgomery.Native32.reduceRaw_toNat` (theorem, [line 82](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32.lean#L82))

> Native Montgomery reduction agrees with the natural-number specification.

```lean
theorem reduceRaw_toNat (hp32 : p32.toNat = modulus) (hp64 : p64.toNat = modulus)
    (hp_pos : 0 < modulus) (hp_bound : modulus < 2 ^ 31)
    (h : x.toNat < modulus * 2 ^ 32) :
    (reduceRaw p32 p64 negInv x).toNat =
      reduceNat (2 ^ 32) modulus negInv.toNat x.toNat
```

`Montgomery.Native32.conditionalSubtract_lt` (theorem, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32.lean#L95))

```lean
theorem conditionalSubtract_lt (h : u.toNat < 2 * p32.toNat) :
    (conditionalSubtract p32 u).toNat < p32.toNat
```

`Montgomery.Native32.conditionalSubtract_cast` (theorem, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32.lean#L107))

```lean
theorem conditionalSubtract_cast :
    ((conditionalSubtract p32 u).toNat : ZMod p32.toNat) =
      (u.toNat : ZMod p32.toNat)
```

`Montgomery.Native32.reduceRaw_lt` (theorem, [line 123](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32.lean#L123))

```lean
theorem reduceRaw_lt (hp : p32.toNat = p64.toNat) (hp_pos : 0 < p64.toNat)
    (hp_bound : p64.toNat < 2 ^ 31)
    (h : x.toNat < p64.toNat * 2 ^ 32) :
    (reduceRaw p32 p64 negInv x).toNat < p32.toNat
```

`Montgomery.Native32.reduceRaw_cast` (theorem, [line 131](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32.lean#L131))

```lean
theorem reduceRaw_cast [Fact (Nat.Prime modulus)]
    (hp32 : p32.toNat = modulus) (hp64 : p64.toNat = modulus)
    (hp_pos : 0 < modulus) (hp_bound : modulus < 2 ^ 31)
    (hnegInv : negInv.toNat * modulus % 2 ^ 32 = 2 ^ 32 - 1)
    (hRne : ((2 ^ 32 : ℕ) : ZMod modulus) ≠ 0)
    (h : x.toNat < modulus * 2 ^ 32) :
    ((reduceRaw p32 p64 negInv x).toNat : ZMod modulus) =
      (x.toNat : ZMod modulus) * ((2 ^ 32 : ℕ) : ZMod modulus)⁻¹
```

## Depends on

- [Montgomery Reduction](basic.md)

## Sources

- [CompPoly/Fields/Montgomery/Native32.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Montgomery.Native32.json)
