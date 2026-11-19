---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.legal_query_size_le, MIPRE.Introspection.legal_query_cost_le, MIPRE.Introspection.original_decider_haltsWithin, MIPRE.Introspection.polynomial_ansBound, MIPRE.Introspection.original_simulation_haltsWithin
statement: formalized
proof: formalized
---

# Absolute costs on the original legal answer cut

For an ambient $\lambda$-bounded verifier, $n\geq1$, and questions and answers of length at most $(2^n)^\lambda$, the actual original decider halts within $2^{(\lambda n+1)^5}$ cost. Any fixed universal simulator also halts on those inputs within $2^{(\lambda n+1)^C}$ for a constant $C$ depending only on its overhead polynomial. The original answer cut is unchanged. Any fixed polynomial of a polynomial-exponent budget fits another such budget.

## Depends on

- [$\lambda$-bounded verifier in the ambient model](../../foundations/part-03/def-lambda-bounded.md)

## Proof

The four encoded fields have size at most $16(2^n)^\lambda+7$. Insert that size into the actual boundedness clause and bound the resulting exponent by $(\lambda n+1)^5$. Bound program and input sizes by the same exponential, and absorb the universal machine's polynomial overhead. No answer-prefix invariance or malformed-input wrapper is asserted here. This is the absolute legal-input bound of Remark [Runtime normalization obligation](../README.md).

## Lean

Formalized as [`MIPRE.Introspection.legal_query_size_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.legal_query_size_le), [`MIPRE.Introspection.legal_query_cost_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.legal_query_cost_le), [`MIPRE.Introspection.original_decider_haltsWithin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.original_decider_haltsWithin), [`MIPRE.Introspection.polynomial_ansBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.polynomial_ansBound), [`MIPRE.Introspection.original_simulation_haltsWithin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.original_simulation_haltsWithin).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 969](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L969)
