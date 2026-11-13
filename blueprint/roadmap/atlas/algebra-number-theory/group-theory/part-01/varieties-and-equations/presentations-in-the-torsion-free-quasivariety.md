---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.TorsionFreeQuasivarietyPresentationKourovka18Problem17Wanted.torsionFreeRelations, MathlibExt.GroupTheory.TorsionFreeQuasivarietyPresentationKourovka18Problem17Wanted.IsTorsionFreeFinitelyPresented, MathlibExt.GroupTheory.TorsionFreeQuasivarietyPresentationKourovka18Problem17Wanted.torsionFreePresentedNotFinitelyPresented, MathlibExt.GroupTheory.TorsionFreeQuasivarietyPresentationKourovka18Problem17Wanted.torsionFreePresentedNotFinitelyPresented_holds
statement: formalized
---

# Presentations in the torsion-free quasivariety

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/presentations-in-the-torsion-free-quasivariety/index.html).

## Relation subgroup of a torsion-free presentation

Let $n$ be a natural number, let $F_n$ be
the free group on the $n$ letters $0, 1, \dots, n - 1$, and let $S$ be a subset of $F_n$. The
relation subgroup of $S$ in the quasivariety of torsion-free groups is the intersection of all
normal subgroups $N$ of $F_n$ that contain $S$ and satisfy the following: for every $x \in F_n$
and every integer $k \ge 1$, if $x^k \in N$ then $x \in N$. Equivalently, it is the least normal
subgroup $N$ of $F_n$ containing $S$ for which $F_n / N$ is torsion-free.

Formalized by `MathlibExt.GroupTheory.TorsionFreeQuasivarietyPresentationKourovka18Problem17Wanted.torsionFreeRelations`, a definition declared in [WantedExt/GroupTheory/TorsionFreeQuasivarietyPresentationKourovka18Problem17Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/TorsionFreeQuasivarietyPresentationKourovka18Problem17Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/presentations-in-the-torsion-free-quasivariety/index.html#torsion-free-relations).

## Groups finitely presented in the torsion-free quasivariety

A group $G$ is finitely
presented in the quasivariety of torsion-free groups if there are a natural number $n$, a finite
subset $S$ of the free group $F_n$ on $n$ letters, and a surjective homomorphism
$f \colon F_n \to G$ whose kernel is the relation subgroup of $S$ in the quasivariety of
torsion-free groups.

Formalized by `MathlibExt.GroupTheory.TorsionFreeQuasivarietyPresentationKourovka18Problem17Wanted.IsTorsionFreeFinitelyPresented`, a definition declared in [WantedExt/GroupTheory/TorsionFreeQuasivarietyPresentationKourovka18Problem17Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/TorsionFreeQuasivarietyPresentationKourovka18Problem17Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/presentations-in-the-torsion-free-quasivariety/index.html#is-torsion-free-finitely-presented).

## Kourovka Problem 18.17 (statement)

The statement that there is a torsion-free group $G$ (no
element of $G$ other than the identity has finite order) that is finitely presented in the
quasivariety of torsion-free groups but is not a finitely presented group.

The problem was posed by O. V. Belegradek.

Formalized by `MathlibExt.GroupTheory.TorsionFreeQuasivarietyPresentationKourovka18Problem17Wanted.torsionFreePresentedNotFinitelyPresented`, a definition declared in [WantedExt/GroupTheory/TorsionFreeQuasivarietyPresentationKourovka18Problem17Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/TorsionFreeQuasivarietyPresentationKourovka18Problem17Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/presentations-in-the-torsion-free-quasivariety/index.html#torsion-free-presented-not-finitely-pres).

## Budkin's theorem (Kourovka Problem 18.17)

There is a torsion-free group $G$ (no element of $G$
other than the identity has finite order) that is finitely presented in the quasivariety of
torsion-free groups but is not a finitely presented group.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 18.17 (O. V. Belegradek); resolution: A. I. Budkin, Siberian Electron. Math. Rep. 14 (2017), 937-945, Kourovka Archive, Problem 18.17: Yes, there is, http://semr.math.nsc.ru.

Stated but not proved: `MathlibExt.GroupTheory.TorsionFreeQuasivarietyPresentationKourovka18Problem17Wanted.torsionFreePresentedNotFinitelyPresented_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/TorsionFreeQuasivarietyPresentationKourovka18Problem17Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/TorsionFreeQuasivarietyPresentationKourovka18Problem17Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/presentations-in-the-torsion-free-quasivariety/index.html#torsion-free-presented-not-finitely-pres-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Presentations in the torsion-free quasivariety](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/presentations-in-the-torsion-free-quasivariety/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/varieties-and-equations/presentations-in-the-torsion-free-quasivariety)
