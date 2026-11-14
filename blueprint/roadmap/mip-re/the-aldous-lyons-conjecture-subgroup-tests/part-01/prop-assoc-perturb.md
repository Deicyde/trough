---
declaration: proposition
origin: cited
lean: MIPRE.Tailored.Sofic.double, MIPRE.Tailored.Sofic.value_double, MIPRE.Tailored.Sofic.dblSwap, MIPRE.Tailored.Sofic.qw, MIPRE.Tailored.Sofic.qwTot, MIPRE.Tailored.Sofic.qwTot_pos, MIPRE.Tailored.Sofic.value_eq, MIPRE.Tailored.Sofic.sig_eq, MIPRE.Tailored.Sofic.fixed_of_passes, MIPRE.Tailored.Sofic.read_of_passes, MIPRE.Tailored.Sofic.npass, MIPRE.Tailored.Sofic.SwapData, MIPRE.Tailored.Sofic.J₂, MIPRE.Tailored.Sofic.Xfix, MIPRE.Tailored.Sofic.perturbed, MIPRE.Tailored.Sofic.checks_perturbed, MIPRE.Tailored.Sofic.card_bad_le, MIPRE.Tailored.Sofic.lose, MIPRE.Tailored.Sofic.loseAt, MIPRE.Tailored.Sofic.weighted_dist_le, MIPRE.Tailored.Sofic.value_perturbed_ge, MIPRE.Tailored.Sofic.numeric_bound, MIPRE.Tailored.Sofic.Cp, MIPRE.Tailored.Sofic.exists_checks_of_value
statement: formalized
proof: formalized
---

# Perturbing to pass Checks 1–3; Proposition I:2267

If an action has value at least $1 - \varepsilon$ against the associated test of a tailored game with answer length $\Lambda$, then an action passing Checks 1–3 everywhere has value at least $1 - 300\,(\Lambda + 1)^4\, 2^{4(\Lambda + 1)}\, \varepsilon$.

## Depends on

- [Stability of involutions, fixed-point-free involutions and commuting families; I:2561–2649](lem-perm-stability.md)
- [Robustness of the value; Claim I:1480](lem-test-robust.md)
- [Significance of the associated test; Proposition I:2283](lem-assoc-significance.md)

## Proof

Double the action first, so that the set is even and carries a fixed-point-free involution commuting with every generator. Make $J$ a fixed-point-free involution, then repair the variables vertex by vertex (Lemma [Stability of involutions, fixed-point-free involutions and commuting families; I:2561–2649](lem-perm-stability.md)), bounding the points changed at a vertex by its losing probability, and conclude by robustness and significance.

## Lean

Formalized as [`MIPRE.Tailored.Sofic.double`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.double), [`MIPRE.Tailored.Sofic.value_double`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.value_double), [`MIPRE.Tailored.Sofic.dblSwap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.dblSwap), [`MIPRE.Tailored.Sofic.qw`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.qw), [`MIPRE.Tailored.Sofic.qwTot`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.qwTot), [`MIPRE.Tailored.Sofic.qwTot_pos`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.qwTot_pos), [`MIPRE.Tailored.Sofic.value_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.value_eq), [`MIPRE.Tailored.Sofic.sig_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.sig_eq), [`MIPRE.Tailored.Sofic.fixed_of_passes`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.fixed_of_passes), [`MIPRE.Tailored.Sofic.read_of_passes`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.read_of_passes), [`MIPRE.Tailored.Sofic.npass`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.npass), [`MIPRE.Tailored.Sofic.SwapData`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.SwapData), [`MIPRE.Tailored.Sofic.J₂`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.J₂), [`MIPRE.Tailored.Sofic.Xfix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Xfix), [`MIPRE.Tailored.Sofic.perturbed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.perturbed), [`MIPRE.Tailored.Sofic.checks_perturbed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.checks_perturbed), [`MIPRE.Tailored.Sofic.card_bad_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.card_bad_le), [`MIPRE.Tailored.Sofic.lose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.lose), [`MIPRE.Tailored.Sofic.loseAt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.loseAt), [`MIPRE.Tailored.Sofic.weighted_dist_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.weighted_dist_le), [`MIPRE.Tailored.Sofic.value_perturbed_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.value_perturbed_ge), [`MIPRE.Tailored.Sofic.numeric_bound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.numeric_bound), [`MIPRE.Tailored.Sofic.Cp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Cp), [`MIPRE.Tailored.Sofic.exists_checks_of_value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.exists_checks_of_value).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 200](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L200)
