---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.pvm_event_stability, MIPRE.Introspection.joint_distance_left, MIPRE.Introspection.testAcceptance_stability_left, MIPRE.Introspection.testAcceptance_stability_right, MIPRE.Introspection.testAcceptance_stability, MIPRE.Introspection.qform_state_stability, MIPRE.Introspection.povmValue_state_stability, MIPRE.Introspection.povmValue_failure_transfer
statement: formalized
proof: formalized
---

# Quantitative measurement and state replacement

Replacing projective measurements at summed squared state distances $\delta_A,\delta_B$ changes any test acceptance by at most $2\sqrt{\delta_A}+2\sqrt{\delta_B}$. Replacing normalized state vectors at squared distance $\eta$ changes the full game value by at most $2\sqrt{\eta}$. These bounds have no answer-cardinality factor. The measurement-replacement statements require projectivity, so the mixing output must first undergo a quantitatively controlled common-ancilla dilation.

## Depends on

- [Local isometries of bipartite models](../../downstream-results/part-03/def-local-isometry.md)
- [Nonlocal game](../../foundations/part-01/def-game.md)

## Proof

Apply two Cauchy–Schwarz bounds to the accepted outcomes of the joint PVM. Summing the unchanged party's outcomes removes it exactly from the distance. For state replacement, the accepted effect is a contraction; expand its quadratic-form difference and average with the normalized question law.

## Lean

Formalized as [`MIPRE.Introspection.pvm_event_stability`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.pvm_event_stability), [`MIPRE.Introspection.joint_distance_left`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.joint_distance_left), [`MIPRE.Introspection.testAcceptance_stability_left`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.testAcceptance_stability_left), [`MIPRE.Introspection.testAcceptance_stability_right`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.testAcceptance_stability_right), [`MIPRE.Introspection.testAcceptance_stability`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.testAcceptance_stability), [`MIPRE.Introspection.qform_state_stability`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.qform_state_stability), [`MIPRE.Introspection.povmValue_state_stability`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.povmValue_state_stability), [`MIPRE.Introspection.povmValue_failure_transfer`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.povmValue_failure_transfer).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2580](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2580)
