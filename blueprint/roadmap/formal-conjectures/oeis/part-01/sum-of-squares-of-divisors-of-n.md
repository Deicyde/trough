---
declaration: theorem
origin: cited
lean: OeisA1157.conjecture
statement: formalized
---

# Sum of squares of divisors of $n$

> *References:*
> - [A001157](https://oeis.org/A001157)

*Quoted from [FormalConjectures/OEIS/1157.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/1157.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA1157.conjecture`

Open: stated without proof.

> Conjecture: For each k = 2,3,..., all the rational numbers
> $\frac{\sigma_k(n)}{n^k} = \sum_{d|n} \frac{1}{d^k}$ (n = 1,2,3,...) have pairwise distinct
> fractional parts. - Zhi-Wei Sun, Oct 15 2015

```lean
theorem conjecture :
  ∀ k : ℕ, 2 ≤ k →
    ∀ n₁ n₂ : ℕ, 0 < n₁ → 0 < n₂ → n₁ ≠ n₂ →
      Int.fract (↑((sigma k) n₁) / (↑n₁ ^ k : ℚ)) ≠
        Int.fract (↑((sigma k) n₂) / (↑n₂ ^ k : ℚ))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/1157.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/1157.lean#L58).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/1157.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/1157.lean)
- [A001157](https://oeis.org/A001157)
