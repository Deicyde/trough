---
declaration: theorem
origin: cited
lean: Erdos732.erdos_732.parts.i, Erdos732.erdos_732.parts.ii
statement: formalized
---

# Erdős Problem 732

> *References:*
> - [erdosproblems.com/732](https://www.erdosproblems.com/732)

*Quoted from [FormalConjectures/ErdosProblems/732.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/732.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/732](https://www.erdosproblems.com/732).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos732.erdos_732.parts.i`

Open: stated without proof.

> Call a sequence $1< X_1\leq \cdots \leq X_m\leq n$ block-compatible if there is a pairwise balanced
> block design $A_1,\ldots,A_m\subseteq \{1,\ldots,n\}$ such that $\lvert A_i\rvert=X_i$ for $1\leq
> i\leq m$. (A pairwise block design means that every pair in $\{1,\ldots,n\}$ is contained in exactly
> one of the $A_i$.) Are there necessary and sufficient conditions for $(X_i)$ to be block-compatible?
> Is there some constant $c>0$ such that for all large $n$ there are
> $$\geq \exp(c n^{1/2}\log n)$$
> many block-compatible sequences for $\{1,\ldots,n\}$?

```lean
theorem erdos_732.parts.i :
    ∀ (n : ℕ) (s : List ℕ), s ∈ Hypergraph.blockSizeProfiles n ↔ erdos_732.parts.i.answer n s
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/732.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/732.lean#L45).

## `Erdos732.erdos_732.parts.ii`

Solved: stated here without proof.

> Is there some constant $c>0$ such that for all large $n$ there are at least
> $\exp(c n^{1/2}\log n)$ block-compatible sequences?
>
> Alon has proved there are at least $2^{(\frac{1}{2}+o(1))n^{1/2}\log n}$ many sequences
> which are block-compatible for $n$.

```lean
theorem erdos_732.parts.ii :
    ∃ c : ℝ, 0 < c ∧ ∀ᶠ n : ℕ in atTop,
    Real.exp (c * Real.sqrt n * Real.log n) ≤ (Hypergraph.blockSizeProfiles n).card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/732.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/732.lean#L57).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/732.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/732.lean)
- [erdosproblems.com/732](https://www.erdosproblems.com/732)
