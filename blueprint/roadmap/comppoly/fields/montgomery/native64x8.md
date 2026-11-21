---
catalog: module
lean: Montgomery.Native64x8.adc_spec, Montgomery.Native64x8.adc_spec_wide, Montgomery.Native64x8.sbb_spec, Montgomery.Native64x8.mac_spec, Montgomery.Native64x8.montM_toNat, Montgomery.Native64x8.adcLo_lt, Montgomery.Native64x8.sbbLo_lt, Montgomery.Native64x8.macLo_lt, Montgomery.Native64x8.montM_lt, Montgomery.Native64x8.Limbs8.zero_bounded, Montgomery.Native64x8.Limbs8.zero_toNat, Montgomery.Native64x8.Limbs8.one_bounded, Montgomery.Native64x8.Limbs8.one_toNat, Montgomery.Native64x8.Limbs8.ofNat_bounded, Montgomery.Native64x8.Limbs8.ofNat_toNat, Montgomery.Native64x8.sum8_lt, Montgomery.Native64x8.Limbs8.ext_of_toNat, Montgomery.Native64x8.Limbs8.toNat_lt, Montgomery.Native64x8.carry_chain_sum, Montgomery.Native64x8.borrow_chain_sum, Montgomery.Native64x8.addLimbs_bounded, Montgomery.Native64x8.addLimbs_spec, Montgomery.Native64x8.addLimbs_toNat, Montgomery.Native64x8.subLimbs_bounded, Montgomery.Native64x8.subLimbs_spec, Montgomery.Native64x8.condSub_bounded, Montgomery.Native64x8.condSub_toNat, Montgomery.Native64x8.condSub_lt, Montgomery.Native64x8.condSubWide_bounded, Montgomery.Native64x8.condSubWide_toNat, Montgomery.Native64x8.condSubWide_lt, Montgomery.Native64x8.add_bounded, Montgomery.Native64x8.sub_bounded, Montgomery.Native64x8.neg_bounded, Montgomery.Native64x8.add_toNat, Montgomery.Native64x8.add_lt, Montgomery.Native64x8.sub_toNat, Montgomery.Native64x8.sub_lt, Montgomery.Native64x8.neg_toNat, Montgomery.Native64x8.neg_lt
statement: formalized
proof: formalized
---

# Native Montgomery arithmetic over eight 32-bit limbs

`CompPoly.Fields.Montgomery.Native64x8`, in [CompPoly/Fields/Montgomery/Native64x8.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean), by Gregor Mitscha-Baude.

> Raw word operations for prime moduli below `2 ^ 256`, represented as eight 32-bit limbs
> carried in the low halves of `UInt64` words (`Limbs8`).  This is the multi-limb sibling of
> `Montgomery/Native32.lean`: every operation is a straight-line chain of `@[inline]` word
> helpers, and each helper comes with an existential `toNat` specification that names its
> outputs as fresh naturals.  The definitions themselves live in the zero-import module
> `Montgomery/Native64x8Defs`; this module states and proves everything about them.
>
> The limb helpers (`adcLo`/`adcCo`, `sbbLo`/`sbbBo`, `macLo`/`macHi`, `montM`) are combined by
> the two telescoping lemmas `carry_chain_sum` and `borrow_chain_sum`, which turn an eight-step
> carry or borrow chain into a single identity between recomposed values.  Every correctness
> statement is generic in the modulus limbs; concrete fields supply their constants through
> the `Mont64x8Field` class of `Montgomery/Native64x8Field`.
>
> Conditional subtraction, addition, subtraction and negation are proved correct here.  The
> CIOS multiplication round `mulRound` is defined in `Montgomery/Native64x8Defs`; its state
> invariant is proved in the sibling module that builds the field carrier.
>
> ## Main results
>
> * `condSub_toNat`, `condSubWide_toNat`, `add_toNat`, `sub_toNat`, `neg_toNat` — correctness
>   of the raw operations
> * `addLimbs_spec`, `subLimbs_spec` — the underlying carry/borrow chains

> ## Word-level specifications

`Montgomery.Native64x8.adc_spec` (theorem, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L55))

> Add-with-carry, existential form: the low limb and the carry-out are named as fresh
> naturals together with their defining equations, so that a chain of them is a linear system
> over plain variables.

```lean
theorem adc_spec (x y c : UInt64) (hx : x.toNat < 2 ^ 32) (hy : y.toNat < 2 ^ 32)
    (hc : c.toNat ≤ 1) :
    ∃ s co : ℕ, (adcLo x y c).toNat = s ∧ (adcCo x y c).toNat = co ∧
      s + 2 ^ 32 * co = x.toNat + y.toNat + c.toNat ∧ co ≤ 1 ∧ s < 2 ^ 32
```

`Montgomery.Native64x8.adc_spec_wide` (theorem, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L65))

> Add-with-carry when the first summand is one bit wider than a limb.

```lean
theorem adc_spec_wide (x y c : UInt64) (hx : x.toNat < 2 ^ 33) (hy : y.toNat < 2 ^ 32)
    (hc : c.toNat ≤ 1) :
    ∃ s co : ℕ, (adcLo x y c).toNat = s ∧ (adcCo x y c).toNat = co ∧
      s + 2 ^ 32 * co = x.toNat + y.toNat + c.toNat ∧ co ≤ 2 ∧ s < 2 ^ 32
```

`Montgomery.Native64x8.sbb_spec` (theorem, [line 75](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L75))

> Subtract-with-borrow, existential form.

```lean
theorem sbb_spec (x y b : UInt64) (hx : x.toNat < 2 ^ 32) (hy : y.toNat < 2 ^ 32)
    (hb : b.toNat ≤ 1) :
    ∃ m bo : ℕ, (sbbLo x y b).toNat = m ∧ (sbbBo x y b).toNat = bo ∧
      m + y.toNat + b.toNat = x.toNat + 2 ^ 32 * bo ∧ bo ≤ 1 ∧ m < 2 ^ 32
```

`Montgomery.Native64x8.mac_spec` (theorem, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L86))

> Multiply-accumulate, existential form.  The accumulator, both factors and the carry-in
> all fit in 32 bits, so `t + x * y + c` cannot overflow a 64-bit word.

```lean
theorem mac_spec (t x y c : UInt64) (ht : t.toNat < 2 ^ 32) (hx : x.toNat < 2 ^ 32)
    (hy : y.toNat < 2 ^ 32) (hc : c.toNat < 2 ^ 32) :
    ∃ lo hi : ℕ, (macLo t x y c).toNat = lo ∧ (macHi t x y c).toNat = hi ∧
      lo + 2 ^ 32 * hi = t.toNat + x.toNat * y.toNat + c.toNat ∧ hi < 2 ^ 32 ∧
      lo < 2 ^ 32
```

`Montgomery.Native64x8.montM_toNat` (theorem, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L100))

> The Montgomery multiplier agrees with its natural-number specification.

```lean
theorem montM_toNat (s negInv : UInt64) (hs : s.toNat < 2 ^ 32) (hn : negInv.toNat < 2 ^ 32) :
    (montM s negInv).toNat = s.toNat * negInv.toNat % 2 ^ 32
```

`Montgomery.Native64x8.adcLo_lt` (theorem, [line 110](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L110))

```lean
theorem adcLo_lt (x y c : UInt64) : (adcLo x y c).toNat < 2 ^ 32
```

`Montgomery.Native64x8.sbbLo_lt` (theorem, [line 115](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L115))

```lean
theorem sbbLo_lt (x y b : UInt64) : (sbbLo x y b).toNat < 2 ^ 32
```

`Montgomery.Native64x8.macLo_lt` (theorem, [line 120](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L120))

```lean
theorem macLo_lt (t x y c : UInt64) : (macLo t x y c).toNat < 2 ^ 32
```

`Montgomery.Native64x8.montM_lt` (theorem, [line 125](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L125))

```lean
theorem montM_lt (s negInv : UInt64) : (montM s negInv).toNat < 2 ^ 32
```

> ## Eight-limb values

`Montgomery.Native64x8.Limbs8.zero_bounded` (theorem, [line 134](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L134))

```lean
theorem zero_bounded : zero.Bounded
```

`Montgomery.Native64x8.Limbs8.zero_toNat` (theorem, [line 138](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L138))

```lean
theorem zero_toNat : zero.toNat = 0
```

`Montgomery.Native64x8.Limbs8.one_bounded` (theorem, [line 141](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L141))

```lean
theorem one_bounded : one.Bounded
```

`Montgomery.Native64x8.Limbs8.one_toNat` (theorem, [line 143](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L143))

```lean
theorem one_toNat : one.toNat = 1
```

`Montgomery.Native64x8.Limbs8.ofNat_bounded` (theorem, [line 145](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L145))

```lean
theorem ofNat_bounded (n : ℕ) : (ofNat n).Bounded
```

`Montgomery.Native64x8.Limbs8.ofNat_toNat` (theorem, [line 149](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L149))

```lean
theorem ofNat_toNat (n : ℕ) : (ofNat n).toNat = n % 2 ^ 256
```

`Montgomery.Native64x8.sum8_lt` (theorem, [line 156](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L156))

> A recomposed value with 32-bit limbs stays below `2 ^ 256`.

```lean
theorem sum8_lt {a0 a1 a2 a3 a4 a5 a6 a7 : ℕ} (h0 : a0 < 2 ^ 32) (h1 : a1 < 2 ^ 32)
    (h2 : a2 < 2 ^ 32) (h3 : a3 < 2 ^ 32) (h4 : a4 < 2 ^ 32) (h5 : a5 < 2 ^ 32)
    (h6 : a6 < 2 ^ 32) (h7 : a7 < 2 ^ 32) :
    a0 + 2 ^ 32 * a1 + 2 ^ 64 * a2 + 2 ^ 96 * a3 + 2 ^ 128 * a4 + 2 ^ 160 * a5 + 2 ^ 192 * a6 +
      2 ^ 224 * a7 < 2 ^ 256
```

`Montgomery.Native64x8.Limbs8.ext_of_toNat` (theorem, [line 164](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L164))

> Bounded limb vectors are determined by their value.

```lean
theorem Limbs8.ext_of_toNat {x y : Limbs8} (hx : x.Bounded) (hy : y.Bounded)
    (h : x.toNat = y.toNat) : x = y
```

`Montgomery.Native64x8.Limbs8.toNat_lt` (theorem, [line 185](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L185))

> A bounded eight-limb value is below `2 ^ 256`.

```lean
theorem Limbs8.toNat_lt {x : Limbs8} (hx : x.Bounded) : x.toNat < 2 ^ 256
```

> ### Chain lemmas
>
> Telescoping identities for an eight-step carry or borrow chain.  They are stated over plain
> naturals and the `y` slots are arbitrary, so `carry_chain_sum` serves both the
> add-with-carry chains and the multiply-accumulate chains of CIOS, where `yᵢ` is a limb
> product.

`Montgomery.Native64x8.carry_chain_sum` (theorem, [line 197](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L197))

> Weighted telescoping of an eight-step carry chain.

```lean
theorem carry_chain_sum {x0 x1 x2 x3 x4 x5 x6 x7 y0 y1 y2 y3 y4 y5 y6 y7 : ℕ}
    {s0 s1 s2 s3 s4 s5 s6 s7 cin c0 c1 c2 c3 c4 c5 c6 c7 : ℕ}
    (e0 : s0 + 2 ^ 32 * c0 = x0 + y0 + cin)
    (e1 : s1 + 2 ^ 32 * c1 = x1 + y1 + c0)
    (e2 : s2 + 2 ^ 32 * c2 = x2 + y2 + c1)
    (e3 : s3 + 2 ^ 32 * c3 = x3 + y3 + c2)
    (e4 : s4 + 2 ^ 32 * c4 = x4 + y4 + c3)
    (e5 : s5 + 2 ^ 32 * c5 = x5 + y5 + c4)
    (e6 : s6 + 2 ^ 32 * c6 = x6 + y6 + c5)
    (e7 : s7 + 2 ^ 32 * c7 = x7 + y7 + c6) :
    s0 + 2 ^ 32 * s1 + 2 ^ 64 * s2 + 2 ^ 96 * s3 + 2 ^ 128 * s4 + 2 ^ 160 * s5 + 2 ^ 192 * s6 +
      2 ^ 224 * s7 + 2 ^ 256 * c7 =
    (x0 + 2 ^ 32 * x1 + 2 ^ 64 * x2 + 2 ^ 96 * x3 + 2 ^ 128 * x4 + 2 ^ 160 * x5 +
      2 ^ 192 * x6 + 2 ^ 224 * x7) +
      (y0 + 2 ^ 32 * y1 + 2 ^ 64 * y2 + 2 ^ 96 * y3 + 2 ^ 128 * y4 + 2 ^ 160 * y5 +
      2 ^ 192 * y6 + 2 ^ 224 * y7) + cin
```

`Montgomery.Native64x8.borrow_chain_sum` (theorem, [line 216](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L216))

> Weighted telescoping of an eight-step borrow chain.

```lean
theorem borrow_chain_sum {x0 x1 x2 x3 x4 x5 x6 x7 y0 y1 y2 y3 y4 y5 y6 y7 : ℕ}
    {m0 m1 m2 m3 m4 m5 m6 m7 bin b0 b1 b2 b3 b4 b5 b6 b7 : ℕ}
    (e0 : m0 + y0 + bin = x0 + 2 ^ 32 * b0)
    (e1 : m1 + y1 + b0 = x1 + 2 ^ 32 * b1)
    (e2 : m2 + y2 + b1 = x2 + 2 ^ 32 * b2)
    (e3 : m3 + y3 + b2 = x3 + 2 ^ 32 * b3)
    (e4 : m4 + y4 + b3 = x4 + 2 ^ 32 * b4)
    (e5 : m5 + y5 + b4 = x5 + 2 ^ 32 * b5)
    (e6 : m6 + y6 + b5 = x6 + 2 ^ 32 * b6)
    (e7 : m7 + y7 + b6 = x7 + 2 ^ 32 * b7) :
    (m0 + 2 ^ 32 * m1 + 2 ^ 64 * m2 + 2 ^ 96 * m3 + 2 ^ 128 * m4 + 2 ^ 160 * m5 +
      2 ^ 192 * m6 + 2 ^ 224 * m7) +
      (y0 + 2 ^ 32 * y1 + 2 ^ 64 * y2 + 2 ^ 96 * y3 + 2 ^ 128 * y4 + 2 ^ 160 * y5 +
      2 ^ 192 * y6 + 2 ^ 224 * y7) + bin =
      x0 + 2 ^ 32 * x1 + 2 ^ 64 * x2 + 2 ^ 96 * x3 + 2 ^ 128 * x4 + 2 ^ 160 * x5 + 2 ^ 192 * x6 +
      2 ^ 224 * x7 + 2 ^ 256 * b7
```

> ### Branch lemmas
>
> The situations that a borrow chain can produce, each as a standalone linear problem over a
> handful of naturals.

> ## Limbwise addition and subtraction

`Montgomery.Native64x8.addLimbs_bounded` (theorem, [line 280](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L280))

```lean
theorem addLimbs_bounded (a b : Limbs8) : (addLimbs a b).Bounded
```

`Montgomery.Native64x8.addLimbs_spec` (theorem, [line 286](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L286))

> The limbwise sum and the top carry recompose the sum of the inputs.

```lean
theorem addLimbs_spec (a b : Limbs8) (ha : a.Bounded) (hb : b.Bounded) :
    (addCarry a b).toNat ≤ 1 ∧
      (addLimbs a b).toNat + 2 ^ 256 * (addCarry a b).toNat = a.toNat + b.toNat
```

`Montgomery.Native64x8.addLimbs_toNat` (theorem, [line 318](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L318))

> The limbwise sum and some top carry recompose the sum of the inputs.

```lean
theorem addLimbs_toNat (a b : Limbs8) (ha : a.Bounded) (hb : b.Bounded) :
    ∃ c : ℕ, c ≤ 1 ∧ (addLimbs a b).toNat + 2 ^ 256 * c = a.toNat + b.toNat
```

`Montgomery.Native64x8.subLimbs_bounded` (theorem, [line 322](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L322))

```lean
theorem subLimbs_bounded (a b : Limbs8) : (subLimbs a b).Bounded
```

`Montgomery.Native64x8.subLimbs_spec` (theorem, [line 328](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L328))

> The limbwise difference and the final borrow recompose the difference of the inputs.

```lean
theorem subLimbs_spec (a b : Limbs8) (ha : a.Bounded) (hb : b.Bounded) :
    (subBorrow a b).toNat ≤ 1 ∧
      (subLimbs a b).toNat + b.toNat = a.toNat + 2 ^ 256 * (subBorrow a b).toNat
```

> ## Conditional subtraction

`Montgomery.Native64x8.condSub_bounded` (theorem, [line 361](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L361))

```lean
theorem condSub_bounded (q t : Limbs8) (ht : t.Bounded) : (condSub q t).Bounded
```

`Montgomery.Native64x8.condSub_toNat` (theorem, [line 368](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L368))

> `condSub` subtracts the modulus exactly when the input is at least the modulus.

```lean
theorem condSub_toNat (q t : Limbs8) (hq : q.Bounded) (ht : t.Bounded) :
    (condSub q t).toNat = if t.toNat < q.toNat then t.toNat else t.toNat - q.toNat
```

`Montgomery.Native64x8.condSub_lt` (theorem, [line 382](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L382))

> `condSub` returns a canonical representative for inputs below `2 * q`.

```lean
theorem condSub_lt (q t : Limbs8) (hq : q.Bounded) (ht : t.Bounded)
    (h : t.toNat < 2 * q.toNat) : (condSub q t).toNat < q.toNat
```

`Montgomery.Native64x8.condSubWide_bounded` (theorem, [line 387](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L387))

```lean
theorem condSubWide_bounded (q : Limbs8) (t : State9) (ht : t.Bounded) :
    (condSubWide q t).Bounded
```

`Montgomery.Native64x8.condSubWide_toNat` (theorem, [line 396](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L396))

> `condSubWide` subtracts the modulus exactly when an accumulator below `2 * q` is at least
> the modulus.

```lean
theorem condSubWide_toNat (q : Limbs8) (t : State9) (hq : q.Bounded) (ht : t.Bounded)
    (h : t.toNat < 2 * q.toNat) :
    (condSubWide q t).toNat = if t.toNat < q.toNat then t.toNat else t.toNat - q.toNat
```

`Montgomery.Native64x8.condSubWide_lt` (theorem, [line 410](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L410))

> `condSubWide` returns a canonical representative for accumulators below `2 * q`.

```lean
theorem condSubWide_lt (q : Limbs8) (t : State9) (hq : q.Bounded) (ht : t.Bounded)
    (h : t.toNat < 2 * q.toNat) : (condSubWide q t).toNat < q.toNat
```

> ## Field operations

`Montgomery.Native64x8.add_bounded` (theorem, [line 417](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L417))

```lean
theorem add_bounded (q a b : Limbs8) : (add q a b).Bounded
```

`Montgomery.Native64x8.sub_bounded` (theorem, [line 423](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L423))

```lean
theorem sub_bounded (q a b : Limbs8) : (sub q a b).Bounded
```

`Montgomery.Native64x8.neg_bounded` (theorem, [line 429](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L429))

```lean
theorem neg_bounded (q a : Limbs8) : (neg q a).Bounded
```

`Montgomery.Native64x8.add_toNat` (theorem, [line 432](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L432))

> Modular addition is correct for canonical inputs of any bounded modulus.

```lean
theorem add_toNat (q a b : Limbs8) (hq : q.Bounded) (ha : a.Bounded) (hb : b.Bounded)
    (haq : a.toNat < q.toNat) (hbq : b.toNat < q.toNat) :
    (add q a b).toNat = (a.toNat + b.toNat) % q.toNat
```

`Montgomery.Native64x8.add_lt` (theorem, [line 448](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L448))

```lean
theorem add_lt (q a b : Limbs8) (hq : q.Bounded) (ha : a.Bounded) (hb : b.Bounded)
    (haq : a.toNat < q.toNat) (hbq : b.toNat < q.toNat) :
    (add q a b).toNat < q.toNat
```

`Montgomery.Native64x8.sub_toNat` (theorem, [line 455](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L455))

> Modular subtraction is correct for canonical inputs of any bounded modulus.

```lean
theorem sub_toNat (q a b : Limbs8) (hq : q.Bounded) (ha : a.Bounded) (hb : b.Bounded)
    (haq : a.toNat < q.toNat) (hbq : b.toNat < q.toNat) :
    (sub q a b).toNat = (a.toNat + (q.toNat - b.toNat)) % q.toNat
```

`Montgomery.Native64x8.sub_lt` (theorem, [line 471](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L471))

```lean
theorem sub_lt (q a b : Limbs8) (hq : q.Bounded) (ha : a.Bounded) (hb : b.Bounded)
    (haq : a.toNat < q.toNat) (hbq : b.toNat < q.toNat) :
    (sub q a b).toNat < q.toNat
```

`Montgomery.Native64x8.neg_toNat` (theorem, [line 478](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L478))

> Modular negation is correct for canonical inputs of any bounded modulus.

```lean
theorem neg_toNat (q a : Limbs8) (hq : q.Bounded) (ha : a.Bounded)
    (haq : a.toNat < q.toNat) :
    (neg q a).toNat = (q.toNat - a.toNat) % q.toNat
```

`Montgomery.Native64x8.neg_lt` (theorem, [line 485](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean#L485))

```lean
theorem neg_lt (q a : Limbs8) (hq : q.Bounded) (ha : a.Bounded)
    (haq : a.toNat < q.toNat) : (neg q a).toNat < q.toNat
```

## Depends on

- [Eight-limb Montgomery arithmetic: runtime definitions (zero-import)](native64x8defs.md)

## Sources

- [CompPoly/Fields/Montgomery/Native64x8.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Montgomery.Native64x8.json)
