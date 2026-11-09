---
declaration: theorem
origin: cited
lean: Erdos711.erdos_711.parts.i, Erdos711.erdos_711.parts.ii
statement: formalized
---

# Erdős Problem 711

> *References:*
> - [erdosproblems.com/711](https://www.erdosproblems.com/711)
> - [ErPo80] Erdős, P. and Pomerance, C.,
>   *Matching the natural numbers up to $n$ with distinct multiples in another interval* (1980).
> - [Er92c] Erdős, P., *Some of my forgotten problems in number theory*.
>   Hardy-Ramanujan J. (1992), 34–50.
> - [vD26] van Doorn, W.,
>   [*On the length of an interval that contains distinct multiples of the first $n$ positive
>   integers*](https://arxiv.org/abs/2601.16972). Integers 26 (2026), #A7.

*Quoted from [FormalConjectures/ErdosProblems/711.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/711.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/711](https://www.erdosproblems.com/711).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos711.erdos_711.parts.i`

Open: stated without proof.

> Let $f(n,m)$ be minimal such that $(m,m+f(n,m))$ contains distinct integers
> $a_1,\ldots,a_n$ with $k \mid a_k$ for $1 \leq k \leq n$. Prove that
> $\max_m f(n,m) \leq n^{1+o(1)}$.

```lean
theorem erdos_711.parts.i : ∃ error : ℕ → ℝ,
    error =o[atTop] (fun _ ↦ (1 : ℝ)) ∧ ∀ᶠ n in atTop, ∀ m, ∃ L,
      HasDivisibleDistinctTuple n m L ∧ (L : ℝ) ≤ Real.rpow n (1 + error n)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/711.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/711.lean#L57).

## `Erdos711.erdos_711.parts.ii`

Solved: stated here without proof.

> Prove that $\max_m (f(n,m)-f(n,n)) \to \infty$.
>
> This was proved by van Doorn [vD26], who obtained the stronger lower bound
> $f(n,m)-f(n,n) \gg n\log n/\log\log n$ for a suitable $m=m(n)$ and all large $n$.

```lean
theorem erdos_711.parts.ii : ∀ B : ℕ, ∀ᶠ n in atTop,
    ∃ m Lm Ln : ℕ, IsMinimalIntervalLength n m Lm ∧
      IsMinimalIntervalLength n n Ln ∧ B ≤ Lm - Ln
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/711.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/711.lean#L67).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/711.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/711.lean)
- [erdosproblems.com/711](https://www.erdosproblems.com/711)
