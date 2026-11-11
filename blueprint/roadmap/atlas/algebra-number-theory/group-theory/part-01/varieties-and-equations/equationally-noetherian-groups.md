---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FreeProductEquationallyNoetherianKourovka14Problem20Wanted.evalEquation, MathlibExt.GroupTheory.FreeProductEquationallyNoetherianKourovka14Problem20Wanted.solutions, MathlibExt.GroupTheory.FreeProductEquationallyNoetherianKourovka14Problem20Wanted.EquationallyNoetherian, MathlibExt.GroupTheory.FreeProductEquationallyNoetherianKourovka14Problem20Wanted.freeProductEquationallyNoetherian, MathlibExt.GroupTheory.FreeProductEquationallyNoetherianKourovka14Problem20Wanted.freeProductEquationallyNoetherian_holds, MathlibExt.GroupTheory.HyperbolicEquationallyNoetherianKourovka14Problem19Wanted.evalEquation, MathlibExt.GroupTheory.HyperbolicEquationallyNoetherianKourovka14Problem19Wanted.solutions, MathlibExt.GroupTheory.HyperbolicEquationallyNoetherianKourovka14Problem19Wanted.EquationallyNoetherian
statement: formalized
---

# Equationally Noetherian groups

10 results, 8 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/equationally-noetherian-groups/index.html).

## Evaluation of an equation at an assignment (Kourovka 14.20)

For a group $G$, let $F_n$ be
the free group on the unknowns $t_0, \dots, t_{n-1}$. For an assignment
$x = (x_0, \dots, x_{n-1}) \in G^n$, evaluation at $x$ is the group homomorphism $G * F_n \to G$
from the free product of $G$ and $F_n$ that is the identity on $G$ and sends $t_i$ to $x_i$ for
each $i < n$; it sends an equation $w \in G * F_n$ over $G$ to its value $w(x)$ at $x$.

Formalized by `MathlibExt.GroupTheory.FreeProductEquationallyNoetherianKourovka14Problem20Wanted.evalEquation`, a definition declared in [WantedExt/GroupTheory/FreeProductEquationallyNoetherianKourovka14Problem20Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FreeProductEquationallyNoetherianKourovka14Problem20Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/equationally-noetherian-groups/index.html#eval-equation).

## Solution set of a system of equations (Kourovka 14.20)

For a group $G$, let $F_n$ be the
free group on the unknowns $t_0, \dots, t_{n-1}$. The solution set of a set $S \subseteq G * F_n$
of equations over $G$ is the set of assignments $x = (x_0, \dots, x_{n-1}) \in G^n$ such that
$w(x) = 1$ for every $w \in S$, where $w(x)$ is the image of $w$ under the homomorphism
$G * F_n \to G$ that is the identity on $G$ and sends $t_i$ to $x_i$.

Formalized by `MathlibExt.GroupTheory.FreeProductEquationallyNoetherianKourovka14Problem20Wanted.solutions`, a definition declared in [WantedExt/GroupTheory/FreeProductEquationallyNoetherianKourovka14Problem20Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FreeProductEquationallyNoetherianKourovka14Problem20Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/equationally-noetherian-groups/index.html#solutions).

## Equationally Noetherian groups (Kourovka 14.20)

A group $G$ is equationally Noetherian
(has the Noetherian Equation Property) if for every $n \in \mathbb{N}$ and every set $S$ of
equations over $G$ in the unknowns $t_0, \dots, t_{n-1}$, that is, every subset $S$ of the free
product $G * F_n$ of $G$ with the free group $F_n$ on $t_0, \dots, t_{n-1}$, there is a finite
subset $S_0 \subseteq S$ with the same solution set as $S$. Here the solution set of a set of
equations is the set of assignments $x = (x_0, \dots, x_{n-1}) \in G^n$ at which every equation in
it evaluates to $1$.

Formalized by `MathlibExt.GroupTheory.FreeProductEquationallyNoetherianKourovka14Problem20Wanted.EquationallyNoetherian`, a definition declared in [WantedExt/GroupTheory/FreeProductEquationallyNoetherianKourovka14Problem20Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FreeProductEquationallyNoetherianKourovka14Problem20Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/equationally-noetherian-groups/index.html#equationally-noetherian).

## Kourovka Problem 14.20 (free products of equationally Noetherian groups)

The statement
that for all groups $G$ and $H$, if $G$ and $H$ are equationally Noetherian (have the Noetherian
Equation Property), then their free product $G * H$ is equationally Noetherian.

Kourovka Notebook Problem 14.20 is due to G. Baumslag, A. G. Myasnikov and V. N. Remeslennikov.

Formalized by `MathlibExt.GroupTheory.FreeProductEquationallyNoetherianKourovka14Problem20Wanted.freeProductEquationallyNoetherian`, a definition declared in [WantedExt/GroupTheory/FreeProductEquationallyNoetherianKourovka14Problem20Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FreeProductEquationallyNoetherianKourovka14Problem20Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/equationally-noetherian-groups/index.html#free-product-equationally-noetherian).

## Free products of equationally Noetherian groups are equationally Noetherian

Resolved true: the Kourovka Notebook (21st issue) answers 14.20 "Yes, it does", citing Sela's
preprint (Theorem 9.1): the free product of two equationally Noetherian groups is equationally
Noetherian. Source: E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The
Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 14.20 (G. Baumslag, A. G.
Myasnikov, V. N. Remeslennikov); resolution: Z. Sela, Diophantine geometry over groups X: The
elementary theory of free products of groups, preprint, arXiv:1012.0044 (2010), Section 9, Theorem
9.1: the free product of two equationally Noetherian groups is equationally Noetherian; the Kourovka
Notebook (21st issue) marks 14.20 solved (Yes, it does), citing this preprint,
https://arxiv.org/abs/1012.0044.

Stated but not proved: `MathlibExt.GroupTheory.FreeProductEquationallyNoetherianKourovka14Problem20Wanted.freeProductEquationallyNoetherian_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/FreeProductEquationallyNoetherianKourovka14Problem20Wanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FreeProductEquationallyNoetherianKourovka14Problem20Wanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/equationally-noetherian-groups/index.html#free-product-equationally-noetherian-hol).

## Evaluating an equation at an assignment

Let $G$ be a group and $n$ a natural number. An
equation over $G$ in the unknowns $x_0, \dots, x_{n-1}$ is an element of the free product
$G * F(x_0, \dots, x_{n-1})$ of $G$ with the free group on $x_0, \dots, x_{n-1}$. For an assignment
$a = (a_0, \dots, a_{n-1}) \in G^n$, evaluation at $a$ is the group homomorphism
$G * F(x_0, \dots, x_{n-1}) \to G$ that is the identity on $G$ and sends each unknown $x_i$ to
$a_i$.

Formalized by `MathlibExt.GroupTheory.HyperbolicEquationallyNoetherianKourovka14Problem19Wanted.evalEquation`, a definition declared in [WantedExt/GroupTheory/HyperbolicEquationallyNoetherianKourovka14Problem19Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/HyperbolicEquationallyNoetherianKourovka14Problem19Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/equationally-noetherian-groups/index.html#eval-equation-2).

## Solution set of a system of equations

Let $G$ be a group, $n$ a natural number and $S$ a
set of equations over $G$ in the unknowns $x_0, \dots, x_{n-1}$, that is, a subset of the free
product $G * F(x_0, \dots, x_{n-1})$ of $G$ with the free group on $x_0, \dots, x_{n-1}$. The
solution set of $S$ is the set of assignments $a \in G^n$ at which every $w \in S$ evaluates to
$1$.

Formalized by `MathlibExt.GroupTheory.HyperbolicEquationallyNoetherianKourovka14Problem19Wanted.solutions`, a definition declared in [WantedExt/GroupTheory/HyperbolicEquationallyNoetherianKourovka14Problem19Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/HyperbolicEquationallyNoetherianKourovka14Problem19Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/equationally-noetherian-groups/index.html#solutions-2).

## The Noetherian Equation Property

A group $G$ has the Noetherian Equation Property (is
equationally Noetherian) if for every natural number $n$ and every system $S$ of equations over $G$
in the unknowns $x_0, \dots, x_{n-1}$, that is, every subset $S$ of the free product
$G * F(x_0, \dots, x_{n-1})$ of $G$ with the free group on $x_0, \dots, x_{n-1}$, there is a
finite subset $S_0 \subseteq S$ whose solution set in $G^n$ equals the solution set of $S$.

Formalized by `MathlibExt.GroupTheory.HyperbolicEquationallyNoetherianKourovka14Problem19Wanted.EquationallyNoetherian`, a definition declared in [WantedExt/GroupTheory/HyperbolicEquationallyNoetherianKourovka14Problem19Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/HyperbolicEquationallyNoetherianKourovka14Problem19Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/equationally-noetherian-groups/index.html#equationally-noetherian-2).

## Kourovka Problem 14.19 (hyperbolic groups and the Noetherian Equation Property)

Every
word-hyperbolic group $G$ has the Noetherian Equation Property: for every natural number $n$, every
system of equations over $G$ in the unknowns $x_0, \dots, x_{n-1}$ has the same solution set in
$G^n$ as some finite subsystem.

The problem is due to G. Baumslag, A. G. Myasnikov and V. N. Remeslennikov.

Formalized by `MathlibExt.GroupTheory.HyperbolicEquationallyNoetherianKourovka14Problem19Wanted.hyperbolicGroupEquationallyNoetherian`, a definition declared in [WantedExt/GroupTheory/HyperbolicEquationallyNoetherianKourovka14Problem19Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/HyperbolicEquationallyNoetherianKourovka14Problem19Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/equationally-noetherian-groups/index.html#hyperbolic-group-equationally-noetherian).

## Hyperbolic groups are equationally Noetherian

Every word-hyperbolic group $G$ has the
Noetherian Equation Property: for every natural number $n$, every system of equations over $G$ in
the unknowns $x_0, \dots, x_{n-1}$ has the same solution set in $G^n$ as some finite subsystem.

This answers Kourovka Problem 14.19 ("Yes, it does"): Weidmann and Reinfeldt prove it for all
hyperbolic groups, and Sela had proved the torsion-free case.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 14.19 (G. Baumslag, A. G. Myasnikov, V. N. Remeslennikov); resolution: R. Weidmann and C. Reinfeldt, Ann. Math. Blaise Pascal 26 (2019), no. 2, 125-214, the Kourovka Notebook (21st issue) marks 14.19 solved (Yes); the torsion-free case is due to Z. Sela, Proc. London Math. Soc. 99 (2009), 217-273.

Stated but not proved: `MathlibExt.GroupTheory.HyperbolicEquationallyNoetherianKourovka14Problem19Wanted.hyperbolicGroupEquationallyNoetherian_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/HyperbolicEquationallyNoetherianKourovka14Problem19Wanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/HyperbolicEquationallyNoetherianKourovka14Problem19Wanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/equationally-noetherian-groups/index.html#hyperbolic-group-equationally-noetherian-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Equationally Noetherian groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/equationally-noetherian-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/varieties-and-equations/equationally-noetherian-groups)
