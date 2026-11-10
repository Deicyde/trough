---
declaration: theorem
origin: cited
lean: Green29.green_29, Green29.green_29.variant
statement: formalized
---

# Ben Green's Open Problem 29

> *References:*
> - [Ben Green's Open Problem 29](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.29)
> - [Gr12] Green, Ben. "What is... an approximate group." Notices Amer. Math. Soc 59.5 (2012): 655-656.
> - [Br13] Breuillard, Emmanuel, Ben Green, and Terence Tao. "Small doubling in groups."
>   Erdős Centennial. Berlin, Heidelberg: Springer Berlin Heidelberg, 2013. 129-151.
> - [Sa10] Sanders, Tom. "On a nonabelian Balog–Szemerédi-type lemma." Journal of the Australian
>   Mathematical Society 89.1 (2010): 127-132.
> - [CrSi10] Croot, Ernie, and Olof Sisask. "A probabilistic technique for finding almost-periods of
>   convolutions." Geometric and functional analysis 20.6 (2010): 1367-1396.

*Quoted from [FormalConjectures/GreensOpenProblems/29.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/29.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved.

## `Green29.green_29`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/green-29-counterexample/blob/1cbf80c3d5a333b2b79c203c0d60129924c8c712/lean/Green29FC.lean#L280-L287](https://github.com/KitaKen1/green-29-counterexample/blob/1cbf80c3d5a333b2b79c203c0d60129924c8c712/lean/Green29FC.lean#L280-L287).

> Suppose that $A$ is a $K$-approximate group (not necessarily abelian). Is there $S \subset A$,
> $|S| \gg K^{-O(1)} |A|$, with $S^8 \subset A^4$?
>
> The answer is negative. A counterexample is given, for arbitrarily large finite groups `H`, by
> `A = ({-1} × H) ∪ ({1} × H) ∪ {(0, 1)}` in `Multiplicative ℤ × H`.

```lean
theorem green_29 :
    ¬ ∃ C c : ℝ, 0 < C ∧ 0 < c ∧
      ∀ {G : Type*} [Group G] [DecidableEq G] (K : ℝ) (A : Finset G),
        1 ≤ K → IsApproximateSubgroup K (A : Set G) →
          ∃ S ⊆ A, C * K ^ (-c) * (A.card : ℝ) ≤ (S.card : ℝ) ∧
          S ^ 8 ⊆ A ^ 4
```

Category `research solved`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/GreensOpenProblems/29.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/29.lean#L50).

## `Green29.green_29.variant`

Solved: stated here without proof.

> Such a conclusion is known with $|S| \gg_K |A|$ [Br13 Problem 6.5, CrSi10, Sa10].

```lean
theorem green_29.variant :
    ∀ K : ℝ, 1 ≤ K →
      ∃ c : ℝ, 0 < c ∧ -- Allow c to depend on K.
        ∀ {G : Type*} [Group G] [DecidableEq G] (A : Finset G),
          IsApproximateSubgroup K (A : Set G) →
            ∃ S : Finset G, -- No S ⊆ A requirement in this variant.
              c * (A.card : ℝ) ≤ (S.card : ℝ) ∧
              S ^ 8 ⊆ A ^ 4
```

Category `research solved`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/GreensOpenProblems/29.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/29.lean#L60).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/29.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/29.lean)
- [Ben Green's Open Problem 29](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.29)
