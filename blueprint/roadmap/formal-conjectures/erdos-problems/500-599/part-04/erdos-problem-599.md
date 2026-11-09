---
declaration: theorem
origin: cited
lean: Erdos599.erdos_599, Erdos599.erdos_599.variants.aharoni_berger
statement: formalized
---

# Erdős Problem 599

> *References:*
> - [erdosproblems.com/599](https://www.erdosproblems.com/599)
> - [AhBe09] Aharoni, Ron and Berger, Eli, *Menger's theorem for infinite graphs*,
>   *Invent. Math.* **176** (2009), 1--62.

*Quoted from [FormalConjectures/ErdosProblems/599.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/599.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/599](https://www.erdosproblems.com/599).

The file states 2 research or textbook statements: 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos599.erdos_599`

Solved: stated here without proof.

> **Erdős Problem 599** (the Erdős–Menger conjecture).
>
> Let $G$ be a (possibly infinite) graph and let $A, B$ be disjoint independent sets of
> vertices. Must there exist a family $P$ of pairwise vertex-disjoint paths from $A$ to $B$,
> and a set $S$ of vertices containing exactly one vertex from each path in $P$, such that
> every path from $A$ to $B$ contains at least one vertex of $S$?
>
> For finite $G$ this is equivalent to Menger's theorem. The answer is **yes**, proved by
> Aharoni and Berger [AhBe09].

```lean
theorem erdos_599 :
    ∀ (V : Type) (G : SimpleGraph V) (A B : Set V),
      Disjoint A B → G.IsIndepSet A → G.IsIndepSet B →
      ∃ (ι : Type) (a b : ι → V) (p : ∀ i, G.Walk (a i) (b i)) (S : Set V),
        (∀ i, a i ∈ A) ∧ (∀ i, b i ∈ B) ∧ (∀ i, (p i).IsPath) ∧
        (Pairwise fun i j => Disjoint {v | v ∈ (p i).support} {v | v ∈ (p j).support}) ∧
        S ⊆ {v | ∃ i, v ∈ (p i).support} ∧
        (∀ i, ∃! v, v ∈ S ∧ v ∈ (p i).support) ∧
        (∀ a' ∈ A, ∀ b' ∈ B, ∀ q : G.Walk a' b', q.IsPath → ∃ v ∈ q.support, v ∈ S)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/599.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/599.lean#L47).

## `Erdos599.erdos_599.variants.aharoni_berger`

Solved: stated here without proof.

> **Menger's theorem for infinite graphs** (Aharoni–Berger [AhBe09]).
>
> The theorem actually proved by Aharoni and Berger holds for arbitrary vertex sets $A$
> and $B$: in any (possibly infinite) graph $G$ there is a family $P$ of pairwise
> vertex-disjoint $A$--$B$ paths together with an $A$--$B$ separator $S$ consisting of the
> choice of exactly one vertex from each path in $P$. The disjointness and independence
> hypotheses of `erdos_599` are not needed.

```lean
theorem erdos_599.variants.aharoni_berger :
    ∀ (V : Type) (G : SimpleGraph V) (A B : Set V),
      ∃ (ι : Type) (a b : ι → V) (p : ∀ i, G.Walk (a i) (b i)) (S : Set V),
        (∀ i, a i ∈ A) ∧ (∀ i, b i ∈ B) ∧ (∀ i, (p i).IsPath) ∧
        (Pairwise fun i j => Disjoint {v | v ∈ (p i).support} {v | v ∈ (p j).support}) ∧
        S ⊆ {v | ∃ i, v ∈ (p i).support} ∧
        (∀ i, ∃! v, v ∈ S ∧ v ∈ (p i).support) ∧
        (∀ a' ∈ A, ∀ b' ∈ B, ∀ q : G.Walk a' b', q.IsPath → ∃ v ∈ q.support, v ∈ S)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/599.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/599.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/599.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/599.lean)
- [erdosproblems.com/599](https://www.erdosproblems.com/599)
