---
declaration: theorem
origin: cited
lean: Erdos134.erdos_134
statement: formalized
---

# Erdős Problem 134

> *References:*
> - [erdosproblems.com/134](https://www.erdosproblems.com/134)
> - [Er97b] Erdős, Paul, *Some old and new problems in various branches of combinatorics*. Discrete Math. (1997), 227-231.

*Quoted from [FormalConjectures/ErdosProblems/134.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/134.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/134](https://www.erdosproblems.com/134).

The file states 1 research or textbook statement: 1 solved.

## `Erdos134.erdos_134`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos134.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos134.lean).

> Let $\epsilon,\delta>0$ and $n$ be sufficiently large in terms of $\epsilon$ and $\delta$.
> Let $G$ be a triangle-free graph on $n$ vertices with maximum degree $\lt n^{1/2-\epsilon}$.
> Can $G$ be made into a triangle-free graph with diameter $2$ by adding at most $\delta n^2$ edges?
>
> Asked by Erdős and Gyárfás, who proved that this is the case when $G$ has maximum degree $\ll \log n/\log\log n$. A construction of Simonovits shows that this conjecture is false if we just have maximum degree $\leq Cn^{1/2}$, for some large enough $C$. In this note Alon solves this problem in a strong form, in particular proving that a triangle-free graph on $n$ vertices with maximum degree $\lt n^{1/2-\epsilon}$ can be made into a triangle-free graph with diameter $2$ by adding at most $O(n^{2-\epsilon})$ edges.

```lean
theorem erdos_134 :
    ∀ (ε δ : ℝ) (hε : 0 < ε) (hδ : 0 < δ),
    ∃ N : ℕ, ∀ n ≥ N, ∀ (G : SimpleGraph (Fin n)) [DecidableRel G.Adj],
      G.CliqueFree 3 →
      (∀ v : Fin n, (G.degree v : ℝ) < Real.rpow (n : ℝ) ((1 : ℝ) / 2 - ε)) →
      ∃ (H : SimpleGraph (Fin n)) (_ : DecidableRel H.Adj),
        G ≤ H ∧
        H.CliqueFree 3 ∧
        (∀ x y : Fin n, x ≠ y → H.Adj x y ∨ ∃ z, H.Adj x z ∧ H.Adj z y) ∧
        ((H.edgeFinset \ G.edgeFinset).card : ℝ) ≤ δ * (n : ℝ) ^ 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/134.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/134.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/134.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/134.lean)
- [erdosproblems.com/134](https://www.erdosproblems.com/134)
