A **monad** on a [category](trough:CategoryTheory.Category) $\mathcal{C}$ is an endofunctor $T$ of $\mathcal{C}$ together with two [natural transformations](trough:CategoryTheory.NatTrans), a unit $\eta \colon 1_{\mathcal{C}} \to T$ and a multiplication $\mu \colon T T \to T$, subject to associativity and unit laws that mirror those of a monoid. Monads arise from every [adjunction](trough:CategoryTheory.Adjunction), and conversely every monad arises from one. They give a uniform language for algebraic structure: groups, monoids, modules and compact Hausdorff spaces can all be described as algebras for a suitable monad. In computer science, monads model computational effects such as failure, nondeterminism and state.

## Definition

Let $\mathcal{C}$ be a category. A monad on $\mathcal{C}$ consists of a [functor](trough:CategoryTheory.Functor) $T \colon \mathcal{C} \to \mathcal{C}$ and natural transformations $\eta \colon 1_{\mathcal{C}} \to T$ and $\mu \colon T \circ T \to T$ such that for every object $X$

$$\mu_X \circ T(\mu_X) = \mu_X \circ \mu_{TX} \colon T^3 X \to TX,$$

$$\mu_X \circ \eta_{TX} = \mathrm{id}_{TX}, \qquad \mu_X \circ T(\eta_X) = \mathrm{id}_{TX}.$$

The first equation is associativity: the two ways of collapsing three layers of $T$ to one agree. The other two are the unit laws.

A morphism of monads $\theta \colon T \to S$ is a natural transformation compatible with the structure, meaning $\theta_X \circ \eta^T_X = \eta^S_X$ and $\theta_X \circ \mu^T_X = \mu^S_X \circ \theta_{SX} \circ T(\theta_X)$ for all $X$. Dually, a comonad is an endofunctor with a counit $T \to 1_{\mathcal{C}}$ and a comultiplication $T \to T T$ satisfying the reversed laws.

## Examples

- **Lists.** On the category of sets, let $T(X)$ be the set of finite [lists](trough:List) of elements of $X$. The unit sends $x$ to the one-element list, and the multiplication concatenates a list of lists into a single list. This is the monad of the free monoid construction.
- **Power set.** Let $T(X)$ be the set of subsets of $X$, with $\eta_X(x) = \{x\}$ and $\mu_X$ sending a family of subsets to its union.
- **Maybe.** Let $T(X) = X \sqcup \{\ast\}$, with $\eta$ the inclusion and $\mu$ identifying the two added points.
- **Ultrafilters.** Sending a set to its set of ultrafilters gives a monad whose unit sends a point to the principal ultrafilter at it, and whose multiplication sends an ultrafilter $\mathcal{U}$ on the set of ultrafilters on $X$ to the ultrafilter of those subsets $A \subseteq X$ for which the set of ultrafilters containing $A$ belongs to $\mathcal{U}$.
- **The [Giry monad](trough:MeasureTheory.Measure.instMeasurableSpace).** On measurable spaces, sending a space to the space of measures on it gives a monad whose unit sends a point to its Dirac measure and whose multiplication sends a measure $m$ on the space of measures to the measure assigning to each measurable set $s$ the value $\int \nu(s) \, dm(\nu) \in [0, \infty]$, a Lebesgue integral of the function $\nu \mapsto \nu(s)$.
- **Programming.** Every lawful monad in the sense of functional programming defines a monad on the category of types.

## Adjunctions and algebras

**Every adjunction gives a monad.** If $F \colon \mathcal{C} \to \mathcal{D}$ is left adjoint to $G \colon \mathcal{D} \to \mathcal{C}$, with unit $\eta$ and counit $\varepsilon$, then $GF$ is a monad on $\mathcal{C}$ with unit $\eta$ and multiplication $G \varepsilon F$, and $FG$ is a comonad on $\mathcal{D}$. The free group functor and the forgetful functor from groups to sets, for instance, give the monad sending a set to the underlying set of the free [group](trough:Group) on it.

**Algebras.** An algebra for $T$, also called an Eilenberg–Moore algebra, is an object $A$ with a morphism $a \colon TA \to A$ satisfying $a \circ \eta_A = \mathrm{id}_A$ and $a \circ \mu_A = a \circ T(a)$. A homomorphism $f \colon (A, a) \to (B, b)$ is a morphism $f \colon A \to B$ with $f \circ a = b \circ T(f)$. Algebras and homomorphisms form a category $\mathcal{C}^T$. For the list monad the algebras are exactly the monoids, for the power set monad they are the complete join-semilattices, and for the maybe monad they are the pointed sets. The algebras for the ultrafilter monad are the compact [Hausdorff](trough:T2Space) spaces: their category is equivalent to the category of compact Hausdorff spaces.

**Every monad comes from an adjunction.** Sending $X$ to the free algebra $(TX, \mu_X)$ gives a functor that is left adjoint to the forgetful functor $\mathcal{C}^T \to \mathcal{C}$, and the monad of this adjunction is isomorphic to $T$. The forgetful functor reflects isomorphisms: a homomorphism of algebras whose underlying morphism is invertible is itself invertible.

**The Kleisli category.** A second adjunction comes from the Kleisli category of $T$, whose objects are those of $\mathcal{C}$ and whose morphisms $X \to Y$ are morphisms $X \to TY$ in $\mathcal{C}$; the composite of $f \colon X \to TY$ and $g \colon Y \to TZ$ is $\mu_Z \circ T(g) \circ f$. There is an adjunction between $\mathcal{C}$ and the Kleisli category whose composite functor is naturally isomorphic to $T$. For the maybe monad, Kleisli morphisms are partial functions. Consider the category whose objects are the adjunctions inducing $T$ and whose morphisms are functors between their middle categories that commute with both the left and the right adjoints. In it the Kleisli adjunction is initial and the Eilenberg–Moore adjunction is terminal.

## Monadic functors

Given an adjunction $F \dashv G$ with $G \colon \mathcal{D} \to \mathcal{C}$, each object $Y$ of $\mathcal{D}$ gives an algebra $(GY, G\varepsilon_Y)$ for the monad $GF$, and this defines a comparison functor $\mathcal{D} \to \mathcal{C}^{GF}$. The functor $G$ is monadic when the comparison functor is an equivalence of categories (this does not depend on the choice of the left adjoint $F$), so that objects of $\mathcal{D}$ are, up to equivalence, the algebras of the monad. The forgetful functors from groups, rings and modules to sets are monadic; the forgetful functor from topological spaces to sets is not, since its monad is the identity and its algebras are just sets. [Beck's monadicity theorem](trough:CategoryTheory.Monad.monadicOfCreatesGSplitCoequalizers) characterizes monadic functors: a right adjoint $G$ is monadic exactly when it reflects isomorphisms and $\mathcal{D}$ has, and $G$ preserves, coequalizers of those parallel pairs whose image under $G$ has a split coequalizer.

## Monads as monoids

The endofunctors of $\mathcal{C}$ form a [monoidal category](trough:CategoryTheory.MonoidalCategory) with composition as the tensor product and the identity functor as the unit. A monad is precisely a monoid object there: $\mu$ is the multiplication and $\eta$ the unit. Accordingly, the category of monads on $\mathcal{C}$ is equivalent to the category of monoid objects in the category of endofunctors of $\mathcal{C}$.

## In Mathlib

Mathlib bundles a monad as a structure extending an endofunctor with its unit and multiplication, and states the three laws one object at a time. Comonads are a separate structure, dual to monads. The category-theoretic notion is distinct from the monad type class of Lean's programming library; the two are linked by the construction above for lawful monads, and their Kleisli categories are equivalent. Being monadic is recorded as extra structure on a functor that includes a chosen left adjoint. Mathlib defines its category of compacta directly as the category of algebras for the ultrafilter monad on types, and then proves the equivalence with compact Hausdorff spaces. Its Giry monad uses all measures, not only probability measures.

## Depends on

- [Category](trough:CategoryTheory.Category)
- [Functor](trough:CategoryTheory.Functor)
- [Natural transformation](trough:CategoryTheory.NatTrans)
