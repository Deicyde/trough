---
article_id: af_f03e5f7719969665d0235ac2
declaration: definition
origin: cited
not_ready: true
---

# Class function over a group

A **class function** on a [group](../../../overview/general-algebra/group-theory/part-01/group.md) $G$ is a function on $G$ that
takes the same value at any two conjugate elements, so that it is constant on
each [conjugacy class](../basic-definitions/conjugacy-classes.md). The
[characters](../../../overview/general-algebra/representation-theory/character.md) of representations are class functions,
and for a finite group over the complex numbers the
irreducible characters form a basis of the space of class functions. This makes
class functions the setting in which representations of a finite group are
studied by means of functions on the group.

## Definition

Let $G$ be a group and $X$ a set. A function $f \colon G \to X$ is a class
function if

$$f(hgh^{-1}) = f(g) \quad \text{for all } g, h \in G.$$

An equivalent condition is $f(gh) = f(hg)$ for all $g, h \in G$: substituting
$gh$ for $g$ in the first condition gives $f(h(gh)h^{-1}) = f(gh)$, that
is, $f(hg) = f(gh)$, and conversely $f(hgh^{-1}) = f(h^{-1} \cdot hg) = f(g)$.

The conjugacy class of $g$ is the set $\{hgh^{-1} : h \in G\}$, and
[two elements have the same conjugacy class exactly when they are conjugate](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Conj.html#ConjClasses.mk_eq_mk_iff_isConj). A class function is therefore
the same thing as a function on the set of conjugacy classes of $G$, composed
with the map sending each element to its class.

Most often $X$ is a field $k$, usually the complex numbers. The class functions
$G \to k$ then form a vector space under pointwise addition and scalar
multiplication, closed also under pointwise multiplication. When $G$ is finite
with conjugacy classes $C_1, \dots, C_r$, the indicator functions of
$C_1, \dots, C_r$ form a basis, so this space has dimension $r$, the number of
conjugacy classes.

## Examples

- **Constant functions and indicators.** Every constant function is a class
  function, as is the indicator function of any conjugacy class, for instance
  the function equal to $1$ at the identity and $0$ elsewhere.
- **Abelian groups.** In a commutative group
  [two elements are conjugate exactly when they are equal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Conj.html#isConj_iff_eq),
  so every function on an abelian group is a class function.
- **Order of an element.** If $ax = ya$, then
  [$x$ and $y$ have the same order](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/OrderOfElement.html#SemiconjBy.orderOf_eq); taking
  $y = axa^{-1}$ shows that conjugate elements have the same
  [order](../basic-definitions/order-of-an-element.md), so $g \mapsto \operatorname{ord}(g)$ is a class function.
- **Homomorphisms to abelian groups.** A homomorphism
  [carries conjugate elements to conjugate elements](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Conj.html#MonoidHom.map_isConj),
  so a homomorphism $\varphi \colon G \to A$ into an abelian group $A$ is a class
  function. The [signature](../permutation-group/signature.md) of a permutation and the
  [determinant](../../../overview/linear-algebra/matrices/determinant.md) of an invertible matrix are examples.
- **Symmetric groups.** [Two permutations of a finite set are conjugate exactly when they have the same cycle type](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Type.html#Equiv.Perm.isConj_iff_cycleType_eq),
  so the class functions on a symmetric group are the functions of the cycle
  type. The number of fixed points of a permutation is an example. In $S_3$ the classes are the identity,
  the three transpositions and the two $3$-cycles, so the class functions on
  $S_3$ with values in a field form a space of dimension $3$.
- **Trace and characteristic polynomial.** For square matrices over a
  commutative ring and $M$ invertible,
  [the trace of $MNM^{-1}$ equals the trace of $N$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/NonsingularInverse.html#Matrix.trace_conj) and
  [the characteristic polynomial of $MNM^{-1}$ equals that of $N$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Charpoly/Basic.html#Matrix.charpoly_units_conj). So the trace and the
  [characteristic polynomial](../../../overview/linear-algebra/endomorphism-polynomials/characteristic-polynomial.md) are class functions on the
  [general linear group](../classical-automorphism-groups/general-linear-group.md).
- **Characters.** If $\rho$ is a finite-dimensional
  [representation](../../../overview/general-algebra/representation-theory/representation.md) of $G$ over a field $k$, its character
  is $\chi(g) = \operatorname{tr} \rho(g)$, and
  [$\chi(hgh^{-1}) = \chi(g)$ for all $g, h \in G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RepresentationTheory/Character.html#FDRep.char_conj).

## Properties

- **Products of characters.** Characters are closed under pointwise
  multiplication inside the algebra of class functions:
  [the character of a tensor product of representations is the product of their characters](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RepresentationTheory/Character.html#FDRep.char_tensor). The character of a direct sum is the sum
  of the characters.
- **Inner product.** For a finite group $G$, complex class functions carry the
  inner product
  $$\langle f_1, f_2 \rangle = \frac{1}{|G|} \sum_{g \in G} f_1(g)\, \overline{f_2(g)}.$$
  For characters, $\overline{\chi(g)} = \chi(g^{-1})$, since the eigenvalues of
  $\rho(g^{-1})$ are the inverses of those of $\rho(g)$, which are roots of
  unity, and the inverse of a root of unity is its complex conjugate. Over an algebraically closed field $k$ in which
  $|G|$ is invertible, the characters of
  [irreducible representations](../../linear-algebra/linear-representations/irreducible-representation.md) $V$ and $W$
  of a finite group satisfy
  [$\frac{1}{|G|}\sum_{g} \chi_V(g)\,\chi_W(g^{-1})$ equals $1$ if $V \cong W$ and $0$ otherwise](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RepresentationTheory/Character.html#FDRep.char_orthonormal): these are the
  [orthogonality relations](../../../overview/general-algebra/representation-theory/orthogonality-of-characters.md).
- **Basis of irreducible characters.** Over the complex numbers the irreducible
  characters of a finite group are not only orthonormal but span the space of
  class functions, so they form an
  [orthonormal basis](orthonormal-basis-of-irreducible-characters.md),
  and the number of irreducible representations up to isomorphism equals the
  number of conjugacy classes.
- **Centre of the group algebra.** Identify a function $f$ on a finite group
  with the element $\sum_g f(g)\, g$ of the group algebra $k[G]$, whose
  multiplication corresponds to [convolution](convolution.md)
  of functions. This element is central exactly when $f$ is a class function, so
  the class functions form the centre of the group algebra.
- **Counting classes.** The dimension $r$ of the space of class functions can be
  read off from commuting pairs: for a finite group,
  [the number of pairs $(g, h)$ with $gh = hg$ equals $r\,|G|$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/CardCommute.html#card_comm_eq_card_conjClasses_mul_card).

## Related concepts

For a finite abelian group every function is a class function, and the
irreducible complex characters are the homomorphisms to the nonzero complex
numbers (equivalently, to the unit circle), which form the
[dual group](dual-groups.md).
Expanding a function in this basis is the
[Fourier transform for finite abelian groups](fourier-transform-for-finite-abelian-groups.md);
expansion of class functions in irreducible characters extends it to finite
groups that are not abelian.

## In Mathlib

Mathlib has no notion of a class function: no predicate saying a function is
constant on conjugacy classes, no space or algebra of class functions, no basis
of class indicators, no inner product on class functions, and no theorem that
irreducible characters span them or that their number equals the number of
conjugacy classes. It does have the parts. Conjugacy is defined for monoids,
with an invertible conjugating element, and the conjugacy classes form a
quotient type, so a class function can be expressed as a function on that
quotient. Characters are plain functions from the group to the field, defined
both for bundled finite-dimensional representations and for unbundled ones, and
their invariance under conjugation is a separate theorem; the unbundled version
proves it for every representation, finite-dimensional or not, since the trace
is taken to be $0$ where it is not otherwise defined. Irreducibility in the
bundled version is simplicity in the category of representations. The
orthogonality relations are stated with $\chi_W(g^{-1})$ in place of a complex
conjugate, which makes sense over any field. The count of commuting pairs is
stated for every group, with cardinality $0$ for an infinite set, so for an
infinite group both sides are $0$. Nothing in the representation theory library
refers to the type of conjugacy classes.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Conjugacy classes](../basic-definitions/conjugacy-classes.md)

## Sources

- [Mathlib undergraduate list: Group Theory › Representation theory of finite groups](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L118)
- [Reference given by Mathlib's undergraduate list](https://en.wikipedia.org/wiki/Class_function)
