---
article_id: af_111e78458bc90b0ad55478bd
concept: undergrad:Group Theory/Representation theory of finite groups/Fourier transform for finite abelian groups
---

The **Fourier transform for finite abelian groups** expresses a complex-valued
function on a finite abelian [group](trough:Group) $G$ as a combination of the
characters of $G$, the homomorphisms from $G$ to the nonzero complex numbers. It is
the finite counterpart of [Fourier series](trough:fourierCoeff) and of the
[Fourier transform](trough:FourierTransform.fourierCLM) on the real line: the
inversion formula, Plancherel's identity and the convolution theorem all hold, but
every integral becomes a finite sum and no question of convergence arises. For the
cyclic group $\mathbb{Z}/N\mathbb{Z}$ it is the discrete Fourier transform, and it is
a standard tool in number theory, additive combinatorics and the analysis of
Boolean functions.

## Definition

Write the finite abelian group $G$ additively and let $n = |G|$. A **character** of
$G$ is a map $\chi : G \to \mathbb{C}^\times$ with $\chi(x + y) = \chi(x)\chi(y)$ for
all $x, y \in G$, that is, a [group morphism](trough:MonoidHom) into the
multiplicative group of $\mathbb{C}$. Since every element of $G$ has finite order,
the values of a character are [roots of unity](trough:Complex.mem_rootsOfUnity); in
particular [$|\chi(x)| = 1$ for every $x$](lean:AddChar.norm_apply) and
[$\chi(-x) = \overline{\chi(x)}$](lean:AddChar.map_neg_eq_conj). Under pointwise
multiplication the characters form a group $\widehat{G}$, the
dual group
of $G$.

The Fourier transform of a function $f : G \to \mathbb{C}$ is the function
$\widehat{f}$ on $\widehat{G}$ given by

$$\widehat{f}(\chi) = \sum_{x \in G} f(x)\,\overline{\chi(x)}.$$

Other conventions divide by $n$ or by $\sqrt{n}$, or use $\chi(x)$ in place of its
conjugate. They move constant factors between the transform and its inverse, or
relabel the characters, and change nothing else.

## Properties

Let $f, g : G \to \mathbb{C}$.

- **Orthogonality.** [The sum of a character over $G$ is $n$ for the trivial
  character and $0$ for every other character](lean:AddChar.sum_eq_ite). Applied to
  the character $\overline{\chi}\psi$, this shows that
  [characters $\chi, \psi$ satisfy $\frac{1}{n}\sum_{x \in G} \overline{\chi(x)}\,\psi(x) = 1$ if $\chi = \psi$ and $0$ otherwise](lean:AddChar.wInner_cWeight_eq_boole).
- **Counting.** [$G$ has exactly $n$ characters](lean:AddChar.card_eq), and
  [they form a basis of the space of functions from $G$ to $\mathbb{C}$](lean:AddChar.complexBasis).
  Dually, [$\sum_{\chi \in \widehat{G}} \chi(x)$ equals $n$ if $x = 0$ and $0$ otherwise](lean:AddChar.sum_apply_eq_ite).
- **Inversion.** Every function is recovered from its transform:
  $$f(x) = \frac{1}{n} \sum_{\chi \in \widehat{G}} \widehat{f}(\chi)\,\chi(x).$$
- **Plancherel's identity.**
  $$\sum_{x \in G} f(x)\,\overline{g(x)} = \frac{1}{n} \sum_{\chi \in \widehat{G}} \widehat{f}(\chi)\,\overline{\widehat{g}(\chi)}.$$
  With $g = f$ this says $\sum_x |f(x)|^2 = \frac{1}{n}\sum_\chi |\widehat{f}(\chi)|^2$.
- **Convolution.** The
  convolution
  $(f * g)(x) = \sum_{y \in G} f(y)\,g(x - y)$
  satisfies $\widehat{f * g} = \widehat{f}\,\widehat{g}$.
- **Translation.** If $f_a(x) = f(x - a)$, then
  $\widehat{f_a}(\chi) = \overline{\chi(a)}\,\widehat{f}(\chi)$.

## Examples

- **Cyclic groups.** For $N \ge 1$ and $k \in \mathbb{Z}/N\mathbb{Z}$, the map
  $\chi_k(j) = e^{2\pi i jk/N}$ is a character of $\mathbb{Z}/N\mathbb{Z}$, and
  [$k \mapsto \chi_k$ is an isomorphism from $\mathbb{Z}/N\mathbb{Z}$ onto its group of characters](lean:AddChar.zmodAddEquiv).
  Labelling characters this way gives the discrete Fourier transform
  $$\widehat{f}(k) = \sum_{j \in \mathbb{Z}/N\mathbb{Z}} f(j)\, e^{-2\pi i jk/N},$$
  whose inverse is $f(j) = \frac{1}{N}\sum_k \widehat{f}(k)\, e^{2\pi i jk/N}$.
- **The Boolean cube.** The characters of $(\mathbb{Z}/2\mathbb{Z})^m$ are the maps
  $\chi_a(x) = (-1)^{a_1 x_1 + \cdots + a_m x_m}$ for $a \in (\mathbb{Z}/2\mathbb{Z})^m$,
  and the transform $\widehat{f}(a) = \sum_x (-1)^{a \cdot x} f(x)$ is the
  Walsh–Hadamard transform.
- **Subgroups.** For a subgroup $H$ of $G$ with indicator function $1_H$,
  $\widehat{1_H}(\chi)$ equals $|H|$ if $\chi$ is trivial on $H$ and $0$ otherwise.
  Plancherel's identity with $g = 1_H$ then gives the finite Poisson summation
  formula $\sum_{h \in H} f(h) = \frac{|H|}{n} \sum \widehat{f}(\chi)$, the sum
  running over the characters trivial on $H$.
- **Gauss sums.** If $\chi$ is a primitive Dirichlet character modulo $N$, viewed as
  a function on $\mathbb{Z}/N\mathbb{Z}$, then
  [its discrete Fourier transform at $k$ is $\chi^{-1}(-k)\,\tau(\chi)$](lean:DirichletCharacter.IsPrimitive.fourierTransform_eq_inv_mul_gaussSum),
  where $\chi^{-1}$ is the inverse Dirichlet character and
  $\tau(\chi) = \sum_a \chi(a)\, e^{2\pi i a/N}$ is the Gauss sum.

## Proof

Orthogonality: if $\chi$ is not trivial, choose $a$ with $\chi(a) \neq 1$. Since
$x \mapsto x + a$ permutes $G$, the sum $S = \sum_x \chi(x)$ satisfies
$S = \chi(a) S$, so $S = 0$. Applied to $\overline{\chi}\psi$, which is nontrivial
when $\chi \neq \psi$, this shows that distinct characters are orthogonal for the
inner product $\sum_x f(x)\overline{g(x)}$. Orthogonal nonzero functions are
linearly independent,
so there are at most $n$ characters. For $\mathbb{Z}/N\mathbb{Z}$ the $N$ characters
$\chi_k$ are distinct. By the
[structure theorem](trough:AddCommGroup.equiv_free_prod_directSum_zmod) every finite
abelian group is a direct sum of cyclic groups. Products of characters of the
summands are characters of the direct sum, and distinct tuples of characters of the
summands give distinct product characters, so $G$ has at least, hence exactly, $n$
characters. They
are therefore an orthogonal basis of the $n$-dimensional space of functions on $G$,
each of squared length $n$ for this inner product. The
coefficient of $\chi$ when $f$ is expanded in this basis is $\widehat{f}(\chi)/n$,
which is the inversion formula, and Plancherel's identity is the expression of the
inner product in an orthogonal basis. The convolution theorem follows by substituting
$z = x - y$ in the double sum defining $\widehat{f * g}$.

## Related concepts

Every irreducible complex representation of a finite abelian group is
one-dimensional and is given by a character, so the expansion above is the abelian
case of the expansion of class functions in the
orthonormal basis of irreducible characters;
see also
representations of abelian groups.
Fourier series on the circle and the Fourier transform on the real line are the
analogous theories for other locally compact abelian groups. The finite form of
Pontryagin duality says that
[the map sending $x$ to the character $\chi \mapsto \chi(x)$ of $\widehat{G}$ is an isomorphism from $G$ onto the dual of $\widehat{G}$](lean:AddChar.doubleDualEquiv).
The computational side is treated in
discrete Fourier transform on a finite abelian group
and fast Fourier transform.

## In Mathlib

Mathlib treats characters as [additive characters](lean:AddChar): maps from an
additive monoid to a multiplicative monoid that send $0$ to $1$ and sums to products.
A character of $G$ in the sense above is an additive character with values in
$\mathbb{C}$. The group of characters carries both a multiplicative and an additive
structure, which agree; the results cited here mostly use the additive one, with the
trivial character as its zero. Orthogonality is stated with the averaged inner
product and holds for values in the real or complex numbers; the sum formula holds
for values in any integral domain. The count of characters, the basis of characters,
the dual orthogonality relation and the double dual isomorphism are proved for every
finite abelian group. The Fourier transform itself is defined only for
$\mathbb{Z}/N\mathbb{Z}$ with $N \ge 1$: [the discrete Fourier transform](lean:ZMod.dft)
is bundled as a linear equivalence on functions with values in any complex vector
space, with
[the sign convention $\widehat{f}(k) = \sum_j e^{-2\pi i jk/N} f(j)$](lean:ZMod.dft_apply)
used above. Mathlib proves
that [its inverse sends $g$ to $k \mapsto \frac{1}{N}\sum_j e^{2\pi i jk/N} g(j)$](lean:ZMod.invDFT_apply), that
[applying the transform twice sends $f$ to $j \mapsto N f(-j)$](lean:ZMod.dft_dft),
and that, for values in a complete normed complex vector space,
[it agrees with Mathlib's general Fourier integral for the counting measure](lean:ZMod.dft_eq_fourier).
It has no Fourier transform indexed by the characters of an arbitrary finite abelian
group (only the general Fourier integral, not specialized to this setting),
and it has no Plancherel identity or convolution theorem in this finite setting.

## Depends on

- [Group](trough:Group)
- [Group morphism](trough:MonoidHom)
- [Complex number](trough:Complex)

## Proof depends on

- [Structure of finitely generated abelian groups](trough:AddCommGroup.equiv_free_prod_directSum_zmod)
- [Basis](trough:Module.Basis)
