---
declaration: section
origin: cited
lean: Nat.IsWieferichPrime, Nat.isWieferichPrime_iff_modEq, Nat.isWieferichPrime_iff_mod
statement: formalized
proof: formalized
---

# Wieferich primes

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/wieferich-primes/index.html).

## Wieferich primes

A natural number $p$ is a Wieferich prime (to base $2$) if $p$ is
prime and $p^2$ divides $2^{p-1} - 1$.

Formalized by `Nat.IsWieferichPrime`, a definition declared in [MathlibExt/NumberTheory/WieferichPrime.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/WieferichPrime.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/wieferich-primes/index.html#is-wieferich-prime).

## Wieferich primes via congruences

For every natural number $p$, $p$ is a Wieferich prime
if and only if $p$ is prime and $2^{p-1} \equiv 1 \pmod{p^2}$.

Formalized by `Nat.isWieferichPrime_iff_modEq`, a theorem declared in [MathlibExt/NumberTheory/WieferichPrime.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/WieferichPrime.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/wieferich-primes/index.html#is-wieferich-prime-iff-mod-eq).

## Wieferich primes via remainders

For every natural number $p$, $p$ is a Wieferich prime
if and only if $p$ is prime and the remainder of $2^{p-1}$ on division by $p^2$ is $1$.

Formalized by `Nat.isWieferichPrime_iff_mod`, a theorem declared in [MathlibExt/NumberTheory/WieferichPrime.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/WieferichPrime.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/wieferich-primes/index.html#is-wieferich-prime-iff-mod).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Wieferich primes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/wieferich-primes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/primes-primality/special-primes/wieferich-primes)
