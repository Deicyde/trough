---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.BinaryQuotient.factorBitsProg, MIPRE.LowDegree.BinaryQuotient.factorBitsProg_factors, MIPRE.LowDegree.BinaryQuotient.factorBitsProg_prod
statement: formalized
proof: formalized
---

# Deterministic squarefree binary factorization

A fixed deterministic polynomial-time program factors every nonconstant monic squarefree polynomial over $\mathbb{F}_2$, given its lower coefficient bits. Every printed factor is monic and irreducible, and their product is the input.

## Depends on

- [Effective Frobenius fixed spaces in binary quotients](lem-binary-quotient-fixed-space.md)
- [Canonical binary Euclidean algorithms](lem-binary-euclidean-algorithms.md)

## Proof

Start with the identity idempotent and split each retained component by each computed Frobenius-fixed generator, discarding zero components. Orthogonality bounds the number of nonzero components by the quotient dimension. A component that no generator splits is primitive, since the generators span all idempotents. For a primitive component represented by $E$, compute $\mathrm{gcd}(f,E-1)$ with the verified Euclidean program. Divisibility by this gcd is equivalent to annihilation by $E$ in the quotient. Bijectivity of squaring and primitivity make the corresponding quotient a field, proving irreducibility. Orthogonal components yield coprime factors, while their sum is the identity; the resulting factors therefore reconstruct $f$. The executable splitting loop caps intermediate lists at the input dimension, providing a polynomial bound on every raw input as well as on inputs satisfying the squarefree contract.

## Lean

Formalized as [`MIPRE.LowDegree.BinaryQuotient.factorBitsProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.factorBitsProg), [`MIPRE.LowDegree.BinaryQuotient.factorBitsProg_factors`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.factorBitsProg_factors), [`MIPRE.LowDegree.BinaryQuotient.factorBitsProg_prod`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.factorBitsProg_prod).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6666](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6666)
