---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.sum_xSqNorm_mirror_transfer, MIPRE.Introspection.TypedEstimates.hiding_register_orientation, MIPRE.Introspection.TypedEstimates.hiding_register_recurrence, MIPRE.Introspection.TypedEstimates.hiding_register_iteration, MIPRE.Introspection.TypedEstimates.hiding_register_iteration_uniform, MIPRE.Introspection.TypedEstimates.hiding_register_rigidity_of_pauli
statement: formalized
proof: formalized
---

# Full hiding rigidity

Under the primitive extracted Pauli guarantees and actual game-success hypothesis above, every hiding level is rigid on both parties. A uniform Bob bound is

$$
B=6^\ell\bigl((94+48\ell^2)e+2\delta_X+24\eta_Z\bigr),
$$

and a uniform Alice bound is $4e+2B$. This completes the hiding-measurement induction without a base-case or prefix-rigidity conclusion among the assumptions. The constant depends on $\ell$, not on the answer alphabet.

## Depends on

- [Initializing hiding from the actual Pauli tests](lem-intro-hiding-initialization.md)
- [An actual adjacent hiding rigidity step](lem-intro-actual-hiding-rigidity-step.md)

## Proof

The actual consistency loop transfers Bob rigidity to Alice with cost $4e+2B_k$. The adjacent step gives $B_{k+1}\leq6B_k+(18+48\ell^2)e+6\delta$. Solve the finite recurrence and substitute the proved base and prefix bounds. No symmetry of the Pauli predicate is needed. Supplying the extracted state and primitive Pauli guarantees from the QLD theorem is a separate interface.

## Lean

Formalized as [`MIPRE.Introspection.sum_xSqNorm_mirror_transfer`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.sum_xSqNorm_mirror_transfer), [`MIPRE.Introspection.TypedEstimates.hiding_register_orientation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hiding_register_orientation), [`MIPRE.Introspection.TypedEstimates.hiding_register_recurrence`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hiding_register_recurrence), [`MIPRE.Introspection.TypedEstimates.hiding_register_iteration`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hiding_register_iteration), [`MIPRE.Introspection.TypedEstimates.hiding_register_iteration_uniform`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hiding_register_iteration_uniform), [`MIPRE.Introspection.TypedEstimates.hiding_register_rigidity_of_pauli`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hiding_register_rigidity_of_pauli).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2409](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2409)
