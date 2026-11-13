---
declaration: theorem
origin: cited
lean: OeisA166944.conjecture
statement: formalized
---

# Rowland-style prime-generating recurrence

> The sequence is defined by $a(1) = 2$ and for $n \ge 2$:
> $a(n) = a(n-1) + \gcd(n, a(n-1))$ if $n$ is even, and
> $a(n) = a(n-1) + \gcd(n-2, a(n-1))$ if $n$ is odd.
>
> *References:*
> - [A166944](https://oeis.org/A166944)
> - E. S. Rowland, "A natural prime-generating recurrence", *J. Integer Sequences* **11** (2008),
>   Article 08.2.8.
> - V. Shevelev, "An infinite set of generators of primes based on the Rowland idea and
>   conjectures concerning twin primes", arXiv preprint
>   [arXiv:0910.4676](https://arxiv.org/abs/0910.4676) [math.NT], 2009.

*Quoted from [FormalConjectures/OEIS/166944.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/166944.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA166944.conjecture`

Open: stated without proof.

> Conjecture: Every record of differences $a(n)-a(n-1)$ more than 5 is the greater of twin primes
> (A006512).

```lean
theorem conjecture (R : ℕ) (hR : 5 < R) (hrec : IsDifferenceRecord R) :
    IsGreaterTwinPrime R
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/166944.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/166944.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/166944.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/166944.lean)
- [A166944](https://oeis.org/A166944)
