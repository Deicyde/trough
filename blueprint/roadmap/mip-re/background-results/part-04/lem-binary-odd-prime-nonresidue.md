---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.BinaryPolynomial.nonresidueLiftBitsProg, MIPRE.LowDegree.BinaryPolynomial.nonresidueLiftBitsProg_correct, MIPRE.LowDegree.BinaryPolynomial.nonresidueLiftBits_order, MIPRE.LowDegree.BinaryPolynomial.nonresidueLiftBits_degree_coprime
statement: formalized
proof: formalized
---

# Effective odd-prime nonresidues

For every odd prime $q$, a fixed polynomial-time program on unary $q$ prints a canonical monic irreducible binary polynomial $f$ of degree $m=\mathrm{ord}_q(2)$, with $\mathrm{gcd}(q,m)=1$, such that the specified root of $f$ in $\mathbb{F}_2[X]/(f)$ has no $q$th root in that field.

## Depends on

- [Deterministic squarefree binary factorization](lem-binary-squarefree-factorization.md)

## Proof depends on

- [Effective indexing and padding arithmetic](../../structure-of-the-proof/part-07/lem-pcp-padding-programs.md)

## Proof

Choose the first irreducible factor of the squarefree cyclotomic polynomial $\Phi_q$. Repeatedly factor $f(X^q)$. A singleton factor list certifies that the current root is a nonresidue; retain the current polynomial and stop. Otherwise, every factor has the original degree $m$, and the first factor advances the primitive-root order from $q^j$ to $q^{j+1}$. The order of a nonzero element of a field of size $2^m$ bounds the number of advances by $m$, so $m$ iterations suffice. Every query is squarefree by its cyclotomic invariant. Clipping each nonterminal choice to the initial coefficient width bounds all raw executions; the exact-degree invariant shows that clipping preserves valid executions.

## Lean

Formalized as [`MIPRE.LowDegree.BinaryPolynomial.nonresidueLiftBitsProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.nonresidueLiftBitsProg), [`MIPRE.LowDegree.BinaryPolynomial.nonresidueLiftBitsProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.nonresidueLiftBitsProg_correct), [`MIPRE.LowDegree.BinaryPolynomial.nonresidueLiftBits_order`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.nonresidueLiftBits_order), [`MIPRE.LowDegree.BinaryPolynomial.nonresidueLiftBits_degree_coprime`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.nonresidueLiftBits_degree_coprime).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6721](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6721)
