---
declaration: theorem
origin: cited
lean: Erdos1034.erdos_1034, Erdos1034.erdos_1034.variants.lower_bound, Erdos1034.erdos_1034.variants.upper_bound, Erdos1034.erdos_1034.variants.k4_free
statement: formalized
---

# Erdős Problem 1034

> *References:*
> - [erdosproblems.com/1034](https://www.erdosproblems.com/1034)
> - [Er93] Erdős, Paul, *Some of my favorite solved and unsolved problems in graph theory*.
>   Quaestiones Math. (1993), 333-350.
> - [MaTa25] Ma, Jie and Tang, Quanyu, *On Erdős problem #1034*.
>   [staff.ustc.edu.cn/~jiema/Erdos-1034.pdf](http://staff.ustc.edu.cn/~jiema/Erdos-1034.pdf)

*Quoted from [FormalConjectures/ErdosProblems/1034.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1034.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1034](https://www.erdosproblems.com/1034).

The file states 4 research or textbook statements: 4 solved.

## `Erdos1034.erdos_1034`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1034.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1034.lean).

> Let $G$ be a graph on $n$ vertices with $>n^2/4$ many edges. Must there be a triangle $T$ in $G$
> and vertices $y_1,\ldots,y_t$, where $t>(\frac{1}{2}-o(1))n$, such that every $y_i$ is joined to
> at least two vertices of $T$?
>
> A conjecture of Erdős and Faudree; a stronger version of [905].
>
> This has been solved in the negative by Ma and Tang [MaTa25], who construct a graph with $n$
> vertices and $>n^2/4$ edges in which every triangle has at most $(2-(5/2)^{1/2}+o(1))n$ vertices
> adjacent to at least two of its vertices (note that $2-(5/2)^{1/2}\approx 0.4189$).

```lean
theorem erdos_1034 :
    ¬ ∀ ε : ℝ, 0 < ε → ∀ᶠ (n : ℕ) in atTop, ∀ G : SimpleGraph (Fin n),
      (n : ℝ) ^ 2 / 4 < (G.edgeSet.ncard : ℝ) →
        ∃ T : Finset (Fin n), G.IsNClique 3 T ∧ ∃ Y : Finset (Fin n),
          JoinedToTwo G T Y ∧ (1 / 2 - ε) * (n : ℝ) < (Y.card : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1034.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1034.lean#L57).

## `Erdos1034.erdos_1034.variants.lower_bound`

Solved: stated here without proof.

> Erdős and Faudree asked about the threshold $h(n)$ such that every graph with $n$ vertices and
> $>n^2/4$ edges contained a triangle and $h(n)$ other vertices which are connected to at least two
> vertices of the triangle. The fact that every graph with $>n^2/4$ edges contains a book of size
> $n/6$ shows that
>
> $$(1/6-o(1))n \leq h(n).$$

```lean
theorem erdos_1034.variants.lower_bound (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ (n : ℕ) in atTop, ∀ G : SimpleGraph (Fin n),
      (n : ℝ) ^ 2 / 4 < (G.edgeSet.ncard : ℝ) →
        ∃ T : Finset (Fin n), G.IsNClique 3 T ∧ ∃ Y : Finset (Fin n),
          JoinedToTwo G T Y ∧ (1 / 6 - ε) * (n : ℝ) ≤ (Y.card : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1034.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1034.lean#L72).

## `Erdos1034.erdos_1034.variants.upper_bound`

Solved: stated here without proof.

> The construction of Ma and Tang [MaTa25] of a graph with $n$ vertices and $>n^2/4$ edges in which
> every triangle has at most $(2-(5/2)^{1/2}+o(1))n$ vertices adjacent to at least two of its
> vertices shows that, for the threshold $h(n)$ of `erdos_1034.variants.lower_bound`,
>
> $$h(n) \leq (2-(5/2)^{1/2}+o(1))n.$$

```lean
theorem erdos_1034.variants.upper_bound (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ (n : ℕ) in atTop, ∃ G : SimpleGraph (Fin n),
      (n : ℝ) ^ 2 / 4 < (G.edgeSet.ncard : ℝ) ∧
        ∀ T : Finset (Fin n), G.IsNClique 3 T → ∀ Y : Finset (Fin n),
          JoinedToTwo G T Y → (Y.card : ℝ) ≤ (2 - Real.sqrt (5 / 2) + ε) * (n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1034.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1034.lean#L86).

## `Erdos1034.erdos_1034.variants.k4_free`

Solved: stated here without proof.

> Erdős suggested that the answer is different if $G$ has no $K_4$. In the comments Ma and Tang
> sketch a proof that the conjecture remains false even if we assume that $G$ contains no $K_4$,
> constructing a graph with $n$ vertices, $>n^2/4$ edges, and no $K_4$, in which every triangle has
> at most $(2\sqrt{3}-3+o(1))n$ vertices adjacent to at least two of its vertices (note that
> $2\sqrt{3}-3\approx 0.464$).

```lean
theorem erdos_1034.variants.k4_free (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ (n : ℕ) in atTop, ∃ G : SimpleGraph (Fin n), G.CliqueFree 4 ∧
      (n : ℝ) ^ 2 / 4 < (G.edgeSet.ncard : ℝ) ∧
        ∀ T : Finset (Fin n), G.IsNClique 3 T → ∀ Y : Finset (Fin n),
          JoinedToTwo G T Y → (Y.card : ℝ) ≤ (2 * Real.sqrt 3 - 3 + ε) * (n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1034.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1034.lean#L101).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1034.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1034.lean)
- [erdosproblems.com/1034](https://www.erdosproblems.com/1034)
