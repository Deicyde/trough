---
declaration: theorem
origin: cited
lean: Erdos1059.erdos_1059
statement: formalized
---

# Erdős Problem 1059

> *Reference:* [erdosproblems.com/1059](https://www.erdosproblems.com/1059)

*Quoted from [FormalConjectures/ErdosProblems/1059.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1059.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1059](https://www.erdosproblems.com/1059).

The file states 1 research or textbook statement: 1 open. It also has 7 test statements, counted here but not shown.

## `Erdos1059.erdos_1059`

Open: stated without proof.

> Are there infinitely many primes $p$ such that $p - k!$ is composite for each $k$ such that $1 ≤ k! < p$?

```lean
theorem erdos_1059 :
    Set.Infinite {p | p.Prime ∧ AllFactorialSubtractionsComposite p}
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1059.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1059.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1059.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1059.lean)
- [erdosproblems.com/1059](https://www.erdosproblems.com/1059)
