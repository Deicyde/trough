---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.UniqueProductPresentationPolycyclicKourovka13Problem11Wanted.IsPolycyclic, MathlibExt.GroupTheory.UniqueProductPresentationPolycyclicKourovka13Problem11Wanted.IsAlmostPolycyclic, MathlibExt.GroupTheory.UniqueProductPresentationPolycyclicKourovka13Problem11Wanted.HasUniqueProductPresentation, MathlibExt.GroupTheory.UniqueProductPresentationPolycyclicKourovka13Problem11Wanted.torsionFreeUniqueProductAlmostPolycyclic, MathlibExt.GroupTheory.UniqueProductPresentationPolycyclicKourovka13Problem11Wanted.torsionFreeUniqueProductAlmostPolycyclic_refuted
statement: formalized
---

# Groups with unique ordered-product normal forms

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/groups-with-unique-ordered-product-normal-forms/index.html).

## Polycyclic groups (Kourovka Problem 13.11)

A group $G$ is polycyclic if it has a finite
series of subgroups $1 = H_0 \le H_1 \le \cdots \le H_n = G$ in which each $H_i$ is normal in
$H_{i+1}$ and each quotient $H_{i+1} / H_i$ is cyclic.

Formalized by `MathlibExt.GroupTheory.UniqueProductPresentationPolycyclicKourovka13Problem11Wanted.IsPolycyclic`, a definition declared in [WantedExt/GroupTheory/UniqueProductPresentationPolycyclicKourovka13Problem11Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/UniqueProductPresentationPolycyclicKourovka13Problem11Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/groups-with-unique-ordered-product-normal-forms/index.html#is-polycyclic).

## Almost polycyclic groups (Kourovka Problem 13.11)

A group $G$ is almost polycyclic, or
virtually polycyclic, if some subgroup of finite index in $G$ is polycyclic.

Formalized by `MathlibExt.GroupTheory.UniqueProductPresentationPolycyclicKourovka13Problem11Wanted.IsAlmostPolycyclic`, a definition declared in [WantedExt/GroupTheory/UniqueProductPresentationPolycyclicKourovka13Problem11Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/UniqueProductPresentationPolycyclicKourovka13Problem11Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/groups-with-unique-ordered-product-normal-forms/index.html#is-almost-polycyclic).

## Groups with a unique product presentation

A group $G$ has a unique product presentation if
there are $n \in \mathbb{N}$ and elements $a_0, \dots, a_{n-1} \in G$ such that every element of $G$
equals $a_0^{k_0} a_1^{k_1} \cdots a_{n-1}^{k_{n-1}}$ for exactly one tuple
$(k_0, \dots, k_{n-1}) \in \mathbb{Z}^n$.

Formalized by `MathlibExt.GroupTheory.UniqueProductPresentationPolycyclicKourovka13Problem11Wanted.HasUniqueProductPresentation`, a definition declared in [WantedExt/GroupTheory/UniqueProductPresentationPolycyclicKourovka13Problem11Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/UniqueProductPresentationPolycyclicKourovka13Problem11Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/groups-with-unique-ordered-product-normal-forms/index.html#has-unique-product-presentation).

## Kourovka Problem 13.11 (torsion-free groups with a unique product presentation)

The
statement, asked by V. V. Bludov, that every group $G$ which is torsion-free (no element of $G$
other than $1$ has finite order) and has a unique product presentation is almost polycyclic.

Formalized by `MathlibExt.GroupTheory.UniqueProductPresentationPolycyclicKourovka13Problem11Wanted.torsionFreeUniqueProductAlmostPolycyclic`, a definition declared in [WantedExt/GroupTheory/UniqueProductPresentationPolycyclicKourovka13Problem11Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/UniqueProductPresentationPolycyclicKourovka13Problem11Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/groups-with-unique-ordered-product-normal-forms/index.html#torsion-free-unique-product-almost-polyc).

## A torsion-free group with a unique product presentation need not be almost polycyclic

Not
every torsion-free group with a unique product presentation is almost polycyclic: there is a group
$G$ in which no element other than $1$ has finite order, which has a unique product presentation,
and which is not almost polycyclic.

Muranov's theorem gives such a group with $n$ generators for every $n \ge 63$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 13.11 (V. V. Bludov); resolution: A. Muranov, On torsion-free groups with finite regular file bases, Trans. Amer. Math. Soc. 359 (2007), 3609-3645, Theorem (Section 1, proved at the end of Section 5), https://doi.org/10.1090/S0002-9947-07-04256-0.

Stated but not proved: `MathlibExt.GroupTheory.UniqueProductPresentationPolycyclicKourovka13Problem11Wanted.torsionFreeUniqueProductAlmostPolycyclic_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/UniqueProductPresentationPolycyclicKourovka13Problem11Wanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/UniqueProductPresentationPolycyclicKourovka13Problem11Wanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/groups-with-unique-ordered-product-normal-forms/index.html#torsion-free-unique-product-almost-polyc-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Groups with unique ordered-product normal forms](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/groups-with-unique-ordered-product-normal-forms/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/commutators-and-engel-conditions/groups-with-unique-ordered-product-normal-forms)
