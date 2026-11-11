---
declaration: section
origin: cited
lean: MetaMathlibExt.pellType_solution_mul_unit, MathlibExt.NumberTheory.PellConvergentWanted.NumberTheory.pell_solution_is_convergent
statement: formalized
---

# Pell's equation

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-s-equation/index.html).

## Composing a Pell-type solution with a norm-one unit

Let $a, b, c, T, U, x, y$ be integers
with $a T^2 - b U^2 = c$ and $x^2 - ab y^2 = 1$. Then the pair $(T x + b U y, a T y + U x)$ is
again a solution: $a (T x + b U y)^2 - b (a T y + U x)^2 = c$.

The source iterates this step, assuming that $ab > 1$ is not a square, to obtain infinitely many
solutions. That conclusion needs further nondegeneracy hypotheses (for $T = U = c = 0$ every
iterate is $(0, 0)$); the single step is the multiplicativity of the norm form and needs no
hypotheses beyond the two equations.

## Sources

- E. L. Roettger and H. C. Williams, "Some Remarks Concerning the Lucas-Lehmer Primality Test," Journal of Integer Sequences 28 (2025), Article 25.2.5, Theorem (an observation of Euler), equation, lines 605–614, <https://cs.uwaterloo.ca/journals/JIS/VOL28/Roettger/roettger15.tex>

Formalized by `MetaMathlibExt.pellType_solution_mul_unit`, a theorem declared in [MathlibExt/NumberTheory/QuadraticForms/PellTypeSolutionMulUnit.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/QuadraticForms/PellTypeSolutionMulUnit.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-s-equation/index.html#pell-type-solution-mul-unit).

## Solutions of Pell's equation are continued-fraction convergents

Let $d$ be a positive
squarefree integer and let $x$ and $y$ be positive integers with $x^2 - d y^2 = 1$. Then $x / y$
is a convergent of the regular continued fraction expansion of $\sqrt{d}$: there is a natural
number $n$ such that the $n$-th convergent of $\sqrt{d}$ (counting from the $0$-th) equals
$x / y$.

## Sources

- J.-L. Lagrange (1770). Listed as §84 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `pell_solution_convergent` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.PellConvergentWanted.NumberTheory.pell_solution_is_convergent` is written with `theorem_wanted` in [WantedExt/NumberTheory/PellConvergentWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PellConvergentWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-s-equation/index.html#pell-solution-is-convergent).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pell's equation](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-s-equation/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-s-equation)
