---
declaration: theorem
origin: cited
lean: Green29.green_29, Green29.green_29.subset_counterexample, Green29.green_29.variant
statement: formalized
---

# Ben Green's Open Problem 29

> *References:*
> - [Ben Green's Open Problem 29](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.29)
> - [Gr12] Green, Ben. "What is... an approximate group." Notices Amer. Math. Soc 59.5 (2012): 655-656.
> - [Br13] Breuillard, Emmanuel, Ben Green, and Terence Tao. "Small doubling in groups."
>   Erdős Centennial. Berlin, Heidelberg: Springer Berlin Heidelberg, 2013. 129-151.
>   [arXiv:1301.7718](https://arxiv.org/abs/1301.7718)
> - [Sa10] Sanders, Tom. "On a nonabelian Balog–Szemerédi-type lemma." Journal of the Australian
>   Mathematical Society 89.1 (2010): 127-132.
> - [CrSi10] Croot, Ernie, and Olof Sisask. "A probabilistic technique for finding almost-periods of
>   convolutions." Geometric and functional analysis 20.6 (2010): 1367-1396.
>
> The printed Problem 29 includes the stronger hypothesis `S ⊆ A`; that strengthened variant is
> false (see `green_29.subset_counterexample`). The open problem is the version without `S ⊆ A`,
> following [Br13, Theorem 6.5 and Problem 6.6].

*Quoted from [FormalConjectures/GreensOpenProblems/29.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/29.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Green29.green_29`

Open: stated without proof.

> **Ben Green's Open Problem 29 / [Br13, Problem 6.6].**
> Suppose that $A$ is a $K$-approximate group (not necessarily abelian). Can one find a set
> $S$ (not necessarily contained in $A$) with $|S| \gg K^{-O(1)} |A|$ and $S^8 \subseteq A^4$?
>
> The stronger variant requiring $S \subseteq A$ is false; see `green_29.subset_counterexample`.
> The known result with $|S| \gg_K |A|$ is `green_29.variant`.

```lean
theorem green_29 :
    ∃ C c : ℝ, 0 < C ∧ 0 < c ∧
      ∀ {G : Type*} [Group G] [DecidableEq G] (K : ℝ) (A : Finset G),
        1 ≤ K → IsApproximateSubgroup K (A : Set G) →
          ∃ S : Finset G, C * K ^ (-c) * (A.card : ℝ) ≤ (S.card : ℝ) ∧
            S ^ 8 ⊆ A ^ 4
```

Category `research open`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/GreensOpenProblems/29.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/29.lean#L52).

## `Green29.green_29.subset_counterexample`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/green-29-counterexample/blob/1cbf80c3d5a333b2b79c203c0d60129924c8c712/lean/Green29FC.lean#L280-L287](https://github.com/KitaKen1/green-29-counterexample/blob/1cbf80c3d5a333b2b79c203c0d60129924c8c712/lean/Green29FC.lean#L280-L287).

> The strengthened variant of Green's Problem 29 requiring $S \subseteq A$ is false.
> A counterexample is given, for arbitrarily large finite groups $H$, by
> $A = (\{-1\} \times H) \cup (\{1\} \times H) \cup \{(0, 1)\}$ in $\mathbb{Z} \times H$.

```lean
theorem green_29.subset_counterexample :
    ¬ ∃ C c : ℝ, 0 < C ∧ 0 < c ∧
      ∀ {G : Type*} [Group G] [DecidableEq G] (K : ℝ) (A : Finset G),
        1 ≤ K → IsApproximateSubgroup K (A : Set G) →
          ∃ S ⊆ A, C * K ^ (-c) * (A.card : ℝ) ≤ (S.card : ℝ) ∧
          S ^ 8 ⊆ A ^ 4
```

Category `research solved`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/GreensOpenProblems/29.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/29.lean#L67).

## `Green29.green_29.variant`

Solved: stated here without proof.

> The known result [Br13, Theorem 6.5; CrSi10; Sa10]: for each $K$ there is $c(K) > 0$
> such that every $K$-approximate group $A$ has a set $S$ (not necessarily contained in $A$) with
> $|S| \ge c(K)|A|$ and $S^8 \subseteq A^4$. The open problem asks whether $c(K)$ can be bounded
> below by $C K^{-c}$ for absolute constants $C, c > 0$.

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

Category `research solved`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/GreensOpenProblems/29.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/29.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/29.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/29.lean)
- [Ben Green's Open Problem 29](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.29)
