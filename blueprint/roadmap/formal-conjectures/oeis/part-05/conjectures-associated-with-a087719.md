---
declaration: theorem
origin: cited
lean: OeisA87719.a_exists, OeisA87719.a_formula
statement: formalized
---

# Conjectures associated with A087719

> Define $\varsigma(n)$ the smallest prime factor of $n$ (`Nat.minFac`). Let $a_n$ be the least
> number such that the count of numbers $k \le a_n$ with $k > \varsigma(k)^n$ exceeds the count
> of numbers with $k \le \varsigma(k)^n$.
>
> The conjecture states that $a_n = 3^n + 3 \cdot 2^n + 6$ for $n \ge 1$.
>
> *References:*
> - [A087719](https://oeis.org/A087719)

*Quoted from [FormalConjectures/OEIS/87719.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/87719.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 textbook results. It also has 3 test statements, counted here but not shown.

## `OeisA87719.a_exists`

Textbook result, proved here.

> There exists m such that countExceeding n m > countNotExceeding n m.

```lean
theorem a_exists (n : ℕ) : ∃ m, countExceeding n m > countNotExceeding n m
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/87719.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/87719.lean#L49).

## `OeisA87719.a_formula`

Textbook result, stated without proof. A Lean proof is at [https://github.com/google-deepmind/formal-conjectures/blob/7a286754f623759d69a3dd18f482c53c1d70959b/FormalConjectures/OEIS/87719.lean#L640](https://github.com/google-deepmind/formal-conjectures/blob/7a286754f623759d69a3dd18f482c53c1d70959b/FormalConjectures/OEIS/87719.lean#L640).

> We have the following formula: $a(n) = 3^n + 3 * 2^n + 6$ for $n \geq 1$.

```lean
theorem a_formula {n : ℕ} (hn : n ≥ 1) : a n = 3 ^ n + 3 * 2 ^ n + 6
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/87719.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/87719.lean#L120).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/87719.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/87719.lean)
- [A087719](https://oeis.org/A087719)
