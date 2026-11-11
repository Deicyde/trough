---
declaration: section
origin: cited
lean: MetaMathlibExt.exponentialGeneratingFunction_binomialTransform, MetaMathlibExt.fallingKBinomialTransform, MetaMathlibExt.binomialTransform, MetaMathlibExt.binomialTransform_eq_sum, MetaMathlibExt.multipleBinomialTransform, MetaMathlibExt.falling_equiv, MetaMathlibExt.mk_sum_choose_mul_eq_inv_one_sub_mul_subst, MetaMathlibExt.ordinary_generating_function_binomial_transform
statement: formalized
proof: formalized
---

# Binomial transforms

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/binomial-transforms/index.html).

## Exponential generating function of the binomial transform

Let $(a_n)_{n \ge 0}$ and
$(b_n)_{n \ge 0}$ be real sequences with $b_n = \sum_{k=0}^{n} \binom{n}{k} a_k$ for every $n$,
and let $A : \mathbb{R} \to \mathbb{R}$ be any function. For every real number $t$, if the series
$\sum_{n \ge 0} a_n t^n / n!$ converges absolutely with sum $A(t)$, then the series
$\sum_{n \ge 0} b_n t^n / n!$ converges absolutely with sum $e^t A(t)$.

The formulation is pointwise: convergence of the exponential generating function of $a$ is
assumed only at the point $t$ under consideration.

## Sources

- Ayhan Dil, Veli Kurt, and Mehmet Cenkci, *Algorithms for Bernoulli and Related Polynomials*, Journal of Integer Sequences 10 (2007), Article 07.5.4, <https://cs.uwaterloo.ca/journals/JIS/VOL10/Dil/dil11.tex>, Proposition `prop2` (proof attributed to Seidel), lines 221-233; the binomial-transform relation `a_0^n = Σᵢ C(n,i) a_i^0` is equation (8)/(9), lines 188-199.

Formalized by `MetaMathlibExt.exponentialGeneratingFunction_binomialTransform`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/BinomialTransformExponentialGeneratingFunction.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/BinomialTransformExponentialGeneratingFunction.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/binomial-transforms/index.html#exponential-generating-function-binomial).

## Falling k-binomial transform

For an integer $k$ and an integer sequence $(a_i)_{i \ge 0}$,
the falling $k$-binomial transform of $a$ is the integer sequence $(b_n)_{n \ge 0}$ given by

$$b_n = \sum_{i=0}^{n} \binom{n}{i} k^{n-i} a_i.$$

Formalized by `MetaMathlibExt.fallingKBinomialTransform`, a definition declared in [MathlibExt/Combinatorics/Enumerative/FallingKBinomialTransform.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FallingKBinomialTransform.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/binomial-transforms/index.html#falling-kbinomial-transform).

## Binomial transform

The binomial transform of an integer sequence $(a_i)_{i \ge 0}$ is the
falling k-binomial transform of $a$ with $k = 1$, the sequence whose $n$-th term is
$\sum_{i=0}^{n} \binom{n}{i} 1^{n-i} a_i$.

Formalized by `MetaMathlibExt.binomialTransform`, a definition declared in [MathlibExt/Combinatorics/Enumerative/FallingKBinomialTransform.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FallingKBinomialTransform.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/binomial-transforms/index.html#binomial-transform).

## Binomial transform as a binomial sum

For every integer sequence $(a_i)_{i \ge 0}$ and
every $n \in \mathbb{N}$, the $n$-th term of the binomial transform of $a$ equals
$\sum_{i=0}^{n} \binom{n}{i} a_i$.

Formalized by `MetaMathlibExt.binomialTransform_eq_sum`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/FallingKBinomialTransform.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FallingKBinomialTransform.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/binomial-transforms/index.html#binomial-transform-eq-sum).

## Multiple binomial transform

The binomial transform sends an integer sequence
$(a_i)_{i \ge 0}$ to the sequence $(b_n)_{n \ge 0}$ given by
$b_n = \sum_{i=0}^{n} \binom{n}{i} a_i$. For a natural number $r$, the $r$-fold binomial
transform of $a$ is obtained by applying the binomial transform $r$ times in succession; the
$0$-fold transform of $a$ is $a$ itself.

* Jiaqiang Pan, *Multiple Binomial Transforms and Families of Integer Sequences*,
  Journal of Integer Sequences 13 (2010), lines 128–150:
  <https://cs.uwaterloo.ca/journals/JIS/VOL13/Pan/pan8.tex>.
* Jiaqiang Pan, *Some Properties of the Multiple Binomial Transform and the Hankel Transform of
  Shifted Sequences*, Journal of Integer Sequences 14 (2011), lines 104–118:
  <https://cs.uwaterloo.ca/journals/JIS/VOL14/Pan/pan12.tex>.

Concept `jis_term_c157679dc9eb88c4ba264101`; source statements
`jis_565fc7c3315ad99b5942cc67` and `jis_a569298bba80b28850af1658`.

## Sources

-

Formalized by `MetaMathlibExt.multipleBinomialTransform`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MultipleBinomialTransform.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MultipleBinomialTransform.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/binomial-transforms/index.html#multiple-binomial-transform).

## The k-fold binomial transform is the falling k-binomial transform

For every integer
sequence $a$ and every integer $k$: if $k \ge 0$, applying the binomial transform $k$ times to
$a$ gives the falling $k$-binomial transform of $a$; if $k < 0$, applying the inverse binomial
transform (the falling $(-1)$-binomial transform) $-k$ times to $a$ gives the falling
$k$-binomial transform of $a$. In both cases the equality is one of integer sequences.

## Sources

- Michael Z. Spivey and Laura L. Steil, "The k-Binomial Transforms and the Hankel Transform", Journal of Integer Sequences 9 (2006), Article 06.1.1, Theorem `falling_equiv`, lines 636-640, <https://cs.uwaterloo.ca/journals/JIS/VOL9/Spivey/spivey7.tex>.

Formalized by `MetaMathlibExt.falling_equiv`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/FallingBinomialTransform.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FallingBinomialTransform.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/binomial-transforms/index.html#falling-equiv).

## Generating function of the binomial transform over a field

Let $K$ be a field and let
$a : \mathbb{N} \to K$ be a sequence with ordinary generating function
$A(X) = \sum_n a_n X^n \in K[[X]]$. Then the ordinary generating function of the binomial
transform $n \mapsto \sum_{k=0}^{n} \binom{n}{k} a_k$ of $a$ equals
$(1 - X)^{-1} \cdot A\big(X (1 - X)^{-1}\big)$ in $K[[X]]$, where $A\big(X (1 - X)^{-1}\big)$ is
the power series obtained by substituting $X (1 - X)^{-1}$ for $X$ in $A$.

Formalized by `MetaMathlibExt.mk_sum_choose_mul_eq_inv_one_sub_mul_subst`, a theorem declared in [MathlibExt/RingTheory/PowerSeries/BinomialTransformGeneratingFunction.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/PowerSeries/BinomialTransformGeneratingFunction.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/binomial-transforms/index.html#mk-sum-choose-mul-eq-inv-one-sub-mul-sub).

## Ordinary generating function of the binomial transform

Let $a : \mathbb{N} \to \mathbb{R}$
be a real sequence with ordinary generating function $A(X) = \sum_n a_n X^n \in \mathbb{R}[[X]]$.
Then the ordinary generating function of the binomial transform
$n \mapsto \sum_{k=0}^{n} \binom{n}{k} a_k$ of $a$ equals
$(1 - X)^{-1} \cdot A\big(X (1 - X)^{-1}\big)$ in $\mathbb{R}[[X]]$, where
$A\big(X (1 - X)^{-1}\big)$ is the power series obtained by substituting $X (1 - X)^{-1}$ for $X$
in $A$.

## Sources

- Ayhan Dil, Veli Kurt, and Mehmet Cenkci, "Algorithms for Bernoulli and Related Polynomials," Journal of Integer Sequences 10 (2007), Article 07.5.4, Proposition, lines 205–218 (proof attributed to Euler there). <https://cs.uwaterloo.ca/journals/JIS/VOL10/Dil/dil11.tex> It is the case `K = ℝ` of `mk_sum_choose_mul_eq_inv_one_sub_mul_subst`.

Formalized by `MetaMathlibExt.ordinary_generating_function_binomial_transform`, a theorem declared in [MathlibExt/RingTheory/PowerSeries/BinomialTransformGeneratingFunction.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/PowerSeries/BinomialTransformGeneratingFunction.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/binomial-transforms/index.html#ordinary-generating-function-binomial-tr).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binomial transforms](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/binomial-transforms/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/binomial-transforms)
