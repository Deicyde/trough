# Hensel's lemma (for $\mathbb{Z}_p$)

**Hensel's lemma** for the [$p$-adic integers](../numbers/p-adic-integer.md) $\mathbb{Z}_p$ says that an
approximate root of a [polynomial](../polynomials-and-power-series/polynomial-in-one-indeterminate.md) can be refined to an exact root,
provided the approximation is good compared with the size of the
[derivative](../../../undergraduate/ring-theory/polynomial-rings/polynomial-derivative.md) at that point. In its most used form it says that a
root modulo a [prime](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md) $p$ at which the derivative is nonzero modulo $p$ lifts
to a unique root in $\mathbb{Z}_p$ congruent to it modulo $p$, and so to a root modulo every power of $p$. It is the
basic tool for deciding which polynomial equations have $p$-adic solutions, and the
model for the notion of a Henselian ring.

## Statement

Let $p$ be a prime, let $|\cdot|$ be the $p$-adic norm on $\mathbb{Z}_p$, normalized so that
[$|p| = 1/p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicIntegers.html#PadicInt.norm_p), and let $F$ be a polynomial with coefficients in
$\mathbb{Z}_p$, with derivative $F'$. Suppose $a \in \mathbb{Z}_p$ satisfies

$$|F(a)| < |F'(a)|^2.$$

Then [there is a $z \in \mathbb{Z}_p$ with $F(z) = 0$, $|z - a| < |F'(a)|$ and $|F'(z)| = |F'(a)|$, and $z$ is the only root of $F$ with $|z - a| < |F'(a)|$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/Hensel.html#hensels_lemma).
The hypothesis forces $F'(a) \neq 0$. A sharper bound also holds: $|z - a| = |F(a)|/|F'(a)|$.

**Simple roots modulo $p$.** [Every $p$-adic integer has norm at most $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicIntegers.html#PadicInt.norm_le_one),
and [an element of $\mathbb{Z}_p$ has norm less than $1$ exactly when it is divisible by $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicIntegers.html#PadicInt.norm_lt_one_iff_dvd).
So if $F(a) \equiv 0 \pmod p$ and $F'(a) \not\equiv 0 \pmod p$, then $|F(a)| < 1 = |F'(a)|^2$,
and the theorem gives a unique root $z$ of $F$ with $z \equiv a \pmod p$. When $F$ has integer
coefficients, reducing $z$ modulo $p^k$ gives a solution of $F(x) \equiv 0 \pmod{p^k}$ for every
$k \ge 1$, all congruent to $a$ modulo $p$.

## Examples

- **Square roots for odd $p$.** Let $p$ be odd and $u \in \mathbb{Z}_p$ not divisible by $p$ that
  is a square modulo $p$, say $a^2 \equiv u \pmod p$ with $a \in \mathbb{Z}$. For $F = X^2 - u$ the derivative $F'(a) = 2a$ is
  not divisible by $p$, so $u$ has a square root in $\mathbb{Z}_p$ congruent to $a$. For instance
  $3^2 \equiv 2 \pmod 7$, so $2$ is a square in $\mathbb{Z}_7$. Hence for odd $p$ a unit of
  $\mathbb{Z}_p$ is a square exactly when it is a square modulo $p$.
- **Square roots in $\mathbb{Z}_2$.** For $p = 2$ the derivative $2X$ is always divisible by $2$,
  so the simple-root form never applies, but the general form does. If $u \equiv 1 \pmod 8$ and
  $a = 1$, then $|F(1)| = |1 - u| \le 1/8 < 1/4 = |2|^2$, so $u$ has a square root $z$ in
  $\mathbb{Z}_2$ with $z \equiv 1 \pmod 4$.
- **Roots of unity.** Take $F = X^{p-1} - 1$ and $a \in \{1, \dots, p-1\}$. By
  [Fermat's little theorem](../../../thousand-plus/number-theory/part-01/fermats-little-theorem.md) $F(a) \equiv 0 \pmod p$, while
  $F'(a) = (p-1)a^{p-2}$ is not divisible by $p$. Each $a$ therefore lifts to a root of $F$, and the
  $p - 1$ lifts lie in different residue classes. So $\mathbb{Z}_p$ contains $p - 1$ distinct
  $(p-1)$-th roots of unity, one in each nonzero residue class modulo $p$.
- **A failure.** The polynomial $X^2 - 3$ has the root $1$ modulo $2$, but $3$ is not a square in
  $\mathbb{Z}_2$, since the square of a unit of $\mathbb{Z}_2$ is congruent to $1$ modulo $8$. The
  hypothesis fails at every $a$: for odd $a$ one has $|a^2 - 3| = 1/2$, which is not less than
  $|2a|^2 = 1/4$, and for even $a$ one has $|a^2 - 3| = 1$.

## Proof

The proof is Newton's method in the $p$-adic metric. Put $a_0 = a$ and
$t = |F(a)|/|F'(a)|^2 < 1$, and define

$$a_{n+1} = a_n - \frac{F(a_n)}{F'(a_n)}.$$

Expanding $F$ around $x$ gives $F(x + h) = F(x) + F'(x)h + h^2 G(x, h)$, where $G$ is a polynomial
with coefficients in $\mathbb{Z}_p$, so $|G(x, h)| \le 1$ for $x, h \in \mathbb{Z}_p$. Likewise
$|F'(x) - F'(y)| \le |x - y|$, an instance of the fact that
[a polynomial over $\mathbb{Z}_p$ does not increase $p$-adic distances](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/Hensel.html#padic_polynomial_dist).
By induction on $n$ one shows that $a_n \in \mathbb{Z}_p$, that $|F'(a_n)| = |F'(a)|$, and that
$|F(a_n)| \le |F'(a)|^2 t^{2^n}$: the step $h = -F(a_n)/F'(a_n)$ kills the linear term, leaving
$|F(a_{n+1})| \le |h|^2$, and the derivative keeps its norm because it moves by less than its own
size, by the [ultrametric inequality](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicIntegers.html#PadicInt.nonarchimedean)
$|x + y| \le \max(|x|, |y|)$, which gives $|x + y| = |x|$ whenever $|y| < |x|$.

The steps satisfy $|a_{n+1} - a_n| \le |F'(a)|\, t^{2^n}$, which tends to $0$. In an ultrametric
space this makes $(a_n)$ a [Cauchy sequence](../../topology/uniform-notions/cauchy-sequence.md), and since
[$\mathbb{Z}_p$ is complete](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicIntegers.html#PadicInt.completeSpace) it converges to some $z$. By continuity
$F(z) = 0$ and $|F'(z)| = |F'(a)|$, and the ultrametric inequality bounds $|z - a|$ by the first
step $|F(a)|/|F'(a)|$, which is less than $|F'(a)|$.

For uniqueness, let $z'$ be another root with $|z' - a| < |F'(a)|$ and put $h = z' - z$, so that
$|h| < |F'(a)| = |F'(z)|$. Then $0 = F(z + h) = h\,(F'(z) + h\,G(z, h))$, and the second factor is
nonzero because $|h\,G(z, h)| \le |h| < |F'(z)|$. Hence $h = 0$.

## Generalizations

The same argument works over the valuation ring $\{x : |x| \le 1\}$ of any field complete for a
nonarchimedean absolute value. Abstracting the simple-root form leads to Henselian rings.
A commutative ring $R$ is
[Henselian at an ideal $I$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Henselian.html#HenselianRing) if $I$ is contained in the Jacobson radical of $R$
and, for every monic polynomial $f$ over $R$ and every $a_0 \in R$ with $f(a_0) \in I$ and
$f'(a_0)$ invertible modulo $I$, there is a root $a$ of $f$ with $a - a_0 \in I$. A
[local ring](../rings/local-ring.md) is
[a Henselian local ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Henselian.html#HenselianLocalRing) when this holds for its maximal ideal.
Every ring that is complete and Hausdorff for the $I$-adic topology is Henselian at $I$; in
particular $\mathbb{Z}_p$, complete for the $p\mathbb{Z}_p$-adic topology, is a Henselian local
ring. Stronger versions of the lemma lift factorizations of monic polynomials into coprime factors, not
just simple roots, from the residue field to the ring.

## In Mathlib

Mathlib proves the lemma in the general form above, with all four conclusions (existence,
distance to $a$, norm of the derivative, uniqueness) packaged in one statement, which needs no
separate case for $F(a) = 0$ (the root is then $a$ itself). The polynomial may have coefficients
in any commutative semiring that maps into $\mathbb{Z}_p$ as an algebra, such as the integers or
$\mathbb{Z}_p$ itself, and it is evaluated at $p$-adic integers through that map. The norm is the
$p$-adic norm with $|p| = 1/p$. The published statement records only the strict bound
$|z - a| < |F'(a)|$, not the sharper equality. Separately, Mathlib's theory of Henselian rings
states its conditions for monic polynomials, and records that fields are Henselian local rings
and that adically complete rings are Henselian, which covers $\mathbb{Z}_p$ as well.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [$p$-adic integer](../numbers/p-adic-integer.md)
- [Polynomial in one indeterminate](../polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Polynomial derivative](../../../undergraduate/ring-theory/polynomial-rings/polynomial-derivative.md)
- [Prime numbers](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)

## Proof depends on

- [Cauchy sequence](../../topology/uniform-notions/cauchy-sequence.md)
- [Completeness](../../topology/uniform-notions/completeness.md)
- [Continuous function](../../topology/general-topology/part-01/continuous-function.md)

## Sources

- [Mathlib documentation: `hensels_lemma`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/Hensel.html#hensels_lemma)
- [Source of `hensels_lemma` in Mathlib/NumberTheory/Padics/Hensel.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/NumberTheory/Padics/Hensel.lean#L460)
- [Mathlib overview: General algebra › Number theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L150)
