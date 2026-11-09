---
declaration: theorem
origin: cited
lean: OeisA189286.conjecture_1, OeisA189286.conjecture_2, OeisA189286.conjecture_3
statement: formalized
---

# Normalized convolution of $\binom{6k}{3k}\binom{3k}{k}$

> The sequence $a(n)$ is defined by
> $$a(n) = \frac{\sum_{k=0}^n \binom{6k}{3k}\binom{3k}{k}
>   \binom{6(n-k)}{3(n-k)}\binom{3(n-k)}{n-k}}{(2n-1)\binom{3n}{n}}.$$
>
> *References:*
> - [A189286](https://oeis.org/A189286)
> - T. Adamczewski, "OEIS Open: How many conjectures can language models turn into theorems?",
>   [arXiv:2608.11941](https://arxiv.org/abs/2608.11941) [cs.AI], 2026.

*Quoted from [FormalConjectures/OEIS/189286.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/189286.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open, 1 solved and 1 textbook result. It also has 5 test statements, counted here but not shown.

## `OeisA189286.conjecture_1`

Solved: stated here without proof.

> Conjecture: $a(n)$ is an integer for every $n = 0, 1, 2, \dots$.
> - _Zhi-Wei Sun_, Apr 19 2011
>
> Proved in the OEIS Open project, see T. Adamczewski, OEIS Open: How many conjectures can
> language models turn into theorems?, [arXiv:2608.11941](https://arxiv.org/abs/2608.11941).

```lean
theorem conjecture_1 (n : ℕ) : (a n).den = 1
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/189286.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/189286.lean#L72).

## `OeisA189286.conjecture_2`

Textbook result, stated without proof.

> Conjecture (i): $a(n)^{1/n}$ tends to $64$ as $n$ tends to infinity.
> - _Zhi-Wei Sun_, Apr 19 2011

```lean
theorem conjecture_2 :
    Filter.Tendsto (fun n : ℕ => (a n : ℝ) ^ (1 / (n : ℝ))) Filter.atTop (nhds 64)
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/189286.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/189286.lean#L80).

## `OeisA189286.conjecture_3`

Open: stated without proof.

> Conjecture (ii): For any positive integer $n$, we have $a(n) \equiv 0 \pmod 8$,
> and $a(n)/8$ is odd if and only if $n$ is a power of two.
> - _Zhi-Wei Sun_, Apr 19 2011

```lean
theorem conjecture_3 (n : ℕ) (hn : 0 < n) :
    ∃ m : ℤ, a n = 8 * m ∧ (Odd m ↔ ∃ k : ℕ, n = 2 ^ k)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/189286.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/189286.lean#L90).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/189286.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/189286.lean)
- [A189286](https://oeis.org/A189286)
