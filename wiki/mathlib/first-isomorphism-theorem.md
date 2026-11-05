---
article_id: af_187106b5b15350d2a064b0a5
concept: QuotientGroup.quotientKerEquivRange
---

The **first isomorphism theorem** says that a [group homomorphism](trough:MonoidHom)
$\varphi \colon G \to H$ identifies the [quotient](trough:QuotientGroup.Quotient.group) of $G$ by the
kernel of $\varphi$ with the image of $\varphi$. Every homomorphism therefore factors as a
surjection onto a quotient followed by an isomorphism and an inclusion, and the
question of which groups are homomorphic images of $G$ becomes the question of which
[normal subgroups](trough:Subgroup.Normal) $G$ has. The theorem is also known as the
fundamental theorem on homomorphisms, and it is the first of three
isomorphism theorems, together with the [second](trough:QuotientGroup.quotientInfEquivProdNormalQuotient)
and the [third](trough:QuotientGroup.quotientQuotientEquivQuotient).

## Statement

Let $\varphi \colon G \to H$ be a homomorphism of [groups](trough:Group), with kernel
$K = \{ g \in G : \varphi(g) = e \}$ and image $\varphi(G)$, a [subgroup](trough:Subgroup) of $H$.
The kernel [is a normal subgroup of $G$](lean:MonoidHom.normal_ker), so the quotient group $G/K$
is defined, and the map

$$G/K \to \varphi(G), \qquad gK \mapsto \varphi(g)$$

is [a well-defined isomorphism of groups](lean:QuotientGroup.quotientKerEquivRange).
When $\varphi$ is surjective this reads
[$G/\ker\varphi \cong H$](lean:QuotientGroup.quotientKerEquivOfSurjective).

## Proof

Write $\psi(gK) = \varphi(g)$. Two cosets $gK$ and $hK$ are equal exactly when
$g^{-1}h \in K$, that is, when $\varphi(g)^{-1}\varphi(h) = e$, that is, when
$\varphi(g) = \varphi(h)$. Read from left to right this says $\psi$ is well defined; read from
right to left it says $\psi$ is injective. Since multiplication of cosets is
$(gK)(hK) = ghK$ and $\varphi$ preserves products, $\psi$ is a homomorphism, and it maps onto
$\varphi(G)$ by construction. Well-definedness and the homomorphism property are a special
case of a more general fact: a homomorphism that is trivial on a normal subgroup $N$
[descends to a homomorphism on $G/N$](lean:QuotientGroup.lift).

## Examples

- **Trivial cases.** The identity map of $G$ has trivial kernel, giving
  [$G/\{e\} \cong G$](lean:QuotientGroup.quotientBot); the map sending everything to $e$ gives $G/G \cong \{e\}$.
- **Integers modulo $n$.** Reduction modulo $n$ is a surjective homomorphism from the
  additive group of [integers](trough:Int) onto the integers modulo $n$, with kernel $n\mathbb{Z}$, so
  [$\mathbb{Z}/n\mathbb{Z}$ is isomorphic to the group of residues modulo $n$](lean:Int.quotientZMultiplesNatEquivZMod).
- **Sign of a permutation.** The [alternating group](trough:alternatingGroup) $A_n$
  [is the kernel](lean:alternatingGroup_eq_sign_ker) of the [sign homomorphism](trough:Equiv.Perm.sign) from the symmetric
  group $S_n$ to $\{\pm 1\}$, and [the sign is onto when $n \ge 2$](lean:Equiv.Perm.sign_surjective).
  Hence $S_n/A_n \cong \{\pm 1\}$, and $A_n$ has index $2$.
- **Determinant.** The [determinant](trough:Matrix.det) maps the
  [general linear group](trough:Matrix.GeneralLinearGroup) $\mathrm{GL}_n(F)$, for $n \ge 1$, over a field $F$ onto the
  multiplicative group $F^\times$, with kernel the [special linear group](trough:Matrix.SpecialLinearGroup),
  so $\mathrm{GL}_n(F)/\mathrm{SL}_n(F) \cong F^\times$.
- **The circle.** The map $t \mapsto e^{2\pi i t}$ from the additive group of real numbers onto
  the unit circle in $\mathbb{C}$ has kernel $\mathbb{Z}$, so $\mathbb{R}/\mathbb{Z}$ is isomorphic to the circle group.

## Consequences

- **Normal subgroups are kernels.** Conversely, every normal
  subgroup $N$ is a kernel: [the quotient map $G \to G/N$ has kernel exactly $N$](lean:QuotientGroup.ker_mk').
- **Counting.** Comparing sizes on both sides, the [index](trough:Subgroup.index) of the kernel
  [equals the order of the image](lean:Subgroup.index_ker). Combined with
  [Lagrange's theorem](trough:Subgroup.card_subgroup_dvd_card) in its product form,
  [the order of a group is the order of a subgroup $L$ times its index](lean:Subgroup.card_mul_index),
  $|G| = |L|\,[G:L]$, this gives
  [$|G| = |\ker\varphi|\,|\varphi(G)|$](lean:Subgroup.card_ker_mul_card_range), so for a finite group $G$
  [the order of the image divides $|G|$](lean:Subgroup.card_range_dvd).
- **Homomorphic images.** Up to isomorphism, the homomorphic images of $G$ are exactly
  the quotients $G/N$ by normal subgroups $N$. In particular a
  [simple group](trough:IsSimpleGroup) has no images other than itself and the trivial group.

## Generalizations

The same argument works wherever a structure has a notion of quotient by a
"kernel". For rings, the quotient of a ring by the kernel of a ring homomorphism
[is isomorphic to its image](lean:RingHom.quotientKerEquivRange) (see the
[first isomorphism theorem for rings](trough:RingHom.quotientKerEquivOfSurjective)). For modules,
the quotient by the [kernel of a linear map](trough:LinearMap.ker)
[is linearly isomorphic to its range](lean:LinearMap.quotKerEquivRange), which for vector spaces
yields the [rank–nullity theorem](trough:LinearMap.rank_range_add_rank_ker). At the bottom of the
hierarchy, any function from a set $X$ induces an equivalence relation on $X$, and
[the set of its classes is in bijection with the image](lean:Setoid.quotientKerEquivRange).
In universal algebra and category theory the theorem takes the form of a factorization
of a morphism through its image.

## In Mathlib

Mathlib gives the theorem as a construction rather than an existence statement: it
builds a specific isomorphism of groups from the quotient by the kernel to the image,
where the image is regarded as a group in its own right, a subgroup of the codomain.
The isomorphism is assembled from a bijective homomorphism, so its inverse is not given
by an explicit formula and the definition is marked noncomputable. A computable variant of the surjective case, an
isomorphism onto the whole codomain, [exists for a homomorphism equipped with a right
inverse](lean:QuotientGroup.quotientKerEquivOfRightInverse). The version for additive
groups is generated automatically from the multiplicative one. In the counting
statements, Mathlib assigns size $0$ to an infinite set and index $0$ to a subgroup of
infinite index, so the statements hold for all groups without finiteness hypotheses. For an
infinite group the statements still say something: the index of the kernel is infinite
exactly when the image is, and the product formula says that the kernel or the image is
infinite. Only the divisibility statement becomes vacuous, since every number divides $0$.

## Depends on

- [Group morphism](trough:MonoidHom)
- [Normal subgroup](trough:Subgroup.Normal)
- [Quotient group](trough:QuotientGroup.Quotient.group)
- [Subgroup](trough:Subgroup)
