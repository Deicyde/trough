---
declaration: theorem
origin: cited
lean: Erdos1094.erdos_1094
statement: formalized
---

# Erdős Problem 1094

> *Reference:* [erdosproblems.com/1094](https://www.erdosproblems.com/1094)

*Quoted from [FormalConjectures/ErdosProblems/1094.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/1094.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1094](https://www.erdosproblems.com/1094).

The file states 1 research or textbook statement: 1 open.

## `Erdos1094.erdos_1094`

Open: stated without proof.

> For all $n\ge 2k$ the least prime factor of $\binom{n}{k}$ is $\le\max(n/k,k)$, with only
> finitely many exceptions.

```lean
theorem erdos_1094 :
    {(n, k) : ℕ × ℕ | 0 < k ∧ 2 * k ≤ n ∧ (n.choose k).minFac > max (n / k) k}.Finite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1094.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/1094.lean#L38).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1094.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/1094.lean)
- [erdosproblems.com/1094](https://www.erdosproblems.com/1094)
