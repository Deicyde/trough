---
declaration: theorem
origin: cited
lean: OeisA250131.conjecture_1, OeisA250131.conjecture_2
statement: formalized
---

# Odd part of the digital sum of $3^n$ divided by the maximal power of $3$

> The sequence $a(n)$ is the odd part of the base-$10$ digital sum of $3^n$ divided by the maximal
> possible power of $3$.
>
> *References:*
> - [A250131](https://oeis.org/A250131)

*Quoted from [FormalConjectures/OEIS/250131.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/250131.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA250131.conjecture_1`

Open: stated without proof.

> Conjecture: Consider the sequence $b(n)$ such that $b(1)=2$, $b(2)=3$, and for $n \ge 3$,
> $b(n)=a(n-2)$. If we apply the Eratosthenes-like sieve to $b(n)$ and remove $1$s, then we obtain
> a sequence of primes.
> - _Vladimir Shevelev_, Dec 12 2014

```lean
theorem conjecture_1 : ∀ n ∈ sievedIndices, (b n).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/250131.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/250131.lean#L80).

## `OeisA250131.conjecture_2`

Open: stated without proof.

> Stronger variant: the sieved sequence $b(n)$ yields the set of all primes (in some perturbed
> order).
>
> Note: This stronger statement is not explicitly written on the [A250131](https://oeis.org/A250131)
> OEIS page (which only states `conjecture_1` and notes via _Peter J. C. Moses_ that "these primes
> follow with some perturbation of order"), but is implied by prepending $b(1)=2, b(2)=3$ (which
> otherwise have no effect on the sieve since $\gcd(a(n), 6) = 1$) and by _Vladimir Shevelev_'s
> analogous conjecture in the cross-referenced entries [A221858](https://oeis.org/A221858) and
> [A225039](https://oeis.org/A225039).

```lean
theorem conjecture_2 : b '' sievedIndices = {p : ℕ | p.Prime}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/250131.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/250131.lean#L95).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/250131.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/250131.lean)
- [A250131](https://oeis.org/A250131)
