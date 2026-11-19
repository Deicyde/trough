---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.adaptiveStageBudget_mono_depth, MIPRE.Introspection.adaptiveFailureBudget_nonneg, MIPRE.Introspection.adaptiveSmallThreshold_pos, MIPRE.Introspection.adaptiveFailureBudget_le_threshold, MIPRE.Introspection.adaptiveStageBudget_le_one_of_threshold
statement: formalized
proof: formalized
---

# An explicit admissible error threshold for finite iteration

For nonnegative edge multiplier $m$, set $C=(512r^2+224)m+128$ and define

$$
t_0=C^{-1},\qquad
t_{n+1}=\min\{t_n/2,(t_n/16)^8/C\}.
$$

Each $t_n$ is positive. If the initial failure and both fixed primitive errors are at most $t_N$, the numerical failure after $n\leq N$ replacements is at most $t_{N-n}$, and every common stage budget is at most one.

## Depends on

- [One stage budget from the actual game tests](../part-04/lem-intro-game-stage.md)

## Proof

When all three errors are at most $t$, the budget is at most $Ct$. The eighth-power threshold and the bound $8B^{1/8}$ reserve at most $t_n/2$ for the new loss; the other half bounds the previous failure. Induct on the number of replacements, using the decreasing thresholds.

## Lean

Formalized as [`MIPRE.Introspection.adaptiveStageBudget_mono_depth`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.adaptiveStageBudget_mono_depth), [`MIPRE.Introspection.adaptiveFailureBudget_nonneg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.adaptiveFailureBudget_nonneg), [`MIPRE.Introspection.adaptiveSmallThreshold_pos`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.adaptiveSmallThreshold_pos), [`MIPRE.Introspection.adaptiveFailureBudget_le_threshold`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.adaptiveFailureBudget_le_threshold), [`MIPRE.Introspection.adaptiveStageBudget_le_one_of_threshold`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.adaptiveStageBudget_le_one_of_threshold).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2951](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2951)
