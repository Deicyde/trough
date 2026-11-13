---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ZassenhausConjectureKourovka17Problem67Wanted.zassenhausConjecture, MathlibExt.GroupTheory.ZassenhausConjectureKourovka17Problem67Wanted.zassenhausConjecture_refuted
statement: formalized
---

# Zassenhaus conjectures

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/zassenhaus-conjectures/index.html).

## Zassenhaus conjecture on torsion units

Kourovka 17.67 (H. Zassenhaus's conjecture, recorded by V. D. Mazurov): every unit of finite
order of the integral group ring `ℤG` of a finite group `G` is conjugate, by a unit of the rational
group ring `ℚG`, to an element `±g` with `g ∈ G`.

Formalized by `MathlibExt.GroupTheory.ZassenhausConjectureKourovka17Problem67Wanted.zassenhausConjecture`, a definition declared in [WantedExt/GroupTheory/ZassenhausConjectureKourovka17Problem67Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ZassenhausConjectureKourovka17Problem67Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/zassenhaus-conjectures/index.html#zassenhaus-conjecture).

## Counterexample to the first Zassenhaus conjecture (Kourovka 17.67)

There exist a finite
group $G$ and a unit $u$ of finite order of the integral group ring $\mathbb{Z}G$ such that for
every unit $v$ of the rational group ring $\mathbb{Q}G$, every $g \in G$ and every sign
$\varepsilon \in \{1, -1\}$, the conjugate $v u v^{-1}$, computed in $\mathbb{Q}G$, is not equal
to $\varepsilon g$. That is, the first Zassenhaus conjecture is false.

Eisele and Margolis (abstract and Theorem A) give a metabelian group $G$ of order
$2^7 \cdot 3^2 \cdot 5 \cdot 7^2 \cdot 19^2$ and a unit of order $7 \cdot 19$ in $\mathbb{Z}G$
that is not conjugate in $\mathbb{Q}G$ to any element $\pm g$, $g \in G$; the Kourovka Archive
records for 17.67 "A counterexample was constructed".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 17.67 (V. D. Mazurov); resolution: F. Eisele and L. Margolis, A counterexample to the first Zassenhaus conjecture, Adv. Math. 339 (2018), 599-641, abstract and Theorem A (a metabelian group of order 2⁷·3²·5·7²·19² whose integral group ring contains a unit of order 7·19 not conjugate in the rational group algebra to any ±g); Kourovka Archive, Problem 17.67 (A counterexample was constructed), http://eprints.gla.ac.uk/177223/7/177223.pdf.

Stated but not proved: `MathlibExt.GroupTheory.ZassenhausConjectureKourovka17Problem67Wanted.zassenhausConjecture_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/ZassenhausConjectureKourovka17Problem67Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ZassenhausConjectureKourovka17Problem67Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/zassenhaus-conjectures/index.html#zassenhaus-conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Zassenhaus conjectures](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/zassenhaus-conjectures/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/group-rings/zassenhaus-conjectures)
