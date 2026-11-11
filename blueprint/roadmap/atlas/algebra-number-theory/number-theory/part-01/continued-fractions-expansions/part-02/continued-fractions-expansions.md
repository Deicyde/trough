---
declaration: section
origin: cited
lean: MetaMathlibExt.IsLaplaceQFamily, MetaMathlibExt.lagrange_quadratic_convergent, GenContFract.of_den_succ_lt_succ_succ
statement: formalized
proof: formalized
---

# Continued fractions and expansions of reals: its own results

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/index.html).

Continued fractions, Farey sequences, Stern–Brocot tree, Engel, Pierce, Lüroth and similar series expansions of real numbers.

## Laplace Q-polynomial families

Let $R$ be a semiring and let $(P_k)_{k \ge 0}$ and
$(Q_k)_{k \ge 0}$ be sequences of polynomials in $R[X]$. The sequence $(Q_k)$ is a Laplace
Q-polynomial family companion to $(P_k)$ when $Q_0 = 1$ and, for every natural number $k \ge 1$,

$$Q_k = P_k + Q_{k-1}' \quad \text{and} \quad Q_{k+1} = X Q_k + (k + 1) Q_{k-1},$$

where $Q_{k-1}'$ denotes the formal derivative of $Q_{k-1}$.

## Sources

- https://cs.uwaterloo.ca/journals/JIS/VOL19/Kreinin/kreinin4.tex, lines 306-315.

Formalized by `MetaMathlibExt.IsLaplaceQFamily`, a definition declared in [MathlibExt/NumberTheory/LaplaceQPolynomial.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LaplaceQPolynomial.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/index.html#is-laplace-qfamily).

## Solutions of $P u^2 + Q u y + R y^2 = 1$ give convergents of $-Q/(2P)$

Let $P, Q, R, u, y$
be integers with $P > 0$ and $y > 0$, and let $D = Q^2 - 4PR$. Assume that $D < 0$, that
$D \ne -3$, and that $P \ne 2$ if $D = -4$. If $P u^2 + Q u y + R y^2 = 1$, then, writing
$\omega = -Q/(2P)$ with regular continued fraction expansion $\omega = [a_0; a_1, a_2, \dots]$,
there is a natural number $n$ such that $u/y$ equals the $n$-th convergent of $\omega$ and either
$n = 0$ or the partial quotient $a_n$ exists (the expansion has not terminated before $a_n$).

A solution of $P u^2 + Q u y + R y^2 = 1$ automatically has $\gcd(u, y) = 1$, as the source's
lemma requires; the exclusion $D \ne -3$ and the condition that $D = -4$ implies $P \ne 2$ are
exactly the source theorem's.

Proof: Following Matthews' theorem and lemma, complete the square, establish the Legendre
approximation bound, and choose the least convergent index so that termination cannot have
occurred earlier.

## Sources

- Keith R. Matthews, "Lagrange's Algorithm Revisited: Solving at^2 + btu + cu^2 = n in the Case of Negative Discriminant," Journal of Integer Sequences 17 (2014), Article 14.11.1, Theorem, lines 167–169, equation, lines 109–111, Lemma, lines 120–122, https://cs.uwaterloo.ca/journals/JIS/VOL17/Matthews/matt10.tex

Formalized by `MetaMathlibExt.lagrange_quadratic_convergent`, a theorem declared in [MathlibExt/NumberTheory/QuadraticForms/LagrangeQuadraticConvergent.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/QuadraticForms/LagrangeQuadraticConvergent.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/index.html#lagrange-quadratic-convergent).

## Strict growth of continued-fraction denominators

Let $K$ be a linearly ordered field
with a floor function, let $v \in K$, and write $v = [a_0; a_1, a_2, \dots]$ for its regular
continued fraction, with convergent denominators $q_0 = 1$, $q_1 = a_1$ and
$q_{k+2} = a_{k+2} q_{k+1} + q_k$. For every natural number $n$, if the partial quotient
$a_{n+2}$ exists (the continued fraction has not terminated before it), then
$q_{n+1} < q_{n+2}$.

The comparison starts at $q_1$ because $q_0 = 1$ while $q_1 = a_1$ can also equal $1$.

## Sources

- arXiv:2607.23662, item D07, which uses the adjacent inequality $q_{k-1} < q_k$.

Formalized by `GenContFract.of_den_succ_lt_succ_succ`, a theorem declared in [MathlibExt/Algebra/ContinuedFractions/Computation/Approximations.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/ContinuedFractions/Computation/Approximations.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-02/index.html#of-den-succ-lt-succ-succ).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Continued fractions and expansions of reals](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/continued-fractions-expansions)
