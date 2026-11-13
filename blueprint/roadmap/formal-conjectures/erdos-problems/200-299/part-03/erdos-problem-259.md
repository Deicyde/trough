---
declaration: theorem
origin: cited
lean: Erdos259.erdos_259
statement: formalized
---

# Erdős Problem 259

> *Reference:* [erdosproblems.com/259](https://www.erdosproblems.com/259)

*Quoted from [FormalConjectures/ErdosProblems/259.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/259.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/259](https://www.erdosproblems.com/259).

The file states 1 research or textbook statement: 1 solved.

## `Erdos259.erdos_259`

Solved: stated here; a Lean proof is at [https://gist.githubusercontent.com/ster-oc/c7429943f6b3a634797dc8b2a3b01f2d/raw/8c6b5b7f08021f0aed2312542dd2e9ee7beaa6d6/Erdos259.lean](https://gist.githubusercontent.com/ster-oc/c7429943f6b3a634797dc8b2a3b01f2d/raw/8c6b5b7f08021f0aed2312542dd2e9ee7beaa6d6/Erdos259.lean).

> Is $\sum_{n} \mu(n)^2\frac{n}{2^n}$ irrational?
>
> This is true, and was proved by Chen and Ruzsa.
>
> [ChRu99] Chen, Yong-Gao and Ruzsa, Imre Z., On the irrationality of certain series. Period. Math. Hungar. (1999), 31--37.

```lean
theorem erdos_259 : Irrational (∑' n : ℕ, (μ n) ^ 2 * n / (2 ^ n))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/259.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/259.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/259.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/259.lean)
- [erdosproblems.com/259](https://www.erdosproblems.com/259)
