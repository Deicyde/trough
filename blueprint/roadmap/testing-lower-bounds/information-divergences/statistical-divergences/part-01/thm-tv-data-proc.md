---
declaration: theorem
origin: cited
lean: ProbabilityTheory.tv_comp_le
statement: formalized
proof: formalized
---

# Data-processing inequality

For $\mu, \nu \in \mathcal M(\mathcal X)$ and $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ a Markov kernel, $\operatorname{TV}(\kappa \circ \mu, \kappa \circ \nu) \le \operatorname{TV}(\mu, \nu)$ .

## Depends on

- [TV](def-tv.md)

## Proof depends on

- [Data-processing inequality](thm-data-proc-statinfo.md)

## Proof

Apply Theorem [Data-processing inequality](thm-data-proc-statinfo.md).

## Lean

Formalized as [`ProbabilityTheory.tv_comp_le`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.tv_comp_le).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/stat_div.tex, line 515](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/stat_div.tex#L515)
