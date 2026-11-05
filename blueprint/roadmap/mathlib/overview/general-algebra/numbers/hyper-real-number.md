---
article_id: af_134479273ab6c3f42eb412b0
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Hyperreal
mathlib_file: Mathlib/Analysis/Real/Hyperreal.lean
---

# Hyper-real number

The **hyper-real numbers**, or hyperreals, form an ordered [field](../field-theory/field.md) $^*\mathbb R$
that contains the [real numbers](real-number.md) together with positive infinitesimals, numbers
greater than $0$ but smaller than every positive real, and infinite elements, numbers larger than
every real.
They are the number system of nonstandard analysis. In $^*\mathbb R$ a derivative can be computed
from a quotient of infinitesimal changes and a limit can be found by rounding a hyper-real number
to the nearest real, which makes arguments with infinitesimals rigorous.

## Definition

The usual construction is an ultrapower of $\mathbb R$. An ultrafilter on the
[natural numbers](natural-number.md) is a [filter](../../topology/general-topology/part-01/filter.md) $\mathcal U$ of subsets of
$\mathbb N$, not containing the empty set, such that for every $A \subseteq \mathbb N$ either $A$
or its complement belongs to $\mathcal U$. It is nonprincipal if it contains no finite set, or
equivalently every set with finite complement. Nonprincipal ultrafilters exist by the axiom of
choice; Mathlib fixes one, its hyperfilter, which
[contains every set with finite complement](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/Filter/Ultrafilter/Basic.html#Filter.hyperfilter_le_cofinite). A set in
$\mathcal U$ is thought of as containing almost all indices.

Two real sequences $(a_n)$ and $(b_n)$ are identified when $\{n : a_n = b_n\} \in \mathcal U$. A
hyper-real number is an equivalence class $[a_n]$, and
[the hyper-real numbers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Hyperreal.html#Hyperreal) are the set of all such classes:
[each sequence defines one](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Hyperreal.html#Hyperreal.ofSeq) and
[every hyper-real number comes from a sequence](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Hyperreal.html#Hyperreal.ofSeq_surjective). Arithmetic is
termwise,

$$[a_n] + [b_n] = [a_n + b_n], \qquad [a_n]\,[b_n] = [a_n b_n],$$

and [$[a_n] < [b_n]$ exactly when $\{n : a_n < b_n\} \in \mathcal U$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Hyperreal.html#Hyperreal.ofSeq_lt_ofSeq).
The order is total because the three sets where $a_n < b_n$, $a_n = b_n$ and $a_n > b_n$
partition $\mathbb N$, so exactly one of them lies in $\mathcal U$. If $[a_n] \neq 0$ then
$a_n \neq 0$ for almost all $n$, and inverting those terms gives the inverse. With these
operations $^*\mathbb R$ is an ordered field.

A real number $r$ is sent to the class of the constant sequence $(r, r, r, \dots)$.
[This embedding](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Hyperreal.html#Hyperreal.ofReal) is
[an order-preserving ring homomorphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Hyperreal.html#Hyperreal.coeRingHom), it is
[injective](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Hyperreal.html#Hyperreal.coe_eq_coe), and
[$r < s$ holds in $^*\mathbb R$ exactly when it holds in $\mathbb R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Hyperreal.html#Hyperreal.coe_lt_coe).

## Examples

Let $\omega = [0, 1, 2, 3, \dots]$ be [the class of the sequence $(n)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Hyperreal.html#Hyperreal.omega).
For a real $r$, all but finitely many $n$ satisfy $n > r$, and that set lies in $\mathcal U$, so
[$r < \omega$ for every real $r$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Hyperreal.html#Hyperreal.coe_lt_omega). Its reciprocal $\varepsilon$ is
[the class of the sequence $(1/n)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Hyperreal.html#Hyperreal.epsilon); changing finitely many terms never
changes a class, so the term at $n = 0$ does not matter. Indeed
[the reciprocal of $\omega$ is $\varepsilon$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Hyperreal.html#Hyperreal.inv_omega), and $\varepsilon$
[is positive](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Hyperreal.html#Hyperreal.epsilon_pos) and
[smaller than every positive real](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Hyperreal.html#Hyperreal.epsilon_lt_of_pos). Further examples are
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
  part $\operatorname{st}(x)$: [for finite $x$ and real $r$, the difference $x - r$ is infinitesimal exactly when $r = \operatorname{st}(x)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/StandardPart.html#ArchimedeanClass.mk_sub_pos_iff).
  The completeness of $\mathbb R$ supplies it:
  [$\operatorname{st}(x)$ is the supremum of the reals below $x$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/StandardPart.html#ArchimedeanClass.stdPart_eq_sSup).
  For finite $x$ and $y$,
  [$\operatorname{st}(x + y) = \operatorname{st}(x) + \operatorname{st}(y)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/StandardPart.html#ArchimedeanClass.stdPart_add)
  and [$\operatorname{st}(xy) = \operatorname{st}(x)\operatorname{st}(y)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/StandardPart.html#ArchimedeanClass.stdPart_mul),
  and [$\operatorname{st}(r) = r$ for real $r$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Hyperreal.html#Hyperreal.stdPart_coe).
- **Limits.** A sequence tends to $L$ along $\mathcal U$ if, for every neighbourhood $V$ of $L$,
  the set of $n$ with $a_n \in V$ lies in $\mathcal U$. [If $(a_n)$ tends to $L$ along $\mathcal U$, then $\operatorname{st}([a_n]) = L$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Hyperreal.html#Hyperreal.stdPart_of_tendsto). Since
  $\mathcal U$ contains every set with finite complement, this covers every sequence with
  [limit](../../../undergraduate/topology/topology-and-metric-spaces/limits-of-sequences.md) $L$ in the usual sense. Likewise
  [$(a_n)$ tends to $+\infty$ along $\mathcal U$ exactly when $[a_n]$ is positive and infinite](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Hyperreal.html#Hyperreal.tendsto_atTop_iff).
- **Continuity.** For a real function $f$ that is [continuous](../../topology/general-topology/part-01/continuous-function.md) at the point $r$,
  [if $(a_n)$ tends to $r$ along $\mathcal U$, then $(f(a_n))$ tends to $f(r)$ along $\mathcal U$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Hyperreal.html#Hyperreal.stdPart_map).
- **Transfer.** Because $^*\mathbb R$ is an ultrapower, [Łoś' theorem](../../../thousand-plus/general-topics-history-and-foundations/03-mathematical-logic-and-foundations/part-03/os-theorem.md)
  applies: [a first-order sentence holds in an ultraproduct of nonempty structures exactly when the set of indices whose factor satisfies it belongs to the ultrafilter](https://leanprover-community.github.io/mathlib4_docs/Mathlib/ModelTheory/Ultraproducts.html#FirstOrder.Language.Ultraproduct.sentence_realize).
  Every factor here is $\mathbb R$, so a first-order sentence in a language with a symbol for each
  real function and relation holds in $^*\mathbb R$ exactly when it holds in $\mathbb R$, where
  each function $f$ is read as its termwise extension $f^*[a_n] = [f(a_n)]$ and each relation $P$
  as the set of classes $[a_n]$ with $P(a_n)$ for almost all $n$. For example, a real function $f$ has
  [derivative](../../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md) $L$ at a real $x$ exactly when
  $(f^*(x + \delta) - f(x))/\delta$ is infinitely close to $L$ for every nonzero infinitesimal
  $\delta$. Transfer does not reach statements that quantify over arbitrary subsets, which is why
  completeness fails.

If the continuum hypothesis holds, all nonprincipal ultrafilters on $\mathbb N$ yield isomorphic
ordered fields.

## Related concepts

The [extended real numbers](extended-real-number.md) add only $+\infty$ and $-\infty$ to $\mathbb R$ and do
not form a field. Infinitesimal and infinite elements make sense in any
[ordered ring](../rings/ordered-ring.md) that is not Archimedean, and the
[Hahn embedding theorem](../../../thousand-plus/combinatorics-and-ordered-structures/06-order-lattices-ordered-algebraic-structures/hahn-embedding-theorem.md) describes ordered groups
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
[the standard part of $\omega$ is $0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Hyperreal.html#Hyperreal.stdPart_omega). The sum and product rules
above hold in every ordered field, and the uniqueness statement and the supremum formula in every
ordered field that receives an order-preserving ring homomorphism from the reals. The transfer
principle is not yet formalized for the hyperreals, though Łoś' theorem is available for
ultraproducts of first-order structures.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Real number](real-number.md)
- [Field](../field-theory/field.md)
- [Ordered ring](../rings/ordered-ring.md)
- [Filter](../../topology/general-topology/part-01/filter.md)

## Sources

- [Mathlib documentation: `Hyperreal`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Hyperreal.html#Hyperreal)
- [Source of `Hyperreal` in Mathlib/Analysis/Real/Hyperreal.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Real/Hyperreal.lean#L44)
- [Mathlib overview: General algebra › Numbers](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L30)
