---
declaration: theorem
origin: cited
lean: Erdos379.erdos_379
statement: formalized
---

# Erdős Problem 379

> *Reference:* [erdosproblems.com/379](https://www.erdosproblems.com/379)

*Quoted from [FormalConjectures/ErdosProblems/379.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/379.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/379](https://www.erdosproblems.com/379).

The file states 1 research or textbook statement: 1 solved.

## `Erdos379.erdos_379`

Solved: stated here; a Lean proof is at [https://github.com/teorth/analysis/blob/4f623b0f4cacdb967f1f8132db0becaee0f1fb3d/Analysis/Misc/erdos_379.lean#L90](https://github.com/teorth/analysis/blob/4f623b0f4cacdb967f1f8132db0becaee0f1fb3d/Analysis/Misc/erdos_379.lean#L90).

> Let $S(n)$ denote the largest integer such that, for all $1 ≤ k < n$, the binomial coefficient
> $\binom{n}{k}$ is divisible by $p^S(n)$ for some prime $p$ (depending on $k$).Then
> $\limsup S(n) = \infty$.
>
> This was formalized in Lean by Tao.

```lean
theorem erdos_379 : atTop.limsup (fun n => (S n : ℕ∞)) = ⊤
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/379.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/379.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/379.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/379.lean)
- [erdosproblems.com/379](https://www.erdosproblems.com/379)
