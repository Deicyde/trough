---
declaration: theorem
origin: cited
lean: Erdos66.erdos_66
statement: formalized
---

# Erdős Problem 66

> *Reference:* [erdosproblems.com/66](https://www.erdosproblems.com/66)

*Quoted from [FormalConjectures/ErdosProblems/66.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/66.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/66](https://www.erdosproblems.com/66).

The file states 1 research or textbook statement: 1 open.

## `Erdos66.erdos_66`

Open: stated without proof.

> Is there and $A \subset \mathbb{N}$ is such that
>
> $$\lim_{n\to \infty}\frac{1_A\ast 1_A(n)}{\log n}$$
>
> exists and is $\ne 0$?

```lean
theorem erdos_66 : ∃ (A : Set ℕ) (c : ℝ), c ≠ 0 ∧
    Tendsto (fun n ↦ (sumRep A n : ℝ) / Real.log n) atTop (𝓝 c)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/66.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/66.lean#L40).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/66.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/66.lean)
- [erdosproblems.com/66](https://www.erdosproblems.com/66)
