---
declaration: theorem
origin: cited
lean: EllipticCurveRank.mordell_weil, EllipticCurveRank.RatEllipticCurve.card_heightLE_div_pow_five_div_six_tensto, EllipticCurveRank.RatEllipticCurve.half_rank_zero_and_half_rank_one, EllipticCurveRank.RatEllipticCurve.avg_rank_lt_0885, EllipticCurveRank.RatEllipticCurve._08375_le_density_rank_zero_one, EllipticCurveRank.RatEllipticCurve._02062_le_density_rank_zero, EllipticCurveRank.RatEllipticCurve.goldfeld_conjecture, EllipticCurveRank.RatEllipticCurve.goldfeld_conjecture.variants.two_le, EllipticCurveRank.RatEllipticCurve.goldfeld_conjecture.variants.squarefree, EllipticCurveRank.RatEllipticCurve.unbounded_rank_conjecture, EllipticCurveRank.RatEllipticCurve.finite_twentyone_lt_finrank, EllipticCurveRank.RatEllipticCurve.rank_height_count_asymptotic, EllipticCurveRank.RatEllipticCurve.twentyone_le_rank_height_count_asymptotic, EllipticCurveRank.RatEllipticCurve.exists_rank_ge_thirtyone, EllipticCurveRank.RatEllipticCurve.exists_rank_ge_thirtytwo, EllipticCurveRank.WeierstrassCurve.thirtyone_le_rank_claudeAlpogeHowell31, EllipticCurveRank.WeierstrassCurve.rank_claudeAlpogeHowell31, EllipticCurveRank.WeierstrassCurve.thirty_le_rank_ranksunbounded30, EllipticCurveRank.WeierstrassCurve.rank_ranksunbounded30, EllipticCurveRank.WeierstrassCurve.twentynine_le_rank_elkiesKlagsbrun29, EllipticCurveRank.WeierstrassCurve.rank_elkiesKlagsbrun29, EllipticCurveRank.WeierstrassCurve.twentyeight_le_rank_elkies28, EllipticCurveRank.WeierstrassCurve.rank_elkies28
statement: formalized
---

# Some conjectures about ranks of elliptic curves over ℚ

> *References:*
> - [PPVW2016] Jennifer Park, Bjorn Poonen, John Voight, and Melanie Matchett Wood.
>     A heuristic for boundedness of ranks of elliptic curves,
>     https://ems.press/journals/jems/articles/16228
> - [BS2013] Manjul Bhargava and Arul Shankar. The average size of the 5-Selmer group of
>    elliptic curves is 6, and the average rank is less than 1, https://arxiv.org/pdf/1312.7859
> - [Goldfeld1979] Dorian Goldfeld. Conjectures on elliptic curves over quadratic fields,
>    Number Theory Carbondale 1979, Lecture Notes in Math. 751, 108-118,
>    https://doi.org/10.1007/BFb0062705
> - [Smith2025] Alexander Smith. The Birch and Swinnerton-Dyer conjecture implies Goldfeld's
>    conjecture, https://arxiv.org/abs/2503.17619
> - [Wikipedia](https://en.wikipedia.org/wiki/Rank_of_an_elliptic_curve)
> - [ICARM](https://elliptic-rank.icarm.cloud/curve/273)
> - [Stoll] Michael Stoll. EllipticCurves, a Lean 4 formalization of the Mordell–Weil theorem
>    and explicit 2-descent, https://github.com/MichaelStollBayreuth/EllipticCurves

*Quoted from [FormalConjectures/Wikipedia/EllipticCurveRank.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 23 research or textbook statements: 12 open, 10 solved and 1 textbook result. It also has 6 test statements and 4 API statements, counted here but not shown.

## `EllipticCurveRank.mordell_weil`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/e58a03a23e0efb40f891f34d3afceca2ce4ccf9b/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L64](https://github.com/mo271/formal-conjectures/blob/e58a03a23e0efb40f891f34d3afceca2ce4ccf9b/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L64).

> The rank of an elliptic curve over a number field is always finite by the Mordell–Weil theorem.
> Consequently, the rank is always finite, so `finrank ℤ E⟮K⟯ = 0` really means that the group of
> rational points is torsion, not that it is of infinite rank.
>
> The proof linked via `formal_proof` is  Michael Stoll's formalization of the Mordell–Weil theorem
> [Stoll]

```lean
theorem mordell_weil {K} [Field K] [NumberField K] [DecidableEq K] (E : Affine K) [E.IsElliptic] :
    Module.Finite ℤ E.Point
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L68).

## `EllipticCurveRank.RatEllipticCurve.card_heightLE_div_pow_five_div_six_tensto`

Textbook result, stated without proof.

> Formula (5.1.1) of [PPVW2016]: The number of elliptic curves over ℚ with naïve height at most
> `H` is asymptotically `2^(4/3)*3^(-3/2)/ζ(10) * H^(5/6)`.

```lean
theorem card_heightLE_div_pow_five_div_six_tensto :
    atTop.Tendsto (fun H ↦ (heightLE H).ncard / (H : ℝ) ^ (5 / 6 : ℝ))
      (𝓝 (2 ^ (4 / 3 : ℝ) * 3 ^ (-3 / 2 : ℝ) / (riemannZeta 10).re))
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L100).

## `EllipticCurveRank.RatEllipticCurve.half_rank_zero_and_half_rank_one`

Open: stated without proof.

> Conjecture by Goldfeld and Katz–Sarnak: if elliptic curves over ℚ are ordered by their
> heights, then 50% of the curves have rank 0 and 50% have rank 1.
> See p. 28 of https://people.maths.bris.ac.uk/~matyd/BSD2011/bsd2011-Bhargava.pdf.

```lean
theorem half_rank_zero_and_half_rank_one (r : ℕ) (hr : r = 0 ∨ r = 1) :
    atTop.Tendsto
      (fun H ↦ ({E ∈ heightLE H | E.rank = r}.ncard / (heightLE H).ncard : ℝ)) (𝓝 (1 / 2))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L109).

## `EllipticCurveRank.RatEllipticCurve.avg_rank_lt_0885`

Solved: stated here without proof.

> Theorem 3 of [BS2013]:
> when elliptic curves over ℚ are ordered by height, their average rank is < .885.

```lean
theorem avg_rank_lt_0885 :
    atTop.limsup (fun H ↦ ((∑ᶠ E : heightLE H, E.1.rank) / (heightLE H).ncard : ℝ)) < 0.885
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L117).

## `EllipticCurveRank.RatEllipticCurve._08375_le_density_rank_zero_one`

Solved: stated here without proof.

> Theorem 4 of [BS2013]:
> when elliptic curves over ℚ are ordered by height, a density of at least 83.75% have
> rank 0 or 1.

```lean
theorem _08375_le_density_rank_zero_one : 0.8375 ≤ atTop.liminf
    fun H ↦ ({E ∈ heightLE H | E.rank = 0 ∨ E.rank = 1}.ncard / (heightLE H).ncard : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 125](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L125).

## `EllipticCurveRank.RatEllipticCurve._02062_le_density_rank_zero`

Solved: stated here without proof.

> Theorem 5 of [BS2013]:
> when elliptic curves over ℚ are ordered by height, a density of at least 20.62% have rank 0.

```lean
theorem _02062_le_density_rank_zero : 0.2062 ≤ atTop.liminf
    fun H ↦ ({E ∈ heightLE H | E.rank = 0}.ncard / (heightLE H).ncard : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 132](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L132).

## `EllipticCurveRank.RatEllipticCurve.goldfeld_conjecture`

Open: stated without proof.

> **Goldfeld's conjecture** ([Goldfeld1979], Conjecture B), in the form stated in the
> introduction of [Smith2025]: when the quadratic twists $E^d$ of an elliptic curve $E$ over
> $\mathbb{Q}$ are ordered by $|d|$, 50% of them have rank $0$ and 50% have rank $1$. See
> `goldfeld_conjecture.variants.two_le` for the remaining case $2 \leq r$.
>
> Goldfeld states the conjecture for the analytic rank of $E^d$, which the Birch and
> Swinnerton-Dyer conjecture predicts is equal to the Mordell–Weil rank used here. Corollary 1.2
> of [Smith2025] proves that the Birch and Swinnerton-Dyer conjecture for the quadratic twist
> family of $E$ implies Goldfeld's conjecture for $E$.

```lean
theorem goldfeld_conjecture (E : RatEllipticCurve) (r : ℕ) (hr : r = 0 ∨ r = 1) :
    atTop.Tendsto
      (fun H ↦ ({d ∈ twistIndexLE H | E.twistRank d = r}.ncard / (twistIndexLE H).ncard : ℝ))
      (𝓝 (1 / 2))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 193](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L193).

## `EllipticCurveRank.RatEllipticCurve.goldfeld_conjecture.variants.two_le`

Solved: stated here without proof.

> **Goldfeld's conjecture** ([Goldfeld1979], Conjecture B), in the form stated in the
> introduction of [Smith2025], in the case $2 \leq r$: a density $0$ of the quadratic twists $E^d$
> of an elliptic curve $E$ over $\mathbb{Q}$ have rank $r$.
>
> For the Mordell–Weil rank used here this is an unconditional theorem: by Theorem 1.1 of
> [Smith2025], $100\%$ of the twists $E^d$ have $2^\infty$-Selmer corank $0$ or $1$, and the
> Mordell–Weil rank is at most the $2^\infty$-Selmer corank (equation (1.1) there), so the twists
> of rank at least $2$ have density $0$. The corresponding statement for the analytic rank is
> open.

```lean
theorem goldfeld_conjecture.variants.two_le (E : RatEllipticCurve) (r : ℕ) (hr : 2 ≤ r) :
    atTop.Tendsto
      (fun H ↦ ({d ∈ twistIndexLE H | E.twistRank d = r}.ncard / (twistIndexLE H).ncard : ℝ))
      (𝓝 0)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 209](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L209).

## `EllipticCurveRank.RatEllipticCurve.goldfeld_conjecture.variants.squarefree`

Open: stated without proof.

> Goldfeld's conjecture with $d$ restricted to squarefree integers, which is how it is usually
> stated informally: 50% of the quadratic twists of $E$ have rank $0$ and 50% have rank $1$. The
> twist $E^d$ only depends on the class of $d$ modulo nonzero rational squares, and the squarefree
> integers are a system of representatives of these classes. (They need not give pairwise
> non-isomorphic curves: if $B = 0$ then $E^{-d} = E^d$.)

```lean
theorem goldfeld_conjecture.variants.squarefree (E : RatEllipticCurve) (r : ℕ)
    (hr : r = 0 ∨ r = 1) :
    atTop.Tendsto
      (fun H ↦ ({d ∈ twistIndexLE H | Squarefree d ∧ E.twistRank d = r}.ncard /
        {d ∈ twistIndexLE H | Squarefree d}.ncard : ℝ))
      (𝓝 (1 / 2))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 221](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L221).

## `EllipticCurveRank.RatEllipticCurve.unbounded_rank_conjecture`

Open: stated without proof.

> From [PPVW2016], Section 3.1: "from the mid-1960s to the present,
> it seems that most experts conjectured unboundedness."

```lean
theorem unbounded_rank_conjecture (n : ℕ) : ∃ E : RatEllipticCurve, n ≤ E.rank
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 232](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L232).

## `EllipticCurveRank.RatEllipticCurve.finite_twentyone_lt_finrank`

Open: stated without proof.

> From [PPVW2016], Section 8.2:
> "Our heuristic predicts (a) All but finitely many E ∈ ℰ satisfy rk E(ℚ) ≤ 21".
> In other words, there are only finitely many elliptic curves over ℚ (up to isomorphism)
> with rank greater than 21.
> Notice that this contradicts the previous conjecture.

```lean
theorem finite_twentyone_lt_finrank : {E : RatEllipticCurve | 21 < E.rank}.Finite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 241](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L241).

## `EllipticCurveRank.RatEllipticCurve.rank_height_count_asymptotic`

Open: stated without proof.

> [PPVW2016] 8.2(b): for 1 ≤ r ≤ 20, the number of elliptic curves over ℚ with rank at least
> `r` and naïve height at most `H` is asymptotically `H ^ ((21 - r) / 24 + o(1))`.
> Note: ℰ_H in 8.2(b) should be ℰ_{≤H}, see the statement of Theorem 7.3.3.
> When `r = 1`, the exponent is `20 / 24 = 5 / 6`, which agrees with the exponent in
> `card_heightLE_div_pow_five_div_six_tensto` and is consistent with
> `half_rank_zero_and_half_rank_one`.
> The equality is asserted only for large `H`, matching the `o(1)` above: it cannot hold
> at small `H`, because `heightLE H` is empty for `H ≤ 3` (`naiveHeight E ≤ 3` forces
> `A = B = 0`, which both `Δ_ne_zero` and `reduced` exclude) and consists only of the two
> rank-zero curves `y² = x³ ± x` for `4 ≤ H ≤ 26`, while the right hand side is
> `Real.rpow` and hence strictly positive.

```lean
theorem rank_height_count_asymptotic (r : ℕ) (h₁ : 1 ≤ r) (h₂ : r ≤ 20) :
    ∃ f : ℕ → ℝ, atTop.Tendsto f (𝓝 0) ∧
      ∀ᶠ H : ℕ in atTop,
        {E ∈ heightLE H | r ≤ E.rank}.ncard = (H : ℝ) ^ ((21 - r) / 24 + f H)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 256](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L256).

## `EllipticCurveRank.RatEllipticCurve.twentyone_le_rank_height_count_asymptotic`

Open: stated without proof.

> [PPVW2016] 8.2(c): the number of elliptic curves over ℚ with rank ≥ 21 and naïve height
> at most `H` is asymptotically at most `H ^ o(1)`.

```lean
theorem twentyone_le_rank_height_count_asymptotic :
    ∃ f : ℕ → ℝ, atTop.Tendsto f (𝓝 0) ∧
      ∀ H : ℕ, 1 < H → {E ∈ heightLE H | 21 ≤ E.rank}.ncard ≤ (H : ℝ) ^ f H
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 265](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L265).

## `EllipticCurveRank.RatEllipticCurve.exists_rank_ge_thirtyone`

Solved: stated here without proof.

> Is there an elliptic curve over ℚ of rank at least 31?
>
> The answer is yes: such a curve was found by Claude, Levent Alpöge and Ava Howell in 2026.
> See https://elliptic-rank.icarm.cloud/curve/302 and `WeierstrassCurve.claudeAlpogeHowell31`
> below.

```lean
theorem exists_rank_ge_thirtyone : ∃ E : RatEllipticCurve, 31 ≤ E.rank
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 276](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L276).

## `EllipticCurveRank.RatEllipticCurve.exists_rank_ge_thirtytwo`

Open: stated without proof.

> Is there an elliptic curve over ℚ of rank at least 32?
> The largest known rank of an elliptic curve over ℚ as of 2026 is at least 31 (and exactly
> 31 assuming the generalized Riemann hypothesis and Birch and Swinnerton-Dyer conjecture).
> See https://elliptic-rank.icarm.cloud/curve/302.

```lean
theorem exists_rank_ge_thirtytwo : ∃ E : RatEllipticCurve, 32 ≤ E.rank
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 284](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L284).

## `EllipticCurveRank.WeierstrassCurve.thirtyone_le_rank_claudeAlpogeHowell31`

Solved: stated here without proof.

> The rank of the Claude–Alpöge–Howell curve is at least 31.

```lean
theorem thirtyone_le_rank_claudeAlpogeHowell31 : 31 ≤ finrank ℤ claudeAlpogeHowell31.Point
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 321](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L321).

## `EllipticCurveRank.WeierstrassCurve.rank_claudeAlpogeHowell31`

Open: stated without proof.

> The rank of the Claude–Alpöge–Howell curve is exactly 31.
> It has rank exactly 31 assuming the generalized Riemann hypothesis and the
> Birch and Swinnerton-Dyer conjecture.

```lean
theorem rank_claudeAlpogeHowell31 : finrank ℤ claudeAlpogeHowell31.Point = 31
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 329](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L329).

## `EllipticCurveRank.WeierstrassCurve.thirty_le_rank_ranksunbounded30`

Solved: stated here without proof.

> The rank of the ranksunbounded curve is at least 30.

```lean
theorem thirty_le_rank_ranksunbounded30 : 30 ≤ finrank ℤ ranksunbounded30.Point
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 357](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L357).

## `EllipticCurveRank.WeierstrassCurve.rank_ranksunbounded30`

Open: stated without proof.

> The rank of the ranksunbounded curve is exactly 30.

```lean
theorem rank_ranksunbounded30 : finrank ℤ ranksunbounded30.Point = 30
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 362](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L362).

## `EllipticCurveRank.WeierstrassCurve.twentynine_le_rank_elkiesKlagsbrun29`

Solved: stated here without proof.

> The rank of the Elkies-Klagsbrun curve is at least 29.

```lean
theorem twentynine_le_rank_elkiesKlagsbrun29 : 29 ≤ finrank ℤ elkiesKlagsbrun29.Point
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 389](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L389).

## `EllipticCurveRank.WeierstrassCurve.rank_elkiesKlagsbrun29`

Open: stated without proof.

> The rank of the Elkies-Klagsbrun curve is exactly 29.

```lean
theorem rank_elkiesKlagsbrun29 : finrank ℤ elkiesKlagsbrun29.Point = 29
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 394](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L394).

## `EllipticCurveRank.WeierstrassCurve.twentyeight_le_rank_elkies28`

Solved: stated here without proof.

> The rank of the Elkies curve is at least 28.

```lean
theorem twentyeight_le_rank_elkies28 : 28 ≤ finrank ℤ elkies28.Point
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 420](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L420).

## `EllipticCurveRank.WeierstrassCurve.rank_elkies28`

Open: stated without proof.

> The rank of the Elkies curve is exactly 28.

```lean
theorem rank_elkies28 : finrank ℤ elkies28.Point = 28
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/EllipticCurveRank.lean, line 425](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean#L425).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/EllipticCurveRank.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EllipticCurveRank.lean)
- [https://ems.press/journals/jems/articles/16228](https://ems.press/journals/jems/articles/16228)
