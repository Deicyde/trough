---
declaration: theorem
origin: cited
lean: OeisA176477.conjecture1, OeisA176477.conjecture2
statement: formalized
---

# Recurrence with fourth powers of binomial coefficients

> The sequence is defined by $a(1) = 2$, and for $n \ge 2$,
>
> $$(2n+1)^3 a(n) = 32n^3 a(n-1) + (21n^3 + 22n^2 + 8n + 1) \binom{2n-1}{n}^4.$$
>
> *References:*
> - [A176477](https://oeis.org/A176477)
> - Z.-W. Sun, "Open Conjectures on Congruences", arXiv preprint
>   [arXiv:0911.5665](https://arxiv.org/abs/0911.5665) [math.NT], 2009-2011.
> - T. Adamczewski, "OEIS Open: How many conjectures can language models turn into theorems?",
>   [arXiv:2608.11941](https://arxiv.org/abs/2608.11941) [cs.AI], 2026.

*Quoted from [FormalConjectures/OEIS/176477.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/176477.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved. It also has 2 test statements, counted here but not shown.

## `OeisA176477.conjecture1`

Solved: stated here; a Lean proof is at [https://github.com/epoch-research/LeanOpenProblems-results/blob/fd09021e79869476ef83cda231312f1a2a89c8d7/runs/oeis-open-lite-gpt6astra-37ly1phzfwj2ech4/oeis_a176477_conjecture/Submission/Spec.lean#L58383](https://github.com/epoch-research/LeanOpenProblems-results/blob/fd09021e79869476ef83cda231312f1a2a89c8d7/runs/oeis-open-lite-gpt6astra-37ly1phzfwj2ech4/oeis_a176477_conjecture/Submission/Spec.lean#L58383).

> Each term $a(n)$ is a positive integer.
> - _Zhi-Wei Sun_, Apr 06 2010
>
> Proved in the OEIS Open project, see T. Adamczewski, OEIS Open: How many conjectures can
> language models turn into theorems?, [arXiv:2608.11941](https://arxiv.org/abs/2608.11941).

```lean
theorem conjecture1 (n : ℕ) (hn : 1 ≤ n) : (a n).den = 1 ∧ 0 < a n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/176477.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/176477.lean#L68).

## `OeisA176477.conjecture2`

Solved: stated here; a Lean proof is at [https://github.com/epoch-research/LeanOpenProblems-results/blob/fd09021e79869476ef83cda231312f1a2a89c8d7/runs/oeis-open-lite-gpt6astra-37ly1phzfwj2ech4/oeis_a176477_conjecture/Submission/Spec.lean#L58383](https://github.com/epoch-research/LeanOpenProblems-results/blob/fd09021e79869476ef83cda231312f1a2a89c8d7/runs/oeis-open-lite-gpt6astra-37ly1phzfwj2ech4/oeis_a176477_conjecture/Submission/Spec.lean#L58383).

> $a(n)$ is odd if and only if $n = 2, 2^2, 2^3, \dots$.
> - _Zhi-Wei Sun_, Apr 06 2010
>
> Proved in the OEIS Open project, see T. Adamczewski, OEIS Open: How many conjectures can
> language models turn into theorems?, [arXiv:2608.11941](https://arxiv.org/abs/2608.11941).

```lean
theorem conjecture2 (n : ℕ) (hn : 1 ≤ n) :
    ((a n).den = 1 ∧ Odd (a n).num) ↔ ∃ m : ℕ, 1 ≤ m ∧ n = 2 ^ m
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/176477.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/176477.lean#L81).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/176477.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/176477.lean)
- [A176477](https://oeis.org/A176477)
