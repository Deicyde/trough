---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.AutFnAutomaticQuestion73Wanted.IsAutomaticGroup, MathlibExt.GroupTheory.AutFnAutomaticQuestion73Wanted.conjecture, MathlibExt.GroupTheory.AutFnAutomaticQuestion73Wanted.conjecture_refuted
statement: formalized
---

# Automaticity of automorphism groups of free groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/automaticity-of-automorphism-groups-of-free-grou/index.html).

## Automatic group

A group $G$ is automatic if there are a finite alphabet $A$, an
involution $\iota$ of $A$, a map $\mathrm{ev} \colon A \to G$ with
$\mathrm{ev}(\iota(a)) = \mathrm{ev}(a)^{-1}$ for all $a \in A$, a language $L$ of words over $A$
that is exactly the set of words accepted by some deterministic finite automaton, and a natural
number $k$ with the following properties. Write $\overline{w} \in G$ for the product of the
images under $\mathrm{ev}$ of the letters of a word $w$, and $w(t)$ for the prefix of $w$ of
length $t$ (all of $w$ if $t$ exceeds its length). Every element of $G$ equals $\overline{w}$ for
some $w \in L$. For all $u, v \in L$ such that $\overline{u} = \overline{v}$, or
$\overline{u}\,\mathrm{ev}(a) = \overline{v}$ for some letter $a$, and for every $t \in \mathbb{N}$,
the element $\overline{u(t)}^{-1}\,\overline{v(t)}$ equals $\overline{w}$ for some word $w$ of
length at most $k$.

This is the fellow-traveller characterization of automatic groups (Epstein et al., Word
Processing in Groups, Theorem 2.3.5).

## Sources

- Question 7.3 [AMR-109-0302], Farb - Problems on Mapping Class Groups and Related Topics, PDF p. 339, https://www.math.uchicago.edu/~farb/papers/mcgbook.pdf.

Formalized by `MathlibExt.GroupTheory.AutFnAutomaticQuestion73Wanted.IsAutomaticGroup`, a definition declared in [WantedExt/GroupTheory/AutFnAutomaticQuestion73Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AutFnAutomaticQuestion73Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/automaticity-of-automorphism-groups-of-free-grou/index.html#is-automatic-group).

## Automaticity of automorphism groups of free groups (Farb's Question 7.3)

The statement
that for every natural number $n > 3$ the automorphism group $\mathrm{Aut}(F_n)$ of the free group
$F_n$ on $n$ generators is an automatic group.

## Sources

- Question 7.3 [AMR-109-0302], Farb - Problems on Mapping Class Groups and Related Topics, PDF p. 339, https://www.math.uchicago.edu/~farb/papers/mcgbook.pdf.

Formalized by `MathlibExt.GroupTheory.AutFnAutomaticQuestion73Wanted.conjecture`, a definition declared in [WantedExt/GroupTheory/AutFnAutomaticQuestion73Wanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AutFnAutomaticQuestion73Wanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/automaticity-of-automorphism-groups-of-free-grou/index.html#conjecture).

## Negative answer to Farb's Question 7.3

It is not the case that for every natural number
$n > 3$ the automorphism group $\mathrm{Aut}(F_n)$ of the free group on $n$ generators is
automatic.

Bridson and Vogtmann, with Handel and Mosher, proved more: $\mathrm{Aut}(F_n)$ has exponential
Dehn function for every $n \ge 3$, while automatic groups have at most quadratic Dehn functions
(Epstein et al.), so $\mathrm{Aut}(F_n)$ is automatic for no $n \ge 3$.

## Sources

- M. R. Bridson, K. Vogtmann, The Dehn functions of Out(F_n) and Aut(F_n), Annales de l'Institut Fourier 62(5) (2012) 1811-1817, arXiv:1011.1506, https://arxiv.org/abs/1011.1506.

Stated but not proved: `MathlibExt.GroupTheory.AutFnAutomaticQuestion73Wanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/AutFnAutomaticQuestion73Wanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AutFnAutomaticQuestion73Wanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/automaticity-of-automorphism-groups-of-free-grou/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Automaticity of automorphism groups of free groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/automaticity-of-automorphism-groups-of-free-grou/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/automaticity-of-automorphism-groups-of-free-grou)
