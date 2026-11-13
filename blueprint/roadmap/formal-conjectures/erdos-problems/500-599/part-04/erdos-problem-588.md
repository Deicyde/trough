---
declaration: theorem
origin: cited
lean: Erdos588.erdos_588, Erdos588.erdos_588.variants.trivial_upper, Erdos588.erdos_588.variants.sylvester, Erdos588.erdos_588.variants.three_lower, Erdos588.erdos_588.variants.three_not_isLittleO, Erdos588.erdos_588.variants.karteszi, Erdos588.erdos_588.variants.grunbaum, Erdos588.erdos_588.variants.solymosi_stojakovic, Erdos588.erdos_588.variants.grunbaum_order
statement: formalized
---

# Erdős Problem 588

> *References:*
> - [erdosproblems.com/588](https://www.erdosproblems.com/588)
> - [BGS74] Burr, Stefan A. and Grünbaum, Branko and Sloane, N. J. A., *The orchard problem*.
>   Geometriae Dedicata (1974), 397-424.
> - [Er84] Erdős, P., *Research problems*. Period. Math. Hungar. (1984), 101-103.
> - [FuPa84] Füredi, Z. and Palásti, I., *Arrangements of lines with a large number of
>   triangles*. Proc. Amer. Math. Soc. (1984), 561-566.
> - [Gr76] Grünbaum, Branko, *New views on some old questions of combinatorial geometry*.
>   Colloquio Internazionale sulle Teorie Combinatorie (Roma, 1973), Tomo I (1976), 451-468.
> - [Ka63] Kárteszi, F., *Sylvester egy tételéről és Erdős egy sejtéséről*. Matematikai Lapok
>   (1963), 3-10.
> - [SoSt13] Solymosi, József and Stojaković, Miloš, *Many collinear $k$-tuples with no $k+1$
>   collinear points*. Discrete Comput. Geom. (2013), 811-820.

*Quoted from [FormalConjectures/ErdosProblems/588.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/588.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/588](https://www.erdosproblems.com/588).

The file states 9 research or textbook statements: 1 open, 7 solved and 1 textbook result.

## `Erdos588.erdos_588`

Open: stated without proof.

> Let $f_k(n)$ be minimal such that if $n$ points in $\mathbb{R}^2$ have no $k+1$ points on a line
> then there must be at most $f_k(n)$ many lines containing at least $k$ points. Is it true that
>
> $$f_k(n) = o(n^2)$$
>
> for $k \geq 4$?
>
> The case $k = 4$ is Erdős Problem 101. The restriction $k \geq 4$ is needed: see
> `Erdos588.erdos_588.variants.three_not_isLittleO`.

```lean
theorem erdos_588 :
    ∀ k : ℕ, 4 ≤ k →
      (fun n : ℕ ↦ (numLinesWithPointsMax k n : ℝ)) =o[atTop] (fun n : ℕ ↦ (n : ℝ) ^ 2)
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/588.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/588.lean#L66).

## `Erdos588.erdos_588.variants.trivial_upper`

Textbook result, stated without proof. A Lean proof is at [https://github.com/veljjanoski/formal-conjectures-proofs/blob/a199537b29d77124f8e1ea0d816a881e96f0cc0f/FcProofs/Erdos588.lean#L81](https://github.com/veljjanoski/formal-conjectures-proofs/blob/a199537b29d77124f8e1ea0d816a881e96f0cc0f/FcProofs/Erdos588.lean#L81).

> The trivial upper bound, by counting pairs of points: for $k \geq 2$,
>
> $$f_k(n) \cdot k(k-1) \leq n(n-1).$$

```lean
theorem erdos_588.variants.trivial_upper (k n : ℕ) (hk : 2 ≤ k) :
    numLinesWithPointsMax k n * (k * (k - 1)) ≤ n * (n - 1)
```

Category `textbook`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/588.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/588.lean#L77).

## `Erdos588.erdos_588.variants.sylvester`

Solved: stated here without proof.

> Sylvester showed (see [BGS74]) that
>
> $$f_3(n) = \frac{n^2}{6} + O(n).$$
>
> The upper bound $f_3(n) \leq n(n-1)/6$ is `Erdos588.erdos_588.variants.trivial_upper` with
> $k = 3$. The lower bound comes from a construction on a cubic curve.

```lean
theorem erdos_588.variants.sylvester :
    (fun n : ℕ ↦ (numLinesWithPointsMax 3 n : ℝ) - (n : ℝ) ^ 2 / 6) =O[atTop]
      (fun n : ℕ ↦ (n : ℝ))
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/588.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/588.lean#L89).

## `Erdos588.erdos_588.variants.three_lower`

Solved: stated here without proof.

> Burr, Grünbaum, and Sloane [BGS74] and Füredi and Palásti [FuPa84] gave constructions which
> show that
>
> $$f_3(n) \geq \left(\frac{1}{6} + o(1)\right) n^2.$$

```lean
theorem erdos_588.variants.three_lower :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      (1 / 6 - ε) * (n : ℝ) ^ 2 ≤ (numLinesWithPointsMax 3 n : ℝ)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/588.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/588.lean#L100).

## `Erdos588.erdos_588.variants.three_not_isLittleO`

Solved: stated here without proof.

> The restriction to $k \geq 4$ in `Erdos588.erdos_588` is necessary: $f_3(n)$ is not $o(n^2)$.
> This follows from `Erdos588.erdos_588.variants.sylvester`.

```lean
theorem erdos_588.variants.three_not_isLittleO :
    ¬ (fun n : ℕ ↦ (numLinesWithPointsMax 3 n : ℝ)) =o[atTop] (fun n : ℕ ↦ (n : ℝ) ^ 2)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/588.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/588.lean#L110).

## `Erdos588.erdos_588.variants.karteszi`

Solved: stated here without proof.

> Kárteszi [Ka63] proved that for $k \geq 4$,
>
> $$f_k(n) \gg_k n \log n,$$
>
> resolving a conjecture of Erdős that $f_k(n)/n \to \infty$.

```lean
theorem erdos_588.variants.karteszi :
    ∀ k : ℕ, 4 ≤ k → ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      c * (n : ℝ) * Real.log (n : ℝ) ≤ (numLinesWithPointsMax k n : ℝ)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/588.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/588.lean#L120).

## `Erdos588.erdos_588.variants.grunbaum`

Solved: stated here without proof.

> Grünbaum [Gr76] proved that for $k \geq 4$,
>
> $$f_k(n) \gg_k n^{1 + \frac{1}{k-2}}.$$

```lean
theorem erdos_588.variants.grunbaum :
    ∀ k : ℕ, 4 ≤ k → ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      c * (n : ℝ) ^ (1 + 1 / ((k : ℝ) - 2)) ≤ (numLinesWithPointsMax k n : ℝ)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/588.lean, line 130](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/588.lean#L130).

## `Erdos588.erdos_588.variants.solymosi_stojakovic`

Solved: stated here without proof.

> Solymosi and Stojaković [SoSt13] proved that for $k \geq 4$,
>
> $$f_k(n) \gg_k n^{2 - O_k(1/\sqrt{\log n})}.$$

```lean
theorem erdos_588.variants.solymosi_stojakovic :
    ∀ k : ℕ, 4 ≤ k → ∃ c > (0 : ℝ), ∃ C > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      c * (n : ℝ) ^ (2 - C / Real.sqrt (Real.log (n : ℝ))) ≤
        (numLinesWithPointsMax k n : ℝ)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/588.lean, line 140](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/588.lean#L140).

## `Erdos588.erdos_588.variants.grunbaum_order`

Solved: stated here without proof.

> Erdős speculated that Grünbaum's bound $n^{1 + \frac{1}{k-2}}$ may be the correct order of
> magnitude of $f_k(n)$ for $k \geq 4$. This is false: by
> `Erdos588.erdos_588.variants.solymosi_stojakovic` [SoSt13], for every $k \geq 4$ we have
> $f_k(n) \neq O(n^{1 + \frac{1}{k-2}})$.

```lean
theorem erdos_588.variants.grunbaum_order :
    ∀ k : ℕ, 4 ≤ k →
      ¬ (fun n : ℕ ↦ (numLinesWithPointsMax k n : ℝ)) =O[atTop]
        (fun n : ℕ ↦ (n : ℝ) ^ (1 + 1 / ((k : ℝ) - 2)))
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/588.lean, line 153](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/588.lean#L153).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/588.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/588.lean)
- [erdosproblems.com/588](https://www.erdosproblems.com/588)
