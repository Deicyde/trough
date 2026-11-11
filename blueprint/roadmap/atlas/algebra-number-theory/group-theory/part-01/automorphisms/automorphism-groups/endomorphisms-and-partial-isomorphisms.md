---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.EndomorphismPartialIsomorphismCountKourovka19Problem20Wanted.endPartialIsoCountImpliesAbelian, MathlibExt.GroupTheory.EndomorphismPartialIsomorphismCountKourovka19Problem20Wanted.endPartialIsoCountImpliesAbelian_refuted
statement: formalized
---

# Endomorphisms and partial isomorphisms

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/endomorphisms-and-partial-isomorphisms/index.html).

## Kourovka Problem 19.20 (Cameron)

The statement that every finite group $G$ with
$|\mathrm{End}(G)| = |\mathrm{PIso}(G)|$ is abelian. Here $\mathrm{End}(G)$ is the set of
endomorphisms of $G$, and $\mathrm{PIso}(G)$ is the set of partial isomorphisms of $G$: the triples
$(H, K, f)$ of subgroups $H$, $K$ of $G$ and an isomorphism $f \colon H \to K$.

Formalized by `MathlibExt.GroupTheory.EndomorphismPartialIsomorphismCountKourovka19Problem20Wanted.endPartialIsoCountImpliesAbelian`, a definition declared in [WantedExt/GroupTheory/EndomorphismPartialIsomorphismCountKourovka19Problem20Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EndomorphismPartialIsomorphismCountKourovka19Problem20Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/endomorphisms-and-partial-isomorphisms/index.html#end-partial-iso-count-implies-abelian).

## Equal endomorphism and partial isomorphism counts do not force commutativity

There is a
finite non-abelian group $G$ with $|\mathrm{End}(G)| = |\mathrm{PIso}(G)|$. Here $\mathrm{End}(G)$
is the set of endomorphisms of $G$, and $\mathrm{PIso}(G)$ is the set of partial isomorphisms of
$G$: the triples $(H, K, f)$ of subgroups $H$, $K$ of $G$ and an isomorphism $f \colon H \to K$.
This answers Kourovka Problem 19.20 (P. J. Cameron) in the negative.

K. Muliarchyk's Theorem 1.1 (2026) gives a non-abelian group of order $512$ for which both counts
equal $129 \cdot 2^{24}$; the Kourovka Notebook (21st issue) answers 19.20 "No, it is not".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 19.20 (P. J. Cameron); resolution: K. Muliarchyk, A nonabelian group with equally many endomorphisms and partial isomorphisms: a computer-assisted counterexample to Kourovka Problem 19.20, preprint, 2026, Theorem 1.1: a nonabelian group of order 512, nilpotency class two and exponent four, with |PIso(G)| = |End(G)| = 129 · 2^24 (the partial isomorphisms counted by exhaustive enumeration); the Kourovka Notebook (21st issue) marks 19.20 solved: No, it is not, https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/09/kourovka_19.20_solution.pdf.

Stated but not proved: `MathlibExt.GroupTheory.EndomorphismPartialIsomorphismCountKourovka19Problem20Wanted.endPartialIsoCountImpliesAbelian_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/EndomorphismPartialIsomorphismCountKourovka19Problem20Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EndomorphismPartialIsomorphismCountKourovka19Problem20Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/endomorphisms-and-partial-isomorphisms/index.html#end-partial-iso-count-implies-abelian-re).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Endomorphisms and partial isomorphisms](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/endomorphisms-and-partial-isomorphisms/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/automorphisms/automorphism-groups/endomorphisms-and-partial-isomorphisms)
