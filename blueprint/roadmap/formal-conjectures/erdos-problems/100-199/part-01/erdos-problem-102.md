---
declaration: theorem
origin: cited
lean: Erdos102.erdos_102, Erdos102.erdos_102.variants.five, Erdos102.erdos_102.variants.upper_sqrt, Erdos102.erdos_102.variants.hunter
statement: formalized
---

# Erdős Problem 102

> *Reference:* [erdosproblems.com/102](https://www.erdosproblems.com/102)

*Quoted from [FormalConjectures/ErdosProblems/102.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/102.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/102](https://www.erdosproblems.com/102).

The file states 4 research or textbook statements: 2 open and 2 solved. It also has 4 API statements, counted here but not shown.

## `Erdos102.erdos_102`

Open: stated without proof.

> Let $c > 0$ and let $h_c(n)$ be such that for any $n$ points in $\mathbb{R}^2$ with at least
> $cn^2$ lines that each contain more than three of the points, some line contains $h_c(n)$ of
> the points. Is it true that, for fixed $c > 0$, $h_c(n) \to \infty$?

```lean
theorem erdos_102 :
    ∀ c > 0, ∀ M : ℕ, ∀ᶠ n in atTop, (M : ℕ∞) ≤ h c n
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/102.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/102.lean#L116).

## `Erdos102.erdos_102.variants.five`

Open: stated without proof.

> It is not known whether $h_c(n) \geq 5$ for all sufficiently large $n$.

```lean
theorem erdos_102.variants.five :
    ∀ c > 0, ∀ᶠ n in atTop, (5 : ℕ∞) ≤ h c n
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/102.lean, line 124](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/102.lean#L124).

## `Erdos102.erdos_102.variants.upper_sqrt`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/eee8e904a0eb8511302bc809b9486116ec079e69/Proofs/T_Erdos102_erdos_102_variants_upper_sqrt.lean#L1100](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/eee8e904a0eb8511302bc809b9486116ec079e69/Proofs/T_Erdos102_erdos_102_variants_upper_sqrt.lean#L1100).

> It is easy to see that $h_c(n) \ll_c n^{1/2}$: for all sufficiently small $c > 0$ there are
> admissible configurations (e.g. grids) in which no line contains more than $C_c n^{1/2}$ points.

```lean
theorem erdos_102.variants.upper_sqrt :
    ∃ c₀ > (0 : ℝ), ∀ c ∈ Set.Ioc 0 c₀, ∃ C : ℝ, ∀ᶠ n in atTop,
      h c n ≤ (⌈C * Real.sqrt n⌉₊ : ℕ∞)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/102.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/102.lean#L134).

## `Erdos102.erdos_102.variants.hunter`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/eee8e904a0eb8511302bc809b9486116ec079e69/Proofs/T_Erdos102_erdos_102_variants_hunter.lean#L1113](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/eee8e904a0eb8511302bc809b9486116ec079e69/Proofs/T_Erdos102_erdos_102_variants_hunter.lean#L1113).

> Erdős [Er95] suggested that perhaps $h_c(n) \gg_c n^{1/2}$. Zach Hunter pointed out that this is
> false: the points of $\{1, \dots, m\}^d$ with $n \approx m^d$, randomly projected to
> $\mathbb{R}^2$, meet every line in $\ll_d n^{1/d}$ points and determine $\gg_d n^2$ lines with
> more than three points. This gives $h_c(n) \ll n^{1 / \log(1/c)}$; we state the underlying form:
> for every $d \geq 1$ there is $c > 0$ with $h_c(n) \ll_d n^{1/d}$.

```lean
theorem erdos_102.variants.hunter :
    ∀ d : ℕ, 1 ≤ d → ∃ c > (0 : ℝ), ∃ C : ℝ, ∀ᶠ n in atTop,
      h c n ≤ (⌈C * (n : ℝ) ^ (1 / (d : ℝ))⌉₊ : ℕ∞)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/102.lean, line 148](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/102.lean#L148).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/102.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/102.lean)
- [erdosproblems.com/102](https://www.erdosproblems.com/102)
