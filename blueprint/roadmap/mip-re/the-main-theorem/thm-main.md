---
declaration: theorem
origin: cited
lean: HaltingGameValue.halting_reduces_to_gameValue, HaltingGameValue.HaltingReducesToGameValue
statement: formalized
proof: formalized
---

# Halting reduces to the game value; Theorem 12.2 of (JNVWY20), synchronous form

There is a computable map $g$ from Turing machines to game descriptions such that for every Turing machine $\mathcal{M}$:

1. (**Completeness**) if $\mathcal{M}$ halts on the empty input, then ${\mathrm{val}^{s}}(\mathfrak{G}_{g(\mathcal{M})}) = 1$;
2. (**Soundness**) if $\mathcal{M}$ does not halt on the empty input, then ${\mathrm{val}^{s}}(\mathfrak{G}_{g(\mathcal{M})}) \leq \tfrac12$.

## Depends on

- [Halting reduction](../structure-of-the-proof/part-09/thm-halting.md)
- [Game description](../foundations/part-02/def-game-description.md)
- [Synchronous value](../foundations/part-01/def-sync-value.md)
- [Recursively enumerable](../foundations/part-02/def-re.md)

## Proof depends on

- [Compression, and $\mathrm{MIP}^* = \mathrm{RE}$, from answer reduction alone](../structure-of-the-proof/part-09/cor-compression-from-answer-reduction.md)
- [Answer reduction](../structure-of-the-proof/part-09/thm-answer-reduction.md)

## Proof

`MIPRE.Halting.halting_reduces_to_gameValue_of` takes a `MIPRE.GapCompression` and a universal machine and concludes exactly this statement; Theorem [Ambient compression inhabitation target](../structure-of-the-proof/part-09/thm-compression-target.md) supplies the compression.

## Lean

Formalized as [`HaltingGameValue.halting_reduces_to_gameValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/HaltingGameValue.halting_reduces_to_gameValue), [`HaltingGameValue.HaltingReducesToGameValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/HaltingGameValue.HaltingReducesToGameValue).

## Sources

- [MIP* = RE blueprint: content/07_main_theorem.tex, line 12](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/07_main_theorem.tex#L12)
