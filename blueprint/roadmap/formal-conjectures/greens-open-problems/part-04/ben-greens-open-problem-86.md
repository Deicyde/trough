---
declaration: theorem
origin: cited
lean: Green86.green_86
statement: formalized
---

# Ben Green's Open Problem 86

> *References:*
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.86)
> - [KRS00] Konyagin, S. V., Ruzsa, I. Z. and Schlag, W., *On uniformly distributed dilates of
>   finite integer sequences*. J. Number Theory 82 (2000), 165--187.
>   [doi:10.1006/jnth.1999.2420](https://doi.org/10.1006/jnth.1999.2420)
> - [Mo94] Montgomery, H. L., *Ten lectures on the interface between analytic number theory and
>   harmonic analysis*. CBMS Regional Conference Series in Mathematics 84, American Mathematical
>   Society (1994).

*Quoted from [FormalConjectures/GreensOpenProblems/86.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/86.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 1 API statement, counted here but not shown.

## `Green86.green_86`

Open: stated without proof.

> Let $c > 0$. Let $A$ be a set of $n$ (distinct) integers. Does there exist $\theta$ such that
> no interval of length $\frac{1}{n}$ in $\mathbb{R}/\mathbb{Z}$ contains more than $n^c$ of the
> numbers $\theta a \pmod 1$, $a \in A$?
>
> We read the question for every $c > 0$ and all $n \ge n_0(c)$. For small $n$ it can fail: for
> $A = \{0, 1, 3\}$ and $3^c < 2$, three points with at most one in each interval of length
> $1/3$ must be equally spaced, which is impossible. Intervals are half-open; for the question
> over all $c > 0$ this does not matter, since a closed interval of length $1/n$ is covered by two
> half-open ones. [Gr24] reports that the answer is yes for $c > 1/3$ [KRS00], and that
> [Mo94, Problem 17 (4)] attributes the problem to Komlós and Ruzsa.

```lean
theorem green_86 :
    ∀ c : ℝ, 0 < c → ∃ n₀ : ℕ, ∀ A : Finset ℤ, n₀ ≤ #A →
      ∃ θ : ℝ, ∀ t : ℝ, (numInInterval A θ t : ℝ) ≤ (#A : ℝ) ^ c
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/86.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/86.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/86.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/86.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.86)
