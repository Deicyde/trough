---
declaration: corollary
origin: cited
lean: MIPRE.Halting.halting_reduction_quantum
statement: formalized
proof: formalized
---

# Halting reduces to the quantum value

With $g$ as in Theorem [Halting reduces to the game value; Theorem 12.2 of (JNVWY20), synchronous form](thm-main.md): if $\mathcal{M}$ halts on the empty input then $\mathrm{val}^*(\mathfrak{G}_{g(\mathcal{M})}) = 1$, and if $\mathcal{M}$ does not halt on the empty input then $\mathrm{val}^*(\mathfrak{G}_{g(\mathcal{M})}) \leq \tfrac12$.

## Depends on

- [Halting reduction](../structure-of-the-proof/part-09/thm-halting.md)
- [Synchronous value lower-bounds the quantum value](../foundations/part-01/lem-sync-le-valstar.md)
- [Quantum value](../foundations/part-01/def-q-value.md)
- [Game description](../foundations/part-02/def-game-description.md)

## Proof depends on

- [Compression, and $\mathrm{MIP}^* = \mathrm{RE}$, from answer reduction alone](../structure-of-the-proof/part-09/cor-compression-from-answer-reduction.md)
- [Answer reduction](../structure-of-the-proof/part-09/thm-answer-reduction.md)

## Proof

At the compression of Theorem [Ambient compression inhabitation target](../structure-of-the-proof/part-09/thm-compression-target.md), as Theorem [Halting reduces to the game value; Theorem 12.2 of (JNVWY20), synchronous form](thm-main.md) is: `MIPRE.Halting.halting_reduction_both_of` produces one computable map with both values, the quantum one from `tab_value` and `Verifier.valStar_eq_one_of_hasPerfectPCC` in the halting branch and from `tab_value` alone in the other; the corollary is its quantum half.

## Lean

Formalized as [`MIPRE.Halting.halting_reduction_quantum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.halting_reduction_quantum).

## Sources

- [MIP* = RE blueprint: content/07_main_theorem.tex, line 106](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/07_main_theorem.tex#L106)
