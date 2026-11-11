---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Calculus.MonotoneDiscontinuousDerivWanted.exists_monotone_differentiable_not_continuous_deriv, MathlibExt.Analysis.Calculus.PolynomialOfPointwiseVanishingDerivWanted.exists_polynomial_eq_of_forall_exists_iteratedDerivWithin_eq_zero, MathlibExt.Analysis.Calculus.EvenC2SquareFactorWanted.exists_contDiffOn_comp_sq_of_even, MathlibExt.Analysis.Calculus.BorelWanted.borel_jet_real, MathlibExt.Analysis.Calculus.PiecewiseContDiffWanted.contDiffOn_piecewise_Icc, MathlibExt.Analysis.Calculus.ExpTaylorPolyOddUniqueZeroWanted.existsUnique_sum_pow_div_factorial_eq_zero_of_odd, MathlibExt.Analysis.Calculus.XSqSinInvSqNonintegrableDerivWanted.differentiable_and_not_integrableOn_deriv_sq_mul_sin_inv_sq, MathlibExt.Analysis.SpecialFunctions.ExpSubExpUniqueFixedPointWanted.existsUnique_exp_sub_one_sub_exp_one_sub_eq_self
statement: formalized
---

# Differential calculus of one variable: its own results

8 results, 1 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/index.html).

Derivatives of real functions of one real variable: mean-value and second-derivative tests, Taylor polynomials and remainders, Borel's lemma, interchange of limits and derivatives, monotone and C^n gluing results; not nowhere-differentiable constructions (see continuity subfield).

## A monotone differentiable function with discontinuous derivative

There is a
nondecreasing function $f : \mathbb{R} \to \mathbb{R}$ that is differentiable at every point and
whose derivative $f'$ is not continuous.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of one variable), problem `ma_proofbench_l1_92`.

Stated but not proved: `MathlibExt.Analysis.Calculus.MonotoneDiscontinuousDerivWanted.exists_monotone_differentiable_not_continuous_deriv` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/MonotoneDiscontinuousDerivWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/MonotoneDiscontinuousDerivWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/index.html#exists-monotone-differentiable-not-conti).

## A smooth function on the unit interval with some vanishing derivative at each point is a polynomial there

**A smooth function on the unit interval with some vanishing derivative at each point is a
polynomial there.** Let $f : \mathbb{R} \to \mathbb{R}$ be infinitely differentiable on $[0, 1]$,
and suppose that for every $x \in [0, 1]$ there is an integer $n \ge 0$ such that the $n$-th
derivative of $f$ within $[0, 1]$ vanishes at $x$ (at the endpoints these derivatives are
one-sided). Then there is a polynomial $p$ with real coefficients such that $f(x) = p(x)$ for
every $x \in [0, 1]$.

Smoothness means infinite differentiability here, not real analyticity: the source's formal
statement assumed real analyticity, which reduces the problem to the identity theorem.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Real functions; Functions of one variable), problem `ma_proofbench_l2_81`, with the change above.

Stated but not proved: `MathlibExt.Analysis.Calculus.PolynomialOfPointwiseVanishingDerivWanted.exists_polynomial_eq_of_forall_exists_iteratedDerivWithin_eq_zero` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/PolynomialOfPointwiseVanishingDerivWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/PolynomialOfPointwiseVanishingDerivWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/index.html#exists-polynomial-eq-of-forall-exists-it).

## An even $C^2$ function is a $C^1$ function of $x^2$

Let $a>0$ and let
$f : \mathbb{R} \to \mathbb{R}$ be twice continuously differentiable on $[-a,a]$ with $f(x)=f(-x)$
for all $x\in[-a,a]$. Then there is $g : \mathbb{R} \to \mathbb{R}$, continuously differentiable on
$[0,a^2]$, with $f(x)=g(x^2)$ for all $x\in[-a,a]$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of one variable), problem `ma_proofbench_l1_11`.

Stated but not proved: `MathlibExt.Analysis.Calculus.EvenC2SquareFactorWanted.exists_contDiffOn_comp_sq_of_even` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/EvenC2SquareFactorWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/EvenC2SquareFactorWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/index.html#exists-cont-diff-on-comp-sq-of-even).

## Borel's lemma

For every sequence $(a_n)_{n \ge 0}$ of real numbers there is an infinitely
differentiable function $f : \mathbb{R} \to \mathbb{R}$ whose derivatives at $0$ are
$f^{(n)}(0) = a_n$ for every $n \ge 0$.

## Sources

- E. Borel, Ann. Sci. Ec. Norm. Sup. (3) 12 (1895), 9-55, DOI 10.24033/asens.406.

Formalized by `MathlibExt.Analysis.Calculus.BorelWanted.borel_jet_real`, a theorem declared in [MathlibExt/Analysis/Calculus/Borel.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/Borel.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/index.html#borel-jet-real).

## Gluing $C^n$ functions on adjacent closed intervals

Let $E$ be a real normed space, let
$n \in \mathbb{N} \cup \{\infty\}$ and let $a \le b \le c$ be real numbers. Let
$f, g : \mathbb{R} \to E$ be such that $f$ is $C^n$ on $[a, b]$ and $g$ is $C^n$ on $[b, c]$, and
suppose that for every natural number $k \le n$ the $k$-th derivative of $f$ within $[a, b]$ and
the $k$-th derivative of $g$ within $[b, c]$ agree at $b$. Then the function equal to $f$ on
$[a, b]$ and to $g$ elsewhere is $C^n$ on $[a, c]$.

## Sources

- https://en.wikipedia.org/wiki/Piecewise#Continuity_and_differentiability_of_piecewise_functions

Stated but not proved: `MathlibExt.Analysis.Calculus.PiecewiseContDiffWanted.contDiffOn_piecewise_Icc` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/PiecewiseContDiffWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/PiecewiseContDiffWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/index.html#cont-diff-on-piecewise-icc).

## Odd Taylor polynomials of the exponential have exactly one real zero

For every odd
positive integer $n$, the polynomial $1+x+x^2/2!+\cdots+x^n/n!$ has exactly one real zero.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Polynomials, rational functions in real analysis), problem `ma_proofbench_l1_19`.

Stated but not proved: `MathlibExt.Analysis.Calculus.ExpTaylorPolyOddUniqueZeroWanted.existsUnique_sum_pow_div_factorial_eq_zero_of_odd` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/ExpTaylorPolyOddUniqueZeroWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/ExpTaylorPolyOddUniqueZeroWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/index.html#exists-unique-sum-pow-div-factorial-eq-z).

## The derivative of $x^2 \sin(1/x^2)$ exists everywhere but is not integrable

Let
$F : \mathbb{R} \to \mathbb{R}$ be given by $F(x) = x^2 \sin(1/x^2)$ for $x \ne 0$ and $F(0) = 0$.
Then $F$ is differentiable at every real $x$, but its derivative $F'$ is not Lebesgue integrable
on $[-1,1]$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of one variable), problem `ma_proofbench_l1_99`.

Stated but not proved: `MathlibExt.Analysis.Calculus.XSqSinInvSqNonintegrableDerivWanted.differentiable_and_not_integrableOn_deriv_sq_mul_sin_inv_sq` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/XSqSinInvSqNonintegrableDerivWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/XSqSinInvSqNonintegrableDerivWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/index.html#differentiable-and-not-integrable-on-der).

## The map $x \mapsto e^{x-1} - e^{1-x}$ has a unique fixed point

There is exactly one
real number $x$ such that $e^{x-1} - e^{1-x} = x$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of one variable), problem `ma_proofbench_l1_59`.

Stated but not proved: `MathlibExt.Analysis.SpecialFunctions.ExpSubExpUniqueFixedPointWanted.existsUnique_exp_sub_one_sub_exp_one_sub_eq_self` is written with `theorem_wanted` in [WantedExt/Analysis/SpecialFunctions/ExpSubExpUniqueFixedPointWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SpecialFunctions/ExpSubExpUniqueFixedPointWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/index.html#exists-unique-exp-sub-one-sub-exp-one-su).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Differential calculus of one variable](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/real-functions/differential-calculus)
