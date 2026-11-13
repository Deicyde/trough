---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.StrangLemma.strang_first_lemma, MathlibExt.Analysis.InnerProductSpace.StrangLemma.strang_first_lemma_iInf
statement: formalized
proof: formalized
---

# Strang's lemma

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/strang-s-lemma/index.html).

## Strang's first lemma

**Strang's first lemma** (pointwise form): if `u` solves the exact
variational problem `B u w = ℓ w` and `uh` solves the perturbed problem
`Bh uh w = ℓh w` on the discrete space `V` (embedded by the linear isometry
`J`), and `Bh` is coercive with constant `α`, then for every competitor
`vh : V` the error `‖u - J uh‖` is bounded by the best-approximation
error of `u` at `vh` plus the consistency errors. Here
`Bh - B.bilinearComp J J` measures the bilinear-form crime and
`ℓh - ℓ.comp J` measures the functional crime.

Formalized by `MathlibExt.Analysis.InnerProductSpace.StrangLemma.strang_first_lemma`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/StrangLemma.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/StrangLemma.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/strang-s-lemma/index.html#strang-first-lemma).

## Strang's first lemma

**Strang's first lemma** (infimum form): the error is bounded by the
best-approximation error `⨅ vh : V, ‖u - J vh‖` plus the consistency
errors.

Formalized by `MathlibExt.Analysis.InnerProductSpace.StrangLemma.strang_first_lemma_iInf`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/StrangLemma.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/StrangLemma.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/strang-s-lemma/index.html#strang-first-lemma-i-inf).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Strang's lemma](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/strang-s-lemma/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/numerical-analysis/strang-s-lemma)
