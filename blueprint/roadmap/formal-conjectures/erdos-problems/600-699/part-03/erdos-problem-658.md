---
declaration: theorem
origin: cited
lean: Erdos658.erdos_658
statement: formalized
---

# Erdős Problem 658

> *References:*
> - [erdosproblems.com/658](https://www.erdosproblems.com/658)
> - [Er97e] Erdős, Paul, *Some of my favourite unsolved problems*. Math. Japon. (1997), 527-537.
> - [FuKa91] Furstenberg, H. and Katznelson, Y., *A density version of the Hales-Jewett Theorem*.
>   Journal d'Analyse Mathématique (1991), 64-119.
> - [So04] Solymosi, J., *A Note on a Question of Erdős and Graham*. Combinatorics, Probability and
>   Computing (2004), 263–267.

*Quoted from [FormalConjectures/ErdosProblems/658.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/658.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/658](https://www.erdosproblems.com/658).

The file states 1 research or textbook statement: 1 solved.

## `Erdos658.erdos_658`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos658.lean#L1516](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos658.lean#L1516).

> Let $\delta>0$ and $N$ be sufficiently large depending on $\delta$. Is it true that if
> $A\subseteq \{1,\ldots,N\}^2$ has $\lvert A\rvert \geq \delta N^2$ then $A$ must contain the
> vertices of a square?
>
> A problem of Graham, if the square is restricted to be axis-aligned. (It is unclear whether in
> [Er97e] had this restriction in mind.)
>
> This qualitative statement follows from the density Hales-Jewett theorem proved by Furstenberg
> and Katznelson [FuKa91]. A quantitative proof (yet with very poor bounds) was given by Solymosi
> [So04].
>
> The square is taken to be axis-aligned (Graham's version), which implies the version allowing
> arbitrary squares.

```lean
theorem erdos_658 : ∀ δ : ℝ, 0 < δ → ∀ᶠ N : ℕ in atTop,
    ∀ A : Finset (ℕ × ℕ), A ⊆ Finset.Icc 1 N ×ˢ Finset.Icc 1 N → δ * N ^ 2 ≤ A.card →
      ∃ a b d : ℕ, 0 < d ∧ (a, b) ∈ A ∧ (a + d, b) ∈ A ∧ (a, b + d) ∈ A ∧ (a + d, b + d) ∈ A
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/658.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/658.lean#L56).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/658.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/658.lean)
- [erdosproblems.com/658](https://www.erdosproblems.com/658)
