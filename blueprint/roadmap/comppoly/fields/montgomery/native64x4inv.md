---
catalog: module
lean: Montgomery.Native64x4.subLimbs_borrow_eq_one_iff, Montgomery.Native64x4.mulWord_spec, Montgomery.Native64x4.add5_spec, Montgomery.Native64x4.lincombTail_lt, Montgomery.Native64x4.gcdLinearCombMontyRed_lt, Montgomery.Native64x4.gcdMainLoop_bounded, Montgomery.Native64x4.gcdFinalChunks_lt, Montgomery.Native64x4.gcdInvCandidate_lt, Montgomery.Native64x4.gcdInvCandidate_lt_modulus, Montgomery.Native64x4.montPow_eq_mul_pow, Montgomery.Native64x4.montPow_eq_inv, Montgomery.Native64x4.invGcdRaw_eq_inv, Montgomery.Native64x4.FastField.invGcd, Montgomery.Native64x4.FastField.invGcd_eq_inv
statement: formalized
proof: formalized
---

# Fast inversion for four-limb Montgomery fields

`CompPoly.Fields.Montgomery.Native64x4Inv`, in [CompPoly/Fields/Montgomery/Native64x4Inv.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Inv.lean), by Georgios Raikos.

> Correctness of the checked inversion of `Montgomery/Native64x4InvDefs`: `invGcdRaw`
> computes the field inverse and `FastField.invGcd` is its proof-carrying wrapper.  The
> divstep coefficient bound comes from `Montgomery/Divstep`.  This module proves the mac-width
> safety of the candidate for the five-word linear combinations.

> ## Order from the borrow chain

`Montgomery.Native64x4.subLimbs_borrow_eq_one_iff` (theorem, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Inv.lean#L29))

> The final borrow decides the numeric order.

```lean
theorem subLimbs_borrow_eq_one_iff {a b : Limbs4} {d0 d1 d2 d3 bo : UInt64}
    (e : subLimbs a b = (d0, d1, d2, d3, bo)) : bo = 1 ↔ a.toNat < b.toNat
```

> ## Five-word specifications

`Montgomery.Native64x4.mulWord_spec` (theorem, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Inv.lean#L42))

> `mulWord` is the exact five-word product.

```lean
theorem mulWord_spec (x : Limbs4) (k : UInt64) :
    ∃ w0 w1 w2 w3 w4 : UInt64, mulWord x k = (w0, w1, w2, w3, w4) ∧
      w0.toNat + 2 ^ 64 * w1.toNat + 2 ^ 128 * w2.toNat + 2 ^ 192 * w3.toNat +
        2 ^ 256 * w4.toNat = x.toNat * k.toNat
```

`Montgomery.Native64x4.add5_spec` (theorem, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Inv.lean#L56))

> `add5` is the exact five-word sum with a one-bit carry.

```lean
theorem add5_spec (a0 a1 a2 a3 a4 b0 b1 b2 b3 b4 : UInt64) :
    ∃ s0 s1 s2 s3 s4 c : UInt64,
      add5 a0 a1 a2 a3 a4 b0 b1 b2 b3 b4 = (s0, s1, s2, s3, s4, c) ∧ c.toNat ≤ 1 ∧
      s0.toNat + 2 ^ 64 * s1.toNat + 2 ^ 128 * s2.toNat + 2 ^ 192 * s3.toNat +
          2 ^ 256 * s4.toNat + 2 ^ 320 * c.toNat =
        (a0.toNat + 2 ^ 64 * a1.toNat + 2 ^ 128 * a2.toNat + 2 ^ 192 * a3.toNat +
          2 ^ 256 * a4.toNat) +
        (b0.toNat + 2 ^ 64 * b1.toNat + 2 ^ 128 * b2.toNat + 2 ^ 192 * b3.toNat +
          2 ^ 256 * b4.toNat)
```

> ## Mac-width safety of the candidate

`Montgomery.Native64x4.lincombTail_lt` (theorem, [line 79](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Inv.lean#L79))

> The Montgomery linear combination stays canonical for magnitudes below the modulus.

```lean
theorem lincombTail_lt {q uS vS : Limbs4} {negInv F G : UInt64} (hq0 : 0 < q.toNat)
    (hnq : negInv.toNat * q.toNat % 2 ^ 64 = 2 ^ 64 - 1)
    (huS : uS.toNat ≤ q.toNat) (hvS : vS.toNat ≤ q.toNat)
    (hFG : F.toNat + G.toNat ≤ 2 ^ 31) :
    (lincombTail q negInv uS vS F G).toNat < q.toNat
```

`Montgomery.Native64x4.gcdLinearCombMontyRed_lt` (theorem, [line 119](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Inv.lean#L119))

> The Montgomery lincomb stays canonical for canonical inputs.

```lean
theorem gcdLinearCombMontyRed_lt {q : Limbs4} {negInv : UInt64} {u v : Limbs4} {f g : Int}
    (hq0 : 0 < q.toNat) (hnq : negInv.toNat * q.toNat % 2 ^ 64 = 2 ^ 64 - 1)
    (huq : u.toNat < q.toNat) (hvq : v.toNat < q.toNat)
    (hfg : f.natAbs + g.natAbs ≤ 2 ^ 31) :
    (gcdLinearCombMontyRed q negInv u v f g).toNat < q.toNat
```

`Montgomery.Native64x4.gcdMainLoop_bounded` (theorem, [line 149](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Inv.lean#L149))

> The main loop keeps the Montgomery pair canonical.

```lean
theorem gcdMainLoop_bounded {q : Limbs4} {negInv : UInt64} {rounds : ℕ}
    {a u b v A U B V : Limbs4}
    (hq0 : 0 < q.toNat) (hnq : negInv.toNat * q.toNat % 2 ^ 64 = 2 ^ 64 - 1)
    (huq : u.toNat < q.toNat) (hvq : v.toNat < q.toNat)
    (heq : gcdMainLoop q negInv rounds a u b v = (A, U, B, V)) :
    U.toNat < q.toNat ∧ V.toNat < q.toNat
```

`Montgomery.Native64x4.gcdFinalChunks_lt` (theorem, [line 199](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Inv.lean#L199))

> The final chunks stay canonical for canonical inputs.

```lean
theorem gcdFinalChunks_lt {q : Limbs4} {negInv : UInt64} {finalRounds : ℕ}
    {a u b v : Limbs4} (hfr : finalRounds ≤ 62)
    (hq0 : 0 < q.toNat) (hnq : negInv.toNat * q.toNat % 2 ^ 64 = 2 ^ 64 - 1)
    (huq : u.toNat < q.toNat) (hvq : v.toNat < q.toNat) :
    (gcdFinalChunks q negInv finalRounds a u b v).toNat < q.toNat
```

`Montgomery.Native64x4.gcdInvCandidate_lt` (theorem, [line 227](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Inv.lean#L227))

> The candidate is canonical.

```lean
theorem gcdInvCandidate_lt {modulus : ℕ} [P : GcdData modulus] {q x : Limbs4}
    {negInv : UInt64} (hqm : q.toNat = modulus) (hq0 : 0 < q.toNat)
    (hnq : negInv.toNat * q.toNat % 2 ^ 64 = 2 ^ 64 - 1) :
    (gcdInvCandidate modulus q negInv x).toNat < q.toNat
```

`Montgomery.Native64x4.gcdInvCandidate_lt_modulus` (theorem, [line 251](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Inv.lean#L251))

> With the class data, the candidate is canonical for any input.

```lean
theorem gcdInvCandidate_lt_modulus [GcdData modulus] (x : Limbs4) :
    (gcdInvCandidate modulus P.modulusLimbs P.montgomeryNegInv x).toNat < modulus
```

> ## The Fermat fallback and the checked raw inversion

`Montgomery.Native64x4.montPow_eq_mul_pow` (theorem, [line 271](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Inv.lean#L271))

> `montPow` computes `acc · xⁿ`.

```lean
theorem montPow_eq_mul_pow (acc x : FastField modulus) (n : ℕ) :
    montPow P.modulusLimbs P.montgomeryNegInv acc.val x.val n = (acc * x ^ n).val
```

`Montgomery.Native64x4.montPow_eq_inv` (theorem, [line 298](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Inv.lean#L298))

> The `montPow` fallback computes the field inverse.

```lean
theorem montPow_eq_inv (x : FastField modulus) :
    montPow P.modulusLimbs P.montgomeryNegInv P.rModModulus x.val (modulus - 2)
      = (x⁻¹).val
```

`Montgomery.Native64x4.invGcdRaw_eq_inv` (theorem, [line 342](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Inv.lean#L342))

> `invGcdRaw` computes the field inverse.

```lean
theorem invGcdRaw_eq_inv [GcdData modulus] (x : FastField modulus) :
    invGcdRaw modulus P.modulusLimbs P.montgomeryNegInv P.rModModulus x.val
      = (x⁻¹).val
```

> ## The proof-carrying wrapper

`Montgomery.Native64x4.FastField.invGcd` (definition, [line 357](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Inv.lean#L357))

> The proof-carrying wrapper of the checked inversion `invGcdRaw`.

```lean
def invGcd [GcdData modulus] (x : FastField modulus) : FastField modulus
```

`Montgomery.Native64x4.FastField.invGcd_eq_inv` (theorem, [line 364](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Inv.lean#L364))

> `invGcd` agrees with the `Field` inverse.

```lean
theorem invGcd_eq_inv [GcdData modulus] (x : FastField modulus) :
    invGcd x = x⁻¹
```

## Depends on

- [Fast four-limb Montgomery fields](native64x4field.md)
- [Four-limb inversion: runtime definitions (Mathlib-free)](native64x4invdefs.md)

## Proof depends on

- [Word-sized divsteps: coefficient bounds](divstep.md)

## Sources

- [CompPoly/Fields/Montgomery/Native64x4Inv.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Inv.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Montgomery.Native64x4Inv.json)
