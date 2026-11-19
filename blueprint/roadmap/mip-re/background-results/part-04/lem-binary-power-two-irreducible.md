---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.BinaryArtinSchreier.powerTwoBitsProg, MIPRE.LowDegree.BinaryArtinSchreier.powerTwoBits_correct, MIPRE.LowDegree.BinaryArtinSchreier.powerTwoBits_length
statement: formalized
proof: formalized
---

# Effective irreducibles of every power-of-two degree

A fixed polynomial-time program, given the requested degree $2^e$ in unary, prints exactly $2^e+1$ coefficient bits of a monic irreducible polynomial of degree $2^e$ over $\mathbb{F}_2$, for every $e\geq 0$.

## Depends on

- [Effective closed Frobenius orbit polynomials](lem-binary-orbit-polynomial.md)
- [Effective normalization of binary polynomials](lem-binary-polynomial-normalization.md)

## Proof

Degree one uses $X$, and degree two starts from $X^2+X+1$. At each later stage, the current root $\alpha$ has the invariant that $Y^2+Y+(\alpha^3+\alpha^2)$ is irreducible. The quadratic-basis calculation preserves this invariant at the next root. Compute the closed orbit polynomial of $\alpha^3+\alpha^2$ over the current field and substitute $X^2+X$; the result is monic of twice the current degree. The new quadratic root lies outside the current field, and the power-of-two subfield divisibility argument proves its full doubled degree. The executable loop stops when the requested width is reached and caps intermediate coefficients by that width. Its fuel is the unary requested degree, so even malformed inputs satisfy one polynomial bound.

## Lean

Formalized as [`MIPRE.LowDegree.BinaryArtinSchreier.powerTwoBitsProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryArtinSchreier.powerTwoBitsProg), [`MIPRE.LowDegree.BinaryArtinSchreier.powerTwoBits_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryArtinSchreier.powerTwoBits_correct), [`MIPRE.LowDegree.BinaryArtinSchreier.powerTwoBits_length`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryArtinSchreier.powerTwoBits_length).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6748](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6748)
