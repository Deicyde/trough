---
declaration: theorem
origin: cited
lean: Erdos326.erdos_326, Erdos326.erdos_326.variants.eq
statement: formalized
---

# Erdős Problem 326

> *References:*
> - [erdosproblems.com/326](https://www.erdosproblems.com/326)
> - [ErGr80] Erdős, P. and Graham, R. L., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathématique (1980), p. 47.
> - [Ca57] Cassels, J. W. S., *Über Basen der natürlichen Zahlenreihe*.
>   Abh. Math. Sem. Univ. Hamburg (1957), 247-257.

*Quoted from [FormalConjectures/ErdosProblems/326.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/326.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/326](https://www.erdosproblems.com/326).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos326.erdos_326`

Open: stated without proof.

> Does there exist $A = \{a_1 < a_2 < \cdots\} \subset \mathbb{N}$ which is a minimal basis of
> order $2$ (i.e. every large integer is the sum of $2$ elements from $A$, and no proper subset of
> $A$ has this property), such that
>
> $$\lim_{k\to\infty} \frac{a_k}{k^2} = c$$
>
> for some $c \neq 0$?
>
> Erdős and Graham conjectured a negative answer to this question [ErGr80].
>
> "Minimal basis of order $2$" is formalised as `Minimal` for the predicate
> `Set.IsAsymptoticAddBasisOfOrder · 2` on sets of naturals ordered by inclusion.

```lean
theorem erdos_326 : ∃ (a : ℕ → ℕ), StrictMono a ∧
    Minimal (fun A : Set ℕ ↦ A.IsAsymptoticAddBasisOfOrder 2) (Set.range a) ∧
      ∃ (c : ℝ), c ≠ 0 ∧ Tendsto (fun n ↦ (a n : ℝ) / n ^ 2) atTop (𝓝 c)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/326.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/326.lean#L52).

## `Erdos326.erdos_326.variants.eq`

Solved: stated here without proof.

> Erdős originally asked this for any basis (not necessarily minimal); such a basis was constructed
> by Cassels [Ca57].

```lean
theorem erdos_326.variants.eq :
    ∃ (a : ℕ → ℕ) (_ : StrictMono a) (_ : Set.range a |>.IsAddBasisOfOrder 2) (x : ℝ) (_ : 0 < x),
      Tendsto (fun n ↦ (a n : ℝ) / n ^ 2) atTop (𝓝 x)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/326.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/326.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/326.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/326.lean)
- [erdosproblems.com/326](https://www.erdosproblems.com/326)
