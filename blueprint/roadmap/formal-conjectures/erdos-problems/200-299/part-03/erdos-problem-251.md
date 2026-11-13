---
declaration: theorem
origin: cited
lean: Erdos251.erdos_251
statement: formalized
---

# Erdős Problem 251

> *Reference:* [erdosproblems.com/251](https://www.erdosproblems.com/251)

*Quoted from [FormalConjectures/ErdosProblems/251.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/251.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/251](https://www.erdosproblems.com/251).

The file states 1 research or textbook statement: 1 open.

## `Erdos251.erdos_251`

Open: stated without proof.

> Is $\sum_{n=1}^\infty \frac{p_n}{2^n}$ irrational? Here $p_n$ is the $n$-th prime ($p_1=2, p_2=3, \dots$).

```lean
theorem erdos_251 : Irrational (∑' n : ℕ, (Nat.nth Nat.Prime n) / (2 ^ n))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/251.lean, line 34](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/251.lean#L34).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/251.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/251.lean)
- [erdosproblems.com/251](https://www.erdosproblems.com/251)
