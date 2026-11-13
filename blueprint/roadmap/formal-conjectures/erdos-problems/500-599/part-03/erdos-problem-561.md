---
declaration: theorem
origin: cited
lean: Erdos561.erdos_561
statement: formalized
---

# Erdős Problem 561

> *References:*
> - [erdosproblems.com/561](https://www.erdosproblems.com/561)
> - [BEFRS78] Burr, S. A. and Erdős, P. and Faudree, R. J. and Rousseau, C. C. and Schelp, R. H.,
>   Ramsey-minimal graphs for multiple copies. Nederl. Akad. Wetensch. Indag. Math. (1978), 187-195.

*Quoted from [FormalConjectures/ErdosProblems/561.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/561.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/561](https://www.erdosproblems.com/561).

The file states 1 research or textbook statement: 1 open.

## `Erdos561.erdos_561`

Open: stated without proof.

> Let $\hat{R}(G)$ denote the size Ramsey number, the minimal number of edges $m$ such that there
> is a graph $H$ with $m$ edges such that in any $2$-colouring of the edges of $H$ there is a
> monochromatic copy of $G$.
>
> Let $F_1$ and $F_2$ be the union of stars. More precisely, let
> $F_1=\cup_{i\leq s}K_{1,n_i}$ and $F_2=\cup_{j\leq t}K_{1,m_j}$ with
> $n_1\geq\cdots\geq n_s\geq1$ and $m_1\geq\cdots\geq m_t\geq1$. Prove that
>
> $$\hat{R}(F_1,F_2)=\sum_{2\leq k\leq s+t}l_k$$
>
> where
>
> $$l_k=\max\{n_i+m_j-1:i+j=k\}.$$
>
> The unions are vertex-disjoint, and $s,t\geq1$. Lean indices start at zero, so the condition
> $i+j=k$ is represented by $(i+1)+(j+1)=k$.

```lean
theorem erdos_561 :
    ∀ (s t : ℕ), 1 ≤ s → 1 ≤ t →
    ∀ (n : Fin s → ℕ) (m : Fin t → ℕ),
      Antitone n → Antitone m → (∀ i, 1 ≤ n i) → (∀ j, 1 ≤ m j) →
      sizeRamsey F(s, n) F(t, m) =
        ∑ k ∈ Finset.Icc 2 (s + t),
          ((Finset.univ : Finset (Fin s × Fin t)).filter
            (fun p ↦ (p.1.val + 1) + (p.2.val + 1) = k)).sup
              (fun p ↦ n p.1 + m p.2 - 1)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/561.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/561.lean#L58).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/561.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/561.lean)
- [erdosproblems.com/561](https://www.erdosproblems.com/561)
