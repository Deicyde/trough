---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.bayesRisk_compProd_le_bayesRisk
---

# bayesRisk_compProd_le_fst

For $P : \Theta \rightsquigarrow \mathcal X$ and $\kappa : \Theta \times \mathcal X \rightsquigarrow \mathcal X'$ a Markov kernel, $\mathcal R^{P \otimes \kappa}_\pi \le \mathcal R^{P}_\pi$ .

## Depends on

- [Bayes risk](def-bayesrisk.md)

## Proof depends on

- [Data-processing inequality](thm-data-proc-bayesrisk.md)

## Proof

Use Theorem [Data-processing inequality](thm-data-proc-bayesrisk.md): $P$ is the composition of $P \otimes \kappa$ and the deterministic kernel $\mathcal X \times \mathcal X' \rightsquigarrow \mathcal X$ that forgets the second value.

## Lean

Formalized as [`ProbabilityTheory.bayesRisk_compProd_le_bayesRisk`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.bayesRisk_compProd_le_bayesRisk).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 187](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L187)
