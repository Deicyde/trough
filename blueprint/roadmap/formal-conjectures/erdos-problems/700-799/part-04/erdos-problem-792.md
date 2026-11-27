---
declaration: theorem
origin: cited
lean: Erdos792.erdos_792, Erdos792.erdos_792.variants.alon_kleitman, Erdos792.erdos_792.variants.bourgain
statement: formalized
---

# Erdős Problem 792

> *References:*
> - [erdosproblems.com/792](https://www.erdosproblems.com/792)
> - [Ben Green's Open Problem 1](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.1):
>   a related question for sets of positive integers; see `Green1.green_1` in
>   `FormalConjectures.GreensOpenProblems.«1»`.
> - [AlKl90] Alon, N. and Kleitman, D. J., *Sum-free subsets*. A tribute to Paul Erdős (1990),
>   13-26.
>   [PDF](https://web.math.princeton.edu/~nalon/PDFS/Publications2/Sum-free%20subsets.pdf)
> - [Be25b] Bedert, B., *Large sum-free subsets of sets of integers via $L^1$-estimates for
>   trigonometric series*. [arXiv:2502.08624](https://arxiv.org/abs/2502.08624) (2025).
> - [Bo97] Bourgain, Jean, *Estimates related to sumfree subsets of sets of integers*. Israel J.
>   Math. 97 (1997), 71-92.
>   [DOI](https://doi.org/10.1007/BF02774027)
> - [EGM14] Eberhard, Sean and Green, Ben and Manners, Freddie, *Sets of integers with no large
>   sum-free subset*. Ann. of Math. (2) 180 (2014), 621-652.
> - [Er65] Erdős, P., *Extremal problems in number theory*. Proc. Sympos. Pure Math., Vol. VIII
>   (1965), 181-189. [PDF](https://www.renyi.hu/~p_erdos/1965-02.pdf)
> - [Er73] Erdős, P., *Problems and results on combinatorial number theory*. A survey of
>   combinatorial theory (Proc. Internat. Sympos., Colorado State Univ., Fort Collins, Colo.,
>   1971) (1973), 117-138. [PDF](https://www.renyi.hu/~p_erdos/1973-21.pdf)

*Quoted from [FormalConjectures/ErdosProblems/792.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/792.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/792](https://www.erdosproblems.com/792).

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 4 test statements, counted here but not shown.

## `Erdos792.erdos_792`

Open: stated without proof.

> Let $f(n)$ be maximal such that in any $A\subset \mathbb{Z}$ with $\lvert A\rvert=n$ there exists
> some sum-free subset $B\subseteq A$ with $\lvert B\rvert \geq f(n)$, so that there are no
> solutions to
>
> $$a+b=c$$
>
> with $a,b,c\in B$, allowing $a=b$. Estimate $f(n)$.
>
> Since $f(n) = n/3 + o(n)$ is known, we interpret "estimate" as
> determining the order of magnitude of the excess $f(n) - n/3$.

```lean
theorem erdos_792 :
    (fun n : ℕ => (f n : ℝ) - n / 3) =Θ[atTop] erdos_792.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/792.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/792.lean#L114).

## `Erdos792.erdos_792.variants.alon_kleitman`

Solved: stated here without proof.

> Alon and Kleitman [AlKl90, Proposition 1.1] improved the lower bound to $(n+1)/3$.
> Here we restrict to sets of $n \geq 3$ positive integers, to match Bourgain's bound below.

```lean
theorem erdos_792.variants.alon_kleitman (A : Finset ℤ)
    (h_positive : ∀ a ∈ A, 0 < a) (h_card : 3 ≤ A.card) :
    ∃ B ⊆ A, IsSumFree (B : Set ℤ) ∧ A.card + 1 ≤ 3 * B.card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/792.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/792.lean#L123).

## `Erdos792.erdos_792.variants.bourgain`

Solved: stated here without proof.

> Bourgain [Bo97, Proposition 1.3] further improved the lower bound to $(n+2)/3$
> for sets of $n \geq 3$ positive integers. The size restriction appears in the proof on p. 76;
> the set $\{1,2\}$ shows why it cannot be omitted.

```lean
theorem erdos_792.variants.bourgain (A : Finset ℤ)
    (h_positive : ∀ a ∈ A, 0 < a) (h_card : 3 ≤ A.card) :
    ∃ B ⊆ A, IsSumFree (B : Set ℤ) ∧ A.card + 2 ≤ 3 * B.card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/792.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/792.lean#L134).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/792.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/792.lean)
- [erdosproblems.com/792](https://www.erdosproblems.com/792)
