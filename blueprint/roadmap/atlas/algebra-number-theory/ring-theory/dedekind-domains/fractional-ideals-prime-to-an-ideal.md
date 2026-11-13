---
declaration: section
origin: cited
lean: FractionalIdeal.nonZeroDivisors_le_comap_algebraMap_atPrime, FractionalIdeal.IsPrimeTo, FractionalIdeal.isPrimeTo_one, FractionalIdeal.IsPrimeTo.mul, FractionalIdeal.IsPrimeTo.inv_unit, FractionalIdeal.unitsPrimeTo, FractionalIdeal.mem_unitsPrimeTo_iff, FractionalIdeal.IsPrimeTo.mono
statement: formalized
proof: formalized
---

# Fractional ideals prime to an ideal

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/fractional-ideals-prime-to-an-ideal/index.html).

## Non-zero-divisors stay non-zero-divisors in a localization at a prime

Let $A$ be a
commutative ring and $\mathfrak p$ a prime ideal of $A$. Every non-zero-divisor of $A$ maps to a
non-zero-divisor of the localization $A_{\mathfrak p}$.

Formalized by `FractionalIdeal.nonZeroDivisors_le_comap_algebraMap_atPrime`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/PrimeTo.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/FractionalIdeal/PrimeTo.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/fractional-ideals-prime-to-an-ideal/index.html#non-zero-divisors-le-comap-algebra-map-a).

## Fractional ideals prime to an ideal

Let $A$ be an integral domain with fraction field
$K$, let $I$ be a fractional ideal of $A$ in $K$ and let $J$ be an ideal of $A$. Then $I$ is prime
to $J$ if for every prime ideal $\mathfrak p$ of $A$ with $J \subseteq \mathfrak p$, the extension
$I A_{\mathfrak p}$ of $I$ to the localization $A_{\mathfrak p}$, a fractional ideal of
$A_{\mathfrak p}$ in $K$, is the unit fractional ideal $A_{\mathfrak p}$.

Formalized by `FractionalIdeal.IsPrimeTo`, a definition declared in [MathlibExt/RingTheory/FractionalIdeal/PrimeTo.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/FractionalIdeal/PrimeTo.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/fractional-ideals-prime-to-an-ideal/index.html#is-prime-to).

## The unit fractional ideal is prime to every ideal

Let $A$ be an integral domain with
fraction field $K$. For every ideal $J$ of $A$, the unit fractional ideal $A$ of $A$ in $K$ is
prime to $J$.

Formalized by `FractionalIdeal.isPrimeTo_one`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/PrimeTo.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/FractionalIdeal/PrimeTo.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/fractional-ideals-prime-to-an-ideal/index.html#is-prime-to-one).

## Products of fractional ideals prime to an ideal

Let $A$ be an integral domain with
fraction field $K$ and let $J$ be an ideal of $A$. If fractional ideals $I$ and $I'$ of $A$ in $K$
are both prime to $J$, then their product $I I'$ is prime to $J$.

Formalized by `FractionalIdeal.IsPrimeTo.mul`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/PrimeTo.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/FractionalIdeal/PrimeTo.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/fractional-ideals-prime-to-an-ideal/index.html#mul).

## Inverses of invertible fractional ideals prime to an ideal

Let $A$ be an integral domain
with fraction field $K$ and let $J$ be an ideal of $A$. If an invertible fractional ideal $I$ of
$A$ in $K$ is prime to $J$, then its inverse $I^{-1}$ is prime to $J$.

Formalized by `FractionalIdeal.IsPrimeTo.inv_unit`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/PrimeTo.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/FractionalIdeal/PrimeTo.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/fractional-ideals-prime-to-an-ideal/index.html#inv-unit).

## Invertible fractional ideals prime to an ideal

Let $A$ be an integral domain with fraction
field $K$ and let $J$ be an ideal of $A$. The invertible fractional ideals of $A$ in $K$ that are
prime to $J$ form a subgroup of the group of invertible fractional ideals of $A$ in $K$.

Formalized by `FractionalIdeal.unitsPrimeTo`, a definition declared in [MathlibExt/RingTheory/FractionalIdeal/PrimeTo.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/FractionalIdeal/PrimeTo.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/fractional-ideals-prime-to-an-ideal/index.html#units-prime-to).

## Membership in the subgroup of units prime to an ideal

Let $A$ be an integral domain with
fraction field $K$ and let $J$ be an ideal of $A$. An invertible fractional ideal $I$ of $A$ in
$K$ lies in the subgroup of invertible fractional ideals prime to $J$ if and only if $I$ is prime
to $J$.

Formalized by `FractionalIdeal.mem_unitsPrimeTo_iff`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/PrimeTo.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/FractionalIdeal/PrimeTo.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/fractional-ideals-prime-to-an-ideal/index.html#mem-units-prime-to-iff).

## Prime to an ideal implies prime to every larger ideal

Let $A$ be an integral domain with
fraction field $K$, let $I$ be a fractional ideal of $A$ in $K$ and let $J \subseteq J'$ be ideals
of $A$. If $I$ is prime to $J$, then $I$ is prime to $J'$.

Formalized by `FractionalIdeal.IsPrimeTo.mono`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/PrimeTo.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/FractionalIdeal/PrimeTo.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/fractional-ideals-prime-to-an-ideal/index.html#mono).

## Monotonicity of the subgroups of units prime to an ideal

Let $A$ be an integral domain
with fraction field $K$ and let $J \subseteq J'$ be ideals of $A$. Then the subgroup of invertible
fractional ideals of $A$ in $K$ prime to $J$ is contained in the subgroup of invertible fractional
ideals of $A$ in $K$ prime to $J'$.

Formalized by `FractionalIdeal.unitsPrimeTo_mono`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/PrimeTo.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/FractionalIdeal/PrimeTo.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/fractional-ideals-prime-to-an-ideal/index.html#units-prime-to-mono).

## Every invertible fractional ideal is prime to the unit ideal

Let $A$ be an integral domain
with fraction field $K$. The subgroup of invertible fractional ideals of $A$ in $K$ prime to the
unit ideal $A$ is the whole group of invertible fractional ideals of $A$ in $K$.

Formalized by `FractionalIdeal.unitsPrimeTo_top`, a theorem declared in [MathlibExt/RingTheory/FractionalIdeal/PrimeTo.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/FractionalIdeal/PrimeTo.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/fractional-ideals-prime-to-an-ideal/index.html#units-prime-to-top).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fractional ideals prime to an ideal](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/fractional-ideals-prime-to-an-ideal/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/dedekind-domains/fractional-ideals-prime-to-an-ideal)
