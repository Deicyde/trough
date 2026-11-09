---
declaration: theorem
origin: cited
lean: Erdos806.erdos_806, Erdos806.erdos_806.variants.alon_bukh_sudakov, Erdos806.erdos_806.variants.erdos_newman
statement: formalized
---

# Erdős Problem 806

> *References:*
> - [erdosproblems.com/806](https://www.erdosproblems.com/806)
> - [ErNe77] Erdős, P. and Newman, D. J., *Bases for sets of integers*. J. Number Theory (1977),
>   420-425.
> - [ABS09] Alon, Noga and Bukh, Boris and Sudakov, Benny, *Discrete Kakeya-type problems and small
>   bases*. Israel J. Math. (2009), 285-301.

*Quoted from [FormalConjectures/ErdosProblems/806.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/806.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/806](https://www.erdosproblems.com/806).

The file states 3 research or textbook statements: 3 solved.

## `Erdos806.erdos_806`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos806.lean#L744](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos806.lean#L744).

> Let $A\subseteq \{1,\ldots,n\}$ with $\lvert A\rvert \leq n^{1/2}$. Must there exist some
> $B\subset\mathbb{Z}$ with $\lvert B\rvert=o(n^{1/2})$ such that $A\subseteq B+B$?
>
> A problem of Erdős and Newman [ErNe77], who proved that there exist $A$ with
> $\lvert A\rvert\asymp n^{1/2}$ such that if $A\subseteq B+B$ then
>
> $$\lvert B\rvert \gg \frac{\log\log n}{\log n}n^{1/2}.$$
>
> Resolved by Alon, Bukh, and Sudakov [ABS09], who proved that for any $A\subseteq \{1,\ldots,n\}$
> with $\lvert A\rvert \leq n^{1/2}$ there exists some $B$ such that $A\subseteq B+B$ and
>
> $$\lvert B\rvert \ll \frac{\log\log n}{\log n}n^{1/2}.$$
>
> See also [333](https://www.erdosproblems.com/333).

```lean
theorem erdos_806 : ∀ ε : ℝ, 0 < ε → ∀ᶠ n : ℕ in atTop,
    ∀ A : Finset ℕ, A ⊆ Finset.Icc 1 n → (A.card : ℝ) ≤ √n →
      ∃ B : Finset ℤ, A.map Nat.castEmbedding ⊆ B + B ∧ (B.card : ℝ) ≤ ε * √n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/806.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/806.lean#L55).

## `Erdos806.erdos_806.variants.alon_bukh_sudakov`

Solved: stated here without proof.

> Alon, Bukh, and Sudakov [ABS09] proved that for any $A\subseteq \{1,\ldots,n\}$ with
> $\lvert A\rvert \leq n^{1/2}$ there exists some $B$ such that $A\subseteq B+B$ and
> $\lvert B\rvert \ll \frac{\log\log n}{\log n}n^{1/2}$.

```lean
theorem erdos_806.variants.alon_bukh_sudakov : ∃ C : ℝ, ∀ᶠ n : ℕ in atTop,
    ∀ A : Finset ℕ, A ⊆ Finset.Icc 1 n → (A.card : ℝ) ≤ √n →
      ∃ B : Finset ℤ, A.map Nat.castEmbedding ⊆ B + B ∧
        (B.card : ℝ) ≤ C * Real.log (Real.log n) / Real.log n * √n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/806.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/806.lean#L66).

## `Erdos806.erdos_806.variants.erdos_newman`

Solved: stated here without proof.

> Erdős and Newman [ErNe77] proved that there exist $A\subseteq\{1,\ldots,n\}$ with
> $\lvert A\rvert\asymp n^{1/2}$ such that if $A\subseteq B+B$ then
> $\lvert B\rvert \gg \frac{\log\log n}{\log n}n^{1/2}$.

```lean
theorem erdos_806.variants.erdos_newman : ∃ c : ℝ, 0 < c ∧ ∀ᶠ n : ℕ in atTop,
    ∃ A : Finset ℕ, A ⊆ Finset.Icc 1 n ∧ c * √n ≤ A.card ∧ (A.card : ℝ) ≤ √n ∧
      ∀ B : Finset ℤ, A.map Nat.castEmbedding ⊆ B + B →
        c * Real.log (Real.log n) / Real.log n * √n ≤ B.card
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/806.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/806.lean#L78).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/806.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/806.lean)
- [erdosproblems.com/806](https://www.erdosproblems.com/806)
