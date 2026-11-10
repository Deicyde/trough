---
declaration: theorem
origin: cited
lean: OeisA37274.home_prime_conjecture
statement: formalized
---

# Home primes (OEIS A037274)

> Starting from an integer $n\geq 2$, list its prime factors in nondecreasing order with
> multiplicity, concatenate their decimal representations, and repeat. The home-prime conjecture
> says that this process always reaches a prime.
>
> For example,
>
> $$25 \longmapsto 55 \longmapsto 511 \longmapsto 773.$$
>
> *References:*
> * [OEIS A037274](https://oeis.org/A037274)
> * M. Herman and J. Schiffman, *Investigating home primes and their families*,
>   Mathematics Teacher 107 (2014), 606–614

*Quoted from [FormalConjectures/OEIS/37274.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/37274.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA37274.home_prime_conjecture`

Open: stated without proof.

> Every integer at least two reaches a home prime.

```lean
theorem home_prime_conjecture : ∀ n : ℕ, 2 ≤ n → ReachesPrime n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/37274.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/37274.lean#L59).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/37274.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/37274.lean)
- [OEIS A037274](https://oeis.org/A037274)
