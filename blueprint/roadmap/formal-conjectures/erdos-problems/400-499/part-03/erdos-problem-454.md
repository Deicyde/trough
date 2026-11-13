---
declaration: theorem
origin: cited
lean: Erdos454.erdos_454, Erdos454.erdos_454.variants.two_le_limsup
statement: formalized
---

# Erdős Problem 454

> *References:*
>  - [erdosproblems.com/454](https://www.erdosproblems.com/454)
>  - [Po79] Pomerance, Carl, The prime number graph. Math. Comp. (1979), 399-408.

*Quoted from [FormalConjectures/ErdosProblems/454.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/454.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/454](https://www.erdosproblems.com/454).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos454.erdos_454`

Open: stated without proof.

> Is it true that `limsup (fun n => (f n - 2 * n.nth Prime : ℕ∞)) atTop = ⊤`?

```lean
theorem erdos_454 : limsup (fun n => (f n - 2 * n.nth Prime : ℕ∞)) atTop = ⊤
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/454.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/454.lean#L40).

## `Erdos454.erdos_454.variants.two_le_limsup`

Solved: stated here without proof.

> `limsup (fun n => (f n - 2 * n.nth Prime : ℕ∞)) atTop ≥ 2`, and this is proved in [Po79].

```lean
theorem erdos_454.variants.two_le_limsup : 2 ≤ limsup (fun n => (f n - 2 * n.nth Prime : ℕ∞)) atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/454.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/454.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/454.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/454.lean)
- [erdosproblems.com/454](https://www.erdosproblems.com/454)
