---
declaration: lemma
origin: cited
lean: MIPRE.AnswerReduction.sampler_cost_le_power
statement: formalized
proof: formalized
---

# Ambient sampler-cost absorption

If $L\leq B$ and $s+1\leq B$, then $L(s+1)^\mu\leq B^{\mu+1}$. Consequently the ambient answer-reduction contract retains the input sampler's degree in its output budget: a universal base polynomial is raised to $\mu+1$, and the base output degree is multiplied by $\mu+1$. This arithmetic bound does not construct the answer-reduction program or its clock.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Bound each factor by its corresponding power of $B$. Compression fixes $\mu$ before choosing its final bound, so that bound is still polynomial.

## Lean

Formalized as [`MIPRE.AnswerReduction.sampler_cost_le_power`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.sampler_cost_le_power).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 995](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L995)
