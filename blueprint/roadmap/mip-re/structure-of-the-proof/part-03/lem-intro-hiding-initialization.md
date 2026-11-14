---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.TypedPresentation.mu_constant_edge, MIPRE.Introspection.TypedPresentation.mu_pauli_aux, MIPRE.Introspection.TypedPresentation.mu_aux_pauli, MIPRE.Introspection.TypedEstimates.pauli_aux_agreement_estimate, MIPRE.Introspection.TypedEstimates.aux_pauli_agreement_estimate, MIPRE.Introspection.Honest.pauliXReadout_firstHide, MIPRE.Introspection.Honest.pauliXReadout_registerState_mirror, MIPRE.Introspection.TypedEstimates.hiding_first_agreement_estimate, MIPRE.Introspection.TypedEstimates.hiding_first_register_rigidity, MIPRE.Introspection.TypedEstimates.idealZ_prefix_fibSum, MIPRE.Introspection.TypedEstimates.introspect_prefix_register_rigidity_bob
statement: formalized
proof: formalized
---

# Initializing hiding from the actual Pauli tests

Let $e=|E|\varepsilon$ for the actual parsed game on an EPR seed and arbitrary normalized auxiliary state. Suppose the fixed Pauli-X and Pauli-Z questions have primitive extracted squared errors $\delta_X$ on Alice and $\eta_Z$ on Bob. The actual X/first-Hide test gives first-Hide Bob error at most $4e+2\delta_X$. The Z/Sample and Sample/Introspect tests give every Bob Introspect-prefix error at most $4\eta_Z+12e$. Projectivity is required where used for coarse-graining; malformed outcomes are included. Constancy of the two Pauli questions is stated explicitly.

## Depends on

- [The parsed introspection decision predicate](../part-02/lem-intro-parsed-predicate.md)
- [Introspection type graph and typed CL family](../part-02/lem-intro-type-presentation.md)
- [The concrete ideal hiding step](lem-intro-concrete-ideal-step.md)

## Proof depends on

- [An actual adjacent hiding rigidity step](lem-intro-actual-hiding-rigidity-step.md)
- [Perfect PCC strategy for the full auxiliary game](lem-intro-honest-full-auxiliary.md)

## Proof

Compute the exact Pauli/auxiliary edge masses. Transfer primitive ideal operators across their exact EPR mirrors before coarse-graining. Identify the ideal first hiding family and every ideal prefix as the corresponding coarsened Pauli readouts, then use the actual accepted-answer comparisons.

## Lean

Formalized as [`MIPRE.Introspection.TypedPresentation.mu_constant_edge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPresentation.mu_constant_edge), [`MIPRE.Introspection.TypedPresentation.mu_pauli_aux`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPresentation.mu_pauli_aux), [`MIPRE.Introspection.TypedPresentation.mu_aux_pauli`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPresentation.mu_aux_pauli), [`MIPRE.Introspection.TypedEstimates.pauli_aux_agreement_estimate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.pauli_aux_agreement_estimate), [`MIPRE.Introspection.TypedEstimates.aux_pauli_agreement_estimate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.aux_pauli_agreement_estimate), [`MIPRE.Introspection.Honest.pauliXReadout_firstHide`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.pauliXReadout_firstHide), [`MIPRE.Introspection.Honest.pauliXReadout_registerState_mirror`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.pauliXReadout_registerState_mirror), [`MIPRE.Introspection.TypedEstimates.hiding_first_agreement_estimate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hiding_first_agreement_estimate), [`MIPRE.Introspection.TypedEstimates.hiding_first_register_rigidity`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hiding_first_register_rigidity), [`MIPRE.Introspection.TypedEstimates.idealZ_prefix_fibSum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.idealZ_prefix_fibSum), [`MIPRE.Introspection.TypedEstimates.introspect_prefix_register_rigidity_bob`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.introspect_prefix_register_rigidity_bob).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2376](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2376)
