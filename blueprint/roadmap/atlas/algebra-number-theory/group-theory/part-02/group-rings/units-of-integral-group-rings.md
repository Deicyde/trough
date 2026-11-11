---
declaration: section
origin: cited
lean: MathlibExt.Algebra.ExoticUnitsC2C2C2C6Wanted.OWRGroup, MathlibExt.Algebra.ExoticUnitsC2C2C2C6Wanted.OWRGroupRing, MathlibExt.Algebra.ExoticUnitsC2C2C2C6Wanted.conjecture, MathlibExt.Algebra.ExoticUnitsC2C2C2C6Wanted.conjecture_refuted
statement: formalized
---

# Units of integral group rings

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/units-of-integral-group-rings/index.html).

## The group $C_2 \times C_2 \times C_2 \times C_6$

The abelian group
$G = C_2 \times C_2 \times C_2 \times C_6$, the product of cyclic groups of orders $2$, $2$, $2$
and $6$, written additively as
$\mathbb{Z}/2 \times \mathbb{Z}/2 \times \mathbb{Z}/2 \times \mathbb{Z}/6$.

## Sources

- `OWR-11129-005` (Computational Group Theory (2012), Oberwolfach Reports, DOI 10.4171/owr/2011/37).

Formalized by `MathlibExt.Algebra.ExoticUnitsC2C2C2C6Wanted.OWRGroup`, an abbreviation declared in [WantedExt/Algebra/ExoticUnitsC2C2C2C6Wanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/ExoticUnitsC2C2C2C6Wanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/units-of-integral-group-rings/index.html#owrgroup).

## The integral group ring of $C_2 \times C_2 \times C_2 \times C_6$

The integral group
ring $\mathbb{Z}G$ of $G = C_2 \times C_2 \times C_2 \times C_6$: finitely supported formal
$\mathbb{Z}$-linear combinations of elements of $G$, with the product extending the group
operation of $G$ bilinearly.

## Sources

- `OWR-11129-005` (Computational Group Theory (2012), Oberwolfach Reports, DOI 10.4171/owr/2011/37).

Formalized by `MathlibExt.Algebra.ExoticUnitsC2C2C2C6Wanted.OWRGroupRing`, an abbreviation declared in [WantedExt/Algebra/ExoticUnitsC2C2C2C6Wanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/ExoticUnitsC2C2C2C6Wanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/units-of-integral-group-rings/index.html#owrgroup-ring).

## Exotic unit conjecture for $C_2 \times C_2 \times C_2 \times C_6$

Let
$G = C_2 \times C_2 \times C_2 \times C_6$. The statement that the integral group ring
$\mathbb{Z}G$ contains an exotic unit: a unit $u$ with $u \ne g$ and $u \ne -g$ for every
$g \in G$.

## Sources

- the open question of `OWR-11129-005` (Computational Group Theory (2012), Oberwolfach Reports, DOI 10.4171/owr/2011/37).

Formalized by `MathlibExt.Algebra.ExoticUnitsC2C2C2C6Wanted.conjecture`, a definition declared in [WantedExt/Algebra/ExoticUnitsC2C2C2C6Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/ExoticUnitsC2C2C2C6Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/units-of-integral-group-rings/index.html#conjecture).

## No exotic units in the integral group ring of $C_2 \times C_2 \times C_2 \times C_6$

Let
$G = C_2 \times C_2 \times C_2 \times C_6$. Every unit $u$ of the integral group ring
$\mathbb{Z}G$ is trivial: $u = g$ or $u = -g$ for some $g \in G$.

Classical: G. Higman (1940) showed the integral group ring of an abelian group
of exponent dividing 4 or 6 has only the units $\pm g$. Via the cut-group criterion in Bächle
(arXiv:1701.04347, Prop. 2.2), $C_2^3 \times C_6$ (exponent 6) is an abelian cut group, so every
unit of $\mathbb{Z}G$ is trivial and no exotic unit exists.

## Sources

- Andreas Bächle, Integral group rings of solvable groups with trivial central units, Forum Math. 30 (2018), arXiv:1701.04347, https://arxiv.org/abs/1701.04347.

Stated but not proved: `MathlibExt.Algebra.ExoticUnitsC2C2C2C6Wanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Algebra/ExoticUnitsC2C2C2C6Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/ExoticUnitsC2C2C2C6Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/units-of-integral-group-rings/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Units of integral group rings](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/units-of-integral-group-rings/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/group-rings/units-of-integral-group-rings)
