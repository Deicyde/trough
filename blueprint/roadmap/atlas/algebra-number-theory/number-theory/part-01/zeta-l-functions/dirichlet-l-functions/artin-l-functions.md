---
declaration: section
origin: cited
lean: Representation.ArtinLocalDatum, Representation.artinLocalDenominator, Representation.ArtinLocalFactorRegular, Representation.artinLocalFactorRaw, Representation.artinEulerProductOfLocalData, Representation.HasArtinEulerProduct, Representation.HasNonzeroArtinEulerProduct, Representation.artinLocalFactorRaw_of_action_eq_id_general
statement: formalized
proof: formalized
---

# Artin L-functions

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/artin-l-functions/index.html).

## Artin local datum

For a finite group $G$, an Artin local datum consists of a subgroup
$D \le G$ (the decomposition group), a normal subgroup $I$ of $D$ (the inertia group), and an
element $\sigma$ of the quotient group $D/I$ (the Frobenius coset).

In the arithmetic application, $L/\mathbb{Q}$ is a finite Galois extension with
$G = \mathrm{Gal}(L/\mathbb{Q})$, $D$ is the decomposition group at a place $w$ of $L$ above a
prime $p$, $I$ is its inertia group and $\sigma$ is the Frobenius. A complex representation of
$G$ restricted to $D$ then gives an action of $D/I$ on the $I$-invariant vectors, on which
$\sigma$ acts as the local operator. The definition does not require the data to arise this way.

Formalized by `Representation.ArtinLocalDatum`, a structure declared in [MathlibExt/NumberTheory/LSeries/Artin.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/Artin.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/artin-l-functions/index.html#artin-local-datum).

## Artin local denominator

Let $\rho$ be a representation of a finite group $G$ on a
finite-dimensional complex vector space $V$, let $p$ be a prime, let $(D, I, \sigma)$ be an Artin
local datum for $G$, and let $s \in \mathbb{C}$. Let $V^{I}$ be the subspace of vectors fixed by
$\rho(I)$, on which $D/I$ acts, and let $\rho(\sigma)$ be the action of $\sigma$ on $V^{I}$. The
Artin local denominator is

$$\det\left(\mathrm{id} - p^{-s}\,\rho(\sigma) \mid V^{I}\right).$$

Formalized by `Representation.artinLocalDenominator`, a definition declared in [MathlibExt/NumberTheory/LSeries/Artin.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/Artin.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/artin-l-functions/index.html#artin-local-denominator).

## Regularity of the Artin local factor

Let $\rho$ be a representation of a finite group $G$
on a finite-dimensional complex vector space $V$, let $p$ be a prime, let $d$ be an Artin local
datum for $G$, and let $s \in \mathbb{C}$. The Artin local factor of $\rho$ at $p$, $d$ is regular
at $s$ when the Artin local denominator of $\rho$ at $p$, $d$ and $s$ is nonzero, that is, when
the local factor has no pole at $s$.

Formalized by `Representation.ArtinLocalFactorRegular`, a definition declared in [MathlibExt/NumberTheory/LSeries/Artin.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/Artin.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/artin-l-functions/index.html#artin-local-factor-regular).

## Artin local factor

Let $\rho$ be a representation of a finite group $G$ on a
finite-dimensional complex vector space $V$, let $p$ be a prime, let $(D, I, \sigma)$ be an Artin
local datum for $G$, and let $s \in \mathbb{C}$. Let $V^{I}$ be the subspace of vectors fixed by
$\rho(I)$ and $\rho(\sigma)$ the induced action of $\sigma \in D/I$ on it. The Artin local factor
is the inverse of the Artin local denominator,

$$\det\left(\mathrm{id} - p^{-s}\,\rho(\sigma) \mid V^{I}\right)^{-1},$$

with the value $0$ when the denominator vanishes.

Where the denominator vanishes the true factor has a pole; the regularity condition picks out
the $s$ at which this value is a genuine finite Euler factor.

Formalized by `Representation.artinLocalFactorRaw`, a definition declared in [MathlibExt/NumberTheory/LSeries/Artin.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/Artin.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/artin-l-functions/index.html#artin-local-factor-raw).

## Euler product of Artin local factors

Let $\rho$ be a representation of a finite group
$G$ on a finite-dimensional complex vector space $V$, and suppose that for every prime $p$ an Artin
local datum $d_p$ for $G$ is given. For $s \in \mathbb{C}$, this is the product over all primes
$p$ of the Artin local factors of $\rho$ at $p$, $d_p$ and $s$, taken as an unconditional infinite
product (the limit of the products over finite sets of primes); when this product does not
converge, the value is $1$ by convention.

The data need not come from the places of a number field, and no independence of the choice of
place above $p$ is asserted.

Formalized by `Representation.artinEulerProductOfLocalData`, a definition declared in [MathlibExt/NumberTheory/LSeries/Artin.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/Artin.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/artin-l-functions/index.html#artin-euler-product-of-local-data).

## Convergent Artin Euler product

Let $\rho$ be a representation of a finite group $G$ on a
finite-dimensional complex vector space $V$, let $d_p$ be an Artin local datum for $G$ for every
prime $p$, and let $s, z \in \mathbb{C}$. The Artin Euler product of $\rho$ and $(d_p)$ has value
$z$ at $s$ when the products of the Artin local factors of $\rho$ at $p$, $d_p$ and $s$ over
finite sets of primes $p$ converge to $z$ as the finite set grows to all primes (unconditional
convergence). The value $z = 0$ is allowed.

Formalized by `Representation.HasArtinEulerProduct`, a definition declared in [MathlibExt/NumberTheory/LSeries/Artin.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/Artin.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/artin-l-functions/index.html#has-artin-euler-product).

## Nonzero convergent Artin Euler product

Let $\rho$ be a representation of a finite group
$G$ on a finite-dimensional complex vector space $V$, let $d_p$ be an Artin local datum for $G$ for
every prime $p$, and let $s, z \in \mathbb{C}$. The Artin Euler product of $\rho$ and $(d_p)$ has
nonzero value $z$ at $s$ when it has value $z$ at $s$ and $z \ne 0$.

In particular every local factor is then regular at $s$: a factor whose denominator vanishes has
value $0$ and would force the product to be $0$, so this describes a genuine finite Euler-product
value rather than a pole.

Formalized by `Representation.HasNonzeroArtinEulerProduct`, a definition declared in [MathlibExt/NumberTheory/LSeries/Artin.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/Artin.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/artin-l-functions/index.html#has-nonzero-artin-euler-product).

## Artin local factor when Frobenius acts trivially

Let $\rho$ be a representation of a
finite group $G$ on a finite-dimensional complex vector space $V$, let $p$ be a prime, let
$(D, I, \sigma)$ be an Artin local datum for $G$, and let $s \in \mathbb{C}$. Let $V^{I}$ be the
subspace of vectors fixed by $\rho(I)$ and $n = \dim V^{I}$. If $\sigma$ acts as the identity on
$V^{I}$, then the Artin local factor of $\rho$ at $p$, $(D, I, \sigma)$ and $s$ equals
$\left((1 - p^{-s})^{n}\right)^{-1}$, where the inverse of $0$ is read as $0$.

Formalized by `Representation.artinLocalFactorRaw_of_action_eq_id_general`, a theorem declared in [MathlibExt/NumberTheory/LSeries/Artin.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/Artin.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/artin-l-functions/index.html#artin-local-factor-raw-of-action-eq-id-g).

## Artin local factor of a one-dimensional trivial Frobenius action

Let $\rho$ be a
representation of a finite group $G$ on a finite-dimensional complex vector space $V$, let $p$ be
a prime, let $(D, I, \sigma)$ be an Artin local datum for $G$, and let $s \in \mathbb{C}$. Let
$V^{I}$ be the subspace of vectors fixed by $\rho(I)$. If $\sigma$ acts as the identity on $V^{I}$
and $V^{I}$ is one-dimensional, then the Artin local factor of $\rho$ at $p$, $(D, I, \sigma)$
and $s$ equals $(1 - p^{-s})^{-1}$, where the inverse of $0$ is read as $0$.

This is the unramified trivial-character case, which gives the local factor of the Riemann zeta
function.

Formalized by `Representation.artinLocalFactorRaw_of_action_eq_id`, a theorem declared in [MathlibExt/NumberTheory/LSeries/Artin.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/Artin.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/artin-l-functions/index.html#artin-local-factor-raw-of-action-eq-id).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Artin L-functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/artin-l-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/artin-l-functions)
