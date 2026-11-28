---
catalog: module
lean: CompPoly.RabinCert.Binary.clmulBits, CompPoly.RabinCert.Binary.clmul, CompPoly.RabinCert.Binary.toPoly, CompPoly.RabinCert.Binary.coeff_toPoly, CompPoly.RabinCert.Binary.toPoly_congr, CompPoly.RabinCert.Binary.toPoly_zero, CompPoly.RabinCert.Binary.toPoly_xor, CompPoly.RabinCert.Binary.toPoly_two_pow, CompPoly.RabinCert.Binary.toPoly_one, CompPoly.RabinCert.Binary.toPoly_two, CompPoly.RabinCert.Binary.toPoly_shiftLeft_one, CompPoly.RabinCert.Binary.toPoly_mod_two_pow_succ, CompPoly.RabinCert.Binary.toPoly_clmulBits, CompPoly.RabinCert.Binary.toPoly_clmul, CompPoly.RabinCert.Binary.Step, CompPoly.RabinCert.Binary.checkStep, CompPoly.RabinCert.Binary.runChain, CompPoly.RabinCert.Binary.chainExp, CompPoly.RabinCert.Binary.checkStep_sound, CompPoly.RabinCert.Binary.step_sound, CompPoly.RabinCert.Binary.runChain_sound, CompPoly.RabinCert.Binary.xpow_mod_of_runChain, CompPoly.RabinCert.Binary.dvd_X_pow_sub_X_of_runChain, CompPoly.RabinCert.Binary.isCoprime_X_pow_sub_X_of_runChain
statement: formalized
proof: formalized
---

# Rabin certificates over `GF(2)` on `ℕ` bitmasks

`CompPoly.Data.Polynomial.RabinCertificateBinary`, in [CompPoly/Data/Polynomial/RabinCertificateBinary.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean), by CompPoly Contributors.

> `CompPoly/Data/Polynomial/RabinCertificate.lean` checks a square-and-multiply chain on
> little-endian coefficient lists with schoolbook arithmetic, which works over any prime field.
> Over `GF(2)` a polynomial is a bitmask: bit `i` of `n : ℕ` is the coefficient of `X^i`.
> Addition is `xor` and multiplication is carry-less, so the kernel checks each step with a few
> GMP-backed `Nat` operations (`xor`, `shiftLeft`, `%`, `/`) instead of walking lists of
> numerals. For the degree-64 modulus of `BF64` this takes the certificate check from about 26 s
> to about 2 s.
>
> The chain format mirrors the list version: each `Step` carries the quotient and remainder of
> one squaring (or multiply-by-`X`) step, the kernel checks `cur² = q·f + r` exactly, and
> `runChain_sound` lifts a checked chain to `X^N % f = r % f` in `(ZMod 2)[X]`. Because the
> bitmask of a `GF(2)` polynomial is unique, checks compare with `==` and need no reduction.
>
> ## Main definitions
>
> * `clmul` — carry-less product of two bitmasks, by structural recursion on a bit count.
> * `toPoly` — the polynomial a bitmask denotes. Specification only; checking never evaluates it.
> * `Step`, `checkStep`, `runChain`, `chainExp` — the chain checker.
>
> ## Main statements
>
> * `toPoly_clmul` — `clmul` is polynomial multiplication.
> * `dvd_X_pow_sub_X_of_runChain`, `isCoprime_X_pow_sub_X_of_runChain` — the two Rabin
>   conditions from certificates, with the same shape as the list versions, so they feed
>   `irreducible_of_rabin_prime_degree` and its siblings unchanged.
>
> Certificate data comes from `scripts/gen_rabin_certificate.py --binary`.

> ### Carry-less multiplication

`CompPoly.RabinCert.Binary.clmulBits` (definition, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L52))

> Carry-less product of the low `n` bits of `a` with `b`. Structural recursion on `n`, so the
> kernel unfolds it once per bit of `a`.

```lean
def clmulBits : ℕ → ℕ → ℕ → ℕ
```

`CompPoly.RabinCert.Binary.clmul` (definition, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L57))

> Carry-less product of two bitmasks: polynomial multiplication over `GF(2)`.

```lean
def clmul (a b : ℕ) : ℕ
```

> ### The specification bridge

`CompPoly.RabinCert.Binary.toPoly` (definition, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L63))

> The polynomial over `GF(2)` whose coefficient of `X^i` is bit `i` of `n`. Every set bit of
> `n` is below `n`, so the sum over `range n` covers them. Specification only.

```lean
noncomputable def toPoly (n : ℕ) : (ZMod 2)[X]
```

`CompPoly.RabinCert.Binary.coeff_toPoly` (theorem, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L66))

```lean
theorem coeff_toPoly (n i : ℕ) :
    (toPoly n).coeff i = if n.testBit i then 1 else 0
```

`CompPoly.RabinCert.Binary.toPoly_congr` (theorem, [line 85](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L85))

> Two bitmasks with the same bits denote the same polynomial.

```lean
theorem toPoly_congr {a b : ℕ} (h : ∀ i, a.testBit i = b.testBit i) : toPoly a = toPoly b
```

`CompPoly.RabinCert.Binary.toPoly_zero` (theorem, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L89))

```lean
theorem toPoly_zero : toPoly 0 = 0
```

`CompPoly.RabinCert.Binary.toPoly_xor` (theorem, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L93))

```lean
theorem toPoly_xor (a b : ℕ) : toPoly (a ^^^ b) = toPoly a + toPoly b
```

`CompPoly.RabinCert.Binary.toPoly_two_pow` (theorem, [line 98](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L98))

```lean
theorem toPoly_two_pow (k : ℕ) : toPoly (2 ^ k) = X ^ k
```

`CompPoly.RabinCert.Binary.toPoly_one` (theorem, [line 105](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L105))

```lean
theorem toPoly_one : toPoly 1 = 1
```

`CompPoly.RabinCert.Binary.toPoly_two` (theorem, [line 109](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L109))

> The bitmask `2` is `X`.

```lean
theorem toPoly_two : toPoly 2 = X
```

`CompPoly.RabinCert.Binary.toPoly_shiftLeft_one` (theorem, [line 112](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L112))

```lean
theorem toPoly_shiftLeft_one (a : ℕ) : toPoly (a <<< 1) = X * toPoly a
```

`CompPoly.RabinCert.Binary.toPoly_mod_two_pow_succ` (theorem, [line 121](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L121))

> Splitting off the lowest bit: the low `n + 1` bits of `a` are bit `0` plus `X` times the low
> `n` bits of `a / 2`.

```lean
theorem toPoly_mod_two_pow_succ (a n : ℕ) :
    toPoly (a % 2 ^ (n + 1)) = (if a % 2 = 1 then 1 else 0) + X * toPoly (a / 2 % 2 ^ n)
```

`CompPoly.RabinCert.Binary.toPoly_clmulBits` (theorem, [line 136](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L136))

```lean
theorem toPoly_clmulBits (n a b : ℕ) :
    toPoly (clmulBits n a b) = toPoly (a % 2 ^ n) * toPoly b
```

`CompPoly.RabinCert.Binary.toPoly_clmul` (theorem, [line 147](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L147))

> **`clmul` is polynomial multiplication over `GF(2)`.**

```lean
theorem toPoly_clmul (a b : ℕ) : toPoly (clmul a b) = toPoly a * toPoly b
```

> ### Square-and-multiply chains

`CompPoly.RabinCert.Binary.Step` (structure, [line 155](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L155))

> One step of a square-and-multiply chain modulo `f`, as for the list checker: square the
> current residue (`mulX = false`) or multiply it by `X` (`mulX = true`), with quotient `q` and
> next residue `r` supplied by the generator.

```lean
structure Step where
  /-- `true` for a multiply-by-`X` step, `false` for a squaring step. -/
  mulX : Bool
  /-- The quotient of the step's product by the modulus, as a bitmask. -/
  q : ℕ
  /-- The remainder — the next residue in the chain — as a bitmask. -/
  r : ℕ
```

`CompPoly.RabinCert.Binary.checkStep` (definition, [line 164](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L164))

> Check one chain step: `cur² = q·f + r` (or `X·cur = q·f + r`) over `GF(2)`.

```lean
def checkStep (f cur : ℕ) (s : Step) : Bool
```

`CompPoly.RabinCert.Binary.runChain` (definition, [line 169](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L169))

> Fold a chain of steps from the residue `cur`, checking each; returns the final residue, or
> `none` if any check fails. One kernel reduction of `runChain` verifies a whole chain.

```lean
def runChain (f : ℕ) : ℕ → List Step → Option ℕ
```

`CompPoly.RabinCert.Binary.chainExp` (definition, [line 174](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L174))

> The exponent a chain computes: squaring doubles it, multiply-by-`X` adds one.

```lean
def chainExp : ℕ → List Step → ℕ
```

`CompPoly.RabinCert.Binary.checkStep_sound` (theorem, [line 179](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L179))

> A checked step is a polynomial identity.

```lean
theorem checkStep_sound {f cur : ℕ} {s : Step} (h : checkStep f cur s = true) :
    toPoly (cond s.mulX (cur <<< 1) (clmul cur cur)) = toPoly s.q * toPoly f + toPoly s.r
```

`CompPoly.RabinCert.Binary.step_sound` (theorem, [line 190](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L190))

> Soundness of one chain step.

```lean
theorem step_sound {fN cur : ℕ} {f : (ZMod 2)[X]} (hfN : toPoly fN = f) (hf0 : f ≠ 0)
    {s : Step} {e : ℕ} (hcheck : checkStep fN cur s = true)
    (hprev : (X : (ZMod 2)[X]) ^ e % f = toPoly cur % f) :
    (X : (ZMod 2)[X]) ^ (cond s.mulX (e + 1) (2 * e)) % f = toPoly s.r % f
```

`CompPoly.RabinCert.Binary.runChain_sound` (theorem, [line 222](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L222))

> **Soundness of a whole chain**: a checked chain starting at the residue of `X^e` ends at
> the residue of `X^(chainExp e steps)`.

```lean
theorem runChain_sound {fN : ℕ} {f : (ZMod 2)[X]} (hfN : toPoly fN = f) (hf0 : f ≠ 0) :
    ∀ (steps : List Step) (cur out : ℕ) (e : ℕ),
      runChain fN cur steps = some out →
      (X : (ZMod 2)[X]) ^ e % f = toPoly cur % f →
      (X : (ZMod 2)[X]) ^ chainExp e steps % f = toPoly out % f
```

`CompPoly.RabinCert.Binary.xpow_mod_of_runChain` (theorem, [line 241](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L241))

> A chain started at `2` (the bitmask of `X`) computes `X^N % f`.

```lean
theorem xpow_mod_of_runChain {fN : ℕ} {f : (ZMod 2)[X]} (hfN : toPoly fN = f) (hf0 : f ≠ 0)
    {steps : List Step} {out N : ℕ} (hrun : runChain fN 2 steps = some out)
    (hexp : chainExp 1 steps = N) :
    (X : (ZMod 2)[X]) ^ N % f = toPoly out % f
```

> ### The two Rabin conditions from certificates

`CompPoly.RabinCert.Binary.dvd_X_pow_sub_X_of_runChain` (theorem, [line 253](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L253))

> **The trace condition from a chain.** A checked chain for `X^N` ending back at `2` (the
> residue `X`) proves `f ∣ X^N - X`.

```lean
theorem dvd_X_pow_sub_X_of_runChain {fN : ℕ} {f : (ZMod 2)[X]} (hfN : toPoly fN = f)
    (hf0 : f ≠ 0) {steps : List Step} {N : ℕ} (hrun : runChain fN 2 steps = some 2)
    (hexp : chainExp 1 steps = N) :
    f ∣ (X : (ZMod 2)[X]) ^ N - X
```

`CompPoly.RabinCert.Binary.isCoprime_X_pow_sub_X_of_runChain` (theorem, [line 266](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean#L266))

> **The coprimality condition from a chain plus a Bézout certificate.** The chain reduces `X^N`
> to a residue `rp`; `rp = w ^^^ 2` says `rp = w + X`, so `X^N - X ≡ w (mod f)`, and the Bézout
> identity `u·f + v·w = 1` witnesses `IsCoprime f (X^N - X)`.

```lean
theorem isCoprime_X_pow_sub_X_of_runChain {fN : ℕ} {f : (ZMod 2)[X]} (hfN : toPoly fN = f)
    (hf0 : f ≠ 0) {steps : List Step} {rp w u v N : ℕ}
    (hrun : runChain fN 2 steps = some rp)
    (hexp : chainExp 1 steps = N)
    (hw : (rp == w ^^^ 2) = true)
    (hbez : (clmul u fN ^^^ clmul v w == 1) = true) :
    IsCoprime f ((X : (ZMod 2)[X]) ^ N - X)
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Proof depends on

- [Kernel-checkable Rabin irreducibility certificates over prime fields](rabincertificate.md)

## Sources

- [CompPoly/Data/Polynomial/RabinCertificateBinary.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Polynomial/RabinCertificateBinary.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.Polynomial.RabinCertificateBinary.json)
