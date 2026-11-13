---
declaration: theorem
origin: cited
lean: Erdos425.erdos_425.parts.i, Erdos425.erdos_425.parts.ii
statement: formalized
---

# Erdős Problem 425

> *Reference:* [Erdős Problem 425](https://www.erdosproblems.com/425)

*Quoted from [FormalConjectures/ErdosProblems/425.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/425.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/425](https://www.erdosproblems.com/425).

The file states 2 research or textbook statements: 2 open. It also has 1 test statement, counted here but not shown.

## `Erdos425.erdos_425.parts.i`

Open: stated without proof.

> Let $F(n)$ be the maximum size of a subset of $\{1,\ldots,n\}$ with distinct
> pairwise products. Is there a constant $c > 0$ such that
>
> $$F(n) = \pi(n) + (c + o(1)) n^{3/4}(\log n)^{-3/2}?$$

```lean
theorem erdos_425.parts.i : ∃ c : ℝ, 0 < c ∧
    Tendsto
      (fun n : ℕ =>
        ((pairProductExtremal n : ℝ) - (Nat.primeCounting n : ℝ)) /
          ((n : ℝ) ^ ((3 : ℝ) / 4) * (Real.log n) ^ (-(3 : ℝ) / 2)))
      atTop (𝓝 c)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/425.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/425.lean#L92).

## `Erdos425.erdos_425.parts.ii`

Open: stated without proof.

> If all products of $r$ distinct elements of $A \subseteq \{1,\ldots,n\}$ are
> distinct, must
>
> $$|A| \leq \pi(n) + O\bigl(n^{(r+1)/(2r)}\bigr)?$$

```lean
theorem erdos_425.parts.ii : ∀ r : ℕ, 1 ≤ r → ∃ C : ℝ, 0 < C ∧
    ∀ᶠ n in atTop, ∀ A : Finset ℕ, A ⊆ Finset.Icc 1 n → RProductsDistinct r A →
      (A.card : ℝ) ≤ (Nat.primeCounting n : ℝ) +
        C * (n : ℝ) ^ (((r : ℝ) + 1) / (2 * r))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/425.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/425.lean#L104).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/425.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/425.lean)
- [erdosproblems.com/425](https://www.erdosproblems.com/425)
