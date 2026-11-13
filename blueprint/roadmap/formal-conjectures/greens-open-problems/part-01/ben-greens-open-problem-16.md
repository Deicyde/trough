---
declaration: theorem
origin: cited
lean: Green16.green_16, Green16.green_16_lower_bound, Green16.green_16_upper_bound, Green16.zhao_question
statement: formalized
---

# Ben Green's Open Problem 16

> *References:*
> * [Ben Green's Open Problem 16](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.16)
> * [Ruzsa\](I. Z. Ruzsa, Solving a linear equation in a set of integers. I. Acta Arith. 65 (1993), no. 3, 259–282.)
> * [Schoen and Sisask\](T. Schoen and O. Sisask, Roth’s theorem for four variables and additive structures in sums of sparse sets Forum of Mathematics, Sigma (2016), Vol. 4, e5, 28 pages.)
> * [Yufei Zhao\](Via Personal Communication with Ben Green)

*Quoted from [FormalConjectures/GreensOpenProblems/16.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/16.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 2 open and 2 solved.

## `Green16.green_16`

Open: stated without proof.

> What is the largest subset of $[N]$ with no solution to $x + 3y = 2z + 2w$ in distinct integers $x, y, z, w$?

```lean
theorem green_16 (N : ℕ) :
    ∃ A : Finset ℕ, A ⊆ Icc 1 N ∧ SolutionFree A ∧
      A.card = green_16.answer N ∧
      MaximalFor (fun B => B ⊆ Icc 1 N ∧ SolutionFree B) Finset.card A
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/16.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/16.lean#L50).

## `Green16.green_16_lower_bound`

Solved: stated here without proof.

> From [Ruzsa] $f(N) \gg N^{1/2}$.

```lean
theorem green_16_lower_bound :
    (fun N ↦ (N : ℝ) ^ (1 / 2 : ℝ)) ≪ fun N ↦ (f N : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/16.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/16.lean#L58).

## `Green16.green_16_upper_bound`

Solved: stated here without proof.

> From [Schoen and Sisask] $f(N) \ll N \cdot e^{-c(\log N)^{1/7}}$.

```lean
theorem green_16_upper_bound :
    ∃ c > (0 : ℝ), (fun N ↦ (f N : ℝ)) ≪ fun N ↦ (N : ℝ) * exp (-c * (log N) ^ (1 / 7 : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/16.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/16.lean#L64).

## `Green16.zhao_question`

Open: stated without proof.

> From [Yufei Zhao]: Is there a subset of $\{1, \ldots, N\}$ of size
> $N^{1/3 - o(1)}$ with no nontrivial solutions to $x + 2y + 3z = x' + 2y' + 3z'$?

```lean
theorem zhao_question :
    ∃ h : ℕ → ℝ, Tendsto h atTop (𝓝 0) ∧
      ∀ᶠ N in atTop, (g N : ℝ) ≥ (N : ℝ) ^ (1 / 3 - h N)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/16.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/16.lean#L86).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/16.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/16.lean)
- [Ben Green's Open Problem 16](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.16)
