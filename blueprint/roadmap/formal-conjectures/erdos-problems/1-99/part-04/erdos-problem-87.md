---
declaration: theorem
origin: cited
lean: Erdos87.erdos_87.parts.i, Erdos87.erdos_87.parts.ii
statement: formalized
---

# Erdős Problem 87

> *References:*
> - [erdosproblems.com/87](https://www.erdosproblems.com/87)
> - [Er95] Erdős, Paul, Some of my favourite problems in number theory, combinatorics, and geometry.
>   Resenhas (1995), 165-186.

*Quoted from [FormalConjectures/ErdosProblems/87.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/87.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/87](https://www.erdosproblems.com/87).

The file states 2 research or textbook statements: 2 open.

## `Erdos87.erdos_87.parts.i`

Open: stated without proof.

> Let $0 < \epsilon < 1$. Is it true that, if $k$ is sufficiently large, then
>
> $$R(G) > (1-\epsilon)^k R(k)$$
>
> for every graph $G$ with chromatic number $\chi(G)=k$?
>
> The restriction $\epsilon < 1$ excludes negative bases in $(1-\epsilon)^k$.
>
> This problem is #12 in Ramsey Theory in the graphs problem collection.

```lean
theorem erdos_87.parts.i :
    ∀ ε > (0 : ℝ), ε < 1 → ∀ᶠ k : ℕ in atTop,
      ∀ (V : Type) [Fintype V] (G : SimpleGraph V), G.chromaticNumber = (k : ℕ∞) →
        (SimpleGraph.diagonalGraphRamsey G : ℝ) >
          (1 - ε) ^ k * (SimpleGraph.diagonalRamsey k : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/87.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/87.lean#L45).

## `Erdos87.erdos_87.parts.ii`

Open: stated without proof.

> Even stronger, is there some $c > 0$ such that, for all large $k$,
>
> $$R(G) > c R(k)$$
>
> for every graph $G$ with chromatic number $\chi(G)=k$?
>
> This problem is #13 in Ramsey Theory in the graphs problem collection.

```lean
theorem erdos_87.parts.ii :
    ∃ c > (0 : ℝ), ∀ᶠ k : ℕ in atTop,
      ∀ (V : Type) [Fintype V] (G : SimpleGraph V), G.chromaticNumber = (k : ℕ∞) →
        (SimpleGraph.diagonalGraphRamsey G : ℝ) > c * (SimpleGraph.diagonalRamsey k : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/87.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/87.lean#L60).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/87.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/87.lean)
- [erdosproblems.com/87](https://www.erdosproblems.com/87)
