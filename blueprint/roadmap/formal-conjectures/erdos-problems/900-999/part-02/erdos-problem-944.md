---
declaration: theorem
origin: cited
lean: Erdos944.erdos_944, Erdos944.erdos_944.variants.dirac_conjecture, Erdos944.erdos_944.variants.dirac_conjecture.k_eq_5, Erdos944.erdos_944.variants.dirac_conjecture.k_sub_one_not_prime, Erdos944.erdos_944.variants.dirac_conjecture.k_ge_five, Erdos944.erdos_944.variants.dirac_conjecture.k_eq_four, Erdos944.erdos_944.variants.large_k_for_any_r
statement: formalized
---

# Erdős Problem 944

> *Reference:* [erdosproblems.com/944](https://www.erdosproblems.com/944)

*Quoted from [FormalConjectures/ErdosProblems/944.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/944.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/944](https://www.erdosproblems.com/944).

The file states 7 research or textbook statements: 1 open and 6 solved.

## `Erdos944.erdos_944`

Open: stated without proof.

> Let $k \ge 4$ and $r\ge 1$. Must there exist a graph $G$ with chromatic number $k$
>  such that every vertex is critical, yet every critical set of edges has size $>r$?

```lean
theorem erdos_944 :
    ∀ k ≥ 4, ∀ r ≥ 1, ∃ (V : Type u) (G : SimpleGraph V), G.IsErdos944 k r
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/944.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/944.lean#L47).

## `Erdos944.erdos_944.variants.dirac_conjecture`

Solved: stated here without proof.

> Let $k \ge 4$. Must there exist a graph $G$ with chromatic number $k$
> such that every vertex is critical, yet every critical set of edges has size $>1$?
>
> This was conjectured by Dirac in 1970.

```lean
theorem erdos_944.variants.dirac_conjecture :
    ∀ k ≥ 4, ∃ (V : Type u) (G : SimpleGraph V), G.IsErdos944 k 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/944.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/944.lean#L58).

## `Erdos944.erdos_944.variants.dirac_conjecture.k_eq_5`

Solved: stated here without proof.

> Dirac's conjecture was proved, for $k=5$: There exists a graph $G$ with chromatic number $5$, such
> that every vertex is critical, yet every critical set of edges has size $>1$, or in other words:
> has no critical edge.
>
> [Br92] Brown, Jason I., A vertex critical graph without critical edges. Discrete Math. (1992), 99--101

```lean
theorem erdos_944.variants.dirac_conjecture.k_eq_5 :
    ∃ (V : Type u) (G : SimpleGraph V), G.IsErdos944 5 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/944.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/944.lean#L71).

## `Erdos944.erdos_944.variants.dirac_conjecture.k_sub_one_not_prime`

Solved: stated here without proof.

> Lattanzio [La02] proved there exist $k$-critical graphs without critical edges for all $k$ such that
> $k - 1$ is not prime.
>
> [La02] Lattanzio, John J., A note on a conjecture of {D}irac. Discrete Math. (2002), 323--330

```lean
theorem erdos_944.variants.dirac_conjecture.k_sub_one_not_prime (k : ℕ) (hk : 4 ≤ k)
    (h : ¬ (k - 1).Prime) : ∃ (V : Type u) (G : SimpleGraph V), G.IsErdos944 k 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/944.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/944.lean#L82).

## `Erdos944.erdos_944.variants.dirac_conjecture.k_ge_five`

Solved: stated here without proof.

> Jensen [Je02] gave an construction for $k$-critical graphs without any critical edges for all $k ≥ 5$.
>
> [Je02] Jensen, Tommy R., Dense critical and vertex-critical graphs. Discrete Math. (2002), 63--84.

```lean
theorem erdos_944.variants.dirac_conjecture.k_ge_five (k : ℕ) (hk : 5 ≤ k) :
    ∃ (V : Type u) (G : SimpleGraph V), G.IsErdos944 k 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/944.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/944.lean#L92).

## `Erdos944.erdos_944.variants.dirac_conjecture.k_eq_four`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/erdos-944-dirac-k4-lean/blob/9606d77/lean4web/Erdos944K4R1Lean4Web.lean#L676-L690](https://github.com/KitaKen1/erdos-944-dirac-k4-lean/blob/9606d77/lean4web/Erdos944K4R1Lean4Web.lean#L676-L690).

> The case $k=4$ and $r=1$ was the remaining open case: Are there $4$-critical graphs
> without any critical edges?
>
> Answer: Yes. The Lean formalization linked below proves the existence of such a graph.
> Together with Jensen's result for $k \ge 5$, this settles Dirac's conjecture for every
> $k \ge 4$.

```lean
theorem erdos_944.variants.dirac_conjecture.k_eq_four :
    ∃ (V : Type u) (G : SimpleGraph V), G.IsErdos944 4 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/944.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/944.lean#L108).

## `Erdos944.erdos_944.variants.large_k_for_any_r`

Solved: stated here without proof.

> Martinsson and Steiner [MaSt25] proved for every $r \ge 1$ if $k$ is sufficiently large, depending
> on $r$, there exist a graph $G$ with chromatic number $k$ such that every vertex is critical,
> yet every critical set of edges has size $>r$.
>
> [MaSt25] Martinsson, Anders and Steiner, Raphael, Vertex-critical graphs far from edge-criticality. Combin. Probab. Comput. (2025), 151--157

```lean
theorem erdos_944.variants.large_k_for_any_r (r : ℕ) (hr : 1 ≤ r) : ∀ᶠ k in Filter.atTop,
    ∃ (V : Type u) (G : SimpleGraph V), G.IsErdos944 k r
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/944.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/944.lean#L120).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/944.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/944.lean)
- [erdosproblems.com/944](https://www.erdosproblems.com/944)
