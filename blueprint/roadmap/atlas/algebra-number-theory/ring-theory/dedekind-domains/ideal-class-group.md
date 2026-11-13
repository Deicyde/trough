---
declaration: section
origin: cited
lean: Ideal.exists_isCoprime_mul_isPrincipal, ClassGroup.exists_mk0_eq_and_isCoprime, IdealFactorization.IdealsSimilar, IsDedekindDomain.uniqueFactorizationMonoid_iff_isPrincipalIdealRing, IsDedekindDomain.isPrincipalIdealRing_iff_subsingleton_classGroup, IsDedekindDomain.uniqueFactorizationMonoid_iff_subsingleton_classGroup
statement: formalized
proof: formalized
---

# Ideal class group

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/ideal-class-group/index.html).

## Making an ideal principal with a factor coprime to a given ideal

Let $A$ be a
Dedekind domain and let $I$ and $\mathfrak{a}$ be nonzero ideals of $A$. Then there is an
ideal $J$ of $A$ with $J + \mathfrak{a} = A$ such that the product $IJ$ is a principal
ideal.

Formalized by `Ideal.exists_isCoprime_mul_isPrincipal`, a theorem declared in [MathlibExt/RingTheory/ClassGroup/CoprimeRepresentative.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/ClassGroup/CoprimeRepresentative.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/ideal-class-group/index.html#exists-is-coprime-mul-is-principal).

## Ideal classes have representatives coprime to a given ideal

Let $A$ be a
Dedekind domain and let $\mathfrak{a}$ be a nonzero ideal of $A$. Then every class $c$ in the
ideal class group of $A$ is the class of some nonzero ideal $K$ of $A$ with
$K + \mathfrak{a} = A$.

Formalized by `ClassGroup.exists_mk0_eq_and_isCoprime`, a theorem declared in [MathlibExt/RingTheory/ClassGroup/CoprimeRepresentative.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/ClassGroup/CoprimeRepresentative.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/ideal-class-group/index.html#exists-mk0-eq-and-is-coprime).

## Similar ideals

Let $R$ be a Dedekind domain. Two nonzero ideals $I$ and $J$ of $R$ are
similar when their classes in the ideal class group of $R$ are equal.

Formalized by `IdealFactorization.IdealsSimilar`, an abbreviation declared in [MathlibExt/RingTheory/ClassGroup/IdealSimilarity.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/ClassGroup/IdealSimilarity.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/ideal-class-group/index.html#ideals-similar).

## Dedekind domains: UFD iff PID

A Dedekind domain $R$ is a unique factorization domain if
and only if it is a principal ideal domain.

## Sources

- ATLAS NumberTheoryI, Section 3.2, Corollary 3.15 (first equivalence).

Formalized by `IsDedekindDomain.uniqueFactorizationMonoid_iff_isPrincipalIdealRing`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/UFD_iff_PID.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DedekindDomain/UFD_iff_PID.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/ideal-class-group/index.html#unique-factorization-monoid-iff-is-princ).

## Dedekind domains: PID iff trivial class group

A Dedekind domain $R$ is a principal ideal
domain if and only if its ideal class group is trivial.

## Sources

- ATLAS NumberTheoryI, Section 3.2, Corollary 3.15 (second equivalence).

Formalized by `IsDedekindDomain.isPrincipalIdealRing_iff_subsingleton_classGroup`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/UFD_iff_PID.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DedekindDomain/UFD_iff_PID.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/ideal-class-group/index.html#is-principal-ideal-ring-iff-subsingleton).

## Dedekind domains: UFD iff trivial class group

A Dedekind domain $R$ is a unique
factorization domain if and only if its ideal class group is trivial.

## Sources

- ATLAS NumberTheoryI, Section 3.2, Corollary 3.15 (combined).

Formalized by `IsDedekindDomain.uniqueFactorizationMonoid_iff_subsingleton_classGroup`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/UFD_iff_PID.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DedekindDomain/UFD_iff_PID.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/ideal-class-group/index.html#unique-factorization-monoid-iff-subsingl).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ideal class group](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/ideal-class-group/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/dedekind-domains/ideal-class-group)
