---
catalog: module
lean: Montgomery.reduceNat, Montgomery.reduceNatQuotient, Montgomery.reduceNatQuotient_lt_two_mul, Montgomery.reduceNat_lt, Montgomery.dvd_add, Montgomery.reduceNatQuotient_cast, Montgomery.reduceNat_cast, Montgomery.natCast_inj_of_lt
statement: formalized
proof: formalized
---

# Montgomery Reduction

`CompPoly.Fields.Montgomery.Basic`, in [CompPoly/Fields/Montgomery/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Basic.lean), by Valerii Huhnin, Georgios Raikos.

> Radix-generic specification and correctness lemmas for single-word Montgomery reduction.
> Word-specific implementations refine these results in sibling modules.

`Montgomery.reduceNat` (definition, [line 25](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Basic.lean#L25))

> Natural-number Montgomery reduction used to specify the native-word reducer.

```lean
def reduceNat (R p negInv x : ℕ) : ℕ
```

`Montgomery.reduceNatQuotient` (definition, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Basic.lean#L31))

> The quotient before the final conditional subtraction in Montgomery reduction.

```lean
def reduceNatQuotient (R p negInv x : ℕ) : ℕ
```

`Montgomery.reduceNatQuotient_lt_two_mul` (theorem, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Basic.lean#L36))

> The pre-subtraction quotient is below twice the modulus.

```lean
theorem reduceNatQuotient_lt_two_mul (R p negInv x : ℕ)
    (hR : 0 < R) (hp : 0 < p) (hx : x < p * R) :
    reduceNatQuotient R p negInv x < 2 * p
```

`Montgomery.reduceNat_lt` (theorem, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Basic.lean#L52))

> Montgomery reduction returns a canonical representative.

```lean
theorem reduceNat_lt (R p negInv x : ℕ)
    (hR : 0 < R) (hp : 0 < p) (hx : x < p * R) :
    reduceNat R p negInv x < p
```

`Montgomery.dvd_add` (theorem, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Basic.lean#L66))

> The Montgomery divisibility identity: if `(negInv * p) % R = R - 1` (i.e.
> `negInv = -p⁻¹ mod R`), then `R ∣ x + ((x mod R)·negInv mod R)·p` for every `x`.

```lean
theorem dvd_add (R p negInv : ℕ) (hR : 0 < R)
    (hnegInv : negInv * p % R = R - 1) (x : ℕ) :
    R ∣ x + ((x % R * negInv) % R) * p
```

`Montgomery.reduceNatQuotient_cast` (theorem, [line 75](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Basic.lean#L75))

> The pre-subtraction quotient represents multiplication by `R⁻¹` in `ZMod p`.

```lean
theorem reduceNatQuotient_cast (R p negInv : ℕ) [Fact (Nat.Prime p)] (hR : 0 < R)
    (hnegInv : negInv * p % R = R - 1) (hRne : (R : ZMod p) ≠ 0) (x : ℕ) :
    (reduceNatQuotient R p negInv x : ZMod p) = (x : ZMod p) * (R : ZMod p)⁻¹
```

`Montgomery.reduceNat_cast` (theorem, [line 91](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Basic.lean#L91))

> Montgomery reduction represents multiplication by `R⁻¹` in `ZMod p`.

```lean
theorem reduceNat_cast (R p negInv : ℕ) [Fact (Nat.Prime p)] (hR : 0 < R)
    (hnegInv : negInv * p % R = R - 1) (hRne : (R : ZMod p) ≠ 0) (x : ℕ) :
    (reduceNat R p negInv x : ZMod p) = (x : ZMod p) * (R : ZMod p)⁻¹
```

`Montgomery.natCast_inj_of_lt` (theorem, [line 112](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Basic.lean#L112))

> Two naturals below `p` are equal once their `ZMod p` casts agree.

```lean
theorem natCast_inj_of_lt {p a b : ℕ} (h : (a : ZMod p) = (b : ZMod p))
    (ha : a < p) (hb : b < p) : a = b
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Fields/Montgomery/Basic.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Basic.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Montgomery.Basic.json)
