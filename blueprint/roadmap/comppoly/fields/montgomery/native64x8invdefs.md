---
catalog: module
lean: Montgomery.Native64x8.GcdData, Montgomery.Native64x8.gcdBitLen, Montgomery.Native64x8.gcdInner, Montgomery.Native64x8.gcdLimb, Montgomery.Native64x8.gcdNumBits, Montgomery.Native64x8.gcdApprox, Montgomery.Native64x8.gcdAdd9, Montgomery.Native64x8.gcdSub9, Montgomery.Native64x8.gcdLinearCombDiv, Montgomery.Native64x8.gcdLinearCombMontyRed, Montgomery.Native64x8.gcdMainLoop, Montgomery.Native64x8.gcdFinalChunks, Montgomery.Native64x8.gcdInvCandidate, Montgomery.Native64x8.montPow, Montgomery.Native64x8.invGcdRaw
statement: formalized
proof: formalized
---

# Eight-limb inversion: runtime definitions (Mathlib-free)

`CompPoly.Fields.Montgomery.Native64x8InvDefs`, in [CompPoly/Fields/Montgomery/Native64x8InvDefs.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8InvDefs.lean), by Georgios Raikos.

> The Pornin binary-GCD inverse candidate over `Limbs8` and its checked wrapper
> (`invGcdRaw`), Mathlib-free for `precompileModules` consumers. The proof side is
> `Montgomery/Native64x8Inv`.

> ## Per-field schedule

`Montgomery.Native64x8.GcdData` (class, [line 26](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8InvDefs.lean#L26))

> Per-field schedule of the binary-GCD inverse candidate; every obligation defaults to
> `decide`.

```lean
class GcdData (modulus : Nat) where
  /-- Divsteps in the final word-sized phase: `2·bits(p) - 2 - 15·31`. -/
  finalRounds : Nat
  /-- Initial `u`: the power of two that keeps the candidate in Montgomery form. -/
  initU : Limbs8
  initU_bounded : initU.Bounded := by decide
  initU_toNat : initU.toNat = 2 ^ (591 - finalRounds) % modulus := by decide
  /-- Final-phase chunks stay at mac width. -/
  finalRounds_le : finalRounds ≤ 62 := by decide
```

> ## Word-sized divstep loop

`Montgomery.Native64x8.gcdBitLen` (definition, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8InvDefs.lean#L39))

> Bit length of a word.

```lean
def gcdBitLen (x : UInt64) : Nat
```

`Montgomery.Native64x8.gcdInner` (definition, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8InvDefs.lean#L52))

> The word-sized divstep loop, accumulating the transition matrix; `b` must be odd.

```lean
def gcdInner (rounds : Nat) (a b : UInt64) (f0 g0 f1 g1 : Int) :
    UInt64 × UInt64 × Int × Int × Int × Int
```

> ## Approximation: 64-bit windows over 32-bit limbs

`Montgomery.Native64x8.gcdLimb` (definition, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8InvDefs.lean#L69))

> Read limb `i` (out-of-range indices read the top limb).

```lean
def gcdLimb (v : Limbs8) : Nat → UInt64
```

`Montgomery.Native64x8.gcdNumBits` (definition, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8InvDefs.lean#L81))

> Highest nonzero limb index among limbs 1-7 of `a ||| b` and its bit length; `(1, 0)`
> when all are zero.

```lean
def gcdNumBits (a b : Limbs8) : Nat × Nat
```

`Montgomery.Native64x8.gcdApprox` (definition, [line 98](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8InvDefs.lean#L98))

> One-word approximation: top 33 bits (at the shared bit length) above the bottom 31;
> exact once both values fit one 64-bit word.

```lean
def gcdApprox (val : Limbs8) (limbIdx bits : Nat) : UInt64
```

> ## Nine-limb linear combinations over the native macs

`Montgomery.Native64x8.gcdAdd9` (definition, [line 110](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8InvDefs.lean#L110))

> 9-limb ripple-carry add (top carry discarded).

```lean
def gcdAdd9 (p q : State9) : State9
```

`Montgomery.Native64x8.gcdSub9` (definition, [line 124](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8InvDefs.lean#L124))

> 9-limb subtract with borrow; the wrapped difference and the final borrow.

```lean
def gcdSub9 (p q : State9) : State9 × UInt64
```

`Montgomery.Native64x8.gcdLinearCombDiv` (definition, [line 139](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8InvDefs.lean#L139))

> `(f·a + g·b) / 2^31` as magnitude and sign. Requires `|f| + |g| ≤ 2^31`.

```lean
def gcdLinearCombDiv (a b : Limbs8) (f g : Int) : Limbs8 × Int
```

`Montgomery.Native64x8.gcdLinearCombMontyRed` (definition, [line 162](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8InvDefs.lean#L162))

> `f·a + g·b` folded through one Montgomery reduction step. Requires
> `|f| + |g| ≤ 2^31`.

```lean
def gcdLinearCombMontyRed (q : Limbs8) (negInv : UInt64) (a b : Limbs8)
    (f g : Int) : Limbs8
```

> ## Main loop and candidate

`Montgomery.Native64x8.gcdMainLoop` (definition, [line 174](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8InvDefs.lean#L174))

> The outer rounds: 31 divsteps on one-word approximations, then the transition matrix
> applied to both tracks.

```lean
def gcdMainLoop (q : Limbs8) (negInv : UInt64) (rounds : Nat) (a u b v : Limbs8) :
    Limbs8 × Limbs8 × Limbs8 × Limbs8
```

`Montgomery.Native64x8.gcdFinalChunks` (definition, [line 194](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8InvDefs.lean#L194))

> The final divsteps as two mac-width chunks, folding the Montgomery pair.

```lean
def gcdFinalChunks (q : Limbs8) (negInv : UInt64) (finalRounds : Nat)
    (a u b v : Limbs8) : Limbs8
```

`Montgomery.Native64x8.gcdInvCandidate` (definition, [line 207](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8InvDefs.lean#L207))

> Pornin binary-GCD candidate for the Montgomery inverse, canonical nonzero `x·R mod p`
> to `x⁻¹·R mod p`; proof-free, callers verify.

```lean
def gcdInvCandidate (modulus : Nat) [P : GcdData modulus] (q : Limbs8)
    (negInv : UInt64) (x : Limbs8) : Limbs8
```

> ## Checked inversion over raw limbs

`Montgomery.Native64x8.montPow` (definition, [line 215](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8InvDefs.lean#L215))

> `acc · x^n` in Montgomery form by binary powering.

```lean
def montPow (q : Limbs8) (negInv : UInt64) (acc x : Limbs8) (n : Nat) : Limbs8
```

`Montgomery.Native64x8.invGcdRaw` (definition, [line 224](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8InvDefs.lean#L224))

> The GCD candidate, accepted only if it verifies (`z · x = 1`); else Fermat `montPow`.

```lean
def invGcdRaw (modulus : Nat) [GcdData modulus] (q : Limbs8) (negInv : UInt64)
    (rMod : Limbs8) (x : Limbs8) : Limbs8
```

## Depends on

- [Eight-limb Montgomery arithmetic: runtime definitions (zero-import)](native64x8defs.md)

## Sources

- [CompPoly/Fields/Montgomery/Native64x8InvDefs.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8InvDefs.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Montgomery.Native64x8InvDefs.json)
