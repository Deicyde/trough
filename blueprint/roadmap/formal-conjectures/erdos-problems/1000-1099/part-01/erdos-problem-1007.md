---
declaration: theorem
origin: cited
lean: Erdos1007.erdos_1007, Erdos1007.erdos_1007.variants.dimension_four_extremal, Erdos1007.erdos_1007.variants.dimension_five, Erdos1007.erdos_1007.variants.dimension_five_extremal
statement: formalized
---

# Erdős Problem 1007

> *References:*
> - [erdosproblems.com/1007](https://www.erdosproblems.com/1007)
> - [ChNo16] Chaffee, Joe and Noble, Matt, *Dimension 4 and dimension 5 graphs with minimum edge
>   set*. Australas. J. Combin. (2016), 327-333.
> - [Ho13] House, Roger F., *A 4-dimensional graph has at least 9 edges*. Discrete Math. (2013),
>   1783-1789.

*Quoted from [FormalConjectures/ErdosProblems/1007.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1007.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1007](https://www.erdosproblems.com/1007).

The file states 4 research or textbook statements: 4 solved.

## `Erdos1007.erdos_1007`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1007.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1007.lean).

> The dimension of a graph $G$ is the minimal $n$ such that $G$ can be embedded in $\mathbb{R}^n$
> such that every edge of $G$ is a unit line segment.
>
> What is the smallest number of edges in a graph with dimension $4$?
>
> Answer: The smallest number of edges is $9$, achieved solely by $K_{3,3}$, proved by House [Ho13]. An
> alternative proof was given by Chaffee and Noble [ChNo16], who also prove that the smallest
> number of edges in a graph of dimension $5$ is $15$ (achieved by $K_6$ and $K_{1,3,3}$).

```lean
theorem erdos_1007 :
    IsLeast {m | ∃ (n : ℕ) (G : SimpleGraph (Fin n)), G.HasDimension 4 ∧ G.edgeSet.ncard = m}
      9
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1007.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1007.lean#L54).

## `Erdos1007.erdos_1007.variants.dimension_four_extremal`

Solved: stated here; a Lean proof is at [https://github.com/Dishah3241/Erdos1007/blob/43f89415a6663848a1445effbda8b3abe77b052b/Erdos1007/Standalone/Mathlib/InlineErdos1007Proof.lean#L306](https://github.com/Dishah3241/Erdos1007/blob/43f89415a6663848a1445effbda8b3abe77b052b/Erdos1007/Standalone/Mathlib/InlineErdos1007Proof.lean#L306).

> The smallest number of edges in a graph of dimension $4$ is achieved solely by $K_{3,3}$.

```lean
theorem erdos_1007.variants.dimension_four_extremal (n : ℕ) (G : SimpleGraph (Fin n))
    (hdim : G.HasDimension 4) (hcard : G.edgeSet.ncard = 9)
    (hdeg : ∀ v : Fin n, ∃ w : Fin n, G.Adj v w) :
    Nonempty (G ≃g completeBipartiteGraph (Fin 3) (Fin 3))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1007.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1007.lean#L66).

## `Erdos1007.erdos_1007.variants.dimension_five`

Solved: stated here; a Lean proof is at [https://github.com/Dishah3241/Erdos1007Dim5/blob/7118d68eabffe49e41a672d16eb8ddba2608f03d/Erdos1007Dim5/Standalone/Mathlib/InlineErdos1007Dim5Proof.lean#L145](https://github.com/Dishah3241/Erdos1007Dim5/blob/7118d68eabffe49e41a672d16eb8ddba2608f03d/Erdos1007Dim5/Standalone/Mathlib/InlineErdos1007Dim5Proof.lean#L145).

> The smallest number of edges in a graph of dimension $5$ is $15$.

```lean
theorem erdos_1007.variants.dimension_five :
    IsLeast {m | ∃ (n : ℕ) (G : SimpleGraph (Fin n)), G.HasDimension 5 ∧ G.edgeSet.ncard = m}
      15
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1007.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1007.lean#L79).

## `Erdos1007.erdos_1007.variants.dimension_five_extremal`

Solved: stated here; a Lean proof is at [https://github.com/Dishah3241/Erdos1007Dim5/blob/7118d68eabffe49e41a672d16eb8ddba2608f03d/Erdos1007Dim5/Standalone/Mathlib/InlineErdos1007Dim5Proof.lean#L161](https://github.com/Dishah3241/Erdos1007Dim5/blob/7118d68eabffe49e41a672d16eb8ddba2608f03d/Erdos1007Dim5/Standalone/Mathlib/InlineErdos1007Dim5Proof.lean#L161).

> The smallest number of edges in a graph of dimension $5$ is achieved by $K_6$ and $K_{1,3,3}$.

```lean
theorem erdos_1007.variants.dimension_five_extremal :
    ((SimpleGraph.completeGraph (Fin 6)).HasDimension 5 ∧
        (SimpleGraph.completeGraph (Fin 6)).edgeSet.ncard = 15) ∧
      (K133.HasDimension 5 ∧ K133.edgeSet.ncard = 15)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1007.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1007.lean#L91).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1007.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1007.lean)
- [erdosproblems.com/1007](https://www.erdosproblems.com/1007)
