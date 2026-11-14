---
declaration: definition
origin: cited
lean: MIPRE.Tailored.RepProg.repLen, MIPRE.Tailored.RepProg.repLp, MIPRE.Tailored.RepProg.lenCore, MIPRE.Tailored.RepProg.lpCore, MIPRE.Tailored.Calls.mapCall
statement: formalized
---

# The repeated programs

The repeated answer-length calculator, on $(n, x, \kappa)$ with the input sampler and calculator stored, asks the sampler for the dimension $s$, computes $k = k(n)$, cuts $x$ into its $k$ blocks of $s$ bits, runs the input calculator on every block at both kinds, and outputs the concatenation of the outputs at the kind $\kappa$. The repeated linear-constraints processor, on $(n, x, y, a^R, b^R)$, does the same for both questions, cuts $a^R$ and $b^R$ into the coordinates' readable answers by the lengths it obtained, runs the input processor on every coordinate, and outputs every coordinate's constraints padded as in Definition [The $k$-fold tailored product; II:11377, direct form](def-tailored-product.md). Both are fixed programs with the input programs stored; every stage between the calls to the input programs is a polynomial-time function, and the calls go through one loop running a stored program on every element of a list through the universal machine.

## Depends on

- [Effective self-dualization of a supplied normal basis](../../background-results/part-05/lem-effective-normal-selfdualization.md)
- [Tailored normal form verifier; II:1758](../part-01/def-tailored-verifier.md)

## Lean

Formalized as [`MIPRE.Tailored.RepProg.repLen`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.RepProg.repLen), [`MIPRE.Tailored.RepProg.repLp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.RepProg.repLp), [`MIPRE.Tailored.RepProg.lenCore`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.RepProg.lenCore), [`MIPRE.Tailored.RepProg.lpCore`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.RepProg.lpCore), [`MIPRE.Tailored.Calls.mapCall`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Calls.mapCall).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1251](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1251)
