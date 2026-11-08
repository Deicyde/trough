---
declaration: lemma
origin: cited
lean: FermatLastTheorem.of_odd_primes
statement: formalized
proof: formalized
---

# FermatLastTheorem.of_odd_primes

If there is a counterexample to Fermat's Last Theorem, then there is a counterexample $a^p+b^p=c^p$ with $p$ an odd prime.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Note: this proof is [in mathlib already](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/FLT/Four.html#FermatLastTheorem.of_odd_primes); we run through it for completeness' sake.

Say $a^n + b^n = c^n$ is a counterexample to Fermat's Last Theorem. Every positive integer is either a power of 2 or has an odd prime factor. If $n=kp$ has an odd prime factor $p$ then $(a^k)^p+(b^k)^p=(c^k)^p$ is the counterexample we seek. It remains to deal with the case where $n$ is a power of 2, so let's assume this. We have $3\leq n$ by assumption, so $n=4k$ must be a multiple of 4, and thus $(a^k)^4=(b^k)^4=(c^k)^4$, giving us a counterexample to Fermat's Last Theorem for $n=4$. However an old result of Fermat himself (proved as [fermatLastTheoremFour](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/FLT/Four.html#fermatLastTheoremFour) in mathlib) says that $x^4+y^4=z^4$ has no solutions in positive integers.

## Lean

Formalized as [`FermatLastTheorem.of_odd_primes`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/FermatLastTheorem.of_odd_primes).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch02reductions.tex, line 19](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch02reductions.tex#L19)
