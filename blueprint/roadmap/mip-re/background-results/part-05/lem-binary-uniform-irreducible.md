---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.BinaryPolynomial.irreducibleBitsProg, MIPRE.LowDegree.BinaryPolynomial.irreducibleBits_correct, MIPRE.LowDegree.BinaryPolynomial.irreducibleBits_length, MIPRE.LowDegree.BinaryPolynomial.irreducibleBitsProg_time_le, MIPRE.LowDegree.exists_shoup_irreducible, MIPRE.LowDegree.shoupIrreducible, MIPRE.LowDegree.shoupIrreducible_monic, MIPRE.LowDegree.shoupIrreducible_irreducible, MIPRE.LowDegree.shoupIrreducible_natDegree
statement: formalized
proof: formalized
---

# Uniform deterministic binary irreducible polynomials

There is one fixed deterministic ambient program and one polynomial $R$ such that, on unary input $n\geq1$, the program prints $n+1$ coefficient bits of a monic irreducible polynomial over $\mathbb{F}_2$ of degree $n$ within $R(n)$ steps. The same bound includes degree zero, where the program returns the constant polynomial one. The public constructor `shoupIrreducible` is this specified program, and `exists_shoup_irreducible` is a proved theorem.

## Depends on

- [Effective irreducibles of every power-of-two degree](../part-04/lem-binary-power-two-irreducible.md)
- [Effective irreducibles of every odd-prime-power degree](../part-04/lem-binary-odd-prime-power-irreducible.md)
- [Effective combination of coprime degrees](../part-04/lem-binary-coprime-degree-combination.md)
- [Effective unary prime-power decomposition](../part-04/lem-binary-degree-decomposition.md)

## Proof

Compute the unary prime-power decomposition of $n$ and dispatch each contribution to the power-of-two or odd-prime-power constructor; neutral contributions use $X$. Starting from $X$, fold the coprime-degree combination over this ordered list. The degrees are pairwise coprime and have product $n$. Every intermediate degree is at most $n$, so clipping the lower coefficients to the original unary input length preserves each valid step and gives a global fold bound. Append the leading coefficient to obtain the exact $n+1$-bit output. The composite `PolyTimeFun` supplies a polynomial bound on actual encoded execution; substituting the unary encoding size $2n+1$ gives the displayed polynomial $R$. No existential choice is used to select the program.

## Lean

Formalized as [`MIPRE.LowDegree.BinaryPolynomial.irreducibleBitsProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.irreducibleBitsProg), [`MIPRE.LowDegree.BinaryPolynomial.irreducibleBits_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.irreducibleBits_correct), [`MIPRE.LowDegree.BinaryPolynomial.irreducibleBits_length`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.irreducibleBits_length), [`MIPRE.LowDegree.BinaryPolynomial.irreducibleBitsProg_time_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.irreducibleBitsProg_time_le), [`MIPRE.LowDegree.exists_shoup_irreducible`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.exists_shoup_irreducible), [`MIPRE.LowDegree.shoupIrreducible`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.shoupIrreducible), [`MIPRE.LowDegree.shoupIrreducible_monic`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.shoupIrreducible_monic), [`MIPRE.LowDegree.shoupIrreducible_irreducible`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.shoupIrreducible_irreducible), [`MIPRE.LowDegree.shoupIrreducible_natDegree`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.shoupIrreducible_natDegree).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6868](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6868)
