---
declaration: theorem
origin: cited
lean: ColossallyAbundantNumber.alaoglu_erdos_colossally_abundant_prime_ratio_conjecture, ColossallyAbundantNumber.alaoglu_erdos_prime_powers_rational_conjecture, ColossallyAbundantNumber.infinite_colossallyAbundant, ColossallyAbundantNumber.alaoglu_erdos_prime_or_semiprime_ratio, ColossallyAbundantNumber.encard_colossallyAbundant_maximizers_le_four
statement: formalized
---

# Alaoglu–Erdős Conjectures on Colossally Abundant Numbers

> On Wikipedia and in [OEIS A004490](https://oeis.org/A004490) ($2, 6, 12, 60, 120, 360, \dots$), an
> integer $n > 1$ is called *colossally abundant* when some $\varepsilon > 0$ satisfies
> $\sigma_1(n) / n^{1+\varepsilon} \ge \sigma_1(k) / k^{1+\varepsilon}$ for every $k > 1$. In their
> 1944 introduction [AE44, p. 448], Alaoglu and Erdős instead required $\ge$ for $1 \le m < n$ and
> strict $>$ for $m > n$, selecting the greatest maximizer at $\varepsilon$. By contrast, the
> inequalities on [AE44, p. 455] and the prime-exponent formula of [AE44, Theorem 10, p. 455] (where
> $[x]$ denotes the largest integer $< x$) select the least maximizer ($>$ for $1 \le m < n$ and
> $\ge$ for $m > n$, formalized as `IsAlaogluErdosColossallyAbundant` below), which defines the same
> set as $\varepsilon > 0$ varies. Alaoglu and Erdős [AE44] predicted that consecutive colossally
> abundant integers always differ by a prime factor, reducing this claim to showing that
> $p^x, q^x \in \mathbb{Q}$ with distinct primes $p \ne q$ forces $x \in \mathbb{Z}$ (cf.
> `Exponentials.four_exponentials_conjecture`). Combined with the six exponentials theorem of Lang
> [La66] and Ramachandra [Ra68] (communicated for prime bases by Siegel in [AE44, p. 455]), [AE44]
> yields unconditionally that consecutive [AE44] colossally abundant integers have prime or
> squarefree-semiprime ratio, and that at most four integers $n > 1$ share any maximizer exponent
> $\varepsilon > 0$ (studied further by Erdős and Nicolas [EN75]).
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Colossally_abundant_number)
> - [AE44] L. Alaoglu and P. Erdős (1944), Trans. Amer. Math. Soc. **56**, 448–469.
> - [La66] S. Lang (1966), *Introduction to Transcendental Numbers*, Addison-Wesley, Reading, Mass.
> - [Ra68] K. Ramachandra (1968), Acta Arith. **14**, 65–72, 73–88.
> - [EN75] P. Erdős and J.-L. Nicolas (1975), Bull. Soc. Math. France **103**, 65–90.

*Quoted from [FormalConjectures/Wikipedia/ColossallyAbundantNumber.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ColossallyAbundantNumber.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 2 open and 3 solved. It also has 2 test statements and 3 API statements, counted here but not shown.

## `ColossallyAbundantNumber.alaoglu_erdos_colossally_abundant_prime_ratio_conjecture`

Open: stated without proof.

> **Alaoglu–Erdős Prime-Ratio Conjecture** [AE44]: whenever $m < n$ satisfy
> `AreConsecutiveColossallyAbundant m n`, $n = p m$ for some prime $p$.

```lean
theorem alaoglu_erdos_colossally_abundant_prime_ratio_conjecture (m n : ℕ)
    (h : AreConsecutiveColossallyAbundant m n) :
    ∃ p : ℕ, p.Prime ∧ n = p * m
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ColossallyAbundantNumber.lean, line 172](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ColossallyAbundantNumber.lean#L172).

## `ColossallyAbundantNumber.alaoglu_erdos_prime_powers_rational_conjecture`

Open: stated without proof.

> **Alaoglu–Erdős Rational Prime-Powers Conjecture** [AE44]: if $p \ne q$ are primes and
> $x \in \mathbb{R}$ satisfies $p^x \in \mathbb{Q}$ and $q^x \in \mathbb{Q}$, then
> $x \in \mathbb{Z}$.

```lean
theorem alaoglu_erdos_prime_powers_rational_conjecture (p q : ℕ) (x : ℝ)
    (hp : p.Prime) (hq : q.Prime) (hpq : p ≠ q)
    (hr₁ : ∃ r₁ : ℚ, (p : ℝ) ^ x = r₁) (hr₂ : ∃ r₂ : ℚ, (q : ℝ) ^ x = r₂) :
    ∃ k : ℤ, x = k
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ColossallyAbundantNumber.lean, line 181](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ColossallyAbundantNumber.lean#L181).

## `ColossallyAbundantNumber.infinite_colossallyAbundant`

Solved: stated here without proof.

> Infinitely many integers satisfy `IsColossallyAbundant` [AE44].

```lean
theorem infinite_colossallyAbundant :
    {n : ℕ | IsColossallyAbundant n}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ColossallyAbundantNumber.lean, line 189](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ColossallyAbundantNumber.lean#L189).

## `ColossallyAbundantNumber.alaoglu_erdos_prime_or_semiprime_ratio`

Solved: stated here without proof.

> Unconditional prime-or-squarefree-semiprime ratio theorem [AE44, p. 455]: if $m < n$ satisfy
> `AreConsecutiveAlaogluErdosColossallyAbundant m n`, then $n / m$ is either prime or a product of two
> distinct primes (proved via the six exponentials theorem [La66, Ra68]). Varying $\varepsilon > 0$
> yields the same set of integers under `IsAlaogluErdosColossallyAbundant` as under [AE44, p. 448]'s
> greatest-maximizer convention, so both give the same consecutive pairs; some one-sided strict
> tie-breaker is needed, since a four-way tie $n, np, nq, npq$ with primes $p < q$ under two-sided
> non-strict `IsColossallyAbundant` would include consecutive terms $np, nq$ of ratio $q / p$.

```lean
theorem alaoglu_erdos_prime_or_semiprime_ratio (m n : ℕ)
    (h : AreConsecutiveAlaogluErdosColossallyAbundant m n) :
    (∃ p : ℕ, p.Prime ∧ n = p * m) ∨
      ∃ p q : ℕ, p.Prime ∧ q.Prime ∧ p ≠ q ∧ n = p * q * m
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ColossallyAbundantNumber.lean, line 201](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ColossallyAbundantNumber.lean#L201).

## `ColossallyAbundantNumber.encard_colossallyAbundant_maximizers_le_four`

Solved: stated here without proof.

> By the six exponentials theorem [La66, Ra68], for each $\varepsilon > 0$, at most four integers
> $n > 1$ simultaneously maximize $\sigma_1(n) / n^{1+\varepsilon}$ [AE44, EN75].

```lean
theorem encard_colossallyAbundant_maximizers_le_four (ε : ℝ) (hε : 0 < ε) :
    Set.encard {n : ℕ | 1 < n ∧ ∀ k : ℕ, 1 < k →
      (σ 1 k : ℝ) / (k : ℝ) ^ (1 + ε) ≤ (σ 1 n : ℝ) / (n : ℝ) ^ (1 + ε)} ≤ 4
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ColossallyAbundantNumber.lean, line 210](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ColossallyAbundantNumber.lean#L210).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/ColossallyAbundantNumber.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ColossallyAbundantNumber.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Colossally_abundant_number)
