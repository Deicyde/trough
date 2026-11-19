---
declaration: theorem
origin: cited
lean: ProbabilityTheory.bayesBinaryRisk_le_bayesBinaryRisk_comp
statement: formalized
proof: formalized
---

# Data-processing inequality

For $\mu, \nu \in \mathcal M(\mathcal X)$ and $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ a Markov kernel, $\mathcal B_\xi(\kappa \circ \mu, \kappa \circ \nu) \ge \mathcal B_\xi(\mu, \nu)$ .

## Depends on

- [bayesBinaryRisk](def-bayesbinaryrisk.md)

## Proof depends on

- [Data-processing inequality](../risk/thm-data-proc-bayesrisk.md)

## Proof

Apply Theorem [Data-processing inequality](../risk/thm-data-proc-bayesrisk.md).

## Lean

Formalized as [`ProbabilityTheory.bayesBinaryRisk_le_bayesBinaryRisk_comp`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.bayesBinaryRisk_le_bayesBinaryRisk_comp).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 614](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L614)
