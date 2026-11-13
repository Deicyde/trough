---
declaration: theorem
origin: cited
lean: Erdos1033.erdos_1033, Erdos1033.erdos_1033.variants.three_halves, Erdos1033.erdos_1033.variants.fan, Erdos1033.erdos_1033.variants.erdos_laskar
statement: formalized
---

# Erdős Problem 1033

> *References:*
> - [erdosproblems.com/1033](https://www.erdosproblems.com/1033)
> - [Er82e] Erdős, Paul, *Some of my favourite problems which recently have been solved*. (1982),
>   59--79.
> - [Er93] Erdős, Paul, *Some of my favorite solved and unsolved problems in graph theory*.
>   Quaestiones Math. (1993), 333-350.
> - [ErLa85] Erdős, Paul and Laskar, Renu, *A note on the size of a chordal subgraph*.
>   Congr. Numer. (1985), 81--86.
> - [Fa88] Fan, Genghua, *Degree sum for a triangle in a graph*. J. Graph Theory (1988), 249--263.

*Quoted from [FormalConjectures/ErdosProblems/1033.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1033.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1033](https://www.erdosproblems.com/1033).

The file states 4 research or textbook statements: 4 solved.

## `Erdos1033.erdos_1033`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-03-000006](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-03-000006).

> Let $h(n)$ be such that every graph on $n$ vertices with $>n^2/4$ many edges contains a triangle
> whose vertices have degrees summing to at least $h(n)$. Estimate $h(n)$. In particular, is it
> true that
>
> $$h(n)\geq (2(\sqrt{3}-1)-o(1))n?$$
>
> A conjecture of Bollobás and Erdős.
>
> The answer is no. A blow-up of the butterfly graph, posted on the
> [Erdős problems forum](https://www.erdosproblems.com/forum/thread/1033) in June and July 2026 and
> written up in [this note](https://woutercvb.github.io/Erdos1033_smalloptimization.pdf), gives
> arbitrarily large graphs with more than $n^2/4$ edges in which every triangle has degree sum at
> most $1.464n$, which is less than $2(\sqrt{3}-1)n$. Estimating the optimal value of $h(n)$ is
> still open.

```lean
theorem erdos_1033 :
    ¬ ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop, ∀ (G : SimpleGraph (Fin n)) [DecidableRel G.Adj],
      n ^ 2 < 4 * #G.edgeFinset →
        ∃ t, G.IsNClique 3 t ∧
          (2 * (Real.sqrt 3 - 1) - ε) * n ≤ ∑ v ∈ t, (G.degree v : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1033.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1033.lean#L57).

## `Erdos1033.erdos_1033.variants.three_halves`

Solved: stated here without proof.

> In [Er82e] it is asked whether $h(n)\geq \frac{3}{2}n$. The answer is no, since the construction
> of Erdős and Laskar [ErLa85] gives $h(n) \leq 2(\sqrt{3}-1)n+O(1)$ and
> $2(\sqrt{3}-1) < \frac{3}{2}$.

```lean
theorem erdos_1033.variants.three_halves :
    ¬ ∀ n : ℕ, ∀ (G : SimpleGraph (Fin n)) [DecidableRel G.Adj], n ^ 2 < 4 * #G.edgeFinset →
      ∃ t, G.IsNClique 3 t ∧ 3 * n ≤ 2 * ∑ v ∈ t, G.degree v
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1033.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1033.lean#L70).

## `Erdos1033.erdos_1033.variants.fan`

Solved: stated here without proof.

> Fan [Fa88] proved that $h(n) \geq \frac{21}{16}n$: every graph on $n$ vertices with $>n^2/4$
> edges contains a triangle whose degrees sum to at least $\frac{21}{16}n$.

```lean
theorem erdos_1033.variants.fan (n : ℕ) (G : SimpleGraph (Fin n)) [DecidableRel G.Adj]
    (hG : n ^ 2 < 4 * #G.edgeFinset) :
    ∃ t, G.IsNClique 3 t ∧ 21 * n ≤ 16 * ∑ v ∈ t, G.degree v
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1033.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1033.lean#L80).

## `Erdos1033.erdos_1033.variants.erdos_laskar`

Solved: stated here without proof.

> Erdős and Laskar [ErLa85] gave a construction showing that $h(n) \leq 2(\sqrt{3}-1)n+O(1)$:
> for all large $n$ there is a graph on $n$ vertices with $>n^2/4$ edges in which every triangle
> has degree sum at most $2(\sqrt{3}-1)n+O(1)$. The construction is made explicit in [Fa88].

```lean
theorem erdos_1033.variants.erdos_laskar :
    ∃ C : ℝ, ∀ᶠ n : ℕ in atTop, ∃ G : SimpleGraph (Fin n), n ^ 2 < 4 * #G.edgeFinset ∧
      ∀ t, G.IsNClique 3 t → ∑ v ∈ t, (G.degree v : ℝ) ≤ 2 * (Real.sqrt 3 - 1) * n + C
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1033.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1033.lean#L92).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1033.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1033.lean)
- [erdosproblems.com/1033](https://www.erdosproblems.com/1033)
