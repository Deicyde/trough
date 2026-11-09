---
declaration: theorem
origin: cited
lean: Erdos1097.erdos_1097, Erdos1097.erdos_1097.variants.weaker, Erdos1097.erdos_1097.variants.lower_bound
statement: formalized
---

# Erdős Problem 1097

> *References:*
> - [erdosproblems.com/1097](https://www.erdosproblems.com/1097)
> - [Bo99] Bourgain, J., On the dimension of {K}akeya sets and related maximal
> inequalities. Geom. Funct. Anal. (1999), 256--282
> - [KaTa99] Katz, Nets Hawk and Tao, Terence, Bounds on arithmetic projections, and applications to the
> {K}akeya conjecture. Math. Res. Lett. (1999), 625--630.
> - [Le15] Lemm, Marius, New counterexamples for sums-differences. Proc. Amer. Math. Soc. (2015), 3863--3868.
> - [GGTW25] B. Georgiev, J. Gómez-Serrano, T. Tao, and A. Wagner, Mathematical exploration and discovery at scale. arXiv:2511.02864 (2025).

*Quoted from [FormalConjectures/ErdosProblems/1097.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1097.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1097](https://www.erdosproblems.com/1097).

The file states 3 research or textbook statements: 1 solved and 2 textbook results.

## `Erdos1097.erdos_1097`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/f13dd54b520cdf2136fdd3a04f0f9fa50e311358/FormalConjectures/ErdosProblems/1097.lean#L306](https://github.com/mo271/formal-conjectures/blob/f13dd54b520cdf2136fdd3a04f0f9fa50e311358/FormalConjectures/ErdosProblems/1097.lean#L306).

> The main conjecture: for any finite set of integers $A$ with $|A| = n$, the number of distinct
> common differences in three-term arithmetic progressions is $O(n^{3/2})$.
>
> This conjecture was resolved negatively by showing that the problem is exactly equivalent to
> Bourgain's sums-differences question [Bo99], which was introduced as an arithmetic path towards
> the Kakeya conjecture. Under this equivalence:
> - The greatest achievable exponent for this problem is equal to the smallest constant $c$
>   achievable for Bourgain's sums-differences question:
>
> $$|A -_G B| \ll \max(|A|, |B|, |A +_G B|)^c$$
>
> - The $O(n^{3/2})$ prediction is disproved because the lower bound has been shown to satisfy
>   $c \ge 1.77898$ (due to Zheng and AlphaEvolve [GGTW25], improving on Lemm [Le15]), which is
>   strictly greater than $3/2 = 1.5$.
> - The best known upper bound is $c \le 11/6 \approx 1.833$ (due to Katz and Tao [KaTa99]).
> - While the specific $O(n^{3/2})$ prediction is resolved negatively, the general question of
>   determining the exact optimal exponent $c$ remains open.

```lean
theorem erdos_1097 : ¬ ∃ C > (0 : ℝ), ∀ (A : Finset ℤ),
    (CommonDifferencesThreeTermAP A).ncard ≤ C * (A.card : ℝ) ^ (3 / 2 : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1097.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1097.lean#L66).

## `Erdos1097.erdos_1097.variants.weaker`

Textbook result, proved here.

> A weaker bound has been proven: there are always at most $n^2$ such values of $d$.

```lean
theorem erdos_1097.variants.weaker :
    ∀ A, (CommonDifferencesThreeTermAP A).ncard ≤ A.card ^ 2
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1097.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1097.lean#L74).

## `Erdos1097.erdos_1097.variants.lower_bound`

Textbook result, proved here.

> A trivial lower bound: for sufficiently large `n` there exist sets $A$ with $|A| = n$ that contain at least $\Omega(n)$
> distinct common differences of three-term arithmetic progressions.

```lean
theorem erdos_1097.variants.lower_bound : ∃ c > (0 : ℝ), ∀ᶠ n in Filter.atTop, ∃ (A : Finset ℤ),
    A.card = n ∧ c * (n : ℝ) ≤ (CommonDifferencesThreeTermAP A).ncard
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1097.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1097.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1097.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1097.lean)
- [erdosproblems.com/1097](https://www.erdosproblems.com/1097)
