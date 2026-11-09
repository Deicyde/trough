---
declaration: theorem
origin: cited
lean: Erdos312.erdos_312
statement: formalized
---

# Erdős Problem 312

> *Reference:* [erdosproblems.com/312](https://www.erdosproblems.com/312)

*Quoted from [FormalConjectures/ErdosProblems/312.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/312.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/312](https://www.erdosproblems.com/312).

The file states 1 research or textbook statement: 1 open.

## `Erdos312.erdos_312`

Open: stated without proof.

> Does there exist a constant `c > 0` such that, for any `K > 1`, whenever `A` is a sufficiently large
> finite multiset of integers with $\sum_{n \in A} 1/n > K$ there exists some $S \subseteq A$ such that
> $1 - \exp(-(c*K)) < \sum_{n \in S} 1/n \le 1$?

```lean
theorem erdos_312 :
    ∃ (c : ℝ), 0 < c ∧
      ∀ (K : ℝ), 1 < K →
        ∃ (N₀ : ℕ),
          ∀ (n : ℕ) (a : Fin n → ℕ),
            (n ≥ N₀ ∧ (∑ i : Fin n, (a i : ℝ)⁻¹) > K) →
              ∃ (S : Finset (Fin n)),
                1 - Real.exp (-(c * K)) < (∑ i ∈ S, (a i : ℝ)⁻¹) ∧
                ∑ i ∈ S, (a i : ℝ)⁻¹ ≤ 1
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/312.lean, line 36](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/312.lean#L36).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/312.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/312.lean)
- [erdosproblems.com/312](https://www.erdosproblems.com/312)
