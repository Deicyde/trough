---
declaration: lemma
origin: cited
lean: Quotienting.quotienting
statement: formalized
---

# quotienting

Let $f:\mathcal{L}\rightarrow\mathbb{F}$ be a function, $d\in\mathbb{N}$ be the degree parameter with $d\le|\mathcal{L}|$, $\delta\in(0,1)$ be a distance parameter, $S\subseteq\mathbb{F}$ be a set with $|S|\lt d$, and $\mathsf{Ans},\mathsf{Fill}:S\rightarrow\mathbb{F}$ are functions. Suppose that for every $u\in\mathsf{List}(f,d,\delta)$ there exists $x\in S$ with $\hat{u}(x)\neq\mathsf{Ans}(x)$. Then

$$
\Delta(\mathsf{Quotient}(f,S,\mathsf{Ans},\mathsf{Fill}),\mathrm{RS}[\mathbb{F},\mathcal{L},d-|S|])+\frac{|T|}{|\mathcal{L}|}>\delta,
$$

where $T:=\{x\in\mathcal{L}\cap S: \hat{\mathsf{Ans}}(x)\neq f(x)\}$.

## Depends on

- [quotient](def-quotient.md)
- [Reed-Solomon Code](../../supporting-theories/coding-theory/def-reed-solomon-code.md)
- [Distance from a Code](../../supporting-theories/coding-theory/def-distance-from-code.md)
- [List of Close Codewords](../../supporting-theories/coding-theory/def-list-close-codewords.md)

## Lean

Stated as [`Quotienting.quotienting`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Quotienting.quotienting); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/stir.tex, line 88](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/stir.tex#L88)
