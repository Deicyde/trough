---
declaration: theorem
origin: cited
lean: Erdos5.erdos_5, Erdos5.erdos_5.variants.limit_point_set, Erdos5.erdos_5.variants.westzynthius, Erdos5.erdos_5.variants.goldston_pintz_yildirim, Erdos5.erdos_5.variants.erdos_ricci, Erdos5.erdos_5.variants.hildebrand_maier, Erdos5.erdos_5.variants.hildebrand_maier_measure, Erdos5.erdos_5.variants.pintz, Erdos5.erdos_5.variants.banks_freiberg_maynard, Erdos5.erdos_5.variants.banks_freiberg_maynard_measure, Erdos5.erdos_5.variants.merikoski, Erdos5.erdos_5.variants.merikoski_measure, Erdos5.erdos_5.variants.merikoski_bounded_gaps, Erdos5.erdos_5.variants.dense
statement: formalized
---

# Erdős Problem 5

> *References:*
> - [erdosproblems.com/5](https://www.erdosproblems.com/5)
> - [BFM16] Banks, William D. and Freiberg, Tristan and Maynard, James, *On limit points of the
>   sequence of normalized prime gaps*. Proc. Lond. Math. Soc. (3) (2016), 515-539.
> - [Er55] Erdős, Paul, *Some remarks on number theory*. Riveon Lematematika (1955), 45-48.
> - [Er65b] Erdős, Paul, *Some recent advances and current problems in number theory*. Lectures on
>   Modern Mathematics, Vol. III (1965), 196-244.
> - [Er85c] Erdős, P., *On some of my problems in number theory I would most like to see solved*.
>   Number theory (Ootacamund, 1984) (1985), 74-84.
> - [Er97c] Erdős, Paul, *Some of my favorite problems and results*. The mathematics of Paul Erdős,
>   I (1997), 47-67.
> - [GPY09] Goldston, Daniel A. and Pintz, János and Yıldırım, Cem Y., *Primes in tuples. I*.
>   Ann. of Math. (2) (2009), 819-862.
> - [HiMa88] Hildebrand, Adolf and Maier, Helmut, *Gaps between prime numbers*. Proc. Amer. Math.
>   Soc. (1988), 1-9.
> - [Me20] Merikoski, Jori, *Limit points of normalized prime gaps*. J. Lond. Math. Soc. (2) (2020),
>   99-124.
> - [Pi16] Pintz, János, *Polignac numbers, conjectures of Erdős on gaps between primes, arithmetic
>   progressions in primes, and the bounded gap conjecture*. From arithmetic to zeta-functions
>   (2016), 367-384.
> - [Ri56] Ricci, Giovanni, *Recherches sur l'allure de la suite $\{p_{n+1}-p_n/\log p_n\}$*.
>   Colloque sur la Théorie des Nombres, Bruxelles, 1955 (1956), 93-106.
> - [We31] Westzynthius, E., *Über die Verteilung der Zahlen, die zu den n ersten Primzahlen
>   teilerfremd sind*. Commentat. Phys. Math. (1931), 1-37.

*Quoted from [FormalConjectures/ErdosProblems/5.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/5.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/5](https://www.erdosproblems.com/5).

The file states 14 research or textbook statements: 3 open and 11 solved. It also has 6 test statements, counted here but not shown.

## `Erdos5.erdos_5`

Open: stated without proof.

> Let $C\geq 0$. Is there an infinite sequence of $n_i$ such that
> $$\lim_{i\to \infty}\frac{p_{n_i+1}-p_{n_i}}{\log n_i}=C?$$
>
> We formalise "an infinite sequence of $n_i$" as a strictly monotone sequence of indices
> `n : ℕ → ℕ`. Note that the numerator is the gap between the two *consecutive* primes
> $p_{n_i}$ and $p_{n_i+1}$, which is `primeGap (n i)`, and not the gap between the primes
> indexed by two consecutive members of the sequence.

```lean
theorem erdos_5 : ∀ C : ℝ, 0 ≤ C →
    ∃ n : ℕ → ℕ, StrictMono n ∧ Tendsto (fun i => normalizedGap (n i)) atTop (𝓝 C)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/5.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/5.lean#L84).

## `Erdos5.erdos_5.variants.limit_point_set`

Open: stated without proof.

> Let $S$ be the set of limit points of $(p_{n+1}-p_n)/\log n$. This problem asks whether
> $S=[0,\infty]$.
>
> Since $\infty\in S$ is known (see `erdos_5.variants.westzynthius`), the open content is the
> equality of the finite part of $S$ with $[0,\infty)$.

```lean
theorem erdos_5.variants.limit_point_set : limitPointSet = Ici 0
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/5.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/5.lean#L96).

## `Erdos5.erdos_5.variants.westzynthius`

Solved: stated here without proof.

> $\infty\in S$ by Westzynthius' result [We31] on large prime gaps.

```lean
theorem erdos_5.variants.westzynthius :
    ∃ n : ℕ → ℕ, StrictMono n ∧ Tendsto (fun i => normalizedGap (n i)) atTop atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/5.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/5.lean#L103).

## `Erdos5.erdos_5.variants.goldston_pintz_yildirim`

Solved: stated here without proof.

> $0\in S$ by the work of Goldston, Pintz, and Yildirim [GPY09] on small prime gaps.

```lean
theorem erdos_5.variants.goldston_pintz_yildirim : (0 : ℝ) ∈ limitPointSet
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/5.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/5.lean#L111).

## `Erdos5.erdos_5.variants.erdos_ricci`

Solved: stated here without proof.

> Erdős [Er55] and Ricci [Ri56] independently showed that $S$ has positive Lebesgue measure.

```lean
theorem erdos_5.variants.erdos_ricci : 0 < volume limitPointSet
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/5.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/5.lean#L118).

## `Erdos5.erdos_5.variants.hildebrand_maier`

Solved: stated here without proof.

> Hildebrand and Maier [HiMa88] showed that $S$ contains arbitrarily large (finite) numbers.

```lean
theorem erdos_5.variants.hildebrand_maier : ∀ C : ℝ, ∃ x ∈ limitPointSet, C < x
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/5.lean, line 125](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/5.lean#L125).

## `Erdos5.erdos_5.variants.hildebrand_maier_measure`

Solved: stated here without proof.

> [HiMa88] in fact prove the stronger statement that there is a constant $c>0$ with
> $\lambda([0,T]\cap S)\geq cT$ for all sufficiently large $T$.

```lean
theorem erdos_5.variants.hildebrand_maier_measure : ∃ c > (0 : ℝ), ∀ᶠ T : ℝ in atTop,
    ENNReal.ofReal (c * T) ≤ volume (limitPointSet ∩ Icc 0 T)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/5.lean, line 133](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/5.lean#L133).

## `Erdos5.erdos_5.variants.pintz`

Solved: stated here without proof.

> Pintz [Pi16] showed that there exists some small constant $c>0$ such that $[0,c]\subset S$.

```lean
theorem erdos_5.variants.pintz : ∃ c > (0 : ℝ), Icc 0 c ⊆ limitPointSet
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/5.lean, line 141](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/5.lean#L141).

## `Erdos5.erdos_5.variants.banks_freiberg_maynard`

Solved: stated here without proof.

> Banks, Freiberg, and Maynard [BFM16] showed that at least $12.5\%$ of $[0,\infty)$ belongs
> to $S$.
>
> This is [BFM16, Theorem 1.1]: for any nine nonnegative reals
> $\beta_1\leq\beta_2\leq\cdots\leq\beta_9$, at least one of the differences $\beta_j-\beta_i$
> with $i\lt j$ belongs to $S$.

```lean
theorem erdos_5.variants.banks_freiberg_maynard (β : Fin 9 → ℝ) (hβ : ∀ i, 0 ≤ β i)
    (hβmono : Monotone β) : ∃ i j, i < j ∧ β j - β i ∈ limitPointSet
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/5.lean, line 153](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/5.lean#L153).

## `Erdos5.erdos_5.variants.banks_freiberg_maynard_measure`

Solved: stated here without proof.

> The $12.5\%$ claim itself, as deduced in [BFM16, Corollary 1.2]:
> $\lambda([0,T]\cap S)\geq (1-o(1))T/8$ as $T\to\infty$.
>
> Note that the constant $1/8$ is only attained asymptotically and ineffectively; the bound
> [BFM16] obtain for *all* $T>0$ is the weaker $\lambda([0,T]\cap S)>T/22$.

```lean
theorem erdos_5.variants.banks_freiberg_maynard_measure : ∀ ε > (0 : ℝ), ∀ᶠ T : ℝ in atTop,
    ENNReal.ofReal ((1 - ε) * T / 8) ≤ volume (limitPointSet ∩ Icc 0 T)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/5.lean, line 165](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/5.lean#L165).

## `Erdos5.erdos_5.variants.merikoski`

Solved: stated here without proof.

> Merikoski [Me20] showed that at least $1/3$ of $[0,\infty)$ belongs to $S$.
>
> This is [Me20, Theorem 1]: for any reals $\beta_1\leq\beta_2\leq\beta_3\leq\beta_4$, at least
> one of the differences $\beta_j-\beta_i$ with $i\lt j$ belongs to $S$. Note that, in contrast with
> `erdos_5.variants.banks_freiberg_maynard`, the $\beta_i$ are not required to be nonnegative.

```lean
theorem erdos_5.variants.merikoski (β : Fin 4 → ℝ) (hβmono : Monotone β) :
    ∃ i j, i < j ∧ β j - β i ∈ limitPointSet
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/5.lean, line 177](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/5.lean#L177).

## `Erdos5.erdos_5.variants.merikoski_measure`

Solved: stated here without proof.

> The $1/3$ claim itself [Me20, Corollary 2]: $\lambda([0,T]\cap S)\geq T/3$ for all $T>0$.
>
> Unlike the $1/8$ of [BFM16], this bound holds uniformly in $T$ with no error term.

```lean
theorem erdos_5.variants.merikoski_measure : ∀ T > (0 : ℝ),
    ENNReal.ofReal (T / 3) ≤ volume (limitPointSet ∩ Icc 0 T)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/5.lean, line 187](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/5.lean#L187).

## `Erdos5.erdos_5.variants.merikoski_bounded_gaps`

Solved: stated here without proof.

> Merikoski [Me20] showed that $S$ has bounded gaps.
>
> This is [Me20, Corollary 3]: there is a (ineffective) constant $C\geq 0$ such that
> $S\cap[T,T+C]\neq\emptyset$ for all $T\geq 0$.

```lean
theorem erdos_5.variants.merikoski_bounded_gaps :
    ∃ C ≥ (0 : ℝ), ∀ T ≥ (0 : ℝ), (limitPointSet ∩ Icc T (T + C)).Nonempty
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/5.lean, line 198](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/5.lean#L198).

## `Erdos5.erdos_5.variants.dense`

Open: stated without proof.

> In [Er65b], [Er85c], and [Er97c] Erdős asks whether $S$ is everywhere dense (but Weisenberg
> notes that clearly $S$ is closed so this is equivalent to asking whether $S=[0,\infty]$).

```lean
theorem erdos_5.variants.dense : Ici (0 : ℝ) ⊆ closure limitPointSet
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/5.lean, line 207](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/5.lean#L207).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/5.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/5.lean)
- [erdosproblems.com/5](https://www.erdosproblems.com/5)
