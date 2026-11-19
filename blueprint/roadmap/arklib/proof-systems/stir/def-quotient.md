---
declaration: definition
origin: cited
lean: Quotienting.funcQuotient
statement: formalized
---

# quotient

Let $f:\mathcal{L}\to\mathbb{F}$ be a function, $S\subseteq\mathbb{F}$ be a finite set, and $\mathsf{Ans},\mathsf{Fill}: S\rightarrow\mathbb{F}$ be functions. Let $\hat{\mathsf{Ans}}\in\mathbb{F}^{<|S|}[X]$ be the unique polynomial of degree less than $|S|$ with $\hat{\mathsf{Ans}}(x)=\mathsf{Ans}(x)$ for every $x\in S$ (the zero polynomial when $S$ is empty), and let $\hat{V}_S(X):=\prod_{s\in S}(X-s)$, the unique monic polynomial of degree $|S|$ vanishing on $S$. The *quotient function* $\mathsf{Quotient}\bigl(f,S,\mathsf{Ans},\mathsf{Fill}\bigr): \mathcal{L}\to\mathbb{F}$ is defined as follows:

$$
\forall x \in \mathcal{L}, \quad
\mathsf{Quotient}\bigl(f, S, \mathsf{Ans}, \mathsf{Fill} \bigr)(x)
:=
\left\{
\begin{array}{ll}
\mathsf{Fill}(x)
& \text{if } x \in S \\[6pt]
\dfrac{f(x) - \hat{\mathsf{Ans}}(x)}{\hat{V}_S(x)}
& \text{otherwise}
\end{array}
\right.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Quotienting.funcQuotient`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Quotienting.funcQuotient).

## Sources

- [ArkLib blueprint: proof_systems/stir.tex, line 51](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/stir.tex#L51)
