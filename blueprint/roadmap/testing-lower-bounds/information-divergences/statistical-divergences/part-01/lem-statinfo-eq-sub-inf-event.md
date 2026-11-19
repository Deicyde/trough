---
declaration: lemma
origin: cited
lean: ProbabilityTheory.statInfo_eq_min_sub_iInf_measurableSet
statement: formalized
proof: formalized
---

# statInfo_eq_sub_inf_event

For finite measures $\mu, \nu$ and $\xi \in \mathcal M(\{0,1\})$,

$$
\begin{aligned}
\mathcal I_\xi(\mu, \nu)
&= \min\{\xi_0 \mu(\mathcal X), \xi_1 \nu(\mathcal X)\} - \inf_{E \text{ event}} \left( \xi_0 \mu(E) + \xi_1 \nu(E^c) \right)
\: .
\end{aligned}
$$

## Depends on

- [statInfo](def-statinfo.md)

## Proof depends on

- [bayesBinaryRisk_eq_event](../../../testing-estimation-risk/simple-binary-hypothesis-testing/lem-bayesbinaryrisk-eq-event.md)

## Proof

This is a direct application of Lemma [bayesBinaryRisk_eq_event](../../../testing-estimation-risk/simple-binary-hypothesis-testing/lem-bayesbinaryrisk-eq-event.md).

## Lean

Formalized as [`ProbabilityTheory.statInfo_eq_min_sub_iInf_measurableSet`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.statInfo_eq_min_sub_iInf_measurableSet).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/stat_div.tex, line 227](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/stat_div.tex#L227)
