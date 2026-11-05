---
article_id: af_dc282c2cb02c23ce9c386ba7
concept: HomologicalComplex.homology
---

**Functorial homology** is the construction that assigns to a complex $K$ and a degree $i$ the homology object $H_i(K)$, the cycles in degree $i$ modulo the boundaries, together with the morphism $H_i(K) \to H_i(L)$ that every chain map $K \to L$ induces. The assignment respects identities and composition, so homology in each degree is a [functor](trough:CategoryTheory.Functor) from complexes to the underlying [category](trough:CategoryTheory.Category). It measures how far a complex is from being exact, and it is a principal source of invariants in algebraic topology, homological algebra and sheaf theory.

## Definition

A complex $K$ in a category $\mathcal{C}$ with zero morphisms consists of objects $X_i$ indexed by a set of degrees and differentials $d_{ij} \colon X_i \to X_j$, where a fixed relation on the degrees (the shape of the complex) says which differentials may be nonzero, each degree has at most one degree mapping to it and at most one degree it maps to, and the composite of two consecutive differentials is zero. A [chain complex](trough:ChainComplex) indexed by the natural numbers is the case where $d_{ij}$ can be nonzero only when $i = j + 1$.

Fix a degree $i$. Let $i'$ be the degree whose differential enters $X_i$ and $i''$ the degree that receives the differential leaving $X_i$ (when no such degree exists, take $i$ itself with a zero differential; see the last section). This gives a sequence

$$X_{i'} \xrightarrow{\;d_{i'i}\;} X_i \xrightarrow{\;d_{ii''}\;} X_{i''}$$

whose composite is zero. For a complex of [modules](trough:Module) over a ring, the cycles $Z_i = \ker d_{ii''}$ contain the boundaries $B_i = \operatorname{im} d_{i'i}$, and

$$H_i(K) = Z_i / B_i.$$

Indeed, [for a sequence of modules $M_1 \xrightarrow{f} M_2 \xrightarrow{g} M_3$ with $g \circ f = 0$, its homology is isomorphic to the kernel of $g$ modulo the image of $f$](lean:CategoryTheory.ShortComplex.moduleCatHomologyIso). In a general category the quotient is replaced by a [universal construction](trough:CategoryTheory.Limits.IsLimit), a cokernel of the map from $X_{i'}$ into the kernel of $d_{ii''}$, and [the homology of $K$ in degree $i$](lean:HomologicalComplex.homology) is defined whenever this construction and its dual, a kernel inside the cokernel of the incoming differential, both exist and agree (made precise in the last section). It always exists in an [abelian category](trough:CategoryTheory.Abelian), since [every such three-term sequence in an abelian category has homology](lean:CategoryTheory.categoryWithHomology_of_abelian).

A chain map $\varphi \colon K \to L$ commutes with the differentials, so it sends cycles to cycles and boundaries to boundaries. It therefore [induces a morphism $H_i(K) \to H_i(L)$](lean:HomologicalComplex.homologyMap), which for complexes of modules sends the class of a cycle $z$ to the class of $\varphi(z)$. The identity chain map [induces the identity](lean:HomologicalComplex.homologyMap_id), and the map induced by a composite $\psi \circ \varphi$ [is the composite of the induced maps](lean:HomologicalComplex.homologyMap_comp). When every such three-term sequence in $\mathcal{C}$ has homology, these data form [the degree $i$ homology functor](lean:HomologicalComplex.homologyFunctor).

## Examples

- **Multiplication by two.** Let $K$ be the chain complex of abelian groups with $X_1 = X_0 = \mathbb{Z}$, the differential $X_1 \to X_0$ given by $n \mapsto 2n$, and all other terms zero. Multiplication by $2$ is injective, so $H_1(K) = 0$, while every element of $X_0$ is a cycle and the boundaries are the even integers, so $H_0(K) = \mathbb{Z}/2\mathbb{Z}$.
- **Zero differentials.** If every differential of $K$ is zero, every element is a cycle and the only boundary is $0$, so $H_i(K) = X_i$ for every $i$.
- **Singular homology.** The $n$-th singular homology of topological spaces is the composite of the singular chain complex construction with the degree $n$ homology functor; Mathlib defines [singular homology with coefficients in an object of a preadditive category with coproducts in which homology exists](lean:AlgebraicTopology.singularHomologyFunctor) in exactly this way.

## Properties

- **Exactness.** A complex $K$ is exact at degree $i$, meaning that the cycles equal the boundaries there, [if and only if $H_i(K)$ is a zero object](lean:HomologicalComplex.exactAt_iff_isZero_homology).
- **Homotopy invariance.** In a preadditive category, [homotopic chain maps induce the same morphism on homology](lean:Homotopy.homologyMap_eq) in every degree where both complexes have homology. Consequently [a homotopy equivalence $K \to L$ induces an isomorphism $H_i(K) \cong H_i(L)$](lean:HomotopyEquiv.toHomologyIso).
- **Quasi-isomorphisms.** A chain map is a [quasi-isomorphism](lean:QuasiIso) when it induces isomorphisms on homology in every degree. In a single degree, [a chain map is a quasi-isomorphism at $i$ if and only if the induced morphism on $H_i$ is an isomorphism](lean:quasiIsoAt_iff_isIso_homologyMap). For complexes in a preadditive category with homology in every degree, [every homotopy equivalence is a quasi-isomorphism](lean:HomotopyEquiv.quasiIso_hom), but not conversely: the map from the complex $\mathbb{Z} \xrightarrow{2} \mathbb{Z}$ above onto $\mathbb{Z}/2\mathbb{Z}$ in degree $0$ is a quasi-isomorphism, yet every chain map back is zero, since $\mathbb{Z}$ has no nonzero element of order $2$, so no map back can invert it up to homotopy.

**Long exact sequence.** In an abelian category, let $0 \to K \to L \to M \to 0$ be a short exact sequence of complexes, and let $i$ and $j$ be degrees joined by a differential from degree $i$ to degree $j$. There is [a connecting morphism $\delta \colon H_i(M) \to H_j(K)$](lean:CategoryTheory.ShortComplex.ShortExact.δ), and the sequence

$$H_i(K) \to H_i(L) \to H_i(M) \xrightarrow{\;\delta\;} H_j(K) \to H_j(L) \to H_j(M)$$

is [exact at $H_i(L)$](lean:CategoryTheory.ShortComplex.ShortExact.homology_exact₂), [exact at $H_i(M)$](lean:CategoryTheory.ShortComplex.ShortExact.homology_exact₃) and [exact at $H_j(K)$](lean:CategoryTheory.ShortComplex.ShortExact.homology_exact₁). Splicing these pieces over all degrees gives the long exact homology sequence.

## In Mathlib

Mathlib works with complexes of an arbitrary shape: the degrees form any type, and a relation on it says which differentials are allowed, so chain complexes, cochain complexes and complexes indexed by the integers are all special cases. A differential is recorded for every pair of degrees, with the requirement that it vanish outside the shape. When no degree precedes $i$, Mathlib uses $i$ itself as the predecessor, with a zero differential, and likewise for successors; so for a chain complex indexed by the natural numbers, $H_0$ is $X_0$ modulo the image of $d_{10}$. The homology in degree $i$ is defined as the [homology of the three-term sequence](lean:CategoryTheory.ShortComplex.homology) above, which in turn rests on a [homology data](lean:CategoryTheory.ShortComplex.HomologyData): a compatible pair consisting of a quotient of the cycles and a subobject of the cokernel of the incoming differential, identified with each other. This needs only zero morphisms, not an abelian category, and the existence of homology in a given degree is a hypothesis carried along rather than a property of the ambient category; only the homology functor asks that every three-term sequence in the category have homology. The homology object is a chosen one, determined up to canonical isomorphism.

## Depends on

- [Category](trough:CategoryTheory.Category)
- [Functor](trough:CategoryTheory.Functor)
- [Abelian category](trough:CategoryTheory.Abelian)
- [Chain complex](trough:ChainComplex)
- [Limits](trough:CategoryTheory.Limits.IsLimit)
