---
declaration: theorem
origin: cited
lean: Green18.green_18, Green18.green_18.bmz_corners
statement: formalized
---

# Ben Green's Open Problem 18

> *Reference:*
> - [Gr26] [Ben Green's Open Problem 18](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.18)
> - [Au16] Austin, Tim. "Ajtai–Szemerédi theorems over quasirandom groups." Recent trends in
>   combinatorics. Cham: Springer International Publishing, 2016. 453-484.
> - [So13] Solymosi, Jozsef. "Roth-type theorems in finite groups." European Journal of Combinatorics
>   34.8 (2013): 1454-1458.
> - [Go01] Gowers, William T. "A new proof of Szemerédi's theorem." Geometric & Functional Analysis
>   GAFA 11.3 (2001): 465-588.

*Quoted from [FormalConjectures/GreensOpenProblems/18.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/18.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Green18.green_18`

Open: stated without proof.

> Suppose that $G$ is a finite group, and let $A \subset G \times G$ be a subset of density $\alpha$.
> Is it true that there are $\gg_\alpha |G|^3$ triples $x, y, g$ such that $(x, y), (gx, y), (x, gy)$
> all lie in $A$?
>
> Note: A is taken as $\alpha$-dense, i.e. $|A| \ge \alpha |G|^2$ [Au16, Question 2]

```lean
theorem green_18 :
    ∀ α > 0, ∃ c > 0, ∃ m₀ : ℕ,
      ∀ (G : Type*) [Group G] [Fintype G] [DecidableEq G] (A : Finset (G × G)),
      Fintype.card G ≥ m₀ →
      (A.card : ℝ) ≥ α * (Fintype.card G) ^ 2 →
      (numNaiveCorners A : ℝ) ≥ c * (Fintype.card G) ^ 3
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/GreensOpenProblems/18.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/18.lean#L60).

## `Green18.green_18.bmz_corners`

Solved: stated here without proof.

> [So13] proved this is true for "BMZ corners". Follows from the proof of Theorem 2.1, p.1456-1457.

```lean
theorem green_18.bmz_corners : ∀ α > 0, ∃ c > 0, ∃ m₀ : ℕ,
    ∀ (G : Type*) [Group G] [Fintype G] [DecidableEq G] (A : Finset (G × G)),
    Fintype.card G ≥ m₀ →
    (A.card : ℝ) ≥ α * (Fintype.card G) ^ 2 →
    (numBmzCorners A : ℝ) ≥ c * (Fintype.card G) ^ 3
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/GreensOpenProblems/18.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/18.lean#L82).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/18.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/18.lean)
- [Ben Green's Open Problem 18](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.18)
