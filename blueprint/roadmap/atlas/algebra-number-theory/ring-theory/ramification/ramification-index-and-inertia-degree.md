---
declaration: section
origin: cited
lean: Ideal.ramificationIdx_mem_Icc, Ideal.inertiaDeg_mem_Icc, Ideal.ncard_primesOver_mem_Icc, Ideal.ramification_inertia_card_mem_Icc, Ideal.ramification_inertia_card_mem_Icc_of_isFractionRing, IsDiscreteValuationRing.map_maximalIdeal_eq_pow_ramificationIdx, IsDiscreteValuationRing.algebraMap_mem_maximalIdeal_pow_ramificationIdx, Ideal.relNorm_eq_pow_inertiaDeg_of_isSeparable
statement: formalized
proof: formalized
---

# Ramification index and inertia degree

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/ramification-index-and-inertia-degree/index.html).

## Bounds on the ramification index

Let $R$ and $S$ be Dedekind domains, with $S$ an
$R$-algebra that is finitely generated and torsion-free as an $R$-module, and let $n$ be the rank
of $S$ as an $R$-module. If $\mathfrak{p}$ is a maximal ideal of $R$ and $\mathfrak{q}$ is a prime
ideal of $S$ lying over $\mathfrak{p}$, then the ramification index $e_{\mathfrak{q}}$ of
$\mathfrak{q}$ over $\mathfrak{p}$ satisfies $1 \le e_{\mathfrak{q}} \le n$.

## Sources

- ATLAS NumberTheoryI, Corollary 5.36 (the $e_{\mathfrak{q}}$ part).

Formalized by `Ideal.ramificationIdx_mem_Icc`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/RamificationBounds.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DedekindDomain/RamificationBounds.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/ramification-index-and-inertia-degree/index.html#ramification-idx-mem-icc).

## Bounds on the inertia degree

Let $R$ and $S$ be Dedekind domains, with $S$ an $R$-algebra
that is finitely generated and torsion-free as an $R$-module, and let $n$ be the rank of $S$ as an
$R$-module. If $\mathfrak{p}$ is a maximal ideal of $R$ and $\mathfrak{q}$ is a prime ideal of $S$
lying over $\mathfrak{p}$, then the inertia degree $f_{\mathfrak{q}}$ of $\mathfrak{q}$ over
$\mathfrak{p}$ satisfies $1 \le f_{\mathfrak{q}} \le n$.

## Sources

- ATLAS NumberTheoryI, Corollary 5.36 (the $f_{\mathfrak{q}}$ part).

Formalized by `Ideal.inertiaDeg_mem_Icc`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/RamificationBounds.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DedekindDomain/RamificationBounds.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/ramification-index-and-inertia-degree/index.html#inertia-deg-mem-icc).

## Bounds on the number of primes above a prime

Let $R$ and $S$ be Dedekind domains, with $S$
an $R$-algebra that is finitely generated and torsion-free as an $R$-module, and let $n$ be the
rank of $S$ as an $R$-module. If $\mathfrak{p}$ is a maximal ideal of $R$, then the number
$g_{\mathfrak{p}}$ of prime ideals of $S$ lying over $\mathfrak{p}$ satisfies
$1 \le g_{\mathfrak{p}} \le n$.

## Sources

- ATLAS NumberTheoryI, Corollary 5.36 (the $g_{\mathfrak{p}}$ part).

Formalized by `Ideal.ncard_primesOver_mem_Icc`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/RamificationBounds.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DedekindDomain/RamificationBounds.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/ramification-index-and-inertia-degree/index.html#ncard-primes-over-mem-icc).

## Bounds on ramification, inertia and splitting

Let $R$ and $S$ be Dedekind domains, with
$S$ an $R$-algebra that is finitely generated and torsion-free as an $R$-module, and let $n$ be the
rank of $S$ as an $R$-module. If $\mathfrak{p}$ is a maximal ideal of $R$ and $\mathfrak{q}$ is a
prime ideal of $S$ lying over $\mathfrak{p}$, then the ramification index $e_{\mathfrak{q}}$ and
the inertia degree $f_{\mathfrak{q}}$ of $\mathfrak{q}$ over $\mathfrak{p}$ and the number
$g_{\mathfrak{p}}$ of prime ideals of $S$ lying over $\mathfrak{p}$ all lie in the interval
$[1, n]$.

## Sources

- ATLAS NumberTheoryI, Corollary 5.36.

Formalized by `Ideal.ramification_inertia_card_mem_Icc`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/RamificationBounds.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DedekindDomain/RamificationBounds.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/ramification-index-and-inertia-degree/index.html#ramification-inertia-card-mem-icc).

## Bounds on ramification, inertia and splitting, fraction-field form

Let $R$ and $S$ be
Dedekind domains, with $S$ an $R$-algebra that is finitely generated and torsion-free as an
$R$-module. Let $K$ be the fraction field of $R$ and $L$ the fraction field of $S$, with $L$ a
$K$-algebra compatible with the maps $R \to K \to L$ and $R \to S \to L$, and let $n = [L : K]$.
If $\mathfrak{p}$ is a maximal ideal of $R$ and $\mathfrak{q}$ is a prime ideal of $S$ lying over
$\mathfrak{p}$, then the ramification index $e_{\mathfrak{q}}$ and the inertia degree
$f_{\mathfrak{q}}$ of $\mathfrak{q}$ over $\mathfrak{p}$ and the number $g_{\mathfrak{p}}$ of prime
ideals of $S$ lying over $\mathfrak{p}$ all lie in the interval $[1, n]$.

## Sources

- ATLAS NumberTheoryI, Corollary 5.36.

Formalized by `Ideal.ramification_inertia_card_mem_Icc_of_isFractionRing`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/RamificationBounds.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DedekindDomain/RamificationBounds.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/ramification-index-and-inertia-degree/index.html#ramification-inertia-card-mem-icc-of-is).

## The extended maximal ideal is a power of the maximal ideal

Let $A$ and $B$ be discrete
valuation rings with maximal ideals $\mathfrak m_A$, $\mathfrak m_B$, and let $B$ be an
$A$-algebra that is torsion-free as an $A$-module and whose structure map is a local
homomorphism. Let $e$ be the ramification index of $\mathfrak m_B$ over $A$. Then the ideal
$\mathfrak m_A B$ of $B$ generated by the image of $\mathfrak m_A$ equals $\mathfrak m_B^e$.

Formalized by `IsDiscreteValuationRing.map_maximalIdeal_eq_pow_ramificationIdx`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/RamificationFiltration.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DiscreteValuationRing/RamificationFiltration.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/ramification-index-and-inertia-degree/index.html#map-maximal-ideal-eq-pow-ramification-id).

## Images of the base maximal ideal lie in the ramification power

Let $A$ and $B$ be
discrete valuation rings with maximal ideals $\mathfrak m_A$, $\mathfrak m_B$, and let $B$ be an
$A$-algebra that is torsion-free as an $A$-module and whose structure map is a local
homomorphism. Let $e$ be the ramification index of $\mathfrak m_B$ over $A$. Then for every
$x \in \mathfrak m_A$, the image of $x$ in $B$ lies in $\mathfrak m_B^e$.

Formalized by `IsDiscreteValuationRing.algebraMap_mem_maximalIdeal_pow_ramificationIdx`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/RamificationFiltration.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DiscreteValuationRing/RamificationFiltration.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/ramification-index-and-inertia-degree/index.html#algebra-map-mem-maximal-ideal-pow-ramifi).

## Relative norm is the base prime to the inertia degree, separable case

Theorem 6.10 of ATLAS `NumberTheoryI`, in the separable (rather than Galois
or perfect-field) form: the relative norm of a maximal ideal lying over a maximal
ideal is the base prime raised to the inertia degree.

Formalized by `Ideal.relNorm_eq_pow_inertiaDeg_of_isSeparable`, a theorem declared in [MathlibExt/RingTheory/Ideal/Norm/RelNormSeparable.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Ideal/Norm/RelNormSeparable.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/ramification-index-and-inertia-degree/index.html#rel-norm-eq-pow-inertia-deg-of-is-separa).

## Multiplicity of the maximal ideal equals the additive valuation

Let $R$ be a discrete
valuation ring with maximal ideal $\mathfrak{m}$ and normalized additive valuation
$v \colon R \to \mathbb{N} \cup \{\infty\}$. For every $x \in R$, the multiplicity of
$\mathfrak{m}$ in the principal ideal $(x)$, that is, the supremum in $\mathbb{N} \cup \{\infty\}$
of the $n \in \mathbb{N}$ such that $\mathfrak{m}^n$ divides $(x)$ as ideals, equals $v(x)$.

Formalized by `IsDiscreteValuationRing.emultiplicity_maximalIdeal_span_eq_addVal`, a theorem declared in [MathlibExt/RingTheory/RamificationInertia/Valuation.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/RamificationInertia/Valuation.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/ramification-index-and-inertia-degree/index.html#emultiplicity-maximal-ideal-span-eq-add).

## Additive valuations scale by the ramification index

Let $A$ and $B$ be discrete
valuation rings, and let $B$ be an $A$-algebra that is torsion-free as an $A$-module and whose
structure map $\varphi \colon A \to B$ is a local homomorphism. Let $v_A$ and $v_B$ be the
normalized additive valuations of $A$ and $B$, with values in $\mathbb{N} \cup \{\infty\}$, and
let $e$ be the ramification index of the maximal ideal of $B$ over $A$. Then
$v_B(\varphi(x)) = e \cdot v_A(x)$ for every $x \in A$.

Formalized by `IsDiscreteValuationRing.addVal_algebraMap_eq_ramificationIdx_mul`, a theorem declared in [MathlibExt/RingTheory/RamificationInertia/Valuation.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/RamificationInertia/Valuation.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/ramification-index-and-inertia-degree/index.html#add-val-algebra-map-eq-ramification-idx).

## Natural numbers that are units in a local ring

Let $R$ be a commutative local ring and
let $p$ be the characteristic of its residue field. For every natural number $n$, the image of
$n$ in $R$ is a unit if and only if $p$ does not divide $n$.

Formalized by `IsLocalRing.isUnit_natCast_iff_ringChar_not_dvd`, a theorem declared in [MathlibExt/RingTheory/RamificationInertia/Valuation.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/RamificationInertia/Valuation.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/ramification-index-and-inertia-degree/index.html#is-unit-nat-cast-iff-ring-char-not-dvd).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ramification index and inertia degree](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/ramification-index-and-inertia-degree/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/ramification/ramification-index-and-inertia-degree)
