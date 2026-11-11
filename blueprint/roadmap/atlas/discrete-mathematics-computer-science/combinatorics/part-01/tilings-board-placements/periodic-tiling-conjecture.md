---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.PeriodicTilingConjectureWanted.PeriodicTilingConjecture.IsTiling, MathlibExt.Combinatorics.PeriodicTilingConjectureWanted.PeriodicTilingConjecture.IsPeriodicTilingSet, MathlibExt.Combinatorics.PeriodicTilingConjectureWanted.PeriodicTilingConjecture.IsAperiodicTilingEquation, MathlibExt.Combinatorics.PeriodicTilingConjectureWanted.PeriodicTilingConjecture.theorem_1_4, MathlibExt.Combinatorics.PeriodicTilingConjectureWanted.PeriodicTilingConjecture.corollary_1_6, MathlibExt.Combinatorics.PeriodicTilingConjectureWanted.PeriodicTilingConjecture.IsContinuousTiling, MathlibExt.Combinatorics.PeriodicTilingConjectureWanted.PeriodicTilingConjecture.IsPeriodicContinuousTilingSet, MathlibExt.Combinatorics.PeriodicTilingConjectureWanted.PeriodicTilingConjecture.IsAperiodicContinuousTilingEquation
statement: formalized
---

# Periodic tiling conjecture

9 results, 6 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/periodic-tiling-conjecture/index.html).

## Tiling of an abelian group by translates

Let $G$ be an abelian group and let
$F, A \subseteq G$. Then $F$ tiles $G$ with tiling set $A$ if the map $A \times F \to G$,
$(a, f) \mapsto a + f$, is a bijection; equivalently, every element of $G$ lies in $a + F$ for
exactly one $a \in A$.

Formalized by `MathlibExt.Combinatorics.PeriodicTilingConjectureWanted.PeriodicTilingConjecture.IsTiling`, an abbreviation declared in [WantedExt/Combinatorics/PeriodicTilingConjectureWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PeriodicTilingConjectureWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/periodic-tiling-conjecture/index.html#is-tiling).

## Periodic tiling set

A subset $A$ of an abelian group $G$ is periodic if there exist a
subgroup $H$ of $G$ of finite index and a finite set $S \subseteq G$ such that $A = S + H$, that
is, $A$ is the union of finitely many cosets of $H$.

Formalized by `MathlibExt.Combinatorics.PeriodicTilingConjectureWanted.PeriodicTilingConjecture.IsPeriodicTilingSet`, a definition declared in [WantedExt/Combinatorics/PeriodicTilingConjectureWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PeriodicTilingConjectureWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/periodic-tiling-conjecture/index.html#is-periodic-tiling-set).

## Aperiodic tiling equation

Let $G$ be an abelian group. A set $F \subseteq G$ forms an
aperiodic tiling equation if $F$ tiles $G$ with some tiling set $A \subseteq G$, and no tiling
set $A \subseteq G$ with which $F$ tiles $G$ is periodic.

Formalized by `MathlibExt.Combinatorics.PeriodicTilingConjectureWanted.PeriodicTilingConjecture.IsAperiodicTilingEquation`, a structure declared in [WantedExt/Combinatorics/PeriodicTilingConjectureWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PeriodicTilingConjectureWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/periodic-tiling-conjecture/index.html#is-aperiodic-tiling-equation).

## Greenfeld–Tao counterexample to the periodic tiling conjecture

There exist a finite abelian
group $G_0$ and a finite non-empty set $F \subseteq \mathbb{Z}^2 \times G_0$ that forms an
aperiodic tiling equation in the group $\mathbb{Z}^2 \times G_0$.

## Sources

- R. Greenfeld and T. Tao, `A counterexample to the periodic tiling conjecture`, Annals of Math, 200 (1) 2024. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_periodic_tiling_conjecture` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.PeriodicTilingConjectureWanted.PeriodicTilingConjecture.theorem_1_4` is written with `theorem_wanted` in [WantedExt/Combinatorics/PeriodicTilingConjectureWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PeriodicTilingConjectureWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/periodic-tiling-conjecture/index.html#theorem-1-4).

## Aperiodic tiling equations in high-dimensional integer lattices

There is a natural number
$d_0$ such that for every natural number $d \ge d_0$ there exists a finite non-empty set
$F \subseteq \mathbb{Z}^d$ that forms an aperiodic tiling equation in $\mathbb{Z}^d$.

## Sources

- R. Greenfeld and T. Tao, `A counterexample to the periodic tiling conjecture`, Annals of Math, 200 (1) 2024. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_periodic_tiling_conjecture` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.PeriodicTilingConjectureWanted.PeriodicTilingConjecture.corollary_1_6` is written with `theorem_wanted` in [WantedExt/Combinatorics/PeriodicTilingConjectureWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PeriodicTilingConjectureWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/periodic-tiling-conjecture/index.html#corollary-1-6).

## Continuous tiling of Euclidean space

For $d \in \mathbb{N}$, a set
$\sigma \subseteq \mathbb{R}^d$ continuously tiles $\mathbb{R}^d$ with tiling set
$\Lambda \subseteq \mathbb{R}^d$ if for almost every $x \in \mathbb{R}^d$ (with respect to
Lebesgue measure) there is exactly one $v \in \Lambda$ with $x \in v + \sigma$.

Formalized by `MathlibExt.Combinatorics.PeriodicTilingConjectureWanted.PeriodicTilingConjecture.IsContinuousTiling`, a definition declared in [WantedExt/Combinatorics/PeriodicTilingConjectureWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PeriodicTilingConjectureWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/periodic-tiling-conjecture/index.html#is-continuous-tiling).

## Periodic continuous tiling set

For $d \in \mathbb{N}$, a set
$\Lambda \subseteq \mathbb{R}^d$ is periodic if there exist a lattice $L \subseteq \mathbb{R}^d$,
that is, a discrete additive subgroup that spans $\mathbb{R}^d$ over $\mathbb{R}$, and a finite
set $S \subseteq \mathbb{R}^d$ such that $\Lambda = S + L$, so that $\Lambda$ is the union of
finitely many cosets of $L$.

Formalized by `MathlibExt.Combinatorics.PeriodicTilingConjectureWanted.PeriodicTilingConjecture.IsPeriodicContinuousTilingSet`, a definition declared in [WantedExt/Combinatorics/PeriodicTilingConjectureWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PeriodicTilingConjectureWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/periodic-tiling-conjecture/index.html#is-periodic-continuous-tiling-set).

## Aperiodic continuous tiling equation

For $d \in \mathbb{N}$, a set
$\sigma \subseteq \mathbb{R}^d$ forms an aperiodic continuous tiling equation if $\sigma$
continuously tiles $\mathbb{R}^d$ with some tiling set $\Lambda \subseteq \mathbb{R}^d$, and no
tiling set $\Lambda$ with which $\sigma$ continuously tiles $\mathbb{R}^d$ is periodic.

Formalized by `MathlibExt.Combinatorics.PeriodicTilingConjectureWanted.PeriodicTilingConjecture.IsAperiodicContinuousTilingEquation`, a structure declared in [WantedExt/Combinatorics/PeriodicTilingConjectureWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PeriodicTilingConjectureWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/periodic-tiling-conjecture/index.html#is-aperiodic-continuous-tiling-equation).

## Aperiodic continuous tiling equations in high-dimensional Euclidean space

There is a natural
number $d_0$ such that for every natural number $d \ge d_0$ there exists a bounded measurable set
$\sigma \subseteq \mathbb{R}^d$ of positive Lebesgue measure that forms an aperiodic continuous
tiling equation.

## Sources

- R. Greenfeld and T. Tao, `A counterexample to the periodic tiling conjecture`, Annals of Math, 200 (1) 2024. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_periodic_tiling_conjecture` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.PeriodicTilingConjectureWanted.PeriodicTilingConjecture.corollary_1_7` is written with `theorem_wanted` in [WantedExt/Combinatorics/PeriodicTilingConjectureWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PeriodicTilingConjectureWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/periodic-tiling-conjecture/index.html#corollary-1-7).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Periodic tiling conjecture](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/periodic-tiling-conjecture/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/tilings-board-placements/periodic-tiling-conjecture)
