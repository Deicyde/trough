---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.adaptiveFailureBudget_add, MIPRE.Introspection.TypedEstimates.exists_intro_two_sided_iteration
statement: formalized
proof: formalized
---

# Both actual terminal measurements

If the initial failure, both primitive Z errors, and the required hiding errors are at most the explicit threshold for $2\ell$ replacements, there are concrete projective measurement families with Alice's false-role and Bob's true-role terminal invariants. The final state uses only fixed local ancillas, and failure is bounded by the single recurrence at $2\ell$. The Lean's final state is a model: Alice's block extends the auxiliary model on her side and Bob's block the result on his, and the final model reduces to the original one (Definition [Reduction of POVM strategies](../../downstream-results/part-03/def-povm-reduction.md)).

## Depends on

- [Player exchange and the actual Bob iteration](lem-intro-bob-iteration.md)
- [An explicit admissible error threshold for finite iteration](lem-intro-iteration-threshold.md)

## Proof

Run Alice's false-role block for $\ell$ steps. The threshold theorem supplies the admissible failure at the midpoint, and the unchanged-question identities supply Bob's primitive inputs. Run Bob's true-role block, retaining Alice's completed measurement. Restarting the numerical recurrence is exactly continuing it, so the two blocks have the stated combined bound.

## Lean

Formalized as [`MIPRE.Introspection.adaptiveFailureBudget_add`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.adaptiveFailureBudget_add), [`MIPRE.Introspection.TypedEstimates.exists_intro_two_sided_iteration`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.exists_intro_two_sided_iteration).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3067](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3067)
