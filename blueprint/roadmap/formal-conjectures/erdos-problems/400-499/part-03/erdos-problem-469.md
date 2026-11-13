---
declaration: theorem
origin: cited
lean: Erdos469.erdos_469
statement: formalized
---

# Erdős Problem 469

> *References:*
> - [erdosproblems.com/469](https://www.erdosproblems.com/469)
> - [Le25] Lewis, Z. J., *On the convergence of the reciprocal sum of primitive pseudoperfect
>   numbers*. Preprint (2025).

*Quoted from [FormalConjectures/ErdosProblems/469.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/469.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/469](https://www.erdosproblems.com/469).

The file states 1 research or textbook statement: 1 solved.

## `Erdos469.erdos_469`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos469.lean](https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos469.lean).

> Let $A$ be the set of all $n$ such that $n = d_1 + ⋯ + d_k$ with $d_i$ distinct
> proper divisors of $n$, but this is not true for any $m ∣ n$ with $m < n$. Does:
>
> $$
>   \sum_{n ∈ A} \frac 1 n
> $$
>
> converge?
>
> Yes: the sum converges. This was proved by Lewis [Le25], whose proof has been formalized in
> Lean.

```lean
theorem erdos_469 :
    letI A := {n : ℕ | 0 < n ∧ n.IsSumDivisors ∧ ∀ m < n, m ∣ n → ¬ m.IsSumDivisors}
    Summable fun n : A ↦ 1 / (n : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/469.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/469.lean#L52).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/469.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/469.lean)
- [erdosproblems.com/469](https://www.erdosproblems.com/469)
