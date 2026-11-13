---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.DivisionRingExtensionSplitKourovka18Problem76Wanted.divisionRingMultiplicationExtensionsSplit, MathlibExt.GroupTheory.DivisionRingExtensionSplitKourovka18Problem76Wanted.divisionRingMultiplicationExtensionsSplit_refuted
statement: formalized
---

# Extensions of the additive group of a division ring

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/extensions-of-the-additive-group-of-a-division-r/index.html).

## Palyutin's splitting problem for division rings (Kourovka 18.76)

The statement that for
every division ring $A$, every subgroup $G$ of its unit group $A^\times$ and every group $E$, if
$i$ is an injective homomorphism from the additive group of $A$ to $E$ and $\pi : E \to G$ is a
surjective homomorphism whose kernel is the image of $i$, such that
$e \, i(a) \, e^{-1} = i(\pi(e) a)$ for all $e \in E$ and $a \in A$ (so $G$ acts on the kernel by
left multiplication), then the extension splits: there is a homomorphism $s : G \to E$ with
$\pi(s(g)) = g$ for every $g \in G$.

Formalized by `MathlibExt.GroupTheory.DivisionRingExtensionSplitKourovka18Problem76Wanted.divisionRingMultiplicationExtensionsSplit`, a definition declared in [WantedExt/GroupTheory/DivisionRingExtensionSplitKourovka18Problem76Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DivisionRingExtensionSplitKourovka18Problem76Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/extensions-of-the-additive-group-of-a-division-r/index.html#division-ring-multiplication-extensions).

## Extensions of a division ring's additive group by units need not split (Kourovka 18.76)

There exist a division ring $A$, a subgroup $G$ of its unit group $A^\times$, a group $E$, an
injective homomorphism $i$ from the additive group of $A$ to $E$ and a surjective homomorphism
$\pi : E \to G$ whose kernel is the image of $i$, with $e \, i(a) \, e^{-1} = i(\pi(e) a)$ for all
$e \in E$ and $a \in A$, such that no homomorphism $s : G \to E$ satisfies $\pi(s(g)) = g$ for all
$g \in G$. That is, the splitting statement of Kourovka Problem 18.76 is false.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 18.76 (E. A. Palyutin); resolution: M. Kinyon and J. Urban, Results on problems from the Kourovka Notebook, preprint, version 4, 19 September 2026; Achyuth Jayadevan, preprint of 14 September 2026, https://zenodo.org/records/22751423, Kinyon-Urban Section 3.28: G = F × L with F, L free of rank 2, D the division closure of kG in a Mal'cev-Neumann division ring (k = Q or a prime field), and a nonsplit extension of (D, +) by G whose conjugation action on the kernel is left multiplication; AI solutions confirmed by B. A. F. Wehrfritz, accepted in the Kourovka Notebook (21st issue), https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/09/kourovka-mathematics.pdf.

Stated but not proved: `MathlibExt.GroupTheory.DivisionRingExtensionSplitKourovka18Problem76Wanted.divisionRingMultiplicationExtensionsSplit_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/DivisionRingExtensionSplitKourovka18Problem76Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DivisionRingExtensionSplitKourovka18Problem76Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/extensions-of-the-additive-group-of-a-division-r/index.html#division-ring-multiplication-extensions-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Extensions of the additive group of a division ring](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/extensions-of-the-additive-group-of-a-division-r/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/extensions-and-cohomology/extensions-of-the-additive-group-of-a-division-r)
