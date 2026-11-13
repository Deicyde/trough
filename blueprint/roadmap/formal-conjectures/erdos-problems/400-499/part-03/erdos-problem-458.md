---
declaration: theorem
origin: cited
lean: Erdos458.erdos_458
statement: formalized
---

# Erdős Problem 458

> *Reference:* [erdosproblems.com/458](https://www.erdosproblems.com/458)

*Quoted from [FormalConjectures/ErdosProblems/458.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/458.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/458](https://www.erdosproblems.com/458).

The file states 1 research or textbook statement: 1 open.

## `Erdos458.erdos_458`

Open: stated without proof.

> Let $\operatorname{lcm}(1, \dots, n)$ denote the least common multiple of $\{1, \dots, n\}$.
> Let $p_k$ be the $k$-th prime.
> Is it true that for all $k \geq 1$, $\operatorname{lcm}(1, \dots, p_{k+1}-1) < p_k \cdot \operatorname{lcm}(1, \dots, p_k)$?

```lean
theorem erdos_458 :
    ∀ k : ℕ, lcm_upto ((k + 1).nth Prime - 1)
     < k.nth Prime * lcm_upto (k.nth Prime)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/458.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/458.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/458.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/458.lean)
- [erdosproblems.com/458](https://www.erdosproblems.com/458)
