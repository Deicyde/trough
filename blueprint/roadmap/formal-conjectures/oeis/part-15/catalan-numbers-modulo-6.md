---
declaration: theorem
origin: cited
lean: OeisA259667.conjecture_1, OeisA259667.conjecture_2
statement: formalized
---

# Catalan numbers modulo $6$

> The sequence $a(n) = C_n \bmod 6$, where $C_n = \frac{1}{n+1} \binom{2n}{n}$ is the $n$-th
> Catalan number (A000108).
>
> *References:*
> - [A259667](https://oeis.org/A259667)

*Quoted from [FormalConjectures/OEIS/259667.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/259667.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA259667.conjecture_1`

Open: stated without proof.

> It is conjectured that the only $k$ which yield $a(2^k - 1) = 1$ are $k = 0, 1$ and $5$.

```lean
theorem conjecture_1 (k : ℕ) :
    a (2 ^ k - 1) = 1 ↔ k = 0 ∨ k = 1 ∨ k = 5
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/259667.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/259667.lean#L64).

## `OeisA259667.conjecture_2`

Open: stated without proof.

> Conjecture: The only $k$ which yield $a(2^k - 1) = 5$ are $k = 2, 8$.

```lean
theorem conjecture_2 (k : ℕ) :
    a (2 ^ k - 1) = 5 ↔ k = 2 ∨ k = 8
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/259667.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/259667.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/259667.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/259667.lean)
- [A259667](https://oeis.org/A259667)
