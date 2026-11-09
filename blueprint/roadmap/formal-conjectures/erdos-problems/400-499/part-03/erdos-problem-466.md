---
declaration: theorem
origin: cited
lean: Erdos466.erdos_466, Erdos466.erdos_466.variants.graham, Erdos466.erdos_466.variants.sarkozy
statement: formalized
---

# Erdős Problem 466

> *References:*
> - [erdosproblems.com/466](https://www.erdosproblems.com/466)
> - [Er72] Erdős, Paul, *Extremal problems in number theory*. Proceedings of the 1972 Number Theory
>   Conference (Univ. Colorado, Boulder, Colo.) (1972), 80-86.
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [Er82e] Erdős, Paul, *Some of my favourite problems which recently have been solved*. (1982),
>   59-79.
> - [Sa76] Sárközy, A., *On distances near integers. I, II*. Studia Sci. Math. Hungar. (1976), 37-50,
>   105-111.

*Quoted from [FormalConjectures/ErdosProblems/466.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/466.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/466](https://www.erdosproblems.com/466).

The file states 3 research or textbook statements: 3 solved.

## `Erdos466.erdos_466`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos466.lean#L292](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos466.lean#L292).

> Let $N(X,\delta)$ denote the maximum number of points $P_1,\ldots,P_n$ which can be chosen in a
> circle of radius $X$ such that
>
> $$\| \lvert P_i-P_j\rvert \| \geq \delta$$
>
> for all $1\leq i\lt j\leq n$. (Here $\|x\|$ is the distance from $x$ to the nearest integer.)
>
> Is there some $\delta>0$ such that
>
> $$\lim_{X\to \infty}N(X,\delta)=\infty?$$
>
> Graham proved this is true, and in fact $N(X,1/10)> \frac{\log X}{10}$. This was substantially
> improved by Sárközy [Sa76], who proved that for all sufficiently small $\delta>0$,
> $N(X,\delta)>X^{1/2-\delta^{1/7}}$.

```lean
theorem erdos_466 : ∃ δ : ℝ, 0 < δ ∧ Tendsto (fun X ↦ N X δ) atTop atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/466.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/466.lean#L66).

## `Erdos466.erdos_466.variants.graham`

Solved: stated here without proof.

> Graham proved that $N(X,1/10)> \frac{\log X}{10}$.

```lean
theorem erdos_466.variants.graham : ∀ X : ℝ, 1 ≤ X → Real.log X / 10 < N X (1 / 10)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/466.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/466.lean#L71).

## `Erdos466.erdos_466.variants.sarkozy`

Solved: stated here without proof.

> Sárközy [Sa76] proved that for all sufficiently small $\delta>0$,
> $N(X,\delta)>X^{1/2-\delta^{1/7}}$ for all sufficiently large $X$.

```lean
theorem erdos_466.variants.sarkozy : ∃ δ₀ : ℝ, 0 < δ₀ ∧ ∀ δ : ℝ, 0 < δ → δ < δ₀ →
    ∀ᶠ X : ℝ in atTop, X ^ (1 / 2 - δ ^ (1 / 7 : ℝ)) < N X δ
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/466.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/466.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/466.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/466.lean)
- [erdosproblems.com/466](https://www.erdosproblems.com/466)
