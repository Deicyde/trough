---
declaration: theorem
origin: cited
lean: Erdos669.erdos_669.parts.i, Erdos669.erdos_669.parts.ii, Erdos669.erdos_669.variants.exactly_le_atLeast, Erdos669.erdos_669.variants.k_two, Erdos669.erdos_669.variants.burr_grunbaum_sloane_exactly, Erdos669.erdos_669.variants.burr_grunbaum_sloane_atLeast, Erdos669.erdos_669.variants.upper_bound, Erdos669.erdos_669.variants.limit_le
statement: formalized
---

# Erdős Problem 669

> *References:*
> - [erdosproblems.com/669](https://www.erdosproblems.com/669)
> - [BGS74] Burr, Stefan A. and Grünbaum, Branko and Sloane, N. J. A., *The orchard problem*.
>   Geometriae Dedicata (1974), 397-424.
> - [Er97f] Erdős, Paul, *Some unsolved problems*. Combinatorics, geometry and probability
>   (Cambridge, 1993) (1997), 1-10.

*Quoted from [FormalConjectures/ErdosProblems/669.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/669.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/669](https://www.erdosproblems.com/669).

The file states 8 research or textbook statements: 2 open and 6 solved. It also has 3 test statements, counted here but not shown.

## `Erdos669.erdos_669.parts.i`

Open: stated without proof.

> Let $F_k(n)$ be minimal such that for any $n$ points in $\mathbb{R}^2$ there exist at most
> $F_k(n)$ many distinct lines passing through at least $k$ of the points, and $f_k(n)$ similarly
> but with lines passing through exactly $k$ points.
>
> Estimate $f_k(n)$ and $F_k(n)$ - in particular, determine $\lim F_k(n)/n^2$ and
> $\lim f_k(n)/n^2$.
>
> This part asks for $\lim F_k(n)/n^2$ for $k \geq 3$ (the case $k = 2$ is trivial). The
> original question [Er97f, Problem 16] asks for the limits "if they exist", so the answer allows
> nonexistence: the answer at $k$ is `some x` if the limit exists and equals $x$, and `none`
> otherwise.

```lean
theorem erdos_669.parts.i :
    ∀ k : ℕ, 3 ≤ k → ∀ x : ℝ,
      erdos_669.parts.i.answer k = some x ↔
        Tendsto (fun n : ℕ => (maxLinesAtLeast k n : ℝ) / (n : ℝ) ^ 2) atTop (𝓝 x)
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/669.lean, line 143](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/669.lean#L143).

## `Erdos669.erdos_669.parts.ii`

Open: stated without proof.

> Let $F_k(n)$ be minimal such that for any $n$ points in $\mathbb{R}^2$ there exist at most
> $F_k(n)$ many distinct lines passing through at least $k$ of the points, and $f_k(n)$ similarly
> but with lines passing through exactly $k$ points.
>
> Estimate $f_k(n)$ and $F_k(n)$ - in particular, determine $\lim F_k(n)/n^2$ and
> $\lim f_k(n)/n^2$.
>
> This part asks for $\lim f_k(n)/n^2$ for $k \geq 3$ (the case $k = 2$ is trivial). The
> original question [Er97f, Problem 16] asks for the limits "if they exist", so the answer allows
> nonexistence: the answer at $k$ is `some x` if the limit exists and equals $x$, and `none`
> otherwise.

```lean
theorem erdos_669.parts.ii :
    ∀ k : ℕ, 3 ≤ k → ∀ x : ℝ,
      erdos_669.parts.ii.answer k = some x ↔
        Tendsto (fun n : ℕ => (maxLinesExactly k n : ℝ) / (n : ℝ) ^ 2) atTop (𝓝 x)
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/669.lean, line 165](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/669.lean#L165).

## `Erdos669.erdos_669.variants.exactly_le_atLeast`

Proved here.

> Trivially $f_k(n)\leq F_k(n)$.

```lean
theorem erdos_669.variants.exactly_le_atLeast (k n : ℕ) :
    maxLinesExactly k n ≤ maxLinesAtLeast k n
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/669.lean, line 175](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/669.lean#L175).

## `Erdos669.erdos_669.variants.k_two`

Solved: stated here without proof.

> $f_2(n)=F_2(n)=\binom{n}{2}$.

```lean
theorem erdos_669.variants.k_two (n : ℕ) :
    maxLinesExactly 2 n = n.choose 2 ∧ maxLinesAtLeast 2 n = n.choose 2
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/669.lean, line 191](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/669.lean#L191).

## `Erdos669.erdos_669.variants.burr_grunbaum_sloane_exactly`

Solved: stated here without proof.

> The problem with $k=3$ is the classical 'Orchard problem' of Sylvester. Burr, Grünbaum, and Sloane
> [BGS74] have proved that
>
> $$f_3(n)=\frac{n^2}{6}-O(n)$$
>
> and
>
> $$F_3(n)=\frac{n^2}{6}-O(n).$$
>
> This is the statement for $f_3$.

```lean
theorem erdos_669.variants.burr_grunbaum_sloane_exactly :
    (fun n : ℕ => (maxLinesExactly 3 n : ℝ) - (n : ℝ) ^ 2 / 6) =O[atTop]
      (fun n : ℕ => (n : ℝ))
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/669.lean, line 205](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/669.lean#L205).

## `Erdos669.erdos_669.variants.burr_grunbaum_sloane_atLeast`

Solved: stated here without proof.

> The problem with $k=3$ is the classical 'Orchard problem' of Sylvester. Burr, Grünbaum, and Sloane
> [BGS74] have proved that
>
> $$f_3(n)=\frac{n^2}{6}-O(n)$$
>
> and
>
> $$F_3(n)=\frac{n^2}{6}-O(n).$$
>
> This is the statement for $F_3$.

```lean
theorem erdos_669.variants.burr_grunbaum_sloane_atLeast :
    (fun n : ℕ => (maxLinesAtLeast 3 n : ℝ) - (n : ℝ) ^ 2 / 6) =O[atTop]
      (fun n : ℕ => (n : ℝ))
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/669.lean, line 220](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/669.lean#L220).

## `Erdos669.erdos_669.variants.upper_bound`

Solved: stated here without proof.

> There is a trivial upper bound of $F_k(n) \leq \binom{n}{2}/\binom{k}{2}$.

```lean
theorem erdos_669.variants.upper_bound (k n : ℕ) (hk : 2 ≤ k) :
    (maxLinesAtLeast k n : ℝ) ≤ (n.choose 2 : ℝ) / (k.choose 2 : ℝ)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/669.lean, line 229](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/669.lean#L229).

## `Erdos669.erdos_669.variants.limit_le`

Solved: stated here without proof.

> There is a trivial upper bound of $F_k(n) \leq \binom{n}{2}/\binom{k}{2}$, and hence
>
> $$\lim F_k(n)/n^2 \leq \frac{1}{k(k-1)}.$$
>
> See also [101](https://www.erdosproblems.com/101).
>
> Here the limit is assumed to exist and is called `L`.

```lean
theorem erdos_669.variants.limit_le (k : ℕ) (hk : 2 ≤ k) (L : ℝ)
    (hL : Tendsto (fun n : ℕ => (maxLinesAtLeast k n : ℝ) / (n : ℝ) ^ 2) atTop (𝓝 L)) :
    L ≤ 1 / ((k : ℝ) * ((k : ℝ) - 1))
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/669.lean, line 241](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/669.lean#L241).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/669.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/669.lean)
- [erdosproblems.com/669](https://www.erdosproblems.com/669)
