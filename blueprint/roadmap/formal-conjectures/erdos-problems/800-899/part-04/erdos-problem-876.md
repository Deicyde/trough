---
declaration: theorem
origin: cited
lean: Erdos876.erdos_876.parts.i, Erdos876.erdos_876.parts.ii, Erdos876.erdos_876.variants.density_zero, Erdos876.erdos_876.variants.recip_sum_lt, Erdos876.erdos_876.variants.recip_sum_bounds, Erdos876.erdos_876.variants.dem_ratio, Erdos876.erdos_876.variants.dem_polynomial
statement: formalized
---

# Erdős Problem 876

> *References:*
> - [erdosproblems.com/876](https://www.erdosproblems.com/876)
> - [Er62c] Erdős, P., *Some remarks on number theory. III* (in Hungarian). Mat. Lapok 13 (1962),
>   28-38. [PDF](https://www.renyi.hu/~p_erdos/1962-22.pdf)
> - [Er75b] Erdős, P., *Problems and results in combinatorial number theory*. Journées Arithmétiques
>   de Bordeaux (Conf., Univ. Bordeaux, 1974), Astérisque 24-25 (1975), 295-310.
>   [PDF](https://www.renyi.hu/~p_erdos/1975-30.pdf)
> - [Er77c] Erdős, P., *Problems and results on combinatorial number theory. III*. Number theory day
>   (Proc. Conf., Rockefeller Univ., New York, 1976), Lecture Notes in Math. 626 (1977), 43-72.
>   [PDF](https://www.renyi.hu/~p_erdos/1977-27.pdf)
> - [Er98] Erdős, P., *Some of my new and almost new problems and results in combinatorial number
>   theory*. Number theory (Eger, 1996) (1998), 169-180.
> - [DEM99] Deshouillers, J.-M., Erdős, P. and Melfi, G., *On a question about sum-free sequences*.
>   Discrete Math. 200 (1999), 49-54.
> - [LeOS77] Levine, E. and O'Sullivan, J., *An upper estimate for the reciprocal sum of a sum-free
>   sequence*. Acta Arith. 34 (1977), 9-24.
> - [Ab87] Abbott, H. L., *On sum-free sequences*. Acta Arith. 48 (1987), 93-96.
>
> See also [erdosproblems.com/790](https://www.erdosproblems.com/790).

*Quoted from [FormalConjectures/ErdosProblems/876.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/876.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/876](https://www.erdosproblems.com/876).

The file states 7 research or textbook statements: 2 open and 5 solved. It also has 1 test statement, counted here but not shown.

## `Erdos876.erdos_876.parts.i`

Open: stated without proof.

> Let $A=\{a_1\lt a_2\lt \cdots\}\subset \mathbb{N}$ be an infinite sum-free set - that is, there are no
> solutions to
>
> $$a=b_1+\cdots+b_r$$
>
> with $b_1\lt \cdots\lt b_r\lt a\in A$. How small can $a_{n+1}-a_n$ be? Is it possible that
> $a_{n+1}-a_n\lt n$?
>
> The gap question is discussed by Erdős in [Er98]. We state the second question. The inequality
> $a_{n+1}-a_n\lt n$ is required for all large $n$, because it fails for $n=1$. The first question is
> vaguer and is not formalised.

```lean
theorem erdos_876.parts.i :
    ∃ A : Set ℕ, A.Infinite ∧ IsSubsetSumFree A ∧ ∀ᶠ n : ℕ in atTop, gap A n < n
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/876.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/876.lean#L93).

## `Erdos876.erdos_876.parts.ii`

Open: stated without proof.

> In [Er75b] and [Er77c] Erdős asks to determine the maximum possible value of
> $\sum_{n\in A}\frac{1}{n}$. Erdős had proved this is $<100$, and Sullivan had shown that this is
> $<4$, and Sullivan conjectured the maximum is slightly larger than $2$ [Er77c, p. 52].
>
> Here $A$ ranges over infinite sum-free sets, and the maximum is read as the supremum
> `maxRecipSum`.

```lean
theorem erdos_876.parts.ii : maxRecipSum = erdos_876.parts.ii.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/876.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/876.lean#L108).

## `Erdos876.erdos_876.variants.density_zero`

Solved: stated here without proof.

> Erdős [Er62c, Theorem I] proved that a sum-free set has density zero (restated as
> [DEM99, Theorem 1]).

```lean
theorem erdos_876.variants.density_zero (A : Set ℕ) (hA : A.Infinite) (hs : IsSubsetSumFree A) :
    A.HasDensity 0
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/876.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/876.lean#L116).

## `Erdos876.erdos_876.variants.recip_sum_lt`

Solved: stated here without proof.

> Erdős [Er62c, Theorem II] proved that $\sum_{a\in A}1/a$ converges and is $<103$ for every
> infinite sum-free set $A$; see also [Er75b, p. 302] and [DEM99, p. 49]. The later paper
> [Er77c, p. 52] states the bound as $100$.

```lean
theorem erdos_876.variants.recip_sum_lt (A : Set ℕ) (hA : A.Infinite) (hs : IsSubsetSumFree A) :
    ∃ s : ℝ, s < 103 ∧ HasSum (fun a : A ↦ (1 : ℝ) / (a : ℕ)) s
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/876.lean, line 126](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/876.lean#L126).

## `Erdos876.erdos_876.variants.recip_sum_bounds`

Solved: stated here without proof.

> Let $R$ be the supremum of $\sum_j 1/n_j$ over sum-free sequences $\{n_j\}$. Levine and O'Sullivan
> [LeOS77] proved $R<4$ (and $R>2.035$), and Abbott [Ab87] improved the lower bound to $R>2.064$,
> as reported in [DEM99, p. 50].

```lean
theorem erdos_876.variants.recip_sum_bounds : 2.064 < maxRecipSum ∧ maxRecipSum < 4
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/876.lean, line 136](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/876.lean#L136).

## `Erdos876.erdos_876.variants.dem_ratio`

Solved: stated here without proof.

> Deshouillers, Erdős and Melfi [DEM99, Theorem 3] constructed an infinite sum-free set with
> $a_{n+1}/a_n\to 1$.

```lean
theorem erdos_876.variants.dem_ratio :
    ∃ A : Set ℕ, A.Infinite ∧ IsSubsetSumFree A ∧
      Tendsto (fun k : ℕ ↦ (Nat.nth (· ∈ A) (k + 1) : ℝ) / (Nat.nth (· ∈ A) k : ℝ))
        atTop (nhds 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/876.lean, line 144](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/876.lean#L144).

## `Erdos876.erdos_876.variants.dem_polynomial`

Solved: stated here without proof.

> Deshouillers, Erdős and Melfi [DEM99, Theorem 4] proved that for every $\delta>0$ there is an
> infinite sum-free set with $a_n\sim n^{3+\delta}$; we state the consequence $a_n\ll n^{3+\delta}$.
> The site writes $a_n\sim n^{3+o(1)}$.

```lean
theorem erdos_876.variants.dem_polynomial (δ : ℝ) (hδ : 0 < δ) :
    ∃ A : Set ℕ, A.Infinite ∧ IsSubsetSumFree A ∧
      ∃ C : ℝ, ∀ k : ℕ, (Nat.nth (· ∈ A) k : ℝ) ≤ C * ((k : ℝ) + 1) ^ (3 + δ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/876.lean, line 156](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/876.lean#L156).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/876.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/876.lean)
- [erdosproblems.com/876](https://www.erdosproblems.com/876)
