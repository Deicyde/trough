---
declaration: theorem
origin: cited
lean: Erdos387.erdos_387, Erdos387.erdos_387.variants.schinzel, Erdos387.erdos_387.variants.easy, Erdos387.erdos_387.variants.guy
statement: formalized
---

# Erdős Problem 387

> *References:*
>  - [erdosproblems.com/387](https://www.erdosproblems.com/387)
>  - [ErGr76b] Erdős, P. and Graham, R. L., *On the prime factors of
>    ${n \choose k}$*. Fibonacci Quart. (1976), 348-352.
>  - [Er78g] Erdős, Pál, *On prime factors of binomial coefficients. II*. Mat. Lapok
>    (1978/82), 307-316.
>  - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial
>    number theory*. Monographies de L'Enseignement Mathematique (1980).
>  - [Sc58] Schinzel, A., *Sur un problème de P. Erdős*. Colloq. Math. (1958), 198-204.
>  - [Gu04] Guy, Richard K., Unsolved problems in number theory. (2004), xviii+437.
>  - [Fa66] Faulkner, M. "On a theorem of Sylvester and Schur." Journal of the London Mathematical
>     Society 1.1 (1966): 107-110.
>  - [BNPZ26] Bui, H., Naprienko, S., Pratt, K., and Zaharescu, A. Binomial coefficients with
>     divisors avoiding an interval. arXiv:2605.21221 (2026).

*Quoted from [FormalConjectures/ErdosProblems/387.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/387.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/387](https://www.erdosproblems.com/387).

The file states 4 research or textbook statements: 1 open and 3 solved.

## `Erdos387.erdos_387`

Solved: stated here without proof.

> Is there an absolute constant $c > 0$ such that, for all $1 \leq k < n$, the binomial coefficient
> $\binom{n}{k}$ has a divisor in $(cn, n]$?
>
> Bui, Naprienko, Pratt, and Zaharescu [BNPZ26] answered this negatively.

```lean
theorem erdos_387 : ¬ ∃ c : ℝ, 0 < c ∧ ∀ n k : ℕ, 1 ≤ k → k < n →
    ∃ d : ℕ, (d : ℝ) ∈ Set.Ioc (c * n) n ∧ d ∣ n.choose k
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/387.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/387.lean#L52).

## `Erdos387.erdos_387.variants.schinzel`

Open: stated without proof.

> The following is Schinzel's conjecture, which appears in [Gu04].

```lean
theorem erdos_387.variants.schinzel :
    ∀ᶠ k in atTop, ¬ IsPrimePow k → ∃ n : ℕ, ∀ i < k, ¬ n - i ∣ n.choose k
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/387.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/387.lean#L62).

## `Erdos387.erdos_387.variants.easy`

Proved here.

> It is easy to see that `n.choose k` has a divisor in `[n / k, n]`.

```lean
theorem erdos_387.variants.easy {n : ℕ} {k : ℕ} (hn : 1 ≤ n) (hk : k ≤ n) : ∃ d : ℕ,
    (d : ℝ) ∈ Set.Icc (n / k : ℝ) n ∧ d ∣ n.choose k
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/387.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/387.lean#L68).

## `Erdos387.erdos_387.variants.guy`

Solved: stated here without proof.

> Is it true for any $c < 1$ and all $n$ sufficiently large, for all $1 \leq k < n$,
> $\binom{n}{k}$ has a divisor in $(cn, n]$?
>
> This variant appears in [Gu04]. Bui, Naprienko, Pratt, and Zaharescu [BNPZ26] answered it
> negatively.

```lean
theorem erdos_387.variants.guy : ¬ ∀ c : ℝ, c < 1 → ∀ᶠ n : ℕ in atTop, ∀ k : ℕ, 1 ≤ k →
    k < n → ∃ d : ℕ, (d : ℝ) ∈ Set.Ioc (c * n) n ∧ d ∣ n.choose k
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/387.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/387.lean#L88).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/387.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/387.lean)
- [erdosproblems.com/387](https://www.erdosproblems.com/387)
