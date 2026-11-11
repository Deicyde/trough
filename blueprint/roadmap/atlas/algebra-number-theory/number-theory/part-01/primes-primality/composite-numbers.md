---
declaration: section
origin: cited
lean: Nat.IsComposite, Nat.IsComposite.one_lt, Nat.IsComposite.not_prime
statement: formalized
proof: formalized
---

# Composite numbers

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/composite-numbers/index.html).

## Composite numbers

A natural number $n$ is composite if $n > 1$ and $n$ is not prime.

Formalized by `Nat.IsComposite`, a definition declared in [MathlibExt/NumberTheory/Composite.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Composite.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/composite-numbers/index.html#is-composite).

## Composite numbers exceed one

Every composite natural number $n$ satisfies $1 < n$.

Formalized by `Nat.IsComposite.one_lt`, a theorem declared in [MathlibExt/NumberTheory/Composite.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Composite.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/composite-numbers/index.html#one-lt).

## Composite numbers are not prime

A composite natural number is not prime.

Formalized by `Nat.IsComposite.not_prime`, a theorem declared in [MathlibExt/NumberTheory/Composite.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Composite.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/composite-numbers/index.html#not-prime).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Composite numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/composite-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/primes-primality/composite-numbers)
