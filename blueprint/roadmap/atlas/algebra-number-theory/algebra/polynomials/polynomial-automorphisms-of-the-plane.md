---
declaration: section
origin: cited
lean: MathlibExt.Algebra.Polynomial.ScottishBook79Wanted.ScottishBookProblem79Claim, MathlibExt.Algebra.Polynomial.ScottishBook79Wanted.mazurOrlicz79_refuted
statement: formalized
---

# Polynomial automorphisms of the plane

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomial-automorphisms-of-the-plane/index.html).

## Mazur–Orlicz claim on polynomial automorphisms of the plane

The statement that every
polynomial map of the plane with a polynomial inverse is affine: for all pairs
$P = (P_1, P_2)$ and $Q = (Q_1, Q_2)$ of real polynomials in two variables such that
$Q(P(x)) = x$ for every $x \in \mathbb{R}^2$ and $P(Q(y)) = y$ for every $y \in \mathbb{R}^2$,
there are a real $2 \times 2$ matrix $A$ with $\det A \neq 0$ and a vector $c \in \mathbb{R}^2$
such that $P(x) = Ax + c$ for every $x \in \mathbb{R}^2$.

This is the affirmative answer to Mazur and Orlicz's Problem 79 of the Scottish Book,
restricted to the Euclidean plane.

Formalized by `MathlibExt.Algebra.Polynomial.ScottishBook79Wanted.ScottishBookProblem79Claim`, a definition declared in [WantedExt/Algebra/Polynomial/ScottishBook79Wanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/Polynomial/ScottishBook79Wanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomial-automorphisms-of-the-plane/index.html#scottish-book-problem79-claim).

## Mazur–Orlicz Problem 79 has a negative answer

The claim of Problem 79 of the Scottish Book
for the plane is false: there is a polynomial map $P$ of $\mathbb{R}^2$ to itself with a
polynomial two-sided inverse that is not of the form $x \mapsto Ax + c$ with $A$ an invertible
real $2 \times 2$ matrix and $c \in \mathbb{R}^2$. For example, the map
$(x_1, x_2) \mapsto (x_1, x_2 + x_1^2)$ has the inverse $(y_1, y_2) \mapsto (y_1, y_2 - y_1^2)$.

## Sources

- S. Mazur and W. Orlicz, Problem 79 of the Scottish Book; typescript Ad 79 records the negative answer, via triangular polynomial automorphisms: maps `y₁ = x₁ + k`, `y₂ = x₂ + φ₂(x₁)`, …, `yₙ = xₙ + φₙ(x₁, …, xₙ₋₁)` with arbitrary polynomials `φ` are polynomial automorphisms with obvious polynomial inverses, but are not affine when some `φ` is nonlinear. For the plane, `y₁ = x₁`, `y₂ = x₂ + x₁²` already refutes affineness.

Stated but not proved: `MathlibExt.Algebra.Polynomial.ScottishBook79Wanted.mazurOrlicz79_refuted` is written with `theorem_wanted` in [WantedExt/Algebra/Polynomial/ScottishBook79Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/Polynomial/ScottishBook79Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomial-automorphisms-of-the-plane/index.html#mazur-orlicz79-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Polynomial automorphisms of the plane](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomial-automorphisms-of-the-plane/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/polynomials/polynomial-automorphisms-of-the-plane)
