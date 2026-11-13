---
declaration: theorem
origin: cited
lean: Erdos934.erdos_934, Erdos934.erdos_934.variants.h_one, Erdos934.erdos_934.variants.h_two, Erdos934.erdos_934.variants.h_three_three, Erdos934.erdos_934.variants.upper, Erdos934.erdos_934.variants.lower_large_t, Erdos934.erdos_934.variants.kmp_h_three_four, Erdos934.erdos_934.variants.ccjk_conjecture_false, Erdos934.erdos_934.variants.kmp_liminf, Erdos934.erdos_934.variants.lower_liminf
statement: formalized
---

# Erdős Problem 934

> *References:*
> - [erdosproblems.com/934](https://www.erdosproblems.com/934)
> - [Er88] Erdős, P., *Problems and results in combinatorial analysis and graph theory*.
>   Discrete Math. 72 (1988), 81-92.
> - [BBPP83] Bermond, J.-C., Bond, J., Paoli, M. and Peyrat, C., *Graphs and interconnection
>   networks: diameter and vulnerability*. Surveys in Combinatorics (Southampton, 1983), London Math.
>   Soc. Lecture Note Ser. 82, Cambridge Univ. Press (1983), 1-30.
> - [CGTT90] Chung, F. R. K., Gyárfás, A., Tuza, Z. and Trotter, W. T., *The maximum number of
>   edges in $2K_2$-free graphs of bounded degree*. Discrete Math. 81 (1990), 129-135.
> - [CCJK22] Cambie, S., Cames van Batenburg, W., de Joannis de Verclos, R. and Kang, R. J.,
>   *Maximising line subgraphs of diameter at most $t$*. SIAM J. Discrete Math. 36 (2022),
>   939-950. [arXiv:2103.11898](https://arxiv.org/abs/2103.11898)
> - [KMP26] Kumar, H., Mohar, B. and Pragada, S., *An improved bound for the strong clique index
>   of graphs*. [arXiv:2607.02698](https://arxiv.org/abs/2607.02698) (2026).
> - [CvBK26] Cames van Batenburg, W. and Korsky, S., *Asymptotically attaining the Moore bound*.
>   [arXiv:2608.03965](https://arxiv.org/abs/2608.03965) (2026).

*Quoted from [FormalConjectures/ErdosProblems/934.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/934.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/934](https://www.erdosproblems.com/934).

The file states 10 research or textbook statements: 1 open and 9 solved. It also has 1 API statement, counted here but not shown.

## `Erdos934.erdos_934`

Open: stated without proof.

> Let $h_t(d)$ be minimal such that every graph $G$ with $h_t(d)$ edges and maximal degree
> $\leq d$ contains two edges whose shortest path between them has length $\geq t$.
>
> Estimate $h_t(d)$.
>
> A problem of Erdős and Nešetřil [Er88]. Erdős wrote 'This problem seems to be interesting only
> if there is a nice expression for $h_t(d)$.' We read "estimate" as asking for an exact
> expression, as in that remark: `h t d = erdos_934.answer t d` for all `1 ≤ t` and all `d`.

```lean
theorem erdos_934 : ∀ t d : ℕ, 1 ≤ t → h t d = erdos_934.answer t d
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/934.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/934.lean#L91).

## `Erdos934.erdos_934.variants.h_one`

Solved: stated here without proof.

> It is easy to see that $h_t(d)\leq 2d^t$ always and $h_1(d)=d+1$.
>
> The site (and [CCJK22, p. 1]) states $h_1(d)=d+1$ without restriction; it fails for $d=2$ (the
> triangle has three pairwise intersecting edges, so $h_1(2)=4$), hence we assume $d\neq 2$.

```lean
theorem erdos_934.variants.h_one : ∀ d : ℕ, d ≠ 2 → h 1 d = d + 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/934.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/934.lean#L101).

## `Erdos934.erdos_934.variants.h_two`

Solved: stated here without proof.

> Erdős and Nešetřil and Bermond, Bond, Paoli, and Peyrat [BBPP83] independently conjectured that
> $h_2(d) \leq \tfrac{5}{4}d^2+1$, with equality for even $d$. This was proved by Chung, Gyárfás,
> Tuza, and Trotter [CGTT90].

```lean
theorem erdos_934.variants.h_two :
    (∀ d : ℕ, 4 * h 2 d ≤ 5 * d ^ 2 + 4) ∧
      ∀ d : ℕ, Even d → 4 * h 2 d = 5 * d ^ 2 + 4
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/934.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/934.lean#L110).

## `Erdos934.erdos_934.variants.h_three_three`

Solved: stated here without proof.

> Cambie, Cames van Batenburg, de Joannis de Verclos, and Kang [CCJK22, Theorem 2] proved that $h_3(3)=23$.

```lean
theorem erdos_934.variants.h_three_three : h 3 3 = 23
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/934.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/934.lean#L119).

## `Erdos934.erdos_934.variants.upper`

Solved: stated here without proof.

> The same authors prove that for all $t\geq 1$ we have
>
> $$h_t(d) \leq \tfrac{3}{2}d^t+1.$$
>
> See [CCJK22, Theorem 6]. Here the inequality is stated as `2 * h t d ≤ 3 * d ^ t + 2`.

```lean
theorem erdos_934.variants.upper :
    ∀ t d : ℕ, 1 ≤ t → 2 * h t d ≤ 3 * d ^ t + 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/934.lean, line 128](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/934.lean#L128).

## `Erdos934.erdos_934.variants.lower_large_t`

Solved: stated here without proof.

> The same authors prove that, if $t$ is large, then there are infinitely many $d$ such that
> $h_t(d) \geq 0.629^td^t$. See [CCJK22, Proposition 5].

```lean
theorem erdos_934.variants.lower_large_t :
    ∃ t₀ : ℕ, ∀ t : ℕ, t₀ ≤ t →
      ∃ᶠ d : ℕ in atTop, ((629 : ℝ) / 1000) ^ t * (d : ℝ) ^ t ≤ (h t d : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/934.lean, line 137](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/934.lean#L137).

## `Erdos934.erdos_934.variants.kmp_h_three_four`

Solved: stated here without proof.

> Cambie, Cames van Batenburg, de Joannis de Verclos, and Kang [CCJK22] conjectured that
> $h_3(d) \leq d^3-d^2+d+2$ (with equality if $d-1$ is a prime power; the site writes "if and only
> if", while [CCJK22, Conjecture 1] says "if"). Kumar, Mohar and Pragada [KMP26, Lemma 3.1]
> refute the inequality: the odd graph $KG(7,3)$ has $35$ vertices, is $4$-regular, has $70$ edges
> and any two of its edges are at distance less than $3$, so $h_3(4)\geq 71 > 54$.

```lean
theorem erdos_934.variants.kmp_h_three_four : 71 ≤ h 3 4
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/934.lean, line 150](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/934.lean#L150).

## `Erdos934.erdos_934.variants.ccjk_conjecture_false`

Solved: stated here without proof.

> The inequality $h_3(d) \leq d^3-d^2+d+2$ conjectured in [CCJK22] is false [KMP26, Conjecture 1.9
> and Lemma 3.1]. Here the inequality is stated as `h 3 d + d ^ 2 ≤ d ^ 3 + d + 2`.

```lean
theorem erdos_934.variants.ccjk_conjecture_false :
    ¬ ∀ d : ℕ, h 3 d + d ^ 2 ≤ d ^ 3 + d + 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/934.lean, line 158](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/934.lean#L158).

## `Erdos934.erdos_934.variants.kmp_liminf`

Solved: stated here without proof.

> Kumar, Mohar and Pragada [KMP26, Theorem 1.11] proved
>
> $$\liminf_{d\to\infty}\frac{h_3(d)}{d^3}\geq \frac{253}{225}.$$
>
> In particular the conjecture of [CCJK22] that $h_t(d)\leq (1+o(1))d^t$ is false for $t=3$.

```lean
theorem erdos_934.variants.kmp_liminf :
    ∀ ε > (0 : ℝ), ∀ᶠ d : ℕ in atTop, (253 / 225 - ε) * (d : ℝ) ^ 3 ≤ (h 3 d : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/934.lean, line 168](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/934.lean#L168).

## `Erdos934.erdos_934.variants.lower_liminf`

Solved: stated here without proof.

> For every fixed $t\geq 2$, $\liminf_{d\to\infty} h_t(d)/d^t \geq 1$ [CvBK26, Corollary 1.2]. This
> confirms, in a strong form, the conjecture of [CCJK22] that $h_t(d)\geq (1-o(1))d^t$ for
> infinitely many $d$.

```lean
theorem erdos_934.variants.lower_liminf :
    ∀ t : ℕ, 2 ≤ t → ∀ ε > (0 : ℝ), ∀ᶠ d : ℕ in atTop,
      (1 - ε) * (d : ℝ) ^ t ≤ (h t d : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/934.lean, line 178](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/934.lean#L178).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/934.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/934.lean)
- [erdosproblems.com/934](https://www.erdosproblems.com/934)
