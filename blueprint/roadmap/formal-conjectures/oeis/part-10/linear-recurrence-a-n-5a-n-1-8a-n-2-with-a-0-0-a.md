---
declaration: theorem
origin: cited
lean: OeisA190969.conjecture_1, OeisA190969.conjecture_2
statement: formalized
---

# Linear recurrence $a(n) = 5a(n-1) - 8a(n-2)$ with $a(0)=0, a(1)=1$

> The sequence $a(n)$ satisfies the linear recurrence relation $a(n) = 5a(n-1) - 8a(n-2)$
> with initial values $a(0) = 0$ and $a(1) = 1$.
>
> *References:*
> - [A190969](https://oeis.org/A190969)
> - [Conjectures involving primes and quadratic forms](https://arxiv.org/abs/1211.1588)
>   by *Zhi-Wei Sun*, arXiv:1211.1588 (2012)

*Quoted from [FormalConjectures/OEIS/190969.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/190969.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA190969.conjecture_1`

Open: stated without proof.

> Conjecture: Let $S(p) := \sum_{k=0}^{p-1} a(4k) \binom{2k}{k}^3 / (-4096)^k$.
> Then $S(p) \equiv 0 \pmod{p^2}$ for every odd prime $p$.
> - _Zhi-Wei Sun_, Mar 13 2013

```lean
theorem conjecture_1 (p : ℕ) (hp : p.Prime) (hp2 : p ≠ 2) :
    sMod p 2 = 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/190969.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/190969.lean#L74).

## `OeisA190969.conjecture_2`

Open: stated without proof.

> Conjecture: Let $S(p) := \sum_{k=0}^{p-1} a(4k) \binom{2k}{k}^3 / (-4096)^k$.
> Then $S(p) \equiv 0 \pmod{p^3}$ for any odd prime $p \equiv 1, 2, 4 \pmod 7$.
> - _Zhi-Wei Sun_, Mar 13 2013

```lean
theorem conjecture_2 (p : ℕ) (hp : p.Prime) (hp2 : p ≠ 2)
    (h7 : p % 7 ∈ ({1, 2, 4} : Finset ℕ)) :
    sMod p 3 = 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/190969.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/190969.lean#L84).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/190969.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/190969.lean)
- [A190969](https://oeis.org/A190969)
