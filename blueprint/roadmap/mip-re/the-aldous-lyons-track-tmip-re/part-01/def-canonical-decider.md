---
declaration: definition
origin: cited
lean: MIPRE.Tailored.canonProg, MIPRE.Tailored.canonFinal, MIPRE.Tailored.satF, MIPRE.Tailored.allSatF, MIPRE.Cost.Prog.pushProg
statement: formalized
---

# The canonical decider, as a program; II:1757–1787

The *canonical decider* of a tailored verifier with answer-length calculator $\mathcal{L}$ and linear-constraints processor $\mathcal{P}$ is the program that, on $(n, x, y, a, b)$, runs $\mathcal{L}$ on $(n, x, \kappa)$ and on $(n, y, \kappa)$ for both kinds $\kappa$ of variables, then $\mathcal{P}$ on $(n, x, y, a^R, b^R)$, where $a^R$ and $b^R$ are the first $\ell^R(x)$ bits of $a$ and the first $\ell^R(y)$ bits of $b$, and accepts when $\left\vert {a} \right\vert = \ell^R(x) + \ell^L(x)$, $\left\vert {b} \right\vert = \ell^R(y) + \ell^L(y)$, and every constraint $c$ that $\mathcal{P}$ outputs has the length of $(a, b, 1)$ and satisfies $\langle c, (a, b, 1)\rangle = 0$ over $\mathbb{F}_2$. It is a sequence of steps, each of which runs one of the two programs on an input computed in polynomial time from the state and pushes the output onto the state, followed by the check, computed in polynomial time.

## Depends on

- [Tailored normal form verifier; II:1758](def-tailored-verifier.md)
- [Effective binary matrix arithmetic and elimination](../../background-results/part-05/lem-effective-binary-linear-algebra.md)
- [Effective indexing and padding arithmetic](../../structure-of-the-proof/part-07/lem-pcp-padding-programs.md)

## Lean

Formalized as [`MIPRE.Tailored.canonProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.canonProg), [`MIPRE.Tailored.canonFinal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.canonFinal), [`MIPRE.Tailored.satF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.satF), [`MIPRE.Tailored.allSatF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.allSatF), [`MIPRE.Cost.Prog.pushProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Prog.pushProg).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 370](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L370)
