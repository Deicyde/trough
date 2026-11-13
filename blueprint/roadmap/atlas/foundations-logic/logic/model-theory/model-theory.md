---
declaration: section
origin: cited
lean: MathlibExt.ModelTheory.MorleyCategoricityWanted.ModelTheory.morley_categoricity_theorem
statement: formalized
---

# Model theory: its own results

1 result, 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/index.html).

Relations between formal theories and their structures: first-order languages of algebraic structures, quantifier elimination, categoricity and o-minimality.

## Morley's categoricity theorem

Let $L$ be a first-order language with at most countably
many symbols, and let $T$ be a complete $L$-theory all of whose models are infinite. Call $T$
$\kappa$-categorical if any two models of $T$ of cardinality $\kappa$ are isomorphic. If $T$ is
$\kappa$-categorical for some uncountable cardinal $\kappa$, then $T$ is $\mu$-categorical for
every uncountable cardinal $\mu$.

## Sources

- M. Ramsey, *Morley's Categoricity Theorem* (UChicago VIGRE REU 2010), Corollary 7.3. https://www.math.uchicago.edu/~may/VIGRE/VIGRE2010/REUPapers/RamseyN.pdf. Problem `morley_categoricity_theorem` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.ModelTheory.MorleyCategoricityWanted.ModelTheory.morley_categoricity_theorem` is written with `theorem_wanted` in [WantedExt/ModelTheory/MorleyCategoricityWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/ModelTheory/MorleyCategoricityWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/index.html#morley-categoricity-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Model theory](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/model-theory)
