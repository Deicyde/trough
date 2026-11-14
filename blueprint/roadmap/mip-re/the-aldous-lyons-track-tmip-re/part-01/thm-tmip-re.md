---
declaration: theorem
origin: cited
lean: TailoredGameValue.tailored_halting_reduction, MIPRE.Tailored.tailored_halting_reduction_quantum, MIPRE.Tailored.tmipStarComputable_eq_re, MIPRE.Tailored.tmipStar_eq_re
statement: formalized
proof: formalized
---

# $\mathrm{TMIP}^* = \mathrm{RE}$; II:1505, Theorem 7.4 of (BCLV24)

The proposition of Definition [The tailored halting reduction, as a proposition](def-tailored-halting-reduction.md) holds: there is a computable map $g$ from Turing machines to tailored game descriptions such that for every Turing machine $\mathcal{M}$:

1. (**Completeness**) if $\mathcal{M}$ halts on the empty input, then $g(\mathcal{M})$ has a perfect ZPC strategy;
2. (**Soundness**) if $\mathcal{M}$ does not halt on the empty input, then ${\mathrm{val}^{s}}(g(\mathcal{M})) \leq \frac12$.

Turing machines, halting and computability are as in Theorem [Halting reduces to the game value; Theorem 12.2 of (JNVWY20), synchronous form](../../the-main-theorem/thm-main.md), and ${\mathrm{val}^{s}}$ is the synchronous value of Definition [Synchronous value](../../foundations/part-01/def-sync-value.md), in its standalone form (Remark [The standalone restatement](../../the-main-theorem/README.md)).

## Depends on

- [The tailored halting reduction, as a proposition](def-tailored-halting-reduction.md)
- [$\mathrm{TMIP}^* = \mathrm{RE}$ from tailored answer reduction](../part-05/cor-tmip-re-from-ar.md)
- [$\mathrm{TMIP}^* = \mathrm{RE}$ for the polynomial-time class; II:787, II:1505](../part-02/thm-tmipstar-poly-eq-re.md)

## Proof depends on

- [Halting from tailored compression; II:1887–2066](../part-02/thm-tailored-halting.md)
- [Tailored compression; II:5643, value form](../part-05/thm-tailored-compression-target.md)

## Proof

Theorem [Halting from tailored compression; II:1887–2066](../part-02/thm-tailored-halting.md) at the compression of Theorem [Tailored compression; II:5643, value form](../part-05/thm-tailored-compression-target.md), the synchronous value being at most the quantum value; the class theorems for both readings of $\mathrm{TMIP}^*$ follow.

## Lean

Formalized as [`TailoredGameValue.tailored_halting_reduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.tailored_halting_reduction), [`MIPRE.Tailored.tailored_halting_reduction_quantum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.tailored_halting_reduction_quantum), [`MIPRE.Tailored.tmipStarComputable_eq_re`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.tmipStarComputable_eq_re), [`MIPRE.Tailored.tmipStar_eq_re`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.tmipStar_eq_re).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 485](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L485)
