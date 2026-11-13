---
declaration: theorem
origin: cited
lean: Erdos43.erdos_43.parts.i, Erdos43.erdos_43.parts.ii
statement: formalized
---

# Erdős Problem 43

> *Reference:* [erdosproblems.com/43](https://www.erdosproblems.com/43)

*Quoted from [FormalConjectures/ErdosProblems/43.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/43.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/43](https://www.erdosproblems.com/43).

The file states 2 research or textbook statements: 2 solved.

## `Erdos43.erdos_43.parts.i`

Solved: stated here without proof.

> If $A$ and $B$ are Sidon sets in $\{1,\ldots,N\}$ with
> $(A-A)\cap(B-B)=\{0\}$, is it true that
>
> $$\binom{\lvert A\rvert}{2}+\binom{\lvert B\rvert}{2}\leq\binom{f(N)}{2}+O(1)?$$
>
> The answer is no; the Erdős Problems page notes that this follows from the solution to
> Erdős Problem 42.

```lean
theorem erdos_43.parts.i :
    ¬ ∃ C : ℝ, ∀ᶠ N in Filter.atTop, ∀ (A B : Finset ℕ),
      A ⊆ Finset.Icc 1 N →
      B ⊆ Finset.Icc 1 N →
      IsSidon (A : Set ℕ) →
      IsSidon (B : Set ℕ) →
      (A - A) ∩ (B - B) = {0} →
      ((A.card.choose 2 + B.card.choose 2 : ℕ) : ℝ) ≤ ((f N).choose 2 : ℝ) + C
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/43.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/43.lean#L46).

## `Erdos43.erdos_43.parts.ii`

Solved: stated here without proof.

> If $A$ and $B$ are equal-sized Sidon sets in $\{1,\ldots,N\}$ with
> $(A-A)\cap(B-B)=\{0\}$, can the bound be improved to
>
> $$\binom{\lvert A\rvert}{2}+\binom{\lvert B\rvert}{2}
>     \leq (1-c+o(1))\binom{f(N)}{2}$$
>
> for some constant $c>0$?
>
> The answer is no; the Erdős Problems page records a negative answer due to Barreto.

```lean
theorem erdos_43.parts.ii :
    ¬ ∃ᵉ (c > 0), ∃ o : ℕ → ℝ, o =o[Filter.atTop] (1 : ℕ → ℝ) ∧
    ∀ᶠ N in Filter.atTop, ∀ (A B : Finset ℕ),
      A ⊆ Finset.Icc 1 N →
      B ⊆ Finset.Icc 1 N →
      IsSidon (A : Set ℕ) →
      IsSidon (B : Set ℕ) →
      A.card = B.card →
      (A - A) ∩ (B - B) = {0} →
      ((A.card.choose 2 + B.card.choose 2 : ℕ) : ℝ) ≤
        (1 - c + o N) * ((f N).choose 2 : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/43.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/43.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/43.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/43.lean)
- [erdosproblems.com/43](https://www.erdosproblems.com/43)
