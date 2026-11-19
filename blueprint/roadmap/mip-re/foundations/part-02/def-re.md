---
declaration: definition
origin: cited
lean: MIPRE.IsRE, MIPRE.isRE_iff
statement: formalized
---

# Recursively enumerable

A language $L \subseteq \{0,1\}^*$ is in $\mathrm{RE}$ if it is the domain (equivalently, the range) of a partial computable function. The *halting problem* — the set of $e$ such that $\phi_e$ halts on the empty input — is $\mathrm{RE}$-complete under many-one reductions.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MIPRE.IsRE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsRE), [`MIPRE.isRE_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.isRE_iff).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 1338](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L1338)
