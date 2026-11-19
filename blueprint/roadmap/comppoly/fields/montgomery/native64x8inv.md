---
catalog: module
lean: Montgomery.Native64x8.gcdInner_zero, Montgomery.Native64x8.gcdInner_succ, Montgomery.Native64x8.gcdInner_natAbs_le, Montgomery.Native64x8.gcdInner_natAbs_le_31, Montgomery.Native64x8.subBorrow_eq_one_iff, Montgomery.Native64x8.gcdLinearCombDiv_bounded, Montgomery.Native64x8.gcdLinearCombMontyRed_lt, Montgomery.Native64x8.gcdMainLoop_bounded, Montgomery.Native64x8.gcdFinalChunks_lt, Montgomery.Native64x8.gcdInvCandidate_lt, Montgomery.Native64x8.gcdInvCandidate_lt_modulus, Montgomery.Native64x8.montPow_eq_mul_pow, Montgomery.Native64x8.montPow_eq_inv, Montgomery.Native64x8.invGcdRaw_eq_inv, Montgomery.Native64x8.FastField.invGcd, Montgomery.Native64x8.FastField.invGcd_eq_inv
statement: formalized
proof: formalized
---

# Fast inversion for eight-limb Montgomery fields

`CompPoly.Fields.Montgomery.Native64x8Inv`, in [CompPoly/Fields/Montgomery/Native64x8Inv.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native64x8Inv.lean), by Georgios Raikos.

> Correctness of the checked inversion of `Montgomery/Native64x8InvDefs`: `invGcdRaw`
> computes the field inverse and `FastField.invGcd` is its proof-carrying wrapper.  Also
> proves the divstep coefficient bound and the mac-width safety of the candidate.

> ## Divstep coefficient bounds

`Montgomery.Native64x8.gcdInner_zero` (theorem, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native64x8Inv.lean#L27))

> Unfolding of the empty divstep run.

```lean
theorem gcdInner_zero (a b : UInt64) (f0 g0 f1 g1 : Int) :
    gcdInner 0 a b f0 g0 f1 g1 = (a, b, f0, g0, f1, g1)
```

`Montgomery.Native64x8.gcdInner_succ` (theorem, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native64x8Inv.lean#L31))

> Unfolding of one divstep.

```lean
theorem gcdInner_succ (rounds : ℕ) (a b : UInt64) (f0 g0 f1 g1 : Int) :
    gcdInner (rounds + 1) a b f0 g0 f1 g1 =
      if a &&& 1 == 0 then
        gcdInner rounds (a >>> 1) b f0 g0 (f1 * 2) (g1 * 2)
      else if a < b then
        gcdInner rounds ((b - a) >>> 1) a (f1 - f0) (g1 - g0) (f0 * 2) (g0 * 2)
      else
        gcdInner rounds ((a - b) >>> 1) b (f0 - f1) (g0 - g1) (f1 * 2) (g1 * 2)
```

`Montgomery.Native64x8.gcdInner_natAbs_le` (theorem, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native64x8Inv.lean#L48))

> Transition entries at most double per divstep.

```lean
theorem gcdInner_natAbs_le {rounds : ℕ} {a b a' b' : UInt64}
    {f0 g0 f1 g1 f0' g0' f1' g1' : Int} {n : ℕ}
    (h0 : f0.natAbs + g0.natAbs ≤ n) (h1 : f1.natAbs + g1.natAbs ≤ n)
    (heq : gcdInner rounds a b f0 g0 f1 g1 = (a', b', f0', g0', f1', g1')) :
    f0'.natAbs + g0'.natAbs ≤ 2 ^ rounds * n ∧
      f1'.natAbs + g1'.natAbs ≤ 2 ^ rounds * n
```

`Montgomery.Native64x8.gcdInner_natAbs_le_31` (theorem, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native64x8Inv.lean#L78))

> Chunks of at most 31 divsteps satisfy the linear-combination bound.

```lean
theorem gcdInner_natAbs_le_31 {rounds : ℕ} (h31 : rounds ≤ 31) {a b a' b' : UInt64}
    {f0' g0' f1' g1' : Int}
    (heq : gcdInner rounds a b 1 0 0 1 = (a', b', f0', g0', f1', g1')) :
    f0'.natAbs + g0'.natAbs ≤ 2 ^ 31 ∧ f1'.natAbs + g1'.natAbs ≤ 2 ^ 31
```

> ## Order from the borrow chain

`Montgomery.Native64x8.subBorrow_eq_one_iff` (theorem, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native64x8Inv.lean#L89))

> The final borrow decides the numeric order.

```lean
theorem subBorrow_eq_one_iff {a b : Limbs8} (ha : a.Bounded) (hb : b.Bounded) :
    subBorrow a b = 1 ↔ a.toNat < b.toNat
```

> ## Mac-width safety of the candidate

`Montgomery.Native64x8.gcdLinearCombDiv_bounded` (theorem, [line 106](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native64x8Inv.lean#L106))

> The division lincomb masks every output limb.

```lean
theorem gcdLinearCombDiv_bounded (a b : Limbs8) (f g : Int) :
    (gcdLinearCombDiv a b f g).1.Bounded
```

`Montgomery.Native64x8.gcdLinearCombMontyRed_lt` (theorem, [line 151](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native64x8Inv.lean#L151))

> The Montgomery lincomb stays canonical for canonical inputs.

```lean
theorem gcdLinearCombMontyRed_lt {q : Limbs8} {negInv : UInt64} {a b : Limbs8} {f g : Int}
    (hq : q.Bounded) (hq0 : 0 < q.toNat)
    (hn : negInv.toNat < 2 ^ 32) (hnq : negInv.toNat * q.toNat % 2 ^ 32 = 2 ^ 32 - 1)
    (ha : a.Bounded) (hb : b.Bounded) (haq : a.toNat < q.toNat) (hbq : b.toNat < q.toNat)
    (hfg : f.natAbs + g.natAbs ≤ 2 ^ 31) :
    (gcdLinearCombMontyRed q negInv a b f g).Bounded ∧
      (gcdLinearCombMontyRed q negInv a b f g).toNat < q.toNat
```

`Montgomery.Native64x8.gcdMainLoop_bounded` (theorem, [line 190](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native64x8Inv.lean#L190))

> The main loop keeps both tracks at mac width and the Montgomery pair canonical.

```lean
theorem gcdMainLoop_bounded {q : Limbs8} {negInv : UInt64} {rounds : ℕ}
    {a u b v A U B V : Limbs8}
    (hq : q.Bounded) (hq0 : 0 < q.toNat)
    (hn : negInv.toNat < 2 ^ 32) (hnq : negInv.toNat * q.toNat % 2 ^ 32 = 2 ^ 32 - 1)
    (ha : a.Bounded) (hb : b.Bounded) (hu : u.Bounded) (huq : u.toNat < q.toNat)
    (hv : v.Bounded) (hvq : v.toNat < q.toNat)
    (heq : gcdMainLoop q negInv rounds a u b v = (A, U, B, V)) :
    A.Bounded ∧ B.Bounded ∧ U.Bounded ∧ U.toNat < q.toNat ∧ V.Bounded ∧
      V.toNat < q.toNat
```

`Montgomery.Native64x8.gcdFinalChunks_lt` (theorem, [line 251](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native64x8Inv.lean#L251))

> The final chunks stay canonical for canonical inputs.

```lean
theorem gcdFinalChunks_lt {q : Limbs8} {negInv : UInt64} {finalRounds : ℕ}
    {a u b v : Limbs8} (hfr : finalRounds ≤ 62)
    (hq : q.Bounded) (hq0 : 0 < q.toNat)
    (hn : negInv.toNat < 2 ^ 32) (hnq : negInv.toNat * q.toNat % 2 ^ 32 = 2 ^ 32 - 1)
    (hu : u.Bounded) (huq : u.toNat < q.toNat) (hv : v.Bounded)
    (hvq : v.toNat < q.toNat) :
    (gcdFinalChunks q negInv finalRounds a u b v).Bounded ∧
      (gcdFinalChunks q negInv finalRounds a u b v).toNat < q.toNat
```

`Montgomery.Native64x8.gcdInvCandidate_lt` (theorem, [line 286](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native64x8Inv.lean#L286))

> The candidate stays at mac width and canonical.

```lean
theorem gcdInvCandidate_lt {modulus : ℕ} [P : GcdData modulus] {q x : Limbs8}
    {negInv : UInt64}
    (hq : q.Bounded) (hqm : q.toNat = modulus) (hq0 : 0 < q.toNat)
    (hn : negInv.toNat < 2 ^ 32)
    (hnq : negInv.toNat * q.toNat % 2 ^ 32 = 2 ^ 32 - 1) (hx : x.Bounded) :
    (gcdInvCandidate modulus q negInv x).Bounded ∧
      (gcdInvCandidate modulus q negInv x).toNat < q.toNat
```

`Montgomery.Native64x8.gcdInvCandidate_lt_modulus` (theorem, [line 313](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native64x8Inv.lean#L313))

> With the class data, the candidate is bounded and canonical for any bounded input.

```lean
theorem gcdInvCandidate_lt_modulus [GcdData modulus] {x : Limbs8} (hx : x.Bounded) :
    (gcdInvCandidate modulus P.modulusLimbs P.montgomeryNegInv x).Bounded ∧
      (gcdInvCandidate modulus P.modulusLimbs P.montgomeryNegInv x).toNat < modulus
```

> ## The Fermat fallback and the checked raw inversion

`Montgomery.Native64x8.montPow_eq_mul_pow` (theorem, [line 334](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native64x8Inv.lean#L334))

> `montPow` computes `acc · xⁿ`.

```lean
theorem montPow_eq_mul_pow (acc x : FastField modulus) (n : ℕ) :
    montPow P.modulusLimbs P.montgomeryNegInv acc.val x.val n = (acc * x ^ n).val
```

`Montgomery.Native64x8.montPow_eq_inv` (theorem, [line 369](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native64x8Inv.lean#L369))

> The `montPow` fallback computes the field inverse.

```lean
theorem montPow_eq_inv (x : FastField modulus) :
    montPow P.modulusLimbs P.montgomeryNegInv P.rModModulus x.val (modulus - 2)
      = (x⁻¹).val
```

`Montgomery.Native64x8.invGcdRaw_eq_inv` (theorem, [line 399](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native64x8Inv.lean#L399))

> `invGcdRaw` computes the field inverse.

```lean
theorem invGcdRaw_eq_inv [GcdData modulus] (x : FastField modulus) :
    invGcdRaw modulus P.modulusLimbs P.montgomeryNegInv P.rModModulus x.val
      = (x⁻¹).val
```

> ## The proof-carrying wrapper

`Montgomery.Native64x8.FastField.invGcd` (definition, [line 420](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native64x8Inv.lean#L420))

> The proof-carrying wrapper of the checked inversion `invGcdRaw`.

```lean
def invGcd [GcdData modulus] (x : FastField modulus) : FastField modulus
```

`Montgomery.Native64x8.FastField.invGcd_eq_inv` (theorem, [line 427](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native64x8Inv.lean#L427))

> `invGcd` agrees with the `Field` inverse.

```lean
theorem invGcd_eq_inv [GcdData modulus] (x : FastField modulus) :
    invGcd x = x⁻¹
```

## Depends on

- [Fast eight-limb Montgomery fields](native64x8field.md)
- [Eight-limb inversion: runtime definitions (Mathlib-free)](native64x8invdefs.md)

## Sources

- [CompPoly/Fields/Montgomery/Native64x8Inv.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native64x8Inv.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Montgomery.Native64x8Inv.json)
