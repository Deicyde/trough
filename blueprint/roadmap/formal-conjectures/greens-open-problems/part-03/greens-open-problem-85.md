---
declaration: theorem
origin: cited
lean: Green85.green_85, Green85.green_85_loose
statement: formalized
---

# Green's Open Problem 85

> *Carbery’s rectangle problem*
>
> References:
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.85)
> - [CCW99] Carbery, Anthony, Michael Christ, and James Wright. "Multidimensional van der Corput and sublevel set estimates." Journal of the American Mathematical Society 12.4 (1999): 981-1015 Section 6.
> - [Ke00] Keleti, Tamás. "Density and covering properties of intervals of ℝn." Mathematika 47.1-2 (2000): 229-242.
> - [KKM02] Katz, Nets Hawk, Elliot Krop, and Mauro Maggioni. "Remarks on the box problem." Mathematical Research Letters 9.4 (2002): 515-520.
> - [Mu02] Mubayi, Dhruv. "Some exact results and new asymptotics for hypergraph Turán numbers." Combinatorics, Probability and Computing 11.3 (2002): 299-309 Conjecture 1.4.
> - [CPZ20] Conlon, David, Cosmin Pohoata, and Dmitriy Zakharov. "Random multilinear maps and the Erd\H {o} s box problem." arXiv preprint arXiv:2011.09024 (2020).

*Quoted from [FormalConjectures/GreensOpenProblems/85.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/85.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Green85.green_85`

Open: stated without proof.

> Suppose that $A$ is an open subset of $[0, 1]^2$ with measure $\alpha$. Are there four points in
> $A$ determining an axis-parallel rectangle with area $\gt c \alpha^2$?

```lean
theorem green_85 :
  ∃ c > 0, ∀ A : Set (ℝ × ℝ),
    IsOpen A →
    A ⊆ Icc 0 1 ×ˢ Icc 0 1 →
    A.Nonempty →
    let α := (volume A).toReal
    ∃ x₁ x₂ y₁ y₂,
      {(x₁, y₁), (x₂, y₁), (x₂, y₂), (x₁, y₂)} ⊆ A ∧
      c * α ^ 2 ≤ |x₁ - x₂| * |y₁ - y₂|
```

Category `research open`; AMS [28 Measure and integration](../../by-subject/part-01/28-measure-and-integration/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/85.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/85.lean#L45).

## `Green85.green_85_loose`

Solved: stated here without proof.

> From [Gr24] "It is quite easy to show using Cauchy-Schwarz that there must be such a rectangle with
> area $\gg \alpha^2 (\log 1/\alpha)^{-1}$."

```lean
theorem green_85_loose :
    ∃ c > 0, ∀ᶠ α in 𝓝[>] 0,
    ∀ A : Set (ℝ × ℝ),
    IsOpen A →
    A ⊆ Icc 0 1 ×ˢ Icc 0 1 →
    A.Nonempty →
    α = (volume A).toReal →
    ∃ x₁ x₂ y₁ y₂,
      {(x₁, y₁), (x₂, y₁), (x₂, y₂), (x₁, y₂)} ⊆ A ∧
      c * α ^ 2 * (Real.log (1/α))⁻¹ ≤ |x₁ - x₂| * |y₁ - y₂|
```

Category `research solved`; AMS [28 Measure and integration](../../by-subject/part-01/28-measure-and-integration/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/85.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/85.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/85.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/85.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.85)
