---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.BoundedPuncturedPlaneConstWanted.eqOn_const_of_differentiableOn_compl_zero_of_bounded, MathlibExt.Analysis.Complex.EntireIteratedDerivPolyWanted.exists_polynomial_of_iteratedDeriv_eq_polynomial, MathlibExt.Analysis.Complex.EntireSublinearGrowthConstantWanted.exists_const_of_differentiable_of_tendsto_div_self_zero
statement: formalized
---

# Liouville-type theorems

3 results, 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/liouville-type-theorems/index.html).

## Bounded holomorphic functions on the punctured plane are constant

Let
$f : \mathbb{C} \to \mathbb{C}$ be holomorphic on $\mathbb{C} \setminus \{0\}$, and suppose that
there is a real number $C$ with $|f(z)| \le C$ for every $z \ne 0$. Then there is a constant
$c \in \mathbb{C}$ with $f(z) = c$ for every $z \ne 0$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functions of a complex variable; Entire and meromorphic functions of one complex variable, and related topics), problem `ma_proofbench_l1_84`.

Stated but not proved: `MathlibExt.Analysis.Complex.BoundedPuncturedPlaneConstWanted.eqOn_const_of_differentiableOn_compl_zero_of_bounded` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/BoundedPuncturedPlaneConstWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/BoundedPuncturedPlaneConstWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/liouville-type-theorems/index.html#eq-on-const-of-differentiable-on-compl-z).

## An entire function with a polynomial derivative is a polynomial

Let $k$ be a positive
integer and let $f : \mathbb{C} \to \mathbb{C}$ be an entire function. If there is a complex
polynomial $p$ such that the $k$th derivative of $f$ satisfies $f^{(k)}(z) = p(z)$ for all
$z \in \mathbb{C}$, then there is a complex polynomial $q$ such that $f(z) = q(z)$ for all
$z \in \mathbb{C}$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functions of a complex variable; Entire and meromorphic functions of one complex variable, and related topics), problem `ma_proofbench_l1_90`.

Stated but not proved: `MathlibExt.Analysis.Complex.EntireIteratedDerivPolyWanted.exists_polynomial_of_iteratedDeriv_eq_polynomial` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/EntireIteratedDerivPolyWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/EntireIteratedDerivPolyWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/liouville-type-theorems/index.html#exists-polynomial-of-iterated-deriv-eq-p).

## An entire function of sublinear growth is constant

Let $f : \mathbb{C} \to \mathbb{C}$
be an entire function such that $f(z)/z \to 0$ as $|z| \to \infty$. Then $f$ is constant: there
is $c \in \mathbb{C}$ with $f(z) = c$ for all $z \in \mathbb{C}$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functions of a complex variable; Entire and meromorphic functions of one complex variable, and related topics), problem `ma_proofbench_l2_28`.

Stated but not proved: `MathlibExt.Analysis.Complex.EntireSublinearGrowthConstantWanted.exists_const_of_differentiable_of_tendsto_div_self_zero` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/EntireSublinearGrowthConstantWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/EntireSublinearGrowthConstantWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/liouville-type-theorems/index.html#exists-const-of-differentiable-of-tendst).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Liouville-type theorems](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/liouville-type-theorems/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/entire-functions/liouville-type-theorems)
