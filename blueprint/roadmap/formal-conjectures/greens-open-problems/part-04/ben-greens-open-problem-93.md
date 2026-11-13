---
declaration: theorem
origin: cited
lean: Green93.green_93, Green93.green_93.variants.konyagin, Green93.green_93.variants.bskk_small, Green93.green_93.variants.bskk_large, Green93.green_93.variants.breuillard_varju
statement: formalized
---

# Ben Green's Open Problem 93

> *References:*
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.93)
> - [BrVa19] Breuillard, E. and Varjú, P. P., *Irreducibility of random polynomials of large
>   degree*. Acta Math. 223 (2019), 195--249. [arXiv:1810.13360](https://arxiv.org/abs/1810.13360)
> - [BSKK23] Bary-Soroker, L., Koukoulopoulos, D. and Kozma, G., *Irreducibility of random
>   polynomials: general measures*. Invent. Math. 233 (2023), 1041--1120.
>   [arXiv:2007.14567](https://arxiv.org/abs/2007.14567)
> - [Ko99] Konyagin, S. V., *On the number of irreducible polynomials with 0,1 coefficients*.
>   Acta Arith. 88 (1999), 333--350.

*Quoted from [FormalConjectures/GreensOpenProblems/93.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/93.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 1 open and 4 solved. It also has 2 API statements, counted here but not shown.

## `Green93.green_93`

Open: stated without proof.

> Is a random polynomial with coefficients in $\{0,1\}$ and nonzero constant term almost surely
> irreducible?
>
> More precisely, writing $p_n$ for the probability that
> $1 + a_1 x + \cdots + a_{n-1} x^{n-1} + x^n$ is irreducible, where the $a_i$ are independent and
> take the values $0$ and $1$ with equal probability, does $p_n \to 1$?
>
> The probability $p_n$ is `irreducibleProb 1 n`. The conjecture is due to Odlyzko and Poonen
> [BrVa19, Section 1].

```lean
theorem green_93 : Tendsto (fun n : ℕ ↦ irreducibleProb 1 n) atTop (𝓝 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/GreensOpenProblems/93.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/93.lean#L99).

## `Green93.green_93.variants.konyagin`

Solved: stated here without proof.

> Konyagin [Ko99] proved that $p_n \ge c / \log n$ for an absolute constant $c > 0$, as stated in
> [BrVa19, Section 1]. We state it for all large $n$. It is superseded by
> `green_93.variants.bskk_small`.

```lean
theorem green_93.variants.konyagin :
    ∃ c : ℝ, 0 < c ∧ ∀ᶠ n : ℕ in atTop, c / Real.log (n : ℝ) ≤ irreducibleProb 1 n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/GreensOpenProblems/93.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/93.lean#L108).

## `Green93.green_93.variants.bskk_small`

Solved: stated here without proof.

> Bary-Soroker, Koukoulopoulos and Kozma [BSKK23, Theorem 1(b)] proved that a random monic
> polynomial of degree $n$ whose coefficients are uniform on $N$ consecutive integers in $[-H, H]$
> with $2 \le N \le 34$, and with nonzero constant term, is irreducible with probability at least
> $\delta$. Here $\delta > 0$ is an absolute constant, and $n$ must be at least an absolute constant
> and at least $(\log H)^3$. We state it for the integers $\{0, 1, \dots, M\}$ with
> $1 \le M \le 33$, so $N = M + 1$ and $H = M$. The condition on $(\log H)^3$ is absorbed into
> $n_0$, because $M$ is bounded. The case $M = 1$ gives $p_n \ge \delta$ for large $n$ for the
> polynomial of `green_93`.

```lean
theorem green_93.variants.bskk_small :
    ∃ δ : ℝ, 0 < δ ∧ ∃ n₀ : ℕ, ∀ M n : ℕ, 1 ≤ M → M ≤ 33 → n₀ ≤ n →
      δ ≤ irreducibleProb M n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/GreensOpenProblems/93.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/93.lean#L123).

## `Green93.green_93.variants.bskk_large`

Solved: stated here without proof.

> Bary-Soroker, Koukoulopoulos and Kozma [BSKK23, Theorem 1(a)] proved that a random monic
> polynomial of degree $n$ whose coefficients are uniform on $N \ge 35$ consecutive integers in
> $[-H, H]$, with nonzero constant term, is irreducible with probability at least $1 - n^{-c}$.
> Here $c > 0$ is an absolute constant, and $n$ must be at least an absolute constant and at least
> $(\log H)^3$. We state it for the integers
> $\{0, 1, \dots, M\}$ with $M \ge 34$, so $N = M + 1 \ge 35$ and $H = M$. In particular
> `irreducibleProb M n` $\to 1$ for each such $M$, which is the analogue of `green_93` for
> coefficients in $\{0, \dots, M\}$.

```lean
theorem green_93.variants.bskk_large :
    ∃ c : ℝ, 0 < c ∧ ∃ n₀ : ℕ, ∀ M n : ℕ, 34 ≤ M → n₀ ≤ n → (Real.log (M : ℝ)) ^ 3 ≤ n →
      1 - (n : ℝ) ^ (-c) ≤ irreducibleProb M n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/GreensOpenProblems/93.lean, line 139](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/93.lean#L139).

## `Green93.green_93.variants.breuillard_varju`

Solved: stated here without proof.

> **Breuillard and Varjú.** Assume the Riemann hypothesis for the Dedekind zeta functions of all
> number fields $\mathbb{Q}(a)$ with $a$ a root of a polynomial with coefficients in $\{0, 1\}$
> (`ZeroOneRootFieldsRH`). Then $p_n \to 1$ [BrVa19, Theorem 1].

```lean
theorem green_93.variants.breuillard_varju :
    ZeroOneRootFieldsRH → Tendsto (fun n : ℕ ↦ irreducibleProb 1 n) atTop (𝓝 1)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/GreensOpenProblems/93.lean, line 163](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/93.lean#L163).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/93.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/93.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.93)
