---
declaration: theorem
origin: cited
lean: Erdos537.erdos_537
statement: formalized
---

# Erdős Problem 537

> *References:*
> - [erdosproblems.com/537](https://www.erdosproblems.com/537)
> - [Er73] Erdős, P., *Problems and results on combinatorial number theory*. A survey of combinatorial
>   theory (Proc. Internat. Sympos., Colorado State Univ., Fort Collins, Colo., 1971) (1973), 117-138.

*Quoted from [FormalConjectures/ErdosProblems/537.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/537.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/537](https://www.erdosproblems.com/537).

The file states 1 research or textbook statement: 1 solved.

## `Erdos537.erdos_537`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos537.lean](https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos537.lean).

> Let $\epsilon>0$ and $N$ be sufficiently large. If $A\subseteq \{1,\ldots,N\}$ has
> $\lvert A\rvert \geq \epsilon N$ then must there exist $a_1,a_2,a_3\in A$ and distinct primes
> $p_1,p_2,p_3$ such that
> $$a_1p_1=a_2p_2=a_3p_3?$$
>
> A positive answer would imply [536].
>
> Erdős describes a construction of Ruzsa which disproves this: consider the set of all
> squarefree numbers of the shape $p_1\cdots p_r$ where $p_{i+1}>2p_i$ for $1\leq i\lt r$. This
> set has positive density, and hence if $A$ is its intersection with $(N/2,N)$ then
> $\lvert A\rvert \gg N$ for all large $N$. Suppose now that $p_1a_1=p_2a_2=p_3a_3$ where
> $a_i\in A$ and $p_1,p_2,p_3$ are distinct primes. Without loss of generality we may assume
> that $a_2>a_3$ and hence $p_2\lt p_3$, and so since $p_2p_3\mid a_1\in A$ we must have
> $2\lt p_3/p_2$. On the other hand $p_3/p_2=a_2/a_3\in (1,2)$, a contradiction.

```lean
theorem erdos_537 :
    ¬ ∀ ε : ℝ, 0 < ε → ∀ᶠ N : ℕ in atTop,
      ∀ A ⊆ Finset.Icc 1 N, (A.card : ℝ) ≥ ε * N →
        ∃ a₁ ∈ A, ∃ a₂ ∈ A, ∃ a₃ ∈ A, ∃ p₁ p₂ p₃ : ℕ,
          p₁.Prime ∧ p₂.Prime ∧ p₃.Prime ∧
          p₁ ≠ p₂ ∧ p₁ ≠ p₃ ∧ p₂ ≠ p₃ ∧
          a₁ * p₁ = a₂ * p₂ ∧ a₂ * p₂ = a₃ * p₃
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/537.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/537.lean#L53).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/537.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/537.lean)
- [erdosproblems.com/537](https://www.erdosproblems.com/537)
