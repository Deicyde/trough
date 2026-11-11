---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SurjectiveRotaBaxterOperatorKourovka20Problem125Wanted.IsRotaBaxterOperator, MathlibExt.GroupTheory.SurjectiveRotaBaxterOperatorKourovka20Problem125Wanted.surjectiveNonInjectiveRotaBaxterOperatorExists, MathlibExt.GroupTheory.SurjectiveRotaBaxterOperatorKourovka20Problem125Wanted.surjectiveNonInjectiveRotaBaxterOperatorExists_holds
statement: formalized
---

# Rota–Baxter operators on groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/rota-baxter-operators-on-groups/index.html).

## Rota–Baxter operators on groups

A Rota–Baxter operator (of weight $1$) on a group $G$ is
a map $B \colon G \to G$ such that $B(g)\,B(h) = B\bigl(g\,B(g)\,h\,B(g)^{-1}\bigr)$ for all
$g, h \in G$.

Formalized by `MathlibExt.GroupTheory.SurjectiveRotaBaxterOperatorKourovka20Problem125Wanted.IsRotaBaxterOperator`, a definition declared in [WantedExt/GroupTheory/SurjectiveRotaBaxterOperatorKourovka20Problem125Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SurjectiveRotaBaxterOperatorKourovka20Problem125Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/rota-baxter-operators-on-groups/index.html#is-rota-baxter-operator).

## Kourovka Problem 20.125 (surjective non-injective Rota–Baxter operators)

The statement,
asked by V. G. Bardakov, that there exist a non-abelian group $G$ and a Rota–Baxter operator $B$ on
$G$ such that $B$ is surjective but not injective.

Formalized by `MathlibExt.GroupTheory.SurjectiveRotaBaxterOperatorKourovka20Problem125Wanted.surjectiveNonInjectiveRotaBaxterOperatorExists`, a definition declared in [WantedExt/GroupTheory/SurjectiveRotaBaxterOperatorKourovka20Problem125Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SurjectiveRotaBaxterOperatorKourovka20Problem125Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/rota-baxter-operators-on-groups/index.html#surjective-non-injective-rota-baxter-ope).

## A surjective, non-injective Rota–Baxter operator on a non-abelian group

There exist a
non-abelian group $G$ and a Rota–Baxter operator $B$ on $G$ that is surjective but not injective.

For example, van Doorn, Judin, Monticone and Morrison take $G = S_3 \times \mathbb{Z}^{\mathbb{N}}$
and $B(\sigma, f) = (\sigma^{-1}, s(f))$, where $s$ is the left shift.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 20.125 (V. G. Bardakov); resolution: P. Monticone, Kourovka Notebook Problem 20.125, solution note, 23 March 2026; W. van Doorn, E. Judin, P. Monticone and D. Morrison, On some problems from the Kourovka Notebook, preprint, arXiv:2607.17477 (2026), van Doorn-Judin-Monticone-Morrison, Theorem 5.1: G = S3 × Z^N with B(σ, f) = (σ⁻¹, s(f)), s the left shift; the Kourovka Notebook (21st issue) marks 20.125 solved (AI solution confirmed by V. G. Bardakov), https://arxiv.org/abs/2607.17477.

Stated but not proved: `MathlibExt.GroupTheory.SurjectiveRotaBaxterOperatorKourovka20Problem125Wanted.surjectiveNonInjectiveRotaBaxterOperatorExists_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SurjectiveRotaBaxterOperatorKourovka20Problem125Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SurjectiveRotaBaxterOperatorKourovka20Problem125Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/rota-baxter-operators-on-groups/index.html#surjective-non-injective-rota-baxter-ope-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rota–Baxter operators on groups](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/rota-baxter-operators-on-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/nonassociative-algebras/rota-baxter-operators-on-groups)
