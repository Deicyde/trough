---
declaration: theorem
origin: cited
lean: Erdos1036.erdos_1036, Erdos1036.erdos_1036.variants.alon_hajnal, Erdos1036.erdos_1036.variants.erdos_hajnal
statement: formalized
---

# Erdős Problem 1036

> *References:*
> - [erdosproblems.com/1036](https://www.erdosproblems.com/1036)
> - [AlHa91] Alon, N. and Hajnal, A., *Ramsey graphs contain many distinct induced subgraphs*.
>   Graphs Combin. (1991), 1-6.
> - [ErHa89b] Erdős, P. and Hajnal, A., *On the number of distinct induced subgraphs of a graph*.
>   Discrete Math. (1989), 145-154.
> - [Sh98] Shelah, Saharon, *Erdős and Rényi conjecture*. J. Combin. Theory Ser. A (1998), 179-185.

*Quoted from [FormalConjectures/ErdosProblems/1036.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1036.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1036](https://www.erdosproblems.com/1036).

The file states 3 research or textbook statements: 3 solved.

## `Erdos1036.erdos_1036`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1036.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1036.lean).

> Let $G$ be a graph on $n$ vertices which does not contain a trivial (empty or complete) graph on
> more than $c\log n$ vertices. Must $G$ contain at least $2^{\Omega_c(n)}$ many induced subgraphs
> which are not pairwise isomorphic?
>
> This is true, and was proved by Shelah [Sh98].

```lean
theorem erdos_1036 :
    ∀ c : ℝ, 0 < c → ∃ δ : ℝ, 0 < δ ∧ ∀ᶠ n : ℕ in atTop, ∀ G : SimpleGraph (Fin n),
      G.IsCRamsey c →
        HasManyNonIsomorphicInducedSubgraphs G ((2 : ℝ) ^ (δ * (n : ℝ)))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1036.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1036.lean#L66).

## `Erdos1036.erdos_1036.variants.alon_hajnal`

Solved: stated here without proof.

> Alon and Hajnal [AlHa91] proved that $G$ must contain at least
>
> $$\exp\left(n(\log n)^{-O(\log\log n)}\right)$$
>
> many non-isomorphic induced subgraphs.

```lean
theorem erdos_1036.variants.alon_hajnal :
    ∀ c : ℝ, 0 < c → ∃ C : ℝ, 0 < C ∧ ∀ᶠ n : ℕ in atTop, ∀ G : SimpleGraph (Fin n),
      G.IsCRamsey c →
        HasManyNonIsomorphicInducedSubgraphs G
          (Real.exp ((n : ℝ) * Real.log (n : ℝ) ^ (-(C * Real.log (Real.log (n : ℝ))))))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1036.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1036.lean#L78).

## `Erdos1036.erdos_1036.variants.erdos_hajnal`

Solved: stated here without proof.

> Erdős and Hajnal [ErHa89b] proved that if neither $G$ nor its complement contains a balanced
> complete bipartite graph $K_{k,k}$ on more than $c\log n$ vertices (as a not necessarily induced
> subgraph) then $G$ contains at least $2^{\Omega_c(n)}$ many non-isomorphic induced subgraphs.

```lean
theorem erdos_1036.variants.erdos_hajnal :
    ∀ c : ℝ, 0 < c → ∃ δ : ℝ, 0 < δ ∧ ∀ᶠ n : ℕ in atTop, ∀ G : SimpleGraph (Fin n),
      NoLargeBiclique G (c * Real.log (n : ℝ)) →
        HasManyNonIsomorphicInducedSubgraphs G ((2 : ℝ) ^ (δ * (n : ℝ)))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1036.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1036.lean#L91).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1036.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1036.lean)
- [erdosproblems.com/1036](https://www.erdosproblems.com/1036)
