---
declaration: theorem
origin: cited
lean: Erdos1013.erdos_1013.parts.i, Erdos1013.erdos_1013.parts.ii, Erdos1013.erdos_1013.variants.graver_yackel, Erdos1013.erdos_1013.variants.lower, Erdos1013.erdos_1013.variants.upper
statement: formalized
---

# Erdős Problem 1013

> *References:*
> - [erdosproblems.com/1013](https://www.erdosproblems.com/1013)
> - [Er71] Erdős, P., *Some unsolved problems in graph theory and combinatorial analysis*.
>   Combinatorial Mathematics and its Applications (Proc. Conf., Oxford, 1969) (1971), 97-109.
> - [GrYa68] Graver, J. E. and Yackel, J., *Some graph theoretic results associated with Ramsey's
>   theorem*. J. Combinatorial Theory 4 (1968), 125-175.
> - [DaIl22] Davies, E. and Illingworth, F., *The $\chi$-Ramsey problem for triangle-free graphs*.
>   SIAM J. Discrete Math. 36 (2022), 1124-1134.
> - [HHKP25] Hefty, Z., Horn, P., King, D. and Pfender, F., *Improving $R(3,k)$ in just two bites*.
>   [arXiv:2510.19718](https://arxiv.org/abs/2510.19718) (2025).

*Quoted from [FormalConjectures/ErdosProblems/1013.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1013.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1013](https://www.erdosproblems.com/1013).

The file states 5 research or textbook statements: 2 open and 3 solved. It also has 1 test statement and 1 API statement, counted here but not shown.

## `Erdos1013.erdos_1013.parts.i`

Open: stated without proof.

> Let $h_3(k)$ be the minimal $n$ such that there exists a triangle-free graph on $n$ vertices with
> chromatic number $k$. Find an asymptotic for $h_3(k)$, and also prove
>
> $$\lim_{k\to \infty}\frac{h_3(k+1)}{h_3(k)}=1.$$
>
> This is the first part.

```lean
theorem erdos_1013.parts.i :
    (fun k ↦ (h3 k : ℝ)) ~[atTop] erdos_1013.parts.i.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1013.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1013.lean#L69).

## `Erdos1013.erdos_1013.parts.ii`

Open: stated without proof.

> Let $h_3(k)$ be the minimal $n$ such that there exists a triangle-free graph on $n$ vertices with
> chromatic number $k$. Find an asymptotic for $h_3(k)$, and also prove
>
> $$\lim_{k\to \infty}\frac{h_3(k+1)}{h_3(k)}=1.$$
>
> This is the second part.

```lean
theorem erdos_1013.parts.ii :
    Tendsto (fun k : ℕ ↦ (h3 (k + 1) : ℝ) / h3 k) atTop (nhds 1)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1013.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1013.lean#L81).

## `Erdos1013.erdos_1013.variants.graver_yackel`

Solved: stated here without proof.

> Graver and Yackel [GrYa68] proved
>
> $$h_3(k)\gg \frac{\log k}{\log\log k}k^2.$$

```lean
theorem erdos_1013.variants.graver_yackel :
    ∃ c > (0 : ℝ), ∀ᶠ k : ℕ in atTop,
      c * (Real.log k / Real.log (Real.log k)) * k ^ 2 ≤ (h3 k : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1013.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1013.lean#L90).

## `Erdos1013.erdos_1013.variants.lower`

Solved: stated here without proof.

> The upper bound $f(n) \leq (2+o(1))(n/\log n)^{1/2}$ of Davies and Illingworth [DaIl22] for the
> function $f$ of [1104] gives
>
> $$\left(\frac{1}{2}-o(1)\right)k^2\log k\leq h_3(k).$$

```lean
theorem erdos_1013.variants.lower :
    ∀ ε > (0 : ℝ), ∀ᶠ k : ℕ in atTop,
      (1 / 2 - ε) * k ^ 2 * Real.log k ≤ (h3 k : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1013.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1013.lean#L101).

## `Erdos1013.erdos_1013.variants.upper`

Solved: stated here without proof.

> The lower bound $f(n) \geq (1-o(1))(n/\log n)^{1/2}$ for the function $f$ of [1104], which follows
> from the construction of Hefty, Horn, King, and Pfender [HHKP25], gives
>
> $$h_3(k) \leq (2+o(1))k^2\log k.$$
>
> The site states $(1+o(1))k^2\log k$, but the bounds recorded in [1104] give only $2+o(1)$.

```lean
theorem erdos_1013.variants.upper :
    ∀ ε > (0 : ℝ), ∀ᶠ k : ℕ in atTop,
      (h3 k : ℝ) ≤ (2 + ε) * k ^ 2 * Real.log k
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1013.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1013.lean#L113).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1013.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1013.lean)
- [erdosproblems.com/1013](https://www.erdosproblems.com/1013)
