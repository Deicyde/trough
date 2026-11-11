---
declaration: section
origin: cited
lean: FractionalIdeal.ringEquivOfRingEquivHom, FractionalIdeal.unitsMulDistribMulAction, FractionalIdeal.units_smul_val, FractionalIdeal.smul_def, FractionalIdeal.mem_smul_iff_exists, FractionalIdeal.mem_smul_iff, FractionalIdeal.smul_coeIdeal, PrimeSpectrum.smul_asIdeal
statement: formalized
proof: formalized
---

# Ring automorphisms acting on ideals

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/ring-automorphisms-acting-on-ideals/index.html).

## Ring automorphisms act on fractional ideals

Let $R$ be a commutative domain
and $K$ a field of fractions of $R$. For a ring automorphism $\sigma$ of $R$, let $\tilde\sigma$
be the automorphism of $K$ extending $\sigma$. Sending $\sigma$ to the map
$I \mapsto \tilde\sigma(I)$ on fractional ideals of $R$ in $K$ defines a group homomorphism from
the group of ring automorphisms of $R$ to the group of ring automorphisms of the semiring of
fractional ideals of $R$ in $K$.

Formalized by `FractionalIdeal.ringEquivOfRingEquivHom`, a definition declared in [MathlibExt/RingTheory/FractionalIdeal/GroupAction.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/GroupAction.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/ring-automorphisms-acting-on-ideals/index.html#ring-equiv-of-ring-equiv-hom).

## Action on invertible fractional ideals

Let a group $G$ act on a commutative domain $R$
by ring automorphisms, let $K$ be a field of fractions of $R$, and let $G$ act on fractional
ideals of $R$ in $K$ by $g \cdot I = \tilde\sigma_g(I)$, where $\tilde\sigma_g$ is the
automorphism of $K$ extending $r \mapsto g \cdot r$. This induces an action of $G$ on the group
of invertible fractional ideals: $g$ sends an invertible fractional ideal $I$ to $g \cdot I$,
whose inverse is $g \cdot I^{-1}$. This action respects products and fixes the unit fractional
ideal $R$.

Formalized by `FractionalIdeal.unitsMulDistribMulAction`, an abbreviation declared in [MathlibExt/RingTheory/FractionalIdeal/GroupAction.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/GroupAction.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/ring-automorphisms-acting-on-ideals/index.html#units-mul-distrib-mul-action).

## Translating an invertible fractional ideal

Let a group $G$ act on a commutative domain
$R$ by ring automorphisms, let $K$ be a field of fractions of $R$, and let $G$ act on fractional
ideals of $R$ in $K$ by $g \cdot I = \tilde\sigma_g(I)$, where $\tilde\sigma_g$ is the
automorphism of $K$ extending $r \mapsto g \cdot r$. For every $g \in G$ and every invertible
fractional ideal $I$, the translate of $I$ under the induced action on invertible fractional
ideals has underlying fractional ideal $g \cdot I$.

Formalized by `FractionalIdeal.units_smul_val`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/GroupAction.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/GroupAction.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/ring-automorphisms-acting-on-ideals/index.html#units-smul-val).

## The action on fractional ideals is by images

Let a group $G$ act on a commutative domain
$R$ by ring automorphisms and let $K$ be a field of fractions of $R$. For $g \in G$ let
$\tilde\sigma_g$ be the automorphism of $K$ extending the automorphism $r \mapsto g \cdot r$ of
$R$. Then for every $g \in G$ and every fractional ideal $I$ of $R$ in $K$, the induced action
satisfies $g \cdot I = \tilde\sigma_g(I)$, the image of $I$ under $\tilde\sigma_g$.

Formalized by `FractionalIdeal.smul_def`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/GroupAction.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/GroupAction.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/ring-automorphisms-acting-on-ideals/index.html#smul-def).

## Elements of a translated fractional ideal are images

Let a group $G$ act on a
commutative domain $R$ by ring automorphisms, let $K$ be a field of fractions of $R$, and let $G$
act on fractional ideals of $R$ in $K$ by $g \cdot I = \tilde\sigma_g(I)$, where $\tilde\sigma_g$
is the automorphism of $K$ extending $r \mapsto g \cdot r$. For every $g \in G$, every fractional
ideal $I$ and every $x \in K$, we have $x \in g \cdot I$ if and only if $\tilde\sigma_g(y) = x$
for some $y \in I$.

Formalized by `FractionalIdeal.mem_smul_iff_exists`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/GroupAction.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/GroupAction.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/ring-automorphisms-acting-on-ideals/index.html#mem-smul-iff-exists).

## Membership in a translated fractional ideal

Let a group $G$ act on a commutative domain
$R$ by ring automorphisms, let $K$ be a field of fractions of $R$, and let $G$ act on fractional
ideals of $R$ in $K$ by $g \cdot I = \tilde\sigma_g(I)$, where $\tilde\sigma_g$ is the
automorphism of $K$ extending $r \mapsto g \cdot r$. For every $g \in G$, every fractional ideal
$I$ and every $x \in K$, we have $x \in g \cdot I$ if and only if
$\tilde\sigma_g^{-1}(x) \in I$.

Formalized by `FractionalIdeal.mem_smul_iff`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/GroupAction.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/GroupAction.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/ring-automorphisms-acting-on-ideals/index.html#mem-smul-iff).

## Translating an integral ideal

Let a group $G$ act on a commutative domain $R$ by ring
automorphisms, let $K$ be a field of fractions of $R$, and let $G$ act on fractional ideals of
$R$ in $K$ by $g \cdot J = \tilde\sigma_g(J)$, where $\tilde\sigma_g$ is the automorphism of $K$
extending $r \mapsto g \cdot r$. For every $g \in G$ and every ideal $I$ of $R$, the translate
$g \cdot I$ of $I$ viewed as a fractional ideal is the ideal $\{g \cdot a : a \in I\}$ of $R$
viewed as a fractional ideal.

Formalized by `FractionalIdeal.smul_coeIdeal`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/GroupAction.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/GroupAction.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/ring-automorphisms-acting-on-ideals/index.html#smul-coe-ideal).

## Translating a prime ideal by a group element

Let a group $G$ act on a commutative
semiring $R$ by semiring automorphisms, and let $G$ act on the prime spectrum of $R$ by the
induced action. For every $g \in G$ and every point $\mathfrak p$ of the prime spectrum of $R$,
the prime ideal underlying the translated point $g \cdot \mathfrak p$ is the image of the ideal
$\mathfrak p$ under the automorphism of $R$ given by $g$.

Formalized by `PrimeSpectrum.smul_asIdeal`, a theorem declared in [MathlibExt/RingTheory/Spectrum/Prime/GroupAction.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Spectrum/Prime/GroupAction.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/ring-automorphisms-acting-on-ideals/index.html#smul-as-ideal).

## Viewing prime ideals as fractional ideals commutes with the group action

Let a group $G$
act on an integral domain $R$ by ring automorphisms, let $K$ be a fraction field of $R$, and let
$G$ act on the fractional ideals of $R$ in $K$ through the extension of each automorphism of $R$
to $K$. For $g \in G$ and a prime ideal $\mathfrak p$ of $R$, write
$g \cdot \mathfrak p = \{g \cdot x : x \in \mathfrak p\}$ for the image of $\mathfrak p$ under
$g$, again a prime ideal of $R$. Then for every $g \in G$ and every prime ideal $\mathfrak p$ of
$R$, the ideal $g \cdot \mathfrak p$ viewed as a fractional ideal in $K$ equals $g$ applied to
$\mathfrak p$ viewed as a fractional ideal in $K$.

Formalized by `PrimeSpectrum.smul_asIdeal_coe`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/Spectrum.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/Spectrum.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/ring-automorphisms-acting-on-ideals/index.html#smul-as-ideal-coe).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ring automorphisms acting on ideals](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/ring-automorphisms-acting-on-ideals/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/dedekind-domains/ring-automorphisms-acting-on-ideals)
