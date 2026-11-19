---
declaration: lemma
origin: cited
lean: MIPRE.QLD.expanded_points
statement: formalized
proof: formalized
---

# Expanded point measurements

Adjoin EPR ancilla registers to $|\psi\rangle$. There are measurements $\widehat{M}^{(\mathtt{Point}, W), u}$ on each player's space together with its ancilla such that, with $\delta_{\mathrm{acom}}(\varepsilon) = O(\sqrt{\varepsilon})$: they are self-consistent across the two sides at error $\varepsilon$, and, the first player's measurements being projective, the $X$-side and $Z$-side coarse observables *approximately commute* on the expanded state at error $\delta_{\mathrm{acom}}$. The Lean proves it for a strategy in any bipartite model, the expanded state being its register model on $\mathbb{F}_q^M$ (Definition [The register model](../../downstream-results/part-03/def-register-model.md)); the statement above is its tensor-product instance.

## Depends on

- [Win implications](lem-qld-win.md)
- [The expanded state, and an inert ancilla](../../foundations/part-02/def-expanded-state.md)
- [Expanded point observables commute](lem-qld-expanded-commutation.md)
- [Expanded point measurements are self-consistent](lem-qld-expanded-consistency.md)
- [The register model](../../downstream-results/part-03/def-register-model.md)

## Proof

Two items, one lemma each. The pivotal one is an exact cancellation of a sign $(-1)^\gamma$ between the strategy's own observables, supplied by the anticommutation relations of Lemma [Win implications](lem-qld-win.md), and the ancilla observables: Lemma [Expanded point observables commute](lem-qld-expanded-commutation.md). Without the ancillas the two bases only commute up to an error carrying that sign, which does not improve with $\varepsilon$; with them the sign cancels identically. Self-consistency is Lemma [Expanded point measurements are self-consistent](lem-qld-expanded-consistency.md).

## Lean

Formalized as [`MIPRE.QLD.expanded_points`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.expanded_points).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 2501](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L2501)
