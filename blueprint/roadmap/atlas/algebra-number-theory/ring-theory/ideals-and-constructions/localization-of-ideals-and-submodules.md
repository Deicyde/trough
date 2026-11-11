---
declaration: section
origin: cited
lean: Submodule.localizedAt, Submodule.mem_localizedAt, Submodule.mem_of_forall_mem_localizedAt_maximal, Submodule.mem_of_forall_mem_localizedAt_prime, Submodule.eq_iInf_localizedAt_maximal, Submodule.eq_iInf_localizedAt_prime, Submodule.eq_iInf_localizedAt_maximal_eq_prime, Ideal.eq_iInf_comap_map_localization_maximal
statement: formalized
proof: formalized
---

# Localization of ideals and submodules

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/localization-of-ideals-and-submodules/index.html).

## Saturation of a submodule at a submonoid

Let $A$ be a commutative ring, $V$ an
$A$-module, $M$ a submodule of $V$ and $S$ a submonoid of $A$. The saturation of $M$ at $S$ is the
submodule of $V$ consisting of the elements $v \in V$ such that $s v \in M$ for some $s \in S$.

Writing $S^{-1}V$ for the localization of $V$ at $S$ and $S^{-1}M \subseteq S^{-1}V$ for that of
$M$, it is the preimage of $S^{-1}M$ under the localization map $V \to S^{-1}V$, that is, the
contraction to $V$ of the extension of $M$ to the localization at $S$.

Formalized by `Submodule.localizedAt`, a definition declared in [MathlibExt/RingTheory/Localization/Submodule.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Localization/Submodule.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/localization-of-ideals-and-submodules/index.html#localized-at).

## Membership in the saturation

Let $A$ be a commutative ring, $V$ an $A$-module, $M$ a
submodule of $V$ and $S$ a submonoid of $A$. An element $v \in V$ lies in the saturation of $M$ at
$S$ if and only if $s v \in M$ for some $s \in S$.

Formalized by `Submodule.mem_localizedAt`, a theorem declared in [MathlibExt/RingTheory/Localization/Submodule.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Localization/Submodule.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/localization-of-ideals-and-submodules/index.html#mem-localized-at).

## Membership is detected at the maximal ideals

Let $A$ be a commutative ring, $V$ an
$A$-module, $M$ a submodule of $V$ and $v \in V$. Suppose that for every maximal ideal
$\mathfrak m$ of $A$, $v$ lies in the saturation of $M$ at $A \setminus \mathfrak m$, that is,
$s v \in M$ for some $s \in A \setminus \mathfrak m$. Then $v \in M$.

## Sources

- ATLAS NumberTheoryI, Section 2.3, Proposition 2.6, element form.

Formalized by `Submodule.mem_of_forall_mem_localizedAt_maximal`, a theorem declared in [MathlibExt/RingTheory/Localization/Submodule.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Localization/Submodule.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/localization-of-ideals-and-submodules/index.html#mem-of-forall-mem-localized-at-maximal).

## Membership is detected at the prime ideals

Let $A$ be a commutative ring, $V$ an
$A$-module, $M$ a submodule of $V$ and $v \in V$. Suppose that for every prime ideal
$\mathfrak p$ of $A$, $v$ lies in the saturation of $M$ at $A \setminus \mathfrak p$, that is,
$s v \in M$ for some $s \in A \setminus \mathfrak p$. Then $v \in M$.

## Sources

- ATLAS NumberTheoryI, Section 2.3, Proposition 2.6, element form.

Formalized by `Submodule.mem_of_forall_mem_localizedAt_prime`, a theorem declared in [MathlibExt/RingTheory/Localization/Submodule.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Localization/Submodule.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/localization-of-ideals-and-submodules/index.html#mem-of-forall-mem-localized-at-prime).

## A submodule is the intersection of its saturations at the maximal ideals

Let $A$ be a
commutative ring, $V$ an $A$-module and $M$ a submodule of $V$. For a maximal ideal
$\mathfrak m$ of $A$, let $M_{\mathfrak m}$ be the saturation of $M$ at $A \setminus \mathfrak m$,
that is, the set of $v \in V$ with $s v \in M$ for some $s \in A \setminus \mathfrak m$. Then $M$
is the intersection of the submodules $M_{\mathfrak m}$ over all maximal ideals $\mathfrak m$
of $A$.

## Sources

- ATLAS NumberTheoryI, Section 2.3, Proposition 2.6, maximal-ideal form.

Formalized by `Submodule.eq_iInf_localizedAt_maximal`, a theorem declared in [MathlibExt/RingTheory/Localization/Submodule.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Localization/Submodule.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/localization-of-ideals-and-submodules/index.html#eq-i-inf-localized-at-maximal-2).

## A submodule is the intersection of its saturations at the prime ideals

Let $A$ be a
commutative ring, $V$ an $A$-module and $M$ a submodule of $V$. For a prime ideal
$\mathfrak p$ of $A$, let $M_{\mathfrak p}$ be the saturation of $M$ at $A \setminus \mathfrak p$,
that is, the set of $v \in V$ with $s v \in M$ for some $s \in A \setminus \mathfrak p$. Then $M$
is the intersection of the submodules $M_{\mathfrak p}$ over all prime ideals $\mathfrak p$
of $A$.

## Sources

- ATLAS NumberTheoryI, Section 2.3, Proposition 2.6, prime-ideal form.

Formalized by `Submodule.eq_iInf_localizedAt_prime`, a theorem declared in [MathlibExt/RingTheory/Localization/Submodule.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Localization/Submodule.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/localization-of-ideals-and-submodules/index.html#eq-i-inf-localized-at-prime-2).

## Intersections of saturations over maximal and over prime ideals agree

Let $A$ be a
commutative ring, $V$ an $A$-module and $M$ a submodule of $V$. For a prime ideal $\mathfrak p$
of $A$, let $M_{\mathfrak p}$ be the saturation of $M$ at $A \setminus \mathfrak p$, that is,
the set of $v \in V$ with $s v \in M$ for some $s \in A \setminus \mathfrak p$. Then the
intersection of the $M_{\mathfrak m}$ over all maximal ideals $\mathfrak m$ of $A$ equals the
intersection of the $M_{\mathfrak p}$ over all prime ideals $\mathfrak p$ of $A$.

Formalized by `Submodule.eq_iInf_localizedAt_maximal_eq_prime`, a theorem declared in [MathlibExt/RingTheory/Localization/Submodule.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Localization/Submodule.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/localization-of-ideals-and-submodules/index.html#eq-i-inf-localized-at-maximal-eq-prime).

## An ideal is the intersection of its contracted localizations at maximal ideals

Let $A$
be a commutative ring and $I$ an ideal of $A$. For a maximal ideal $\mathfrak{m}$ of $A$, let
$\varphi_{\mathfrak{m}} \colon A \to A_{\mathfrak{m}}$ be the canonical map to the localization
of $A$ at $\mathfrak{m}$. Then
$I = \bigcap_{\mathfrak{m}} \varphi_{\mathfrak{m}}^{-1}(I A_{\mathfrak{m}})$, the intersection
over all maximal ideals $\mathfrak{m}$ of $A$: an ideal is the intersection of the contractions
to $A$ of its extensions to the localizations at the maximal ideals.

Formalized by `Ideal.eq_iInf_comap_map_localization_maximal`, a theorem declared in [MathlibExt/RingTheory/Localization/Ideal.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Localization/Ideal.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/localization-of-ideals-and-submodules/index.html#eq-i-inf-comap-map-localization-maximal).

## An ideal is the intersection of its contracted localizations at prime ideals

Let $A$
be a commutative ring and $I$ an ideal of $A$. For a prime ideal $\mathfrak{p}$ of $A$, let
$\varphi_{\mathfrak{p}} \colon A \to A_{\mathfrak{p}}$ be the canonical map to the localization
of $A$ at $\mathfrak{p}$. Then
$I = \bigcap_{\mathfrak{p}} \varphi_{\mathfrak{p}}^{-1}(I A_{\mathfrak{p}})$, the intersection
over all prime ideals $\mathfrak{p}$ of $A$: an ideal is the intersection of the contractions
to $A$ of its extensions to the localizations at the prime ideals.

Formalized by `Ideal.eq_iInf_comap_map_localization_prime`, a theorem declared in [MathlibExt/RingTheory/Localization/Ideal.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Localization/Ideal.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/localization-of-ideals-and-submodules/index.html#eq-i-inf-comap-map-localization-prime).

## Contracted localizations of an ideal: the maximal and prime intersections agree

Let $A$
be a commutative ring and $I$ an ideal of $A$. For a prime ideal $\mathfrak{p}$ of $A$, let
$\varphi_{\mathfrak{p}} \colon A \to A_{\mathfrak{p}}$ be the canonical map to the localization
of $A$ at $\mathfrak{p}$. Then
$\bigcap_{\mathfrak{m}} \varphi_{\mathfrak{m}}^{-1}(I A_{\mathfrak{m}}) =
\bigcap_{\mathfrak{p}} \varphi_{\mathfrak{p}}^{-1}(I A_{\mathfrak{p}})$, where the left
intersection runs over all maximal ideals $\mathfrak{m}$ of $A$ and the right one over all
prime ideals $\mathfrak{p}$ of $A$.

Formalized by `Ideal.iInf_comap_map_localization_maximal_eq_prime`, a theorem declared in [MathlibExt/RingTheory/Localization/Ideal.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Localization/Ideal.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/localization-of-ideals-and-submodules/index.html#i-inf-comap-map-localization-maximal-eq).

## The image of an ideal in the fraction field is the intersection of its localizations at maximal ideals

**The image of an ideal in the fraction field is the intersection of its localizations at
maximal ideals.** Let $A$ be an integral domain with fraction field $K$, let $I$ be an ideal of
$A$, and let $M \subseteq K$ be the image of $I$ under the canonical map $A \to K$, an
$A$-submodule of $K$. For a maximal ideal $\mathfrak{m}$ of $A$, let $M_{\mathfrak{m}}$ be the
localization of $M$ at $\mathfrak{m}$: the set of $x \in K$ such that $s x \in M$ for some
$s \in A \setminus \mathfrak{m}$. Then $M = \bigcap_{\mathfrak{m}} M_{\mathfrak{m}}$, the
intersection over all maximal ideals $\mathfrak{m}$ of $A$, taken inside $K$.

## Sources

- ATLAS NumberTheoryI, Section 2.3, Corollary 2.7, maximal-ideal form.

Formalized by `Ideal.eq_iInf_localizedAt_maximal`, a theorem declared in [MathlibExt/RingTheory/Localization/Ideal.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Localization/Ideal.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/localization-of-ideals-and-submodules/index.html#eq-i-inf-localized-at-maximal).

## The image of an ideal in the fraction field is the intersection of its localizations at prime ideals

**The image of an ideal in the fraction field is the intersection of its localizations at
prime ideals.** Let $A$ be an integral domain with fraction field $K$, let $I$ be an ideal of
$A$, and let $M \subseteq K$ be the image of $I$ under the canonical map $A \to K$, an
$A$-submodule of $K$. For a prime ideal $\mathfrak{p}$ of $A$, let $M_{\mathfrak{p}}$ be the
localization of $M$ at $\mathfrak{p}$: the set of $x \in K$ such that $s x \in M$ for some
$s \in A \setminus \mathfrak{p}$. Then $M = \bigcap_{\mathfrak{p}} M_{\mathfrak{p}}$, the
intersection over all prime ideals $\mathfrak{p}$ of $A$, taken inside $K$.

## Sources

- ATLAS NumberTheoryI, Section 2.3, Corollary 2.7, prime-ideal form.

Formalized by `Ideal.eq_iInf_localizedAt_prime`, a theorem declared in [MathlibExt/RingTheory/Localization/Ideal.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Localization/Ideal.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/localization-of-ideals-and-submodules/index.html#eq-i-inf-localized-at-prime).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Localization of ideals and submodules](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/localization-of-ideals-and-submodules/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/ideals-and-constructions/localization-of-ideals-and-submodules)
