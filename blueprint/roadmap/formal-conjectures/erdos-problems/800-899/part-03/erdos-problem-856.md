---
declaration: theorem
origin: cited
lean: Erdos856.erdos_856, Erdos856.erdos_856.variants.erdos_upper, Erdos856.erdos_856.variants.tang_zhang_lower, Erdos856.erdos_856.variants.tang_zhang_three_lower, Erdos856.erdos_856.variants.tang_zhang_three_upper
statement: formalized
---

# Erdős Problem 856

> *References:*
> - [erdosproblems.com/856](https://www.erdosproblems.com/856)
> - [Er70] Erdős, P., *Some extremal problems in combinatorial number theory*. Mathematical Essays
>   Dedicated to A. J. Macintyre (1970), 123-133. [PDF](https://www.renyi.hu/~p_erdos/1970-21.pdf)
> - [TaZh25b] Tang, Q. and Zhang, S., *Harmonic LCM patterns and sunflower-free capacity*.
>   [arXiv:2512.20055](https://arxiv.org/abs/2512.20055) (2025).
>
> The problem is closely related to the sunflower problem
> [erdosproblems.com/857](https://www.erdosproblems.com/857). The version with natural density in
> place of the harmonic sum is [erdosproblems.com/536](https://www.erdosproblems.com/536).

*Quoted from [FormalConjectures/ErdosProblems/856.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/856.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/856](https://www.erdosproblems.com/856).

The file states 5 research or textbook statements: 1 open and 4 solved. It also has 1 test statement and 1 API statement, counted here but not shown.

## `Erdos856.erdos_856`

Open: stated without proof.

> Let $k\geq 3$ and $f_k(N)$ be the maximum value of $\sum_{n\in A}\frac{1}{n}$, where $A$ ranges
> over all subsets of $\{1,\ldots,N\}$ which contain no subset of size $k$ with the same pairwise
> least common multiple.
>
> Estimate $f_k(N)$.
>
> This is the question of Erdős [Er70, p. 127]. We read "estimate" as
> $f_k(N) = \Theta(\text{answer})$ as $N \to \infty$, for each fixed $k$.

```lean
theorem erdos_856 (k : ℕ) (hk : 3 ≤ k) :
    f k =Θ[atTop] erdos_856.answer k
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/856.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/856.lean#L87).

## `Erdos856.erdos_856.variants.erdos_upper`

Solved: stated here without proof.

> Erdős [Er70, p. 127] notes that
>
> $$f_k(N) \ll \frac{\log N}{\log\log N}.$$
>
> The implied constant depends on $k$.

```lean
theorem erdos_856.variants.erdos_upper (k : ℕ) (hk : 3 ≤ k) :
    ∃ C > (0 : ℝ), ∀ᶠ N : ℕ in atTop, f k N ≤ C * (Real.log N / Real.log (Real.log N))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/856.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/856.lean#L98).

## `Erdos856.erdos_856.variants.tang_zhang_lower`

Solved: stated here without proof.

> Tang and Zhang [TaZh25b, Theorem 1.2] proved that, for fixed $k\geq 3$ and as $N\to\infty$,
>
> $$f_k(N) \geq (\log N)^{c_k - o(1)}, \qquad c_k = \frac{k-2}{e\,((k-2)!)^{1/(k-2)}}.$$
>
> The $o(1)$ is stated with an arbitrary $\varepsilon > 0$.

```lean
theorem erdos_856.variants.tang_zhang_lower (k : ℕ) (hk : 3 ≤ k) (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ N : ℕ in atTop, Real.log N ^ (tangZhangExponent k - ε) ≤ f k N
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/856.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/856.lean#L114).

## `Erdos856.erdos_856.variants.tang_zhang_three_lower`

Solved: stated here without proof.

> Tang and Zhang [TaZh25b, Corollary 1.7] proved, as $N\to\infty$,
>
> $$(\log N)^{\log(1.551)-o(1)}\leq f_3(N)\ll(\log N)^{\frac{3}{2^{2/3}}-1+o(1)}.$$
>
> This is the lower bound, with the $o(1)$ stated with an arbitrary $\varepsilon > 0$. Since
> $\log(1.551) = 0.4389\ldots$, it implies the site's $(\log N)^{0.438}\leq f_3(N)$ for large $N$.

```lean
theorem erdos_856.variants.tang_zhang_three_lower (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ N : ℕ in atTop, Real.log N ^ (Real.log 1.551 - ε) ≤ f 3 N
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/856.lean, line 126](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/856.lean#L126).

## `Erdos856.erdos_856.variants.tang_zhang_three_upper`

Solved: stated here without proof.

> Tang and Zhang [TaZh25b, Corollary 1.7] proved, as $N\to\infty$,
>
> $$(\log N)^{\log(1.551)-o(1)}\leq f_3(N)\ll(\log N)^{\frac{3}{2^{2/3}}-1+o(1)}.$$
>
> This is the upper bound, with the $o(1)$ and the implied constant absorbed into an arbitrary
> $\varepsilon > 0$. The site rounds the exponent to $0.889$, but $\frac{3}{2^{2/3}}-1=0.8898\ldots$.

```lean
theorem erdos_856.variants.tang_zhang_three_upper (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ N : ℕ in atTop, f 3 N ≤ Real.log N ^ (3 / (2 : ℝ) ^ ((2 : ℝ) / 3) - 1 + ε)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/856.lean, line 138](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/856.lean#L138).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/856.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/856.lean)
- [erdosproblems.com/856](https://www.erdosproblems.com/856)
