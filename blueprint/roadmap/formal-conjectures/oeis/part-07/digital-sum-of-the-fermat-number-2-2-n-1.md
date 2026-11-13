---
declaration: theorem
origin: cited
lean: OeisA108301.primes_in_a, OeisA108301.conjecture
statement: formalized
---

# Digital sum of the Fermat number $2^{2^n} + 1$

> `a n` is the digital sum of the Fermat number $2^{2^n} + 1$.
> The conjecture asks if there are any prime numbers in this sequence beyond $n=11$.
>
> *References:*
> - [A108301](https://oeis.org/A108301)

*Quoted from [FormalConjectures/OEIS/108301.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/108301.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 textbook result. It also has 5 test statements, counted here but not shown.

## `OeisA108301.primes_in_a`

Textbook result, proved here.

> $a(0)$, $a(1)$, $a(5)$, $a(6)$, $a(7)$ and $a(11)$ are primes.

```lean
theorem primes_in_a :
    (a 0).Prime ∧ (a 1).Prime ∧ (a 5).Prime ∧
    (a 6).Prime ∧ (a 7).Prime ∧ (a 11).Prime
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/108301.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/108301.lean#L58).

## `OeisA108301.conjecture`

Open: stated without proof.

> $a(0)$, $a(1)$, $a(5)$, $a(6)$, $a(7)$ and $a(11)$ are primes. Are there any more?

```lean
theorem conjecture : ∃ n > 11, (a n).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/108301.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/108301.lean#L67).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/108301.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/108301.lean)
- [A108301](https://oeis.org/A108301)
