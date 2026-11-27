---
declaration: theorem
origin: cited
lean: CramerConjecture.cramer_conjecture, CramerConjecture.cramer_conjecture.variants.limsup_eq_one, CramerConjecture.cramer_conjecture.variants.strict_bound, CramerConjecture.cramer_conjecture.variants.granville, CramerConjecture.cramer_conjecture.variants.conditional_rh, CramerConjecture.cramer_conjecture.variants.westzynthius, CramerConjecture.cramer_conjecture.variants.baker_harman_pintz
statement: formalized
---

# Cramér's Conjecture on Prime Gaps

> Write $p_n$ for the $n$-th prime (`Nat.nth Nat.Prime`, with $p_0 = 2$) and $g_n = p_{n+1} - p_n$
> (`primeGap n`). Using an independent random prime heuristic, Harald Cramér [Cr36] conjectured in
> 1936 that $g_n = O((\log p_n)^2)$; his random model further predicts
>
> $$\limsup_{n \to \infty} \frac{p_{n+1} - p_n}{(\log p_n)^2} = 1,$$
>
> while numerical searches also test the strict inequality $g_n < (\log p_n)^2$ for $n \ge 4$
> ($p_n \ge 11$). Accounting for Helmut Maier's short-interval oscillations [Ma85] and small-prime
> sieve factors, Andrew Granville [Gr95] conjectured instead that the limit superior is at least
> $2 e^{-\gamma} \approx 1.1229$ (contradicting $\limsup = 1$). Unconditionally, Baker, Harman, and
> Pintz [BHP01] proved $g_n = O(p_n^{0.525})$. See also `Erdos5`, `Erdos233`, `Andrica`, `Oppermann`,
> and `Firoozbakht` (`Firoozbakht.firoozbakht_conjecture_consequence`).
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_conjecture)
> - [We31] E. Westzynthius (1931), Commentat. Phys.-Math. **5**, no. 25, 1–37.
> - [Cr36] H. Cramér (1936), Acta Arith. **2**, no. 1, 23–46.
> - [Ma85] H. Maier (1985), Michigan Math. J. **32**, no. 2, 221–225.
> - [Gr95] A. Granville (1995), Scand. Actuar. J. **1995**, no. 1, 12–28.
> - [BHP01] R. C. Baker, G. Harman, and J. Pintz (2001), Proc. London Math. Soc. (3) **83**, no. 3,
>   532–562.

*Quoted from [FormalConjectures/Wikipedia/CramerConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/CramerConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 7 research or textbook statements: 4 open and 3 solved. It also has 1 test statement, counted here but not shown.

## `CramerConjecture.cramer_conjecture`

Open: stated without proof.

> **Cramér's Conjecture** [Cr36]: consecutive prime differences satisfy
> $p_{n+1} - p_n = O((\log p_n)^2)$ as $n \to \infty$.

```lean
theorem cramer_conjecture :
    (fun n : ℕ => (primeGap n : ℝ)) =O[Filter.atTop]
      (fun n : ℕ => (Real.log (Nat.nth Nat.Prime n)) ^ 2)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/CramerConjecture.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/CramerConjecture.lean#L92).

## `CramerConjecture.cramer_conjecture.variants.limsup_eq_one`

Open: stated without proof.

> **Cramér's Heuristic Limit-Superior Prediction**: $\limsup_{n \to \infty} g_n / (\log p_n)^2 =
> 1$. Rather than an explicit conjecture in [Cr36], this stronger statement comes from Cramér's
> probabilistic prime model and contradicts `cramer_conjecture.variants.granville`
> ($2 e^{-\gamma} > 1$).

```lean
theorem cramer_conjecture.variants.limsup_eq_one :
    (∀ ε : ℝ, 0 < ε → ∀ᶠ n in Filter.atTop, cramerRatio n ≤ 1 + ε) ∧
      (∀ ε : ℝ, 0 < ε → ∃ᶠ n in Filter.atTop, 1 - ε ≤ cramerRatio n)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/CramerConjecture.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/CramerConjecture.lean#L102).

## `CramerConjecture.cramer_conjecture.variants.strict_bound`

Open: stated without proof.

> **Strong Numerical Cramér Inequality**: for every $n \ge 4$ ($p_n \ge 11$),
> $p_{n+1} - p_n < (\log p_n)^2$ (indices $n \in \{0, 1, 3\}$ fail; see
> `cramerRatio_small_index_bounds`, and compare `Firoozbakht.firoozbakht_conjecture_consequence` for
> the stronger bound $p_{n+1} - p_n < (\log p_n)^2 - \log p_n$ on the same range).

```lean
theorem cramer_conjecture.variants.strict_bound (n : ℕ) (hn : 4 ≤ n) :
    cramerRatio n < 1
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/CramerConjecture.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/CramerConjecture.lean#L112).

## `CramerConjecture.cramer_conjecture.variants.granville`

Open: stated without proof.

> **Cramér–Granville Conjecture** [Gr95]: $\limsup_{n \to \infty} g_n / (\log p_n)^2 \ge
> 2 e^{-\gamma}$, stated without conditional `ℝ`-suprema as infinitely many $n$ satisfying
> $\operatorname{cramerRatio}(n) \ge c$ for each $c < 2 e^{-\gamma}$ (contradicting
> `limsup_eq_one` and `strict_bound`).

```lean
theorem cramer_conjecture.variants.granville (c : ℝ)
    (hc : c < 2 * Real.exp (-Real.eulerMascheroniConstant)) :
    ∃ᶠ n : ℕ in Filter.atTop, c ≤ cramerRatio n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/CramerConjecture.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/CramerConjecture.lean#L121).

## `CramerConjecture.cramer_conjecture.variants.conditional_rh`

Solved: stated here without proof.

> **Cramér's Conditional Prime Gap Bound** [Cr36]: under `RiemannHypothesis`,
> $p_{n+1} - p_n = O(\sqrt{p_n} \log p_n)$.

```lean
theorem cramer_conjecture.variants.conditional_rh (hRH : RiemannHypothesis) :
    (fun n : ℕ => (primeGap n : ℝ)) =O[Filter.atTop]
      (fun n : ℕ => Real.sqrt (Nat.nth Nat.Prime n) * Real.log (Nat.nth Nat.Prime n))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/CramerConjecture.lean, line 129](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/CramerConjecture.lean#L129).

## `CramerConjecture.cramer_conjecture.variants.westzynthius`

Solved: stated here without proof.

> **Westzynthius's Theorem** [We31] (cf. `Erdos5.erdos_5.variants.westzynthius`): for every real
> $M$, infinitely many indices $n$ satisfy $p_{n+1} - p_n \ge M \log p_n$.

```lean
theorem cramer_conjecture.variants.westzynthius (M : ℝ) :
    ∃ᶠ n : ℕ in Filter.atTop,
      M * Real.log (Nat.nth Nat.Prime n : ℝ) ≤ (primeGap n : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/CramerConjecture.lean, line 137](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/CramerConjecture.lean#L137).

## `CramerConjecture.cramer_conjecture.variants.baker_harman_pintz`

Solved: stated here without proof.

> **Baker–Harman–Pintz Bound** [BHP01]: $p_{n+1} - p_n = O(p_n^{0.525})$ as $n \to \infty$.

```lean
theorem cramer_conjecture.variants.baker_harman_pintz :
    (fun n : ℕ => (primeGap n : ℝ)) =O[Filter.atTop]
      (fun n : ℕ => (Nat.nth Nat.Prime n : ℝ) ^ (0.525 : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/CramerConjecture.lean, line 144](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/CramerConjecture.lean#L144).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/CramerConjecture.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/CramerConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_conjecture)
