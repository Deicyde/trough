---
declaration: theorem
origin: cited
lean: Erdos1193.erdos_1193.parts.i, Erdos1193.erdos_1193.parts.ii, Erdos1193.erdos_1193.variants.sumRep_univ, Erdos1193.erdos_1193.variants.upper_density_pos
statement: formalized
---

# Erdős Problem 1193

> *References:*
> - [erdosproblems.com/1193](https://www.erdosproblems.com/1193)
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
>   (1980), 89-115.

*Quoted from [FormalConjectures/ErdosProblems/1193.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1193.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1193](https://www.erdosproblems.com/1193).

The file states 4 research or textbook statements: 4 solved.

## `Erdos1193.erdos_1193.parts.i`

Proved here.

> Let $A\subset \mathbb{N}$ and let $g(n)$ be a non-decreasing function of $n$ which is always $>0$.
>
> Is the lower density of
>
> $$\{ n : 1_A\ast 1_A(n)=g(n)\}$$
>
> always $0$?
>
> The answer is trivially no to both questions: indeed if $A=\mathbb{N}$ (assuming $0\in\mathbb{N}$)
> then $1_A\ast 1_A(n)=n+1$ for all $n$. Presumably Erdős had some additional restrictions on either
> $g$ or $A$ in mind, but these are not recorded in [Er80].

```lean
theorem erdos_1193.parts.i :
    ¬ ∀ (A : Set ℕ) (g : ℕ → ℕ), Monotone g → (∀ n, 0 < g n) →
      {n : ℕ | sumRep A n = g n}.lowerDensity = 0
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1193.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1193.lean#L47).

## `Erdos1193.erdos_1193.parts.ii`

Proved here.

> Let $A\subset \mathbb{N}$ and let $g(n)$ be a non-decreasing function of $n$ which is always $>0$.
>
> Is the upper density of
>
> $$\{ n : 1_A\ast 1_A(n)=g(n)\}$$
>
> always $\lt c$ for some constant $c<1$?
>
> The answer is trivially no to both questions: indeed if $A=\mathbb{N}$ (assuming $0\in\mathbb{N}$)
> then $1_A\ast 1_A(n)=n+1$ for all $n$. Presumably Erdős had some additional restrictions on either
> $g$ or $A$ in mind, but these are not recorded in [Er80].

```lean
theorem erdos_1193.parts.ii :
    ¬ ∃ c < (1 : ℝ), ∀ (A : Set ℕ) (g : ℕ → ℕ), Monotone g → (∀ n, 0 < g n) →
      {n : ℕ | sumRep A n = g n}.upperDensity < c
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1193.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1193.lean#L70).

## `Erdos1193.erdos_1193.variants.sumRep_univ`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1193.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1193.lean).

> Indeed if $A=\mathbb{N}$ (assuming $0\in\mathbb{N}$) then $1_A\ast 1_A(n)=n+1$ for all $n$.

```lean
theorem erdos_1193.variants.sumRep_univ (n : ℕ) : sumRep (Set.univ : Set ℕ) n = n + 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1193.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1193.lean#L86).

## `Erdos1193.erdos_1193.variants.upper_density_pos`

Proved here.

> Erdős writes the upper density can be positive, but he believes it is bounded away from $1$.

```lean
theorem erdos_1193.variants.upper_density_pos :
    ∃ (A : Set ℕ) (g : ℕ → ℕ), Monotone g ∧ (∀ n, 0 < g n) ∧
      0 < {n : ℕ | sumRep A n = g n}.upperDensity
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1193.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1193.lean#L93).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1193.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1193.lean)
- [erdosproblems.com/1193](https://www.erdosproblems.com/1193)
