---
declaration: theorem
origin: cited
lean: Erdos557.erdos_557, Erdos557.erdos_557.variants.explicit, Erdos557.erdos_557.variants.tight, Erdos557.erdos_557.variants.tight_odd
statement: formalized
---

# Erdős Problem 557

> *References:*
> - [erdosproblems.com/557](https://www.erdosproblems.com/557)
> - [ErGr75] Erdős, P. and Graham, R. L., *On partition theorems for finite graphs*. Infinite and
>   finite sets (Colloq., Keszthely, 1973), Vol. I, Colloq. Math. Soc. János Bolyai 10 (1975),
>   515-527.
> - [ReSt26] Reed, Bruce and Stein, Maya, *The Erdős-Sós conjecture in dense graphs*.
>   [arXiv:2609.05417](https://arxiv.org/abs/2609.05417) (2026).

*Quoted from [FormalConjectures/ErdosProblems/557.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/557.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/557](https://www.erdosproblems.com/557).

The file states 4 research or textbook statements: 4 solved.

## `Erdos557.erdos_557`

Solved: stated here; a Lean proof is at [https://github.com/zhangjun725/erdos557/blob/c4e0ab13027f8bb50defade11cf8a53c7b8b0ba9/Erdos557/Basic.lean#L153](https://github.com/zhangjun725/erdos557/blob/c4e0ab13027f8bb50defade11cf8a53c7b8b0ba9/Erdos557/Basic.lean#L153).

> Let $R_k(G)$ denote the minimal $m$ such that if the edges of $K_m$ are $k$-coloured then there
> is a monochromatic copy of $G$. Is it true that
>
> $$R_k(T)\leq kn+O(1)$$
>
> for any tree $T$ on $n$ vertices?
>
> The answer is yes, with an absolute constant: $R_k(T) \leq kn + 3$ for all $k$ and $n$. For
> $n \geq 2$ this follows from the explicit bound $R_k(T) \leq k(n-2)+3$, a consequence of the
> Erdős–Sós theorem (Erdős problem 548) by the pigeonhole principle, as recorded on the problem page;
> Reed and Stein [ReSt26] derived that bound for $n$ large in terms of $k$ from their dense-graph case
> of Erdős–Sós. For the one-vertex tree, $R_k(T) \leq 2$.

```lean
theorem erdos_557 :
    ∃ c : ℕ, ∀ (k n : ℕ) (T : SimpleGraph (Fin n)), T.IsTree →
      multicolourGraphRamsey k T ≤ k * n + c
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/557.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/557.lean#L53).

## `Erdos557.erdos_557.variants.explicit`

Solved: stated here; a Lean proof is at [https://github.com/zhangjun725/erdos557/blob/c4e0ab13027f8bb50defade11cf8a53c7b8b0ba9/Erdos557/Basic.lean#L147](https://github.com/zhangjun725/erdos557/blob/c4e0ab13027f8bb50defade11cf8a53c7b8b0ba9/Erdos557/Basic.lean#L147).

> The explicit bound $R_k(T) \leq k(n-2)+3$ for every $k$ and every tree $T$ on $n \geq 2$ vertices.
> The problem page states this bound for $n$ sufficiently large in terms of $k$.
>
> The Lean statement uses natural-number subtraction, so for $n = 1$ it reads $R_k(T) \leq 3$, which
> also holds (the one-vertex tree has $R_k(T) \leq 2$). With ordinary subtraction the displayed formula
> would be false for $n = 1$ and $k \geq 3$.

```lean
theorem erdos_557.variants.explicit (k n : ℕ) (T : SimpleGraph (Fin n)) (hT : T.IsTree) :
    multicolourGraphRamsey k T ≤ k * (n - 2) + 3
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/557.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/557.lean#L69).

## `Erdos557.erdos_557.variants.tight`

Solved: stated here; a Lean proof is at [https://github.com/zhangjun725/erdos557/blob/828ad6fdb5d0f1a72b8dcd812f4c91c285570ff6/Erdos557/Tight.lean#L108](https://github.com/zhangjun725/erdos557/blob/828ad6fdb5d0f1a72b8dcd812f4c91c285570ff6/Erdos557/Tight.lean#L108).

> The best-possible bound $R_k(T) \leq k(n-2)+2$ for every $k$ and every tree $T$ on $n \geq 2$
> vertices, attained by stars. It follows from the sharp form of the Erdős–Sós theorem (a graph on
> $m$ vertices with more than $(n-2)m/2$ edges contains every tree on $n$ vertices) by the
> pigeonhole principle.

```lean
theorem erdos_557.variants.tight (k n : ℕ) (hn : 2 ≤ n) (T : SimpleGraph (Fin n))
    (hT : T.IsTree) : multicolourGraphRamsey k T ≤ k * (n - 2) + 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/557.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/557.lean#L82).

## `Erdos557.erdos_557.variants.tight_odd`

Solved: stated here; a Lean proof is at [https://github.com/zhangjun725/erdos557/blob/828ad6fdb5d0f1a72b8dcd812f4c91c285570ff6/Erdos557/Tight.lean#L114](https://github.com/zhangjun725/erdos557/blob/828ad6fdb5d0f1a72b8dcd812f4c91c285570ff6/Erdos557/Tight.lean#L114).

> When $n$ is odd and $k \geq 2$ is even, $R_k(T) \leq k(n-2)+1$ for every tree $T$ on $n$ vertices,
> again attained by stars: with $m = k(n-2)+1$ some colour class has at least $(n-2)m/2$ edges, and
> $(n-2)m$ is odd, so it has more than $(n-2)m/2$ edges.

```lean
theorem erdos_557.variants.tight_odd (k n : ℕ) (hk : 0 < k) (hke : Even k) (hn : 2 ≤ n)
    (hno : Odd n) (T : SimpleGraph (Fin n)) (hT : T.IsTree) :
    multicolourGraphRamsey k T ≤ k * (n - 2) + 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/557.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/557.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/557.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/557.lean)
- [erdosproblems.com/557](https://www.erdosproblems.com/557)
