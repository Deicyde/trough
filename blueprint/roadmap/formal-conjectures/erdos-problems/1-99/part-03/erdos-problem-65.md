---
declaration: theorem
origin: cited
lean: Erdos65.erdos_65.parts.i, Erdos65.erdos_65.parts.ii, Erdos65.erdos_65.variants.liu_montgomery
statement: formalized
---

# Erdős Problem 65

> *References:*
> - [erdosproblems.com/65](https://www.erdosproblems.com/65)
> - [GKS84] Gyárfás, A., Komlós, J. and Szemerédi, E., On the distribution of cycle lengths in graphs.
>   J. Graph Theory (1984), 441-462.
> - [GPSV85] Gyárfás, A., Prömel, H. J., Szemerédi, E. and Voigt, B., On the sum of the reciprocals
>   of cycle lengths in sparse graphs. Combinatorica (1985), 41-52.
> - [LiMo20] Liu, H. and Montgomery, R., A solution to Erdős and Hajnal's odd cycle problem.
>   arXiv:2010.15802 (2020).

*Quoted from [FormalConjectures/ErdosProblems/65.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/65.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/65](https://www.erdosproblems.com/65).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos65.erdos_65.parts.i`

Solved: stated here without proof.

> Let $G$ be a graph with $n$ vertices and $kn$ edges, and $a_1\lt a_2\lt \cdots$ be the lengths of
> cycles in $G$. Assume $n>0$. Is it true that
>
> $$\sum\frac{1}{a_i}\gg \log k?$$
>
> Gyárfás, Komlós, and Szemerédi [GKS84] have proved that this sum is $\gg \log k$, so that only
> the second question remains.
>
> The bound is stated for all sufficiently large $k$: [GKS84, Theorem 4'] proves it for $k \geq b$,
> where $b$ is a constant. The case of $k$ slightly larger than $1$ is a separate problem, studied
> in [GPSV85].

```lean
theorem erdos_65.parts.i :
    ∃ c > (0 : ℝ), ∀ᶠ k : ℝ in Filter.atTop,
      ∀ (n : ℕ) (V : Type) [Fintype V] (G : SimpleGraph V),
        0 < n →
        Fintype.card V = n →
        (G.edgeSet.ncard : ℝ) = k * n →
        (∑ᶠ a ∈ G.cycleLengths, (1 : ℝ) / a) ≥ c * Real.log k
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/65.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/65.lean#L50).

## `Erdos65.erdos_65.parts.ii`

Open: stated without proof.

> Is the sum $\sum\frac{1}{a_i}$ minimised when $G$ is a complete bipartite graph?
>
> This problem is #65 in Extremal Graph Theory in the graphs problem collection.

```lean
theorem erdos_65.parts.ii :
    ∀ (k : ℝ) (hk : 0 < k),
      ∀ (n : ℕ) (V : Type) [Fintype V] (G : SimpleGraph V),
        0 < n →
        Fintype.card V = n →
        (G.edgeSet.ncard : ℝ) = k * n →
        ∀ (A B : Type) [Fintype A] [Fintype B],
          Fintype.card (A ⊕ B) = n →
          ((completeBipartiteGraph A B).edgeSet.ncard : ℝ) = k * n →
          (∑ᶠ a ∈ (completeBipartiteGraph A B).cycleLengths, (1 : ℝ) / a) ≤
            (∑ᶠ a ∈ G.cycleLengths, (1 : ℝ) / a)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/65.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/65.lean#L65).

## `Erdos65.erdos_65.variants.liu_montgomery`

Solved: stated here without proof.

> Liu and Montgomery [LiMo20, Corollary 1.2] have proved the asymptotically sharp lower bound of
> $\geq (\tfrac{1}{2}-o(1))\log k$.

```lean
theorem erdos_65.variants.liu_montgomery :
    ∀ ε > (0 : ℝ), ∀ᶠ k : ℝ in Filter.atTop,
      ∀ (n : ℕ) (V : Type) [Fintype V] (G : SimpleGraph V),
        0 < n →
        Fintype.card V = n →
        (G.edgeSet.ncard : ℝ) = k * n →
        (∑ᶠ a ∈ G.cycleLengths, (1 : ℝ) / a) ≥ (1 / 2 - ε) * Real.log k
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/65.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/65.lean#L83).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/65.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/65.lean)
- [erdosproblems.com/65](https://www.erdosproblems.com/65)
