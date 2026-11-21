---
catalog: module
lean: Montgomery.Native64x8.sum8_mul, Montgomery.Native64x8.mul_sum8, Montgomery.Native64x8.Limbs8.toNat_mod, Montgomery.Native64x8.State9.zero_bounded, Montgomery.Native64x8.State9.zero_toNat, Montgomery.Native64x8.State9.toNat_eq, Montgomery.Native64x8.mulAccum_spec, Montgomery.Native64x8.mulReduce_spec, Montgomery.Native64x8.mulRound_spec, Montgomery.Native64x8.mul_spec
statement: formalized
proof: formalized
---

# Correctness of eight-limb CIOS Montgomery multiplication

`CompPoly.Fields.Montgomery.Native64x8Mul`, in [CompPoly/Fields/Montgomery/Native64x8Mul.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Mul.lean), by Gregor Mitscha-Baude.

> A CIOS round is the composition of an accumulation and a reduction step:
>
> * `mulAccum a bi t` accumulates `a * bi` into the accumulator without losing information,
>   `⟦mulAccum a bi t⟧ = ⟦t⟧ + ⟦a⟧ * bi`;
> * `mulReduce q negInv s` adds the multiple `m * q` of the modulus that cancels the low limb
>   and drops that limb, `2 ^ 32 * ⟦mulReduce q negInv s⟧ = ⟦s⟧ + m * q`.
>
> Composing them gives the round invariant `2 ^ 32 * ⟦mulRound⟧ = ⟦t⟧ + ⟦a⟧ * bi + m * q`, and
> folding eight rounds gives `2 ^ 256 * ⟦t₈⟧ = ⟦a⟧ * ⟦b⟧ + M * q`, so the accumulator is the
> Montgomery product up to the final conditional subtraction.
>
> ## Main results
>
> * `mulAccum_spec`, `mulReduce_spec` — the two halves of a round
> * `mulRound_spec` — the round invariant, with limb bounds and the `2 * q` bound
> * `mul_spec` — `mul` is canonical and satisfies `2 ^ 256 * ⟦mul a b⟧ ≡ ⟦a⟧ * ⟦b⟧ [MOD q]`

> ### Arithmetic helpers

`Montgomery.Native64x8.sum8_mul` (theorem, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Mul.lean#L40))

> Scalar multiplication distributes over a limb recomposition.

```lean
theorem sum8_mul (a0 a1 a2 a3 a4 a5 a6 a7 b : ℕ) :
    (a0 + 2 ^ 32 * a1 + 2 ^ 64 * a2 + 2 ^ 96 * a3 + 2 ^ 128 * a4 + 2 ^ 160 * a5 +
        2 ^ 192 * a6 + 2 ^ 224 * a7) * b =
      a0 * b + 2 ^ 32 * (a1 * b) + 2 ^ 64 * (a2 * b) + 2 ^ 96 * (a3 * b) +
        2 ^ 128 * (a4 * b) + 2 ^ 160 * (a5 * b) + 2 ^ 192 * (a6 * b) + 2 ^ 224 * (a7 * b)
```

`Montgomery.Native64x8.mul_sum8` (theorem, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Mul.lean#L48))

> Scalar multiplication distributes over a limb recomposition, from the left.

```lean
theorem mul_sum8 (b a0 a1 a2 a3 a4 a5 a6 a7 : ℕ) :
    b * (a0 + 2 ^ 32 * a1 + 2 ^ 64 * a2 + 2 ^ 96 * a3 + 2 ^ 128 * a4 + 2 ^ 160 * a5 +
        2 ^ 192 * a6 + 2 ^ 224 * a7) =
      b * a0 + 2 ^ 32 * (b * a1) + 2 ^ 64 * (b * a2) + 2 ^ 96 * (b * a3) +
        2 ^ 128 * (b * a4) + 2 ^ 160 * (b * a5) + 2 ^ 192 * (b * a6) + 2 ^ 224 * (b * a7)
```

`Montgomery.Native64x8.Limbs8.toNat_mod` (theorem, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Mul.lean#L56))

> The low limb of a bounded value is its residue modulo `2 ^ 32`.

```lean
theorem Limbs8.toNat_mod (x : Limbs8) (h : x.l0.toNat < 2 ^ 32) :
    x.toNat % 2 ^ 32 = x.l0.toNat
```

> ### The accumulator

`Montgomery.Native64x8.State9.zero_bounded` (theorem, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Mul.lean#L95))

```lean
theorem State9.zero_bounded : State9.zero.Bounded
```

`Montgomery.Native64x8.State9.zero_toNat` (theorem, [line 99](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Mul.lean#L99))

```lean
theorem State9.zero_toNat : State9.zero.toNat = 0
```

`Montgomery.Native64x8.State9.toNat_eq` (theorem, [line 103](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Mul.lean#L103))

> The value of an accumulator in terms of its limbs.

```lean
theorem State9.toNat_eq (t : State9) :
    t.toNat = t.t0.toNat + 2 ^ 32 * t.t1.toNat + 2 ^ 64 * t.t2.toNat + 2 ^ 96 * t.t3.toNat +
      2 ^ 128 * t.t4.toNat + 2 ^ 160 * t.t5.toNat + 2 ^ 192 * t.t6.toNat +
      2 ^ 224 * t.t7.toNat + 2 ^ 256 * t.t8.toNat
```

> ### The accumulation step

`Montgomery.Native64x8.mulAccum_spec` (theorem, [line 113](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Mul.lean#L113))

> `mulAccum` adds `a * bi` to the accumulator exactly: the carry out of the top limb is
> retained in the head limb.

```lean
theorem mulAccum_spec (a : Limbs8) (bi : UInt64) (t : State9) (ha : a.Bounded)
    (ht : t.Bounded) (hbi : bi.toNat < 2 ^ 32) :
    (mulAccum a bi t).toLimbs8.Bounded ∧ (mulAccum a bi t).t8.toNat < 2 ^ 33 ∧
      (mulAccum a bi t).toNat = t.toNat + a.toNat * bi.toNat
```

> ### The reduction step

`Montgomery.Native64x8.mulReduce_spec` (theorem, [line 162](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Mul.lean#L162))

> `mulReduce` adds the multiple of the modulus that cancels the low limb, and the division
> by `2 ^ 32` performed by dropping that limb is exact.

```lean
theorem mulReduce_spec (q : Limbs8) (negInv : UInt64) (s : State9) (hq : q.Bounded)
    (hs : s.toLimbs8.Bounded) (hs8 : s.t8.toNat < 2 ^ 33) (hn : negInv.toNat < 2 ^ 32)
    (hnq : negInv.toNat * q.toNat % 2 ^ 32 = 2 ^ 32 - 1) :
    (mulReduce q negInv s).Bounded ∧
      2 ^ 32 * (mulReduce q negInv s).toNat =
        s.toNat + (montM s.t0 negInv).toNat * q.toNat
```

> ### The round invariant

`Montgomery.Native64x8.mulRound_spec` (theorem, [line 218](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Mul.lean#L218))

> The CIOS round invariant: one round accumulates `a * bi` and cancels the low limb against
> a multiple `m` of the modulus; the accumulator stays limbwise bounded and below `2 * q`.

```lean
theorem mulRound_spec (q a : Limbs8) (negInv bi : UInt64) (t : State9)
    (hq : q.Bounded) (ha : a.Bounded) (ht : t.Bounded) (hbi : bi.toNat < 2 ^ 32)
    (hn : negInv.toNat < 2 ^ 32) (hnq : negInv.toNat * q.toNat % 2 ^ 32 = 2 ^ 32 - 1)
    (haq : a.toNat < q.toNat) (htq : t.toNat < 2 * q.toNat) :
    (mulRound q negInv a bi t).Bounded ∧ (mulRound q negInv a bi t).toNat < 2 * q.toNat ∧
      ∃ m : ℕ, m < 2 ^ 32 ∧
        2 ^ 32 * (mulRound q negInv a bi t).toNat =
          t.toNat + a.toNat * bi.toNat + m * q.toNat
```

> ### The eight-round fold

`Montgomery.Native64x8.mul_spec` (theorem, [line 273](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Mul.lean#L273))

> Montgomery multiplication is canonical and computes `a * b * (2 ^ 256)⁻¹ mod q`.

```lean
theorem mul_spec (q : Limbs8) (negInv : UInt64) (a b : Limbs8)
    (hq : q.Bounded) (ha : a.Bounded) (hb : b.Bounded) (hn : negInv.toNat < 2 ^ 32)
    (hnq : negInv.toNat * q.toNat % 2 ^ 32 = 2 ^ 32 - 1)
    (haq : a.toNat < q.toNat) :
    (mul q negInv a b).Bounded ∧ (mul q negInv a b).toNat < q.toNat ∧
      2 ^ 256 * (mul q negInv a b).toNat ≡ a.toNat * b.toNat [MOD q.toNat]
```

## Depends on

- [Eight-limb Montgomery arithmetic: runtime definitions (zero-import)](native64x8defs.md)

## Proof depends on

- [Montgomery Reduction](basic.md)
- [Native Montgomery arithmetic over eight 32-bit limbs](native64x8.md)

## Sources

- [CompPoly/Fields/Montgomery/Native64x8Mul.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Mul.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Montgomery.Native64x8Mul.json)
