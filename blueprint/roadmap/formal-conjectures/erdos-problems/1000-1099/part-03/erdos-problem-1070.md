---
declaration: theorem
origin: cited
lean: Erdos1070.erdos_1070.parts.i, Erdos1070.erdos_1070.parts.ii, Erdos1070.erdos_1070.variants.moser_spindle, Erdos1070.erdos_1070.variants.matolcsi_ruzsa_varga_zsamboki_graphs, Erdos1070.erdos_1070.variants.matolcsi_ruzsa_varga_zsamboki
statement: formalized
---

# Erdős Problem 1070

> *References:*
> - [erdosproblems.com/1070](https://www.erdosproblems.com/1070)
> - [DuVa26] Dúcz, Á. and Varga, D., *A unit-distance graph in the plane with independence ratio
>   below 1/4*. [arXiv:2606.28157](https://arxiv.org/abs/2606.28157) (2026).
> - [Er87b] Erdős, P., *Some combinatorial and metric problems in geometry*.
>   Intuitive geometry (Siófok, 1985) (1987), 167-177.
>   [PDF](https://www.renyi.hu/~p_erdos/1987-27.pdf)
> - [MRVZ23] Matolcsi, M., Ruzsa, I. Z., Varga, D. and Zsámboki, P., *The fractional chromatic
>   number of the plane is at least $4$*. [arXiv:2311.10069](https://arxiv.org/abs/2311.10069)
>   (2023).
>
> If we also insist that no two points are distance $<1$ apart, we get
> [erdosproblems.com/1066](https://www.erdosproblems.com/1066).

*Quoted from [FormalConjectures/ErdosProblems/1070.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1070.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1070](https://www.erdosproblems.com/1070).

The file states 5 research or textbook statements: 1 open, 3 solved and 1 textbook result. It also has 1 API statement, counted here but not shown.

## `Erdos1070.erdos_1070.parts.i`

Open: stated without proof.

> Let $f(n)$ be maximal such that, given any $n$ points in $\mathbb{R}^2$, there exist $f(n)$ points
> such that no two are distance $1$ apart. Estimate $f(n)$. In particular, is it true that
> $f(n)\geq n/4$?
>
> This is the first part, a problem of Erdős [Er87b, p. 171]. Since $f(n)=\Theta(n)$ is already
> known, we ask for $\lim f(n)/n$. The limit exists by Fekete's lemma, since placing two
> configurations far apart shows $f(a+b) \leq f(a)+f(b)$.

```lean
theorem erdos_1070.parts.i :
    Tendsto (fun n : ℕ ↦ (f n : ℝ) / n) atTop (𝓝 erdos_1070.parts.i.answer)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1070.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1070.lean#L75).

## `Erdos1070.erdos_1070.parts.ii`

Solved: stated here without proof.

> Let $f(n)$ be maximal such that, given any $n$ points in $\mathbb{R}^2$, there exist $f(n)$ points
> such that no two are distance $1$ apart. Estimate $f(n)$. In particular, is it true that
> $f(n)\geq n/4$?
>
> This is the second part, read as the inequality for every $n$. The answer is no: Dúcz and Varga
> [DuVa26, Theorem 1] construct a finite unit distance graph $G$ in the plane with
> $\alpha(G) < |V(G)|/4$. For its vertex set $X$, `f_le X` gives
> $f(|X|) \leq \alpha(U_X) \leq \alpha(G) < |X|/4$, where $U_X$ is the unit distance graph on $X$.

```lean
theorem erdos_1070.parts.ii : ¬ ∀ n : ℕ, (n : ℝ) / 4 ≤ (f n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1070.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1070.lean#L90).

## `Erdos1070.erdos_1070.variants.moser_spindle`

Textbook result, stated without proof.

> The Moser spindle shows $f(n)\leq \frac{2}{7}n\approx 0.285n$.
>
> The Moser spindle has $7$ points and independence number $2$, so $m$ far-apart copies give the
> bound for $n=7m$.

```lean
theorem erdos_1070.variants.moser_spindle (m : ℕ) : f (7 * m) ≤ 2 * m
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1070.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1070.lean#L100).

## `Erdos1070.erdos_1070.variants.matolcsi_ruzsa_varga_zsamboki_graphs`

Solved: stated here without proof.

> Matolcsi, Ruzsa, Varga, and Zsámboki [MRVZ23, Section 3, after Theorem 2] showed that for every
> $\varepsilon>0$ there is a finite unit distance graph $G\subseteq\mathbb{R}^2$ whose largest
> independent set has size at most $(1/4+\varepsilon)|G|$.

```lean
theorem erdos_1070.variants.matolcsi_ruzsa_varga_zsamboki_graphs :
    ∀ ε > (0 : ℝ), ∃ X : Finset ℝ², X.Nonempty ∧
      ((UnitDistancePlaneGraph (X : Set ℝ²)).indepNum : ℝ) ≤ (1 / 4 + ε) * X.card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1070.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1070.lean#L109).

## `Erdos1070.erdos_1070.variants.matolcsi_ruzsa_varga_zsamboki`

Solved: stated here without proof.

> Matolcsi, Ruzsa, Varga, and Zsámboki [MRVZ23] have improved the upper bound to
> $$f(n) \leq \left(\frac{1}{4}+o(1)\right)n.$$
>
> This follows from the previous statement by taking disjoint copies of the graph far apart.

```lean
theorem erdos_1070.variants.matolcsi_ruzsa_varga_zsamboki :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop, (f n : ℝ) ≤ (1 / 4 + ε) * n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1070.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1070.lean#L121).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1070.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1070.lean)
- [erdosproblems.com/1070](https://www.erdosproblems.com/1070)
