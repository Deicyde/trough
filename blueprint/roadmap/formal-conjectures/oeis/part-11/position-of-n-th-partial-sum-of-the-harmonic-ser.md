---
declaration: theorem
origin: cited
lean: OeisA206911.conjecture_1, OeisA206911.conjecture_2
statement: formalized
---

# Position of $n$-th partial sum of the harmonic series when jointly ranked with $\{\log(k+1)\}$

> Position of $n$-th partial sum of the harmonic series when all the partial sums are jointly ranked
> with the set $\{\log(k+1)\}$; complement of A206912.
>
> *References:*
> - [A206911](https://oeis.org/A206911)
> - T. Adamczewski, "OEIS Open: How many conjectures can language models turn into theorems?",
>   [arXiv:2608.11941](https://arxiv.org/abs/2608.11941) [cs.AI], 2026.

*Quoted from [FormalConjectures/OEIS/206911.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/206911.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved. It also has 5 test statements, counted here but not shown.

## `OeisA206911.conjecture_1`

Solved: stated here without proof.

> "Conjecture: the difference sequence of A206911 consists of $2$s and $3$s."
> - _Clark Kimberling_, Feb 13 2012
>
> Proved in the OEIS Open project, see T. Adamczewski, OEIS Open: How many conjectures can
> language models turn into theorems?, [arXiv:2608.11941](https://arxiv.org/abs/2608.11941).

```lean
theorem conjecture_1 (n : ℕ) (hn : 1 ≤ n) : diff n = 2 ∨ diff n = 3
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/206911.lean, line 179](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/206911.lean#L179).

## `OeisA206911.conjecture_2`

Solved: stated here without proof.

> "Conjecture: the ratio (number of $3$s)/(number of $2$s) tends to a number between $3.5$ and $3.6$."
> - _Clark Kimberling_, Feb 13 2012
>
> Proved in the OEIS Open project, see T. Adamczewski, OEIS Open: How many conjectures can
> language models turn into theorems?, [arXiv:2608.11941](https://arxiv.org/abs/2608.11941).

```lean
theorem conjecture_2 :
    ∃ l : ℝ, 3.5 < l ∧ l < 3.6 ∧
      Filter.Tendsto (fun N : ℕ => (count3 N : ℝ) / (count2 N : ℝ)) Filter.atTop (nhds l)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/206911.lean, line 190](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/206911.lean#L190).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/206911.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/206911.lean)
- [A206911](https://oeis.org/A206911)
