---
catalog: module
lean: Montgomery.Native64x4.sum4_mul, Montgomery.Native64x4.mul_sum4, Montgomery.Native64x4.State5.zero_toNat, Montgomery.Native64x4.State5.toNat_eq, Montgomery.Native64x4.mulAccum_spec, Montgomery.Native64x4.mulReduce_spec, Montgomery.Native64x4.mulRound_spec, Montgomery.Native64x4.mul_spec
statement: formalized
proof: formalized
---

# Correctness of four-limb CIOS Montgomery multiplication

`CompPoly.Fields.Montgomery.Native64x4Mul`, in [CompPoly/Fields/Montgomery/Native64x4Mul.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Mul.lean), by Georgios Raikos.

> A round accumulates `a * bi` exactly (`mulAccum_spec`) and cancels the low limb against a
> multiple of the modulus (`mulReduce_spec`); folding four rounds gives
> `2 ^ 256 * ⟦t₄⟧ = ⟦a⟧ * ⟦b⟧ + M * q`, the Montgomery product up to the final conditional
> subtraction.
>
> ## Main results
>
> * `mulRound_spec` — the round invariant with the `2 * q` bound
> * `mul_spec` — `mul` is canonical and satisfies `2 ^ 256 * ⟦mul a b⟧ ≡ ⟦a⟧ * ⟦b⟧ [MOD q]`

> ### Arithmetic helpers

`Montgomery.Native64x4.sum4_mul` (theorem, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Mul.lean#L33))

> Scalar multiplication distributes over a limb recomposition.

```lean
theorem sum4_mul (a0 a1 a2 a3 b : ℕ) :
    (a0 + 2 ^ 64 * a1 + 2 ^ 128 * a2 + 2 ^ 192 * a3) * b =
      a0 * b + 2 ^ 64 * (a1 * b) + 2 ^ 128 * (a2 * b) + 2 ^ 192 * (a3 * b)
```

`Montgomery.Native64x4.mul_sum4` (theorem, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Mul.lean#L39))

> Scalar multiplication distributes over a limb recomposition, from the left.

```lean
theorem mul_sum4 (b a0 a1 a2 a3 : ℕ) :
    b * (a0 + 2 ^ 64 * a1 + 2 ^ 128 * a2 + 2 ^ 192 * a3) =
      b * a0 + 2 ^ 64 * (b * a1) + 2 ^ 128 * (b * a2) + 2 ^ 192 * (b * a3)
```

> ### The accumulator

`Montgomery.Native64x4.State5.zero_toNat` (theorem, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Mul.lean#L65))

```lean
theorem State5.zero_toNat : State5.zero.toNat = 0
```

`Montgomery.Native64x4.State5.toNat_eq` (theorem, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Mul.lean#L69))

> The value of an accumulator in terms of its limbs.

```lean
theorem State5.toNat_eq (t : State5) :
    t.toNat = t.t0.toNat + 2 ^ 64 * t.t1.toNat + 2 ^ 128 * t.t2.toNat + 2 ^ 192 * t.t3.toNat +
      2 ^ 256 * t.t4.toNat
```

> ### The accumulation step

`Montgomery.Native64x4.mulAccum_spec` (theorem, [line 77](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Mul.lean#L77))

> `mulAccum` adds `a * bi` to the accumulator exactly, with a one-bit carry limb.

```lean
theorem mulAccum_spec (a : Limbs4) (bi : UInt64) (t : State5) :
    (mulAccum a bi t).t5.toNat ≤ 1 ∧
      (mulAccum a bi t).toNat = t.toNat + a.toNat * bi.toNat
```

> ### The reduction step

`Montgomery.Native64x4.mulReduce_spec` (theorem, [line 98](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Mul.lean#L98))

> `mulReduce` adds the multiple of the modulus that cancels the low limb, so dropping that
> limb divides by `2 ^ 64` exactly.

```lean
theorem mulReduce_spec (q : Limbs4) (negInv : UInt64) (s : State6) (hs5 : s.t5.toNat ≤ 1)
    (hnq : negInv.toNat * q.toNat % 2 ^ 64 = 2 ^ 64 - 1) :
    2 ^ 64 * (mulReduce q negInv s).toNat =
      s.toNat + (montM s.t0 negInv).toNat * q.toNat
```

> ### The round invariant

`Montgomery.Native64x4.mulRound_spec` (theorem, [line 128](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Mul.lean#L128))

> The CIOS round invariant: one round accumulates `a * bi` and cancels the low limb against
> a multiple `m` of the modulus; the accumulator stays below `2 * q`.

```lean
theorem mulRound_spec (q a : Limbs4) (negInv bi : UInt64) (t : State5)
    (hnq : negInv.toNat * q.toNat % 2 ^ 64 = 2 ^ 64 - 1)
    (haq : a.toNat < q.toNat) (htq : t.toNat < 2 * q.toNat) :
    (mulRound q negInv a bi t).toNat < 2 * q.toNat ∧
      ∃ m : ℕ, m < 2 ^ 64 ∧
        2 ^ 64 * (mulRound q negInv a bi t).toNat =
          t.toNat + a.toNat * bi.toNat + m * q.toNat
```

> ### The four-round fold

`Montgomery.Native64x4.mul_spec` (theorem, [line 174](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Mul.lean#L174))

> Montgomery multiplication is canonical and computes `a * b * (2 ^ 256)⁻¹ mod q`.

```lean
theorem mul_spec (q : Limbs4) (negInv : UInt64) (a b : Limbs4)
    (hnq : negInv.toNat * q.toNat % 2 ^ 64 = 2 ^ 64 - 1) (haq : a.toNat < q.toNat) :
    (mul q negInv a b).toNat < q.toNat ∧
      2 ^ 256 * (mul q negInv a b).toNat ≡ a.toNat * b.toNat [MOD q.toNat]
```

## Depends on

- [Four-limb Montgomery arithmetic: runtime definitions (zero-import)](native64x4defs.md)

## Proof depends on

- [Montgomery Reduction](basic.md)
- [Native Montgomery arithmetic over four 64-bit limbs](native64x4.md)

## Sources

- [CompPoly/Fields/Montgomery/Native64x4Mul.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Mul.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Montgomery.Native64x4Mul.json)
