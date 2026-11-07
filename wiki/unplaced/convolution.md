The **convolution** of two functions $f$ and $g$ on a finite [group](trough:Group) $G$ is the function $f * g$ whose value at $x$ adds up the products $f(a)\,g(b)$ over all ways of writing $x = ab$. It turns the space of functions on $G$ into an associative algebra, the group algebra, in which the product of the point masses at $s$ and $t$ is the point mass at $st$. Representations of $G$ are the modules over this algebra, its centre consists of the class functions, and for an abelian group the Fourier transform turns convolution into pointwise multiplication.

## Definition

Let $G$ be a finite group and $R$ a commutative [ring](trough:Ring), for instance the complex numbers. For functions $f, g \colon G \to R$, the convolution $f * g \colon G \to R$ is

$$(f * g)(x) = \sum_{\substack{a, b \in G \\ ab = x}} f(a)\,g(b) = \sum_{y \in G} f(y)\,g(y^{-1}x).$$

The second form comes from parametrizing the pairs with $ab = x$ by $a = y$, $b = y^{-1}x$. Parametrizing by $b$ instead gives the equivalent form $\sum_{y} f(xy^{-1})\,g(y)$.

For each $s \in G$ let $\delta_s$ be the function equal to $1$ at $s$ and $0$ elsewhere. Every function is a combination $f = \sum_s f(s)\,\delta_s$, and convolution is the bilinear operation determined by $\delta_s * \delta_t = \delta_{st}$. Written this way, the definition also makes sense for an infinite group, provided one restricts to [finitely supported functions](trough:Finsupp); the resulting ring $R[G]$ is the group algebra, in which the product of $f$ and $g$ is $\sum_{a, b} f(a)\,g(b)\,\delta_{ab}$, summed over the finitely many $a$ and $b$ where $f$ and $g$ are nonzero. In it $(r\delta_s) * (r'\delta_t) = rr'\,\delta_{st}$, and the value of $f * g$ at $x$ is the sum of $f(y)\,g(y^{-1}x)$ over the finitely many $y$ with $f(y) \neq 0$; equivalently, it is the sum of $f(xy^{-1})\,g(y)$ over the $y$ with $g(y) \neq 0$.

## Examples

- **Translation.** Convolving with a point mass translates: $(r\delta_s * f)(x) = r\,f(s^{-1}x)$. With $s = e$, the identity of $G$, and $r = 1$ this gives $\delta_e * f = f$; indeed the identity of the group algebra is $\delta_e$.
- **Counting products.** If $A$ and $B$ are subsets of $G$ with indicator functions $1_A$ and $1_B$, then $(1_A * 1_B)(x)$ is the number of pairs $(a, b) \in A \times B$ with $ab = x$. Mathlib defines this counting function for finite subsets of a group directly.
- **Random products.** If $f$ and $g$ are probability distributions on $G$ and $X$, $Y$ are independent random elements with these distributions, then $f * g$ is the distribution of $XY$. Repeated convolution therefore describes random walks on groups, such as repeated card shuffles in a symmetric group.
- **Cyclic groups.** On the cyclic group $\mathbb{Z}/n\mathbb{Z}$, written additively, $(f * g)(k) = \sum_j f(j)\,g(k - j)$, the cyclic convolution of signal processing. The group algebra is isomorphic to $R[x]/(x^n - 1)$, with $\delta_k$ corresponding to $x^k$.
- **Beyond groups.** The same recipe works over a monoid. Over the natural numbers under addition it is multiplication of [polynomials](trough:Polynomial): the coefficient of $x^n$ in $pq$ is $\sum_{i + j = n} p_i\,q_j$. Over the positive integers under multiplication it is Dirichlet convolution of [arithmetic functions](trough:ArithmeticFunction): for $n \geq 1$, $(f * g)(n)$ is the sum of $f(a)\,g(b)$ over the pairs of positive integers with $ab = n$.

## Properties

- **Ring structure.** Expanding both sides, $((f * g) * h)(x)$ and $(f * (g * h))(x)$ both equal the sum of $f(a)\,g(b)\,h(c)$ over all triples with $abc = x$. Hence convolution is associative. It is also bilinear, so it distributes over addition, and the group algebra $R[G]$ is a ring whose identity is $\delta_e$.
- **Commutativity.** If $G$ is abelian, $R[G]$ is a commutative ring. Conversely, if $st \neq ts$ and $R$ is not the zero ring, then $\delta_s * \delta_t = \delta_{st}$ differs from $\delta_t * \delta_s = \delta_{ts}$.
- **The centre.** A function $f$ commutes with every function under convolution exactly when it commutes with each $\delta_s$, which says $f(sxs^{-1}) = f(x)$ for all $s$ and $x$. So the centre of $R[G]$ consists of the class functions, those constant on each [conjugacy class](trough:ConjClasses).
- **Representations.** A [representation](trough:Representation) of $G$ on a vector space $V$ over a field $k$ extends linearly to an action of $k[G]$ on $V$, and conversely; representations of $G$ are the same thing as $k[G]$-modules. In this language [Maschke's theorem](trough:MonoidAlgebra.Submodule.exists_isCompl) says that when the characteristic of $k$ does not divide $|G|$, every submodule of a $k[G]$-module has a complementary submodule.
- **Characters.** For irreducible complex [characters](trough:FDRep.character) $\chi$ and $\psi$ of $G$, one has $\chi * \psi = 0$ when $\chi \neq \psi$, and $\chi * \chi = (|G|/\chi(e))\,\chi$. This refines the orthogonality of irreducible characters, which is its value at $x = e$.
- **Fourier transform.** Let $G$ be a finite abelian group, and for a character $\chi \colon G \to \mathbb{C}^\times$ put $\hat f(\chi) = \sum_{x} f(x)\,\overline{\chi(x)}$. Substituting $x = yz$ gives

$$\widehat{f * g}(\chi) = \hat f(\chi)\,\hat g(\chi),$$

so the Fourier transform turns convolution into pointwise multiplication of functions on the dual group.

## Related concepts

On a locally compact group the sum is replaced by an integral against Haar measure. Mathlib's [convolution in analysis](trough:MeasureTheory.convolution) is the integral of $L(f(t), g(x - t))$ over $t$ against a measure on an additive group, for a continuous bilinear map $L$. Its values lie in normed spaces, so for real or complex values, with $L$ the product of scalars and the counting measure on a finite abelian group in which every subset is measurable, it recovers the sum above.

## In Mathlib

Mathlib's group algebra is the monoid algebra over a semiring, defined for any monoid, finite or not, as the finitely supported functions with multiplication given by bilinear extension of the rule for point masses; the coefficient formulas above are theorems about it. It is a ring when the coefficients form a ring and commutative when both the monoid and the coefficients are. Separately, Mathlib has a convolution of arbitrary functions on a monoid with values in a semiring carrying a topology, the possibly infinite sum of $f(a)\,g(b)$ over the pairs with $ab = x$; by Mathlib's convention for infinite sums its value is $0$ where the sum does not converge. No continuity of the ring operations is assumed. For it Mathlib proves that $\delta_e$ is a left and a right identity, that convolution distributes over addition on the left and on the right when the topology is Hausdorff, addition is continuous and the sums involved converge, and that convolution is commutative over a commutative monoid with commutative values, but not associativity, and it does not connect this operation to the multiplication of the monoid algebra. Its finite-sum formula needs an explicit finite list of the factorizations of each element, which Mathlib does not provide for finite groups. Mathlib also lacks the description of the centre of the group algebra by class functions, the convolution identities for characters, and the convolution theorem for the Fourier transform on finite abelian groups, including its discrete Fourier transform on $\mathbb{Z}/n\mathbb{Z}$.

## Depends on

- [Group](trough:Group)
- [Ring](trough:Ring)
