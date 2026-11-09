---
declaration: theorem
origin: cited
lean: OeisA116150.conjecture
statement: formalized
---

# $a(n) = \sum_{j=1}^{n} (3^j + (-2)^j)$

> *References:*
> - [A116150](https://oeis.org/A116150)

*Quoted from [FormalConjectures/OEIS/116150.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/116150.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA116150.conjecture`

Open: stated without proof.

> First primes are $a(11) = 264353$ and $a(17) = 193622861$.
> Additional primes: $a(71)$, $a(91)$, $a(431)$.
> What is the next prime?

```lean
theorem conjecture : conjecture.answer = a (sInf {n : ℕ | 431 < n ∧ (a n).Prime})
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/116150.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/116150.lean#L60).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/116150.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/116150.lean)
- [A116150](https://oeis.org/A116150)
