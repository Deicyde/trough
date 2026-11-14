---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Sofic.invFix, MIPRE.Tailored.Sofic.invFix_invol, MIPRE.Tailored.Sofic.diffCard_invFix, MIPRE.Tailored.Sofic.fpfFix, MIPRE.Tailored.Sofic.fpfFix_invol, MIPRE.Tailored.Sofic.fpfFix_free, MIPRE.Tailored.Sofic.diffCard_fpfFix, MIPRE.Tailored.Sofic.ordProd, MIPRE.Tailored.Sofic.commFix, MIPRE.Tailored.Sofic.commFix_invol, MIPRE.Tailored.Sofic.commFix_comm, MIPRE.Tailored.Sofic.commFix_J, MIPRE.Tailored.Sofic.commFix_readable, MIPRE.Tailored.Sofic.diffCard_commFix
statement: formalized
proof: formalized
---

# Stability of involutions, fixed-point-free involutions and commuting families; I:2561–2649

A permutation $\pi$ is within $d(\pi^2, 1)$ of an involution; an involution of an even set almost without fixed points is close to one without, given a fixed-point-free involution commuting with it; and a family of involutions at a vertex, together with $J$, can be made into commuting involutions commuting with $J$, the readable ones acting as the identity or as $J$, by changing them on at most $2^{\ell + 1}$ times the points at which some relation fails.

## Depends on

- [Hamming distance of permutations](lem-perm-hamming.md)

## Proof

The first two as in the paper. The third replaces Claim I:2600 and Glebsky–Rivera (Claim I:2631): restrict the variables to the set of points from which every ordered product of them reaches only points where all relations hold, invariant under the variables and $J$, and let them act as the identity elsewhere.

## Lean

Formalized as [`MIPRE.Tailored.Sofic.invFix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.invFix), [`MIPRE.Tailored.Sofic.invFix_invol`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.invFix_invol), [`MIPRE.Tailored.Sofic.diffCard_invFix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.diffCard_invFix), [`MIPRE.Tailored.Sofic.fpfFix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.fpfFix), [`MIPRE.Tailored.Sofic.fpfFix_invol`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.fpfFix_invol), [`MIPRE.Tailored.Sofic.fpfFix_free`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.fpfFix_free), [`MIPRE.Tailored.Sofic.diffCard_fpfFix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.diffCard_fpfFix), [`MIPRE.Tailored.Sofic.ordProd`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ordProd), [`MIPRE.Tailored.Sofic.commFix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.commFix), [`MIPRE.Tailored.Sofic.commFix_invol`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.commFix_invol), [`MIPRE.Tailored.Sofic.commFix_comm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.commFix_comm), [`MIPRE.Tailored.Sofic.commFix_J`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.commFix_J), [`MIPRE.Tailored.Sofic.commFix_readable`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.commFix_readable), [`MIPRE.Tailored.Sofic.diffCard_commFix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.diffCard_commFix).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 137](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L137)
