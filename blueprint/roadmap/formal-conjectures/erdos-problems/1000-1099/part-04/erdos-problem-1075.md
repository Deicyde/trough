---
declaration: theorem
origin: cited
lean: Erdos1075.erdos_1075
statement: formalized
---

# Erdős Problem 1075

> *References:*
> - [erdosproblems.com/1075](https://www.erdosproblems.com/1075)
> - [Er64f] Erdős, P., On extremal problems of graphs and generalized graphs. Israel J. Math. (1964),
>   183--190.

*Quoted from [FormalConjectures/ErdosProblems/1075.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/1075.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1075](https://www.erdosproblems.com/1075).

The file states 1 research or textbook statement: 1 open.

## `Erdos1075.erdos_1075`

Open: stated without proof.

> Let $r\geq 3$. There exists $c_r>r^{-r}$ such that, for any $\epsilon>0$, if $n$ is sufficiently
> large, the following holds. Any $r$-uniform hypergraph on $n$ vertices with at least
> $(1+\epsilon)(n/r)^r$ many edges contains a subgraph on $m$ vertices with at least $c_rm^r$ edges,
> where $m=m(n)\to \infty$ as $n\to \infty$.

```lean
theorem erdos_1075 :
    ∀ r : ℕ, 3 ≤ r → ∃ c : ℝ, (r : ℝ)⁻¹ ^ r < c ∧
    ∀ ε : ℝ, 0 < ε → ∃ m : ℕ → ℕ, Tendsto m atTop atTop ∧
      ∀ᶠ n : ℕ in atTop, ∀ H : Finset (Finset (Fin n)),
        H.IsUniform r → (1 + ε) * ((n : ℝ) / r) ^ r ≤ H.card →
          ∃ S : Finset (Fin n), S.card = m n ∧
            c * (S.card : ℝ) ^ r ≤ (H.hypergraphInduce S).card
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1075.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/1075.lean#L42).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1075.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/1075.lean)
- [erdosproblems.com/1075](https://www.erdosproblems.com/1075)
