---
declaration: theorem
origin: cited
lean: Erdos458.erdos_458
statement: formalized
---

# Erdős Problem 458

> *Reference:* [erdosproblems.com/458](https://www.erdosproblems.com/458)

*Quoted from [FormalConjectures/ErdosProblems/458.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/458.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

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

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/458.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/458.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/458.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/458.lean)
- [erdosproblems.com/458](https://www.erdosproblems.com/458)
