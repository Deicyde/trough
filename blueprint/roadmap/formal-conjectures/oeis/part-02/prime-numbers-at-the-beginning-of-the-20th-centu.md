---
declaration: theorem
origin: cited
lean: OeisA8578.conjecture
statement: formalized
---

# Prime numbers at the beginning of the 20th century

> The sequence consists of $1$ and the prime numbers. Today $1$ is no longer regarded as a prime.
>
> *References:*
> - [A008578](https://oeis.org/A008578)

*Quoted from [FormalConjectures/OEIS/8578.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/8578.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA8578.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/otoi-lab/oeis-lean-proofs/blob/14f275b8b370bcf76213de10bb3f8fda84a6461e/OeisProofs/FC/A8578.lean#L18-L21](https://github.com/otoi-lab/oeis-lean-proofs/blob/14f275b8b370bcf76213de10bb3f8fda84a6461e/OeisProofs/FC/A8578.lean#L18-L21).

> "Conjecture: the sequence contains exactly those k such that sigma(k) > k*BigOmega(k)."
> - Irina Gerasimova, Jun 08 2013
>
> Here $\sigma(k)$ is the sum of the divisors of $k$ and $\Omega(k)$ is the number of prime factors
> of $k$ counted with multiplicity. Both sides are false for $k = 0$.
>
> Solved by Claude (Anthropic) prompted by otoinobuo. The proof shows $\sigma(k) < k P$ for the
> largest prime factor $P$ of $k$ and uses induction on $k / P$.

```lean
theorem conjecture (k : ℕ) : A k ↔ k * cardFactors k < sigma 1 k
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/8578.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/8578.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/8578.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/8578.lean)
- [A008578](https://oeis.org/A008578)
