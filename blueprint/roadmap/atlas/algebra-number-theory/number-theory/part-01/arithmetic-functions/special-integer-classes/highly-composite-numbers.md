---
declaration: section
origin: cited
lean: Nat.IsHighlyComposite, Nat.IsHighlyComposite.factorization_antitone, Nat.IsHighlyComposite.dvd_of_prime_le
statement: formalized
proof: formalized
---

# Highly composite numbers

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/highly-composite-numbers/index.html).

## Highly composite numbers

A positive natural number is highly composite if it has strictly
more divisors than every smaller positive natural number.

Formalized by `Nat.IsHighlyComposite`, a definition declared in [MathlibExt/NumberTheory/HighlyComposite.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/HighlyComposite.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/highly-composite-numbers/index.html#is-highly-composite).

## Exponents of highly composite numbers are non-increasing

If $H$ is a highly composite
number and $p \le q$ are primes, then the exponent of $q$ in the prime factorization of $H$ is at
most the exponent of $p$.

Formalized by `Nat.IsHighlyComposite.factorization_antitone`, a theorem declared in [MathlibExt/NumberTheory/HighlyComposite.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/HighlyComposite.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/highly-composite-numbers/index.html#factorization-antitone).

## Prime divisors of highly composite numbers form an initial segment

If $H$ is a highly
composite number and $p \le q$ are primes with $q \mid H$, then $p \mid H$. In other words, the
set of primes dividing $H$ is an initial segment of the primes.

Formalized by `Nat.IsHighlyComposite.dvd_of_prime_le`, a theorem declared in [MathlibExt/NumberTheory/HighlyComposite.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/HighlyComposite.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/highly-composite-numbers/index.html#dvd-of-prime-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Highly composite numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/highly-composite-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/highly-composite-numbers)
