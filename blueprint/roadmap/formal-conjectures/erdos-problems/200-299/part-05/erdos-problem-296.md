---
declaration: theorem
origin: cited
lean: Erdos296.erdos_296
statement: formalized
---

# Erdős Problem 296

> *References:*
> - [erdosproblems.com/296](https://www.erdosproblems.com/296)
> - [Bl21] Bloom, T. F., *On a density conjecture about unit fractions*.
>   arXiv:2112.03726 (2021).

*Quoted from [FormalConjectures/ErdosProblems/296.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/296.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/296](https://www.erdosproblems.com/296).

The file states 1 research or textbook statement: 1 solved.

## `Erdos296.erdos_296`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos296.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos296.lean).

> Let $N\geq 1$ and let $k(N)$ be maximal such that there are $k$ disjoint $A_1,\ldots,A_k\subseteq \{1,\ldots,N\}$ with $\sum_{n\in A_i}\frac{1}{n}=1$ for all $i$. Estimate $k(N)$. Is it true that $k(N)=o(\log N)$?
>
> Hunter and Sawhney observed that Bloom's theorem [Bl21], together with the greedy
> argument, gives $k(N)=(1-o(1))\log N$.

```lean
theorem erdos_296 :
    (∀ N k : ℕ, HasDisjointUnitDecomps N k → (k : ℚ) ≤ recipSum (Finset.Icc 1 N)) ∧
      (∀ ε : ℝ, 0 < ε → ε < 1 → ∀ᶠ N : ℕ in atTop,
        HasDisjointUnitDecomps N ⌊(1 - ε) * Real.log N⌋₊)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/296.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/296.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/296.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/296.lean)
- [erdosproblems.com/296](https://www.erdosproblems.com/296)
