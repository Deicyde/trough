---
catalog: module
lean: Montgomery.Native64x4.GcdData, Montgomery.Native64x4.mulWord, Montgomery.Native64x4.add5, Montgomery.Native64x4.sub5, Montgomery.Native64x4.gcdLinearCombDiv, Montgomery.Native64x4.negMod, Montgomery.Native64x4.lincombTail, Montgomery.Native64x4.gcdLinearCombMontyRed, Montgomery.Native64x4.gcdLimb, Montgomery.Native64x4.gcdNumBits, Montgomery.Native64x4.gcdApprox, Montgomery.Native64x4.gcdMainLoop, Montgomery.Native64x4.gcdFinalChunks, Montgomery.Native64x4.gcdInvCandidate, Montgomery.Native64x4.montPow, Montgomery.Native64x4.invGcdRaw
statement: formalized
proof: formalized
---

# Four-limb inversion: runtime definitions (Mathlib-free)

`CompPoly.Fields.Montgomery.Native64x4InvDefs`, in [CompPoly/Fields/Montgomery/Native64x4InvDefs.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4InvDefs.lean), by Georgios Raikos.

> The Pornin binary-GCD inverse candidate over `Limbs4` and its checked wrapper
> (`invGcdRaw`), Mathlib-free for `precompileModules` consumers.  The word-sized divstep loop
> and bit-length helper come from `Montgomery/DivstepDefs`.  The proof side is
> `Montgomery/Native64x4Inv`.

> ## Per-field schedule

`Montgomery.Native64x4.GcdData` (class, [line 28](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4InvDefs.lean#L28))

> Per-field schedule of the binary-GCD inverse candidate; every obligation defaults to
> `decide`.

```lean
class GcdData (modulus : Nat) where
  /-- Divsteps in the final word-sized phase: `2·bits(p) - 2 - 15·31`. -/
  finalRounds : Nat
  /-- Initial `u`: the power of two that keeps the candidate in Montgomery form. -/
  initU : Limbs4
  initU_toNat : initU.toNat = 2 ^ (1135 - finalRounds) % modulus := by decide
  /-- Final-phase chunks stay at mac width. -/
  finalRounds_le : finalRounds ≤ 62 := by decide
```

> ## Five-word arithmetic

`Montgomery.Native64x4.mulWord` (definition, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4InvDefs.lean#L40))

> `x * k` as five words.

```lean
def mulWord (x : Limbs4) (k : UInt64) : UInt64 × UInt64 × UInt64 × UInt64 × UInt64
```

`Montgomery.Native64x4.add5` (definition, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4InvDefs.lean#L48))

> Five-word add: the sum words and the carry out.

```lean
def add5 (a0 a1 a2 a3 a4 b0 b1 b2 b3 b4 : UInt64) :
    UInt64 × UInt64 × UInt64 × UInt64 × UInt64 × UInt64
```

`Montgomery.Native64x4.sub5` (definition, [line 58](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4InvDefs.lean#L58))

> Five-word subtract: the difference words and the borrow out.

```lean
def sub5 (a0 a1 a2 a3 a4 b0 b1 b2 b3 b4 : UInt64) :
    UInt64 × UInt64 × UInt64 × UInt64 × UInt64 × UInt64
```

> ## Linear combinations

`Montgomery.Native64x4.gcdLinearCombDiv` (definition, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4InvDefs.lean#L70))

> `(f·a + g·b) / 2^31` as magnitude and sign.  Requires `|f| + |g| ≤ 2^31`.

```lean
def gcdLinearCombDiv (a b : Limbs4) (f g : Int) : Limbs4 × Int
```

`Montgomery.Native64x4.negMod` (definition, [line 99](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4InvDefs.lean#L99))

> `n - u` as limbs, for `u < n`.

```lean
def negMod (q u : Limbs4) : Limbs4
```

`Montgomery.Native64x4.lincombTail` (definition, [line 105](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4InvDefs.lean#L105))

> The Montgomery linear combination on magnitudes: `(F·uS + G·vS) · 2^-64 mod q`, reduced
> once through `condSubWide`.  Requires `F + G ≤ 2^31` and `uS, vS ≤ q`.

```lean
def lincombTail (q : Limbs4) (negInv : UInt64) (uS vS : Limbs4) (F G : UInt64) :
    Limbs4
```

`Montgomery.Native64x4.gcdLinearCombMontyRed` (definition, [line 116](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4InvDefs.lean#L116))

> `(f·u + g·v) · 2^-64 mod q`, canonical.  Requires `|f| + |g| ≤ 2^31` and `u, v < q`.

```lean
def gcdLinearCombMontyRed (q : Limbs4) (negInv : UInt64) (u v : Limbs4)
    (f g : Int) : Limbs4
```

> ## Approximation: one word at the shared bit length

`Montgomery.Native64x4.gcdLimb` (definition, [line 124](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4InvDefs.lean#L124))

> Read limb `i` (out-of-range indices read the top limb).

```lean
def gcdLimb (v : Limbs4) : Nat → UInt64
```

`Montgomery.Native64x4.gcdNumBits` (definition, [line 132](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4InvDefs.lean#L132))

> Highest nonzero limb index among limbs 1-3 of `a ||| b` and its bit length; `(0, 0)`
> when all are zero.

```lean
def gcdNumBits (a b : Limbs4) : Nat × Nat
```

`Montgomery.Native64x4.gcdApprox` (definition, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4InvDefs.lean#L142))

> One-word approximation: the top 33 bits at the shared bit length above the bottom 31;
> exact once both values fit one word.

```lean
def gcdApprox (val : Limbs4) (limbIdx bits : Nat) : UInt64
```

> ## Main loop and candidate

`Montgomery.Native64x4.gcdMainLoop` (definition, [line 157](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4InvDefs.lean#L157))

> The outer rounds: 31 divsteps on one-word approximations, then the transition matrix
> applied to both tracks.

```lean
def gcdMainLoop (q : Limbs4) (negInv : UInt64) (rounds : Nat) (a u b v : Limbs4) :
    Limbs4 × Limbs4 × Limbs4 × Limbs4
```

`Montgomery.Native64x4.gcdFinalChunks` (definition, [line 177](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4InvDefs.lean#L177))

> The final divsteps as two mac-width chunks, folding the Montgomery pair.

```lean
def gcdFinalChunks (q : Limbs4) (negInv : UInt64) (finalRounds : Nat)
    (a u b v : Limbs4) : Limbs4
```

`Montgomery.Native64x4.gcdInvCandidate` (definition, [line 188](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4InvDefs.lean#L188))

> Pornin binary-GCD candidate for the Montgomery inverse, canonical nonzero `x·R mod p`
> to `x⁻¹·R mod p`; proof-free, callers verify.

```lean
def gcdInvCandidate (modulus : Nat) [P : GcdData modulus] (q : Limbs4)
    (negInv : UInt64) (x : Limbs4) : Limbs4
```

> ## Checked inversion over raw limbs

`Montgomery.Native64x4.montPow` (definition, [line 196](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4InvDefs.lean#L196))

> `acc · x^n` in Montgomery form by binary powering.

```lean
def montPow (q : Limbs4) (negInv : UInt64) (acc x : Limbs4) (n : Nat) : Limbs4
```

`Montgomery.Native64x4.invGcdRaw` (definition, [line 205](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4InvDefs.lean#L205))

> The GCD candidate, accepted only if it verifies (`z · x = 1`); else Fermat `montPow`.

```lean
def invGcdRaw (modulus : Nat) [GcdData modulus] (q : Limbs4) (negInv : UInt64)
    (rMod : Limbs4) (x : Limbs4) : Limbs4
```

## Depends on

- [Word-sized divsteps: runtime definitions (zero-import)](divstepdefs.md)
- [Four-limb Montgomery arithmetic: runtime definitions (zero-import)](native64x4defs.md)

## Sources

- [CompPoly/Fields/Montgomery/Native64x4InvDefs.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4InvDefs.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Montgomery.Native64x4InvDefs.json)
