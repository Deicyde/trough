---
declaration: theorem
origin: cited
lean: OeisA5258.conjecture
statement: formalized
---

# Apéry numbers

> Apéry numbers:
>
> $$a(n) = \sum_{k=0}^n \binom{n}{k}^2 \binom{n+k}{k}$$
>
> *References:*
> - [A005258](https://oeis.org/A005258)

*Quoted from [FormalConjectures/OEIS/5258.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/5258.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA5258.conjecture`

Open: stated without proof.

> For each $n = 1, 2, 3, \dots$ the polynomial
> $a_n(x) = \sum_{k=0}^n \binom{n}{k}^2 \binom{n+k}{k} x^k$
> is irreducible over the field of rational numbers.
> - Zhi-Wei Sun, Mar 21 2013

```lean
theorem conjecture (n : ℕ) (hn : 1 ≤ n) : Irreducible (aperyPoly n)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/OEIS/5258.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/5258.lean#L67).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/5258.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/5258.lean)
- [A005258](https://oeis.org/A005258)
