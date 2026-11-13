---
declaration: section
origin: cited
lean: IsDiscreteValuationRing.isAdicComplete_of_finite_local_extension, Ideal.comap_eq_base_maximal_of_isAdicComplete_of_isIntegral, isLocalRing_of_isIntegral_of_isAdicComplete_maximal, IsIntegralClosure.isLocalRing_of_isAdicComplete, IsIntegralClosure.isDiscreteValuationRing_of_isAdicComplete, IsIntegralClosure.isAdicComplete_of_isAdicComplete, IsIntegralClosure.existsUnique_primesOver_maximalIdeal_of_isAdicComplete, Valuation.integer_isIntegralClosure_of_isAdicComplete
statement: formalized
proof: formalized
---

# Finite extensions of complete discrete valuation rings

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/finite-extensions-of-complete-discrete-valuation/index.html).

## Completeness passes to finite extensions of discrete valuation rings

Let $A$ and $B$ be
discrete valuation rings, and let $B$ be an $A$-algebra that is finitely generated as an
$A$-module and whose structure map $A \to B$ is injective. If $A$ is complete and Hausdorff for
the adic topology of its maximal ideal, then $B$ is complete and Hausdorff for the adic topology
of its maximal ideal.

## Sources

- generalizes `integral_closure_isAdicComplete` (atlas-lean v1) from the integral closure to any finite faithful extension of DVRs.

Formalized by `IsDiscreteValuationRing.isAdicComplete_of_finite_local_extension`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/FiniteExtensionComplete.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DiscreteValuationRing/FiniteExtensionComplete.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/finite-extensions-of-complete-discrete-valuation/index.html#is-adic-complete-of-finite-local-extensi).

## Maximal ideals contract to the maximal ideal of a complete base

Let $A$ and $B$ be
commutative rings with $B$ an $A$-algebra that is integral over $A$, and let $\mathfrak p$ be a
maximal ideal of $A$ such that $A$ is $\mathfrak p$-adically complete. Then every maximal ideal
$Q$ of $B$ has preimage $\mathfrak p$ under the structure map $A \to B$.

Formalized by `Ideal.comap_eq_base_maximal_of_isAdicComplete_of_isIntegral`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/IntegralClosureComplete.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DiscreteValuationRing/IntegralClosureComplete.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/finite-extensions-of-complete-discrete-valuation/index.html#comap-eq-base-maximal-of-is-adic-complet).

## Domains integral over a complete local domain are local

Let $A$ be an integral domain
and $\mathfrak p$ a maximal ideal of $A$ such that $A$ is $\mathfrak p$-adically complete. If $B$
is an integral domain and an $A$-algebra that is integral over $A$, then $B$ is a local ring.

Formalized by `isLocalRing_of_isIntegral_of_isAdicComplete_maximal`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/IntegralClosureComplete.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DiscreteValuationRing/IntegralClosureComplete.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/finite-extensions-of-complete-discrete-valuation/index.html#is-local-ring-of-is-integral-of-is-adic).

## The integral closure of a complete DVR is local

Let $A$ be a discrete valuation ring
that is complete with respect to its maximal ideal, $K$ its fraction field and $L$ a finite
separable extension of $K$. Then the integral closure of $A$ in $L$ is a local ring.

Formalized by `IsIntegralClosure.isLocalRing_of_isAdicComplete`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/IntegralClosureComplete.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DiscreteValuationRing/IntegralClosureComplete.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/finite-extensions-of-complete-discrete-valuation/index.html#is-local-ring-of-is-adic-complete).

## The integral closure of a complete DVR is a DVR

Let $A$ be a discrete valuation ring
that is complete with respect to its maximal ideal, $K$ its fraction field and $L$ a finite
separable extension of $K$. Then the integral closure of $A$ in $L$ is a discrete valuation
ring.

Formalized by `IsIntegralClosure.isDiscreteValuationRing_of_isAdicComplete`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/IntegralClosureComplete.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DiscreteValuationRing/IntegralClosureComplete.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/finite-extensions-of-complete-discrete-valuation/index.html#is-discrete-valuation-ring-of-is-adic-co).

## The integral closure of a complete DVR is complete

Let $A$ be a discrete valuation ring
that is complete with respect to its maximal ideal, $K$ its fraction field, $L$ a finite separable
extension of $K$, and $B$ the integral closure of $A$ in $L$. If $B$ is local (as it always is
here), then $B$ is complete with respect to its maximal ideal.

## Sources

- ATLAS `integral_closure_isAdicComplete`, obtained here from the general completeness theorem for finite local extensions.

Formalized by `IsIntegralClosure.isAdicComplete_of_isAdicComplete`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/IntegralClosureComplete.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DiscreteValuationRing/IntegralClosureComplete.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/finite-extensions-of-complete-discrete-valuation/index.html#is-adic-complete-of-is-adic-complete).

## Exactly one prime lies over the maximal ideal of a complete DVR

Let $A$ be a discrete
valuation ring that is complete with respect to its maximal ideal $\mathfrak m$, $K$ its fraction
field, $L$ a finite separable extension of $K$, and $B$ the integral closure of $A$ in $L$. Then
there is exactly one prime ideal of $B$ whose preimage under $A \to B$ is $\mathfrak m$.

Formalized by `IsIntegralClosure.existsUnique_primesOver_maximalIdeal_of_isAdicComplete`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/IntegralClosureComplete.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DiscreteValuationRing/IntegralClosureComplete.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/finite-extensions-of-complete-discrete-valuation/index.html#exists-unique-primes-over-maximal-ideal).

## Valuation rings dominating a complete DVR are integral closures

Let $A$ be a discrete
valuation ring that is complete with respect to its maximal ideal, $K$ its fraction field, and
$L$ a finite separable extension of $K$. Let $v$ be a valuation on $L$ with values in a linearly
ordered commutative group with zero, with valuation ring $\mathcal O_v = \{x \in L : v(x) \le 1\}$.
Suppose $\mathcal O_v$ is an $A$-algebra such that the composite $A \to \mathcal O_v \subseteq L$
is the structure map $A \to L$, and $A \to \mathcal O_v$ is a local homomorphism. Then
$\mathcal O_v$ is the integral closure of $A$ in $L$.

Formalized by `Valuation.integer_isIntegralClosure_of_isAdicComplete`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/IntegralClosureComplete.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DiscreteValuationRing/IntegralClosureComplete.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/finite-extensions-of-complete-discrete-valuation/index.html#integer-is-integral-closure-of-is-adic-c).

## Valuation rings dominating a complete DVR are finite over it

Let $A$ be a discrete
valuation ring that is complete with respect to its maximal ideal, $K$ its fraction field, and
$L$ a finite separable extension of $K$. Let $v$ be a valuation on $L$ with values in a linearly
ordered commutative group with zero, with valuation ring $\mathcal O_v = \{x \in L : v(x) \le 1\}$.
Suppose $\mathcal O_v$ is an $A$-algebra such that the composite $A \to \mathcal O_v \subseteq L$
is the structure map $A \to L$, and $A \to \mathcal O_v$ is a local homomorphism. Then
$\mathcal O_v$ is a finitely generated $A$-module.

Formalized by `Valuation.module_finite_integer_of_isAdicComplete`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/IntegralClosureComplete.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DiscreteValuationRing/IntegralClosureComplete.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/finite-extensions-of-complete-discrete-valuation/index.html#module-finite-integer-of-is-adic-complet).

## Integral closure of a complete DVR in a separable extension

The integral closure of a complete discrete valuation ring in a finite
separable extension of its fraction field is finite over the base, is a
discrete valuation ring, and is complete for its maximal ideal.

Formalized by `integralClosure.finite_and_isDiscreteValuationRing_and_isAdicComplete_maximalIdeal`, a theorem declared in [MathlibExt/RingTheory/IntegralClosure/DVR.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/IntegralClosure/DVR.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/finite-extensions-of-complete-discrete-valuation/index.html#finite-and-is-discrete-valuation-ring-an).

## Finite domains over adically complete local rings are local

A finite algebra over an adically complete Noetherian local ring that is
a domain is itself local.

Formalized by `IsLocalRing.of_isDomain_of_module_finite_of_isAdicComplete`, a theorem declared in [MathlibExt/RingTheory/LocalRing/AdicCompleteDomain.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/LocalRing/AdicCompleteDomain.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/finite-extensions-of-complete-discrete-valuation/index.html#of-is-domain-of-module-finite-of-is-adic).

## Finitely many DVR points with trivial common kernel

A finite torsion-free local reduced algebra over an adically complete DVR
with finite residue field and characteristic zero admits finitely many
adically complete DVR points whose kernels intersect to `⊥`, with a common
denominator clearing all denominators.

Formalized by `IsLocalRing.exists_fin_points_dvr_iInf_ker_eq_bot`, a theorem declared in [MathlibExt/RingTheory/LocalRing/DVRPoints.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/LocalRing/DVRPoints.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/finite-extensions-of-complete-discrete-valuation/index.html#exists-fin-points-dvr-i-inf-ker-eq-bot).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite extensions of complete discrete valuation rings](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/finite-extensions-of-complete-discrete-valuation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/valuation-rings/finite-extensions-of-complete-discrete-valuation)
