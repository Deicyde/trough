---
declaration: theorem
origin: cited
lean: Erdos741.erdos_741.parts.i, Erdos741.erdos_741.variants.lower, Erdos741.erdos_741.variants.exact_density, Erdos741.erdos_741.parts.ii
statement: formalized
---

# Erdős Problem 741

> *References:*
>  - [erdosproblems.com/741](https://www.erdosproblems.com/741)
>  - [Er94b] Erdős, Paul, Some problems in number theory, combinatorics and combinatorial geometry.
>     Math. Pannon. (1994), 261-269.

*Quoted from [FormalConjectures/ErdosProblems/741.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/741.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/741](https://www.erdosproblems.com/741).

The file states 4 research or textbook statements: 1 open and 3 solved.

## `Erdos741.erdos_741.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/google-deepmind/formal-conjectures/blob/9d492049e42167b0d2fd58a9e91da3bf160172b5/FormalConjectures/ErdosProblems/741.lean#L228](https://github.com/google-deepmind/formal-conjectures/blob/9d492049e42167b0d2fd58a9e91da3bf160172b5/FormalConjectures/ErdosProblems/741.lean#L228).

> Let $A\subseteq \mathbb{N}$ be such that $A+A$ has positive upper density.
> Can one always decompose $A=A_1\sqcup A_2$ such that $A_1+A_1$ and $A_2+A_2$
> both have positive upper density?
>
> This was proved by the DeepMind prover agent.

```lean
theorem erdos_741.parts.i : ∀ A : Set ℕ, 0 < upperDensity (A + A) → ∃ A₁ A₂,
    A = A₁ ∪ A₂ ∧ Disjoint A₁ A₂ ∧ 0 < upperDensity (A₁ + A₁)
    ∧ 0 < upperDensity (A₂ + A₂)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/741.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/741.lean#L46).

## `Erdos741.erdos_741.variants.lower`

Open: stated without proof.

> Let $A\subseteq \mathbb{N}$ be such that $A+A$ has positive lower density.
> Can one always decompose $A=A_1\sqcup A_2$ such that $A_1+A_1$ and $A_2+A_2$
> both have positive lower density?

```lean
theorem erdos_741.variants.lower : ∀ A : Set ℕ, 0 < lowerDensity (A + A) → ∃ A₁ A₂,
    A = A₁ ∪ A₂ ∧ Disjoint A₁ A₂ ∧ 0 < lowerDensity (A₁ + A₁)
    ∧ 0 < lowerDensity (A₂ + A₂)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/741.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/741.lean#L57).

## `Erdos741.erdos_741.variants.exact_density`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/486bc8afae062b6711cd16d3466d651ee2880a52/FormalConjectures/ErdosProblems/741.lean#L1449](https://github.com/mo271/formal-conjectures/blob/486bc8afae062b6711cd16d3466d651ee2880a52/FormalConjectures/ErdosProblems/741.lean#L1449).

> Let $A\subseteq \mathbb{N}$ be such that $A+A$ has positive density in the literal sense that its
> natural density exists and is positive.
> Can one always decompose $A=A_1\sqcup A_2$ such that $A_1+A_1$ and $A_2+A_2$
> both have positive density in this sense?
>
> This was disproved by the DeepMind prover agent.

```lean
theorem erdos_741.variants.exact_density :
    ¬ ∀ A : Set ℕ, HasPosDensity (A + A) → ∃ A₁ A₂,
    A = A₁ ∪ A₂ ∧ Disjoint A₁ A₂ ∧ HasPosDensity (A₁ + A₁)
    ∧ HasPosDensity (A₂ + A₂)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/741.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/741.lean#L73).

## `Erdos741.erdos_741.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/486bc8afae062b6711cd16d3466d651ee2880a52/FormalConjectures/ErdosProblems/741.lean#L1629](https://github.com/mo271/formal-conjectures/blob/486bc8afae062b6711cd16d3466d651ee2880a52/FormalConjectures/ErdosProblems/741.lean#L1629).

> Is there a basis $A$ of order $2$ such that if $A=A_1\sqcup A_2$ then $A_1+A_1$ and $A_2+A_2$
> cannot both have bounded gaps?
>
> This was proved by DeepMind prover agent.

```lean
theorem erdos_741.parts.ii : ∃ A : Set ℕ, IsAddBasisOfOrder (A ∪ {0}) 2 ∧ ∀ A₁ A₂,
    A = A₁ ∪ A₂ → Disjoint A₁ A₂ → ¬ (IsSyndetic (A₁ + A₁) ∧ IsSyndetic (A₂ + A₂))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/741.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/741.lean#L88).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/741.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/741.lean)
- [erdosproblems.com/741](https://www.erdosproblems.com/741)
