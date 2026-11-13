---
declaration: section
origin: cited
lean: MetaMathlibExt.mazur_torsion_ncard_le, MathlibExt.NumberTheory.MazurTorsionWanted.NumberTheory.MazurTorsion.IsInMazurClass, MathlibExt.NumberTheory.MazurTorsionWanted.NumberTheory.MazurTorsion.mazur_torsion
statement: formalized
---

# Mazur's torsion theorem

3 results, 1 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/mazur-s-torsion-theorem/index.html).

## Mazur's torsion theorem

Let $E$ be an elliptic curve over $\mathbb{Q}$. The torsion
subgroup of the group $E(\mathbb{Q})$ of rational points of $E$ is finite and has at most $16$
elements.

Only this bound is stated, not Mazur's full list of the fifteen possible torsion subgroups.

## Sources

- B. Mazur, *Modular curves and the Eisenstein ideal*, Publ. Math. IHÉS 47 (1977), 33–186, doi:10.1007/BF02684339, <https://www.numdam.org/item/?id=PMIHES_1977__47__33_0>.

Stated but not proved: `MetaMathlibExt.mazur_torsion_ncard_le` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/EllipticCurve/MazurTorsionBoundWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/EllipticCurve/MazurTorsionBoundWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/mazur-s-torsion-theorem/index.html#mazur-torsion-ncard-le).

## The Mazur class of abelian groups

An abelian group $T$ is in the Mazur class when it is
isomorphic to $\mathbb{Z}/n\mathbb{Z}$ for some $n \in \{1, 2, \ldots, 10, 12\}$, or to
$\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2m\mathbb{Z}$ for some $m \in \{1, 2, 3, 4\}$.

Formalized by `MathlibExt.NumberTheory.MazurTorsionWanted.NumberTheory.MazurTorsion.IsInMazurClass`, a definition declared in [WantedExt/NumberTheory/MazurTorsionWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MazurTorsionWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/mazur-s-torsion-theorem/index.html#is-in-mazur-class).

## Mazur's torsion theorem

Let $E$ be an elliptic curve over $\mathbb{Q}$, given by a
Weierstrass equation. The torsion subgroup of the group $E(\mathbb{Q})$ of rational points of $E$
is in the Mazur class: it is isomorphic to $\mathbb{Z}/n\mathbb{Z}$ for some
$n \in \{1, 2, \ldots, 10, 12\}$, or to $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2m\mathbb{Z}$ for
some $m \in \{1, 2, 3, 4\}$.

## Sources

- B. Mazur, *Modular curves and the Eisenstein ideal*, Publ. IHÉS 47 (1977). Knill, *Some fundamental theorems in mathematics*, §139. Problem `mazur_torsion` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.MazurTorsionWanted.NumberTheory.MazurTorsion.mazur_torsion` is written with `theorem_wanted` in [WantedExt/NumberTheory/MazurTorsionWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MazurTorsionWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/mazur-s-torsion-theorem/index.html#mazur-torsion).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mazur's torsion theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/mazur-s-torsion-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-geometry/mazur-s-torsion-theorem)
