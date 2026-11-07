An **abelian category** is a [category](trough:CategoryTheory.Category) whose morphisms can be added and in which kernels, cokernels, images and exact sequences behave as they do for [modules](trough:Module) over a [ring](trough:Ring). The notion isolates the formal properties of abelian groups and modules that homological algebra actually uses, so that constructions such as [chain complexes](trough:ChainComplex), [homology](trough:HomologicalComplex.homology) and derived functors can be carried out once, uniformly, for modules, sheaves, representations and many other settings.

## Definition

A category $\mathcal{A}$ is abelian when it satisfies the following conditions.

1. It is preadditive: every set of morphisms $\mathrm{Hom}(X, Y)$ carries the structure of an abelian group, and composition is additive in each variable, so that $(f + f') \circ g = f \circ g + f' \circ g$ and $h \circ (f + f') = h \circ f + h \circ f'$.
2. It has all finite products, including the empty product, which is a terminal object.
3. Every morphism has a kernel and a cokernel.
4. Every monomorphism is the kernel of some morphism, and every epimorphism is the cokernel of some morphism.

In a preadditive category a terminal object is also initial, so an abelian category has a zero object, and its finite products are at the same time coproducts: an abelian category has finite biproducts, usually written as direct sums $X \oplus Y$.

For a morphism $f \colon X \to Y$, the *image* of $f$ is the kernel of its cokernel and the *coimage* is the cokernel of its kernel. The morphism factors as $X \to \operatorname{coim} f \to \operatorname{im} f \to Y$, and in an abelian category the middle map is a canonical isomorphism from the coimage to the image. This gives an equivalent definition: a preadditive category with kernels, cokernels and finite products in which the comparison from coimage to image is always an isomorphism is abelian.

A sequence $X \xrightarrow{f} Y \xrightarrow{g} Z$ with $g \circ f = 0$ is *exact* at $Y$ when the image of $f$ and the kernel of $g$ are the same subobject of $Y$. For modules this is the familiar condition that the range of $f$ equals the kernel of $g$.

## Examples

- For any ring $R$, commutative or not, the [category of $R$-modules](trough:ModuleCat) is abelian. Taking $R = \mathbb{Z}$ gives the category of abelian groups, and taking $R$ a field gives vector spaces. Kernels and cokernels are the usual [kernel](trough:LinearMap.ker) and quotient by the [range](trough:LinearMap.range).
- If $\mathcal{A}$ is abelian and $\mathcal{C}$ is any category, then the category of functors from $\mathcal{C}$ to $\mathcal{A}$ is abelian, with kernels and cokernels computed objectwise. In particular presheaves of abelian groups form an abelian category.
- If $\mathcal{A}$ is abelian, then for a [Grothendieck topology](trough:CategoryTheory.GrothendieckTopology) on a category for which sheafification with values in $\mathcal{A}$ exists, the category of sheaves with values in $\mathcal{A}$ is abelian. The classical case is sheaves of abelian groups on a topological space.
- The opposite of an abelian category is abelian: the opposite of a preadditive category is preadditive, and the other conditions turn into their duals, which abelian categories also satisfy. Chain complexes in an abelian category again form an abelian category.

Not every additive setting is abelian. In the category of free abelian groups, multiplication by $2$ on $\mathbb{Z}$ is both a monomorphism and an epimorphism but has no inverse, which is impossible in an abelian category (see below). The category of all groups is not abelian either: the trivial group is a zero object, but for nontrivial groups $G$ and $H$ the product $G \times H$ is not a coproduct (the coproduct is the free product $G * H$), whereas in an abelian category finite products and coproducts coincide.

## Properties

- A morphism that is both a monomorphism and an epimorphism is an [isomorphism](trough:CategoryTheory.Iso); in other words, abelian categories are balanced, where a category is balanced when every morphism that is both a monomorphism and an epimorphism is an isomorphism.
- An abelian category has all finite limits and all finite colimits (see [limits](trough:CategoryTheory.Limits.IsLimit)).
- The pullback of an epimorphism along any morphism is an epimorphism, and dually the pushout of a monomorphism along any morphism is a monomorphism.
- Exactness as defined above agrees with the homological definition: for $X \xrightarrow{f} Y \xrightarrow{g} Z$ with $g \circ f = 0$, the homology at $Y$ vanishes exactly when the image of $f$ and the kernel of $g$ are the same subobject of $Y$.
- The standard diagram lemmas hold. The five lemma says that, given a map between two exact rows of five objects whose first component is an epimorphism, whose second and fourth are isomorphisms and whose fifth is a monomorphism, the middle component is an isomorphism. The snake lemma says that a map from an exact row $A \to B \to C \to 0$ to an exact row $0 \to A' \to B' \to C'$, with vertical maps $a$, $b$, $c$, gives an exact sequence
$$\ker a \to \ker b \to \ker c \to \operatorname{coker} a \to \operatorname{coker} b \to \operatorname{coker} c.$$

Many such arguments are first checked with elements in module categories and then transferred. [Mitchell's embedding theorem](trough:CategoryTheory.Abelian.freyd_mitchell) justifies this: every abelian category admits a fully faithful functor into the modules over some ring that preserves finite limits and finite colimits, so it is equivalent to a full subcategory of a module category, compatibly with kernels, cokernels and exactness.

## In Mathlib

Mathlib defines an abelian category as a structure placed on a category, extending its preadditive structure, rather than as a property of the category. A category usually comes with its own addition of morphisms, and requiring this addition as data lets each example supply it directly. Exactness is defined for any category with zero morphisms, by the vanishing of homology, and in an abelian category it agrees with the condition on images and kernels above. That abelian categories are balanced is likewise not stated in one place but derived in steps: every epimorphism in an abelian category is normal, hence regular, hence strong, and a category in which every epimorphism is strong is balanced. Mathlib also shows that the addition is not extra information in principle: a category with a zero object, and hence zero morphisms, with finite products and coproducts, kernels and cokernels, in which every monomorphism and every epimorphism is normal, carries an abelian structure, the addition being constructed from the other axioms. Mathlib's embedding theorem needs no smallness hypothesis on the category: the ring and its modules are taken in a universe large enough to contain the objects of the category, whereas textbook statements usually assume a small category.

## Depends on

- [Category](trough:CategoryTheory.Category)
- [Group](trough:Group)
- [Limits](trough:CategoryTheory.Limits.IsLimit)
