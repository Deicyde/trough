---
declaration: theorem
origin: cited
lean: Green15.green_15, Green15.green_15_ap4
statement: formalized
---

# Green's Open Problem 15

> References:
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.15)
> - [BJP14] T. Brown, V. Jungić and A. Poelstra, "On double 3-term arithmetic progressions",
>   Integers 14 (2014), Paper No. A43.
> - [CCS14] J. Cassaigne, J. D. Currie, L. Schaeffer and J. Shallit, "Avoidance of additive cubes and
>   related results", Adv. in Appl. Math. 56 (2014), 25–66.

*Quoted from [FormalConjectures/GreensOpenProblems/15.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/15.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Green15.green_15`

Open: stated without proof.

> Does there exist a Lipschitz function $f : \mathbb{N} \to \mathbb{Z}$ whose graph
> $\Gamma = \{(n, f(n)) : n \in \mathbb{N}\} \subseteq \mathbb{Z}^2$ is free of 3-term progressions?

```lean
theorem green_15 :
    ∃ K : ℝ≥0, ∃ f : ℕ → ℤ, LipschitzWith K f ∧
      IsAPOfLengthFree {((n, f n) : ℤ × ℤ) | (n : ℕ)} 3
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/15.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/15.lean#L43).

## `Green15.green_15_ap4`

Solved: stated here without proof.

> The answer is YES for 4-term progressions [BJP14].

```lean
theorem green_15_ap4 :
    ∃ K : ℝ≥0, ∃ f : ℕ → ℤ, LipschitzWith K f ∧
      IsAPOfLengthFree  {((n, f n) : ℤ × ℤ) | (n : ℕ)} 4
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/15.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/15.lean#L52).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/15.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/15.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.15)
