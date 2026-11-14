---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.BinaryQuotient.length_toBits, MIPRE.LowDegree.BinaryQuotient.ofBits_toBits, MIPRE.LowDegree.BinaryQuotient.toBits_ofBits, MIPRE.LowDegree.BinaryQuotient.evalBits_eq_iff, MIPRE.LowDegree.BinaryQuotient.ofBits_xor, MIPRE.LowDegree.BinaryQuotient.ofBits_mulReduce
statement: formalized
proof: formalized
---

# Canonical coordinates in monic binary quotients

For every monic $f\in\mathbb{F}_2[X]$ of degree $d$, the quotient $\mathbb{F}_2[X]/(f)$ has canonical $d$-bit coordinates in its power basis. Encoding and decoding are inverse on correctly sized lists, and equality of their root evaluations is equivalent to equality of the lists. The uniform XOR and reduced-multiplication programs implement quotient addition and multiplication. Irreducibility and squarefreeness are not required.

## Depends on

- [The low-degree code](../../structure-of-the-proof/part-07/def-ld-encoding.md)

## Proof

The monic power basis identifies each quotient element with its $d$ binary coefficients. The basis representation identities prove the two inverse laws. Evaluation at the canonical root equals decoding on fixed-width vectors. The root satisfies the monic reduction equation, so the generic XOR and Horner multiplication identities give the stated arithmetic. The constant-one modulus has a trivial quotient and empty coordinate vectors.

## Lean

Formalized as [`MIPRE.LowDegree.BinaryQuotient.length_toBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.length_toBits), [`MIPRE.LowDegree.BinaryQuotient.ofBits_toBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.ofBits_toBits), [`MIPRE.LowDegree.BinaryQuotient.toBits_ofBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.toBits_ofBits), [`MIPRE.LowDegree.BinaryQuotient.evalBits_eq_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.evalBits_eq_iff), [`MIPRE.LowDegree.BinaryQuotient.ofBits_xor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.ofBits_xor), [`MIPRE.LowDegree.BinaryQuotient.ofBits_mulReduce`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.ofBits_mulReduce).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6570](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6570)
