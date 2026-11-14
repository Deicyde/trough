---
declaration: definition
origin: cited
lean: Polynomial.FoldingPolynomial.polyFold, Polynomial.FoldingPolynomial.polyFold_natDegree_le
statement: formalized
---

# poly_folding

Given a polynomial $\hat{f}\in\mathbb{F}[X]$, a folding parameter $k\in\mathbb{N}$ with $k\ge1$ and $r\in\mathbb{F}$, we define a polynomial $\mathsf{PolyFold}(\hat{f},k,r)\in\mathbb{F}[X]$ as follows. Let $\hat{Q}[X,Y]$ be the bivariate polynomial derived from $\hat{f}$ using Fact [poly_folding](fact-poly-folding.md) with the non-constant polynomial $\hat{q}(X):=X^k$. Then $\mathsf{PolyFold}(\hat{f},k,r)(X):=\hat{Q}(X,r)$. Its degree is at most $\lfloor\mathsf{deg}(\hat{f})/k\rfloor$.

## Depends on

- [poly_folding](fact-poly-folding.md)

## Lean

Formalized as [`Polynomial.FoldingPolynomial.polyFold`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Polynomial.FoldingPolynomial.polyFold), [`Polynomial.FoldingPolynomial.polyFold_natDegree_le`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Polynomial.FoldingPolynomial.polyFold_natDegree_le).

## Sources

- [ArkLib blueprint: proof_systems/stir.tex, line 153](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/stir.tex#L153)
