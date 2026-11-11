---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.Word, MathlibExt.GroupTheory.TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.evalWord, MathlibExt.GroupTheory.TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.CNF, MathlibExt.GroupTheory.TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.CNF.HoldsAt, MathlibExt.GroupTheory.TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.realizePrenex, MathlibExt.GroupTheory.TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.PrenexSentence, MathlibExt.GroupTheory.TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.PrenexSentence.HoldsIn, MathlibExt.GroupTheory.TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.torsionFreeHyperbolicTheoryDecidable
statement: formalized
---

# Elementary theory of torsion-free hyperbolic groups

9 results, 8 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/elementary-theory-of-torsion-free-hyperbolic-gro/index.html).

## Group words in countably many variables

A group word in the variables $x_0, x_1, \dots$ is
coded as a finite list of letters $(i, b)$, where $i$ is a natural number and $b$ is a Boolean: the
letter $(i, \mathrm{true})$ stands for $x_i$ and the letter $(i, \mathrm{false})$ for $x_i^{-1}$.
The word is read as the product of its letters in order, an element of the free group on
$x_0, x_1, \dots$.

Formalized by `MathlibExt.GroupTheory.TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.Word`, an abbreviation declared in [WantedExt/GroupTheory/TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/elementary-theory-of-torsion-free-hyperbolic-gro/index.html#word).

## Value of a group word

Let $G$ be a group and $a \colon \mathbb{N} \to G$ an assignment of
values to the variables $x_0, x_1, \dots$. The value of a group word $w$ under $a$ is the product in
$G$, in the order of the letters of $w$, of $a(i)$ for each letter $x_i$ and of $a(i)^{-1}$ for
each letter $x_i^{-1}$; equivalently, it is the image of $w$ under the homomorphism from the free
group on $x_0, x_1, \dots$ to $G$ that sends $x_i$ to $a(i)$.

Formalized by `MathlibExt.GroupTheory.TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.evalWord`, a definition declared in [WantedExt/GroupTheory/TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/elementary-theory-of-torsion-free-hyperbolic-gro/index.html#eval-word).

## Quantifier-free formulas in conjunctive normal form

A quantifier-free formula of the
language of groups in conjunctive normal form is coded as a finite list of clauses, each clause a
finite list of literals. A literal is a pair $(b, w)$ of a Boolean $b$ and a group word $w$; it
stands for the equation $w = 1$ when $b$ is true and for the inequation $w \ne 1$ when $b$ is
false. The formula is the conjunction of its clauses, and each clause is the disjunction of its
literals.

Formalized by `MathlibExt.GroupTheory.TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.CNF`, an abbreviation declared in [WantedExt/GroupTheory/TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/elementary-theory-of-torsion-free-hyperbolic-gro/index.html#cnf).

## Truth of a formula in conjunctive normal form

Let $G$ be a group, let
$a \colon \mathbb{N} \to G$ assign values to the variables $x_0, x_1, \dots$, and let $\varphi$ be
a quantifier-free formula in conjunctive normal form. Then $\varphi$ holds in $G$ under $a$ when
every clause of $\varphi$ contains a literal $(b, w)$ such that the value of $w$ under $a$ equals
$1$ if and only if $b$ is true, that is, a literal $w = 1$ whose word has value $1$ or a literal
$w \ne 1$ whose word does not.

Formalized by `MathlibExt.GroupTheory.TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.CNF.HoldsAt`, a definition declared in [WantedExt/GroupTheory/TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/elementary-theory-of-torsion-free-hyperbolic-gro/index.html#holds-at).

## Truth of a prenex formula

Let $G$ be a group, $\varphi$ a quantifier-free formula in
conjunctive normal form, $q$ a finite list of Booleans read as a quantifier prefix ($\mathrm{true}$
for $\forall$, $\mathrm{false}$ for $\exists$), $i$ a natural number and $a \colon \mathbb{N} \to G$
an assignment of values to the variables $x_0, x_1, \dots$. Truth in $G$ under $a$ of the formula
with prefix $q$, whose first quantifier binds $x_i$, and matrix $\varphi$ is defined by recursion
on $q$. For the empty prefix it is truth of $\varphi$ in $G$ under $a$. For a prefix $\forall$
followed by $q'$, it holds when for every $g \in G$ the formula with prefix $q'$, whose first
quantifier binds $x_{i+1}$, holds under the assignment that agrees with $a$ except that $x_i$ takes
the value $g$; for a prefix $\exists$ followed by $q'$, the same holds for some $g \in G$. Thus the
quantifiers of $q$ bind $x_i, x_{i+1}, \dots$ in order, and the other variables keep their values
under $a$.

Formalized by `MathlibExt.GroupTheory.TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.realizePrenex`, a definition declared in [WantedExt/GroupTheory/TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/elementary-theory-of-torsion-free-hyperbolic-gro/index.html#realize-prenex).

## Prenex sentences of the language of groups

A sentence of the language of groups in prenex
form with matrix in conjunctive normal form is coded as a pair $(q, \varphi)$ of a finite list $q$
of Booleans, the quantifier prefix ($\mathrm{true}$ for $\forall$, $\mathrm{false}$ for $\exists$),
and a quantifier-free formula $\varphi$ in conjunctive normal form. The quantifiers of $q$ bind the
variables $x_0, x_1, \dots$ in order, and variables of $\varphi$ not bound by the prefix are read
as $1$.

Every first-order sentence of the language of groups is effectively equivalent to such a code, and
conversely.

Formalized by `MathlibExt.GroupTheory.TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.PrenexSentence`, an abbreviation declared in [WantedExt/GroupTheory/TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/elementary-theory-of-torsion-free-hyperbolic-gro/index.html#prenex-sentence).

## Truth of a prenex sentence in a group

A prenex sentence $(q, \varphi)$ holds in a group $G$
when the formula with quantifier prefix $q$ and matrix $\varphi$, whose quantifiers bind the
variables $x_0, x_1, \dots$ in order, is true in $G$ under the assignment that gives every variable
the value $1$; thus the variables not bound by $q$ are read as $1$.

Formalized by `MathlibExt.GroupTheory.TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.PrenexSentence.HoldsIn`, a definition declared in [WantedExt/GroupTheory/TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/elementary-theory-of-torsion-free-hyperbolic-gro/index.html#holds-in).

## Decidability of the elementary theory of torsion-free hyperbolic groups

The proposition
stating Kourovka Problem 16.71 (A. G. Myasnikov, O. G. Kharlampovich): for every torsion-free
word-hyperbolic group $G$ (every element $g \ne 1$ of $G$ has infinite order), the set of prenex
sentences of the language of groups that hold in $G$ is computable, that is, some algorithm
decides for each prenex sentence whether it holds in $G$.

Formalized by `MathlibExt.GroupTheory.TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.torsionFreeHyperbolicTheoryDecidable`, a definition declared in [WantedExt/GroupTheory/TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/elementary-theory-of-torsion-free-hyperbolic-gro/index.html#torsion-free-hyperbolic-theory-decidable).

## Torsion-free hyperbolic groups have decidable elementary theory

For every torsion-free
word-hyperbolic group $G$ (every element $g \ne 1$ of $G$ has infinite order), the set of prenex
sentences of the language of groups that hold in $G$ is computable, that is, some algorithm decides
for each prenex sentence whether it holds in $G$.

This answers Kourovka Problem 16.71 affirmatively (the Kourovka Archive answers "Yes, it is"); it
is Theorem 3 of Kharlampovich and Myasnikov.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.71 (A. G. Myasnikov, O. G. Kharlampovich); resolution: O. Kharlampovich and A. Myasnikov, Decidability of the elementary theory of a torsion-free hyperbolic group, arXiv:1303.0760, Theorem 3 (the elementary theory of a torsion-free hyperbolic group is decidable); Kourovka Archive, Problem 16.71 (Yes, it is), https://arxiv.org/abs/1303.0760.

Stated but not proved: `MathlibExt.GroupTheory.TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.torsionFreeHyperbolicTheoryDecidable_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TorsionFreeHyperbolicElementaryTheoryKourovka16Problem71Wanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/elementary-theory-of-torsion-free-hyperbolic-gro/index.html#torsion-free-hyperbolic-theory-decidable-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Elementary theory of torsion-free hyperbolic groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/elementary-theory-of-torsion-free-hyperbolic-gro/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/varieties-and-equations/elementary-theory-of-torsion-free-hyperbolic-gro)
