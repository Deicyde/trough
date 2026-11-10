---
declaration: theorem
origin: cited
lean: OeisA113271.conjecture1
statement: formalized
---

# Ascending descending base exponent transform of $2^n$

> *References:*
> - [A113271](https://oeis.org/A113271)

*Quoted from [FormalConjectures/OEIS/113271.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/113271.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 8 test statements, counted here but not shown.

## `OeisA113271.conjecture1`

Open: stated without proof.

> The first prime terms in this (always odd) sequence are $a(1) = 3$, $a(3) = 41$, and
> $a(4) = 593$. What is the next prime?
>
> The OEIS comment currently says `$a(5) = 543$`, but this conflicts with its defining formula,
> b-file, and examples: the actual index-five term is the composite number `135457`. Consequently the
> search for the next prime must begin after index `4`, not after index `5`.

```lean
theorem conjecture1 :
  conjecture1.answer = a (sInf {n : ℕ | 4 < n ∧ (a n).Prime})
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/113271.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/113271.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/113271.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/113271.lean)
- [A113271](https://oeis.org/A113271)
