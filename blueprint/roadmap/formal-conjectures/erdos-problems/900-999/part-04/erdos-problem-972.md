---
declaration: theorem
origin: cited
lean: Erdos972.erdos_972
statement: formalized
---

# Erdős Problem 972

> *Reference:* [erdosproblems.com/972](https://www.erdosproblems.com/972)

*Quoted from [FormalConjectures/ErdosProblems/972.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/972.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/972](https://www.erdosproblems.com/972).

The file states 1 research or textbook statement: 1 open.

## `Erdos972.erdos_972`

Open: stated without proof.

> **Erdős problem 972.**
> Let $\alpha > 1$ be irrational. Are there infinitely many primes $p$
> such that $\lfloor p\alpha \rfloor$ is also prime?

```lean
theorem erdos_972 : ∀ α > 1, Irrational α → (primeSet α).Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/972.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/972.lean#L42).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/972.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/972.lean)
- [erdosproblems.com/972](https://www.erdosproblems.com/972)
