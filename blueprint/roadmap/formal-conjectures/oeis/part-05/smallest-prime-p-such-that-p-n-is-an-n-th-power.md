---
declaration: theorem
origin: cited
lean: OeisA84046.conjecture
statement: formalized
---

# Smallest prime $p$ such that $p + n$ is an $n$-th power

> Smallest prime $p$ such that $p + n$ is an $n$-th power, or $0$ if no such number exists.
> That is, the smallest prime of the form $k^n - n$.
>
> *References:*
> - [A084046](https://oeis.org/A084046)

*Quoted from [FormalConjectures/OEIS/84046.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/84046.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 4 test statements, counted here but not shown.

## `OeisA84046.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-full-50usd-oai-jajpvieznaevpoyg/a084046_conjecture_0/Submission/Spec.lean#L17](https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-full-50usd-oai-jajpvieznaevpoyg/a084046_conjecture_0/Submission/Spec.lean#L17).

> Conjecture: if a(k) = 0 then k is an even square.
>
> This is false for $k = 27$. Every candidate $x^{27} - 27$ factors as
> $(x^9 - 3)(x^{18} + 3x^9 + 9)$, so $a(27) = 0$, but $27$ is not an even square.

```lean
theorem conjecture : ¬ ∀ k : ℕ, a k = 0 → ∃ m : ℕ, k = (2 * m) ^ 2
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/84046.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/84046.lean#L112).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/84046.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/84046.lean)
- [A084046](https://oeis.org/A084046)
