---
declaration: theorem
origin: cited
lean: Erdos450.erdos_450, Erdos450.erdos_450.linear_scale_suffices
statement: formalized
---

# Erdős Problem 450

> *Reference:* [erdosproblems.com/450](https://www.erdosproblems.com/450)

*Quoted from [FormalConjectures/ErdosProblems/450.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/450.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/450](https://www.erdosproblems.com/450).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos450.erdos_450`

Open: stated without proof.

> How large must $y=y(\epsilon,n)$ be such that the number of integers in
> $(x,x+y)$ with a divisor in $(n,2n)$ is at most $\epsilon y$?
>
> The bound is required for every $x$ and every window length at least $y$, and
> $y(\epsilon,n)$ is the least such threshold (or $\infty$ if there is none).
> A **linear** scale $y \le C(\epsilon) n$ is known to suffice for fixed $\epsilon$
> and all large $n$ (see `erdos_450.linear_scale_suffices`).

```lean
theorem erdos_450 (ε : ℝ) (hε : 0 < ε) (n : ℕ) : windowThreshold ε n = erdos_450.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/450.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/450.lean#L64).

## `Erdos450.erdos_450.linear_scale_suffices`

Solved: stated here; a Lean proof is at [https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-450/Research/TuranAnswer.lean](https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-450/Research/TuranAnswer.lean).

> A translate-uniform **linear** scale suffices: there is a sufficient window
> length `Y` with `Y ε n ≤ C(ε) · n`. This is an upper bound on the optimal scale,
> not the exact threshold asked for in `erdos_450`.

```lean
theorem erdos_450.linear_scale_suffices :
    ∃ Y : ℝ → ℕ → ℕ,
      (∀ ε : ℝ, 0 < ε → ∃ C : ℝ, ∀ n : ℕ, (Y ε n : ℝ) ≤ C * n) ∧ IsSufficientScale Y
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/450.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/450.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/450.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/450.lean)
- [erdosproblems.com/450](https://www.erdosproblems.com/450)
