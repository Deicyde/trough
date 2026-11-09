---
declaration: theorem
origin: cited
lean: SimpleGraph.theorem1, SimpleGraph.theorem2, SimpleGraph.F, SimpleGraph.F_three, SimpleGraph.F_four_le, SimpleGraph.F_four_le_fifteen
statement: formalized
---

# Degree sequences in triangle-free graphs

> Authors: P. Erdős, S. Fajtlowicz and W. Staton,
> Published in Discrete Mathematics 92 (1991) 85–88.

*Quoted from [FormalConjectures/Paper/DegreeSequencesTriangleFree.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/DegreeSequencesTriangleFree.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 6 solved. It also has 8 API statements, counted here but not shown.

## `SimpleGraph.theorem1`

Solved: stated here without proof.

> **Theorem 1.** If a triangle-free graph has `f = 2`,
> then it is bipartite, has minimum degree `1`, and
> its degree sequence is compact.

```lean
theorem theorem1 (G : SimpleGraph α) (h_conn: G.Connected) [DecidableRel G.Adj]
    (h₁ : G.CliqueFree 3) (h₂ : degreeSequenceMultiplicity G = 2) :
    G.IsBipartite ∧ G.minDegree = 1 ∧ HasCompactdegreeSequence G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/DegreeSequencesTriangleFree.lean, line 254](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/DegreeSequencesTriangleFree.lean#L254).

## `SimpleGraph.theorem2`

Solved: stated here without proof.

> **Theorem 2.** Every triangle-free graph is an induced subgraph of one
> with `f = 3`.

```lean
theorem theorem2 (G : SimpleGraph α) [DecidableRel G.Adj] (h_conn: G.Connected)
    (h : G.CliqueFree 3) :
    ∃ (β : Type*) (_ : Fintype β) (H : SimpleGraph β) (_ : DecidableRel H.Adj) (i : G ↪g H),
      H.CliqueFree 3 ∧ degreeSequenceMultiplicity H = 3
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/DegreeSequencesTriangleFree.lean, line 287](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/DegreeSequencesTriangleFree.lean#L287).

## `SimpleGraph.F`

A definition (`def`), not a statement; its category attribute says research solved.

> `F n` is the smallest number of vertices of a triangle-free graph
> with chromatic number `n` and `f = 3`.

```lean
noncomputable def F (n : ℕ) : ℕ
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/DegreeSequencesTriangleFree.lean, line 296](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/DegreeSequencesTriangleFree.lean#L296).

## `SimpleGraph.F_three`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/fc4f1f1d43b54106b0f932518075fef57829d6fb/Proofs/T_SimpleGraph_F_three.lean#L569](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/fc4f1f1d43b54106b0f932518075fef57829d6fb/Proofs/T_SimpleGraph_F_three.lean#L569).

> The smallest number of vertices of a triangle-free graph with chromatic number 3 and f=3 is 7.

```lean
theorem F_three : F 3 = 7
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/DegreeSequencesTriangleFree.lean, line 303](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/DegreeSequencesTriangleFree.lean#L303).

## `SimpleGraph.F_four_le`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/fc4f1f1d43b54106b0f932518075fef57829d6fb/Proofs/T_SimpleGraph_F_four_le.lean#L469](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/fc4f1f1d43b54106b0f932518075fef57829d6fb/Proofs/T_SimpleGraph_F_four_le.lean#L469).

> The smallest number of vertices of a triangle-free graph with chromatic number 4 and f=3 is at most 19.

```lean
theorem F_four_le : F 4 ≤ 19
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/DegreeSequencesTriangleFree.lean, line 309](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/DegreeSequencesTriangleFree.lean#L309).

## `SimpleGraph.F_four_le_fifteen`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/fc4f1f1d43b54106b0f932518075fef57829d6fb/Proofs/T_SimpleGraph_F_four_le.lean#L464](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/fc4f1f1d43b54106b0f932518075fef57829d6fb/Proofs/T_SimpleGraph_F_four_le.lean#L464).

> There is a triangle-free graph with chromatic number 4 and f=3 on 15 vertices: the Grötzsch
> graph with four more vertices, with degrees 2,2,2,3,3,3,4,4,4,5,5,5,6,6,6. This improves the bound
> 19 of Erdős, Fajtlowicz and Staton. An exhaustive computer search, not formalized, shows that 15 is
> optimal; see https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/fc4f1f1d43b54106b0f932518075fef57829d6fb/docs/EFS_F4.md.

```lean
theorem F_four_le_fifteen : F 4 ≤ 15
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/DegreeSequencesTriangleFree.lean, line 318](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/DegreeSequencesTriangleFree.lean#L318).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/DegreeSequencesTriangleFree.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/DegreeSequencesTriangleFree.lean)
