---
declaration: theorem
origin: cited
lean: Erdos48.erdos_48
statement: formalized
---

# Erdős Problem 48

> *Reference:* [erdosproblems.com/48](https://www.erdosproblems.com/48)

*Quoted from [FormalConjectures/ErdosProblems/48.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/48.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/48](https://www.erdosproblems.com/48).

The file states 1 research or textbook statement: 1 solved.

## `Erdos48.erdos_48`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos48.lean#L599](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos48.lean#L599).

> Are there infinitely many integers $n, m$ such that $ϕ(n) = σ(m)$?

```lean
theorem erdos_48 :
    {(n, m) : ℕ × ℕ | n.totient = σ 1 m}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/48.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/48.lean#L38).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/48.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/48.lean)
- [erdosproblems.com/48](https://www.erdosproblems.com/48)
