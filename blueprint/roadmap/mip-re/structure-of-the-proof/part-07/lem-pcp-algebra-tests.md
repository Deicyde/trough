---
declaration: lemma
origin: cited
lean: MIPRE.SAT.PcpAlgebra.completeness, MIPRE.SAT.PcpAlgebra.degreeOf_constraint_le, MIPRE.SAT.PcpAlgebra.degreeOf_zeroCombination_le, MIPRE.SAT.PcpAlgebra.identities_of_majority, MIPRE.SAT.PcpAlgebra.clause_satisfied_of_identities, MIPRE.SAT.PcpAlgebra.clause_decoded_of_identities, MIPRE.LowDegree.eq_of_majority_agree, MIPRE.LowDegree.eq_of_majority_subset
statement: formalized
proof: formalized
---

# The algebraic PCP tests

Write $p=\varphi\prod_{i=1}^5(g_i-X_{s_i})$ and $z_c=\sum_j c_jX_j(1-X_j)$. The algebraic verifier tests $c_0=p$ and $c_0=z_c$ at its sampled point. If $p$ vanishes on the Boolean cube and has individual degree at most $d$, certificates of individual degree at most $d$ pass both tests everywhere. Conversely, if $\varphi$ has individual degree at most six, all $g_i,c_j,c_0$ have individual degree at most $d$, and $|\mathbb{F}|\geq 2m(6+5\max\{d,1\})$, acceptance on more than half of $\mathbb{F}^m$ forces both polynomial identities. On each Boolean point with $\varphi=1$, one of the five answer evaluations equals its sign.

## Depends on

- [Boolean-cube zero certificates](lem-pcp-zero-basis.md)
- [Schwartz–Zippel](../../background-results/part-05/lem-schwartz-zippel.md)

## Proof

Completeness uses Lemma [Boolean-cube zero certificates](lem-pcp-zero-basis.md). For soundness, the two tested polynomials have individual degree at most $6+5\max\{d,1\}$ and $d+2$, respectively. Schwartz–Zippel forces equality from strict majority agreement. Evaluation on the Boolean cube annihilates every zero-certificate term, so the product of the five literal factors is zero on a described clause. This is the algebraic component only: padding, answer-block embeddings, decoded answer strings and the ambient verifier program remain separate obligations.

## Lean

Formalized as [`MIPRE.SAT.PcpAlgebra.completeness`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpAlgebra.completeness), [`MIPRE.SAT.PcpAlgebra.degreeOf_constraint_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpAlgebra.degreeOf_constraint_le), [`MIPRE.SAT.PcpAlgebra.degreeOf_zeroCombination_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpAlgebra.degreeOf_zeroCombination_le), [`MIPRE.SAT.PcpAlgebra.identities_of_majority`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpAlgebra.identities_of_majority), [`MIPRE.SAT.PcpAlgebra.clause_satisfied_of_identities`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpAlgebra.clause_satisfied_of_identities), [`MIPRE.SAT.PcpAlgebra.clause_decoded_of_identities`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpAlgebra.clause_decoded_of_identities), [`MIPRE.LowDegree.eq_of_majority_agree`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.eq_of_majority_agree), [`MIPRE.LowDegree.eq_of_majority_subset`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.eq_of_majority_subset).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 5034](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5034)
