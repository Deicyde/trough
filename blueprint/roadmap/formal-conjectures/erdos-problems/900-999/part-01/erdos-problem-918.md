---
declaration: theorem
origin: cited
lean: Erdos918.erdos_918.parts.i, Erdos918.erdos_918.parts.ii, Erdos918.erdos_918.variants.all_subgraphs.parts.i, Erdos918.erdos_918.variants.all_subgraphs.parts.ii, Erdos918.erdos_918.variants.erdos_hajnal, Erdos918.erdos_918.variants.eq_aleph_0.parts.i, Erdos918.erdos_918.variants.eq_aleph_0_all_subgraphs.parts.i, Erdos918.erdos_918.variants.eq_aleph_0.parts.ii, Erdos918.erdos_918.variants.eq_aleph_0_all_subgraphs.parts.ii
statement: formalized
---

# Erdős Problem 918

> *References:*
> - [erdosproblems.com/918](https://www.erdosproblems.com/918)
> - [ErHa68b] Erdős, P. and Hajnal, A., On chromatic number of infinite graphs. (1968), 83--98.
> - [Er69b] Erdős, P., Problems and results in chromatic graph theory. Proof Techniques in Graph Theory (Proc. Second Ann Arbor Graph Theory Conf., Ann Arbor, Mich., 1968) (1969), 27-35.

*Quoted from [FormalConjectures/ErdosProblems/918.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/918.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/918](https://www.erdosproblems.com/918).

The file states 9 research or textbook statements: 4 open, 1 solved and 4 textbook results.

## `Erdos918.erdos_918.parts.i`

Open: stated without proof.

> Is there a graph with $\aleph_2$ vertices and chromatic number $\aleph_2$ such that every
> subgraph on $\aleph_1$ vertices has chromatic number $\leq\aleph_0$?

```lean
theorem erdos_918.parts.i :
    ∃ (V : Type u) (G : SimpleGraph V), #V = ℵ_ 2 ∧ G.chromaticCardinal = ℵ_ 2 ∧
      ∀ (W : Set V) (_ : #W = ℵ₁), (G.induce W).chromaticCardinal ≤ ℵ₀
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/918.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/918.lean#L41).

## `Erdos918.erdos_918.parts.ii`

Open: stated without proof.

> Is there a graph with $\aleph_{\omega+1}$ vertices and chromatic number $\aleph_1$ such that
> every subgraph on $\aleph_\omega$ vertices has chromatic number $\leq\aleph_0$?

```lean
theorem erdos_918.parts.ii :
    ∃ (V : Type u) (G : SimpleGraph V), #V = ℵ_ (ω + 1) ∧ G.chromaticCardinal = ℵ₁ ∧
      ∀ (W : Set V) (_ : #W = ℵ_ ω), (G.induce W).chromaticCardinal ≤ ℵ₀
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/918.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/918.lean#L52).

## `Erdos918.erdos_918.variants.all_subgraphs.parts.i`

Open: stated without proof.

> Is there a graph with $\aleph_2$ vertices and chromatic number $\aleph_2$ such that every
> subgraph on $\aleph_1$ vertices has chromatic number $\leq\aleph_0$?

```lean
theorem erdos_918.variants.all_subgraphs.parts.i :
    ∃ (V : Type u) (G : SimpleGraph V), #V = ℵ_ 2 ∧ G.chromaticCardinal = ℵ_ 2 ∧
      ∀ (H : G.Subgraph) (_ : #H.verts = ℵ₁), H.coe.chromaticCardinal ≤ ℵ₀
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/918.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/918.lean#L66).

## `Erdos918.erdos_918.variants.all_subgraphs.parts.ii`

Open: stated without proof.

> Is there a graph with $\aleph_{\omega+1}$ vertices and chromatic number $\aleph_1$ such that
> every subgraph on $\aleph_\omega$ vertices has chromatic number $\leq\aleph_0$?

```lean
theorem erdos_918.variants.all_subgraphs.parts.ii :
    ∃ (V : Type u) (G : SimpleGraph V), #V = ℵ_ (ω + 1) ∧ G.chromaticCardinal = ℵ₁ ∧
    ∀ (H : G.Subgraph) (_ : #H.verts = ℵ_ ω), H.coe.chromaticCardinal ≤ ℵ₀
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/918.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/918.lean#L74).

## `Erdos918.erdos_918.variants.erdos_hajnal`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/82c9238052cac467baaf930d5dbe8ae6191a574c/erdos-918/Solution.lean#L56](https://github.com/linrock/math-proofs/blob/82c9238052cac467baaf930d5dbe8ae6191a574c/erdos-918/Solution.lean#L56).

> A question of Erd\H{o}s and Hajnal [ErHa68b], who proved, assuming the generalized continuum
> hypothesis, that for every finite $k \geq 1$ there is a graph with chromatic number $\aleph_1$ and
> $\aleph_k$ vertices where each subgraph on less than $\aleph_k$ vertices has chromatic number
> $\leq \aleph_0$.

```lean
theorem erdos_918.variants.erdos_hajnal (hGCH : ∀ c : Cardinal.{u}, ℵ₀ ≤ c → 2 ^ c = Order.succ c)
    (k : ℕ) (hk : 0 < k) : ∃ (V : Type u) (G : SimpleGraph V),
    #V = ℵ_ k ∧ G.chromaticCardinal = ℵ₁ ∧
      ∀ (W : Set V) (_ : #W < ℵ_ k), (G.induce W).chromaticCardinal ≤ ℵ₀
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/918.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/918.lean#L89).

## `Erdos918.erdos_918.variants.eq_aleph_0.parts.i`

Textbook result, stated without proof. A Lean proof is at [https://github.com/linrock/math-proofs/blob/82c9238052cac467baaf930d5dbe8ae6191a574c/erdos-918/Solution.lean#L62](https://github.com/linrock/math-proofs/blob/82c9238052cac467baaf930d5dbe8ae6191a574c/erdos-918/Solution.lean#L62).

> In [Er69b] the questions are stated with $= \aleph_0$ rather than $\leq\aleph_0$. This is
> a likely typo since it can be shown that no such graph exists in this case.
>
> This is the first question with induced subgraphs.

```lean
theorem erdos_918.variants.eq_aleph_0.parts.i :
    ¬∃ (V : Type u) (G : SimpleGraph V), #V = ℵ_ 2 ∧ G.chromaticCardinal = ℵ_ 2 ∧
      ∀ (W : Set V) (_ : #W = ℵ₁), (G.induce W).chromaticCardinal = ℵ₀
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/918.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/918.lean#L106).

## `Erdos918.erdos_918.variants.eq_aleph_0_all_subgraphs.parts.i`

Textbook result, stated without proof. A Lean proof is at [https://github.com/linrock/math-proofs/blob/82c9238052cac467baaf930d5dbe8ae6191a574c/erdos-918/Solution.lean#L67](https://github.com/linrock/math-proofs/blob/82c9238052cac467baaf930d5dbe8ae6191a574c/erdos-918/Solution.lean#L67).

> In [Er69b] the questions are stated with $= \aleph_0$ rather than $\leq\aleph_0$. This is
> a likely typo since it can be shown that no such graph exists in this case.
>
> This is the first question with all subgraphs.

```lean
theorem erdos_918.variants.eq_aleph_0_all_subgraphs.parts.i :
    ¬∃ (V : Type u) (G : SimpleGraph V), #V = ℵ_ 2 ∧ G.chromaticCardinal = ℵ_ 2 ∧
      ∀ (H : G.Subgraph) (_ : #H.verts = ℵ₁), H.coe.chromaticCardinal = ℵ₀
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/918.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/918.lean#L117).

## `Erdos918.erdos_918.variants.eq_aleph_0.parts.ii`

Textbook result, stated without proof. A Lean proof is at [https://github.com/linrock/math-proofs/blob/82c9238052cac467baaf930d5dbe8ae6191a574c/erdos-918/Solution.lean#L72](https://github.com/linrock/math-proofs/blob/82c9238052cac467baaf930d5dbe8ae6191a574c/erdos-918/Solution.lean#L72).

> In [Er69b] the questions are stated with $= \aleph_0$ rather than $\leq\aleph_0$. This is
> a likely typo since it can be shown that no such graph exists in this case.
>
> This is the second question with induced subgraphs.

```lean
theorem erdos_918.variants.eq_aleph_0.parts.ii :
    ¬∃ (V : Type u) (G : SimpleGraph V), #V = ℵ_ (ω + 1) ∧ G.chromaticCardinal = ℵ₁ ∧
      ∀ (W : Set V) (_ : #W = ℵ_ ω), (G.induce W).chromaticCardinal = ℵ₀
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/918.lean, line 133](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/918.lean#L133).

## `Erdos918.erdos_918.variants.eq_aleph_0_all_subgraphs.parts.ii`

Textbook result, stated without proof. A Lean proof is at [https://github.com/linrock/math-proofs/blob/82c9238052cac467baaf930d5dbe8ae6191a574c/erdos-918/Solution.lean#L78](https://github.com/linrock/math-proofs/blob/82c9238052cac467baaf930d5dbe8ae6191a574c/erdos-918/Solution.lean#L78).

> In [Er69b] the questions are stated with $= \aleph_0$ rather than $\leq\aleph_0$. This is
> a likely typo since it can be shown that no such graph exists in this case.
>
> This is the second question with all subgraphs.

```lean
theorem erdos_918.variants.eq_aleph_0_all_subgraphs.parts.ii :
    ¬∃ (V : Type u) (G : SimpleGraph V), #V = ℵ_ (ω + 1) ∧ G.chromaticCardinal = ℵ₁ ∧
      ∀ (H : G.Subgraph) (_ : #H.verts = ℵ_ ω), H.coe.chromaticCardinal = ℵ₀
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/918.lean, line 144](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/918.lean#L144).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/918.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/918.lean)
- [erdosproblems.com/918](https://www.erdosproblems.com/918)
