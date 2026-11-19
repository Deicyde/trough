---
declaration: corollary
origin: cited
lean: MIPRE.Tailored.TailoredGapCompression.ofAnswerReduction, MIPRE.Tailored.tailored_halting_reduction_of_answerReduction, MIPRE.Tailored.tmipStarComputable_eq_re_of_answerReduction
statement: formalized
proof: formalized
---

# $\mathrm{TMIP}^* = \mathrm{RE}$ from tailored answer reduction

An answer reduction at input level $5$ (Definition [The three stage contracts](../part-03/def-tailored-stages.md)) gives a tailored gap compression at level $7$, hence the halting reduction to tailored games of Definition [The tailored halting reduction, as a proposition](../part-01/def-tailored-halting-reduction.md) and $\mathrm{TMIP}^* = \mathrm{RE}$.

## Depends on

- [Tailored compression from its stages; II:5643, value form](thm-tailored-compression-from-stages.md)
- [Question reduction for tailored verifiers; II:5712](../part-03/thm-tailored-qr.md)
- [Parallel repetition of tailored verifiers; II:11103, direct form](../part-03/thm-tailored-rep.md)
- [Halting from tailored compression; II:1887–2066](../part-02/thm-tailored-halting.md)
- [$\mathrm{TMIP}^* = \mathrm{RE}$, as classes; II:787, II:1838, II:6997](../part-02/thm-tmipstar-eq-re.md)

## Proof

Theorem [Tailored compression from its stages; II:5643, value form](thm-tailored-compression-from-stages.md) with the question reduction of Theorem [Question reduction for tailored verifiers; II:5712](../part-03/thm-tailored-qr.md) and the repetition of Theorem [Parallel repetition of tailored verifiers; II:11103, direct form](../part-03/thm-tailored-rep.md); then Theorems [Halting from tailored compression; II:1887–2066](../part-02/thm-tailored-halting.md) and [$\mathrm{TMIP}^* = \mathrm{RE}$, as classes; II:787, II:1838, II:6997](../part-02/thm-tmipstar-eq-re.md).

## Lean

Formalized as [`MIPRE.Tailored.TailoredGapCompression.ofAnswerReduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGapCompression.ofAnswerReduction), [`MIPRE.Tailored.tailored_halting_reduction_of_answerReduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.tailored_halting_reduction_of_answerReduction), [`MIPRE.Tailored.tmipStarComputable_eq_re_of_answerReduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.tmipStarComputable_eq_re_of_answerReduction).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2277](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2277)
