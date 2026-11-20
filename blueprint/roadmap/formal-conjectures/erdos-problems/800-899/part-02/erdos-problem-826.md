---
declaration: theorem
origin: cited
lean: Erdos826.erdos_826
statement: formalized
---

# Erdős Problem 826

> *Reference:* [erdosproblems.com/826](https://www.erdosproblems.com/826)

*Quoted from [FormalConjectures/ErdosProblems/826.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/826.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/826](https://www.erdosproblems.com/826).

The file states 1 research or textbook statement: 1 open.

## `Erdos826.erdos_826`

Open: stated without proof.

> Are there infinitely many $n$ such that, for all $k\geq 1$
>
> $$
>   \tau(n + k) \ll k?
> $$

```lean
theorem erdos_826 :
    ∃ C > (0 : ℝ), { n | ∀ k ≥ 1, σ 0 (n + k) ≤ C * k }.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/826.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/826.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/826.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/826.lean)
- [erdosproblems.com/826](https://www.erdosproblems.com/826)
