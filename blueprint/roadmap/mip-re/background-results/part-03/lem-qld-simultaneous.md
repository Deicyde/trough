---
declaration: lemma
origin: cited
lean: MIPRE.QLD.PolyPair, MIPRE.QLD.PolyPair.proj, MIPRE.QLD.evalMarg, MIPRE.QLD.evalMarg_mats, MIPRE.QLD.isPVM_evalMarg, MIPRE.QLD.SimulPair, MIPRE.QLD.SimulPair.mono, MIPRE.QLD.SimulPair.bornProb_aOp_aOp, MIPRE.QLD.GlobalPair.toSimulPair, MIPRE.QLD.exists_simulPair, MIPRE.QLD.evalMarg_pushforward, MIPRE.QLD.SimulPair.ψ_unit, MIPRE.QLD.SimulPair.transport, MIPRE.QLD.SimulPair.transport_SA, MIPRE.QLD.SimulPair.transport_SB, MIPRE.QLD.CutSimul
statement: formalized
proof: formalized
---

# The simultaneous global measurement

There are universal $a>1$, $0\lt b<1$ and, on each relevant padded local space, a complete projective measurement $\widehat S_{g_X,g_Z}$ of pairs of individual-degree-$d$ polynomials on $\mathbb{F}_q^m$. Its evaluated $X$ and $Z$ marginals are consistent with the opposite expanded point measurements, with error at most $\delta_S=a(md)^a(\varepsilon^b+q^{-b}+2^{-bmd})$. Both register versions are required; no symmetric-strategy hypothesis is added. The Lean proves it for a legal projective strategy in any bipartite model in which the seeded CL test is sound in every ancilla extension by a unit vector, the pair measurements living in the padded model of Definition [The models of stages 4 and 5](def-qld-physical-model.md), for every padding size beyond a threshold; the statement above is its tensor-product instance.

## Depends on

- [Global robustness in both register versions](lem-qld-global-robustness.md)
- [The models of stages 4 and 5](def-qld-physical-model.md)

## Proof depends on

- [A global padded polynomial PVM](lem-qld-global-pvm.md)

## Proof

Lemma [A global padded polynomial PVM](lem-qld-global-pvm.md) supplies the pair $(G_A, G_B)$ with error $\delta_{\mathrm{ld}}$; Lemmas [Removing dummy-coordinate dependence](lem-qld-global-dummy.md)–[Global robustness in both register versions](lem-qld-global-robustness.md) complete it to a projective measurement of pairs whose evaluated marginals track the opposite party's expanded point measurements with error $\delta_S = 2\sqrt{\Delta} + 2/q + 8\Delta$, $\Delta = 2\delta_{\mathrm{ld}} + 2 \cdot 57676416\,\varepsilon$, in the same model, so no register has to be moved. The displayed functional form is proved with the error of Theorem [Pauli basis test / quantum low individual degree test](../part-01/thm-qld.md), in Lemma [The error of the Pauli basis test](lem-qld-error.md), where $\delta_{\mathrm{ld}}$ is the seeded soundness theorem's error and the square root halves the exponent $b$.

## Lean

Formalized as [`MIPRE.QLD.PolyPair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PolyPair), [`MIPRE.QLD.PolyPair.proj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PolyPair.proj), [`MIPRE.QLD.evalMarg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.evalMarg), [`MIPRE.QLD.evalMarg_mats`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.evalMarg_mats), [`MIPRE.QLD.isPVM_evalMarg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.isPVM_evalMarg), [`MIPRE.QLD.SimulPair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.SimulPair), [`MIPRE.QLD.SimulPair.mono`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.SimulPair.mono), [`MIPRE.QLD.SimulPair.bornProb_aOp_aOp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.SimulPair.bornProb_aOp_aOp), [`MIPRE.QLD.GlobalPair.toSimulPair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.GlobalPair.toSimulPair), [`MIPRE.QLD.exists_simulPair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.exists_simulPair), [`MIPRE.QLD.evalMarg_pushforward`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.evalMarg_pushforward), [`MIPRE.QLD.SimulPair.ψ_unit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.SimulPair.ψ_unit), [`MIPRE.QLD.SimulPair.transport`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.SimulPair.transport), [`MIPRE.QLD.SimulPair.transport_SA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.SimulPair.transport_SA), [`MIPRE.QLD.SimulPair.transport_SB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.SimulPair.transport_SB), [`MIPRE.QLD.CutSimul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.CutSimul).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 3814](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L3814)
