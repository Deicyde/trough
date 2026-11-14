---
declaration: lemma
origin: cited
lean: MIPRE.SAT.PcpAlgebra.degreeOf_liftAnswer_le, MIPRE.SAT.PcpAlgebra.literal_product_degree_le, MIPRE.SAT.PcpAlgebra.honest_constraint_degree_le, MIPRE.SAT.PcpAlgebra.typedAccepts_ev_iff, MIPRE.SAT.PcpAlgebra.exists_proof_of_satisfying_assignment, MIPRE.SAT.PcpAlgebra.decoded_clause_of_majority
statement: formalized
proof: formalized
---

# PCP answer blocks, honest proof and decoded clauses

Embed each of the five answer polynomials in its own coordinate block of the $m'$-variate point, with distinct sign coordinates outside those blocks. This preserves individual degree, and for multilinear answers the product of the five literal factors is multilinear. Consequently a degree-six Boolean clause-description polynomial and a satisfying five-tuple of Boolean assignments give a degree-seven PCP proof passing both algebraic tests at every point. Conversely, for $q\geq82m'$, strict majority acceptance of a degree-seven proof implies that the Boolean decoding satisfies every described Boolean clause. These are statements about the existing PCP proof type and its typed evaluations.

## Depends on

- [The algebraic PCP tests](lem-pcp-algebra-tests.md)
- [The low-degree code](def-ld-encoding.md)

## Proof

Injectivity of each coordinate embedding preserves degrees; the images of different blocks, and their sign coordinates, are disjoint. A coordinate therefore contributes degree at most one to the literal product. Encode the five assignments multilinearly and apply the zero-basis decomposition to the degree-seven constraint. For soundness, transport the degree bounds to the ambient point and use Lemma [The algebraic PCP tests](lem-pcp-algebra-tests.md). Any answer evaluation equal to its Boolean sign survives the decoding map.

## Lean

Formalized as [`MIPRE.SAT.PcpAlgebra.degreeOf_liftAnswer_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpAlgebra.degreeOf_liftAnswer_le), [`MIPRE.SAT.PcpAlgebra.literal_product_degree_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpAlgebra.literal_product_degree_le), [`MIPRE.SAT.PcpAlgebra.honest_constraint_degree_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpAlgebra.honest_constraint_degree_le), [`MIPRE.SAT.PcpAlgebra.typedAccepts_ev_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpAlgebra.typedAccepts_ev_iff), [`MIPRE.SAT.PcpAlgebra.exists_proof_of_satisfying_assignment`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpAlgebra.exists_proof_of_satisfying_assignment), [`MIPRE.SAT.PcpAlgebra.decoded_clause_of_majority`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpAlgebra.decoded_clause_of_majority).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 5068](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5068)
