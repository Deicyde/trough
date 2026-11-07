The **Yoneda embedding** of a [category](trough:CategoryTheory.Category) $\mathcal{C}$
sends each object $X$ to the presheaf of morphisms into $X$, the contravariant
[functor](trough:CategoryTheory.Functor) $Y \mapsto \mathrm{Hom}(Y, X)$ to sets. It is
fully faithful, so $\mathcal{C}$ sits inside the category of presheaves on $\mathcal{C}$
without losing or gaining any morphisms. The underlying result, the Yoneda lemma,
identifies the natural transformations from the presheaf of morphisms into $X$ to any
presheaf $F$ with the elements of $F(X)$. It implies that an object is determined up to isomorphism by the functor of
morphisms into it; this justifies
defining objects by the functors they represent, a method used throughout algebra,
topology and algebraic geometry.

## Definition

Let $\mathcal{C}$ be a category in which the morphisms between any two objects form a
set. For an object $X$, write $h_X$ for the functor from the opposite category
$\mathcal{C}^{\mathrm{op}}$ to sets given by

$$h_X(Y) = \mathrm{Hom}(Y, X), \qquad h_X(g)(f) = f \circ g$$

for a morphism $g \colon Y' \to Y$ and $f \in \mathrm{Hom}(Y, X)$. A morphism
$u \colon X \to X'$ induces a [natural transformation](trough:CategoryTheory.NatTrans)
$h_u \colon h_X \to h_{X'}$ whose component at $Y$ is composition with $u$, sending $f$ to
$u \circ f$. The assignments $X \mapsto h_X$ and $u \mapsto h_u$ form
the Yoneda embedding, a functor from $\mathcal{C}$ to the
category of presheaves on $\mathcal{C}$, that is, of functors
$\mathcal{C}^{\mathrm{op}} \to \mathbf{Set}$ with natural transformations as morphisms.

Reversing the roles of source and target gives the
co-Yoneda embedding, which sends $X$ to the covariant
functor $\mathrm{Hom}(X, -)$ and is a functor out of $\mathcal{C}^{\mathrm{op}}$.

## The Yoneda lemma

Let $F$ be a presheaf on $\mathcal{C}$ and $X$ an object. A natural transformation
$\eta \colon h_X \to F$ determines the element $\eta_X(\mathrm{id}_X)$ of $F(X)$, and
naturality forces $\eta_Y(f) = F(f)\bigl(\eta_X(\mathrm{id}_X)\bigr)$ for every
$f \colon Y \to X$. Conversely every element $x$ of $F(X)$ defines a natural
transformation by $f \mapsto F(f)(x)$. Hence
natural transformations from $h_X$ to $F$ correspond bijectively to elements of $F(X)$,
and this bijection is natural in both $X$ and $F$.

Taking $F = h_{X'}$ shows that every natural transformation $h_X \to h_{X'}$ is $h_u$ for
exactly one morphism $u \colon X \to X'$, namely the image of $\mathrm{id}_X$. In other
words, the Yoneda embedding is fully faithful:
it is full and
faithful. The same argument shows that
the co-Yoneda embedding is fully faithful.

## Consequences

- **Objects are determined by their morphisms.** If there are bijections
  $\mathrm{Hom}(Z, X) \cong \mathrm{Hom}(Z, Y)$ for all $Z$, natural in $Z$, then
  $X$ and $Y$ are isomorphic.
- **Detecting isomorphisms.** A morphism $f \colon X \to Y$ is an
  [isomorphism](trough:CategoryTheory.Iso) if and only if
  for every object $T$, composition with $f$ is a bijection from $\mathrm{Hom}(T, X)$ to $\mathrm{Hom}(T, Y)$.
- **Representable functors.** A presheaf $F$ is
  representable if it is naturally
  isomorphic to $h_X$ for some object $X$. Such an isomorphism is the same as a choice of
  bijections $\mathrm{Hom}(Y, X) \cong F(Y)$ natural in $Y$, and by the Yoneda lemma it
  is determined by a single element of $F(X)$, the universal element.
  Two objects representing the same presheaf are isomorphic.
  Universal properties are statements of representability: a product of $A$ and $B$, for
  instance, is an object representing $Y \mapsto \mathrm{Hom}(Y, A) \times \mathrm{Hom}(Y, B)$,
  which is why products and other [limits](trough:CategoryTheory.Limits.IsLimit) are
  unique up to a unique isomorphism compatible with their universal elements (for a
  product, with the two projections).
- **Maps out of presheaves.** Two morphisms of presheaves $P \to Q$ are equal as soon as
  they agree after composing with every morphism $h_X \to P$,
  so a presheaf is controlled by the representable presheaves mapping to it.

## Examples

- **Monoids.** A monoid $M$ can be regarded as a category with one object whose morphisms are the elements
  of $M$, composed by multiplication. A presheaf on it is a set with a right action of $M$,
  and the single representable presheaf is $M$ acting on itself by right multiplication.
  The maps from $M$ to itself that commute with this action are exactly the left
  multiplications, and full faithfulness says that $m \mapsto (x \mapsto mx)$ identifies
  $M$ with them. So every monoid is isomorphic to a monoid of maps from a set to itself under
  composition; for a [group](trough:Group) this is
  [Cayley's theorem](trough:Equiv.Perm.subgroupOfMulAction), that every group is
  isomorphic to a group of permutations.
- **Partial orders.** A partially ordered set can be regarded as a category with one morphism from $y$ to
  $x$ when $y \le x$ and none otherwise. Then $h_x(y)$ is a one-point set when $y \le x$
  and empty otherwise, so $h_x$ records the set of elements below $x$. Full faithfulness
  says that $x \le x'$ exactly when every element below $x$ lies below $x'$.
- **Subsets.** On the category of sets, the presheaf sending a set $Y$ to its set of
  subsets, and a map to the operation of taking preimages, is represented by a two-element
  set $\{0, 1\}$: a subset corresponds to its indicator function, and the universal element
  is the subset $\{1\}$.

## Related concepts

Representability of the functor $Y \mapsto \mathrm{Hom}(F(Y), Z)$ for each $Z$ is what it
means for a functor $F$ to have a right [adjoint](trough:CategoryTheory.Adjunction), and
much of the theory of adjunctions is the Yoneda lemma applied with parameters. On a
[small category](trough:CategoryTheory.SmallCategory) every presheaf is a colimit of
representable ones, and the presheaf category is the free completion of $\mathcal{C}$
under colimits. Replacing presheaves by sheaves for a
[Grothendieck topology](trough:CategoryTheory.GrothendieckTopology) gives the setting in
which schemes and other geometric objects can be studied through the functors of
morphisms into them.

## In Mathlib

Mathlib defines the Yoneda embedding for every category, with presheaves valued in the
types of the same universe as the morphisms of $\mathcal{C}$; this plays the role of the
hypothesis that morphisms between two objects form a set, so no separate smallness
assumption is needed, and a variant raising the universe of the values is also provided.
Composition is written in diagrammatic order, so the formulas above appear with their
factors reversed. The Yoneda lemma is given both as a plain bijection for fixed $X$ and
$F$ and as a natural isomorphism between two functors of the pair $(X, F)$; because the
second ranges over all presheaves, its values are lifted to a larger universe. Full
faithfulness is recorded as data, an explicit inverse to the action on morphisms, from
which fullness and faithfulness follow. A representation of a presheaf is likewise data,
a family of bijections natural in the argument, while representability is the
proposition that some representation exists; presheaves valued in any universe may be
representable.

## Depends on

- [Category](trough:CategoryTheory.Category)
- [Functor](trough:CategoryTheory.Functor)
- [Natural transformation](trough:CategoryTheory.NatTrans)
