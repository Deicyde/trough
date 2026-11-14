---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.terminalAuxPOVM_isPVM, MIPRE.Introspection.IntroPrefixInvariant.terminal_some, MIPRE.Introspection.IntroPrefixInvariant.terminal_none
statement: formalized
proof: formalized
---

# Terminal conditional readouts with malformed answers

Suppose the CL presentation covers the whole register exactly. A terminal prefix invariant gives a projective auxiliary measurement $T_y$ on $\mathrm{Option}(A)$ for each reported question $y$. Every valid effect is the question readout at $y$ tensored with $T_y(\mathrm{some}(a))$. The malformed effect is the sum over $y$ of the question readout tensored with $T_y(\mathrm{none})$; it is not assumed to vanish.

## Depends on

- [Pauli mixing with a retained classical fibre](../part-02/lem-pauli-mixing.md)
- [The register model](../../downstream-results/part-03/def-register-model.md)

## Proof depends on

- [The parsed introspection decision predicate](../part-02/lem-intro-parsed-predicate.md)
- [Projective strategy in a bipartite model](../../downstream-results/part-02/def-model-proj-strategy.md)

## Proof

The remaining register is empty at the terminal level, so transport its unique basis vector away. The valid-answer support invariant fixes the reported question on each residual branch. Coarsen only that question component; projectivity and normalization are preserved on the full option alphabet. Reassembling the residual effects gives both formulas.

## Lean

Formalized as [`MIPRE.Introspection.terminalAuxPOVM_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.terminalAuxPOVM_isPVM), [`MIPRE.Introspection.IntroPrefixInvariant.terminal_some`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.IntroPrefixInvariant.terminal_some), [`MIPRE.Introspection.IntroPrefixInvariant.terminal_none`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.IntroPrefixInvariant.terminal_none).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3007](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3007)
