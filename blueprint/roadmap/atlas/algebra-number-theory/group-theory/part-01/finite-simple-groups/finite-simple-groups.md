---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.BrauerFowlerWanted.GroupTheory.brauer_fowler, MathlibExt.GroupTheory.GorensteinWalterWanted.GroupTheory.gorenstein_walter
statement: formalized
---

# Finite simple groups and involutions: its own results

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-simple-groups/index.html).

Finite simple and almost simple groups and the local analysis behind their classification: specific simple groups (Mathieu, Suzuki, PSL), strongly embedded subgroups (Bender–Suzuki), classification by Sylow 2-subgroups (Gorenstein–Walter, Brauer–Suzuki), Baer–Suzuki, Glauberman Z*, Brauer–Fowler, involution centralizers and 3-transpositions; generation questions go to Generation of groups and spectrum recognition to Group orders, element orders and spectra.

## Brauer–Fowler theorem

There is a function $f \colon \mathbb{N} \to \mathbb{N}$ such that
for every finite nonabelian simple group $G$ and every element $t \in G$ of order $2$, with
centralizer $C_G(t)$ in $G$, the order of $G$ satisfies $|G| \le f(|C_G(t)|)$.

## Sources

- R. Brauer and K. A. Fowler, On groups of even order, Ann. of Math. (2) 62 (1955), 565-583. https://doi.org/10.2307/1970080. Problem `brauer_fowler` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.BrauerFowlerWanted.GroupTheory.brauer_fowler` is written with `theorem_wanted` in [WantedExt/GroupTheory/BrauerFowlerWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BrauerFowlerWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-simple-groups/index.html#brauer-fowler).

## Gorenstein–Walter theorem

Let $G$ be a finite nonabelian simple group, and let $P$ be a
Sylow $2$-subgroup of $G$ that is isomorphic to the dihedral group $D_n$ for some natural number
$n$ (of order $2n$ when $n \ge 1$; $D_0$ is the infinite dihedral group). Then $G$ is isomorphic
to the alternating group $A_7$, or to the projective special linear group
$\mathrm{PSL}_2(\mathbb{F}_q)$ for some power $q = p^k$ of an odd prime $p$ with $q \ge 5$.

## Sources

- D. Gorenstein and J. H. Walter, The characterization of finite groups with dihedral Sylow 2-subgroups, J. Algebra 2 (1965), 85-151, 218-270, 354-393. https://doi.org/10.1016/0021-8693(65)90027-X. Problem `gorenstein_walter` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.GorensteinWalterWanted.GroupTheory.gorenstein_walter` is written with `theorem_wanted` in [WantedExt/GroupTheory/GorensteinWalterWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/GorensteinWalterWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-simple-groups/index.html#gorenstein-walter).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite simple groups and involutions](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-simple-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/finite-simple-groups)
