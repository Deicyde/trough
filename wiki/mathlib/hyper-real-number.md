---
article_id: af_134479273ab6c3f42eb412b0
concept: Hyperreal
---

The **hyper-real numbers**, or hyperreals, form an ordered [field](trough:Field) $^*\mathbb R$
that contains the [real numbers](trough:Real) together with positive infinitesimals, numbers
greater than $0$ but smaller than every positive real, and infinite elements, numbers larger than
every real.
They are the number system of nonstandard analysis. In $^*\mathbb R$ a derivative can be computed
from a quotient of infinitesimal changes and a limit can be found by rounding a hyper-real number
to the nearest real, which makes arguments with infinitesimals rigorous.

## Definition

The usual construction is an ultrapower of $\mathbb R$. An ultrafilter on the
[natural numbers](trough:Nat) is a [filter](trough:Filter) $\mathcal U$ of subsets of
$\mathbb N$, not containing the empty set, such that for every $A \subseteq \mathbb N$ either $A$
or its complement belongs to $\mathcal U$. It is nonprincipal if it contains no finite set, or
equivalently every set with finite complement. Nonprincipal ultrafilters exist by the axiom of
choice; Mathlib fixes one, its hyperfilter, which
[contains every set with finite complement](lean:Filter.hyperfilter_le_cofinite). A set in
$\mathcal U$ is thought of as containing almost all indices.

Two real sequences $(a_n)$ and $(b_n)$ are identified when $\{n : a_n = b_n\} \in \mathcal U$. A
hyper-real number is an equivalence class $[a_n]$, and
[the hyper-real numbers](lean:Hyperreal) are the set of all such classes:
[each sequence defines one](lean:Hyperreal.ofSeq) and
[every hyper-real number comes from a sequence](lean:Hyperreal.ofSeq_surjective). Arithmetic is
termwise,

$$[a_n] + [b_n] = [a_n + b_n], \qquad [a_n]\,[b_n] = [a_n b_n],$$

and [$[a_n] < [b_n]$ exactly when $\{n : a_n < b_n\} \in \mathcal U$](lean:Hyperreal.ofSeq_lt_ofSeq).
The order is total because the three sets where $a_n < b_n$, $a_n = b_n$ and $a_n > b_n$
partition $\mathbb N$, so exactly one of them lies in $\mathcal U$. If $[a_n] \neq 0$ then
$a_n \neq 0$ for almost all $n$, and inverting those terms gives the inverse. With these
operations $^*\mathbb R$ is an ordered field.

A real number $r$ is sent to the class of the constant sequence $(r, r, r, \dots)$.
[This embedding](lean:Hyperreal.ofReal) is
[an order-preserving ring homomorphism](lean:Hyperreal.coeRingHom), it is
[injective](lean:Hyperreal.coe_eq_coe), and
[$r < s$ holds in $^*\mathbb R$ exactly when it holds in $\mathbb R$](lean:Hyperreal.coe_lt_coe).

## Examples

Let $\omega = [0, 1, 2, 3, \dots]$ be [the class of the sequence $(n)$](lean:Hyperreal.omega).
For a real $r$, all but finitely many $n$ satisfy $n > r$, and that set lies in $\mathcal U$, so
[$r < \omega$ for every real $r$](lean:Hyperreal.coe_lt_omega). Its reciprocal $\varepsilon$ is
[the class of the sequence $(1/n)$](lean:Hyperreal.epsilon); changing finitely many terms never
changes a class, so the term at $n = 0$ does not matter. Indeed
[the reciprocal of $\omega$ is $\varepsilon$](lean:Hyperreal.inv_omega), and $\varepsilon$
[is positive](lean:Hyperreal.epsilon_pos) and
[smaller than every positive real](lean:Hyperreal.epsilon_lt_of_pos). Further examples are
$\omega + 1$, $\omega^2$ and $[\sqrt n]$, all infinite, and $\varepsilon^2$, an infinitesimal
smaller than $\varepsilon$; the numbers $r + \varepsilon$ and $r - \varepsilon$ differ from the
real $r$ by an infinitesimal.

## Properties

A hyper-real number $x$ is infinitesimal if $|x| < r$ for every positive real $r$ (so $0$ is
infinitesimal), finite if $|x| < r$ for some real $r$, and infinite otherwise. Two hyper-real
numbers are infinitely close if their difference is infinitesimal. Sums of
infinitesimals and products of an infinitesimal with a finite number are infinitesimal, and the
reciprocal of a nonzero infinitesimal is infinite.

- **Not Archimedean.** Since $\omega$ exceeds every natural number, $^*\mathbb R$ is not an
  Archimedean field.
- **Not complete.** The infinitesimals form a nonempty set bounded above by $1$ with no least
  upper bound. An upper bound $s$ is at least $\varepsilon > 0$; it cannot be infinitesimal, since
  $2s$ would then be a larger infinitesimal. So $s \ge r$ for some positive real $r$, and then
  $s/2$ is a smaller upper bound.
- **Standard part.** Every finite $x$ is infinitely close to exactly one real number, its standard
  part $\operatorname{st}(x)$: [for finite $x$ and real $r$, the difference $x - r$ is
  infinitesimal exactly when $r = \operatorname{st}(x)$](lean:ArchimedeanClass.mk_sub_pos_iff).
  The completeness of $\mathbb R$ supplies it:
  [$\operatorname{st}(x)$ is the supremum of the reals below $x$](lean:ArchimedeanClass.stdPart_eq_sSup).
  For finite $x$ and $y$,
  [$\operatorname{st}(x + y) = \operatorname{st}(x) + \operatorname{st}(y)$](lean:ArchimedeanClass.stdPart_add)
  and [$\operatorname{st}(xy) = \operatorname{st}(x)\operatorname{st}(y)$](lean:ArchimedeanClass.stdPart_mul),
  and [$\operatorname{st}(r) = r$ for real $r$](lean:Hyperreal.stdPart_coe).
- **Limits.** A sequence tends to $L$ along $\mathcal U$ if, for every neighbourhood $V$ of $L$,
  the set of $n$ with $a_n \in V$ lies in $\mathcal U$. [If $(a_n)$ tends to $L$ along
  $\mathcal U$, then $\operatorname{st}([a_n]) = L$](lean:Hyperreal.stdPart_of_tendsto). Since
  $\mathcal U$ contains every set with finite complement, this covers every sequence with
  [limit](trough:Metric.tendsto_atTop) $L$ in the usual sense. Likewise
  [$(a_n)$ tends to $+\infty$ along $\mathcal U$ exactly when $[a_n]$ is positive and
  infinite](lean:Hyperreal.tendsto_atTop_iff).
- **Continuity.** For a real function $f$ that is [continuous](trough:Continuous) at the point $r$,
  [if $(a_n)$ tends to $r$ along $\mathcal U$, then $(f(a_n))$ tends to $f(r)$ along
  $\mathcal U$](lean:Hyperreal.stdPart_map).
- **Transfer.** Because $^*\mathbb R$ is an ultrapower, [Łoś' theorem](trough:FirstOrder.Language.Ultraproduct.sentence_realize)
  applies: [a first-order sentence holds in an ultraproduct of nonempty structures exactly when
  the set of indices whose factor satisfies it belongs to the ultrafilter](lean:FirstOrder.Language.Ultraproduct.sentence_realize).
  Every factor here is $\mathbb R$, so a first-order sentence in a language with a symbol for each
  real function and relation holds in $^*\mathbb R$ exactly when it holds in $\mathbb R$, where
  each function $f$ is read as its termwise extension $f^*[a_n] = [f(a_n)]$ and each relation $P$
  as the set of classes $[a_n]$ with $P(a_n)$ for almost all $n$. For example, a real function $f$ has
  [derivative](trough:HasDerivAt) $L$ at a real $x$ exactly when
  $(f^*(x + \delta) - f(x))/\delta$ is infinitely close to $L$ for every nonzero infinitesimal
  $\delta$. Transfer does not reach statements that quantify over arbitrary subsets, which is why
  completeness fails.

If the continuum hypothesis holds, all nonprincipal ultrafilters on $\mathbb N$ yield isomorphic
ordered fields.

## Related concepts

The [extended real numbers](trough:EReal) add only $+\infty$ and $-\infty$ to $\mathbb R$ and do
not form a field. Infinitesimal and infinite elements make sense in any
[ordered ring](trough:IsOrderedRing) that is not Archimedean, and the
[Hahn embedding theorem](trough:hahnEmbedding_isOrderedAddMonoid) describes ordered groups
through the same Archimedean classes that separate these sizes.

## In Mathlib

Mathlib builds the hyperreals as germs of real sequences at its hyperfilter, one ultrafilter on
$\mathbb N$ extending the cofinite filter chosen by the axiom of choice, so its hyperreals are a
single field rather than a family indexed by ultrafilters. The field operations and the linear
order come from the general theory of germs, the reals sit inside as constant sequences, and
$\omega$ and $\varepsilon$ are provided by name. Infinitesimal and infinite elements and the
standard part are not special to the hyperreals: Mathlib treats them in every ordered field
through the Archimedean class of an element, ordered so that smaller elements have larger
classes; an element is infinitesimal when its class is above that of $1$ and infinite when it is
below. The standard part is defined for every element, with value $0$ at infinite elements, so
[the standard part of $\omega$ is $0$](lean:Hyperreal.stdPart_omega). The sum and product rules
above hold in every ordered field, and the uniqueness statement and the supremum formula in every
ordered field that receives an order-preserving ring homomorphism from the reals. The transfer
principle is not yet formalized for the hyperreals, though Łoś' theorem is available for
ultraproducts of first-order structures.

## Depends on

- [Real number](trough:Real)
- [Field](trough:Field)
- [Ordered ring](trough:IsOrderedRing)
- [Filter](trough:Filter)
