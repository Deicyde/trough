---
declaration: section
origin: cited
lean: arithFrobAt_eq_of_under_eq, restrictNormalHom_eq_of_isArithFrobAt
statement: formalized
proof: formalized
---

# Frobenius elements: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/index.html).

## In an abelian group the Frobenius element depends only on the prime below

Let $S$ be
a commutative algebra over a commutative ring $R$, and let a finite commutative group $G$ act on
$S$ by $R$-algebra automorphisms such that every element of $S$ fixed by $G$ is the image of an
element of $R$. For a prime $Q$ of $S$ with $S/Q$ finite, let $\mathrm{Frob}_Q \in G$ be the
chosen arithmetic Frobenius element at $Q$: an element $\sigma \in G$ with
$\sigma(x) \equiv x^q \pmod Q$ for all $x \in S$, where $q$ is the number of elements of $R$
modulo the preimage of $Q$ in $R$, chosen so that the elements chosen at primes with the same
preimage in $R$ are conjugate. If $Q$ and $Q'$ are primes of $S$ with $S/Q$ and $S/Q'$ finite
that have the same preimage in $R$, then $\mathrm{Frob}_Q = \mathrm{Frob}_{Q'}$.

Formalized by `arithFrobAt_eq_of_under_eq`, a theorem declared in [MathlibExt/RingTheory/Frobenius/Abelian.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Frobenius/Abelian.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/index.html#arith-frob-at-eq-of-under-eq).

## Restricting a Frobenius element to an intermediate field

Let $K \subseteq L \subseteq M$
be a tower of number fields with $L/K$ and $M/K$ Galois, and let $\mathcal{O}_K$,
$\mathcal{O}_L$ and $\mathcal{O}_M$ be their rings of integers. Let $Q_L$ be a prime of
$\mathcal{O}_L$ at which $\mathcal{O}_L$ is unramified over $\mathcal{O}_K$, let $Q_M$ be a
prime of $\mathcal{O}_M$ lying over $Q_L$ with $\mathcal{O}_M/Q_M$ finite, and let $q$ be the
number of elements of $\mathcal{O}_K/\mathfrak{p}$, where $\mathfrak{p}$ is the prime of
$\mathcal{O}_K$ below $Q_M$ (equivalently, below $Q_L$). If $\sigma_M \in \mathrm{Gal}(M/K)$
satisfies $\sigma_M(x) \equiv x^q \pmod{Q_M}$ for all $x \in \mathcal{O}_M$ and
$\sigma_L \in \mathrm{Gal}(L/K)$ satisfies $\sigma_L(y) \equiv y^q \pmod{Q_L}$ for all
$y \in \mathcal{O}_L$, then the restriction of $\sigma_M$ to $L$ equals $\sigma_L$.

## Sources

- ATLAS Proposition 7.13, generalized from the chosen Frobenius elements at chosen primes to arbitrary Frobenius elements at explicit primes.

Formalized by `restrictNormalHom_eq_of_isArithFrobAt`, a theorem declared in [MathlibExt/RingTheory/Frobenius/Restriction.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Frobenius/Restriction.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/index.html#restrict-normal-hom-eq-of-is-arith-frob).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Frobenius elements](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/ramification/frobenius-elements)
