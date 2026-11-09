---
declaration: theorem
origin: cited
lean: OeisA401006.eventually_prime
statement: formalized
---

# Decimal concatenation of a cofactor and the largest prime factor

> For a composite positive integer $n$, let $p$ be its largest prime factor. The sequence value
> $a(n)$ concatenates the decimal representations of $n/p$ and $p$, in that order. It fixes primes
> and one, and is extended here by $a(0)=0$. OEIS A397122 records the prime reached by iterating
> this map from each starting value, or $-1$ if no prime is reached.
>
> *References:*
> - [OEIS A401006](https://oeis.org/A401006)
> - [OEIS A397122](https://oeis.org/A397122)

*Quoted from [FormalConjectures/OEIS/401006.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/401006.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 21 test statements and 5 API statements, counted here but not shown.

## `OeisA401006.eventually_prime`

Open: stated without proof.

> If we start at $n \ge 2$, and repeatedly apply the map $k \mapsto a(k)$, we will eventually
> reach a prime, which is then a fixed point.
>
> — [OEIS A401006](https://oeis.org/A401006)

```lean
theorem eventually_prime : ∀ n : ℕ, 2 ≤ n → ReachesPrime n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/401006.lean, line 214](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/401006.lean#L214).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/401006.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/401006.lean)
- [OEIS A401006](https://oeis.org/A401006)
