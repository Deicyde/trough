---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.DegreeArithmetic.modUnaryProg, MIPRE.LowDegree.DegreeArithmetic.dvdUnaryProg, MIPRE.LowDegree.DegreeArithmetic.mulUnaryProg, MIPRE.LowDegree.DegreeArithmetic.primeUnaryProg, MIPRE.LowDegree.DegreeArithmetic.primeUnary_eq, MIPRE.LowDegree.DegreeArithmetic.primePowerUnaryProg, MIPRE.LowDegree.DegreeArithmetic.primePowerUnary_correct, MIPRE.LowDegree.DegreeArithmetic.primePowerPairsProg, MIPRE.LowDegree.DegreeArithmetic.primePowerPairs_eq, MIPRE.LowDegree.DegreeArithmetic.primePowerPairs_prod, MIPRE.LowDegree.DegreeArithmetic.primePowerPairs_pairwise, MIPRE.LowDegree.BinaryDegreeFactors.degreeFactors_prod, MIPRE.LowDegree.BinaryDegreeFactors.degreeFactors_pairwise, MIPRE.LowDegree.BinaryDegreeFactors.degreeFactors_dvd, MIPRE.LowDegree.BinaryDegreeFactors.degreeFactors_pos, MIPRE.LowDegree.BinaryDegreeFactors.degreeFactors_le, MIPRE.LowDegree.BinaryDegreeFactors.prefix_prod_dvd
statement: formalized
proof: formalized
---

# Effective unary prime-power decomposition

A fixed polynomial-time program on unary $n$ prints, in ascending base order, the pairs $(q,q^{v_q(n)})$ for $0\leq q\leq n$, with exponent zero at nonprime indices. For $n>0$, the second coordinates are positive, pairwise coprime, and have product $n$. Each listed degree, and every prefix product, divides $n$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Enumerate the unary indices from zero through $n$, test primality by trial division, and compute the largest dividing prime power by bounded unary multiplication and divisibility tests. Each arithmetic routine has a polynomial bound on all inputs. The resulting list agrees with the proof-only list $q^{n.\mathrm{factorization}(q)}$. Unique factorization gives its product; distinct prime indices give coprime powers, and all other indices contribute one. Divisibility of entries and prefix products follows from the product identity. The mathematical factorization function appears only in correctness proofs, not in the executable program.

## Lean

Formalized as [`MIPRE.LowDegree.DegreeArithmetic.modUnaryProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.DegreeArithmetic.modUnaryProg), [`MIPRE.LowDegree.DegreeArithmetic.dvdUnaryProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.DegreeArithmetic.dvdUnaryProg), [`MIPRE.LowDegree.DegreeArithmetic.mulUnaryProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.DegreeArithmetic.mulUnaryProg), [`MIPRE.LowDegree.DegreeArithmetic.primeUnaryProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.DegreeArithmetic.primeUnaryProg), [`MIPRE.LowDegree.DegreeArithmetic.primeUnary_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.DegreeArithmetic.primeUnary_eq), [`MIPRE.LowDegree.DegreeArithmetic.primePowerUnaryProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.DegreeArithmetic.primePowerUnaryProg), [`MIPRE.LowDegree.DegreeArithmetic.primePowerUnary_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.DegreeArithmetic.primePowerUnary_correct), [`MIPRE.LowDegree.DegreeArithmetic.primePowerPairsProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.DegreeArithmetic.primePowerPairsProg), [`MIPRE.LowDegree.DegreeArithmetic.primePowerPairs_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.DegreeArithmetic.primePowerPairs_eq), [`MIPRE.LowDegree.DegreeArithmetic.primePowerPairs_prod`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.DegreeArithmetic.primePowerPairs_prod), [`MIPRE.LowDegree.DegreeArithmetic.primePowerPairs_pairwise`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.DegreeArithmetic.primePowerPairs_pairwise), [`MIPRE.LowDegree.BinaryDegreeFactors.degreeFactors_prod`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryDegreeFactors.degreeFactors_prod), [`MIPRE.LowDegree.BinaryDegreeFactors.degreeFactors_pairwise`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryDegreeFactors.degreeFactors_pairwise), [`MIPRE.LowDegree.BinaryDegreeFactors.degreeFactors_dvd`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryDegreeFactors.degreeFactors_dvd), [`MIPRE.LowDegree.BinaryDegreeFactors.degreeFactors_pos`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryDegreeFactors.degreeFactors_pos), [`MIPRE.LowDegree.BinaryDegreeFactors.degreeFactors_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryDegreeFactors.degreeFactors_le), [`MIPRE.LowDegree.BinaryDegreeFactors.prefix_prod_dvd`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryDegreeFactors.prefix_prod_dvd).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6830](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6830)
