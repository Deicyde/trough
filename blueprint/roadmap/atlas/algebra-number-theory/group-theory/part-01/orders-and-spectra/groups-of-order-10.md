---
declaration: section
origin: cited
lean: MetaMathlibExt.nonempty_mulEquiv_dihedralGroup_of_card_eq_ten_of_not_isCyclic, MetaMathlibExt.groups_of_order_10_classification, MetaMathlibExt.groups_of_order_10_classification_xor, MetaMathlibExt.groups_of_order_10_classification_prod, MetaMathlibExt.groups_of_order_10_classification_prod_xor
statement: formalized
proof: formalized
---

# Groups of order 10

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/groups-of-order-10/index.html).

## Noncyclic groups of order 10 are dihedral

Every finite group of order $10$ that is not
cyclic is isomorphic to the dihedral group $D_5$ of order $10$.

## Sources

- the generators and inversion argument are adapted from the archived AlgebraNotes source; the final isomorphism uses the shared index-two constructor.

Formalized by `MetaMathlibExt.nonempty_mulEquiv_dihedralGroup_of_card_eq_ten_of_not_isCyclic`, a theorem declared in [MathlibExt/GroupTheory/SpecificGroups/OrderTen.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/SpecificGroups/OrderTen.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/groups-of-order-10/index.html#nonempty-mul-equiv-dihedral-group-of-car).

## Classification of groups of order 10

Every finite group of order $10$ is isomorphic
either to the cyclic group $C_{10}$ of order $10$ or to the dihedral group $D_5$ of order $10$.

Formalized by `MetaMathlibExt.groups_of_order_10_classification`, a theorem declared in [MathlibExt/GroupTheory/SpecificGroups/OrderTen.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/SpecificGroups/OrderTen.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/groups-of-order-10/index.html#groups-of-order-10-classification).

## Exclusive classification of groups of order 10

Let $G$ be a finite group of order $10$.
Then exactly one of the following holds: $G$ is isomorphic to the cyclic group $C_{10}$ of order
$10$, or $G$ is isomorphic to the dihedral group $D_5$ of order $10$.

The two alternatives cannot both hold, since $C_{10}$ is cyclic, $D_5$ is not, and cyclicity is
preserved under isomorphism.

Formalized by `MetaMathlibExt.groups_of_order_10_classification_xor`, a theorem declared in [MathlibExt/GroupTheory/SpecificGroups/OrderTen.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/SpecificGroups/OrderTen.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/groups-of-order-10/index.html#groups-of-order-10-classification-xor).

## Classification of groups of order 10, product form

Let $C_n$ denote the cyclic group of
order $n$ and let $D_5$ denote the dihedral group of order $10$. Every finite group of order $10$
is isomorphic to the direct product $C_5 \times C_2$ or to $D_5$.

Formalized by `MetaMathlibExt.groups_of_order_10_classification_prod`, a theorem declared in [MathlibExt/GroupTheory/SpecificGroups/OrderTen.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/SpecificGroups/OrderTen.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/groups-of-order-10/index.html#groups-of-order-10-classification-prod).

## Exclusive classification of groups of order 10, product form

Let $G$ be a finite group
of order $10$, let $C_n$ denote the cyclic group of order $n$, and let $D_5$ denote the dihedral
group of order $10$. Then exactly one of the following holds: $G$ is isomorphic to the direct
product $C_5 \times C_2$, or $G$ is isomorphic to $D_5$.

The product $C_5 \times C_2$ is cyclic and $D_5$ is not, so the two alternatives cannot both hold.

Formalized by `MetaMathlibExt.groups_of_order_10_classification_prod_xor`, a theorem declared in [MathlibExt/GroupTheory/SpecificGroups/OrderTen.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/SpecificGroups/OrderTen.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/groups-of-order-10/index.html#groups-of-order-10-classification-prod-x).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Groups of order 10](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/groups-of-order-10/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/orders-and-spectra/groups-of-order-10)
