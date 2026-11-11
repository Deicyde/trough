---
declaration: section
origin: cited
lean: ValuationBijection.extendsValuation, ValuationBijection.primesAbove, ValuationBijection.mem_of_liesOver, ValuationBijection.valuation_extends_of_liesOver, ValuationBijection.dvr_overring_equiv, ValuationBijection.valuation_surjective_of_extends, ValuationBijection.extending_valuation_bijection_primes_above
statement: formalized
proof: formalized
---

# Extensions of valuations above a prime

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/extensions-of-valuations-above-a-prime/index.html).

## Valuations extending a prime-adic valuation

Let $A$ be a Dedekind domain with fraction
field $K$, let $L$ be a field extension of $K$, and let $\mathfrak{p}$ be a height-one prime of $A$.
A valuation $w$ on $L$ with values in the multiplicative group $\mathbb{Z}$ with a zero adjoined
extends the $\mathfrak{p}$-adic valuation of $K$ when its restriction to $K$ is equivalent to the
$\mathfrak{p}$-adic valuation of $K$.

This relation does not record an extension index or a normalization.

Formalized by `ValuationBijection.extendsValuation`, a definition declared in [MathlibExt/RingTheory/DedekindDomain/ValuationBijection.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/ValuationBijection.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/extensions-of-valuations-above-a-prime/index.html#extends-valuation).

## Height-one primes above a prime

Let $A$ and $B$ be Dedekind domains with $B$ an
$A$-algebra, and let $\mathfrak{p}$ be a height-one prime of $A$. The primes above $\mathfrak{p}$
form the set of height-one primes $\mathfrak{q}$ of $B$ lying over $\mathfrak{p}$, that is, whose
preimage in $A$ is $\mathfrak{p}$.

Formalized by `ValuationBijection.primesAbove`, a definition declared in [MathlibExt/RingTheory/DedekindDomain/ValuationBijection.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/ValuationBijection.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/extensions-of-valuations-above-a-prime/index.html#primes-above).

## Membership in a prime is detected by a prime lying over it

Let $A$ and $B$ be Dedekind
domains with $B$ an $A$-algebra, let $\mathfrak{p}$ be a height-one prime of $A$, and let
$\mathfrak{q}$ be a height-one prime of $B$ lying over $\mathfrak{p}$. Then for every $a \in A$,
$a \in \mathfrak{p}$ if and only if the image of $a$ in $B$ lies in $\mathfrak{q}$.

Formalized by `ValuationBijection.mem_of_liesOver`, a lemma declared in [MathlibExt/RingTheory/DedekindDomain/ValuationBijection.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/ValuationBijection.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/extensions-of-valuations-above-a-prime/index.html#mem-of-lies-over).

## The adic valuation of a prime lying over extends the adic valuation below

Let $A$ be a
Dedekind domain with fraction field $K$, let $L$ be a finite separable extension of $K$, and let
$B$ be a Dedekind domain that is the integral closure of $A$ in $L$ and has fraction field $L$.
If $\mathfrak{q}$ is a height-one prime of $B$ lying over a height-one prime $\mathfrak{p}$ of
$A$, then the $\mathfrak{q}$-adic valuation of $L$ extends the $\mathfrak{p}$-adic valuation of
$K$: its restriction to $K$ is equivalent to the $\mathfrak{p}$-adic valuation of $K$.

Formalized by `ValuationBijection.valuation_extends_of_liesOver`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/ValuationBijection.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/ValuationBijection.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/extensions-of-valuations-above-a-prime/index.html#valuation-extends-of-lies-over).

## A valuation centered at a height-one prime is equivalent to its adic valuation

Let $B$ be
a Dedekind domain with fraction field $L$, let $\mathfrak{q}$ be a height-one prime of $B$, and let
$w$ be a valuation on $L$ with values in the multiplicative group $\mathbb{Z}$ with a zero adjoined.
Suppose that $w(b) \le 1$ for every $b \in B$, and that for every $b \in B$ we have
$b \in \mathfrak{q}$ if and only if $w(b) < 1$. Then the $\mathfrak{q}$-adic valuation of $L$ is
equivalent to $w$.

Formalized by `ValuationBijection.dvr_overring_equiv`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/ValuationBijection.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/ValuationBijection.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/extensions-of-valuations-above-a-prime/index.html#dvr-overring-equiv).

## Each extension of a prime-adic valuation comes from some prime above

Let $A$ be a
Dedekind domain with fraction field $K$, let $L$ be a finite separable extension of $K$, and let
$B$ be a Dedekind domain that is the integral closure of $A$ in $L$ and has fraction field $L$.
Let $\mathfrak{p}$ be a height-one prime of $A$, and let $w$ be a valuation on $L$ with values in
the multiplicative group $\mathbb{Z}$ with a zero adjoined whose restriction to $K$ is equivalent
to the $\mathfrak{p}$-adic valuation of $K$. Then there is a height-one prime $\mathfrak{q}$ of $B$
lying over $\mathfrak{p}$ such that the $\mathfrak{q}$-adic valuation of $L$ is equivalent
to $w$.

Formalized by `ValuationBijection.valuation_surjective_of_extends`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/ValuationBijection.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/ValuationBijection.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/extensions-of-valuations-above-a-prime/index.html#valuation-surjective-of-extends).

## Each extension of a prime-adic valuation comes from exactly one prime above

Let $A$ be a
Dedekind domain with fraction field $K$, let $L$ be a finite separable extension of $K$, and let
$B$ be a Dedekind domain that is the integral closure of $A$ in $L$ and has fraction field $L$.
Let $\mathfrak{p}$ be a height-one prime of $A$, and consider valuations on $L$ with values in the
multiplicative group $\mathbb{Z}$ with a zero adjoined. Then (1) if $\mathfrak{q}_1$ and
$\mathfrak{q}_2$ are height-one primes of $B$ lying over $\mathfrak{p}$ whose adic valuations on
$L$ are equivalent, then $\mathfrak{q}_1 = \mathfrak{q}_2$; and (2) every such valuation $w$ on $L$
whose restriction to $K$ is equivalent to the $\mathfrak{p}$-adic valuation of $K$ is equivalent
to the $\mathfrak{q}$-adic valuation of $L$ for some height-one prime $\mathfrak{q}$ of $B$ lying
over $\mathfrak{p}$.

Valuations are compared only up to equivalence; no normalization or ramification index is
asserted.

Formalized by `ValuationBijection.extending_valuation_bijection_primes_above`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/ValuationBijection.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/ValuationBijection.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/extensions-of-valuations-above-a-prime/index.html#extending-valuation-bijection-primes-abo).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Extensions of valuations above a prime](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/extensions-of-valuations-above-a-prime/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/ramification/extensions-of-valuations-above-a-prime)
