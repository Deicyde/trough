---
declaration: theorem
origin: cited
lean: Erdos650.erdos_650.parts.i, Erdos650.erdos_650.parts.ii, Erdos650.erdos_650.variants.erdos_suranyi, Erdos650.erdos_650.variants.erdos_selfridge
statement: formalized
---

# Erdős Problem 650

> *References:*
> - [erdosproblems.com/650](https://www.erdosproblems.com/650)
> - [Er78] Erdős, Paul, *Problems and results in combinatorial analysis and combinatorial number
>   theory*. Proceedings of the Ninth Southeastern Conference on Combinatorics, Graph Theory, and
>   Computing (Florida Atlantic Univ., Boca Raton, Fla., 1978) (1978), 29-40.
> - [Er86c] Erdős, P., *Some problems on number theory*. (1986), 53-67.
> - [Er95c] Erdős, Paul, *Some problems in number theory*. Octogon Math. Mag. (1995), 3-5.
> - [ErSu59] Erdős, Pál and Surányi, János, *Bemerkungen zu einer Aufgabe eines mathematischen
>   Wettbewerbs*. Mat. Lapok (1959), 39-48.
> - [VLT26] W. Van Doorn, Y. Li, and Q. Tang, *Optimal bounds for an Erdős problem on matching
>   integers to distinct multiples*. arXiv:2603.28636 (2026).

*Quoted from [FormalConjectures/ErdosProblems/650.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/650.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/650](https://www.erdosproblems.com/650).

The file states 4 research or textbook statements: 4 solved.

## `Erdos650.erdos_650.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/Woett/Lean-files/blob/main/ErdosProblem650.lean](https://github.com/Woett/Lean-files/blob/main/ErdosProblem650.lean).

> Let $f(m)$ be such that if $A\subseteq \{1,\ldots,N\}$ has $\lvert A\rvert=m$ then every interval
> in $[1,\infty)$ of length $2N$ contains $\geq f(m)$ many distinct integers $b_1,\ldots,b_r$ where
> each $b_i$ is divisible by some $a_i\in A$, where $a_1,\ldots,a_r$ are distinct.
>
> Estimate $f(m)$.
>
> GPT 5.4 Pro (prompted by He, Li, and Tang) proved $f(m)\leq \lceil 2\sqrt{m}\rceil$. A
> corresponding lower bound was given by GPT 5.4 Pro and Aristotle; it is now known (see the paper
> of van Doorn, Li, and Tang [VLT26]) that
> $$f(m) = \min(m, \lceil 2\sqrt{m}\rceil)$$
> for all $m$.
>
> This was formalized in Lean by van Doorn using Aristotle.

```lean
theorem erdos_650.parts.i (m : ℕ) : f m = min m ⌈2 * Real.sqrt m⌉₊
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/650.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/650.lean#L67).

## `Erdos650.erdos_650.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/Woett/Lean-files/blob/main/ErdosProblem650.lean](https://github.com/Woett/Lean-files/blob/main/ErdosProblem650.lean).

> Let $f(m)$ be such that if $A\subseteq \{1,\ldots,N\}$ has $\lvert A\rvert=m$ then every interval
> in $[1,\infty)$ of length $2N$ contains $\geq f(m)$ many distinct integers $b_1,\ldots,b_r$ where
> each $b_i$ is divisible by some $a_i\in A$, where $a_1,\ldots,a_r$ are distinct.
>
> In particular is it true that $f(m)\leq \sqrt{m}$?
>
> GPT 5.4 Pro (prompted by He, Li, and Tang) proved $f(m)\leq \lceil 2\sqrt{m}\rceil$. A
> corresponding lower bound was given by GPT 5.4 Pro and Aristotle; it is now known (see the paper
> of van Doorn, Li, and Tang [VLT26]) that
> $$f(m) = \min(m, \lceil 2\sqrt{m}\rceil)$$
> for all $m$.
>
> This was formalized in Lean by van Doorn using Aristotle.

```lean
theorem erdos_650.parts.ii : ¬ ∀ m : ℕ, (f m : ℝ) ≤ Real.sqrt m
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/650.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/650.lean#L88).

## `Erdos650.erdos_650.variants.erdos_suranyi`

Solved: stated here without proof.

> Erdős and Surányi [ErSu59] proved that $f(m)\geq\sqrt{m}$.

```lean
theorem erdos_650.variants.erdos_suranyi (m : ℕ) : Real.sqrt m ≤ (f m : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/650.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/650.lean#L95).

## `Erdos650.erdos_650.variants.erdos_selfridge`

Solved: stated here without proof.

> Erdős and Selfridge proved (see [Er78] and [Er86c]) that $f(m^2)\leq 2m$, which implies
> $f(m)\leq 2\lceil \sqrt{m}\rceil$ for all $m$.

```lean
theorem erdos_650.variants.erdos_selfridge (m : ℕ) : f (m ^ 2) ≤ 2 * m
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/650.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/650.lean#L103).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/650.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/650.lean)
- [erdosproblems.com/650](https://www.erdosproblems.com/650)
