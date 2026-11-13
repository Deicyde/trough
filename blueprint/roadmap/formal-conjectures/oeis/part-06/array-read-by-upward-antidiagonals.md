---
declaration: theorem
origin: cited
lean: OeisA105020.conjecture
statement: formalized
---

# Array read by upward antidiagonals

> Array read by upward antidiagonals: row $n$ ($n \ge 0$) contains the numbers
> $m^2 - n^2$, $m \ge n+1$.
>
> *References:*
> - [A105020](https://oeis.org/A105020)

*Quoted from [FormalConjectures/OEIS/105020.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/105020.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA105020.conjecture`

Open: stated without proof.

> A "Goldbach Conjecture" for this sequence: when there are $n$ terms between consecutive odd
> integers $2n+1$ and $2n+3$ for $n > 0$, at least one will be the product of 2 primes
> (not necessarily distinct). Example: $n=3$ for consecutive odd integers $a(7) = 7$ and
> $a(11) = 9$ and of the 3 sequence entries $a(8) = 12$, $a(9) = 15$ and $a(10) = 16$ between
> them, one is the product of 2 primes $a(9) = 15=3*5$. - _Michael Hiebl_, Jul 15 2007

```lean
theorem conjecture :
  ∀ (n i j : ℕ), 1 ≤ n →
    a i = 2 * n + 1 →
    a j = 2 * n + 3 →
    j = i + n + 1 →
    ∃ (k : ℕ),
      i < k ∧
      k < j ∧
      (a k).IsSemiprime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/105020.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/105020.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/105020.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/105020.lean)
- [A105020](https://oeis.org/A105020)
