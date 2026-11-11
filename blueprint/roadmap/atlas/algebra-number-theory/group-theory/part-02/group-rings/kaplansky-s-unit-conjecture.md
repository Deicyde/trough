---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.generators, MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.a, MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.b, MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.relations, MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.P, MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.x, MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.y, MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.z
statement: formalized
---

# Kaplansky's unit conjecture

15 results, 14 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/kaplansky-s-unit-conjecture/index.html).

## Generators of Gardam's presentation

This is the two-element set consisting of the
distinct formal symbols $a$ and $b$, which serve as the generators of the group presentation in
Theorem A of Gardam's counterexample to the unit conjecture.

Formalized by `MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.generators`, an inductive type declared in [WantedExt/GroupTheory/UnitConjectureWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UnitConjectureWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/kaplansky-s-unit-conjecture/index.html#generators).

## First free generator of Gardam's presentation

$a$ is the generator $a$, viewed as an
element of the free group on the two generators $a$ and $b$.

Formalized by `MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.a`, a definition declared in [WantedExt/GroupTheory/UnitConjectureWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UnitConjectureWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/kaplansky-s-unit-conjecture/index.html#a).

## Second free generator of Gardam's presentation

$b$ is the generator $b$, viewed as an
element of the free group on the two generators $a$ and $b$.

Formalized by `MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.b`, a definition declared in [WantedExt/GroupTheory/UnitConjectureWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UnitConjectureWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/kaplansky-s-unit-conjecture/index.html#b).

## Relators of Gardam's group

In the free group on the generators $a$ and $b$, the relators
are the two elements $b^{-1}a^2ba^2$ and $a^{-1}b^2ab^2$.

Imposing them gives the relations $b^{-1}a^2b = a^{-2}$ and $a^{-1}b^2a = b^{-2}$ of Theorem A of
Gardam's counterexample to the unit conjecture.

Formalized by `MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.relations`, a definition declared in [WantedExt/GroupTheory/UnitConjectureWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UnitConjectureWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/kaplansky-s-unit-conjecture/index.html#relations).

## Gardam's group

$P$ is the group with generators $a$ and $b$ and relators
$b^{-1}a^2ba^2$ and $a^{-1}b^2ab^2$, that is,
$P = \langle a, b \mid b^{-1}a^2b = a^{-2}, a^{-1}b^2a = b^{-2} \rangle$.

This is the group of Theorem A of Gardam's counterexample to the unit conjecture.

Formalized by `MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.P`, a definition declared in [WantedExt/GroupTheory/UnitConjectureWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UnitConjectureWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/kaplansky-s-unit-conjecture/index.html#p).

## The element x of Gardam's group

In the group $P$ with presentation
$\langle a, b \mid b^{-1}a^2b = a^{-2},\ a^{-1}b^2a = b^{-2} \rangle$, $x = a^2$.

Formalized by `MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.x`, a definition declared in [WantedExt/GroupTheory/UnitConjectureWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UnitConjectureWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/kaplansky-s-unit-conjecture/index.html#x).

## The element y of Gardam's group

In the group $P$ with presentation
$\langle a, b \mid b^{-1}a^2b = a^{-2},\ a^{-1}b^2a = b^{-2} \rangle$, $y = b^2$.

Formalized by `MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.y`, a definition declared in [WantedExt/GroupTheory/UnitConjectureWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UnitConjectureWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/kaplansky-s-unit-conjecture/index.html#y).

## The element z of Gardam's group

In the group $P$ with presentation
$\langle a, b \mid b^{-1}a^2b = a^{-2},\ a^{-1}b^2a = b^{-2} \rangle$, $z = (ab)^2$.

Formalized by `MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.z`, a definition declared in [WantedExt/GroupTheory/UnitConjectureWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UnitConjectureWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/kaplansky-s-unit-conjecture/index.html#z).

## Group ring of Gardam's group over the field with two elements

$\mathbb{F}_2[P]$ is the
group ring of Gardam's group $P$ over the field $\mathbb{F}_2 = \mathbb{Z}/2\mathbb{Z}$.

Formalized by `MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.R`, an abbreviation declared in [WantedExt/GroupTheory/UnitConjectureWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UnitConjectureWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/kaplansky-s-unit-conjecture/index.html#r).

## Gardam's element p

In the group ring $\mathbb{F}_2[P]$ of Gardam's group $P$ with
generators $a$ and $b$, let $x = a^2$, $y = b^2$ and $z = (ab)^2$ in $P$, viewed as elements of
$\mathbb{F}_2[P]$. Then $p$ is the element $(1 + x)(1 + y)(1 + z^{-1})$ of $\mathbb{F}_2[P]$.

Formalized by `MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.p`, a definition declared in [WantedExt/GroupTheory/UnitConjectureWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UnitConjectureWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/kaplansky-s-unit-conjecture/index.html#p-2).

## Gardam's element q

In the group ring $\mathbb{F}_2[P]$ of Gardam's group $P$ with
generators $a$ and $b$, let $x = a^2$, $y = b^2$ and $z = (ab)^2$ in $P$, viewed as elements of
$\mathbb{F}_2[P]$. Then $q$ is the element $x^{-1}y^{-1} + x + y^{-1}z + z$ of $\mathbb{F}_2[P]$.

Formalized by `MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.q`, a definition declared in [WantedExt/GroupTheory/UnitConjectureWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UnitConjectureWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/kaplansky-s-unit-conjecture/index.html#q).

## Gardam's element r

In the group ring $\mathbb{F}_2[P]$ of Gardam's group $P$ with
generators $a$ and $b$, let $x = a^2$, $y = b^2$ and $z = (ab)^2$ in $P$, viewed as elements of
$\mathbb{F}_2[P]$. Then $r$ is the element $1 + x + y^{-1}z + xyz$ of $\mathbb{F}_2[P]$.

Formalized by `MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.r`, a definition declared in [WantedExt/GroupTheory/UnitConjectureWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UnitConjectureWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/kaplansky-s-unit-conjecture/index.html#r-2).

## Gardam's element s

In the group ring $\mathbb{F}_2[P]$ of Gardam's group $P$ with
generators $a$ and $b$, let $x = a^2$, $y = b^2$ and $z = (ab)^2$ in $P$, viewed as elements of
$\mathbb{F}_2[P]$. Then $s$ is the element $1 + (x + x^{-1} + y + y^{-1})z^{-1}$ of
$\mathbb{F}_2[P]$.

Formalized by `MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.s`, a definition declared in [WantedExt/GroupTheory/UnitConjectureWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UnitConjectureWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/kaplansky-s-unit-conjecture/index.html#s).

## Gardam's unit

Let $P$ be the group with presentation
$\langle a, b \mid b^{-1}a^2b = a^{-2},\ a^{-1}b^2a = b^{-2} \rangle$ and set $x = a^2$,
$y = b^2$, $z = (ab)^2$. In the group ring $\mathbb{F}_2[P]$, $u = p + qa + rb + sab$, where
$p = (1 + x)(1 + y)(1 + z^{-1})$, $q = x^{-1}y^{-1} + x + y^{-1}z + z$,
$r = 1 + x + y^{-1}z + xyz$ and $s = 1 + (x + x^{-1} + y + y^{-1})z^{-1}$.

Formalized by `MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.u`, a definition declared in [WantedExt/GroupTheory/UnitConjectureWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UnitConjectureWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/kaplansky-s-unit-conjecture/index.html#u).

## Gardam's counterexample to the unit conjecture

Let $P$ be the group with presentation
$\langle a, b \mid b^{-1}a^2b = a^{-2},\ a^{-1}b^2a = b^{-2} \rangle$, and set $x = a^2$,
$y = b^2$ and $z = (ab)^2$. In the group ring $\mathbb{F}_2[P]$ set
$p = (1 + x)(1 + y)(1 + z^{-1})$, $q = x^{-1}y^{-1} + x + y^{-1}z + z$,
$r = 1 + x + y^{-1}z + xyz$ and $s = 1 + (x + x^{-1} + y + y^{-1})z^{-1}$, and let
$u = p + qa + rb + sab$. Then $P$ is torsion-free (if $g \in P$ and $g^n = 1$ for some
natural number $n \neq 0$, then $g = 1$), $u$ is a unit of $\mathbb{F}_2[P]$, and $u$ is not
equal to any element $g$ of $P$ viewed in $\mathbb{F}_2[P]$; that is, $u$ is a non-trivial unit.

## Sources

- G. Gardam, `A counterexample to the unit conjecture for group rings`, Annals of Math, 194 (3) 2021. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_unit_conjecture` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.UnitConjectureWanted.UnitConjecture.theorem_A` is written with `theorem_wanted` in [WantedExt/GroupTheory/UnitConjectureWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UnitConjectureWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/kaplansky-s-unit-conjecture/index.html#theorem-a).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kaplansky's unit conjecture](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/kaplansky-s-unit-conjecture/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/group-rings/kaplansky-s-unit-conjecture)
