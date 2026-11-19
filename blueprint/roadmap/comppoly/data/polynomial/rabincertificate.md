---
catalog: module
lean: CompPoly.RabinCert.addNat, CompPoly.RabinCert.scaleNat, CompPoly.RabinCert.mulNat, CompPoly.RabinCert.eqModP, CompPoly.RabinCert.toPoly, CompPoly.RabinCert.toPoly_nil, CompPoly.RabinCert.toPoly_cons, CompPoly.RabinCert.toPoly_X, CompPoly.RabinCert.toPoly_one, CompPoly.RabinCert.toPoly_addNat, CompPoly.RabinCert.toPoly_scaleNat, CompPoly.RabinCert.toPoly_mulNat, CompPoly.RabinCert.cast_eq_cast_of_mod_eq, CompPoly.RabinCert.toPoly_eq_zero_of_all_mod_eq_zero, CompPoly.RabinCert.toPoly_eq_of_eqModP, CompPoly.RabinCert.verify_mulAdd, CompPoly.RabinCert.Step, CompPoly.RabinCert.checkStep, CompPoly.RabinCert.runChain, CompPoly.RabinCert.chainExp, CompPoly.RabinCert.step_sound, CompPoly.RabinCert.runChain_sound, CompPoly.RabinCert.xpow_mod_of_runChain, CompPoly.RabinCert.dvd_sub_of_mod_eq, CompPoly.RabinCert.dvd_X_pow_sub_X_of_runChain, CompPoly.RabinCert.isCoprime_X_pow_sub_X_of_runChain, CompPoly.RabinCert.irreducible_of_rabin_prime_degree, CompPoly.RabinCert.irreducible_of_rabin_prime_degree_of_card, CompPoly.RabinCert.irreducible_of_rabin_prime_power, CompPoly.RabinCert.irreducible_of_rabin_two_prime_factors, CompPoly.RabinCert.irreducible_of_rabin_degree_six, CompPoly.RabinCert.irreducible_of_rabin_degree_six_of_card
statement: formalized
proof: formalized
---

# Kernel-checkable Rabin irreducibility certificates over prime fields

`CompPoly.Data.Polynomial.RabinCertificate`, in [CompPoly/Data/Polynomial/RabinCertificate.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean), by Derek Sorensen.

> Rabin's test (`CompPoly/Data/Polynomial/Rabin.lean`) reduces irreducibility of a degree-`d`
> polynomial `f` over `ZMod p` to divisibility and coprimality conditions against `X^(p^k) - X`.
> Verifying those conditions requires computing `X^(p^k) mod f` — around `d · log₂ p` modular
> squarings — which is far beyond what `decide` can do on `Polynomial` values and which this
> repository's TCB policy forbids delegating to `native_decide`.
>
> This file provides the reusable, degree-agnostic *certificate* infrastructure:
>
> * Polynomials are represented as little-endian `ℕ`-coefficient lists (`toPoly` interprets them
>   in `(ZMod p)[X]`), with schoolbook arithmetic (`addNat`, `mulNat`) by structural recursion,
>   so every check reduces in the kernel via GMP-accelerated `Nat` operations.
> * A certificate `Step` records a squaring (or multiply-by-`X`) together with the quotient and
>   remainder of the division by `f`; `checkStep` verifies `cur² = q·f + r` (coefficientwise,
>   mod `p`) and `runChain` folds a whole square-and-multiply chain, so an entire exponentiation
>   certificate is one list literal checked by a single kernel reduction.
> * `runChain_sound` lifts a checked chain to `X^N % f = r % f` in `(ZMod p)[X]`; the two Rabin
>   conditions follow via `dvd_X_pow_sub_X_of_runChain` (trace) and
>   `isCoprime_X_pow_sub_X_of_runChain` (coprimality, from a Bézout certificate on the reduced
>   residue).
> * `irreducible_of_rabin_prime_degree` packages Rabin's test for *prime* degree `d`, where the
>   conditions collapse to a single trace and a single coprimality check;
>   `irreducible_of_rabin_prime_power` does the same at `d = ℓ ^ k`, where the collapse is still
>   sound; `irreducible_of_rabin_two_prime_factors` and `irreducible_of_rabin_degree_six` cover a
>   degree with two distinct prime factors. All take the field size as a numeral `q` with
>   `Fintype.card F = q`, the shape concrete extensions use.
>
> Certificate data is produced by the untrusted generator `scripts/gen_rabin_certificate.py`;
> the kernel re-checks every step. Contrast `CompPoly/Fields/Binary/BF128Ghash/`, the bespoke
> GF(2¹²⁸) predecessor of this framework, which spells out each step as a separate lemma.

> ### `ℕ`-level polynomial arithmetic
>
> Little-endian coefficient lists. No coefficient is ever reduced during a product — entries
> stay below `d² · p²`, comfortably inside GMP range — and comparisons reduce mod `p` at the
> end (`eqModP`), so no subtraction (and hence no truncation) occurs anywhere.

`CompPoly.RabinCert.addNat` (definition, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L60))

> Coefficientwise addition of little-endian coefficient lists.

```lean
def addNat : List ℕ → List ℕ → List ℕ
```

`CompPoly.RabinCert.scaleNat` (definition, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L66))

> Scale a coefficient list by a constant.

```lean
def scaleNat (c : ℕ) (l : List ℕ) : List ℕ
```

`CompPoly.RabinCert.mulNat` (definition, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L69))

> Schoolbook product of little-endian coefficient lists.

```lean
def mulNat : List ℕ → List ℕ → List ℕ
```

`CompPoly.RabinCert.eqModP` (definition, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L74))

> Coefficientwise equality modulo `p`, treating entries beyond a list's end as `0`.

```lean
def eqModP (p : ℕ) : List ℕ → List ℕ → Bool
```

> ### The specification bridge

`CompPoly.RabinCert.toPoly` (definition, [line 83](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L83))

> Interpret a little-endian coefficient list in `(ZMod p)[X]`, Horner-style. Specification
> only; certificate checking never evaluates it.

```lean
noncomputable def toPoly (p : ℕ) : List ℕ → (ZMod p)[X]
```

`CompPoly.RabinCert.toPoly_nil` (theorem, [line 87](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L87))

```lean
theorem toPoly_nil {p : ℕ} : toPoly p [] = 0
```

`CompPoly.RabinCert.toPoly_cons` (theorem, [line 91](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L91))

> The defining Horner step of `toPoly`, as a rewrite rule: a head coefficient contributes a
> constant and the tail is multiplied by `X`.

```lean
theorem toPoly_cons {p : ℕ} (c : ℕ) (cs : List ℕ) :
    toPoly p (c :: cs) = C (c : ZMod p) + X * toPoly p cs
```

`CompPoly.RabinCert.toPoly_X` (theorem, [line 94](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L94))

```lean
theorem toPoly_X {p : ℕ} : toPoly p [0, 1] = X
```

`CompPoly.RabinCert.toPoly_one` (theorem, [line 98](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L98))

```lean
theorem toPoly_one {p : ℕ} : toPoly p [1] = 1
```

`CompPoly.RabinCert.toPoly_addNat` (theorem, [line 104](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L104))

> `addNat` denotes addition: the coefficientwise sum of two lists is the sum of the
> polynomials they denote. One of the three specification bridges that make the `ℕ`-list
> arithmetic usable as a certificate format.

```lean
theorem toPoly_addNat {p : ℕ} : ∀ a b : List ℕ,
    toPoly p (addNat a b) = toPoly p a + toPoly p b
```

`CompPoly.RabinCert.toPoly_scaleNat` (theorem, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L114))

> `scaleNat` denotes multiplication by a constant.

```lean
theorem toPoly_scaleNat {p : ℕ} (c : ℕ) : ∀ l : List ℕ,
    toPoly p (scaleNat c l) = C (c : ZMod p) * toPoly p l
```

`CompPoly.RabinCert.toPoly_mulNat` (theorem, [line 125](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L125))

> `mulNat` denotes multiplication: schoolbook convolution of the coefficient lists is the
> product of the polynomials they denote. Proved from `toPoly_addNat` and `toPoly_scaleNat`,
> following the same recursion `mulNat` uses.

```lean
theorem toPoly_mulNat {p : ℕ} : ∀ a b : List ℕ,
    toPoly p (mulNat a b) = toPoly p a * toPoly p b
```

`CompPoly.RabinCert.cast_eq_cast_of_mod_eq` (theorem, [line 135](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L135))

> Two naturals equal mod `p` cast to the same element of `ZMod p`.

```lean
theorem cast_eq_cast_of_mod_eq {p a b : ℕ} (h : a % p = b % p) :
    (a : ZMod p) = (b : ZMod p)
```

`CompPoly.RabinCert.toPoly_eq_zero_of_all_mod_eq_zero` (theorem, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L142))

> A list whose every coefficient is `0` mod `p` denotes the zero polynomial. This is the base
> case behind `toPoly_eq_of_eqModP`, which is how a `eqModP` kernel check becomes an equation
> between polynomials.

```lean
theorem toPoly_eq_zero_of_all_mod_eq_zero {p : ℕ} : ∀ {l : List ℕ},
    l.all (· % p == 0) = true → toPoly p l = 0
```

`CompPoly.RabinCert.toPoly_eq_of_eqModP` (theorem, [line 151](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L151))

> Soundness of the coefficientwise checker: `eqModP` lists denote the same polynomial.

```lean
theorem toPoly_eq_of_eqModP {p : ℕ} : ∀ {a b : List ℕ},
    eqModP p a b = true → toPoly p a = toPoly p b
```

`CompPoly.RabinCert.verify_mulAdd` (theorem, [line 167](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L167))

> Lift a checked `ℕ`-level identity `a·b ≡ q·f + r (mod p)` to `(ZMod p)[X]`.

```lean
theorem verify_mulAdd {p : ℕ} {a b q fL r : List ℕ}
    (h : eqModP p (mulNat a b) (addNat (mulNat q fL) r) = true) :
    toPoly p a * toPoly p b = toPoly p q * toPoly p fL + toPoly p r
```

> ### Square-and-multiply chains

`CompPoly.RabinCert.Step` (structure, [line 181](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L181))

> One step of a square-and-multiply chain modulo `f`: from the current residue `cur`, either
> square it (`mulX = false`) or multiply it by `X` (`mulX = true`), and divide by `f` to get
> quotient `q` and next residue `r`. The generator supplies `q` and `r`; the checker only has
> to confirm one polynomial identity per step.

```lean
structure Step where
  /-- `true` for a multiply-by-`X` step, `false` for a squaring step. -/
  mulX : Bool
  /-- The quotient of the step's product by the modulus. -/
  q : List ℕ
  /-- The remainder — the next residue in the chain. -/
  r : List ℕ
```

`CompPoly.RabinCert.checkStep` (definition, [line 190](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L190))

> Check one chain step: `cur² = q·f + r` (or `X·cur = q·f + r`), coefficientwise mod `p`.

```lean
def checkStep (p : ℕ) (fL cur : List ℕ) (s : Step) : Bool
```

`CompPoly.RabinCert.runChain` (definition, [line 195](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L195))

> Fold a chain of steps from the residue `cur`, checking each; returns the final residue,
> or `none` if any check fails. One kernel reduction of `runChain` verifies a whole chain.

```lean
def runChain (p : ℕ) (fL : List ℕ) : List ℕ → List Step → Option (List ℕ)
```

`CompPoly.RabinCert.chainExp` (definition, [line 200](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L200))

> The exponent a chain computes: squaring doubles it, multiply-by-`X` adds one.

```lean
def chainExp : ℕ → List Step → ℕ
```

`CompPoly.RabinCert.step_sound` (theorem, [line 211](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L211))

> Soundness of one chain step.

```lean
theorem step_sound {p : ℕ} [Fact p.Prime] {fL cur : List ℕ} {f : (ZMod p)[X]}
    (hfL : toPoly p fL = f) (hf0 : f ≠ 0) {s : Step} {e : ℕ}
    (hcheck : checkStep p fL cur s = true)
    (hprev : (X : (ZMod p)[X]) ^ e % f = toPoly p cur % f) :
    (X : (ZMod p)[X]) ^ (cond s.mulX (e + 1) (2 * e)) % f = toPoly p s.r % f
```

`CompPoly.RabinCert.runChain_sound` (theorem, [line 248](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L248))

> **Soundness of a whole chain**: a checked chain starting at the residue of `X^e` ends at
> the residue of `X^(chainExp e steps)`.

```lean
theorem runChain_sound {p : ℕ} [Fact p.Prime] {fL : List ℕ} {f : (ZMod p)[X]}
    (hfL : toPoly p fL = f) (hf0 : f ≠ 0) :
    ∀ (steps : List Step) (cur out : List ℕ) (e : ℕ),
      runChain p fL cur steps = some out →
      (X : (ZMod p)[X]) ^ e % f = toPoly p cur % f →
      (X : (ZMod p)[X]) ^ chainExp e steps % f = toPoly p out % f
```

`CompPoly.RabinCert.xpow_mod_of_runChain` (theorem, [line 268](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L268))

> A chain started at `[0, 1]` (the residue of `X¹`) computes `X^N % f`.

```lean
theorem xpow_mod_of_runChain {p : ℕ} [Fact p.Prime] {fL : List ℕ} {f : (ZMod p)[X]}
    (hfL : toPoly p fL = f) (hf0 : f ≠ 0) {steps : List Step} {out : List ℕ} {N : ℕ}
    (hrun : runChain p fL [0, 1] steps = some out)
    (hexp : chainExp 1 steps = N) :
    (X : (ZMod p)[X]) ^ N % f = toPoly p out % f
```

> ### The two Rabin conditions from certificates

`CompPoly.RabinCert.dvd_sub_of_mod_eq` (theorem, [line 280](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L280))

> Equal remainders mean the divisor divides the difference.

```lean
theorem dvd_sub_of_mod_eq {R : Type*} [EuclideanDomain R] {a b n : R} (h : a % n = b % n) :
    n ∣ a - b
```

`CompPoly.RabinCert.dvd_X_pow_sub_X_of_runChain` (theorem, [line 290](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L290))

> **The trace condition from a chain.** A checked chain for `X^N` ending back at `[0, 1]`
> (the residue `X`) proves `f ∣ X^N - X`.

```lean
theorem dvd_X_pow_sub_X_of_runChain {p : ℕ} [Fact p.Prime] {fL : List ℕ} {f : (ZMod p)[X]}
    (hfL : toPoly p fL = f) (hf0 : f ≠ 0) {steps : List Step} {N : ℕ}
    (hrun : runChain p fL [0, 1] steps = some [0, 1])
    (hexp : chainExp 1 steps = N) :
    f ∣ (X : (ZMod p)[X]) ^ N - X
```

`CompPoly.RabinCert.isCoprime_X_pow_sub_X_of_runChain` (theorem, [line 306](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L306))

> **The coprimality condition from a chain plus a Bézout certificate.**
>
> The chain reduces `X^N` to a residue `rp`; writing `rp = w + X` (checked by `eqModP`), we have
> `X^N - X ≡ w (mod f)`, so a Bézout identity `u·f + v·w = 1` (again checked by `eqModP`)
> witnesses `IsCoprime f (X^N - X)`.

```lean
theorem isCoprime_X_pow_sub_X_of_runChain {p : ℕ} [Fact p.Prime] {fL : List ℕ} {f : (ZMod p)[X]}
    (hfL : toPoly p fL = f) (hf0 : f ≠ 0) {steps : List Step} {rp w u v : List ℕ} {N : ℕ}
    (hrun : runChain p fL [0, 1] steps = some rp)
    (hexp : chainExp 1 steps = N)
    (hw : eqModP p rp (addNat w [0, 1]) = true)
    (hbez : eqModP p (addNat (mulNat u fL) (mulNat v w)) [1] = true) :
    IsCoprime f ((X : (ZMod p)[X]) ^ N - X)
```

> ### Packaging Rabin's test at a concrete degree
>
> `Polynomial.irreducible_of_rabin` already quantifies the coprimality condition over
> `d.primeFactors`. The wrappers below discharge that quantifier for the shapes of `d` that
> concrete extensions use, so a caller supplies one coprimality proof per prime factor and nothing
> else. Each takes the field size as a numeral `q` with `hcard : Fintype.card F = q`, exactly as
> `Polynomial.irreducible_of_rabin` does — supply `ZMod.card _` at a concrete field, or `rfl` to
> read the conditions at `Fintype.card F`. The section comment in
> `CompPoly/Data/Polynomial/Rabin.lean` records why that is the only shape these statements have.
>
> Note that `irreducible_of_rabin_prime_degree` does **not** apply at composite `d`, and its
> collapsed condition is not merely inconvenient but unsound there: a product of equal-degree
> factors divides `X^(q^d) - X` and is coprime to `X^q - X`, so it would pass.
> `irreducible_of_rabin_prime_power` is the collapse that *is* sound at `d = ℓ ^ k`.

`CompPoly.RabinCert.irreducible_of_rabin_prime_degree` (theorem, [line 351](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L351))

> **Rabin's test for prime degree.** For `f` of *prime* degree `d` over a finite field with `q`
> elements, the per-prime-factor conditions collapse to a single coprimality check at exponent `q`:
> `f` is irreducible provided `f ∣ X^(q^d) - X` and `IsCoprime f (X^q - X)`.

```lean
theorem irreducible_of_rabin_prime_degree {F : Type*} [Field F] [Fintype F] {f : F[X]} {d q : ℕ}
    (hcard : Fintype.card F = q)
    (hd : d.Prime) (h_deg : f.natDegree = d)
    (h_trace : f ∣ X ^ (q ^ d) - X)
    (h_cop : IsCoprime f (X ^ q - X)) :
    Irreducible f
```

`CompPoly.RabinCert.irreducible_of_rabin_prime_degree_of_card` (alias, [line 364](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L364))

```lean
alias irreducible_of_rabin_prime_degree_of_card
```

`CompPoly.RabinCert.irreducible_of_rabin_prime_power` (theorem, [line 378](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L378))

> **Rabin's test for a prime-power degree**, such as `d = 8`, `64` or `128`.
>
> `d = ℓ ^ k` has the single prime factor `ℓ`, so — exactly as at prime degree — the caller supplies
> the trace condition plus one coprimality certificate, here at exponent `q ^ (d / ℓ)`. Unlike
> `irreducible_of_rabin_prime_degree` this is *sound* at composite `d`: the check at `d / ℓ` rules
> out every proper divisor of `d`, because every proper divisor of `ℓ ^ k` divides `ℓ ^ (k - 1)`.
>
> `d` is kept separate from `ℓ ^ k` and tied to it by `hd_eq` so that the conditions read at the
> caller's numeral (`q ^ 64`, not `q ^ 2 ^ 6`); supply `hd_eq` as `by norm_num`. This is the shape
> the characteristic-two moduli use — `Aes.modulus` at `d = 8` and `BF64.basePoly` at `d = 64`.

```lean
theorem irreducible_of_rabin_prime_power {F : Type*} [Field F] [Fintype F] {f : F[X]}
    {d ℓ k q : ℕ} (hcard : Fintype.card F = q)
    (hℓ : ℓ.Prime) (hk : k ≠ 0) (hd_eq : d = ℓ ^ k)
    (h_deg : f.natDegree = d)
    (h_trace : f ∣ X ^ (q ^ d) - X)
    (h_cop : IsCoprime f (X ^ (q ^ (d / ℓ)) - X)) :
    Irreducible f
```

`CompPoly.RabinCert.irreducible_of_rabin_two_prime_factors` (theorem, [line 402](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L402))

> **Rabin's test for a degree with exactly two prime factors**, such as `d = 6`.
>
> The caller supplies the trace condition plus one coprimality certificate per prime factor, at
> exponents `q^(d/ℓ₁)` and `q^(d/ℓ₂)`. The hypothesis `h_factors` is `by decide` at a concrete
> degree — for `d = 6` it is `(6 : ℕ).primeFactors = {2, 3}`, giving checks at `q^3` and `q^2`.
>
> Both checks are needed. Dropping the `q^3` one admits a product of two irreducible cubics;
> dropping the `q^2` one admits a product of three irreducible quadratics.

```lean
theorem irreducible_of_rabin_two_prime_factors {F : Type*} [Field F] [Fintype F] {f : F[X]}
    {d ℓ₁ ℓ₂ q : ℕ} (hcard : Fintype.card F = q)
    (h_deg : f.natDegree = d) (h_pos : 0 < d)
    (h_factors : d.primeFactors = {ℓ₁, ℓ₂})
    (h_trace : f ∣ X ^ (q ^ d) - X)
    (h_cop₁ : IsCoprime f (X ^ (q ^ (d / ℓ₁)) - X))
    (h_cop₂ : IsCoprime f (X ^ (q ^ (d / ℓ₂)) - X)) :
    Irreducible f
```

`CompPoly.RabinCert.irreducible_of_rabin_degree_six` (theorem, [line 436](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L436))

> **Rabin's test at degree 6.** `f` of degree 6 over a finite field with `q` elements is irreducible
> provided `f ∣ X^(q^6) - X`, `IsCoprime f (X^(q^3) - X)`, and `IsCoprime f (X^(q^2) - X)`.
>
> This is the shape used by the KoalaBear degree-6 extension. It differs from
> `irreducible_of_rabin_two_prime_factors` only in discharging `Nat.primeFactors 6 = {2, 3}`
> internally, so callers never touch `Nat.primeFactors`.
>
> The `q^3` check is what rules out a product of two irreducible cubics, and the `q^2` check a
> product of three irreducible quadratics; the trace condition alone permits both.

```lean
theorem irreducible_of_rabin_degree_six {F : Type*} [Field F] [Fintype F] {f : F[X]} {q : ℕ}
    (hcard : Fintype.card F = q)
    (h_deg : f.natDegree = 6)
    (h_trace : f ∣ X ^ (q ^ 6) - X)
    (h_cop₃ : IsCoprime f (X ^ (q ^ 3) - X))
    (h_cop₂ : IsCoprime f (X ^ (q ^ 2) - X)) :
    Irreducible f
```

`CompPoly.RabinCert.irreducible_of_rabin_degree_six_of_card` (alias, [line 447](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean#L447))

```lean
alias irreducible_of_rabin_degree_six_of_card
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Proof depends on

- [Rabin's irreducibility test](rabin.md)
- [Canonical Euclidean Domains](../ringtheory/canonicaleuclideandomain.md)

## Sources

- [CompPoly/Data/Polynomial/RabinCertificate.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/RabinCertificate.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.Polynomial.RabinCertificate.json)
