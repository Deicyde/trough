---
declaration: section
origin: cited
lean: dualSubmodule_mul_eq_div, Submodule.exists_mul_rep, LinearMap.BilinForm.mul_nondegenerate, Submodule.span_coe_eq_top, Submodule.mul_dualSubmoduleToDual_surjective, Submodule.dualEquivMulDualSubmodule, Submodule.dualEquivMulDualSubmodule_spec, FractionalIdeal.coe_inv_eq_mul_dualSubmodule
statement: formalized
proof: formalized
---

# Invertible fractional ideals

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html).

## The multiplication dual is a colon quotient

Let $A$ be a commutative ring and $K$ a field
that is an $A$-algebra, and write $1$ for the $A$-submodule $A \cdot 1$ of $K$. For every
$A$-submodule $M$ of $K$, the dual submodule of $M$ with respect to the multiplication form
$(x, y) \mapsto xy$ on $K$ equals the quotient $1 / M$, the set of $x \in K$ with $xy \in A \cdot 1$
for all $y \in M$.

Formalized by `dualSubmodule_mul_eq_div`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/Dual.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/Dual.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#dual-submodule-mul-eq-div).

## Functionals on a submodule of the fraction field are multiplications

Let $A$ be an
integral domain with fraction field $K$ and let $M$ be a nonzero $A$-submodule of $K$. For every
$A$-linear map $f \colon M \to A$ there is $x \in K$ such that the image of $f(m)$ in $K$ equals
$xm$ for every $m \in M$.

Formalized by `Submodule.exists_mul_rep`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/Dual.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/Dual.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#exists-mul-rep).

## Multiplication is a nondegenerate bilinear form

For every field $K$, the $K$-bilinear
form $(x, y) \mapsto xy$ on $K$ is nondegenerate: if $xy = 0$ for all $y \in K$ then $x = 0$, and
if $xy = 0$ for all $x \in K$ then $y = 0$.

Formalized by `LinearMap.BilinForm.mul_nondegenerate`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/Dual.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/Dual.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#mul-nondegenerate).

## A nonzero submodule spans the field

Let $A$ be a commutative ring and $K$ a field that is
an $A$-algebra. Then every nonzero $A$-submodule $M$ of $K$ spans $K$ as a $K$-vector space.

Formalized by `Submodule.span_coe_eq_top`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/Dual.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/Dual.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#span-coe-eq-top).

## Every functional comes from the multiplication dual

Let $A$ be an integral domain with
fraction field $K$, identify $A$ with its image in $K$, and let $M$ be a nonzero $A$-submodule of
$K$. Let $M^\vee = \{x \in K : xy \in A \text{ for all } y \in M\}$ be the dual submodule of $M$
for the multiplication form $(x, y) \mapsto xy$ on $K$. Then the $A$-linear map
$M^\vee \to \operatorname{Hom}_A(M, A)$ sending $x$ to the functional $y \mapsto xy$ on $M$ is
surjective.

Formalized by `Submodule.mul_dualSubmoduleToDual_surjective`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/Dual.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/Dual.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#mul-dual-submodule-to-dual-surjective).

## Dual of a nonzero submodule of the fraction field

Let $A$ be an integral domain with
fraction field $K$, identify $A$ with its image in $K$, and let $M$ be a nonzero $A$-submodule of
$K$. Let $M^\vee = \{x \in K : xy \in A \text{ for all } y \in M\}$ be the dual submodule of $M$
for the multiplication form $(x, y) \mapsto xy$ on $K$. This is the $A$-linear isomorphism
$\operatorname{Hom}_A(M, A) \to M^\vee$ inverse to the map sending $x \in M^\vee$ to the
functional $y \mapsto xy$ on $M$; it sends $f$ to the unique $x \in M^\vee$ with $f(y) = xy$ for
all $y \in M$.

Formalized by `Submodule.dualEquivMulDualSubmodule`, a definition declared in [MathlibExt/RingTheory/FractionalIdeal/Dual.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/Dual.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#dual-equiv-mul-dual-submodule).

## Formula for the isomorphism onto the multiplication dual

Let $A$ be an integral domain
with fraction field $K$, let $M$ be a nonzero $A$-submodule of $K$, and let
$\varphi \colon \operatorname{Hom}_A(M, A) \to M^\vee$ be the isomorphism onto the dual submodule
$M^\vee$ of $M$ for the multiplication form $(x, y) \mapsto xy$ on $K$. Then for every
$f \in \operatorname{Hom}_A(M, A)$ and every $m \in M$, the image of $f(m)$ in $K$ equals
$\varphi(f) \, m$.

Formalized by `Submodule.dualEquivMulDualSubmodule_spec`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/Dual.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/Dual.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#dual-equiv-mul-dual-submodule-spec).

## The inverse of a nonzero fractional ideal is its multiplication dual

Let $A$ be an
integral domain with fraction field $K$, and let $I$ be a nonzero fractional ideal of $A$ in $K$.
Then $I^{-1}$, viewed as an $A$-submodule of $K$, equals the dual submodule of $I$ with respect
to the multiplication form $(x, y) \mapsto xy$ on $K$, namely the set
$\{x \in K : xy \in A \text{ for all } y \in I\}$, where $A$ is identified with its image in $K$.

Formalized by `FractionalIdeal.coe_inv_eq_mul_dualSubmodule`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/Dual.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/Dual.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#coe-inv-eq-mul-dual-submodule).

## Dual of a nonzero fractional ideal is its inverse

Let $A$ be an integral domain with
fraction field $K$ and let $I$ be a nonzero fractional ideal of $A$ in $K$. This is the $A$-linear
isomorphism $\operatorname{Hom}_A(I, A) \to I^{-1}$, with $I^{-1}$ viewed as an $A$-submodule of
$K$, sending $f$ to the unique $x \in I^{-1}$ such that $f(y) = xy$ in $K$ for all $y \in I$
(where $A$ is identified with its image in $K$).

Formalized by `FractionalIdeal.dualEquivInv`, a definition declared in [MathlibExt/RingTheory/FractionalIdeal/Dual.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/Dual.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#dual-equiv-inv).

## Double dual of an invertible fractional ideal

Let $A$ be an integral domain with fraction
field $K$ and let $I$ be an invertible fractional ideal of $A$ in $K$. This is the $A$-linear
isomorphism $\operatorname{Hom}_A(\operatorname{Hom}_A(I, A), A) \to I$ inverse to the canonical
evaluation map $I \to \operatorname{Hom}_A(\operatorname{Hom}_A(I, A), A)$,
$x \mapsto (f \mapsto f(x))$.

Formalized by `FractionalIdeal.doubleDualEquivOfIsUnit`, a definition declared in [MathlibExt/RingTheory/FractionalIdeal/Dual.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/Dual.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#double-dual-equiv-of-is-unit).

## Localization commutes with division by a finitely generated submodule

Let $R$, $S$ and $K$
be commutative rings with algebra maps $R \to S \to K$ forming a scalar tower, let $p$ be a
submonoid of $R$ such that $S$ is the localization of $R$ at $p$, and suppose the identity map of
$K$ is a localization of the $R$-module $K$ at $p$. For an $R$-submodule $M$ of $K$ write
$M_p = \{x/s : x \in M,\ s \in p\}$ for its localization, an $S$-submodule of $K$, where $x/s$ is
the element $y \in K$ with $s y = x$. For submodules write $M/N = \{x \in K : xN \subseteq M\}$.
Then for $R$-submodules $I$ and $J$ of $K$ with $J$ finitely generated, $(I/J)_p = I_p/J_p$.

Formalized by `Submodule.localized'_div_of_fg`, a lemma declared in [MathlibExt/RingTheory/FractionalIdeal/Extended.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/Extended.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#localized-div-of-fg).

## Extension to a localization is localization

Let $A$ and $B$ be integral domains with $B$
a torsion-free $A$-algebra, and let $K$ be a field that is a fraction field of both $A$ and $B$,
compatibly with $A \to B \to K$. Let $S$ be a submonoid of $A$ such that $B$ is the localization
of $A$ at $S$ and the identity map of $K$ is a localization of the $A$-module $K$ at $S$. Then for
every fractional ideal $I$ of $A$ in $K$, the $B$-submodule of $K$ underlying the extension of $I$
to a fractional ideal of $B$ (the $B$-submodule generated by $I$) equals the localization
$S^{-1}I = \{x/s : x \in I,\ s \in S\}$ of $I$, viewed as a $B$-submodule of $K$.

Formalized by `FractionalIdeal.coe_extendedHom_eq_localized'`, a lemma declared in [MathlibExt/RingTheory/FractionalIdeal/Extended.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/Extended.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#coe-extended-hom-eq-localized).

## Extension to a localization commutes with division by a finitely generated ideal

Let $A$
and $B$ be integral domains with $B$ a torsion-free $A$-algebra, and let $K$ be a field that is a
fraction field of both $A$ and $B$, compatibly with $A \to B \to K$. Let $S$ be a submonoid of $A$
such that $B$ is the localization of $A$ at $S$. Let $I$ and $J$ be fractional ideals of $A$ in $K$
with $J \ne 0$ and $J$ finitely generated as an $A$-module, and write $IB$ for the extension of $I$
to a fractional ideal of $B$. Then $(I/J)B = IB/JB$, where for a nonzero denominator the quotient
of fractional ideals is $I/J = \{x \in K : xJ \subseteq I\}$.

Formalized by `FractionalIdeal.extendedHom_div_of_fg`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/Extended.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/Extended.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#extended-hom-div-of-fg).

## Over a Noetherian domain, extension to a localization commutes with division

Let $A$ be
a Noetherian integral domain, $B$ an integral domain that is a torsion-free $A$-algebra, and $K$ a
field that is a fraction field of both $A$ and $B$, compatibly with $A \to B \to K$. Let $S$ be a
submonoid of $A$ such that $B$ is the localization of $A$ at $S$. Let $I$ and $J$ be fractional
ideals of $A$ in $K$ with $J \ne 0$, and write $IB$ for the extension of $I$ to a fractional ideal
of $B$. Then $(I/J)B = IB/JB$, where for a nonzero denominator the quotient of fractional ideals
is $I/J = \{x \in K : xJ \subseteq I\}$.

Formalized by `FractionalIdeal.extendedHom_div`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/Extended.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/Extended.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#extended-hom-div).

## Invertible fractional ideals of a Noetherian local domain are principal

Let $A$ be a
Noetherian local integral domain with fraction field $K$, and let $I$ be a nonzero fractional ideal
of $A$ in $K$. Then $I$ is invertible if and only if $I$ is principal.

## Sources

- ATLAS NumberTheoryI, Section 3.1, Lemma 3.4.

Formalized by `fractionalIdeal_isUnit_iff_isPrincipal`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/LocalInvertibility.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/LocalInvertibility.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#fractional-ideal-is-unit-iff-is-principa).

## Localization of a fractional ideal at a prime

Let $A$ be an integral domain with fraction
field $K$, let $\mathfrak p$ be a prime ideal of $A$, and write $A_{\mathfrak p}$ for the
localization of $A$ at $\mathfrak p$. The localization $I_{\mathfrak p}$ of a fractional ideal $I$
of $A$ in $K$ is the fractional ideal of $A_{\mathfrak p}$ in $K$ obtained by extending $I$ along
$A \to A_{\mathfrak p}$, that is, the $A_{\mathfrak p}$-submodule of $K$ generated by $I$.

Formalized by `FractionalIdeal.localizeAtPrime`, a definition declared in [MathlibExt/RingTheory/FractionalIdeal/LocalInvertibility.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/LocalInvertibility.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#localize-at-prime).

## Locally principal fractional ideal

Let $A$ be an integral domain with fraction field $K$.
For a maximal ideal $\mathfrak m$ of $A$, write $A_{\mathfrak m}$ for the localization of $A$ at
$\mathfrak m$ and $I_{\mathfrak m}$ for the localization of a fractional ideal $I$ of $A$ in $K$,
the $A_{\mathfrak m}$-submodule of $K$ generated by $I$. A fractional ideal $I$ of $A$ in $K$ is
locally principal if for every maximal ideal $\mathfrak m$ of $A$ the localization
$I_{\mathfrak m}$, as an $A_{\mathfrak m}$-submodule of $K$, is principal.

Formalized by `FractionalIdeal.IsLocallyPrincipal`, a definition declared in [MathlibExt/RingTheory/FractionalIdeal/LocalInvertibility.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/LocalInvertibility.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#is-locally-principal).

## Localization commutes with inverting fractional ideals

Localization commutes with inversion of fractional ideals.

Formalized by `FractionalIdeal.localizeAtPrime_inv`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/LocalInvertibility.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/LocalInvertibility.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#localize-at-prime-inv).

## Inverse of a localized fractional ideal is bounded by localization

The inverse/localization inequality follows from equality.

Formalized by `FractionalIdeal.inv_localizeAtPrime_le`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/LocalInvertibility.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/LocalInvertibility.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#inv-localize-at-prime-le).

## Theorem 3.2

**Theorem 3.2** (maximal-ideal form). A fractional ideal of a Noetherian domain is invertible
iff its localization at every maximal ideal is invertible.

Formalized by `FractionalIdeal.isUnit_iff_isUnit_localizeAtPrime`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/LocalInvertibility.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/LocalInvertibility.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#is-unit-iff-is-unit-localize-at-prime).

## Theorem 3.2

**Theorem 3.2** (prime-ideal form). A fractional ideal of a Noetherian domain is invertible iff
its localization at every prime ideal is invertible.

Formalized by `FractionalIdeal.isUnit_iff_isUnit_localizeAtPrime_all_primes`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/LocalInvertibility.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/LocalInvertibility.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#is-unit-iff-is-unit-localize-at-prime-al).

## Corollary 3.5

A nonzero fractional ideal of a Noetherian domain is invertible iff it is
locally principal.

Formalized by `FractionalIdeal.isUnit_iff_isLocallyPrincipal`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/LocalInvertibility.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/FractionalIdeal/LocalInvertibility.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html#is-unit-iff-is-locally-principal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Invertible fractional ideals](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/dedekind-domains/invertible-fractional-ideals)
