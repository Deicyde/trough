---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.BinaryQuotient.orbitPolynomialBitsProg, MIPRE.LowDegree.BinaryQuotient.map_orbitPolynomialBits, MIPRE.LowDegree.BinaryQuotient.orbitPolynomialBits_monic_natDegree, MIPRE.LowDegree.BinaryQuotient.orbitPolynomialBits_eq_minpoly, MIPRE.LowDegree.BinaryQuotient.orbitPolynomialBits_irreducible
statement: formalized
proof: formalized
---

# Effective closed Frobenius orbit polynomials

Given a supplied monic irreducible binary modulus, a fixed-width representation of $a$ in its quotient field, and a unary integer $r$, a fixed polynomial-time program prints the binary coefficients of $\prod_{i=0}^{r-1}(X+a^{2^i})$ whenever $a^{2^r}=a$. The output polynomial is monic of degree $r$. If $r>0$ is the minimal-polynomial degree of $a$ over $\mathbb{F}_2$, the output is that minimal polynomial and is irreducible.

## Depends on

- [Canonical coordinates in monic binary quotients](lem-binary-monic-quotient.md)

## Proof

Repeated modular squaring constructs the orbit, and polynomial multiplication in the supplied quotient constructs the product. Closing the orbit makes each coefficient fixed by squaring. In a field of characteristic two such a coefficient is zero or one; faithful power-basis coordinates therefore justify reading its constant bit. The resulting binary polynomial vanishes at $a$. Minimal-polynomial divisibility, monicity, and equal degrees identify it with the minimal polynomial when the exact-degree hypothesis holds. All loops are bounded by supplied unary lengths and coefficient widths.

## Lean

Formalized as [`MIPRE.LowDegree.BinaryQuotient.orbitPolynomialBitsProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.orbitPolynomialBitsProg), [`MIPRE.LowDegree.BinaryQuotient.map_orbitPolynomialBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.map_orbitPolynomialBits), [`MIPRE.LowDegree.BinaryQuotient.orbitPolynomialBits_monic_natDegree`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.orbitPolynomialBits_monic_natDegree), [`MIPRE.LowDegree.BinaryQuotient.orbitPolynomialBits_eq_minpoly`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.orbitPolynomialBits_eq_minpoly), [`MIPRE.LowDegree.BinaryQuotient.orbitPolynomialBits_irreducible`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.orbitPolynomialBits_irreducible).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6693](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6693)
