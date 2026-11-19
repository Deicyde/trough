---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Sofic.wordCount, MIPRE.Tailored.Sofic.sig, MIPRE.Tailored.Sofic.withPerms, MIPRE.Tailored.Sofic.diffCard_wordPerm, MIPRE.Tailored.Sofic.abs_passProb_sub_le, MIPRE.Tailored.Sofic.abs_value_sub_le
statement: formalized
proof: formalized
---

# Robustness of the value; Claim I:1480

For two actions of the generators on the same finite set, $|\mathrm{val}(T, \sigma) - \mathrm{val}(T, \sigma')| \leq \sum_k S_T(k)\, d(\sigma_k, \sigma'_k)$, where the significance $S_T(k)$ is the expected number of occurrences of the generator $k$ in the words of a challenge.

## Depends on

- [Subgroup tests and their sofic value; I:439–520](def-subgroup-test.md)
- [Hamming distance of permutations](lem-perm-hamming.md)

## Proof

A word moves a point differently under the two actions only if one of its letters does at an intermediate point; letters and their inverses cost the same.

## Lean

Formalized as [`MIPRE.Tailored.Sofic.wordCount`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.wordCount), [`MIPRE.Tailored.Sofic.sig`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.sig), [`MIPRE.Tailored.Sofic.withPerms`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.withPerms), [`MIPRE.Tailored.Sofic.diffCard_wordPerm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.diffCard_wordPerm), [`MIPRE.Tailored.Sofic.abs_passProb_sub_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.abs_passProb_sub_le), [`MIPRE.Tailored.Sofic.abs_value_sub_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.abs_value_sub_le).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 164](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L164)
