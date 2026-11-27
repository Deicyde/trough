---
declaration: theorem
origin: cited
lean: SkewesNumber.littlewood_pi_minus_li_infinite_sign_changes, SkewesNumber.skewes_crossover_known_bounds, SkewesNumber.skewes_number, SkewesNumber.skewes_number.variants.no_crossover_below_known_region
statement: formalized
---

# Skewes's Number and Sign Changes of $\pi(x) - \operatorname{li}(x)$

> Let $\pi(x)$ count primes up to $x$ and let
> $\operatorname{li}(x) = \operatorname{pv} \int_0^x \frac{dt}{\log t}$ (`Real.logIntegral`) denote
> the Cauchy principal-value logarithmic integral. John Edensor Littlewood (1914) proved that
> $\pi(x) - \operatorname{li}(x)$ reverses sign infinitely often, and Stanley Skewes (1933, 1955)
> established the first explicit upper bounds for a crossover point. Analytic zero-free and
> explicit-formula bounds show $\pi(x) < \operatorname{li}(x)$ for $2 \le x \le 10^{19}$ (Büthe
> 2015), while a crossing region near $e^{727.95133} \approx 1.3972 \times 10^{316}$ was located by
> Bays–Hudson (2000, below $e^{727.95209}$), Saouter–Demichel (2010, below $e^{727.9513468}$), and
> Saouter–Trudgian–Demichel (2015, below $e^{727.95134}$). Determining the least integer $n \ge 2$
> with $\pi(n) > \operatorname{li}(n)$—and whether any crossing precedes the $e^{727.95133}$
> region—remains open.
>
> *References:*
> - [Wikipedia: Skewes's number](https://en.wikipedia.org/wiki/Skewes%27s_number)
> - [Wikipedia](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics#Prime_numbers)
> - J. E. Littlewood, *Sur la distribution des nombres premiers*, C. R. Acad. Sci. **158**
>   (1914), 1869–1872.
> - S. Skewes, *On the difference $\pi(x) - \operatorname{li}(x)$*, J. London Math. Soc. **8**
>   (1933), 277–283.
> - S. Skewes, *On the difference $\pi(x) - \operatorname{li}(x)$ (II)*, Proc. London Math. Soc. (3)
>   **5** (1955), 48–70.
> - C. Bays and R. H. Hudson, *A new bound for the smallest $x$ with $\pi(x) > \operatorname{li}(x)$*,
>   Math. Comp. **69** (2000), no. 231, 1285–1296.
> - Y. Saouter and P. Demichel, *A sharp region where $\pi(x) - \operatorname{li}(x)$ is positive*,
>   Math. Comp. **79** (2010), no. 272, 2395–2405.
> - Y. Saouter, T. Trudgian, and P. Demichel, *A still sharper region where
>   $\pi(x) - \operatorname{li}(x)$ is positive*, Math. Comp. **84** (2015), no. 295, 2433–2446.
> - J. Büthe, *An analytic method for bounding $\psi(x)$*, Math. Comp. **87** (2018), no. 312,
>   1991–2009 (`arXiv:1511.02032`, 2015).

*Quoted from [FormalConjectures/Wikipedia/SkewesNumber.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/SkewesNumber.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 2 open and 2 solved.

## `SkewesNumber.littlewood_pi_minus_li_infinite_sign_changes`

Solved: stated here without proof.

> Littlewood's oscillation theorem (1914): both $\{m \ge 2 \mid \operatorname{li}(m) < \pi(m)\}$ and
> $\{n \ge 2 \mid \pi(n) < \operatorname{li}(n)\}$ are infinite.

```lean
theorem littlewood_pi_minus_li_infinite_sign_changes :
    {m : ℕ | 2 ≤ m ∧ Real.logIntegral (m : ℝ) < (Nat.primeCounting m : ℝ)}.Infinite ∧
      {n : ℕ | 2 ≤ n ∧ (Nat.primeCounting n : ℝ) < Real.logIntegral (n : ℝ)}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/SkewesNumber.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/SkewesNumber.lean#L63).

## `SkewesNumber.skewes_crossover_known_bounds`

Solved: stated here without proof.

> Unconditional bounds on the first Skewes crossover: $\pi(n) < \operatorname{li}(n)$ holds for every
> integer $2 \le n \le 10^{19}$ (Büthe 2015), whereas some integer $2 \le n < e^{727.95134}$
> satisfies $\operatorname{li}(n) < \pi(n)$ (Saouter–Trudgian–Demichel 2015, sharpening Bays–Hudson's
> $e^{727.95209}$ and Saouter–Demichel's $e^{727.9513468}$).

```lean
theorem skewes_crossover_known_bounds :
    (∀ n : ℕ, 2 ≤ n → n ≤ 10 ^ 19 → (Nat.primeCounting n : ℝ) < Real.logIntegral (n : ℝ)) ∧
      (∃ n : ℕ, 2 ≤ n ∧ (n : ℝ) < Real.exp (72795134 / 100000) ∧
        Real.logIntegral (n : ℝ) < (Nat.primeCounting n : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/SkewesNumber.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/SkewesNumber.lean#L75).

## `SkewesNumber.skewes_number`

Open: stated without proof.

> What is Skewes's number, the smallest integer $n \ge 2$ satisfying
> $\pi(n) > \operatorname{li}(n)$? The bound $n \ge 2$ avoids the singularity of $\operatorname{li}$
> at $1$ and $0 = \pi(0) = \operatorname{li}(0)$.

```lean
theorem skewes_number :
    IsLeast {n : ℕ | 2 ≤ n ∧ Real.logIntegral (n : ℝ) < (Nat.primeCounting n : ℝ)}
      skewes_number.answer
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/SkewesNumber.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/SkewesNumber.lean#L89).

## `SkewesNumber.skewes_number.variants.no_crossover_below_known_region`

Open: stated without proof.

> Does $\pi(n) \le \operatorname{li}(n)$ hold for every integer $n \ge 2$ below $e^{727.95132}$, so
> that no crossover precedes the known crossing region near $e^{727.95133}$? The rounded threshold
> $e^{727.95132}$ is a formalization choice lying just below the crossing interval.

```lean
theorem skewes_number.variants.no_crossover_below_known_region :
    ∀ n : ℕ, 2 ≤ n → (n : ℝ) < Real.exp (72795132 / 100000) →
      (Nat.primeCounting n : ℝ) ≤ Real.logIntegral (n : ℝ)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/SkewesNumber.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/SkewesNumber.lean#L100).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/SkewesNumber.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/SkewesNumber.lean)
- [Wikipedia: Skewes's number](https://en.wikipedia.org/wiki/Skewes%27s_number)
