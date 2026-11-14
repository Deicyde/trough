---
declaration: definition
origin: cited
lean: Quotienting.polyQuotient
statement: formalized
---

# poly_quotient

Let $\hat{f}\in\mathbb{F}^{\lt d}[X]$ be a polynomial and $S\subseteq\mathbb{F}$ be a finite set with $|S|\led$, and let $\hat{V}_S(X):=\prod_{s\in S}(X-s)$, the unique monic polynomial of degree $|S|$ vanishing on $S$. The *polynomial quotient* $\mathsf{PolyQuotient}(\hat{f},S)\in\mathbb{F}^{\lt d-|S|}[X]$ is defined as follows:

$$
\mathsf{PolyQuotient}(\hat{f},S)(X):=\frac{\hat{f}(X)-\hat{\mathsf{Ans}}(X)}{\hat{V}_S(X)}
$$

where $\hat{\mathsf{Ans}}\in\mathbb{F}^{<|S|}[X]$ is the unique polynomial of degree less than $|S|$ interpolating $\hat{f}$ on $S$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Quotienting.polyQuotient`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Quotienting.polyQuotient).

## Sources

- [ArkLib blueprint: proof_systems/stir.tex, line 76](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/stir.tex#L76)
