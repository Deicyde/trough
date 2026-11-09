---
declaration: theorem
origin: cited
lean: Erdos611.erdos_611.parts.i, Erdos611.erdos_611.parts.ii, Erdos611.erdos_611.variants.bollobas_erdos, Erdos611.erdos_611.variants.bollobas_erdos_sharp
statement: formalized
---

# Erdős Problem 611

> *References:*
> - [erdosproblems.com/611](https://www.erdosproblems.com/611)
> - [EGT92] Erdős, Paul and Gallai, Tibor and Tuza, Zsolt, *Covering the cliques of a graph with
>   vertices*. Discrete Math. (1992), 279-289.
> - [Er94] Erdős, P., *Problems and results on set systems and hypergraphs*. Extremal problems for
>   finite sets (Visegrád, 1991) (1994), 217-227.
> - [Er99] Erdős, Paul, *A selection of problems and results in combinatorics*. Combin. Probab.
>   Comput. (1999), 1-6.

*Quoted from [FormalConjectures/ErdosProblems/611.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/611.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/611](https://www.erdosproblems.com/611).

The file states 4 research or textbook statements: 2 open and 2 solved.

## `Erdos611.erdos_611.parts.i`

Open: stated without proof.

> For a graph $G$ let $\tau(G)$ denote the minimal number of vertices that include at least one
> from each maximal clique of $G$. Is it true that if all maximal cliques in $G$ have at least $cn$
> vertices then $\tau(G) = o_c(n)$?
>
> Here $n$ is the number of vertices, and $o_c(n)$ is uniform over all such graphs on $n$ vertices.
> $\tau(G)$ is `SimpleGraph.cliqueTransversalNumber`, which (as in Erdős Problem 151) ignores
> maximal cliques on one vertex; this makes no difference here, since for large $n$ every maximal
> clique has at least $cn \geq 2$ vertices.

```lean
theorem erdos_611.parts.i :
    ∀ c > (0 : ℝ), ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop, ∀ G : SimpleGraph (Fin n),
      AllMaximalCliquesAtLeast G (c * (n : ℝ)) →
        (G.cliqueTransversalNumber : ℝ) ≤ ε * (n : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/611.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/611.lean#L66).

## `Erdos611.erdos_611.parts.ii`

Open: stated without proof.

> For $0 < c < 1$, estimate the minimal $k_c(n)$ such that if every maximal clique in a graph $G$
> on $n$ vertices has at least $k_c(n)$ vertices then $\tau(G) < (1 - c)n$.
>
> We require $c < 1$: for $c \geq 1$ the bound $\tau(G) < (1 - c)n \leq 0$ is impossible, so
> $k_c(n)$ is degenerate. Erdős, Gallai, and Tuza [EGT92] proved a lower bound of the form
> $k_c(n) \geq n^{c'/\log\log n}$ for some $c' > 0$ (as reported on erdosproblems.com).

```lean
theorem erdos_611.parts.ii :
    ∀ c : ℝ, 0 < c → c < 1 →
      (fun n ↦ (cliqueThreshold c n : ℝ)) =Θ[atTop] erdos_611.parts.ii.answer c
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/611.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/611.lean#L83).

## `Erdos611.erdos_611.variants.bollobas_erdos`

Solved: stated here without proof.

> Bollobás and Erdős proved that if every maximal clique of a graph $G$ on $n$ vertices has at
> least $n + 3 - 2\sqrt{n}$ vertices then $\tau(G) = 1$ (as reported on erdosproblems.com).

```lean
theorem erdos_611.variants.bollobas_erdos :
    ∀ n : ℕ, ∀ G : SimpleGraph (Fin n),
      AllMaximalCliquesAtLeast G ((n : ℝ) + 3 - 2 * Real.sqrt (n : ℝ)) →
        G.cliqueTransversalNumber = 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/611.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/611.lean#L93).

## `Erdos611.erdos_611.variants.bollobas_erdos_sharp`

Solved: stated here without proof.

> The threshold $n + 3 - 2\sqrt{n}$ of Bollobás and Erdős is best possible. We formalise this as:
> for every $n = m^2$ with $m \geq 2$ there is a graph on $n$ vertices whose maximal cliques all
> have at least $n + 2 - 2\sqrt{n} = m^2 + 2 - 2m$ vertices and with $\tau(G) \geq 2$.

```lean
theorem erdos_611.variants.bollobas_erdos_sharp :
    ∀ m : ℕ, 2 ≤ m → ∃ G : SimpleGraph (Fin (m ^ 2)),
      AllMaximalCliquesAtLeast G ((m : ℝ) ^ 2 + 2 - 2 * (m : ℝ)) ∧
        2 ≤ G.cliqueTransversalNumber
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/611.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/611.lean#L105).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/611.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/611.lean)
- [erdosproblems.com/611](https://www.erdosproblems.com/611)
