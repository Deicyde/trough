---
declaration: theorem
origin: cited
lean: OeisA232174.conjecture
statement: formalized
---

# Representations with prime conditions

> Any integer $n > 1$ can be written as $x + y$ with $x, y > 0$ such that both $x + ny$ and
> $x^2 + ny^2$ are prime.
>
> Zhi-Wei Sun has offered a \$200 prize for the first proof.
>
> *References:*
> - [A232174](https://oeis.org/A232174)
> - Z.-W. Sun, "Conjectures on representations involving primes," in: M. Nathanson (ed.),
>   Combinatorial and Additive Number Theory II: CANT, Springer Proc. in Math. & Stat.,
>   Vol. 220, Springer, 2017, pp. 279-310. https://arxiv.org/abs/1211.1588
> - D.A. Cox, "Primes of the Form x² + ny²," John Wiley & Sons, 1989.

*Quoted from [FormalConjectures/OEIS/232174.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/232174.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 6 test statements, counted here but not shown.

## `OeisA232174.conjecture`

Open: stated without proof.

> **Zhi-Wei Sun's Conjecture (A232174)**: Any integer $n > 1$ can be written as $x + y$ with
> $x, y > 0$ such that both $x + ny$ and $x^2 + ny^2$ are prime.

```lean
theorem conjecture (n : ℕ) (hn : 1 < n) : A n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/232174.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/232174.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/232174.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/232174.lean)
- [A232174](https://oeis.org/A232174)
