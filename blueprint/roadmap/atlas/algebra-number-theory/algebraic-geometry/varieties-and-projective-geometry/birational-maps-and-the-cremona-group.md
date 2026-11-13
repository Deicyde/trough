---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.BirationalMap, AlgebraicGeometry.Scheme.BirationalMap.refl, AlgebraicGeometry.Scheme.BirationalMap.symm, AlgebraicGeometry.Scheme.BirationalMap.trans, AlgebraicGeometry.Scheme.BirationalMap.IsOver, AlgebraicGeometry.Scheme.birationalAutOver, AlgebraicGeometry.Scheme.PartialIso.toBirationalMap, MathlibExt.AlgebraicGeometry.MotivicInvariantsWanted.MotivicInvariants.Variety
statement: formalized
---

# Birational maps and the Cremona group

19 results, 13 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group/index.html).

## Scheme

## Birational map

Let $X$ and $Y$ be irreducible schemes. A birational map from $X$ to $Y$
consists of dominant rational maps $f \colon X \dashrightarrow Y$ and
$g \colon Y \dashrightarrow X$ that are mutually inverse: $g \circ f$ is the identity rational
map of $X$ and $f \circ g$ is the identity rational map of $Y$.

Formalized by `AlgebraicGeometry.Scheme.BirationalMap`, a structure declared in [WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group/index.html#birational-map).

## Identity birational map

For an irreducible scheme $X$, the identity birational map of
$X$ has the identity rational map of $X$ as both its forward and its inverse map.

Formalized by `AlgebraicGeometry.Scheme.BirationalMap.refl`, a definition declared in [WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group/index.html#refl).

## Inverse birational map

Let $X$ and $Y$ be irreducible schemes. The inverse of a
birational map from $X$ to $Y$ is the birational map from $Y$ to $X$ whose forward map is the
inverse rational map of the original and whose inverse map is its forward rational map.

Formalized by `AlgebraicGeometry.Scheme.BirationalMap.symm`, a definition declared in [WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group/index.html#symm).

## Composition of birational maps

Let $X$, $Y$ and $Z$ be irreducible schemes, let $f$ be a
birational map from $X$ to $Y$ and let $g$ be a birational map from $Y$ to $Z$. The composite of
$f$ and $g$ is the birational map from $X$ to $Z$ whose forward rational map is the forward map of
$f$ followed by the forward map of $g$, and whose inverse rational map is the inverse of $g$
followed by the inverse of $f$.

Formalized by `AlgebraicGeometry.Scheme.BirationalMap.trans`, a definition declared in [WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group/index.html#trans).

## Birational maps over a base

Let $X$ and $Y$ be irreducible schemes over a scheme $S$.
A birational map from $X$ to $Y$ is over $S$ when its forward rational map
$X \dashrightarrow Y$ is compatible with the structure maps to $S$.

Its inverse rational map is then compatible with the structure maps to $S$ as well.

Formalized by `AlgebraicGeometry.Scheme.BirationalMap.IsOver`, an abbreviation declared in [WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group/index.html#is-over).

## Birational automorphisms over a base

Let $X$ be an irreducible scheme over a scheme
$S$. The birational automorphisms of $X$ over $S$ form the subgroup of the group of birational
self-maps of $X$ consisting of those birational maps whose forward rational map
$X \dashrightarrow X$ is compatible with the structure maps to $S$.

Formalized by `AlgebraicGeometry.Scheme.birationalAutOver`, a definition declared in [WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group/index.html#birational-aut-over).

## Birational map of a partial isomorphism

Let $X$ and $Y$ be irreducible schemes and let
$f$ be a partial isomorphism from $X$ to $Y$, that is, an isomorphism from a dense open subscheme
of $X$ onto a dense open subscheme of $Y$. The birational map from $X$ to $Y$ given by $f$ has as
forward map the rational map $X \dashrightarrow Y$ represented by $f$, and as inverse the rational
map $Y \dashrightarrow X$ represented by the inverse of $f$.

Formalized by `AlgebraicGeometry.Scheme.PartialIso.toBirationalMap`, a definition declared in [WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group/index.html#to-birational-map).

## Integral variety over a field

Let $k$ be a field. A variety over $k$ in this sense is a
scheme $X$ together with a morphism $X \to \operatorname{Spec} k$ such that $X$ is integral
(irreducible and reduced) and the morphism is separated and of finite type (locally of finite type
and quasi-compact).

Formalized by `MathlibExt.AlgebraicGeometry.MotivicInvariantsWanted.MotivicInvariants.Variety`, a class declared in [WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group/index.html#variety).

## Pseudo-isomorphism

Let $X$ and $Y$ be schemes. A partial isomorphism from $X$ to $Y$,
that is, an isomorphism $U \cong V$ between dense open subschemes $U \subseteq X$ and
$V \subseteq Y$, is a pseudo-isomorphism if it is an isomorphism in codimension one: every
point of $X$ outside $U$ and every point of $Y$ outside $V$ has coheight at least $2$ in the
specialization order of points.

Formalized by `MathlibExt.AlgebraicGeometry.MotivicInvariantsWanted.MotivicInvariants.IsPseudoIso`, a structure declared in [WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group/index.html#is-pseudo-iso).

## Pseudo-regularization of a birational automorphism

Let $X$ be a variety over a field
$k$ and let $\varphi$ be a birational automorphism of $X$. A pseudo-regularization of $\varphi$
consists of a variety $X'$ over $k$, a birational map $\alpha \colon X \dashrightarrow X'$ over
$k$, and a partial isomorphism $\gamma$ from $X'$ to itself over $k$ that is a
pseudo-isomorphism, such that $\varphi = \alpha^{-1} \circ \gamma \circ \alpha$, where $\gamma$
is viewed as a birational map.

Formalized by `MathlibExt.AlgebraicGeometry.MotivicInvariantsWanted.MotivicInvariants.PseudoRegularization`, a structure declared in [WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group/index.html#pseudo-regularization).

## Pseudo-regularizable birational automorphism

Let $X$ be a variety over a field $k$. A
birational automorphism $\varphi$ of $X$ is pseudo-regularizable if there exist a variety $X'$
over $k$, a birational map $\alpha \colon X \dashrightarrow X'$ over $k$, and a partial
isomorphism $\gamma$ from $X'$ to itself over $k$ that is a pseudo-isomorphism (an isomorphism
in codimension one), such that $\varphi = \alpha^{-1} \circ \gamma \circ \alpha$, where $\gamma$
is viewed as a birational map. The variety $X'$ need not be smooth or projective.

## Sources

- H.-Y. Lin and E. Shinder, Motivic invariants of birational maps, Definition 4.1.

Formalized by `MathlibExt.AlgebraicGeometry.MotivicInvariantsWanted.MotivicInvariants.IsPseudoRegularizable`, an abbreviation declared in [WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group/index.html#is-pseudo-regularizable).

## Cremona group

For a field $k$ and $n \in \mathbb{N}$, the Cremona group
$\mathrm{Cr}_n(k)$ is the group of birational automorphisms of affine $n$-space
$\mathbb{A}^n_k$ over $\operatorname{Spec} k$.

Formalized by `MathlibExt.AlgebraicGeometry.MotivicInvariantsWanted.MotivicInvariants.Cr`, an abbreviation declared in [WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group/index.html#cr).

## Cremona group generated by pseudo-regularizable elements

For a field $k$ and
$n \in \mathbb{N}$, this is the proposition that the Cremona group $\mathrm{Cr}_n(k)$ is
generated, as a group, by its pseudo-regularizable elements.

Formalized by `MathlibExt.AlgebraicGeometry.MotivicInvariantsWanted.MotivicInvariants.GenByPseudoRegularizable`, an abbreviation declared in [WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group/index.html#gen-by-pseudo-regularizable).

## $\mathrm{Cr}_3$ of a number field is not generated by pseudo-regularizable elements

Let $k$
be a number field. The Cremona group $\mathrm{Cr}_3(k)$, the group of birational automorphisms of
affine $3$-space over $k$, is not generated by its pseudo-regularizable elements.

This is Theorem 1.2 (1) (a) of Lin and Shinder.

## Sources

- H.-Y. Lin and E. Shinder, `Motivic invariants of birational maps`, Annals of Math, 199 (1) 2024. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_motivic_invariants` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.MotivicInvariantsWanted.MotivicInvariants.theorem_1_2_1_a` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group/index.html#theorem-1-2-1-a).

## $\mathrm{Cr}_3$ of a function field over a number field is not generated by pseudo-regularizable elements

**$\mathrm{Cr}_3$ of a function field over a number field is not generated by pseudo-regularizable
elements.** Let $F$ be a number field and let $X$ be a variety over $F$ of positive dimension, with
function field $F(X)$. The Cremona group $\mathrm{Cr}_3(F(X))$, the group of birational
automorphisms of affine $3$-space over $F(X)$, is not generated by its pseudo-regularizable
elements.

This is Theorem 1.2 (1) (b) of Lin and Shinder.

## Sources

- H.-Y. Lin and E. Shinder, `Motivic invariants of birational maps`, Annals of Math, 199 (1) 2024. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_motivic_invariants` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.MotivicInvariantsWanted.MotivicInvariants.theorem_1_2_1_b` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group/index.html#theorem-1-2-1-b).

## $\mathrm{Cr}_3$ of a function field over a finite field is not generated by pseudo-regularizable elements

**$\mathrm{Cr}_3$ of a function field over a finite field is not generated by pseudo-regularizable
elements.** Let $F$ be a finite field and let $X$ be a variety over $F$ of positive dimension, with
function field $F(X)$. The Cremona group $\mathrm{Cr}_3(F(X))$, the group of birational
automorphisms of affine $3$-space over $F(X)$, is not generated by its pseudo-regularizable
elements.

This is Theorem 1.2 (1) (c) of Lin and Shinder.

## Sources

- H.-Y. Lin and E. Shinder, `Motivic invariants of birational maps`, Annals of Math, 199 (1) 2024. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_motivic_invariants` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.MotivicInvariantsWanted.MotivicInvariants.theorem_1_2_1_c` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group/index.html#theorem-1-2-1-c).

## $\mathrm{Cr}_3$ of a function field over an algebraically closed field is not generated by pseudo-regularizable elements

**$\mathrm{Cr}_3$ of a function field over an algebraically closed field is not generated by
pseudo-regularizable elements.** Let $F$ be an algebraically closed field and let $X$ be a variety
over $F$ of positive dimension, with function field $F(X)$. The Cremona group
$\mathrm{Cr}_3(F(X))$, the group of birational automorphisms of affine $3$-space over $F(X)$, is
not generated by its pseudo-regularizable elements.

This is Theorem 1.2 (1) (d) of Lin and Shinder.

## Sources

- H.-Y. Lin and E. Shinder, `Motivic invariants of birational maps`, Annals of Math, 199 (1) 2024. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_motivic_invariants` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.MotivicInvariantsWanted.MotivicInvariants.theorem_1_2_1_d` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group/index.html#theorem-1-2-1-d).

## $\mathrm{Cr}_n$ of a subfield of $\mathbb{C}$ is not generated by pseudo-regularizable elements for $n \ge 4$

**$\mathrm{Cr}_n$ of a subfield of $\mathbb{C}$ is not generated by pseudo-regularizable
elements for $n \ge 4$.** Let $k$ be a subfield of $\mathbb{C}$ and let $n \ge 4$. The Cremona group
$\mathrm{Cr}_n(k)$, the group of birational automorphisms of affine $n$-space over $k$, is not
generated by its pseudo-regularizable elements.

This is Theorem 1.2 (2) of Lin and Shinder.

## Sources

- H.-Y. Lin and E. Shinder, `Motivic invariants of birational maps`, Annals of Math, 199 (1) 2024. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_motivic_invariants` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.MotivicInvariantsWanted.MotivicInvariants.theorem_1_2_2` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group/index.html#theorem-1-2-2).

## $\mathrm{Cr}_n$ of an infinite field is not generated by pseudo-regularizable elements for $n \ge 5$

**$\mathrm{Cr}_n$ of an infinite field is not generated by pseudo-regularizable elements for
$n \ge 5$.** Let $k$ be an infinite field and let $n \ge 5$. The Cremona group $\mathrm{Cr}_n(k)$,
the group of birational automorphisms of affine $n$-space over $k$, is not generated by its
pseudo-regularizable elements.

This is Theorem 1.2 (3) of Lin and Shinder.

## Sources

- H.-Y. Lin and E. Shinder, `Motivic invariants of birational maps`, Annals of Math, 199 (1) 2024. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_motivic_invariants` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.MotivicInvariantsWanted.MotivicInvariants.theorem_1_2_3` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/MotivicInvariantsWanted.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group/index.html#theorem-1-2-3).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Birational maps and the Cremona group](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/birational-maps-and-the-cremona-group)
