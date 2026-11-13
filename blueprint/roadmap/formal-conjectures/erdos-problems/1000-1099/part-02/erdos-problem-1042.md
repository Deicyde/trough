---
declaration: theorem
origin: cited
lean: Erdos1042.erdos_1042.parts.i, Erdos1042.erdos_1042.variants.chebyshev_segment, Erdos1042.erdos_1042.variants.universal, Erdos1042.erdos_1042.parts.ii, Erdos1042.erdos_1042.variants.connected_le_quarter
statement: formalized
---

# Erdős Problem 1042

> *References:*
> - [erdosproblems.com/1042](https://www.erdosproblems.com/1042)
> - [EHP58] Erdős, P. and Herzog, F. and Piranian, G., *Metric properties of polynomials*.
>   J. Analyse Math. (1958), 125-148. [PDF](https://www.renyi.hu/~p_erdos/1958-05.pdf)
> - [GhRa24] Ghosh, S. and Ramachandran, K., *Number of components of polynomial lemniscates: a
>   problem of Erdős, Herzog, and Piranian*. J. Math. Anal. Appl. (2024), Paper No. 128571.
>   [arXiv:2312.13673](https://arxiv.org/abs/2312.13673)

*Quoted from [FormalConjectures/ErdosProblems/1042.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1042.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1042](https://www.erdosproblems.com/1042).

The file states 5 research or textbook statements: 1 open and 4 solved.

## `Erdos1042.erdos_1042.parts.i`

Solved: stated here without proof.

> Let $F\subset\mathbb{C}$ be a closed set of transfinite diameter $1$ which is not contained in
> any closed disc of radius $1$.
>
> If $f(z)=\prod_{i=1}^n(z-z_i)\in\mathbb{C}[x]$ with all $z_i\in F$ then can
>
> $$\{ z: \lvert f(z)\rvert < 1\}$$
>
> have $n$ connected components?
>
> A problem of Erdős, Herzog, and Piranian [EHP58, p. 139, Problem 6], who proved that if $F$ is the
> disc of radius $1$ then this set can have $n$ connected components (for example $f(z)=z^n+1$).
>
> As in the answer of Ghosh and Ramachandran [GhRa24] to their Question 1.2, we read "can"
> existentially: there is such an $F$ for which $n$ components occur for infinitely many $n$.
> [GhRa24] answer this question in the affirmative; the classical example $F=[-2,2]$
> [GhRa24, Example 2.7] already gives $n$ components for every $n\ge 1$, see
> `erdos_1042.variants.chebyshev_segment`. The universal reading, for every such $F$, is
> `erdos_1042.variants.universal`.

```lean
theorem erdos_1042.parts.i :
    ∃ F : Set ℂ, IsClosed F ∧ transfiniteDiameter F = 1 ∧
      (∀ c : ℂ, ¬ F ⊆ Metric.closedBall c 1) ∧
      ∃ᶠ n : ℕ in atTop, ∃ f : ℂ[X], MonicWithRootsIn F n f ∧ numComponents f = n
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1042.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1042.lean#L88).

## `Erdos1042.erdos_1042.variants.chebyshev_segment`

Solved: stated here without proof.

> Ghosh and Ramachandran [GhRa24, Example 2.7] note that for $F=[-2,2]\subset\mathbb{C}$ (a closed
> set of transfinite diameter $1$ which is not contained in any closed disc of radius $1$) the
> monic Chebyshev polynomial $f_n(z)=2T_n(z/2)$ has all its roots in $F$ and all its $n-1$ critical
> values equal to $\pm 2$, so $\{\lvert f_n\rvert<1\}$ has exactly $n$ components, for every
> $n\ge 1$.

```lean
theorem erdos_1042.variants.chebyshev_segment (F : Set ℂ)
    (hF : F = Complex.ofReal '' Set.Icc (-2 : ℝ) 2) :
    IsClosed F ∧ transfiniteDiameter F = 1 ∧ (∀ c : ℂ, ¬ F ⊆ Metric.closedBall c 1) ∧
      ∀ n : ℕ, 1 ≤ n → ∃ f : ℂ[X], MonicWithRootsIn F n f ∧ numComponents f = n
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1042.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1042.lean#L102).

## `Erdos1042.erdos_1042.variants.universal`

Open: stated without proof.

> The first question of [EHP58, p. 139, Problem 6] read universally: for every closed $F$ of
> transfinite diameter $1$ which is not contained in any closed disc of radius $1$, are there
> infinitely many $n$ for which some $f$ with all roots in $F$ gives $n$ components?
>
> This is not settled by [GhRa24], who prove it for closed lemniscates [GhRa24, Proposition 2.3]
> and conjecture the weaker statement $\limsup_n C_n(F)/n=1$ for every compact $F$ of capacity $1$
> [GhRa24, §2.1.1]. "Some $n$" instead of infinitely many would be trivial ($n=1$).

```lean
theorem erdos_1042.variants.universal :
    ∀ F : Set ℂ, IsClosed F → transfiniteDiameter F = 1 →
      (∀ c : ℂ, ¬ F ⊆ Metric.closedBall c 1) →
      ∃ᶠ n : ℕ in atTop, ∃ f : ℂ[X], MonicWithRootsIn F n f ∧ numComponents f = n
```

Category `research open`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1042.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1042.lean#L118).

## `Erdos1042.erdos_1042.parts.ii`

Solved: stated here without proof.

> If the transfinite diameter of $F$ is $<1$ then must this set only have at most $(1-c)n$
> connected components, where $c>0$ depends only on $F$ (or just the transfinite diameter of $F$)?
>
> This is the second question of [EHP58, p. 139, Problem 6], which asks for $n$ large. It was solved
> by Ghosh and Ramachandran [GhRa24, Theorem 2.1(a)], who proved that, if $d$ is the transfinite
> diameter of $F$ and $0\lt d<1$, then the set has at most $(1-c)n$ connected components for some
> $c>0$ depending on $F$. Precisely, they prove $\limsup_n C_n(F)/n<1$, where $C_n(F)$ is the
> maximal number of components over all admissible $f$ of degree $n$; this is the statement below.
> The answer is yes, in this form.
>
> [GhRa24] assume throughout that $F$ is compact of positive capacity, so we assume $0\lt d$; a closed
> $F$ with $d<1$ is bounded, hence compact. The condition "$n$ large" is needed: for $n=1$ the set
> $\{\lvert z-z_1\rvert<1\}$ has one component, which is more than $(1-c)n$. The parenthetical
> "or just the transfinite diameter of $F$" is not formalised: [GhRa24] only remark that their
> quantities $M(K)$ and $m(K)$ are not determined by the capacity.

```lean
theorem erdos_1042.parts.ii :
    ∀ F : Set ℂ, IsClosed F → 0 < transfiniteDiameter F → transfiniteDiameter F < 1 →
      ∃ c : ℝ, 0 < c ∧ ∀ᶠ n : ℕ in atTop, ∀ f : ℂ[X], MonicWithRootsIn F n f →
        (numComponents f : ℝ) ≤ (1 - c) * n
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1042.lean, line 142](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1042.lean#L142).

## `Erdos1042.erdos_1042.variants.connected_le_quarter`

Solved: stated here without proof.

> If $d\leq 1/4$ and $F$ is connected then the set has only one connected component.
>
> This is [GhRa24, Theorem 2.1(c)]: if the logarithmic capacity of the compact connected set $K$ is
> at most $1/4$ then $\{\lvert f\rvert<1\}$ is connected for every monic $f$ with all roots in $K$.
> We take the degree $n\ge 1$ (for $n=0$ the set is empty) and, as in [GhRa24], positive capacity.

```lean
theorem erdos_1042.variants.connected_le_quarter (F : Set ℂ) (hF : IsClosed F)
    (hconn : IsConnected F) (h₀ : 0 < transfiniteDiameter F) (hd : transfiniteDiameter F ≤ 1 / 4)
    (n : ℕ) (hn : 1 ≤ n) (f : ℂ[X]) (hf : MonicWithRootsIn F n f) :
    numComponents f = 1
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1042.lean, line 156](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1042.lean#L156).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1042.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1042.lean)
- [erdosproblems.com/1042](https://www.erdosproblems.com/1042)
