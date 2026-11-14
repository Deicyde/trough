---
declaration: definition
origin: cited
lean: MIPRE.Tailored.TailoredVerifier.repTV, MIPRE.Tailored.TailoredVerifier.qEquiv, MIPRE.Tailored.TailoredVerifier.RepSpec
statement: formalized
---

# Repeated tailored verifiers and the specification of their programs

The repeated verifier of $\mathsf{V}$ at $(\lambda, \tau)$ has the repeated sampler of Theorem [Parallel repetition of normal form verifiers](../../structure-of-the-proof/part-09/thm-parallel-repetition.md), $k(n) = 2^{\tau(\left\vert {\lambda} \right\vert + \left\vert {n} \right\vert)}$ independent copies of $\mathsf{V}$'s, and two programs $\mathcal{L}$ and $\mathcal{P}$. Call a question of the $n$-th game *good* when $\mathsf{V}$'s answer-length calculator halts at each of its coordinates. The programs *meet the specification* at $n$ when $\mathcal{L}$ outputs at a good question the sums of the coordinates' lengths and halts at no other question, and $\mathcal{P}$, at good questions and readable answers of the right lengths, halts exactly when $\mathsf{V}$'s linear-constraints processor halts on every coordinate, and then outputs the constraints of the $k(n)$-fold product of $\mathsf{V}_n$.

## Depends on

- [Tailored normal form verifier; II:1758](../part-01/def-tailored-verifier.md)
- [The $k$-fold tailored product; II:11377, direct form](def-tailored-product.md)
- [Direct sums of families, and their distributions](../../structure-of-the-proof/part-01/lem-cl-famsum.md)
- [Efficient s-m-n](../../computability/lem-smn.md)

## Lean

Formalized as [`MIPRE.Tailored.TailoredVerifier.repTV`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.repTV), [`MIPRE.Tailored.TailoredVerifier.qEquiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.qEquiv), [`MIPRE.Tailored.TailoredVerifier.RepSpec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.RepSpec).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1196](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1196)
