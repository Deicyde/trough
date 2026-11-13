---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.MonochromeSymmetricSubsetKourovka15Problem77Wanted.monochromeSymmetricSubsetExists, MathlibExt.GroupTheory.MonochromeSymmetricSubsetKourovka15Problem77Wanted.monochromeSymmetricSubsetExists_holds
statement: formalized
---

# Monochromatic symmetric subsets of abelian groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/monochromatic-symmetric-subsets-of-abelian-group/index.html).

## Monochrome symmetric subsets (Kourovka 15.77)

The statement, written additively, that for
every infinite abelian group $G$, every cardinal $\alpha < |G|$, every natural number $n$ and every
colouring $\chi \colon G \to \{0, \dots, n - 1\}$, there are a set $A \subseteq G$ of cardinality
$\alpha$ on which $\chi$ is constant and an element $g \in G$ such that $2g - a \in A$ for every
$a \in A$; that is, $A$ is a monochrome set symmetric with respect to $g$.

Formalized by `MathlibExt.GroupTheory.MonochromeSymmetricSubsetKourovka15Problem77Wanted.monochromeSymmetricSubsetExists`, a definition declared in [WantedExt/GroupTheory/MonochromeSymmetricSubsetKourovka15Problem77Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MonochromeSymmetricSubsetKourovka15Problem77Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/monochromatic-symmetric-subsets-of-abelian-group/index.html#monochrome-symmetric-subset-exists).

## Monochromatic symmetric subsets in finite colourings (Jayadevan)

Let $G$ be an infinite
abelian group, written additively, let $\alpha$ be a cardinal with $\alpha < |G|$, and let $n$ be
a natural number. For every colouring $\chi \colon G \to \{0, \dots, n - 1\}$ there are a set
$A \subseteq G$ of cardinality $\alpha$ on which $\chi$ is constant and an element $g \in G$ such
that $2g - a \in A$ for every $a \in A$.

This answers Kourovka Problem 15.77 (I. V. Protasov) affirmatively; the Kourovka Notebook (21st
issue) marks it solved, "Yes, it is true" (AI solution confirmed by I. V. Protasov).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 15.77 (I. V. Protasov); resolution: A. Jayadevan, Monochromatic symmetric subsets in finite colourings of infinite abelian groups, preprint, Zenodo record 22909420 (2026), AI-generated solution confirmed by I. V. Protasov, main theorem (for G infinite abelian and α < |G|, every finite colouring has a monochromatic S with |S| = α and 2g - S = S for some g); the Kourovka Notebook (21st issue) marks 15.77 solved, https://zenodo.org/records/22909420.

Stated but not proved: `MathlibExt.GroupTheory.MonochromeSymmetricSubsetKourovka15Problem77Wanted.monochromeSymmetricSubsetExists_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/MonochromeSymmetricSubsetKourovka15Problem77Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MonochromeSymmetricSubsetKourovka15Problem77Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/monochromatic-symmetric-subsets-of-abelian-group/index.html#monochrome-symmetric-subset-exists-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monochromatic symmetric subsets of abelian groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/monochromatic-symmetric-subsets-of-abelian-group/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/combinatorics-in-groups/monochromatic-symmetric-subsets-of-abelian-group)
