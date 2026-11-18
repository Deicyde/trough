---
catalog: module
lean: Cslib.Crypto.PRG.Family, Cslib.Crypto.PRG.Family.Secure, Cslib.Crypto.PRG.Family.Secure.of_admissible, Cslib.Crypto.PRG.Family.SecureWithError, Cslib.Crypto.PRG.Family.SecureWithError.secure, Cslib.Crypto.PRG.Family.not_secure_of_rangeAdversary, Cslib.Crypto.PRG.Family.not_secure_of_two_mul_card_le, Cslib.Crypto.PRG.Family.not_secure_of_bitstring_stretch, Cslib.Crypto.PRG.Family.not_exists_secure_bitstring_stretch, Cslib.Crypto.PRG.Family.not_secure_of_bitVec_stretch, Cslib.Crypto.PRG.Family.not_exists_secure_bitVec_stretch
statement: formalized
proof: formalized
---

# Asymptotic pseudorandom generator security

`Cslib.Crypto.Primitives.PRG.Asymptotic`, in [Cslib/Crypto/Primitives/PRG/Asymptotic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Asymptotic.lean), by Samuel Schlesinger.

> Security for families of generators means negligible advantage for each admissible
> adversary family, following [BonehShoup2023], Definition 3.1. Negligibility uses Mathlib's
> `Asymptotics.SuperpolynomialDecay`. Admissibility is a predicate on the whole adversary
> family, so a downstream computational model can express a uniform resource restriction.
> This model has a natural-number security parameter and no sampled public system parameters.
> Efficiency of generation and sampling is not asserted by these semantic definitions.
>
> `SecureWithError` bounds every admissible family's advantage at parameter `n` by `ε n`.
> A negligible bound implies `Secure`.
>
> A non-negligible lower bound on the fraction of outputs outside the image rules out security
> when the range-test family is admissible. In particular, a bitstring family that eventually
> stretches by at least one bit is insecure against any class admitting its range test.

`Cslib.Crypto.PRG.Family` (abbreviation, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Asymptotic.lean#L39))

> A security-parameter-indexed collection of deterministic generators.

```lean
abbrev Family (Seed Output : ℕ → Type*)
```

`Cslib.Crypto.PRG.Family.Secure` (definition, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Asymptotic.lean#L49))

> Every admissible adversary family has negligible distinguishing advantage.
> The predicate can encode computational restrictions; `fun _ => True` permits all families.

```lean
def Secure (G : Family Seed Output)
    (Admissible : (∀ n, Adversary (Output n)) → Prop) : Prop
```

`Cslib.Crypto.PRG.Family.Secure.of_admissible` (theorem, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Asymptotic.lean#L56))

> Restricting the admissible adversary families preserves asymptotic security.

```lean
theorem Secure.of_admissible {G : Family Seed Output}
    {Admissible Restricted : (∀ n, Adversary (Output n)) → Prop}
    (h : G.Secure Admissible)
    (hsub : ∀ adversary_family, Restricted adversary_family → Admissible adversary_family) :
    G.Secure Restricted
```

`Cslib.Crypto.PRG.Family.SecureWithError` (definition, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Asymptotic.lean#L64))

> Every admissible adversary family has advantage at most `ε n` at each parameter `n`.

```lean
def SecureWithError (G : Family Seed Output)
    (Admissible : (∀ n, Adversary (Output n)) → Prop) (ε : ℕ → ℝ≥0) : Prop
```

`Cslib.Crypto.PRG.Family.SecureWithError.secure` (theorem, [line 70](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Asymptotic.lean#L70))

> A negligible error bound implies asymptotic security.

```lean
theorem SecureWithError.secure {G : Family Seed Output}
    {Admissible : (∀ n, Adversary (Output n)) → Prop} {ε : ℕ → ℝ≥0}
    (h : G.SecureWithError Admissible ε)
    (hε : Asymptotics.SuperpolynomialDecay atTop (fun n : ℕ => (n : ℝ))
      (fun n => (ε n : ℝ))) : G.Secure Admissible
```

`Cslib.Crypto.PRG.Family.not_secure_of_rangeAdversary` (theorem, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Asymptotic.lean#L87))

> A non-negligible lower bound on the fraction of outputs outside the image rules out
> security whenever exhaustive range testing is admissible.

```lean
theorem not_secure_of_rangeAdversary (G : Family Seed Output)
    {Admissible : (∀ n, Adversary (Output n)) → Prop}
    (ha : Admissible (fun n => (G n).rangeAdversary)) {δ : ℕ → ℝ≥0}
    (hδ : ¬ Asymptotics.SuperpolynomialDecay atTop (fun n : ℕ => (n : ℝ))
      (fun n => (δ n : ℝ)))
    (hgap : ∀ᶠ n in atTop,
      (δ n : ℝ) ≤ 1 - Nat.card (Set.range (G n)) / (Fintype.card (Output n) : ℝ)) :
    ¬ G.Secure Admissible
```

`Cslib.Crypto.PRG.Family.not_secure_of_two_mul_card_le` (theorem, [line 106](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Asymptotic.lean#L106))

> If outputs eventually outnumber seeds by a factor of two, admissibility of exhaustive
> seed enumeration and output comparison suffices to rule out security.

```lean
theorem not_secure_of_two_mul_card_le (G : Family Seed Output)
    {Admissible : (∀ n, Adversary (Output n)) → Prop}
    (ha : Admissible (fun n => (G n).rangeAdversary))
    (hsize : ∀ᶠ n in atTop, 2 * Fintype.card (Seed n) ≤ Fintype.card (Output n)) :
    ¬ G.Secure Admissible
```

`Cslib.Crypto.PRG.Family.not_secure_of_bitstring_stretch` (theorem, [line 130](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Asymptotic.lean#L130))

> A bitstring generator that eventually stretches by at least one bit is insecure
> against any class admitting its range-test family.

```lean
theorem not_secure_of_bitstring_stretch {seedLength outputLength : ℕ → ℕ}
    (G : Family (fun n => Fin (seedLength n) → Bool) (fun n => Fin (outputLength n) → Bool))
    {Admissible : (∀ n, Adversary (Fin (outputLength n) → Bool)) → Prop}
    (ha : Admissible (fun n => (G n).rangeAdversary))
    (hstretch : ∀ᶠ n in atTop, seedLength n < outputLength n) :
    ¬ G.Secure Admissible
```

`Cslib.Crypto.PRG.Family.not_exists_secure_bitstring_stretch` (theorem, [line 145](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Asymptotic.lean#L145))

> No bitstring generator family that eventually stretches by at least one bit is secure
> against all adversary families.

```lean
theorem not_exists_secure_bitstring_stretch {seedLength outputLength : ℕ → ℕ}
    (hstretch : ∀ᶠ n in atTop, seedLength n < outputLength n) :
    ¬ ∃ G : Family (fun n => Fin (seedLength n) → Bool)
      (fun n => Fin (outputLength n) → Bool), G.Secure (fun _ => True)
```

`Cslib.Crypto.PRG.Family.not_secure_of_bitVec_stretch` (theorem, [line 154](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Asymptotic.lean#L154))

> A `BitVec` generator that eventually stretches by at least one bit is insecure
> against any class admitting its range-test family.

```lean
theorem not_secure_of_bitVec_stretch {seedLength outputLength : ℕ → ℕ}
    (G : Family (fun n => BitVec (seedLength n)) (fun n => BitVec (outputLength n)))
    {Admissible : (∀ n, Adversary (BitVec (outputLength n))) → Prop}
    (ha : Admissible (fun n => (G n).rangeAdversary))
    (hstretch : ∀ᶠ n in atTop, seedLength n < outputLength n) :
    ¬ G.Secure Admissible
```

`Cslib.Crypto.PRG.Family.not_exists_secure_bitVec_stretch` (theorem, [line 169](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Asymptotic.lean#L169))

> No `BitVec` generator family that eventually stretches by at least one bit is secure
> against all adversary families.

```lean
theorem not_exists_secure_bitVec_stretch {seedLength outputLength : ℕ → ℕ}
    (hstretch : ∀ᶠ n in atTop, seedLength n < outputLength n) :
    ¬ ∃ G : Family (fun n => BitVec (seedLength n)) (fun n => BitVec (outputLength n)),
      G.Secure (fun _ => True)
```

## Depends on

- [Pseudorandom generators against arbitrary adversaries](basic.md)

## Sources

- [Cslib/Crypto/Primitives/PRG/Asymptotic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Asymptotic.lean)
