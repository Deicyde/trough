---
declaration: theorem
origin: cited
lean: Erdos787.erdos_787, Erdos787.erdos_787.variants.integers, Erdos787.erdos_787.variants.klarner, Erdos787.erdos_787.variants.choi, Erdos787.erdos_787.variants.sanders, Erdos787.erdos_787.variants.ruzsa, Erdos787.erdos_787.variants.beker
statement: formalized
---

# Erdős Problem 787

> *References:*
> - [erdosproblems.com/787](https://www.erdosproblems.com/787)
> - [Be25] Beker, A., *The Erdős-Moser sum-free set problem via improved bounds for
>   $k$-configurations*. [arXiv:2501.10203](https://arxiv.org/abs/2501.10203) (2025).
> - [Ch71] Choi, S. L. G., *On a combinatorial problem in number theory*.
>   Proc. London Math. Soc. (3) (1971), 629-642.
> - [Er65] Erdős, P., *Extremal problems in number theory*. Proc. Sympos. Pure Math., Vol. VIII
>   (1965), 181-189. [PDF](https://www.renyi.hu/~p_erdos/1965-02.pdf)
> - [Er73] Erdős, P., *Problems and results on combinatorial number theory*. A survey of
>   combinatorial theory (Proc. Internat. Sympos., Colorado State Univ., Fort Collins, Colo.,
>   1971) (1973), 117-138. [PDF](https://www.renyi.hu/~p_erdos/1973-21.pdf)
> - [Ru05] Ruzsa, Imre Z., *Sum-avoiding subsets*. Ramanujan J. (2005), 77-82.
> - [Sa21] Sanders, Tom, *The Erdős-Moser sum-free set problem*. Canad. J. Math. (2021), 63-107.

*Quoted from [FormalConjectures/ErdosProblems/787.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/787.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/787](https://www.erdosproblems.com/787).

The file states 7 research or textbook statements: 1 open and 6 solved. It also has 2 API statements, counted here but not shown.

## `Erdos787.erdos_787`

Open: stated without proof.

> Let $g(n)$ be maximal such that given any set $A\subset \mathbb{R}$ with $\lvert A\rvert=n$ there
> exists some $B\subseteq A$ of size $\lvert B\rvert\geq g(n)$ such that $b_1+b_2\not\in A$ for all
> $b_1\neq b_2\in B$.
>
> Estimate $g(n)$.

```lean
theorem erdos_787 : (fun n ↦ (g ℝ n : ℝ)) =Θ[atTop] erdos_787.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/787.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/787.lean#L95).

## `Erdos787.erdos_787.variants.integers`

Solved: stated here without proof.

> This function was considered by Erdős and Moser. Choi observed that, without loss of generality,
> one can assume that $A\subset \mathbb{Z}$.
>
> Here this means that sets of integers give the same value $g(n)$ as sets of reals.

```lean
theorem erdos_787.variants.integers (n : ℕ) : g ℤ n = g ℝ n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/787.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/787.lean#L105).

## `Erdos787.erdos_787.variants.klarner`

Solved: stated here without proof.

> Klarner proved $g(n) \gg \log n$ (indeed, a greedy construction suffices).

```lean
theorem erdos_787.variants.klarner :
    ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop, c * Real.log n ≤ (g ℝ n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/787.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/787.lean#L112).

## `Erdos787.erdos_787.variants.choi`

Solved: stated here without proof.

> Choi [Ch71] proved $g(n) \ll n^{2/5+o(1)}$.
>
> Here this means that $g(n) \leq n^{2/5+\varepsilon}$ for every $\varepsilon > 0$ and all large $n$,
> as in [Er73, p. 130].

```lean
theorem erdos_787.variants.choi :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop, (g ℝ n : ℝ) ≤ (n : ℝ) ^ (2 / 5 + ε)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/787.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/787.lean#L123).

## `Erdos787.erdos_787.variants.sanders`

Solved: stated here without proof.

> The current best bounds known are
> $$(\log n)^{1+c} \ll g(n) \ll \exp(\sqrt{\log n})$$
> for some constant $c>0$, the lower bound due to Sanders [Sa21] and the upper bound due to
> Ruzsa [Ru05].
>
> This is the lower bound.

```lean
theorem erdos_787.variants.sanders :
    ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop, Real.log n ^ (1 + c) ≤ (g ℝ n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/787.lean, line 136](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/787.lean#L136).

## `Erdos787.erdos_787.variants.ruzsa`

Solved: stated here without proof.

> The current best bounds known are
> $$(\log n)^{1+c} \ll g(n) \ll \exp(\sqrt{\log n})$$
> for some constant $c>0$, the lower bound due to Sanders [Sa21] and the upper bound due to
> Ruzsa [Ru05].
>
> This is the upper bound. [Ru05] proves it in the form $\exp(O(\sqrt{\log n}))$, which is the form
> stated here.

```lean
theorem erdos_787.variants.ruzsa :
    ∃ C > (0 : ℝ), ∀ᶠ n : ℕ in atTop, (g ℝ n : ℝ) ≤ Real.exp (C * Real.sqrt (Real.log n))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/787.lean, line 150](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/787.lean#L150).

## `Erdos787.erdos_787.variants.beker`

Solved: stated here without proof.

> Beker [Be25] has proved
> $$(\log n)^{1+\tfrac{1}{68}+o(1)} \ll g(n).$$
>
> Here this means that $g(n) \geq (\log n)^{1+c}$ for every $c < 1/68$ and all large $n$
> [Be25, Theorem 1.2].

```lean
theorem erdos_787.variants.beker :
    ∀ c : ℝ, 0 < c → c < 1 / 68 → ∀ᶠ n : ℕ in atTop, Real.log n ^ (1 + c) ≤ (g ℝ n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/787.lean, line 162](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/787.lean#L162).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/787.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/787.lean)
- [erdosproblems.com/787](https://www.erdosproblems.com/787)
