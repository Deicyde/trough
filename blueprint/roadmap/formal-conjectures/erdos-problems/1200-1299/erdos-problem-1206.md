---
declaration: theorem
origin: cited
lean: Erdos1206.erdos_1206.parts.i, Erdos1206.erdos_1206.parts.ii
statement: formalized
---

# Erdős Problem 1206

> *References:*
> - [erdosproblems.com/1206](https://www.erdosproblems.com/1206)
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
>   (1980), 89-115.
> - [GGK26] M. Garaev, F. Garayev, and S. Konyagin, *On Sidon sets with squares, cubes, and quartics
>   in short intervals*. arXiv:2602.08807 (2026).
> - [GaKo24] Gabdullin, M. R. and Konyagin, S. V., *Trigonometric polynomials with frequencies in the
>   set of cubes*. Math. Notes (2024), 336--340.

*Quoted from [FormalConjectures/ErdosProblems/1206.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1206.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1206](https://www.erdosproblems.com/1206).

The file states 2 research or textbook statements: 2 open.

## `Erdos1206.erdos_1206.parts.i`

Open: stated without proof.

> Does $\{1,2^3,\ldots,N^3\}$ contain a Sidon set of size $\gg N$?

```lean
theorem erdos_1206.parts.i :
    ∃ c : ℝ, 0 < c ∧ ∀ᶠ N in Filter.atTop, ∃ S : Finset ℕ,
      S ⊆ (Finset.Icc 1 N).image (fun n => n ^ 3) ∧
      IsSidon (S : Set ℕ) ∧ c * (N : ℝ) ≤ (S.card : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1206.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1206.lean#L41).

## `Erdos1206.erdos_1206.parts.ii`

Open: stated without proof.

> Is there an infinite set $A\subset \mathbb{N}$ of positive density such that $\{a^3 : a\in A\}$ is a Sidon set?

```lean
theorem erdos_1206.parts.ii :
    ∃ A : Set ℕ, A.Infinite ∧ 0 < A.lowerDensity ∧
      IsSidon ((fun a : ℕ => a ^ 3) '' A)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1206.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1206.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1206.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1206.lean)
- [erdosproblems.com/1206](https://www.erdosproblems.com/1206)
