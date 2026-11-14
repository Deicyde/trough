---
declaration: lemma
origin: cited
lean: Polynomial.FoldingPolynomial.foldingPolynomial, Polynomial.FoldingPolynomial.substitution_property_of_folding_polynomial, Polynomial.FoldingPolynomial.folding_polynomial_deg_x, Polynomial.FoldingPolynomial.folding_polynomial_deg_y_bound, Polynomial.FoldingPolynomial.folding_polynomial_is_unique, Polynomial.FoldingPolynomial.folding_polynomial_deg_x_bound, Polynomial.FoldingPolynomial.folded_poly_degree_bound
statement: formalized
---

# poly_folding

Given a non-constant polynomial $\hat{q}\in\mathbb{F}[X]$:

- For every univariate polynomial $\hat{f}\in\mathbb{F}[X]$, there exists a unique bivariate polynomial $\hat{Q}\in\mathbb{F}[X,Y]$ with:

    $$
    \mathsf{deg}_X(\hat{Q}) := \left\lfloor \frac{\mathsf{deg}(\hat{f})}{\mathsf{deg}(\hat{q})} \right\rfloor,\quad \mathsf{deg}_Y(\hat{Q}) < \mathsf{deg}(\hat{q})
    $$

    such that $\hat{f}(Z)=\hat{Q}(\hat{q}(Z),Z)$. Observe that if $\mathsf{deg}(\hat{f})\lt t\cdot\mathsf{deg}(\hat{q})$ then $\mathsf{deg}_X(\hat{Q})\lt t$.

- For every $\hat{Q}[X,Y]$ with $\mathsf{deg}_X(\hat{Q})\lt t$ and $\mathsf{deg}_Y(\hat{Q})\lt \mathsf{deg}(\hat{q})$, the polynomial $\hat{f}(Z)=\hat{Q}(\hat{q}(Z),Z)$ has degree $\mathsf{deg}(\hat{f})\lt t\cdot\mathsf{deg}(\hat{q})$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Stated as [`Polynomial.FoldingPolynomial.foldingPolynomial`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Polynomial.FoldingPolynomial.foldingPolynomial), [`Polynomial.FoldingPolynomial.substitution_property_of_folding_polynomial`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Polynomial.FoldingPolynomial.substitution_property_of_folding_polynomial), [`Polynomial.FoldingPolynomial.folding_polynomial_deg_x`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Polynomial.FoldingPolynomial.folding_polynomial_deg_x), [`Polynomial.FoldingPolynomial.folding_polynomial_deg_y_bound`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Polynomial.FoldingPolynomial.folding_polynomial_deg_y_bound), [`Polynomial.FoldingPolynomial.folding_polynomial_is_unique`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Polynomial.FoldingPolynomial.folding_polynomial_is_unique), [`Polynomial.FoldingPolynomial.folding_polynomial_deg_x_bound`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Polynomial.FoldingPolynomial.folding_polynomial_deg_x_bound), [`Polynomial.FoldingPolynomial.folded_poly_degree_bound`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Polynomial.FoldingPolynomial.folded_poly_degree_bound); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/stir.tex, line 127](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/stir.tex#L127)
