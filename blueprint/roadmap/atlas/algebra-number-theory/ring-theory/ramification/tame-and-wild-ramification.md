---
declaration: section
origin: cited
lean: Algebra.IsResidueSeparableAt, Algebra.IsTamelyRamifiedAt, Algebra.IsWildlyRamifiedAt, Algebra.isResidueSeparableAt_iff, Algebra.isTamelyRamifiedAt_iff, Algebra.isWildlyRamifiedAt_iff, Algebra.isTamelyRamifiedAt_mk, Algebra.IsTamelyRamifiedAt.isSeparable
statement: formalized
proof: formalized
---

# Tame and wild ramification

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-and-wild-ramification/index.html).

## Residue separability at a prime

Let $R$ and $S$ be commutative rings with $S$ an
$R$-algebra, let $q$ be a prime ideal of $S$, and let $p$ be its preimage in $R$. Then $q$ is
residue separable over $R$ when the residue field $\kappa(q)$ is separable over the residue field
$\kappa(p)$, for the algebra structure induced by the canonical local homomorphism $R_p \to S_q$
of localizations.

Formalized by `Algebra.IsResidueSeparableAt`, a definition declared in [MathlibExt/NumberTheory/RamificationInertia/Tame.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/Tame.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-and-wild-ramification/index.html#is-residue-separable-at).

## Tamely ramified prime

Let $R$ and $S$ be commutative rings with $S$ an $R$-algebra, and
let $q$ be a prime ideal of $S$. Then $q$ is *tamely ramified* over $R$ when $q$ is residue
separable over $R$ and the characteristic of the residue field $\kappa(q)$ does not divide the
ramification index of $q$ over $R$.

Formalized by `Algebra.IsTamelyRamifiedAt`, a definition declared in [MathlibExt/NumberTheory/RamificationInertia/Tame.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/Tame.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-and-wild-ramification/index.html#is-tamely-ramified-at).

## Wildly ramified prime

Let $R$ be a commutative ring, $S$ a commutative $R$-algebra and
$q$ a prime ideal of $S$. Then $q$ is *wildly ramified* over $R$ if it is not tamely ramified
over $R$.

Formalized by `Algebra.IsWildlyRamifiedAt`, a definition declared in [MathlibExt/NumberTheory/RamificationInertia/Tame.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/Tame.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-and-wild-ramification/index.html#is-wildly-ramified-at).

## Residue separability, unfolded

Let $R$ and $S$ be commutative rings with $S$ an
$R$-algebra, let $q$ be a prime ideal of $S$, and let $p$ be its preimage in $R$. Then $q$ is
residue separable over $R$ if and only if the residue field $\kappa(q)$ is separable over the
residue field $\kappa(p)$, for the algebra structure induced by the canonical local homomorphism
$R_p \to S_q$ of localizations.

Formalized by `Algebra.isResidueSeparableAt_iff`, a theorem declared in [MathlibExt/NumberTheory/RamificationInertia/Tame.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/Tame.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-and-wild-ramification/index.html#is-residue-separable-at-iff).

## Characterization of tame ramification

Let $R$ and $S$ be commutative rings with $S$ an
$R$-algebra, and let $q$ be a prime ideal of $S$. Then $q$ is tamely ramified over $R$ if and only
if $q$ is residue separable over $R$ and the characteristic of the residue field $\kappa(q)$ does
not divide the ramification index of $q$ over $R$.

Formalized by `Algebra.isTamelyRamifiedAt_iff`, a theorem declared in [MathlibExt/NumberTheory/RamificationInertia/Tame.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/Tame.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-and-wild-ramification/index.html#is-tamely-ramified-at-iff).

## Wild ramification is the failure of tame ramification

Let $R$ be a commutative ring,
$S$ a commutative $R$-algebra and $q$ a prime ideal of $S$. Then $q$ is wildly ramified over $R$
if and only if $q$ is not tamely ramified over $R$.

Formalized by `Algebra.isWildlyRamifiedAt_iff`, a theorem declared in [MathlibExt/NumberTheory/RamificationInertia/Tame.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/Tame.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-and-wild-ramification/index.html#is-wildly-ramified-at-iff).

## Criterion for tame ramification

Let $R$ and $S$ be commutative rings with $S$ an
$R$-algebra, and let $q$ be a prime ideal of $S$. If $q$ is residue separable over $R$ and the
characteristic of the residue field $\kappa(q)$ does not divide the ramification index of $q$ over
$R$, then $q$ is tamely ramified over $R$.

Formalized by `Algebra.isTamelyRamifiedAt_mk`, a theorem declared in [MathlibExt/NumberTheory/RamificationInertia/Tame.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/Tame.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-and-wild-ramification/index.html#is-tamely-ramified-at-mk).

## Tame primes are residue separable

Let $R$ and $S$ be commutative rings with $S$ an
$R$-algebra, and let $q$ be a prime ideal of $S$. If $q$ is tamely ramified over $R$, then $q$ is
residue separable over $R$.

Formalized by `Algebra.IsTamelyRamifiedAt.isSeparable`, a theorem declared in [MathlibExt/NumberTheory/RamificationInertia/Tame.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/Tame.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-and-wild-ramification/index.html#is-separable).

## The residue characteristic of a tame prime does not divide its ramification index

Let
$R$ be a commutative ring, $S$ a commutative $R$-algebra and $q$ a prime ideal of $S$ with residue
field $\kappa(q)$. If $q$ is tamely ramified over $R$, then the characteristic of $\kappa(q)$ does
not divide the ramification index of $q$ over $R$.

Formalized by `Algebra.IsTamelyRamifiedAt.not_dvd`, a theorem declared in [MathlibExt/NumberTheory/RamificationInertia/Tame.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/Tame.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-and-wild-ramification/index.html#not-dvd).

## Wild ramification under residue separability

Let $R$ and $S$ be commutative rings with $S$
an $R$-algebra, and let $q$ be a prime ideal of $S$ that is residue separable over $R$. Then $q$ is
wildly ramified over $R$ if and only if the characteristic of the residue field $\kappa(q)$ divides
the ramification index of $q$ over $R$.

Formalized by `Algebra.isWildlyRamifiedAt_iff_char_dvd`, a theorem declared in [MathlibExt/NumberTheory/RamificationInertia/Tame.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/Tame.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-and-wild-ramification/index.html#is-wildly-ramified-at-iff-char-dvd).

## Divisibility of the ramification index forces wild ramification

Let $R$ be a
commutative ring, $S$ a commutative $R$-algebra and $q$ a prime ideal of $S$ with residue field
$\kappa(q)$. If the characteristic of $\kappa(q)$ divides the ramification index of $q$ over $R$,
then $q$ is wildly ramified over $R$.

No separability hypothesis on the residue field extension is needed.

Formalized by `Algebra.isWildlyRamifiedAt_of_char_dvd`, a theorem declared in [MathlibExt/NumberTheory/RamificationInertia/Tame.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/Tame.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-and-wild-ramification/index.html#is-wildly-ramified-at-of-char-dvd).

## An inseparable residue field extension forces wild ramification

Let $R$ be a
commutative ring, $S$ a commutative $R$-algebra, $q$ a prime ideal of $S$ and $p$ the preimage
of $q$ in $R$. If the residue field extension $\kappa(p) \to \kappa(q)$ is not separable, then
$q$ is wildly ramified over $R$.

Formalized by `Algebra.isWildlyRamifiedAt_of_not_isResidueSeparableAt`, a theorem declared in [MathlibExt/NumberTheory/RamificationInertia/Tame.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/Tame.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-and-wild-ramification/index.html#is-wildly-ramified-at-of-not-is-residue).

## Unramified primes are residue separable

Let $R$ and $S$ be commutative rings with $S$ an
$R$-algebra that is essentially of finite type, and let $q$ be a prime ideal of $S$ at which $S$ is
unramified over $R$, that is, the localization $S_q$ is formally unramified over $R$. Then $q$ is
residue separable over $R$.

Formalized by `Algebra.isResidueSeparableAt_of_isUnramifiedAt`, a theorem declared in [MathlibExt/NumberTheory/RamificationInertia/Tame.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/Tame.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-and-wild-ramification/index.html#is-residue-separable-at-of-is-unramified).

## Unramified primes are tamely ramified

Let $R$ and $S$ be commutative rings with $S$ an
$R$-algebra that is essentially of finite type, and let $q$ be a prime ideal of $S$ at which $S$ is
unramified over $R$, that is, the localization $S_q$ is formally unramified over $R$. Then $q$ is
tamely ramified over $R$.

Formalized by `Algebra.isTamelyRamifiedAt_of_isUnramifiedAt`, a theorem declared in [MathlibExt/NumberTheory/RamificationInertia/Tame.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/Tame.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-and-wild-ramification/index.html#is-tamely-ramified-at-of-is-unramified-a).

## Tameness in residue characteristic zero

Let $R$ and $S$ be commutative rings with $S$ an
$R$-algebra that is finite as an $R$-module, and let $q$ be a prime ideal of $S$ whose residue
field $\kappa(q)$ has characteristic $0$. Then $q$ is tamely ramified over $R$ if and only if $q$
is residue separable over $R$.

Formalized by `Algebra.isTamelyRamifiedAt_iff_isSeparable_of_charZero`, a theorem declared in [MathlibExt/NumberTheory/RamificationInertia/Tame.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/Tame.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-and-wild-ramification/index.html#is-tamely-ramified-at-iff-is-separable-o).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tame and wild ramification](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-and-wild-ramification/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/ramification/tame-and-wild-ramification)
