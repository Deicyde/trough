---
declaration: theorem
origin: cited
lean: Erdos987.erdos_987.parts.i, Erdos987.erdos_987.variants.sup_limsup_infty, Erdos987.erdos_987.variants.log_lower_bound, Erdos987.erdos_987.variants.sqrt_lower_bound, Erdos987.erdos_987.variants.linear_upper_bound_weak, Erdos987.erdos_987.variants.linear_upper_bound_clunie, Erdos987.erdos_987.variants.linear_upper_bound, Erdos987.erdos_987.variants.sqrt_log_upper_bound, Erdos987.erdos_987.parts.ii, Erdos987.erdos_987.variants.finite_distinct_points
statement: formalized
---

# Erdős Problem 987

> *References:*
> - [erdosproblems.com/987](https://www.erdosproblems.com/987)
> - [APSSV26b] B. Alexeev, M. Putterman, M. Sawhney, M. Sellke, and G. Valiant,
>   [Short proofs in combinatorics, probability, and number theory II](https://arxiv.org/abs/2604.06609).
>   arXiv:2604.06609 (2026).
> - [Cl67] Clunie, J., On a problem of Erdős. J. London Math. Soc. (1967), 133--136.
> - [Er64b] Erdős, P., Problems and results on diophantine approximations. Compositio Math. (1964),
>   52-65.
> - [Er65b] Erdős, P., Some remarks on number theory. Israel J. Math. (the actual reference
>   cited by Clunie 1967 as [2]; the erdosproblems.com bibliography points to a different
>   Erdős 1965 paper, "Some recent advances and current problems in number theory" (Lectures
>   on Modern Mathematics III, 1965, 196-244), which does not appear to contain the
>   exponential-sum log-bound proof).
> - [Ha74] Hayman, W. K., Research problems in function theory: new problems. (1974), 155--180.
> - [Li69] Lindström, B., An inequality for $B_2$-sequences. J. Combinatorial Theory (1969), 211-212.

*Quoted from [FormalConjectures/ErdosProblems/987.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/987.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/987](https://www.erdosproblems.com/987).

The file states 10 research or textbook statements: 10 solved.

## `Erdos987.erdos_987.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean](https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean).

> Question 1:
>
> Is it true that $\limsup_{k \to \infty} A_k = \infty$?
>
> Erdős [Er64b] remarks it is "easy to see" that $\limsup_k \sup_n |\sum_{j \le n} e(k x_j)| = \infty$.
> Erdős [Er65b] later found a "very easy" proof that $A_k \gg \log k$ for infinitely many $k$.
> Clunie [Cl67] proved that $A_k \gg k^{1/2}$ for infinitely many $k$, which implies the answer is
> yes (Tao independently found a proof). This is Problem 7.21 in [Ha74].

```lean
theorem erdos_987.parts.i :
    ∀ (x : ℕ → ℝ) (_ : ∀ j : ℕ, x j ∈ Set.Ioo (0 : ℝ) 1),
      atTop.limsup (fun k : ℕ => A x k) = ⊤
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [40 Sequences, series, summability](../../../by-subject/part-02/40-sequences-series-summability/README.md), [42 Harmonic analysis on Euclidean spaces](../../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/ErdosProblems/987.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/987.lean#L74).

## `Erdos987.erdos_987.variants.sup_limsup_infty`

Solved: stated here; a Lean proof is at [https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean](https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean).

> Erdős [Er64b] remarks it is "easy to see" that for every infinite sequence
> $x_1, x_2, \ldots \in (0, 1)$,
> $$\limsup_{k \to \infty} \sup_n \left\lvert \sum_{j \le n} e(k x_j) \right\rvert = \infty.$$

```lean
theorem erdos_987.variants.sup_limsup_infty
    (x : ℕ → ℝ) (hx : ∀ j : ℕ, x j ∈ Set.Ioo (0 : ℝ) 1) :
    atTop.limsup (fun k : ℕ =>
      ⨆ n : ℕ, ((‖∑ j ∈ range n, e ((k : ℝ) * x j)‖ : ℝ) : EReal)) = ⊤
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [40 Sequences, series, summability](../../../by-subject/part-02/40-sequences-series-summability/README.md), [42 Harmonic analysis on Euclidean spaces](../../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/ErdosProblems/987.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/987.lean#L85).

## `Erdos987.erdos_987.variants.log_lower_bound`

Solved: stated here; a Lean proof is at [https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean](https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean).

> Erdős [Er65b] proved that, for every infinite sequence $x_1, x_2, \ldots \in (0, 1)$,
> $A_k \gg \log k$ for infinitely many $k$.

```lean
theorem erdos_987.variants.log_lower_bound
    (x : ℕ → ℝ) (_hx : ∀ j : ℕ, x j ∈ Set.Ioo (0 : ℝ) 1) :
    ∃ c > 0, ∃ᶠ k : ℕ in atTop, ((c * Real.log k : ℝ) : EReal) ≤ A x k
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [40 Sequences, series, summability](../../../by-subject/part-02/40-sequences-series-summability/README.md), [42 Harmonic analysis on Euclidean spaces](../../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/ErdosProblems/987.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/987.lean#L96).

## `Erdos987.erdos_987.variants.sqrt_lower_bound`

Solved: stated here; a Lean proof is at [https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean](https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean).

> Clunie [Cl67] proved that, for every infinite sequence $x_1, x_2, \ldots \in (0, 1)$,
> $A_k \gg k^{1/2}$ for infinitely many $k$. (Tao independently found a proof.)

```lean
theorem erdos_987.variants.sqrt_lower_bound
    (x : ℕ → ℝ) (hx : ∀ j : ℕ, x j ∈ Set.Ioo (0 : ℝ) 1) :
    ∃ c > 0, ∃ᶠ k : ℕ in atTop, ((c * Real.sqrt k : ℝ) : EReal) ≤ A x k
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [40 Sequences, series, summability](../../../by-subject/part-02/40-sequences-series-summability/README.md), [42 Harmonic analysis on Euclidean spaces](../../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/ErdosProblems/987.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/987.lean#L106).

## `Erdos987.erdos_987.variants.linear_upper_bound_weak`

Solved: stated here; a Lean proof is at [https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean](https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean).

> **Linear upper bound (weakened).** A first weakened version of Clunie's `A_k ≤ k`: there
> exists a sequence $x \in (0,1)$ with $A_k \le 2k$ for all $k \ge 1$. The witness is the
> (shifted) van der Corput sequence. For the tighter $A_k \le k + 1$ bound see
> `linear_upper_bound_clunie`.

```lean
theorem erdos_987.variants.linear_upper_bound_weak :
    ∃ (x : ℕ → ℝ) (_ : ∀ j : ℕ, x j ∈ Set.Ioo (0 : ℝ) 1),
      ∀ k : ℕ, 1 ≤ k → A x k ≤ ((2 * k : ℝ) : EReal)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [40 Sequences, series, summability](../../../by-subject/part-02/40-sequences-series-summability/README.md), [42 Harmonic analysis on Euclidean spaces](../../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/ErdosProblems/987.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/987.lean#L118).

## `Erdos987.erdos_987.variants.linear_upper_bound_clunie`

Solved: stated here; a Lean proof is at [https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean](https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean).

> **Linear upper bound (tight via Clunie phase tracking).** Tighter than
> `linear_upper_bound_weak`: there exists a sequence $x \in (0,1)$ with $A_k \le k + 1$ for all
> $k \ge 1$, via the (shifted) van der Corput sequence. Whether the $+1$ can be eliminated to
> recover Clunie's exact $A_k \le k$ under the strict $\mathrm{Ioo}\,0\,1$ hypothesis is open in
> this formalization (see `linear_upper_bound`).

```lean
theorem erdos_987.variants.linear_upper_bound_clunie :
    ∃ (x : ℕ → ℝ) (_ : ∀ j : ℕ, x j ∈ Set.Ioo (0 : ℝ) 1),
      ∀ k : ℕ, 1 ≤ k → A x k ≤ (((k : ℝ) + 1) : EReal)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [40 Sequences, series, summability](../../../by-subject/part-02/40-sequences-series-summability/README.md), [42 Harmonic analysis on Euclidean spaces](../../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/ErdosProblems/987.lean, line 131](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/987.lean#L131).

## `Erdos987.erdos_987.variants.linear_upper_bound`

Solved: stated here; a Lean proof is at [https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean](https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean).

> Clunie [Cl67] proved that there exists an infinite sequence $\{z_\nu\}$ on the unit circle
> with $A_\nu \le \nu$ for all $\nu \ge 1$. Translating $z_\nu = e(x_\nu)$, the natural domain of
> $x_\nu$ is the half-open unit interval $\mathrm{Ico}\,0\,1$, matching the original
> [Er64b]/[Cl67] statement (any unit complex number is allowed, including $z = 1$, i.e. $x = 0$).
>
> **Note**: erdosproblems.com/987 phrases the problem with the *open* interval
> $x_\nu \in (0, 1)$, which excludes $z = 1$ and is strictly stronger than what [Er64b]/[Cl67]
> state; we align with the original papers here. The shifted-vdc $\le k + 1$ variant under the
> open interval is preserved as `linear_upper_bound_clunie`.

```lean
theorem erdos_987.variants.linear_upper_bound :
    ∃ (x : ℕ → ℝ) (_ : ∀ j : ℕ, x j ∈ Set.Ico (0 : ℝ) 1),
      ∀ k : ℕ, 1 ≤ k → A x k ≤ ((k : ℝ) : EReal)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [40 Sequences, series, summability](../../../by-subject/part-02/40-sequences-series-summability/README.md), [42 Harmonic analysis on Euclidean spaces](../../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/ErdosProblems/987.lean, line 148](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/987.lean#L148).

## `Erdos987.erdos_987.variants.sqrt_log_upper_bound`

Solved: stated here; a Lean proof is at [https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean](https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean).

> An internal OpenAI model (see [APSSV26b, §3]) proved that there exists an infinite sequence
> $x_1, x_2, \ldots \in (0, 1)$ such that
> $\sup_n \left\lvert \sum_{j \le n} e(k x_j) \right\rvert \ll (k \log k)^{1/2}$ for all $k \ge 1$
> (in particular $A_k \ll (k \log k)^{1/2}$).
>
> Note: the bound is restricted to $k \ge 2$ since $\log 1 = 0$ would make the RHS vanish at
> $k = 1$, while the LHS $\|\sum_{j < n} e(x_j)\|$ can equal $1$ (e.g. for $n = 1$).

```lean
theorem erdos_987.variants.sqrt_log_upper_bound :
    ∃ (x : ℕ → ℝ) (_ : ∀ j : ℕ, x j ∈ Set.Ioo (0 : ℝ) 1) (C : ℝ) (_ : 0 < C),
      ∀ k n : ℕ, 2 ≤ k → ‖∑ j ∈ range n, e (k * x j)‖ ≤ C * Real.sqrt (k * Real.log k)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [40 Sequences, series, summability](../../../by-subject/part-02/40-sequences-series-summability/README.md), [42 Harmonic analysis on Euclidean spaces](../../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/ErdosProblems/987.lean, line 163](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/987.lean#L163).

## `Erdos987.erdos_987.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean](https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean).

> **Question 2 (parts.ii)**: Is it possible for $A_k = o(k)$? Yes — there exists a sequence
> $(x_n) \in (0, 1)$ and a bound $b(k) = o(k)$ with $A x k \le b k$ eventually. A corollary of
> `sqrt_log_upper_bound` (which gives a $\sqrt{k \log k}$ bound) plus the asymptotic
> $\sqrt{k \log k} = o(k)$.

```lean
theorem erdos_987.parts.ii :
    ∃ (x : ℕ → ℝ) (_ : ∀ j : ℕ, x j ∈ Set.Ioo (0 : ℝ) 1) (b : ℕ → ℝ),
      b =o[atTop] (fun k : ℕ => (k : ℝ)) ∧ ∀ᶠ k : ℕ in atTop, A x k ≤ ((b k : ℝ) : EReal)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [40 Sequences, series, summability](../../../by-subject/part-02/40-sequences-series-summability/README.md), [42 Harmonic analysis on Euclidean spaces](../../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/ErdosProblems/987.lean, line 177](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/987.lean#L177).

## `Erdos987.erdos_987.variants.finite_distinct_points`

Solved: stated here; a Lean proof is at [https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean](https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean).

> Liu [Li69] showed that, for any $\epsilon > 0$, $A_k \gg k^{1 - \epsilon}$ infinitely often
> under the additional assumption that there are only a finite number of distinct points. Clunie
> observed in the Mathscinet review of [Li69] that under this assumption in fact $A_k = \infty$
> infinitely often (the version stated here).

```lean
theorem erdos_987.variants.finite_distinct_points
    (x : ℕ → ℝ) (_hx : ∀ j : ℕ, x j ∈ Set.Ioo (0 : ℝ) 1)
    (hfin : (Set.range x).Finite) :
    ∃ᶠ k : ℕ in atTop, A x k = ⊤
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [40 Sequences, series, summability](../../../by-subject/part-02/40-sequences-series-summability/README.md), [42 Harmonic analysis on Euclidean spaces](../../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/ErdosProblems/987.lean, line 189](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/987.lean#L189).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/987.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/987.lean)
- [erdosproblems.com/987](https://www.erdosproblems.com/987)
