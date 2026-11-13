---
declaration: theorem
origin: cited
lean: Erdos151.erdos_151, Erdos151.erdos_151.variants.cliqueFree_four, Erdos151.erdos_151.variants.cliqueFree_three, Erdos151.erdos_151.variants.sqrt_bound
statement: formalized
---

# Erdős Problem 151

> *References:*
> - [erdosproblems.com/151](https://www.erdosproblems.com/151)
> - [Er88] Erdős, P., *Problems and results in combinatorial analysis and graph theory*.
>   Discrete Math. (1988), 81-92.
> - [EGT92] Erdős, P. and Gallai, T. and Tuza, Zs., *Covering the cliques of a graph with
>   vertices*. Discrete Math. (1992), 279-289.

*Quoted from [FormalConjectures/ErdosProblems/151.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/151.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/151](https://www.erdosproblems.com/151).

The file states 4 research or textbook statements: 2 open and 2 solved.

## `Erdos151.erdos_151`

Open: stated without proof.

> For a graph $G$, let $\tau(G)$ denote the minimal number of vertices that include at least one
> from each maximal clique of $G$ on at least two vertices. Let $H(n)$ be maximal such that every
> triangle-free graph on $n$ vertices contains an independent set on $H(n)$ vertices.
>
> If $G$ is a graph on $n$ vertices, is $\tau(G)\leq n-H(n)$?
>
> Erdős remarked that this is perhaps completely wrongheaded [Er88].

```lean
theorem erdos_151 :
    ∀ (n : ℕ) (G : SimpleGraph (Fin n)), cliqueTransversalNumber G ≤ n - H n
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/151.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/151.lean#L52).

## `Erdos151.erdos_151.variants.cliqueFree_four`

Open: stated without proof.

> Erdős and Gallai made no progress on the question even when $G$ is $K_4$-free [Er88].

```lean
theorem erdos_151.variants.cliqueFree_four :
    ∀ (n : ℕ) (G : SimpleGraph (Fin n)), G.CliqueFree 4 →
      cliqueTransversalNumber G ≤ n - H n
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/151.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/151.lean#L60).

## `Erdos151.erdos_151.variants.cliqueFree_three`

Solved: stated here without proof.

> If $G$ is triangle-free, then $\tau(G)\leq n-H(n)$: the complement of an independent set meets
> every edge.

```lean
theorem erdos_151.variants.cliqueFree_three (n : ℕ) (G : SimpleGraph (Fin n))
    (hG : G.CliqueFree 3) : cliqueTransversalNumber G ≤ n - H n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/151.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/151.lean#L70).

## `Erdos151.erdos_151.variants.sqrt_bound`

Solved: stated here without proof.

> It is easy to see that $\tau(G)\leq n-\sqrt{n}$. We state this with $\lfloor\sqrt{n}\rfloor$:
> with the real square root the bound fails for a single edge ($n = 2$, $\tau = 1$).

```lean
theorem erdos_151.variants.sqrt_bound (n : ℕ) (G : SimpleGraph (Fin n)) :
    cliqueTransversalNumber G ≤ n - Nat.sqrt n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/151.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/151.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/151.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/151.lean)
- [erdosproblems.com/151](https://www.erdosproblems.com/151)
