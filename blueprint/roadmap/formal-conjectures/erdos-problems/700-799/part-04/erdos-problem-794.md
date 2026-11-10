---
declaration: theorem
origin: cited
lean: Erdos794.erdos_794, Erdos794.erdos_794.variants.balogh, Erdos794.erdos_794.variants.harris, Erdos794.erdos_794.variants.frankl_furedi
statement: formalized
---

# Erdős Problem 794

> *References:*
> - [erdosproblems.com/794](https://www.erdosproblems.com/794)
> - [Er69] Erdős, Paul, *Some applications of graph theory to number theory*. The Many Facets of
>   Graph Theory (Proc. Conf., Western Mich. Univ., Kalamazoo, Mich., 1968) (1969), 77-82.
> - [FrFu84] Frankl, P. and Füredi, Z., *An exact result for $3$-graphs*. Discrete Math. (1984),
>   323-328.

*Quoted from [FormalConjectures/ErdosProblems/794.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/794.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/794](https://www.erdosproblems.com/794).

The file states 4 research or textbook statements: 4 solved.

## `Erdos794.erdos_794`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos794.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos794.lean).

> Is it true that every $3$-uniform hypergraph on $3n$ vertices with at least $n^3+1$ edges must
> contain either a subgraph on $4$ vertices with $3$ edges or a subgraph on $5$ vertices with $7$
> edges?
>
> Harris has provided the following simple counterexample to the problem as stated: the
> $3$-uniform graph on $\{1,\ldots,9\}$ with $28$ edges, formed by taking $27$ edges by choosing
> one element each from $\{1,2,3\},\{4,5,6\},\{7,8,9\}$, and then adding the edge $\{1,2,3\}$.

```lean
theorem erdos_794 :
    ¬ ∀ n : ℕ, ∀ H : Finset (Finset (Fin (3 * n))), H.IsUniform 3 →
      n ^ 3 + 1 ≤ H.card → H.ContainsSubgraph 4 3 ∨ H.ContainsSubgraph 5 7
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/794.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/794.lean#L59).

## `Erdos794.erdos_794.variants.balogh`

Proved here.

> Balogh has observed that this problem is probably misstated by Erdős - indeed, every graph with
> $5$ vertices spanning $7$ edges contains a graph on $4$ vertices spanning $3$ edges, so the
> second condition can be dropped.

```lean
theorem erdos_794.variants.balogh {V : Type*} [DecidableEq V] (H : Finset (Finset V))
    (hH : H.IsUniform 3) (h : H.ContainsSubgraph 5 7) : H.ContainsSubgraph 4 3
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/794.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/794.lean#L70).

## `Erdos794.erdos_794.variants.harris`

Proved here.

> Harris has provided the following simple counterexample to the problem as stated: the
> $3$-uniform graph on $\{1,\ldots,9\}$ with $28$ edges, formed by taking $27$ edges by choosing
> one element each from $\{1,2,3\},\{4,5,6\},\{7,8,9\}$, and then adding the edge $\{1,2,3\}$.

```lean
theorem erdos_794.variants.harris :
    harrisHypergraph.IsUniform 3 ∧ harrisHypergraph.card = 28 ∧
      ¬ harrisHypergraph.ContainsSubgraph 4 3 ∧ ¬ harrisHypergraph.ContainsSubgraph 5 7
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/794.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/794.lean#L109).

## `Erdos794.erdos_794.variants.frankl_furedi`

Solved: stated here without proof.

> This problem is then now asking how many edges a $3$-uniform hypergraph can have before it
> contains $K_4$ minus an edge, and whether the critical edge density is $2/9$. In fact there is a
> construction of Frankl and Füredi [FrFu84] showing it must be at least $2/7$, which is the
> conjectured truth (although Turán conjectured before [Er69] that the edge density was $1/4$, and
> so likely there is simply a typo in this problem's statement).

```lean
theorem erdos_794.variants.frankl_furedi (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ n : ℕ in atTop, ∃ H : Finset (Finset (Fin n)), H.IsUniform 3 ∧
      ¬ H.ContainsSubgraph 4 3 ∧ (2 / 7 - ε) * (n.choose 3 : ℝ) ≤ (H.card : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/794.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/794.lean#L123).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/794.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/794.lean)
- [erdosproblems.com/794](https://www.erdosproblems.com/794)
