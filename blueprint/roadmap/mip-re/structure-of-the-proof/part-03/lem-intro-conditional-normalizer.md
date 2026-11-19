---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.conditionalIdeal_isPVM, MIPRE.Introspection.conditional_coarse_overlap, MIPRE.Introspection.conditional_coarse_ideal_distance, MIPRE.Introspection.conditional_normalizer_change, MIPRE.Introspection.conditional_coarse_ideal_replacement, MIPRE.Introspection.conditional_coarse_ideal_of_test, MIPRE.Introspection.conditionalIdeal_mirror, MIPRE.Introspection.conditional_coarse_ideal_replacement_mirror
statement: formalized
proof: formalized
---

# Dimension-independent conditional normalizer replacement

Let $M_i,P_i$ be complete projective families on opposite parties and $Q_y$ a complete projective prefix family commuting with every $P_i$. For arbitrary keyed maps $f_y$, define $T_{y,z}=Q_y\sum_{i:f_y(i)=z}P_i$. This is a PVM. If the fine cross-party squared error is at most $\varepsilon_f$, the actual marginal $R_y$ has squared error at most $\eta$ from $Q_y$, and the conditional comparison has squared error at most $\alpha$, then the later measurement has squared error at most $3\alpha+3\eta+3\varepsilon_f$ from $T$. There is no alphabet-size factor. Exact mirrors of the primitive prefix and fine families transfer this conclusion to the opposite-party ideal family.

## Depends on

- [State-dependent POVM distance](../../foundations/part-02/def-state-distance.md)

## Proof depends on

- [Conditional estimate for the actual adjacent hiding test](../part-04/lem-intro-adjacent-hiding.md)

## Proof

All keyed off-diagonal Born terms are nonnegative because the ideal prefix and fine projectors commute. The diagonal terms recover the original fine overlap after summing the complete prefix family. Convert overlap to squared distance with the prefix attached as a normalizer. Completeness removes Alice's coarse projectors from the summed normalizer-change error. Apply the three-term squared triangle inequality. Exact mirrors reverse products; commutation restores the order in the ideal family.

## Lean

Formalized as [`MIPRE.Introspection.conditionalIdeal_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.conditionalIdeal_isPVM), [`MIPRE.Introspection.conditional_coarse_overlap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.conditional_coarse_overlap), [`MIPRE.Introspection.conditional_coarse_ideal_distance`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.conditional_coarse_ideal_distance), [`MIPRE.Introspection.conditional_normalizer_change`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.conditional_normalizer_change), [`MIPRE.Introspection.conditional_coarse_ideal_replacement`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.conditional_coarse_ideal_replacement), [`MIPRE.Introspection.conditional_coarse_ideal_of_test`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.conditional_coarse_ideal_of_test), [`MIPRE.Introspection.conditionalIdeal_mirror`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.conditionalIdeal_mirror), [`MIPRE.Introspection.conditional_coarse_ideal_replacement_mirror`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.conditional_coarse_ideal_replacement_mirror).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2268](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2268)
