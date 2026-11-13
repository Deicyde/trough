---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.TorsionQuotientFinitelyPresentedKourovka19Problem24Wanted.torsionClosure, MathlibExt.GroupTheory.TorsionQuotientFinitelyPresentedKourovka19Problem24Wanted.existsFinitelyPresentedTorsionQuotientNotFinitelyPresented, MathlibExt.GroupTheory.TorsionQuotientFinitelyPresentedKourovka19Problem24Wanted.existsFinitelyPresentedTorsionQuotientNotFinitelyPresented_holds
statement: formalized
---

# Torsion quotients of finitely presented groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/torsion-quotients-of-finitely-presented-groups/index.html).

## Torsion closure

For a group $G$, $\mathrm{Tor}(G)$ is the normal closure in $G$ of the set
of elements of finite order of $G$.

Formalized by `MathlibExt.GroupTheory.TorsionQuotientFinitelyPresentedKourovka19Problem24Wanted.torsionClosure`, an abbreviation declared in [WantedExt/GroupTheory/TorsionQuotientFinitelyPresentedKourovka19Problem24Wanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/TorsionQuotientFinitelyPresentedKourovka19Problem24Wanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/torsion-quotients-of-finitely-presented-groups/index.html#torsion-closure).

## Kourovka Problem 19.24 (torsion quotients of finitely presented groups)

The statement,
asked by M. Chiodo and R. Vyas, that there exists a finitely presented group $G$ such that
$G / \mathrm{Tor}(G)$ is not finitely presented, where $\mathrm{Tor}(G)$ is the normal closure of
the set of elements of finite order of $G$.

Formalized by `MathlibExt.GroupTheory.TorsionQuotientFinitelyPresentedKourovka19Problem24Wanted.existsFinitelyPresentedTorsionQuotientNotFinitelyPresented`, a definition declared in [WantedExt/GroupTheory/TorsionQuotientFinitelyPresentedKourovka19Problem24Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/TorsionQuotientFinitelyPresentedKourovka19Problem24Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/torsion-quotients-of-finitely-presented-groups/index.html#exists-finitely-presented-torsion-quotie).

## Torsion quotients of finitely presented groups need not be finitely presented

There exists
a finitely presented group $G$ such that $G / \mathrm{Tor}(G)$ is not finitely presented, where
$\mathrm{Tor}(G)$ is the normal closure of the set of elements of finite order of $G$.

The Kourovka Archive answers Problem 19.24 "Yes, such groups exist": Leary and Minasyan
(Constructions 3.1 and 3.2) give a soluble example and a virtually torsion-free example.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 19.24 (M. Chiodo, R. Vyas); resolution: I. J. Leary and A. Minasyan, A note on torsion length and torsion subgroups, J. Group Theory 26 (2023), no. 4, 741-750 (arXiv:2112.14546), Section 3, Construction 3.1 (Abels' finitely presented soluble group H modulo an infinite cyclic central subgroup C: G = H / C has G / Tor(G) ≅ H / Z(H), which is not finitely presented) and Construction 3.2 (a virtually torsion-free example built from Bestvina-Brady groups); Kourovka Archive, Problem 19.24: Yes, such groups exist, one soluble and one virtually torsion-free, https://arxiv.org/abs/2112.14546.

Stated but not proved: `MathlibExt.GroupTheory.TorsionQuotientFinitelyPresentedKourovka19Problem24Wanted.existsFinitelyPresentedTorsionQuotientNotFinitelyPresented_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/TorsionQuotientFinitelyPresentedKourovka19Problem24Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/TorsionQuotientFinitelyPresentedKourovka19Problem24Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/torsion-quotients-of-finitely-presented-groups/index.html#exists-finitely-presented-torsion-quotie-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Torsion quotients of finitely presented groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/torsion-quotients-of-finitely-presented-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/presentations-and-decision-problems/torsion-quotients-of-finitely-presented-groups)
