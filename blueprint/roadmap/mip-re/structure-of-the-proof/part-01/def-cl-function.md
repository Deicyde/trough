---
declaration: definition
origin: cited
lean: MIPRE.CL.CLFun, MIPRE.CL.CLFun.eval, MIPRE.CL.CLFun.SupportedOn, MIPRE.CL.IsCLFun, MIPRE.CL.clDist
statement: formalized
---

# Conditionally linear function

Let $V = \mathbb{F}^n$ for a finite field $\mathbb{F}$ and $n \geq 0$. A *register subspace* of $V$ is the span of a subset of the standard basis; for a register subspace $W$ and $x \in V$, $x^W$ denotes the projection of $x$ onto $W$ along the complementary register subspace. For $\ell \geq 0$, the *$\ell$-level conditionally linear (CL) functions* on $V$ are defined inductively: the only $0$-level CL function is the zero function on $V$; for $\ell \geq 1$, an $\ell$-level CL function is a function $L : V \to V$ of the form

$$
L(x) = L_1\bigl(x^{V_1}\bigr) + L_{>1,\, L_1(x^{V_1})}\bigl(x^{V_{>1}}\bigr)
$$

for complementary register subspaces $V = V_1 \oplus V_{>1}$, a linear map $L_1 : V_1 \to V_1$, and, for each $v$ in the range of $L_1$, an $(\ell-1)$-level CL function $L_{>1,v}$ on $V_{>1}$. A *CL distribution* is the distribution of $(L^\textsc{A}(x), L^\textsc{B}(x))$ for uniformly random $x \in V$ and CL functions $L^\textsc{A}, L^\textsc{B}$ on $V$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MIPRE.CL.CLFun`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun), [`MIPRE.CL.CLFun.eval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.eval), [`MIPRE.CL.CLFun.SupportedOn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.SupportedOn), [`MIPRE.CL.IsCLFun`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.IsCLFun), [`MIPRE.CL.clDist`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.clDist).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 39](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L39)
