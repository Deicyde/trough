---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.iteratedRoot_scale_le, MIPRE.Introspection.adaptiveFailureBudget_le_power, MIPRE.Introspection.adaptiveSoundness_power_cases, MIPRE.Introspection.exists_adaptiveSoundness_errorProfile
statement: formalized
proof: formalized
---

# A power bound for the entire finite recurrence

For fixed depth and type graph, the failure after $N$ replacements is at most a fixed coefficient times the $3N$-fold square root of a common input error in the admissible regime. A second explicit coefficient makes the same bound at least one outside that regime. Consequently the combined bound has the paper's two-term error profile, with positive exponent at most one and constants independent of the register dimension.

## Depends on

- [An explicit admissible error threshold for finite iteration](lem-intro-iteration-threshold.md)
- [Absorbing fixed introspection error losses](../part-03/lem-intro-error-absorption.md)

## Proof

Bound each stage loss by a constant times an eighth root and induct over the actual recurrence. Add the reciprocal of the iterated root of the positive threshold to handle the large-error regime. Apply fixed-power absorption to the common input profile.

## Lean

Formalized as [`MIPRE.Introspection.iteratedRoot_scale_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.iteratedRoot_scale_le), [`MIPRE.Introspection.adaptiveFailureBudget_le_power`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.adaptiveFailureBudget_le_power), [`MIPRE.Introspection.adaptiveSoundness_power_cases`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.adaptiveSoundness_power_cases), [`MIPRE.Introspection.exists_adaptiveSoundness_errorProfile`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_adaptiveSoundness_errorProfile).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3114](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3114)
