---
declaration: theorem
origin: cited
lean: Erdos241.erdos_241, Erdos241.erdos_241.variants.lower_bound, Erdos241.erdos_241.variants.upper_bound, Erdos241.erdos_241.variants.upper_bound_white, Erdos241.erdos_241.variants.generalization, Erdos241.erdos_241.variants.r_eq_2
statement: formalized
---

# Erdős Problem 241

> *References:*
> - [erdosproblems.com/30](https://www.erdosproblems.com/30)
> - [erdosproblems.com/241](https://www.erdosproblems.com/241)
> - [BoCh62] Bose, R. C. and Chowla, S., Theorems in the additive theory of numbers. Comment. Math.
>   Helv. (1962/63), 141-147.
> - [Gr01] Green, Ben, The number of squares and {$B_h[g]$} sets. Acta Arith. (2001), 365-390.
> - [Gu04] Guy, Richard K., Unsolved problems in number theory. (2004), xviii+437.
> - [Wh24] White, Ethan Patrick, An optimal $L^2$ autoconvolution inequality. Canad. Math. Bull.
>   67 (2024), 108-121. [doi:10.4153/S0008439523000565](https://doi.org/10.4153/S0008439523000565)

*Quoted from [FormalConjectures/ErdosProblems/241.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/241.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/241](https://www.erdosproblems.com/241).

The file states 6 research or textbook statements: 2 open and 4 solved.

## `Erdos241.erdos_241`

Open: stated without proof.

> Is it true that $f(N)\sim N^{1/3}$?
>
> Originally asked to Erdős by Bose.
>
> This is discussed in problem C11 of Guy's collection [Gu04].

```lean
theorem erdos_241 :
    (fun N ↦ (f N 3 : ℝ)) ~[atTop] (fun N ↦ (N : ℝ) ^ ((1 : ℝ) / 3))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/241.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/241.lean#L64).

## `Erdos241.erdos_241.variants.lower_bound`

Solved: stated here without proof.

> Bose and Chowla [BoCh62] provided a construction proving one half of this, namely
> $(1+o(1))N^{1/3}\leq f(N)$.

```lean
theorem erdos_241.variants.lower_bound :
    ∃ ε : ℕ → ℝ, ε =o[atTop] (fun _ ↦ (1 : ℝ)) ∧
    ∀ᶠ N in atTop, (1 + ε N) * (N : ℝ) ^ ((1 : ℝ) / 3) ≤ (f N 3 : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/241.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/241.lean#L73).

## `Erdos241.erdos_241.variants.upper_bound`

Solved: stated here without proof.

> Green [Gr01] proved the upper bound $f(N) \leq ((7/2)^{1/3}+o(1))N^{1/3}$
> (note that $(7/2)^{1/3}\approx 1.519$).

```lean
theorem erdos_241.variants.upper_bound :
    ∃ ε : ℕ → ℝ, ε =o[atTop] (fun _ ↦ (1 : ℝ)) ∧
    ∀ᶠ N in atTop, (f N 3 : ℝ) ≤ ((7 / 2 : ℝ) ^ ((1 : ℝ) / 3) + ε N) * (N : ℝ) ^ ((1 : ℝ) / 3)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/241.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/241.lean#L83).

## `Erdos241.erdos_241.variants.upper_bound_white`

Solved: stated here without proof.

> Green's argument gives $f(N) \leq ((2/\mu_2^2)^{1/3}+o(1))N^{1/3}$, where
> $\mu_2^2 = \inf \lVert g \ast g \rVert_2^2$ over $g \colon [-1/2,1/2] \to \mathbb{R}$ with
> $\int g = 1$; Green used $\mu_2^2 \geq 4/7$. White [Wh24, Theorem 1 and Corollary 2] proved
> $0.574636066 \leq \mu_2^2 \leq 0.574642912$, which gives the best upper bound known to date,
> $f(N) \leq ((2/0.574636066)^{1/3}+o(1))N^{1/3}$ (note that $(2/0.574636066)^{1/3}\approx 1.5155$).

```lean
theorem erdos_241.variants.upper_bound_white :
    ∃ ε : ℕ → ℝ, ε =o[atTop] (fun _ ↦ (1 : ℝ)) ∧
    ∀ᶠ N in atTop, (f N 3 : ℝ) ≤
      ((2 / 0.574636066 : ℝ) ^ ((1 : ℝ) / 3) + ε N) * (N : ℝ) ^ ((1 : ℝ) / 3)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/241.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/241.lean#L96).

## `Erdos241.erdos_241.variants.generalization`

Open: stated without proof.

> More generally, Bose and Chowla [BoCh62] conjectured that the maximum size of
> $A\subseteq \{1,\ldots,N\}$ with all $r$-fold sums distinct (aside from the trivial coincidences)
> then $\lvert A\rvert \sim N^{1/r}.$

```lean
theorem erdos_241.variants.generalization (r : ℕ) (hr : r ≥ 2) :  BoseChowlaConjecture r
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/241.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/241.lean#L114).

## `Erdos241.erdos_241.variants.r_eq_2`

Solved: stated here without proof.

> This is known only for $r=2$ (see [erdosproblems.com/30]).

```lean
theorem erdos_241.variants.r_eq_2 :
    BoseChowlaConjecture 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/241.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/241.lean#L121).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/241.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/241.lean)
- [erdosproblems.com/241](https://www.erdosproblems.com/241)
