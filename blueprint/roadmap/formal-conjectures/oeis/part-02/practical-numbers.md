---
declaration: theorem
origin: cited
lean: OeisA5153.conjecture
statement: formalized
---

# Practical numbers

> A positive integer $n$ is called a *practical number* (or *panarithmic number*) if every positive
> integer $m \le n$ can be represented as a sum of distinct divisors of $n$.
>
> *References:*
> - [A005153](https://oeis.org/A005153)

*Quoted from [FormalConjectures/OEIS/5153.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/5153.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA5153.conjecture`

Open: stated without proof.

> Conjecture: every odd number, beginning with 3, is the sum of a prime number and a practical
> number.
> - Hal M. Switkay, Jan 28 2023

```lean
theorem conjecture (n : ℕ) (hn : 3 ≤ n) (hodd : Odd n) :
    ∃ p q : ℕ, p.Prime ∧ A q ∧ n = p + q
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/5153.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/5153.lean#L104).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/5153.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/5153.lean)
- [A005153](https://oeis.org/A005153)
