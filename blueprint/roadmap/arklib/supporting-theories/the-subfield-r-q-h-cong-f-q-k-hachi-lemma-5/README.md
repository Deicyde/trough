# The Subfield $R_q^H \cong \mathbb{F}_{q^k}$ (Hachi Lemma 5)

This section covers Hachi ([Nguyen et al. 2026](https://eprint.iacr.org/2026/156)) §3, Lemma 5: the fixed subring $R_q^H$ is a *field* and is isomorphic to $\mathbb{F}_{q^k}$. The packing map $\psi$ and the trace formula of Theorem 2 (the rest of §3) are formalized as well.

Throughout, $d = 2^\alpha$, $R_q = \mathbb{Z}_q[X]/(X^{d}+1)$ with $q$ an odd prime, $k = 2^\kappa$ a divisor of $d/2$ (i.e. $2k \mid d$), and $H = \langle \sigma_{-1}, \sigma_{4k+1}\rangle$. For the field statement we additionally assume $q \equiv 5 \pmod 8$.

## The fixed subring and the packing map

- [Fixed subring](def-fixedsubring.md)
- [Cardinality, Eq. 7](thm-card-fixedsubring.md)
- [Packing bijection, Theorem 2](thm-psi-bijective.md)

The rest of the section establishes the field structure.

## Main result

- [Lemma 5: field isomorphism](thm-fixedsubring-equiv-galoisfield.md)

The point of this decomposition is that *the cardinality is already known* (Theorem [Cardinality, Eq. 7](thm-card-fixedsubring.md)), so once field-ness is established we get the isomorphism *without* any finite-field Galois-descent analysis of the $\sigma_{4k+1}$-action.

## Reduction to “$R_q^H$ is a field”

The whole difficulty concentrates in field-ness; everything else is generic algebra reused from Mathlib.

- [$R_q^H$ is a field](thm-fixedsubring-isfield.md)
- [Conjugation-fixed subring $R_q^{\sigma_{-1}}$](def-conjfixedsubring.md)
- [$R_q^H \le R_q^{\sigma_{-1}}$](lem-fixedsubring-le-conjfixedsubring.md)

## The crux: $R_q^{\sigma_{-1}}$ is a field

This is the only genuinely new mathematics. The route is the *two-factor* decomposition of $R_q$ that is special to $q \equiv 5 \pmod 8$.

- [Order of $q$ modulo the conductor](lem-order-q.md)
- [Two irreducible factors](lem-two-factors.md)
- [Factor existence](lem-factorization.md)

## The swap: $\sigma_{-1}$ and polynomial reversal

The proof rests on one fact: $\sigma_{-1}$ interchanges the two factors. Rather than build the explicit CRT product $K \times K$, we work directly in $S := \mathbb{F}_q[X]/(X^{2^\alpha}+1)$ via a *reverse identity* and a divisibility argument.

- [The reverse identity](lem-conj-reverse.md)
- [No self-reciprocal factor](lem-no-selfreciprocal.md)
- [$-1 \notin \langle q\rangle$](lem-neg-one-notmem.md)

## Assembling the field and the isomorphism

- [Core unit lemma](thm-core-unit.md)
- [$R_q^{\sigma_{-1}}$ is a field](thm-conjfixedsubring-isfield.md)

The proof works directly in $S$ via the reverse identity and a divisibility argument, rather than constructing the explicit CRT product $R_q \cong K\times K$.
