---
article_id: af_480c30ffdbb44ef7116b32ed
concept: CategoryTheory.MonoidalClosed
---

A **cartesian closed category** is a [category](trough:CategoryTheory.Category) with finite products in which, for any two objects $A$ and $B$, there is an object $B^A$ of "morphisms from $A$ to $B$" that behaves like a function space: morphisms $A \times Y \to B$ correspond exactly to morphisms $Y \to B^A$. The category of sets is the basic example, with $B^A$ the set of all functions. Cartesian closed categories are a natural setting for currying functions of several variables, which is why they serve as models of the simply typed lambda calculus, and every topos is one.

## Definition

Let $C$ be a category with finite products, that is, with a terminal object $1$ and a product $A \times Y$ for every pair of objects. An object $A$ is called exponentiable if the [functor](trough:CategoryTheory.Functor) $Y \mapsto A \times Y$ has a right [adjoint](trough:CategoryTheory.Adjunction), written $X \mapsto X^A$. Spelled out, there is a bijection

$$\operatorname{Hom}(A \times Y, X) \cong \operatorname{Hom}(Y, X^A),$$

natural in $X$ and $Y$. The map from left to right is called currying and its inverse uncurrying. The object $X^A$ is the exponential, or internal hom, and the morphism $A \times X^A \to X$ corresponding to the identity of $X^A$ is evaluation. The category $C$ is **cartesian closed** if every object is exponentiable.

This is the special case of a closed [monoidal category](trough:CategoryTheory.MonoidalCategory) in which the tensor product is the categorical product: a monoidal category is [monoidal closed](lean:CategoryTheory.MonoidalClosed) when [every object is closed](lean:CategoryTheory.Closed), meaning that [tensoring with it on the left has a right adjoint](lean:CategoryTheory.ihom.adjunction), called its internal hom functor. For a general tensor product the same definition yields [currying](lean:CategoryTheory.MonoidalClosed.curry) and [uncurrying](lean:CategoryTheory.MonoidalClosed.uncurry), and [uncurrying undoes currying](lean:CategoryTheory.MonoidalClosed.uncurry_curry) while [currying undoes uncurrying](lean:CategoryTheory.MonoidalClosed.curry_uncurry).

## Examples

- **Sets.** In the category of sets, [taking the product with $X$ is left adjoint to the functor of functions out of $X$](lean:CategoryTheory.Types.tensorProductAdjunction): a function of two variables $X \times Y \to Z$ is the same as a function from $Y$ to the set of functions $X \to Z$.
- **Presheaves.** For any small category $D$, [the category of functors from $D$ to sets, with the pointwise product, is cartesian closed](lean:CategoryTheory.FunctorToTypes.monoidalClosed). Mathlib proves this without smallness, for functors into any universe of sets at least as large as the objects and morphisms of $D$. Applied to the opposite category, this covers presheaves; applied to a group viewed as a one-object category, it shows that the category of sets with an action of a group is cartesian closed.
- **Preorders and posets.** A preordered set, viewed as a category, is cartesian closed exactly when it has a greatest element, binary meets, and for each $a, b$ an element $a \Rightarrow b$ with $c \le (a \Rightarrow b)$ if and only if $c \wedge a \le b$. A lattice with a least element and this structure is a Heyting algebra; every Boolean algebra is one.
- **Non-examples.** The category of topological spaces is not cartesian closed. Neither is the category of vector spaces over a field, although it is monoidal closed for the tensor product: it has a zero object, and [in a cartesian closed category with a zero object every hom-set has exactly one element](lean:CategoryTheory.uniqueHomsetOfZero), so such a category is [equivalent to the category with one object and one morphism](lean:CategoryTheory.equivPUnit). In particular a nontrivial [abelian category](trough:CategoryTheory.Abelian) is never cartesian closed.

## Properties

- Since $A \times (-)$ is a left adjoint, it preserves all colimits that exist. In particular products distribute over coproducts, $A \times (B + B') \cong (A \times B) + (A \times B')$, and [the product of $A$ with an initial object $0$ is initial](lean:CategoryTheory.zeroMul).
- Initial objects are strict: [every morphism from an exponentiable object into an initial object is an isomorphism](lean:CategoryTheory.strict_initial). Consequently [every morphism out of an initial object is a monomorphism](lean:CategoryTheory.initial_mono).
- The usual laws of exponents hold up to natural [isomorphism](trough:CategoryTheory.Iso), for instance $(X^B)^A \cong X^{A \times B}$ and $(X \times X')^A \cong X^A \times X'^A$. For the terminal object, [the exponential $X^1$ is isomorphic to $X$](lean:CategoryTheory.MonoidalClosed.unitIsoSelf).
- Being cartesian closed is invariant under equivalence: [a category with finite products that is equivalent to a cartesian closed category is cartesian closed](lean:CategoryTheory.cartesianClosedOfEquiv).
- A full subcategory $D$ of a cartesian closed category $C$, closed under isomorphism, is called an [exponential ideal](lean:CategoryTheory.ExponentialIdeal) if $X^A$ lies in $D$ whenever $X$ lies in $D$, for every object $A$ of $C$. If $D$ is moreover reflective, then [it is again cartesian closed, with any choice of finite products](lean:CategoryTheory.cartesianClosedOfReflective).

## Generalizations

Replacing the product by an arbitrary tensor product gives closed monoidal categories, whose internal homs include the space of linear maps between vector spaces, or between modules over a commutative ring. Locally cartesian closed categories ask that every slice category be cartesian closed; toposes are cartesian closed categories with finite limits and a subobject classifier.

## In Mathlib

Mathlib has no separate class for cartesian closed categories: a cartesian closed category is a category carrying a chosen cartesian monoidal structure (a [chosen terminal object and chosen binary products](lean:CategoryTheory.CartesianMonoidalCategory), used as the tensor product) together with a monoidal closed structure. The closed structure is data rather than a property: each object comes with a specified right adjoint, unique only up to isomorphism. The convention is right closedness, adjoining on the side of $A \otimes Y$ as above; for a cartesian product the two sides agree up to the symmetry of the product. Several basic results are stated with weaker hypotheses than full cartesian closedness, for instance the strictness of initial objects, which needs only the one object to be exponentiable. Likewise, exponential ideals are defined for an arbitrary functor into $C$, an object counting as lying in the subcategory when it is isomorphic to an image of that functor.

## Depends on

- [Category](trough:CategoryTheory.Category)
- [Functor](trough:CategoryTheory.Functor)
- [Adjunction](trough:CategoryTheory.Adjunction)
- [Limits](trough:CategoryTheory.Limits.IsLimit)
- [Monoidal category](trough:CategoryTheory.MonoidalCategory)
