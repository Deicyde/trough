---
declaration: theorem
origin: cited
lean: OeisA86766.conjecture1, OeisA86766.conjecture2, OeisA86766.conjecture3
statement: formalized
---

# Smallest $r$ such that (concatenation of $n$, $r$ times) $\cdot 10 + 1$ is prime

> $a(n)$ is the smallest $r$ where (concatenation of $n$, $r$ times with itself) $\cdot 10 + 1$
> is a prime, or $0$ if no such number exists.
> The number resulting from concatenating $n$, $r$ times, is
> $n \cdot \sum_{i=0}^{r-1} (10^d)^i$, where $d$ is the number of digits of $n$.
>
> *References:*
> - [A086766](https://oeis.org/A086766)

*Quoted from [FormalConjectures/OEIS/86766.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/86766.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 open. It also has 5 test statements, counted here but not shown.

## `OeisA86766.conjecture1`

Open: stated without proof.

> What is the smallest integer $m > 1$ such that $a(10^m)$ is nonzero?
> - _Farideh Firoozbakht_, Jan 07 2015

```lean
theorem conjecture1 :
    conjecture1.answer =
      if h : ∃ m, 1 < m ∧ a (10 ^ m) ≠ 0 then
        some (sInf {m | 1 < m ∧ a (10 ^ m) ≠ 0})
      else
        none
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/86766.lean, line 149](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/86766.lean#L149).

## `OeisA86766.conjecture2`

Open: stated without proof.

> Conjecture: If $n$ is not of the form $10^m$ then $a(n)$ is nonzero.
> - _Farideh Firoozbakht_, Jan 07 2015

```lean
theorem conjecture2 (n : ℕ) (hn : 0 < n) (h : ∀ m : ℕ, n ≠ 10 ^ m) : a n ≠ 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/86766.lean, line 163](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/86766.lean#L163).

## `OeisA86766.conjecture3`

Open: stated without proof.

> What is the smallest odd prime $p$ such that $(10^{p^2}-1)/(10^p-1)$ is a prime number
> (and $a(10^{p-1})$ could be nonzero)?
> - _Farideh Firoozbakht_, Jan 07 2015

```lean
theorem conjecture3 :
    conjecture3.answer =
      if h : ∃ p, p.Prime ∧ 2 < p ∧ ((10 ^ (p ^ 2) - 1) / (10 ^ p - 1)).Prime then
        some (sInf {p | p.Prime ∧ 2 < p ∧ ((10 ^ (p ^ 2) - 1) / (10 ^ p - 1)).Prime})
      else
        none
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/86766.lean, line 175](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/86766.lean#L175).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/86766.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/86766.lean)
- [A086766](https://oeis.org/A086766)
