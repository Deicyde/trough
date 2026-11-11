---
declaration: section
origin: cited
lean: Polynomial.exists_monic_coprime_factorization_of_isAdicComplete, Polynomial.exists_monic_coprime_factorization_of_isAdicComplete_natDegree, Polynomial.Monic.isCoprime_of_isCoprime_map, Polynomial.existsUnique_monic_map_eq_dvd_of_isCoprime_of_ker_pow_eq_bot, Polynomial.exists_monic_mul_eq_and_map_eq_of_isCoprime_of_isAdicComplete, Polynomial.exists_isRoot_sub_mem_maximalIdeal_of_isUnit_derivative, Polynomial.addVal_sub_le_addVal_eval_sub, Polynomial.addVal_derivative_eval_eq_of_lt_addVal_sub
statement: formalized
proof: formalized
---

# Henselian rings and Hensel's lemma

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/henselian-rings-and-hensel-s-lemma/index.html).

## Hensel lifting of monic coprime factorizations

Let $A$ be a commutative ring and $I$ an
ideal of $A$ such that $A$ is $I$-adically complete, and let $f \in A[X]$ be monic. Suppose the
reduction of $f$ modulo $I$ equals $\bar g \bar h$, where $\bar g, \bar h \in (A/I)[X]$ are monic
and coprime (that is, $a \bar g + b \bar h = 1$ for some $a, b \in (A/I)[X]$). Then there exist
monic $g, h \in A[X]$ with $f = gh$ whose reductions modulo $I$ are $\bar g$ and $\bar h$
respectively.

The proof packages the residue factorization via the universal coprime factorization ring, lifts
its structure map through $I$-adic completeness, and evaluates the universal factors over $A$.

Formalized by `Polynomial.exists_monic_coprime_factorization_of_isAdicComplete`, a theorem declared in [MathlibExt/NumberTheory/HenselFactorization.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/HenselFactorization.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/henselian-rings-and-hensel-s-lemma/index.html#exists-monic-coprime-factorization-of-is).

## Hensel lifting of monic coprime factorizations, with degrees

Let $A$ be a commutative
ring and $I$ an ideal of $A$ such that $A$ is $I$-adically complete and $A/I$ is not the zero
ring, and let $f \in A[X]$ be monic. Suppose the reduction of $f$ modulo $I$ equals
$\bar g \bar h$, where $\bar g, \bar h \in (A/I)[X]$ are monic and coprime (that is,
$a \bar g + b \bar h = 1$ for some $a, b \in (A/I)[X]$). Then there exist monic $g, h \in A[X]$
with $f = gh$ whose reductions modulo $I$ are $\bar g$ and $\bar h$ respectively, and such that
$\deg g = \deg \bar g$ and $\deg h = \deg \bar h$.

Formalized by `Polynomial.exists_monic_coprime_factorization_of_isAdicComplete_natDegree`, a theorem declared in [MathlibExt/NumberTheory/HenselFactorization.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/HenselFactorization.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/henselian-rings-and-hensel-s-lemma/index.html#exists-monic-coprime-factorization-of-is-2).

## Local homomorphisms reflect coprimality with a monic polynomial

A local ring homomorphism reflects coprimality of polynomials when the
first polynomial is monic. Neither ring needs to be local.

Formalized by `Polynomial.Monic.isCoprime_of_isCoprime_map`, a theorem declared in [MathlibExt/NumberTheory/HenselFactorizationUniqueness.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/HenselFactorizationUniqueness.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/henselian-rings-and-hensel-s-lemma/index.html#is-coprime-of-is-coprime-map).

## Unique lift of a monic factor through a nilpotent-kernel surjection

A monic factor of a coprime factorization lifts uniquely through a
surjective homomorphism with nilpotent kernel. The original polynomial
and the complementary reduced factor are not required to be monic.

Formalized by `Polynomial.existsUnique_monic_map_eq_dvd_of_isCoprime_of_ker_pow_eq_bot`, a theorem declared in [MathlibExt/NumberTheory/HenselFactorizationUniqueness.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/HenselFactorizationUniqueness.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/henselian-rings-and-hensel-s-lemma/index.html#exists-unique-monic-map-eq-dvd-of-is-cop).

## Hensel lifting of coprime monic factors over a complete ring

Coprime monic factors lift over a ring complete at the kernel of a
surjective homomorphism. The lifts are coprime, and the first is the unique
monic divisor of the original polynomial with its specified reduction.

Formalized by `Polynomial.exists_monic_mul_eq_and_map_eq_of_isCoprime_of_isAdicComplete`, a theorem declared in [MathlibExt/NumberTheory/HenselFactorizationUniqueness.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/HenselFactorizationUniqueness.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/henselian-rings-and-hensel-s-lemma/index.html#exists-monic-mul-eq-and-map-eq-of-is-cop).

## Hensel's lemma for complete discrete valuation rings

Let $A$ be a discrete valuation ring
with maximal ideal $\mathfrak{m}$ that is complete and Hausdorff for the $\mathfrak{m}$-adic
topology. Let $f \in A[X]$ have derivative $f'$, and let $a_0 \in A$ satisfy
$f(a_0) \in \mathfrak{m}$ with $f'(a_0)$ a unit of $A$. Then $f$ has a root $a \in A$ with
$a - a_0 \in \mathfrak{m}$.

Formalized by `Polynomial.exists_isRoot_sub_mem_maximalIdeal_of_isUnit_derivative`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/Hensel.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/Hensel.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/henselian-rings-and-hensel-s-lemma/index.html#exists-is-root-sub-mem-maximal-ideal-of).

## Polynomials do not decrease the valuation of differences

Let $A$ be a discrete valuation
ring with normalized additive valuation $v \colon A \to \mathbb{N} \cup \{\infty\}$. For every
polynomial $p \in A[X]$ and all $a, a_0 \in A$, we have $v(a - a_0) \le v(p(a) - p(a_0))$.

Formalized by `Polynomial.addVal_sub_le_addVal_eval_sub`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/Hensel.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/Hensel.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/henselian-rings-and-hensel-s-lemma/index.html#add-val-sub-le-add-val-eval-sub).

## Nearby roots share the derivative valuation

A root sufficiently close to the approximation has the same derivative valuation.

Formalized by `Polynomial.addVal_derivative_eval_eq_of_lt_addVal_sub`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/Hensel.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/Hensel.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/henselian-rings-and-hensel-s-lemma/index.html#add-val-derivative-eval-eq-of-lt-add-val).

## Uniqueness of roots near a point

Let $A$ be a discrete valuation ring with normalized
additive valuation $v \colon A \to \mathbb{N} \cup \{\infty\}$, let $f \in A[X]$ have derivative
$f'$, and let $a_0 \in A$. If $a, a' \in A$ are roots of $f$ with $v(f'(a_0)) < v(a - a_0)$ and
$v(f'(a_0)) < v(a' - a_0)$, then $a = a'$.

Formalized by `Polynomial.eq_of_isRoot_of_addVal_derivative_lt_addVal_sub`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/Hensel.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/Hensel.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/henselian-rings-and-hensel-s-lemma/index.html#eq-of-is-root-of-add-val-derivative-lt-a).

## Elements of the maximal ideal have positive valuation

Let $A$ be a discrete valuation
ring with maximal ideal $\mathfrak{m}$ and normalized additive valuation
$v \colon A \to \mathbb{N} \cup \{\infty\}$. If $d \in A$ is nonzero and $q \in \mathfrak{m}$, then
$v(d) < v(d) + v(q)$.

Since $v(dq) = v(d) + v(q)$, multiplying a nonzero element by an element of the maximal ideal
strictly increases its valuation.

Formalized by `IsDiscreteValuationRing.addVal_lt_addVal_add_of_mem_maximalIdeal`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/Hensel.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/Hensel.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/henselian-rings-and-hensel-s-lemma/index.html#add-val-lt-add-val-add-of-mem-maximal-id).

## Hensel's lemma with a derivative bound

Let $A$ be a discrete valuation ring with maximal
ideal $\mathfrak{m}$ that is complete and Hausdorff for the $\mathfrak{m}$-adic topology, and let
$v \colon A \to \mathbb{N} \cup \{\infty\}$ be its normalized additive valuation. Let $f \in A[X]$
have derivative $f'$, and let $a_0 \in A$ satisfy $2 v(f'(a_0)) < v(f(a_0))$. Then $f$ has a root
$a \in A$ such that $a - a_0 \in \mathfrak{m}$, $v(f'(a_0)) < v(a - a_0)$,
$v(f(a_0)) \le v(a - a_0) + 2 v(f'(a_0))$ and $v(f'(a)) = v(f'(a_0))$. Moreover, every root
$a' \in A$ of $f$ with $v(f'(a_0)) < v(a' - a_0)$ equals $a$.

## Sources

- ATLAS Hensel endpoint; the published statement dropped the condition $v(f'(a_0)) < v(a - a_0)$ on the root, which is kept here so that uniqueness applies to it.

Formalized by `Polynomial.exists_isRoot_of_two_mul_addVal_derivative_lt_addVal`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/Hensel.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/Hensel.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/henselian-rings-and-hensel-s-lemma/index.html#exists-is-root-of-two-mul-add-val-deriva).

## Sections of étale algebras over Henselian local rings

Over a Henselian local ring, an étale algebra has a section lifting any
residue-field point.

Formalized by `HenselianLocalRing.exists_algHom_lift_of_etale`, a theorem declared in [MathlibExt/RingTheory/Henselian/EtaleLift.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Henselian/EtaleLift.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/henselian-rings-and-hensel-s-lemma/index.html#exists-alg-hom-lift-of-etale).

## Complete local rings are Henselian

Let $R$ be a local ring with maximal ideal
$\mathfrak m$. If $R$ is Hausdorff and complete for the $\mathfrak m$-adic topology, then $R$
is a Henselian local ring.

Formalized by `HenselianLocalRing.of_isAdicComplete_maximalIdeal`, a theorem declared in [MathlibExt/RingTheory/LocalRing/Henselian.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/LocalRing/Henselian.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/henselian-rings-and-hensel-s-lemma/index.html#of-is-adic-complete-maximal-ideal).

## Valuation subrings of algebraically closed fields are Henselian

A valuation subring of an algebraically closed field is Henselian.

Formalized by `ValuationSubring.henselianLocalRing_of_isAlgClosed`, a theorem declared in [MathlibExt/RingTheory/Valuation/Henselian.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Valuation/Henselian.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/henselian-rings-and-hensel-s-lemma/index.html#henselian-local-ring-of-is-alg-closed).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Henselian rings and Hensel's lemma](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/henselian-rings-and-hensel-s-lemma/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/valuation-rings/henselian-rings-and-hensel-s-lemma)
