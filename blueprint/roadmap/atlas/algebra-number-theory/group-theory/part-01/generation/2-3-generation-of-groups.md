---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SL3IntTwoThreeGenerationKourovka14Problem49Wanted.sl3IntGeneratedByOrderTwoAndThree, MathlibExt.GroupTheory.SL3IntTwoThreeGenerationKourovka14Problem49Wanted.sl3IntGeneratedByOrderTwoAndThree_refuted
statement: formalized
---

# (2,3)-generation of groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/generation/2-3-generation-of-groups/index.html).

## $(2,3)$-generation of $\mathrm{SL}_3(\mathbb{Z})$ (Kourovka 14.49)

The statement that
there are $a, b \in \mathrm{SL}_3(\mathbb{Z})$ such that $a$ has order $2$, $b$ has order $3$, and
$a$ and $b$ generate $\mathrm{SL}_3(\mathbb{Z})$.

Kourovka Notebook Problem 14.49 (M. Conder) asks whether $\mathrm{SL}_3(\mathbb{Z})$ is a quotient
of the modular group $\mathrm{PSL}_2(\mathbb{Z}) \cong C_2 \ast C_3$; since
$\mathrm{SL}_3(\mathbb{Z})$ is not cyclic, this is equivalent to the statement above.

Formalized by `MathlibExt.GroupTheory.SL3IntTwoThreeGenerationKourovka14Problem49Wanted.sl3IntGeneratedByOrderTwoAndThree`, a definition declared in [WantedExt/GroupTheory/SL3IntTwoThreeGenerationKourovka14Problem49Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SL3IntTwoThreeGenerationKourovka14Problem49Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/generation/2-3-generation-of-groups/index.html#sl3-int-generated-by-order-two-and-three).

## $\mathrm{SL}_3(\mathbb{Z})$ is not $(2,3)$-generated

There are no $a, b \in
\mathrm{SL}_3(\mathbb{Z})$ such that $a$ has order $2$, $b$ has order $3$, and $a$ and $b$ generate
$\mathrm{SL}_3(\mathbb{Z})$. Equivalently, $\mathrm{SL}_3(\mathbb{Z})$ is not a quotient of the
modular group $\mathrm{PSL}_2(\mathbb{Z}) \cong C_2 \ast C_3$.

This is the negative answer to Kourovka Notebook Problem 14.49 (M. Conder), due to Tamburini and
Zucca, and Nuzhin.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 14.49 (M. Conder); resolution: M. C. Tamburini and P. Zucca, Rend. Lincei Mat. Appl. (9) 11 (2000), no. 1, 5-7; Ya. N. Nuzhin, Math. Notes 70 (2001), no. 1-2, 71-78, Kourovka Archive, Problem 14.49 (answer: No, it is not; SL_d(ℤ) is such a quotient for d ≥ 28).

Stated but not proved: `MathlibExt.GroupTheory.SL3IntTwoThreeGenerationKourovka14Problem49Wanted.sl3IntGeneratedByOrderTwoAndThree_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/SL3IntTwoThreeGenerationKourovka14Problem49Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SL3IntTwoThreeGenerationKourovka14Problem49Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/generation/2-3-generation-of-groups/index.html#sl3-int-generated-by-order-two-and-three-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: (2,3)-generation of groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/generation/2-3-generation-of-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/generation/2-3-generation-of-groups)
