---
catalog: module
lean: Montgomery.Native64x4.adc_spec, Montgomery.Native64x4.sbb_spec, Montgomery.Native64x4.mulHi_spec, Montgomery.Native64x4.mac_spec, Montgomery.Native64x4.montM_toNat, Montgomery.Native64x4.Limbs4.zero_toNat, Montgomery.Native64x4.Limbs4.one_toNat, Montgomery.Native64x4.Limbs4.ofNat_toNat, Montgomery.Native64x4.Limbs4.toNat_lt, Montgomery.Native64x4.Limbs4.toNat_mod, Montgomery.Native64x4.Limbs4.ext_of_toNat, Montgomery.Native64x4.carry_chain_sum, Montgomery.Native64x4.borrow_chain_sum, Montgomery.Native64x4.addLimbs_spec, Montgomery.Native64x4.subLimbs_spec, Montgomery.Native64x4.condSub_toNat, Montgomery.Native64x4.condSub_lt, Montgomery.Native64x4.condSubWide_toNat, Montgomery.Native64x4.condSubWide_lt, Montgomery.Native64x4.add_toNat, Montgomery.Native64x4.add_lt, Montgomery.Native64x4.sub_toNat, Montgomery.Native64x4.sub_lt, Montgomery.Native64x4.neg_toNat, Montgomery.Native64x4.neg_lt
statement: formalized
proof: formalized
---

# Native Montgomery arithmetic over four 64-bit limbs

`CompPoly.Fields.Montgomery.Native64x4`, in [CompPoly/Fields/Montgomery/Native64x4.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean), by Georgios Raikos.

> Raw word operations for prime moduli below `2 ^ 256`, represented as four 64-bit limbs
> (`Limbs4`); the definitions live in the zero-import module `Montgomery/Native64x4Defs`.  Each
> word helper's specification exhibits the pair it returns, so a chain of `let (s, c) := ...`
> bindings unfolds to a linear system over naturals that `omega` closes.
>
> ## Main results
>
> * `condSub_toNat`, `condSubWide_toNat`, `add_toNat`, `sub_toNat`, `neg_toNat` — correctness
>   of the raw operations
> * `addLimbs_spec`, `subLimbs_spec` — the underlying carry/borrow chains
> * `mac_spec`, `mulHi_spec` — the widening multiply-accumulate

> ## Word-level specifications

`Montgomery.Native64x4.adc_spec` (theorem, [line 72](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L72))

> Add-with-carry, existential form: the exact sum identity with a one-bit carry.

```lean
theorem adc_spec (x y c : UInt64) (hc : c.toNat ≤ 1) :
    ∃ s co : UInt64, adc x y c = (s, co) ∧
      s.toNat + 2 ^ 64 * co.toNat = x.toNat + y.toNat + c.toNat ∧ co.toNat ≤ 1
```

`Montgomery.Native64x4.sbb_spec` (theorem, [line 91](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L91))

> Subtract-with-borrow, existential form: the exact difference identity with a one-bit
> borrow.

```lean
theorem sbb_spec (x y b : UInt64) (hb : b.toNat ≤ 1) :
    ∃ d bo : UInt64, sbb x y b = (d, bo) ∧
      d.toNat + y.toNat + b.toNat = x.toNat + 2 ^ 64 * bo.toNat ∧ bo.toNat ≤ 1
```

`Montgomery.Native64x4.mulHi_spec` (theorem, [line 117](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L117))

> The low and high words recompose the exact `64 × 64` product.

```lean
theorem mulHi_spec (a b : UInt64) :
    (a * b).toNat + 2 ^ 64 * (mulHi a b).toNat = a.toNat * b.toNat
```

`Montgomery.Native64x4.mac_spec` (theorem, [line 186](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L186))

> Multiply-accumulate, existential form: `t + a * b + c` never overflows two words.

```lean
theorem mac_spec (t a b c : UInt64) :
    ∃ lo hi : UInt64, mac t a b c = (lo, hi) ∧
      lo.toNat + 2 ^ 64 * hi.toNat = t.toNat + a.toNat * b.toNat + c.toNat
```

`Montgomery.Native64x4.montM_toNat` (theorem, [line 213](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L213))

> The Montgomery multiplier agrees with its natural-number specification.

```lean
theorem montM_toNat (s negInv : UInt64) :
    (montM s negInv).toNat = s.toNat * negInv.toNat % 2 ^ 64
```

> ## Four-limb values

`Montgomery.Native64x4.Limbs4.zero_toNat` (theorem, [line 221](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L221))

```lean
theorem zero_toNat : zero.toNat = 0
```

`Montgomery.Native64x4.Limbs4.one_toNat` (theorem, [line 223](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L223))

```lean
theorem one_toNat : one.toNat = 1
```

`Montgomery.Native64x4.Limbs4.ofNat_toNat` (theorem, [line 225](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L225))

```lean
theorem ofNat_toNat (n : ℕ) : (ofNat n).toNat = n % 2 ^ 256
```

`Montgomery.Native64x4.Limbs4.toNat_lt` (theorem, [line 230](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L230))

> A four-limb value is below `2 ^ 256`.

```lean
theorem toNat_lt (x : Limbs4) : x.toNat < 2 ^ 256
```

`Montgomery.Native64x4.Limbs4.toNat_mod` (theorem, [line 239](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L239))

> The low limb of a value is its residue modulo `2 ^ 64`.

```lean
theorem toNat_mod (x : Limbs4) : x.toNat % 2 ^ 64 = x.l0.toNat
```

`Montgomery.Native64x4.Limbs4.ext_of_toNat` (theorem, [line 245](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L245))

> Limb vectors are determined by their value.

```lean
theorem ext_of_toNat {x y : Limbs4} (h : x.toNat = y.toNat) : x = y
```

> ### Chain lemmas

`Montgomery.Native64x4.carry_chain_sum` (theorem, [line 270](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L270))

> Weighted telescoping of a four-step carry chain.

```lean
theorem carry_chain_sum {x0 x1 x2 x3 y0 y1 y2 y3 s0 s1 s2 s3 cin c0 c1 c2 c3 : ℕ}
    (e0 : s0 + 2 ^ 64 * c0 = x0 + y0 + cin)
    (e1 : s1 + 2 ^ 64 * c1 = x1 + y1 + c0)
    (e2 : s2 + 2 ^ 64 * c2 = x2 + y2 + c1)
    (e3 : s3 + 2 ^ 64 * c3 = x3 + y3 + c2) :
    s0 + 2 ^ 64 * s1 + 2 ^ 128 * s2 + 2 ^ 192 * s3 + 2 ^ 256 * c3 =
      (x0 + 2 ^ 64 * x1 + 2 ^ 128 * x2 + 2 ^ 192 * x3) +
        (y0 + 2 ^ 64 * y1 + 2 ^ 128 * y2 + 2 ^ 192 * y3) + cin
```

`Montgomery.Native64x4.borrow_chain_sum` (theorem, [line 281](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L281))

> Weighted telescoping of a four-step borrow chain.

```lean
theorem borrow_chain_sum {x0 x1 x2 x3 y0 y1 y2 y3 m0 m1 m2 m3 bin b0 b1 b2 b3 : ℕ}
    (e0 : m0 + y0 + bin = x0 + 2 ^ 64 * b0)
    (e1 : m1 + y1 + b0 = x1 + 2 ^ 64 * b1)
    (e2 : m2 + y2 + b1 = x2 + 2 ^ 64 * b2)
    (e3 : m3 + y3 + b2 = x3 + 2 ^ 64 * b3) :
    (m0 + 2 ^ 64 * m1 + 2 ^ 128 * m2 + 2 ^ 192 * m3) +
        (y0 + 2 ^ 64 * y1 + 2 ^ 128 * y2 + 2 ^ 192 * y3) + bin =
      x0 + 2 ^ 64 * x1 + 2 ^ 128 * x2 + 2 ^ 192 * x3 + 2 ^ 256 * b3
```

> ### Branch lemmas

> ## Limbwise addition and subtraction

`Montgomery.Native64x4.addLimbs_spec` (theorem, [line 327](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L327))

> The limbwise sum and the top carry recompose the sum of the inputs.

```lean
theorem addLimbs_spec (a b : Limbs4) :
    ∃ s0 s1 s2 s3 c : UInt64, addLimbs a b = (s0, s1, s2, s3, c) ∧ c.toNat ≤ 1 ∧
      (⟨s0, s1, s2, s3⟩ : Limbs4).toNat + 2 ^ 256 * c.toNat = a.toNat + b.toNat
```

`Montgomery.Native64x4.subLimbs_spec` (theorem, [line 343](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L343))

> The limbwise difference and the final borrow recompose the difference of the inputs.

```lean
theorem subLimbs_spec (a b : Limbs4) :
    ∃ d0 d1 d2 d3 bo : UInt64, subLimbs a b = (d0, d1, d2, d3, bo) ∧ bo.toNat ≤ 1 ∧
      (⟨d0, d1, d2, d3⟩ : Limbs4).toNat + b.toNat = a.toNat + 2 ^ 256 * bo.toNat
```

> ## Conditional subtraction

`Montgomery.Native64x4.condSub_toNat` (theorem, [line 361](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L361))

> `condSub` subtracts the modulus exactly when the input is at least the modulus.

```lean
theorem condSub_toNat (q t : Limbs4) :
    (condSub q t).toNat = if t.toNat < q.toNat then t.toNat else t.toNat - q.toNat
```

`Montgomery.Native64x4.condSub_lt` (theorem, [line 375](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L375))

> `condSub` returns a canonical representative for inputs below `2 * q`.

```lean
theorem condSub_lt (q t : Limbs4) (h : t.toNat < 2 * q.toNat) :
    (condSub q t).toNat < q.toNat
```

`Montgomery.Native64x4.condSubWide_toNat` (theorem, [line 382](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L382))

> `condSubWide` subtracts the modulus exactly when an accumulator below `2 * q` is at least
> the modulus.

```lean
theorem condSubWide_toNat (q : Limbs4) (t : State5) (h : t.toNat < 2 * q.toNat) :
    (condSubWide q t).toNat = if t.toNat < q.toNat then t.toNat else t.toNat - q.toNat
```

`Montgomery.Native64x4.condSubWide_lt` (theorem, [line 405](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L405))

> `condSubWide` returns a canonical representative for accumulators below `2 * q`.

```lean
theorem condSubWide_lt (q : Limbs4) (t : State5) (h : t.toNat < 2 * q.toNat) :
    (condSubWide q t).toNat < q.toNat
```

> ## Field operations

`Montgomery.Native64x4.add_toNat` (theorem, [line 413](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L413))

> Modular addition is correct for canonical inputs of any modulus.

```lean
theorem add_toNat (q a b : Limbs4) (haq : a.toNat < q.toNat) (hbq : b.toNat < q.toNat) :
    (add q a b).toNat = (a.toNat + b.toNat) % q.toNat
```

`Montgomery.Native64x4.add_lt` (theorem, [line 436](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L436))

```lean
theorem add_lt (q a b : Limbs4) (haq : a.toNat < q.toNat) (hbq : b.toNat < q.toNat) :
    (add q a b).toNat < q.toNat
```

`Montgomery.Native64x4.sub_toNat` (theorem, [line 442](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L442))

> Modular subtraction is correct for canonical inputs of any modulus.

```lean
theorem sub_toNat (q a b : Limbs4) (haq : a.toNat < q.toNat) (hbq : b.toNat < q.toNat) :
    (sub q a b).toNat = (a.toNat + (q.toNat - b.toNat)) % q.toNat
```

`Montgomery.Native64x4.sub_lt` (theorem, [line 458](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L458))

```lean
theorem sub_lt (q a b : Limbs4) (haq : a.toNat < q.toNat) (hbq : b.toNat < q.toNat) :
    (sub q a b).toNat < q.toNat
```

`Montgomery.Native64x4.neg_toNat` (theorem, [line 464](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L464))

> Modular negation is correct for canonical inputs of any modulus.

```lean
theorem neg_toNat (q a : Limbs4) (haq : a.toNat < q.toNat) :
    (neg q a).toNat = (q.toNat - a.toNat) % q.toNat
```

`Montgomery.Native64x4.neg_lt` (theorem, [line 470](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean#L470))

```lean
theorem neg_lt (q a : Limbs4) (haq : a.toNat < q.toNat) : (neg q a).toNat < q.toNat
```

## Depends on

- [Four-limb Montgomery arithmetic: runtime definitions (zero-import)](native64x4defs.md)

## Sources

- [CompPoly/Fields/Montgomery/Native64x4.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Montgomery.Native64x4.json)
