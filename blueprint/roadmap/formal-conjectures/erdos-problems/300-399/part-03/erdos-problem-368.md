---
declaration: theorem
origin: cited
lean: Erdos368.erdos_368.lower_bound, Erdos368.erdos_368.upper_bound, Erdos368.erdos_368.variants.tendsto, Erdos368.erdos_368.variants.subpower
statement: formalized
---

# Erdős Problem 368

> *References:*
> - [erdosproblems.com/368](https://www.erdosproblems.com/368)
> - [Er76d] Erdős, P., Problems and results on number theoretic properties of consecutive
>   integers and related questions. Proceedings of the Fifth Manitoba Conference on Numerical
>   Mathematics (1976), 25–44.
> - [Po18] Pólya, Georg, Zur arithmetischen Untersuchung der Polynome.
>   Math. Z. (1918), 143–148.
> - [Sc67b] Schinzel, A., On two theorems of Gelfond and some of their applications.
>   Acta Arith. (1967/68), 177–236.

*Quoted from [FormalConjectures/ErdosProblems/368.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/368.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/368](https://www.erdosproblems.com/368).

The file states 4 research or textbook statements: 2 open and 2 solved.

## `Erdos368.erdos_368.lower_bound`

Open: stated without proof.

> How large is the largest prime factor of $n(n+1)$?
> The truth is probably $F(n)\gg (\log n)^2$ for all $n$.

```lean
theorem erdos_368.lower_bound :
    ∃ c : ℝ, 0 < c ∧ ∀ n : ℕ, 1 ≤ n → c * Real.log n ^ 2 ≤ (F n : ℝ)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/368.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/368.lean#L48).

## `Erdos368.erdos_368.upper_bound`

Open: stated without proof.

> Erdős [Er76d] conjectured that, for every $\epsilon>0$, there are infinitely many $n$
> such that $F(n)<(\log n)^{2+\epsilon}$.

```lean
theorem erdos_368.upper_bound :
    ∀ ε : ℝ, 0 < ε → ∃ᶠ n : ℕ in atTop, (F n : ℝ) < Real.log n ^ (2 + ε)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/368.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/368.lean#L57).

## `Erdos368.erdos_368.variants.tendsto`

Solved: stated here without proof.

> Pólya [Po18] proved that $F(n)\to\infty$ as $n\to\infty$.

```lean
theorem erdos_368.variants.tendsto : Tendsto F atTop atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/368.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/368.lean#L63).

## `Erdos368.erdos_368.variants.subpower`

Solved: stated here without proof.

> For every $\delta>0$, there are infinitely many $n$ with $F(n)\leq n^\delta$.
> This follows from Schinzel's [Sc67b] observation that, for infinitely many $n$,
> $F(n)\leq n^{O(1/\log\log\log n)}$.

```lean
theorem erdos_368.variants.subpower :
    ∀ δ : ℝ, 0 < δ → ∃ᶠ n : ℕ in atTop, (F n : ℝ) ≤ (n : ℝ) ^ δ
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/368.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/368.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/368.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/368.lean)
- [erdosproblems.com/368](https://www.erdosproblems.com/368)
