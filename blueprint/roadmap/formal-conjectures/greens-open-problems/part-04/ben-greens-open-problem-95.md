---
declaration: theorem
origin: cited
lean: Green95.green_95, Green95.green_95.variants.zakharov, Green95.green_95.variants.three_palindromes, Green95.green_95.variants.lower_bound
statement: formalized
---

# Ben Green's Open Problem 95

> *References:*
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.95)
> - [CLB18] Cilleruelo, J., Luca, F. and Baxter, L., *Every positive integer is a sum of three
>   palindromes*. Math. Comp. 87 (2018), 3023--3055.
>   [arXiv:1602.06208](https://arxiv.org/abs/1602.06208)
> - [Za24] Zakharov, D., *Most integers are not a sum of two palindromes*. Math. Proc. Cambridge
>   Philos. Soc. 177 (2024), 363--366. [arXiv:2402.10808](https://arxiv.org/abs/2402.10808)

*Quoted from [FormalConjectures/GreensOpenProblems/95.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/95.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 4 solved. It also has 2 test statements, counted here but not shown.

## `Green95.green_95`

Solved: stated here without proof.

> Are a positive proportion of positive integers a sum of two palindromes?
>
> [Gr24] adds: "Of course one must specify a base $g$ (say $g = 10$) in which one is working." We
> state the question in every base $g \ge 2$ and read "a positive proportion" as positive lower
> density. Whether $0$ counts as a palindrome does not change the density.
>
> The answer is no: Zakharov showed that the number of $n < X$ which are sums of two base-$g$
> palindromes is at most $X / \log^c X$ [Za24, Theorem 1], see `green_95.variants.zakharov`.

```lean
theorem green_95 : ∀ g : ℕ, 2 ≤ g → ¬ 0 < (sumsOfTwo g).lowerDensity
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/95.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/95.lean#L81).

## `Green95.green_95.variants.zakharov`

Solved: stated here without proof.

> **Zakharov's theorem.** For every integer $g \ge 2$ there is a constant $c > 0$ such that, for all
> large $X$, the number of $n < X$ which are a sum of two positive base-$g$ palindromes is at most
> $X / \log^c X$ [Za24, Theorem 1]. We state it for integer $X$. This answers the question of
> [CLB18], who had proved an upper bound $c X$ with $c < 1$ for $g \ge 3$ [CLB18, Theorem 1.4].

```lean
theorem green_95.variants.zakharov :
    ∀ g : ℕ, 2 ≤ g → ∃ c : ℝ, 0 < c ∧ ∀ᶠ X : ℕ in atTop,
      ((sumsOfTwoPositive g ∩ Set.Iio X).ncard : ℝ) ≤ (X : ℝ) / Real.log X ^ c
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/95.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/95.lean#L91).

## `Green95.green_95.variants.three_palindromes`

Solved: stated here without proof.

> **Cilleruelo, Luca and Baxter.** Let $g \ge 5$. Then every positive integer is a sum of three
> base-$g$ palindromes [CLB18, Theorem 1.2]. Here $0$ counts as a palindrome, as in [CLB18], so
> this says that every positive integer is a sum of at most three positive palindromes.

```lean
theorem green_95.variants.three_palindromes :
    ∀ g : ℕ, 5 ≤ g → ∀ n : ℕ, 0 < n →
      ∃ p q r, IsPalindrome g p ∧ IsPalindrome g q ∧ IsPalindrome g r ∧ p + q + r = n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/95.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/95.lean#L102).

## `Green95.green_95.variants.lower_bound`

Solved: stated here without proof.

> **Cilleruelo, Luca and Baxter.** Let $g \ge 2$. There is a constant $c_1 > 0$ such that, for all
> real $x \ge 2$, the number of $n \le x$ which are a sum of two base-$g$ palindromes is at least
> $x^{1 - c_1 / \sqrt{\log x}} = x e^{-c_1 \sqrt{\log x}}$ [CLB18, Theorem 1.3]. We count positive
> $n$ only.

```lean
theorem green_95.variants.lower_bound :
    ∀ g : ℕ, 2 ≤ g → ∃ c₁ : ℝ, 0 < c₁ ∧ ∀ x : ℝ, 2 ≤ x →
      x ^ (1 - c₁ / Real.sqrt (Real.log x)) ≤
        ({n : ℕ | 0 < n ∧ (n : ℝ) ≤ x ∧ n ∈ sumsOfTwo g}.ncard : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/95.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/95.lean#L114).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/95.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/95.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.95)
