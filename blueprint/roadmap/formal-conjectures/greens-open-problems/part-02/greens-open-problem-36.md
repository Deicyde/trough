---
declaration: theorem
origin: cited
lean: Green36.green_36, Green36.green_36.variants.cks05
statement: formalized
---

# Green's Open Problem 36

> *References:*
> * [Gr24] [Green's Open Problems #36](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.36)
> * [CKS05] Cohn, H., Kleinberg, R., Szegedy, B., and Umans, C. "Group-theoretic Algorithms for
>   Matrix Multiplication" (Problem 4.7)

*Quoted from [FormalConjectures/GreensOpenProblems/36.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/36.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open.

## `Green36.green_36`

Open: stated without proof.

> Do the following exist, for arbitrarily large $n$? An abelian group $H$ with $|H| = n^{2+o(1)}$,
> together with subsets $A_1, ..., A_n, B_1, ..., B_n$ satisfying $|A_i||B_i| \ge n^{2-o(1)}$ and
> $|A_i + B_i| = |A_i||B_i|$, such that the sets $A_i + B_i$ are disjoint from the sets $A_j + B_k$
> ($j \neq k$)?
>
> NOTE: according to [CKS05, 4.1], the conditions should be $A_i + B_j$ disjoint from $A_j + B_k$ for
> $i \neq k$. See `green_36.variants.cks05`.

```lean
theorem green_36 :
    ∀ ε > (0 : ℝ), ∃ᶠ n in atTop,
      ∃ (H : Type) (_ : AddCommGroup H) (_ : Finite H) (A B : Fin n → Finset H),
        (n : ℝ) ^ (2 - ε) ≤ Nat.card H ∧ Nat.card H ≤ (n : ℝ) ^ (2 + ε) ∧
        (∀ i, (n : ℝ) ^ (2 - ε) ≤ (A i).card * (B i).card) ∧
        Green36Property A B
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/GreensOpenProblems/36.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/36.lean#L60).

## `Green36.green_36.variants.cks05`

Open: stated without proof.

> Variant using the exact simultaneous double product property from [CKS05, 4.1].

```lean
theorem green_36.variants.cks05 :
    ∀ ε > (0 : ℝ), ∃ᶠ n in atTop,
      ∃ (H : Type) (_ : AddCommGroup H) (_ : Finite H) (A B : Fin n → Finset H),
        (n : ℝ) ^ (2 - ε) ≤ Nat.card H ∧ Nat.card H ≤ (n : ℝ) ^ (2 + ε) ∧
        (∀ i, (n : ℝ) ^ (2 - ε) ≤ (A i).card * (B i).card) ∧
        SimultaneousDoubleProduct A B
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/GreensOpenProblems/36.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/36.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/36.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/36.lean)
- [Green's Open Problems #36](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.36)
