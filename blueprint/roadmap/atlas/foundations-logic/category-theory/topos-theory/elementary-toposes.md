---
declaration: section
origin: cited
lean: MathlibExt.CategoryTheory.FundamentalToposWanted.ToposTheory.IsTopos, MathlibExt.CategoryTheory.FundamentalToposWanted.ToposTheory.fundamental_topos_theory
statement: formalized
---

# Elementary toposes

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/CategoryTheory/topos-theory/elementary-toposes/index.html).

## Elementary topos

A category $E$ is an elementary topos if it has all finite limits, it
admits a cartesian monoidal structure for which it is monoidal closed (that is, $E$ is cartesian
closed), and it has a subobject classifier.

Formalized by `MathlibExt.CategoryTheory.FundamentalToposWanted.ToposTheory.IsTopos`, a definition declared in [WantedExt/CategoryTheory/FundamentalToposWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/CategoryTheory/FundamentalToposWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/CategoryTheory/topos-theory/elementary-toposes/index.html#is-topos).

## Fundamental theorem of topos theory

If $E$ is an elementary topos and $X$ is an object
of $E$, then the slice category $E/X$ of objects of $E$ over $X$ is again an elementary topos.

## Sources

- F. W. Lawvere & M. Tierney (elementary topos, 1970); see S. Mac Lane & I. Moerdijk, *Sheaves in Geometry and Logic*, IV.7. Knill, *Some fundamental theorems in mathematics*, §54. Problem `fundamental_topos_theory` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.CategoryTheory.FundamentalToposWanted.ToposTheory.fundamental_topos_theory` is written with `theorem_wanted` in [WantedExt/CategoryTheory/FundamentalToposWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/CategoryTheory/FundamentalToposWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/CategoryTheory/topos-theory/elementary-toposes/index.html#fundamental-topos-theory).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Elementary toposes](https://deicyde.github.io/atlas-lean/roadmap/CategoryTheory/topos-theory/elementary-toposes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/CategoryTheory/topos-theory/elementary-toposes)
