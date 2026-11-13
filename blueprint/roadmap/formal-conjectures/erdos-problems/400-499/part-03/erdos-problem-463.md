---
declaration: theorem
origin: cited
lean: Erdos463.erdos_463
statement: formalized
---

# Erdős Problem 463

> *Reference:* [erdosproblems.com/463](https://www.erdosproblems.com/463)

*Quoted from [FormalConjectures/ErdosProblems/463.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/463.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/463](https://www.erdosproblems.com/463).

The file states 1 research or textbook statement: 1 open.

## `Erdos463.erdos_463`

Open: stated without proof.

> Is there a function $f$ with $f(n)\to\infty$ as $n\to\infty$ such that,
> for all large $n$, there is a composite number $m$ such that
>
> $$
> n + f(n) < m < n + p(m)
> $$
>
> Here $p(m)$ is the least prime factor of $m$.

```lean
theorem erdos_463 : ∃ (f : ℕ → ℕ) (_ : Tendsto f atTop atTop),
    ∀ᶠ n in atTop,
      ∃ m, m.Composite ∧
        n + f n < m ∧ m < n + m.minFac
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/463.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/463.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/463.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/463.lean)
- [erdosproblems.com/463](https://www.erdosproblems.com/463)
