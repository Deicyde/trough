---
declaration: section
origin: cited
lean: MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightProfinite.shift, MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.ι, MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.ι_split, MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.P_map, MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.P, MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.P_proj, MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.PSequence, MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.PSequence_exact
statement: formalized
---

# Solid condensed homology of CW complexes

45 results, 32 proved and 13 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html).

## Light Profinite

## The shift map on $\mathbb{N} \cup \{\infty\}$

Write $\mathbb{N} \cup \{\infty\}$ for the
one-point compactification of $\mathbb{N}$, viewed as a light profinite set. The shift map is the
continuous map $\mathbb{N} \cup \{\infty\} \to \mathbb{N} \cup \{\infty\}$ sending $n$ to $n + 1$
and $\infty$ to $\infty$.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightProfinite.shift`, a definition declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#shift).

## Inclusion of the point at infinity

The morphism of light profinite spaces from the
one-point space to the one-point compactification $\mathbb{N} \cup \{\infty\}$ of $\mathbb{N}$
that sends the point to $\infty$.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.ι`, a definition declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#untitled).

## Splitting of the inclusion of the point at infinity

The inclusion of the point at infinity
into the one-point compactification $\mathbb{N} \cup \{\infty\}$ of $\mathbb{N}$ is a split
monomorphism of light profinite spaces, with retraction the unique map from
$\mathbb{N} \cup \{\infty\}$ to the one-point space.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.ι_split`, a definition declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#split).

## The map ℤ(∞) → ℤ(ℕ ∪ \{∞})

For a light profinite set $S$, let $\mathbb{Z}[S]$ be the free
light condensed abelian group on $S$, and let $\iota$ be the inclusion of the point $\infty$ into
$\mathbb{N} \cup \{\infty\}$. This is the morphism
$\mathbb{Z}[\infty] \to \mathbb{Z}[\mathbb{N} \cup \{\infty\}]$ induced by $\iota$, where
$\mathbb{Z}[\infty]$ is the free light condensed abelian group on a point.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.P_map`, a definition declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#p-map).

## The light condensed abelian group P

For a light profinite set $S$, let $\mathbb{Z}[S]$ be
the free light condensed abelian group on $S$, and let $\mathbb{N} \cup \{\infty\}$ be the
one-point compactification of $\mathbb{N}$. Then
$P = \mathbb{Z}[\mathbb{N} \cup \{\infty\}]/\mathbb{Z}[\infty]$ is the cokernel of the morphism
$\mathbb{Z}[\infty] \to \mathbb{Z}[\mathbb{N} \cup \{\infty\}]$ induced by the inclusion of the
point $\infty$.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.P`, a definition declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#p).

## The projection onto P

Write $\mathbb{Z}[S]$ for the free light condensed abelian group on
a light profinite set $S$, and let $P = \mathbb{Z}[\mathbb{N} \cup \{\infty\}]/\mathbb{Z}[\infty]$.
This is the quotient map $\mathbb{Z}[\mathbb{N} \cup \{\infty\}] \to P$, the cokernel projection
of the map $\mathbb{Z}[\infty] \to \mathbb{Z}[\mathbb{N} \cup \{\infty\}]$ induced by the
inclusion of the point $\infty$.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.P_proj`, a definition declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#p-proj).

## The short complex defining $P$

Write $\mathbb{N} \cup \{\infty\}$ for the one-point
compactification of $\mathbb{N}$, viewed as a light profinite set, and $\mathbb{Z}[S]$ for the free
light condensed abelian group on a light profinite set $S$, with $\mathbb{Z}[\infty]$ the one on a
point. This is the short complex of light condensed abelian groups
$\mathbb{Z}[\infty] \to \mathbb{Z}[\mathbb{N} \cup \{\infty\}] \to P$ whose first map is induced by
the inclusion of the point $\infty$ and whose second map is the cokernel projection onto
$P = \mathbb{Z}[\mathbb{N} \cup \{\infty\}]/\mathbb{Z}[\infty]$.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.PSequence`, a definition declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#psequence).

## Short exactness of the sequence defining $P$

Write $\mathbb{N} \cup \{\infty\}$ for the
one-point compactification of $\mathbb{N}$, viewed as a light profinite set, and $\mathbb{Z}[S]$ for
the free light condensed abelian group on a light profinite set $S$, with $\mathbb{Z}[\infty]$ the
one on a point. The short complex of light condensed abelian groups
$\mathbb{Z}[\infty] \to \mathbb{Z}[\mathbb{N} \cup \{\infty\}] \to P$, whose first map is induced
by the inclusion of the point $\infty$ and whose second map is the cokernel projection onto
$P = \mathbb{Z}[\mathbb{N} \cup \{\infty\}]/\mathbb{Z}[\infty]$, is short exact: the first map is
a monomorphism, the second map is an epimorphism, and the sequence is exact in the middle.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.PSequence_exact`, a lemma declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#psequence-exact).

## A splitting of the sequence defining $P$

Write $\mathbb{N} \cup \{\infty\}$ for the
one-point compactification of $\mathbb{N}$, viewed as a light profinite set, and $\mathbb{Z}[S]$ for
the free light condensed abelian group on a light profinite set $S$, with $\mathbb{Z}[\infty]$ the
one on a point. Let $f \colon \mathbb{Z}[\infty] \to \mathbb{Z}[\mathbb{N} \cup \{\infty\}]$ be
induced by the inclusion of the point $\infty$, and let
$g \colon \mathbb{Z}[\mathbb{N} \cup \{\infty\}] \to P$ be the cokernel projection onto
$P = \mathbb{Z}[\mathbb{N} \cup \{\infty\}]/\mathbb{Z}[\infty]$. This is a chosen splitting of the
short exact sequence of light condensed abelian groups
$\mathbb{Z}[\infty] \xrightarrow{f} \mathbb{Z}[\mathbb{N} \cup \{\infty\}] \xrightarrow{g} P$,
that is, maps $r \colon \mathbb{Z}[\mathbb{N} \cup \{\infty\}] \to \mathbb{Z}[\infty]$ and
$s \colon P \to \mathbb{Z}[\mathbb{N} \cup \{\infty\}]$ such that $r \circ f = \mathrm{id}$,
$g \circ s = \mathrm{id}$ and $f \circ r + s \circ g = \mathrm{id}$, where $r$ is induced by the
map from $\mathbb{N} \cup \{\infty\}$ to the point.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.PSequence_split`, a definition declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#psequence-split).

## P is a retract of ℤ(ℕ ∪ \{∞})

Write $\mathbb{Z}[S]$ for the free light condensed abelian
group on a light profinite set $S$. The quotient
$P = \mathbb{Z}[\mathbb{N} \cup \{\infty\}]/\mathbb{Z}[\infty]$ by the image of the map induced by
the inclusion of the point $\infty$ is a retract of $\mathbb{Z}[\mathbb{N} \cup \{\infty\}]$: the
short exact sequence
$0 \to \mathbb{Z}[\infty] \to \mathbb{Z}[\mathbb{N} \cup \{\infty\}] \to P \to 0$ splits, and a
section of the projection $\mathbb{Z}[\mathbb{N} \cup \{\infty\}] \to P$ from this splitting,
together with the projection, exhibits the retraction.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.P_retract`, a definition declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#p-retract).

## Maps out of P

Write $\mathbb{Z}[S]$ for the free light condensed abelian group on a light
profinite set $S$, and let $P = \mathbb{Z}[\mathbb{N} \cup \{\infty\}]/\mathbb{Z}[\infty]$ be the
cokernel of the map $\mathbb{Z}[\infty] \to \mathbb{Z}[\mathbb{N} \cup \{\infty\}]$ induced by the
inclusion of the point $\infty$. Let $A$ be a light condensed abelian group and let
$f \colon \mathbb{Z}[\mathbb{N} \cup \{\infty\}] \to A$ be a morphism whose composite with this
map is zero. Then $f$ factors through the projection
$\mathbb{Z}[\mathbb{N} \cup \{\infty\}] \to P$, and this is the induced morphism $P \to A$.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.P_homMk`, a definition declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#p-hom-mk).

## One minus shift on ℤ(ℕ ∪ \{∞})

Let $\mathbb{Z}[\mathbb{N} \cup \{\infty\}]$ be the free
light condensed abelian group on the light profinite set $\mathbb{N} \cup \{\infty\}$, and let
$\mathrm{shift}$ be its endomorphism induced by the map $n \mapsto n + 1$, $\infty \mapsto \infty$.
This is the endomorphism $1 - \mathrm{shift}$ of $\mathbb{Z}[\mathbb{N} \cup \{\infty\}]$.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.oneMinusShift'`, a definition declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#one-minus-shift).

## One minus shift on P

Write $\mathbb{Z}[S]$ for the free light condensed abelian group on
a light profinite set $S$, let $\mathbb{N} \cup \{\infty\}$ be the one-point compactification of
$\mathbb{N}$, and let $P = \mathbb{Z}[\mathbb{N} \cup \{\infty\}]/\mathbb{Z}[\infty]$ be the
cokernel of the map induced by the inclusion of the point $\infty$. Let $\mathrm{shift}$ be the
endomorphism of $\mathbb{Z}[\mathbb{N} \cup \{\infty\}]$ induced by $n \mapsto n + 1$,
$\infty \mapsto \infty$. The endomorphism $1 - \mathrm{shift}$ vanishes on $\mathbb{Z}[\infty]$,
so it factors through a morphism $P \to \mathbb{Z}[\mathbb{N} \cup \{\infty\}]$. Composing this
morphism with the projection onto $P$ gives the induced endomorphism $1 - \mathrm{shift}$ of
$P$.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.oneMinusShift`, a definition declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#one-minus-shift-2).

## Solid light condensed abelian groups

Write $\mathbb{Z}[S]$ for the free light condensed
abelian group on a light profinite set $S$, let $\mathbb{N} \cup \{\infty\}$ be the one-point
compactification of $\mathbb{N}$, and let
$P = \mathbb{Z}[\mathbb{N} \cup \{\infty\}]/\mathbb{Z}[\infty]$ be the cokernel of the map induced
by the inclusion of the point $\infty$. The shift $n \mapsto n + 1$, $\infty \mapsto \infty$
induces an endomorphism $1 - \mathrm{shift}$ of $\mathbb{Z}[\mathbb{N} \cup \{\infty\}]$, and
hence of $P$. A light condensed abelian group $A$ is *solid* if precomposition with this
endomorphism of $P$ is an isomorphism from the internal hom $\underline{\mathrm{Hom}}(P, A)$ to
itself.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.isSolid`, a definition declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#is-solid).

## The solidity class

For a light condensed abelian group $A$, the class asserting that $A$
is solid.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.IsSolid`, an abbreviation declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#is-solid-2).

## The category of light solid abelian groups

Write $\mathbb{Z}[S]$ for the free light
condensed abelian group on a light profinite set $S$, let $\mathbb{N} \cup \{\infty\}$ be the
one-point compactification of $\mathbb{N}$, viewed as a light profinite set, write $\mathrm{pt}$ for
the one-point light profinite set, and let $P$ be the cokernel of the map
$\mathbb{Z}[\mathrm{pt}] \to \mathbb{Z}[\mathbb{N} \cup \{\infty\}]$ induced by the inclusion of
the point $\infty$. The endomorphism $1 - \mathrm{shift}$ of
$\mathbb{Z}[\mathbb{N} \cup \{\infty\}]$, where $\mathrm{shift}$ is induced by $n \mapsto n + 1$
and $\infty \mapsto \infty$, descends to an endomorphism of $P$. A light condensed abelian group
$A$ is solid when this endomorphism of $P$ induces an isomorphism of internal homs
$\underline{\mathrm{Hom}}(P, A) \to \underline{\mathrm{Hom}}(P, A)$. The category of light solid
abelian groups is the full subcategory of light condensed abelian groups on the solid objects.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid`, an abbreviation declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#solid).

## Derived category of light condensed abelian groups

The derived category of the abelian
category of light condensed abelian groups.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.DLightCondAb`, an abbreviation declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#dlight-cond-ab).

## Derived category of light solid abelian groups

The derived category of the abelian
category of light solid abelian groups.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.DSolid`, an abbreviation declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#dsolid).

## Solidification

The solidification functor from the category of light condensed abelian
groups to the category of light solid abelian groups.

This declaration fixes only the functor. Its intended characterization, as left adjoint to the
inclusion of light solid abelian groups into light condensed abelian groups, is the separate
solidification adjunction.

## Sources

- https://github.com/dagurtomas/LeanCondensed; D. Clausen and P. Scholze, lectures on analytic stacks and light condensed mathematics.; P. Scholze, Lectures on Condensed Mathematics, https://arxiv.org/pdf/2605.03658. Problem `derived_solidification_free_CW_homology` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.solidification` is written with `def_wanted` in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#solidification).

## Solidification adjunction

An adjunction exhibiting the solidification functor from light
condensed abelian groups to light solid abelian groups as left adjoint to the inclusion of the full
subcategory of light solid abelian groups into light condensed abelian groups.

## Sources

- https://github.com/dagurtomas/LeanCondensed; D. Clausen and P. Scholze, lectures on analytic stacks and light condensed mathematics.; P. Scholze, Lectures on Condensed Mathematics, https://arxiv.org/pdf/2605.03658. Problem `derived_solidification_free_CW_homology` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.solidificationAdjunction` is written with `def_wanted` in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#solidification-adjunction).

## Derived solidification

A functor from the derived category of light condensed abelian
groups to the derived category of light solid abelian groups.

Separate statements require it to be the left derived functor of degreewise solidification and
left adjoint to the derived inclusion; these determine it up to natural isomorphism.

## Sources

- https://github.com/dagurtomas/LeanCondensed; D. Clausen and P. Scholze, lectures on analytic stacks and light condensed mathematics.; P. Scholze, Lectures on Condensed Mathematics, https://arxiv.org/pdf/2605.03658. Problem `derived_solidification_free_CW_homology` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.derivedSolidification` is written with `def_wanted` in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#derived-solidification).

## Comparison map from derived to degreewise solidification

Let $Q$ denote the localization
functors from cochain complexes to derived categories. This is a natural transformation from the
functor sending a cochain complex $K$ of light condensed abelian groups to the derived
solidification of $Q(K)$ to the functor sending $K$ to $Q(\mathrm{Sol}(K))$, where
$\mathrm{Sol}(K)$ is the complex of light solid abelian groups obtained by applying solidification
to $K$ degreewise.

## Sources

- https://github.com/dagurtomas/LeanCondensed; D. Clausen and P. Scholze, lectures on analytic stacks and light condensed mathematics.; P. Scholze, Lectures on Condensed Mathematics, https://arxiv.org/pdf/2605.03658. Problem `derived_solidification_free_CW_homology` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.derivedSolidificationCounit` is written with `def_wanted` in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#derived-solidification-counit).

## Derived solidification is the left derived functor of solidification

Let $Q$ denote the
localization functors from cochain complexes indexed by $\mathbb{Z}$ to derived categories.
Derived solidification, together with the comparison natural transformation from $Q$ followed by
derived solidification to degreewise solidification followed by $Q$, is a left derived functor of
the functor that applies solidification degreewise to a cochain complex of light condensed abelian
groups and then passes to the derived category of light solid abelian groups, with respect to the
quasi-isomorphisms of cochain complexes of light condensed abelian groups.

## Sources

- https://github.com/dagurtomas/LeanCondensed; D. Clausen and P. Scholze, lectures on analytic stacks and light condensed mathematics.; P. Scholze, Lectures on Condensed Mathematics, https://arxiv.org/pdf/2605.03658. Problem `derived_solidification_free_CW_homology` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.derivedSolidification_isLeftDerivedFunctor` is written with `def_wanted` in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 367](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L367). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#derived-solidification-is-left-derived-f).

## Degreewise inclusion of complexes of light solid abelian groups

The functor from cochain
complexes indexed by $\mathbb{Z}$ of light solid abelian groups to cochain complexes indexed by
$\mathbb{Z}$ of light condensed abelian groups that applies the inclusion of light solid abelian
groups into light condensed abelian groups in each degree.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.inclusionComplexes`, an abbreviation declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#inclusion-complexes).

## Derived inclusion of solid abelian groups

The inclusion $\iota$ of light solid abelian
groups into light condensed abelian groups is exact, so it induces a functor $D(\iota)$ from the
derived category of light solid abelian groups to the derived category of light condensed abelian
groups.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.derivedInclusion`, an abbreviation declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#derived-inclusion).

## The derived inclusion is computed degreewise

Let $\iota$ be the inclusion of light solid
abelian groups into light condensed abelian groups, $D(\iota)$ the induced derived inclusion, and
$Q$ the localization functors from cochain complexes to derived categories. This is the natural
isomorphism $D(\iota)(Q K) \cong Q(\iota K)$ for cochain complexes $K$ of light solid abelian
groups, where $\iota K$ is $K$ with $\iota$ applied degreewise.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.derivedInclusionFactors`, an abbreviation declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#derived-inclusion-factors).

## Comparison map for the derived inclusion

Let $\iota$ be the inclusion of light solid
abelian groups into light condensed abelian groups, $D(\iota)$ the induced derived inclusion, and
$Q$ the localization functors from cochain complexes to derived categories. The comparison map is
the natural transformation from $K \mapsto Q(\iota K)$ to $K \mapsto D(\iota)(Q K)$, for cochain
complexes $K$ of light solid abelian groups, where $\iota K$ is $K$ with $\iota$ applied
degreewise; it is the inverse of the natural isomorphism $D(\iota)(Q K) \cong Q(\iota K)$.

With this comparison map, $D(\iota)$ is a right derived functor of the degreewise inclusion with
respect to quasi-isomorphisms.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.derivedInclusionComparison`, an abbreviation declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#derived-inclusion-comparison).

## Derived solidification is left adjoint to the derived inclusion

An adjunction in which
derived solidification, from the derived category of light condensed abelian groups to the derived
category of light solid abelian groups, is left adjoint to the derived inclusion $D(\iota)$ induced
by the inclusion $\iota$ of light solid abelian groups into light condensed abelian groups.

## Sources

- https://github.com/dagurtomas/LeanCondensed; D. Clausen and P. Scholze, lectures on analytic stacks and light condensed mathematics.; P. Scholze, Lectures on Condensed Mathematics, https://arxiv.org/pdf/2605.03658. Problem `derived_solidification_free_CW_homology` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.derivedSolidificationAdjunction` is written with `def_wanted` in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#derived-solidification-adjunction).

## Free light condensed abelian group on a topological space

For a topological space $X$,
$\mathbb{Z}[X]$ is the free light condensed abelian group on the light condensed set associated
with $X$.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.freeLightCondAbOfTop`, an abbreviation declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#free-light-cond-ab-of-top).

## Free light condensed abelian group functor on topological spaces

The functor from
topological spaces to light condensed abelian groups sending a space $X$ to the free light
condensed abelian group $\mathbb{Z}[X]$ on the light condensed set associated with $X$.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.freeLightCondAbOfTopFunctor`, an abbreviation declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#free-light-cond-ab-of-top-functor).

## Singular homology as a light condensed abelian group

For a topological space $X$ and
$n \in \mathbb{N}$, this is the discrete light condensed abelian group on the $n$-th integral
singular homology group $H_n(X; \mathbb{Z})$.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.singularHomologyLightCondAb`, an abbreviation declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 414](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L414). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#singular-homology-light-cond-ab).

## The singular chain complex as a complex of light condensed abelian groups

This is the
functor from topological spaces to cochain complexes of light condensed abelian groups sending a
space $X$ to the complex whose term in degree $-n$, for $n \ge 0$, is the discrete light condensed
abelian group on the integral singular $n$-chains $C_n(X; \mathbb{Z})$, with the singular boundary
maps as differentials and zero in positive degrees.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.singularChainsLightCondAbComplexFunctor`, an abbreviation declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#singular-chains-light-cond-ab-complex-fu).

## The singular chain functor into the derived category

This is the functor from topological
spaces to the derived category of light condensed abelian groups sending a space $X$ to its
integral singular chain complex, regarded as a cochain complex of discrete light condensed abelian
groups with the $n$-chains in degree $-n$.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.singularChainsLightCondAbDerivedFunctor`, an abbreviation declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#singular-chains-light-cond-ab-derived-fu).

## The singular chains of a space in the derived category

For a topological space $X$, this
is the integral singular chain complex of $X$, regarded as a cochain complex of discrete light
condensed abelian groups with the $n$-chains in degree $-n$, as an object of the derived category
of light condensed abelian groups.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.singularChainsLightCondAbDerived`, an abbreviation declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 433](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L433). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#singular-chains-light-cond-ab-derived).

## Spaces admitting a CW complex structure

A topological space $X$ has this property when
it admits a classical CW complex structure whose underlying set is all of $X$.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.isCWTopCat`, an abbreviation declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#is-cwtop-cat).

## The category of spaces admitting a CW structure

The full subcategory of the category of
topological spaces whose objects are the spaces $X$ admitting a classical CW complex structure
with underlying set all of $X$; its morphisms are all continuous maps between such spaces.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.CWTopCat`, an abbreviation declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 441](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#cwtop-cat).

## Inclusion of CW spaces into topological spaces

The inclusion functor from the full
subcategory of topological spaces admitting a classical CW complex structure into the category of
topological spaces.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.CWTopCat.toTopCat`, an abbreviation declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 449](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L449). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#to-top-cat).

## Derived solidification on CW complexes

A functor from the category of topological spaces
admitting a CW complex structure, with all continuous maps as morphisms, to the derived category
of light condensed abelian groups.

A separate specification identifies it, up to natural isomorphism, with the functor sending $X$
to the derived inclusion of the derived solidification of the free light condensed abelian group
$\mathbb{Z}[X]$, viewed as a complex concentrated in degree $0$.

## Sources

- https://github.com/dagurtomas/LeanCondensed; D. Clausen and P. Scholze, lectures on analytic stacks and light condensed mathematics.; P. Scholze, Lectures on Condensed Mathematics, https://arxiv.org/pdf/2605.03658. Problem `derived_solidification_free_CW_homology` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.derivedSolidificationFreeCWFunctor` is written with `def_wanted` in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 456](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L456). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#derived-solidification-free-cwfunctor).

## Natural isomorphism specifying derived solidification on CW complexes

A natural
isomorphism between the derived solidification functor on CW complexes and the composite functor
that sends a topological space $X$ admitting a CW complex structure to the free light condensed
abelian group $\mathbb{Z}[X]$, views it as a complex concentrated in degree $0$ in the derived
category of light condensed abelian groups, applies derived solidification, and then applies the
derived inclusion of light solid abelian groups into light condensed abelian groups. Both are
functors from the category of topological spaces admitting a CW complex structure, with all
continuous maps as morphisms, to the derived category of light condensed abelian groups.

## Sources

- https://github.com/dagurtomas/LeanCondensed; D. Clausen and P. Scholze, lectures on analytic stacks and light condensed mathematics.; P. Scholze, Lectures on Condensed Mathematics, https://arxiv.org/pdf/2605.03658. Problem `derived_solidification_free_CW_homology` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.derivedSolidificationFreeCWFunctorSpec` is written with `def_wanted` in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 461](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L461). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#derived-solidification-free-cwfunctor-sp).

## The singular chain functor on CW spaces

This is the functor from the category of
topological spaces admitting a CW complex structure, with all continuous maps as morphisms, to the
derived category of light condensed abelian groups sending $X$ to its integral singular chain
complex, regarded as a cochain complex of discrete light condensed abelian groups with the
$n$-chains in degree $-n$.

Formalized by `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.singularChainsLightCondAbCWDerivedFunctor`, an abbreviation declared in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 468](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L468). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#singular-chains-light-cond-ab-cwderived).

## Derived solidification of free CW complexes computes singular chains

A natural
isomorphism of functors from the category of spaces admitting a CW structure to the derived
category of light condensed abelian groups, from the derived solidification functor $F$ to the
integral singular chain complex functor. Here $F(X)$ is the derived inclusion of the derived
solidification of the free light condensed abelian group $\mathbb{Z}[X]$ placed in degree $0$ (up
to a specified natural isomorphism), and the singular chain complex of $X$ is viewed as a complex
of discrete light condensed abelian groups with chains of degree $n$ in cohomological degree $-n$.

## Sources

- https://github.com/dagurtomas/LeanCondensed; D. Clausen and P. Scholze, lectures on analytic stacks and light condensed mathematics.; P. Scholze, Lectures on Condensed Mathematics, https://arxiv.org/pdf/2605.03658. Problem `derived_solidification_free_CW_homology` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.derivedSolidification_free_CW_derivedNatIso` is written with `def_wanted` in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 476](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L476). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#derived-solidification-free-cw-derived-n).

## Pointwise derived comparison for CW complexes

For a topological space $X$ with a CW
complex structure on all of $X$, an isomorphism in the derived category of light condensed abelian
groups from the derived inclusion of the derived solidification of the free light condensed
abelian group $\mathbb{Z}[X]$, placed in degree $0$, to the integral singular chain complex of $X$,
viewed as a complex of discrete light condensed abelian groups with chains of degree $n$ placed in
cohomological degree $-n$.

Stated but not proved: `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.derivedSolidification_free_CW_derivedIso` is written with `def_wanted` in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 480](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L480). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#derived-solidification-free-cw-derived-i).

## The pointwise derived comparison is the component of the natural one

Let $X$ be a
topological space with a CW complex structure on all of $X$, regarded as an object of the category
of spaces admitting a CW structure, and let $\mathbb{Z}[X]$ be the free light condensed abelian
group on $X$. Let $F$ be the derived solidification functor on spaces admitting a CW structure,
let $\sigma$ be the natural isomorphism from $F$ to the functor sending $X$ to the derived
inclusion of the derived solidification of $\mathbb{Z}[X]$ placed in degree $0$, and let $\nu$ be
the natural isomorphism from $F$ to the integral singular chain complex functor with values in the
derived category of light condensed abelian groups. Then the pointwise isomorphism $\phi_X$ from
the derived inclusion of the derived solidification of $\mathbb{Z}[X]$ (placed in degree $0$) to
the singular chain complex of $X$ equals $\nu_X \circ \sigma_X^{-1}$.

Stated but not proved: `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.derivedSolidification_free_CW_derivedIso_eq` is written with `theorem_wanted` in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 489](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L489). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#derived-solidification-free-cw-derived-i-2).

## Derived solidification computes singular homology

Let $X$ be a topological space
equipped with a CW complex structure, let $n$ be a natural number, and let $\mathbb{Z}[X]$ be the
free light condensed abelian group on $X$, viewed as a complex concentrated in degree $0$ in the
derived category of light condensed abelian groups. Apply derived solidification to
$\mathbb{Z}[X]$, take the homology in cohomological degree $-n$, which is a light solid abelian
group, and regard it as a light condensed abelian group. This is an isomorphism between the
resulting light condensed abelian group and the $n$-th singular homology group $H_n(X; \mathbb{Z})$
of $X$ with integer coefficients, regarded as a discrete light condensed abelian group.

The derived category is cohomologically indexed, so the $n$-th homology group sits in degree $-n$.

## Sources

- https://github.com/dagurtomas/LeanCondensed; D. Clausen and P. Scholze, lectures on analytic stacks and light condensed mathematics.; P. Scholze, Lectures on Condensed Mathematics, https://arxiv.org/pdf/2605.03658. Problem `derived_solidification_free_CW_homology` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.derivedSolidification_free_CW_homologyIso` is written with `def_wanted` in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 499](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#derived-solidification-free-cw-homology).

## Homology of the derived solidification of a free CW complex

Let $X$ be a topological space
with a CW complex structure on all of $X$, let $\mathbb{Z}[X]$ be the free light condensed abelian
group on $X$, and let $n$ be a natural number. Then the cohomology in degree $-n$ of the derived
solidification of $\mathbb{Z}[X]$ placed in degree $0$, a light solid abelian group regarded as a
light condensed abelian group, is isomorphic to the integral singular homology group
$H_n(X; \mathbb{Z})$ viewed as a discrete light condensed abelian group.

## Sources

- https://github.com/dagurtomas/LeanCondensed; D. Clausen and P. Scholze, lectures on analytic stacks and light condensed mathematics.; P. Scholze, Lectures on Condensed Mathematics, https://arxiv.org/pdf/2605.03658. Problem `derived_solidification_free_CW_homology` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.DerivedSolidCWHomologyWanted.LightCondensed.Solid.derivedSolidification_free_CW_homology` is written with `theorem_wanted` in [WantedExt/Topology/DerivedSolidCWHomologyWanted.lean, line 511](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/DerivedSolidCWHomologyWanted.lean#L511). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html#derived-solidification-free-cw-homology-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Solid condensed homology of CW complexes](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Topology/algebraic-topology/solid-condensed-homology-of-cw-complexes)
