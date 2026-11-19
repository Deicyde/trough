---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.TypedEstimates.exists_intro_iteration
statement: formalized
proof: formalized
---

# Finite iteration of the actual Alice strategy

In the actual parsed-game setup, suppose the starting measurements are projective, the primitive Bob-Z and every fixed Alice hiding error have the stated bounds, and these bounds and the initial failure are at most $t_\ell$. For every $n\leq\ell$ there is an actual projective Alice measurement family with the prefix invariant at level $n$ and failure at most the explicit numerical recurrence. Its auxiliary carrier and product ancilla state are constructed recursively. Bob's measurement family is retained, all other Alice questions have their exact iterated identity extensions, and the primitive Bob-Z and Alice hiding errors remain unchanged. The Lean states it in the register model (Definition [The register model](../../downstream-results/part-03/def-register-model.md)) of a normalized auxiliary model: each stage adjoins a one-sided ancilla whose size the dilation chooses, so the iteration returns a new normalized auxiliary model in place of the recursive carrier and state, and that model reduces to the original one (Definition [Reduction of POVM strategies](../../downstream-results/part-03/def-povm-reduction.md)).

## Depends on

- [Initializing and advancing the actual prefix invariant](../part-04/lem-intro-actual-successor.md)
- [An explicit admissible error threshold for finite iteration](lem-intro-iteration-threshold.md)

## Proof depends on

- [Reductions](../../downstream-results/part-03/lem-povm-reduction.md)

## Proof

Initialize the concrete residual measurement. At each successor apply Lemma [Initializing and advancing the actual prefix invariant](../part-04/lem-intro-actual-successor.md) to the current strategy. The explicit threshold proves its smallness premise, and replacing remaining depth by the full depth bounds the loss by the common recurrence. Exact preservation of the fixed errors supplies the next stage's primitive inputs.

## Lean

Formalized as [`MIPRE.Introspection.TypedEstimates.exists_intro_iteration`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.exists_intro_iteration).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2978](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2978)
