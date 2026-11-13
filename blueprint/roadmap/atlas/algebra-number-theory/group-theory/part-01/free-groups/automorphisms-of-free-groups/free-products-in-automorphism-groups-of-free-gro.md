---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FreeProductAutFreeGroupEmbeddingKourovka18Problem11Wanted.freeProductAutFreeGroupEmbeds, MathlibExt.GroupTheory.FreeProductAutFreeGroupEmbeddingKourovka18Problem11Wanted.freeProductAutFreeGroupEmbeds_holds
statement: formalized
---

# Free products in automorphism groups of free groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/free-products-in-automorphism-groups-of-free-gro/index.html).

## Bardakov's question on free products in $\mathrm{Aut}(F_n)$ (Kourovka 18.11)

The statement
that for every natural number $n \ge 2$ and all subgroups $G$ and $H$ of the automorphism group
$\mathrm{Aut}(F_n)$ of the free group $F_n$ of rank $n$, there are a natural number $m$ and an
injective group homomorphism from the free product $G \ast H$ to $\mathrm{Aut}(F_m)$.

Formalized by `MathlibExt.GroupTheory.FreeProductAutFreeGroupEmbeddingKourovka18Problem11Wanted.freeProductAutFreeGroupEmbeds`, a definition declared in [WantedExt/GroupTheory/FreeProductAutFreeGroupEmbeddingKourovka18Problem11Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeProductAutFreeGroupEmbeddingKourovka18Problem11Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/free-products-in-automorphism-groups-of-free-gro/index.html#free-product-aut-free-group-embeds).

## Free products of subgroups of $\mathrm{Aut}(F_n)$ embed in some $\mathrm{Aut}(F_m)$

For
every natural number $n \ge 2$ and all subgroups $G$ and $H$ of the automorphism group
$\mathrm{Aut}(F_n)$ of the free group $F_n$ of rank $n$, there are a natural number $m$ and an
injective group homomorphism from the free product $G \ast H$ to $\mathrm{Aut}(F_m)$.

Jayadevan constructs, for subgroups $G \le \mathrm{Aut}(F_n)$ and $H \le \mathrm{Aut}(F_k)$ with
no finite-generation hypothesis, an embedding of $G \ast H$ in $\mathrm{Aut}(F_{n+k+3})$; the
Kourovka Notebook (21st issue) answers 18.11 "Yes, it is true" (AI solution confirmed by V. G.
Bardakov).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 18.11 (V. G. Bardakov); resolution: A. Jayadevan, Free products of free-group automorphism groups: a finite-rank embedding by separating cocycles, preprint, Zenodo record 22722085 (2026), abstract (for G ≤ Aut(F_n), H ≤ Aut(F_m), G ∗ H embeds in Aut(F_{n+m+3}); no finite-generation hypothesis); the Kourovka Notebook (21st issue) marks 18.11 solved (Yes, it is true; AI solution confirmed by V. G. Bardakov), https://zenodo.org/records/22722085.

Stated but not proved: `MathlibExt.GroupTheory.FreeProductAutFreeGroupEmbeddingKourovka18Problem11Wanted.freeProductAutFreeGroupEmbeds_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/FreeProductAutFreeGroupEmbeddingKourovka18Problem11Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeProductAutFreeGroupEmbeddingKourovka18Problem11Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/free-products-in-automorphism-groups-of-free-gro/index.html#free-product-aut-free-group-embeds-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Free products in automorphism groups of free groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/free-products-in-automorphism-groups-of-free-gro/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/free-products-in-automorphism-groups-of-free-gro)
