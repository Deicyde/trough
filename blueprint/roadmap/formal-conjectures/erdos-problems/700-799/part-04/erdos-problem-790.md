---
declaration: theorem
origin: cited
lean: Erdos790.erdos_790.parts.i, Erdos790.erdos_790.parts.ii, Erdos790.erdos_790.parts.iii, Erdos790.erdos_790.variants.lower_bound, Erdos790.erdos_790.variants.upper_bound, Erdos790.erdos_790.variants.near_linear
statement: formalized
---

# Erdős Problem 790

> *References:*
> - [erdosproblems.com/790](https://www.erdosproblems.com/790)
> - [Er65] Erdős, P., _Extremal problems in number theory_. Proc. Sympos. Pure Math.
>   8 (1965), 181–189, p. 188.
> - [Er73] Erdős, P., _Problems and results on combinatorial number theory_.
>   A Survey of Combinatorial Theory (1973), 117–138, p. 130.
> - [CKS75] Choi, S. L. G., Komlós, J. and Szemerédi, E., _On sum-free subsequences_.
>   Trans. Amer. Math. Soc. 212 (1975), 307–313.
>   [DOI](https://doi.org/10.1090/S0002-9947-1975-0376594-1).

*Quoted from [FormalConjectures/ErdosProblems/790.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/790.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/790](https://www.erdosproblems.com/790).

The file states 6 research or textbook statements: 3 open and 3 solved.

## `Erdos790.erdos_790.parts.i`

Open: stated without proof.

> Let $l(n)$ be maximal such that if $A\subset\mathbb{Z}$ with $\lvert A\rvert=n$
> then there exists a sum-free $B\subseteq A$ with $\lvert B\rvert \geq l(n)$ - that is,
> $B$ is such that there are no solutions to $a_1=a_2+\cdots+a_r$
> with $a_i\in B$ all distinct.
> Estimate $l(n)$.
>
> This is interpreted as asking for the order of growth of $l(n)$.

```lean
theorem erdos_790.parts.i :
    (fun n ↦ (l n : ℝ)) =Θ[atTop] erdos_790.parts.i.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/790.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/790.lean#L67).

## `Erdos790.erdos_790.parts.ii`

Solved: stated here without proof.

> In particular, is it true that $l(n)n^{-1/2}\to\infty$? The lower bound in [CKS75,
> Theorem (1.1)] gives a positive answer.

```lean
theorem erdos_790.parts.ii :
    Tendsto (fun n : ℕ ↦ (l n : ℝ) / Real.sqrt (n : ℝ)) atTop atTop
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/790.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/790.lean#L74).

## `Erdos790.erdos_790.parts.iii`

Open: stated without proof.

> Is it true that $l(n)\lt n^{1-c}$ for some $c>0$?
> The inequality is interpreted as holding for all sufficiently large $n$.

```lean
theorem erdos_790.parts.iii :
    ∃ c : ℝ, 0 < c ∧ ∀ᶠ n : ℕ in atTop,
      (l n : ℝ) < (n : ℝ) ^ (1 - c)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/790.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/790.lean#L81).

## `Erdos790.erdos_790.variants.lower_bound`

Solved: stated here without proof.

> Choi, Komlós and Szemerédi [CKS75, Theorem (1.1)] proved
> $\sqrt{n\log n/\log\log n}\ll l(n)$.

```lean
theorem erdos_790.variants.lower_bound :
    (fun n : ℕ ↦ Real.sqrt ((n : ℝ) * Real.log n / Real.log (Real.log n)))
      =O[atTop] (fun n ↦ (l n : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/790.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/790.lean#L89).

## `Erdos790.erdos_790.variants.upper_bound`

Solved: stated here without proof.

> Choi, Komlós and Szemerédi [CKS75, Theorem (1.1)] proved
> $l(n)\ll n/\log n$.

```lean
theorem erdos_790.variants.upper_bound :
    (fun n ↦ (l n : ℝ)) =O[atTop] (fun n : ℕ ↦ (n : ℝ) / Real.log n)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/790.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/790.lean#L97).

## `Erdos790.erdos_790.variants.near_linear`

Open: stated without proof.

> Choi, Komlós and Szemerédi suggest in the closing paragraph of [CKS75]
> that $l(n)\geq n^{1-o(1)}$.

```lean
theorem erdos_790.variants.near_linear :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ n : ℕ in atTop,
      (n : ℝ) ^ (1 - ε) ≤ (l n : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/790.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/790.lean#L104).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/790.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/790.lean)
- [erdosproblems.com/790](https://www.erdosproblems.com/790)
