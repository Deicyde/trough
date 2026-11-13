---
declaration: section
origin: cited
lean: MetaMathlibExt.laurentInvVar, MetaMathlibExt.laurentInvVar_mul_single_one, MetaMathlibExt.polyToLaurentInv, MetaMathlibExt.polyToLaurentInv_X, MetaMathlibExt.laurentPolyPart, MetaMathlibExt.laurentPolyPart_coeff, MetaMathlibExt.laurentPolyPart_laurentInvVar, MetaMathlibExt.laurentCompleteQuotient
statement: formalized
---

# Continued fractions of Laurent series

30 results, 16 proved and 14 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html).

## The variable $x$ of $K((x^{-1}))$

Let $K$ be a field. Formal Laurent series in $x^{-1}$
over $K$ are realized as Laurent series $\sum_n c_n X^n$ in $X = x^{-1}$, and the variable $x$
is the series $X^{-1}$, with coefficient $1$ at $X^{-1}$ and $0$ elsewhere.

A series $\alpha = \sum_n c_n x^{-n} \ne 0$ has absolute value $|\alpha| = |x|^{-v(\alpha)}$,
where its order $v(\alpha)$ is the least $n$ with $c_n \ne 0$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Section 1.

Formalized by `MetaMathlibExt.laurentInvVar`, a definition declared in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#laurent-inv-var).

## The variable $x$ times $x^{-1}$ is one

Let $K$ be a field. In $K((x^{-1}))$, the
product of the variable $x$ and the series $x^{-1}$ (coefficient $1$ at $x^{-1}$ and $0$
elsewhere) is $1$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Section 1.

Formalized by `MetaMathlibExt.laurentInvVar_mul_single_one`, a theorem declared in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#laurent-inv-var-mul-single-one).

## Polynomials as Laurent series in the inverse variable

Let $K$ be a field. The embedding
$K[x] \to K((x^{-1}))$ is the $K$-algebra homomorphism that sends $x$ to the element $x$ of
$K((x^{-1}))$, that is, it evaluates a polynomial at $x$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Section 1.

Formalized by `MetaMathlibExt.polyToLaurentInv`, a definition declared in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#poly-to-laurent-inv).

## The polynomial variable embeds as the Laurent variable

Let $K$ be a field. The
embedding $K[x] \to K((x^{-1}))$ sends the polynomial $x$ to the element $x$ of
$K((x^{-1}))$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Section 1.

Formalized by `MetaMathlibExt.polyToLaurentInv_X`, a theorem declared in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#poly-to-laurent-inv-x).

## Polynomial part of a Laurent series

Let $K$ be a field and write a Laurent series
$\alpha \in K((x^{-1}))$ as $\alpha = \sum_n c_n x^{-n}$. Its polynomial part is
$[\alpha] = \sum_{n \le 0} c_n x^{-n}$, the sum of the terms in nonnegative powers of $x$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Section 1, (1.3).

Formalized by `MetaMathlibExt.laurentPolyPart`, a definition declared in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#laurent-poly-part).

## Coefficients of the polynomial part of a Laurent series

Let $K$ be a field and write
$\alpha \in K((x^{-1}))$ as $\alpha = \sum_n c_n x^{-n}$. For every integer $n$, the coefficient
of $x^{-n}$ in the polynomial part $[\alpha]$ is $c_n$ if $n \le 0$ and $0$ if $n > 0$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Section 1, (1.3).

Formalized by `MetaMathlibExt.laurentPolyPart_coeff`, a theorem declared in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#laurent-poly-part-coeff).

## Polynomial parts of the variable and its inverse

Let $K$ be a field. In
$K((x^{-1}))$ the polynomial part of $x$ is $x$, and the polynomial part of $x^{-1}$ is $0$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Section 1, (1.3).

Formalized by `MetaMathlibExt.laurentPolyPart_laurentInvVar`, a theorem declared in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#laurent-poly-part-laurent-inv-var).

## Complete quotients of a Laurent series

Let $K$ be a field and $\alpha \in K((x^{-1}))$. The
complete quotients of the continued fraction expansion of $\alpha$ are $\alpha_0 = \alpha$ and
$\alpha_{n+1} = (\alpha_n - [\alpha_n])^{-1}$ for $n \ge 0$, where $[\beta]$ is the polynomial part
of $\beta$ and $0^{-1} = 0$. So the complete quotients become $0$ after a finite expansion ends.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Section 1, (1.3).

Formalized by `MetaMathlibExt.laurentCompleteQuotient`, a definition declared in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#laurent-complete-quotient).

## Partial quotients of a Laurent series

Let $K$ be a field, $\alpha \in K((x^{-1}))$ and
$n \ge 0$. The $n$-th partial quotient of $\alpha$ is $b_n = [\alpha_n]$, the polynomial part of
the $n$-th complete quotient $\alpha_n$ of $\alpha$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Section 1, (1.3).

Formalized by `MetaMathlibExt.laurentPartialQuotient`, a definition declared in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#laurent-partial-quotient).

## First step of the continued fraction of a Laurent series

Let $K$ be a field and
$\alpha \in K((x^{-1}))$. The partial quotient $b_0$ of $\alpha$ is its polynomial part
$[\alpha]$, and the complete quotient $\alpha_1$ is $(\alpha - [\alpha])^{-1}$, where
$0^{-1} = 0$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Section 1, (1.3).

Formalized by `MetaMathlibExt.laurentPartialQuotient_zero`, a theorem declared in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#laurent-partial-quotient-zero).

## Laurent series with bounded partial quotients

Let $K$ be a field. A Laurent series
$\alpha \in K((x^{-1}))$ with partial quotients $b_0, b_1, \dots$ has bounded partial quotients
if there is an integer $B$ such that for every $n \ge 0$ and every integer $k > B$ the
coefficient of $x^k$ in $b_n$ is zero, that is, every nonzero $b_n$ is a polynomial in $x$ of
degree at most $B$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Section 1.

Formalized by `MetaMathlibExt.LaurentHasBoundedPartialQuotients`, a definition declared in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#laurent-has-bounded-partial-quotients).

## Numerators of the convergents of a Laurent series

Let $K$ be a field and let
$\alpha \in K((x^{-1}))$ have partial quotients $b_0, b_1, \dots$. The numerators of the
convergents of $\alpha$ are $P_{-1} = 1$, $P_0 = b_0$ and $P_{n+1} = b_{n+1} P_n + P_{n-1}$ for
$n \ge 0$. The sequence is indexed with a shift of one: its term at $n \ge 0$ is $P_{n-1}$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Section 1.

Formalized by `MetaMathlibExt.laurentConvNum`, a definition declared in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#laurent-conv-num).

## Denominators of the convergents

Let $K$ be a field, let $\alpha \in K((x^{-1}))$ and let
$b_0, b_1, \dots$ be its partial quotients. The denominators of the convergents of $\alpha$ are
given by $Q_{-1} = 0$, $Q_0 = 1$ and $Q_{n+1} = b_{n+1} Q_n + Q_{n-1}$ for $n \ge 0$. They are
indexed from $0$ here: the $k$-th term of the sequence is $Q_{k-1}$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Section 1.

Formalized by `MetaMathlibExt.laurentConvDen`, a definition declared in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#laurent-conv-den).

## The convergent $P_1 / Q_1$ of a Laurent series

Let $K$ be a field and let
$\alpha \in K((x^{-1}))$ have partial quotients $b_0, b_1, \dots$. Let $P_n$ and $Q_n$ be the
numerators and denominators of its convergents, given by $P_{-1} = 1$, $Q_{-1} = 0$, $P_0 = b_0$,
$Q_0 = 1$, $P_{n+1} = b_{n+1} P_n + P_{n-1}$ and $Q_{n+1} = b_{n+1} Q_n + Q_{n-1}$. Then
$P_1 = b_1 b_0 + 1$ and $Q_1 = b_1$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Section 1.

Formalized by `MetaMathlibExt.laurentConv_two`, a theorem declared in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#laurent-conv-two).

## Irrational Laurent series

Let $K$ be a field. A Laurent series $\alpha \in K((x^{-1}))$
is irrational if $Q \alpha \ne P$ for all polynomials $P, Q \in K[x]$ with $Q \ne 0$, where
polynomials are embedded in $K((x^{-1}))$ by sending $x$ to the variable $x$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Section 1.

Formalized by `MetaMathlibExt.LaurentIsIrrational`, a definition declared in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#laurent-is-irrational).

## Polynomials are not irrational

Let $K$ be a field. For every polynomial $P \in K[x]$,
the image of $P$ in $K((x^{-1}))$ is not irrational.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Section 1.

Formalized by `MetaMathlibExt.not_laurentIsIrrational_polyToLaurentInv`, a theorem declared in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#not-laurent-is-irrational-poly-to-lauren).

## Baum–Sweet: cubics with bounded partial quotients

Let $p \in \mathbb{F}_2[x]$ have degree
at least $1$. If $f \in \mathbb{F}_2((x^{-1}))$ satisfies $f^3 + p^{-1} f + 1 = 0$, then $f$ has
bounded partial quotients.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Theorem 1 (quoting Baum and Sweet, Corollary 3).

Stated but not proved: `MetaMathlibExt.baumSweet_cubic_boundedPartialQuotients` is written with `theorem_wanted` in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#baum-sweet-cubic-bounded-partial-quotien).

## Baum–Sweet: unbounded partial quotients for higher degrees

Let $n > 1$ and let
$g \in \mathbb{F}_2[x]$ have degree at least $1$. If $f \in \mathbb{F}_2((x^{-1}))$ satisfies
$f^{2^n+1} + g^{-1} f + 1 = 0$, then $f$ does not have bounded partial quotients.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Theorem 2 (quoting Baum and Sweet, Theorem 5).

Stated but not proved: `MetaMathlibExt.baumSweet_unboundedPartialQuotients` is written with `theorem_wanted` in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#baum-sweet-unbounded-partial-quotients).

## Baum–Sweet: explicit continued fractions of roots

Let $n \ge 0$ and let
$P, Q \in \mathbb{F}_2[x]$ with $P + Q^{2^n} \ne 0$ and $P + Q^{2^n} \ne 1$. Then some
$f \in \mathbb{F}_2((x^{-1}))$ satisfies $f^{2^n+1} + Q f^{2^n} + P f + QP + 1 = 0$ and has partial
quotients $b_0 = Q$ and $b_k = P^{2^{(k-1)n}} + Q^{2^{kn}}$ for all $k \ge 1$, that is,
$f = [Q; P + Q^{2^n}, P^{2^n} + Q^{2^{2n}}, P^{2^{2n}} + Q^{2^{3n}}, \dots]$.

The paper also claims that this root is unique, which fails: for $n = 0$, $P = x$ and $Q = 0$ the
equation $f(f + x) = 1$ has the two roots $[0; x, x, \dots]$ and $[x; x, x, \dots]$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Theorem 3 (quoting Baum and Sweet).

Stated but not proved: `MetaMathlibExt.baumSweet_exists_root_continuedFraction` is written with `theorem_wanted` in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#baum-sweet-exists-root-continued-fractio).

## Basic properties of the convergents of a Laurent series

Let $K$ be a field and let
$\alpha \in K((x^{-1}))$ be irrational, with partial quotients $b_0, b_1, \dots$ and convergents
$P_n / Q_n$, where $P_{-1} = 1$, $Q_{-1} = 0$, $P_0 = b_0$, $Q_0 = 1$,
$P_{n+1} = b_{n+1} P_n + P_{n-1}$ and $Q_{n+1} = b_{n+1} Q_n + Q_{n-1}$. For a Laurent series
$y = \sum_m c_m x^{-m}$ let $v(y)$ be its order, the least $m$ with $c_m \ne 0$, and let
$v(0) = 0$; thus $|y| = |x|^{-v(y)}$ for $y \ne 0$. For $\beta \in K((x^{-1}))$ write
$[b_k, \dots, b_n, \beta] = b_k + 1/(b_{k+1} + 1/(\cdots + 1/(b_n + 1/\beta)))$. Then:
(i) for every $n \ge 0$ and every $\beta \ne 0$ such that $[b_k, \dots, b_n, \beta] \ne 0$ for
all $1 \le k \le n$, $(\beta P_n + P_{n-1}) / (\beta Q_n + Q_{n-1}) = [b_0, \dots, b_n, \beta]$;
(ii) $P_n Q_{n-1} - P_{n-1} Q_n = (-1)^{n+1}$ for every $n \ge 0$;
(iii) $Q_{n-1} \ne 0$ and $v(Q_n) < v(Q_{n-1})$ for every $n \ge 1$;
(iv) $v(Q_n) = v(b_1) + \dots + v(b_n)$ for every $n \ge 1$;
(v) $v(\alpha - P_n / Q_n) = -v(b_{n+1}) - 2 v(Q_n)$ for every $n \ge 1$;
(vi) $v(Q_n \alpha - P_n) < v(Q_{n+1} \alpha - P_{n+1})$ for every $n \ge 1$.

Part (iii) fails at $n = 0$ because $Q_{-1} = 0$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Lemma 1.

Stated but not proved: `MetaMathlibExt.laurentConvergent_properties` is written with `theorem_wanted` in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#laurent-convergent-properties).

## Frobenius acts on continued fractions of Laurent series

Let $K$ be a finite field with
$q$ elements and let $\alpha \in K((x^{-1}))$, with partial quotients $b_0, b_1, \dots$ and
convergent numerators and denominators $P_n, Q_n$, where $P_{-1} = 1$ and $Q_{-1} = 0$. Then for
every $n \ge 0$ the $n$-th partial quotient of $\alpha^q$ is $b_n^q$, and for every $n \ge -1$
the convergent numerator and denominator of $\alpha^q$ of index $n$ are $P_n^q$ and $Q_n^q$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Lemma 2.

Stated but not proved: `MetaMathlibExt.laurentPartialQuotient_pow_card` is written with `theorem_wanted` in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#laurent-partial-quotient-pow-card).

## Close rational approximations and convergents

Let $K$ be a field and let
$\alpha \in K((x^{-1}))$ be irrational, with partial quotients $b_0, b_1, \dots$ and convergents
$P_n / Q_n$, where $P_{-1} = 1$, $Q_{-1} = 0$, $P_0 = b_0$, $Q_0 = 1$,
$P_{n+1} = b_{n+1} P_n + P_{n-1}$ and $Q_{n+1} = b_{n+1} Q_n + Q_{n-1}$. For a Laurent series
$y = \sum_m c_m x^{-m}$ let $v(y)$ be its order, the least $m$ with $c_m \ne 0$, and let
$v(0) = 0$. Let $P, Q \in K[x]$ be coprime with $Q \ne 0$.
(i) If $v(Q \alpha - P) = s + \deg Q$ for some integer $s \ge 1$, then there are $n \ge 0$ and
$c \in K \setminus \{0\}$ with $P = c P_n$, $Q = c Q_n$ and $v(b_{n+1}) = -s$.
(ii) If $v(Q \alpha - P) = \deg Q$, then there are $n \ge 0$ and $c, d \in K \setminus \{0\}$
with $P = c P_n + d P_{n-1}$ and $Q = c Q_n + d Q_{n-1}$.

With $|y| = |x|^{-v(y)}$, the hypothesis of (i) reads $|Q \alpha - P| = |x|^{-s} |Q|^{-1}$ and
its conclusion $|b_{n+1}| = |x|^s$; the hypothesis of (ii) reads $|Q \alpha - P| = |Q|^{-1}$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Lemma 3 (generalizing Baum and Sweet, Lemma 1).

Stated but not proved: `MetaMathlibExt.laurent_eq_convergent_of_order` is written with `theorem_wanted` in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#laurent-eq-convergent-of-order).

## Distance from an irrational Laurent series to its convergents

Let $K$ be a field, let
$\alpha \in K((x^{-1}))$ be irrational with convergents $P_n/Q_n$ ($n \ge 0$), and for nonzero
$y \in K((x^{-1}))$ let $|y| = |x|^{\deg y}$, where $\deg y$ is the largest exponent of $x$
occurring in $y$ and $|x| > 1$ is fixed. (i) If $|\alpha| \ge 1$, then
$|\alpha - P_n/Q_n| < |\alpha|$ for all $n \ge 0$. (ii) If $|\alpha| < 1$, then
$|\alpha - P_0/Q_0| = |\alpha|$ and $|\alpha - P_n/Q_n| < |\alpha|$ for all $n \ge 1$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Lemma 4.

Stated but not proved: `MetaMathlibExt.laurent_sub_convergent_order` is written with `theorem_wanted` in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#laurent-sub-convergent-order).

## Lasjaunias's bound on the next partial quotient

Let $\mathbb{F}_q$ be a finite field, let
$A, B, C, D \in \mathbb{F}_q[x]$ with $\Delta = AD - BC \ne 0$ and $C \ne 0$, and let
$\alpha \in \mathbb{F}_q((x^{-1}))$ be irrational with $\alpha = (A\alpha^q + B)/(C\alpha^q + D)$.
Write $|y| = |x|^{\deg y}$ for the absolute value on $\mathbb{F}_q((x^{-1}))$, where $\deg y$ is
the largest exponent of $x$ occurring in $y \ne 0$, and write $P_n/Q_n$ for the convergents and
$b_n$ for the partial quotients of $\alpha$. Let $n \ge 0$, let $P, Q \in \mathbb{F}_q[x]$ be
coprime with $Q \ne 0$ and $P/Q = P_n/Q_n$, and suppose $|\alpha - P/Q| < |\alpha - A/C|$. Put
$R_1 = DP - BQ$, $S_1 = -CP + AQ$ and $\delta_1 = \gcd(R_1, S_1)$. If $R_1/\delta_1$ or
$S_1/\delta_1$ is not a $q$-th power in $\mathbb{F}_q[x]$, then
$|b_{n+1}| < |\Delta|\,|\delta_1|^{-2}$.

The hypothesis $C \ne 0$, which makes $A/C$ meaningful, is implicit in the paper.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Lemma 5 (quoting Lasjaunias, Lemma 1).

Stated but not proved: `MetaMathlibExt.lasjaunias_partialQuotient_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#lasjaunias-partial-quotient-bound).

## Difference identities for a Möbius–Frobenius fixed point

Let $K$ be a finite field with
$q$ elements, let $A, B, C, D \in K[x]$ with $\Delta = AD - BC \ne 0$, and let
$\alpha \in K((x^{-1}))$ be irrational with $\alpha = (A \alpha^q + B) / (C \alpha^q + D)$. Let
$P, Q \in K[x]$ with $Q \ne 0$, put $R_1 = DP - BQ$, $S_1 = -CP + AQ$, $R_2 = AP^q + BQ^q$ and
$S_2 = CP^q + DQ^q$, and assume $S_1 \ne 0$ and $S_2 \ne 0$. Then
$\alpha^q - R_1 / S_1 = \Delta (Q \alpha - P) / ((A - C \alpha) S_1)$ and
$\alpha - R_2 / S_2 = \Delta (Q \alpha - P)^q / ((C \alpha^q + D) S_2)$.

For $C \ne 0$ the conditions $S_1 \ne 0$ and $S_2 \ne 0$ say $P/Q \ne A/C$ and
$(P/Q)^q \ne -D/C$. The source also assumes $\gcd(A, B, C, D) = 1$ and that $P/Q$ is a
convergent of $\alpha$ in lowest terms; the identities do not need these hypotheses.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Lemma 6.

Stated but not proved: `MetaMathlibExt.laurentMobius_sub_identities` is written with `theorem_wanted` in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#laurent-mobius-sub-identities).

## Degree identities at convergents of a Möbius–Frobenius fixed point

Let $K$ be a finite
field with $q$ elements, let $A, B, C, D \in K[x]$ with $\Delta = AD - BC \ne 0$ and $C \ne 0$,
and let $\alpha \in K((x^{-1}))$ be irrational with $\alpha = (A \alpha^q + B) / (C \alpha^q + D)$.
Let $b_0, b_1, \dots$ be the partial quotients of $\alpha$ and $P_n / Q_n$ its convergents, where
$P_{-1} = 1$, $Q_{-1} = 0$, $P_0 = b_0$, $Q_0 = 1$, $P_{n+1} = b_{n+1} P_n + P_{n-1}$ and
$Q_{n+1} = b_{n+1} Q_n + Q_{n-1}$. For a Laurent series $y = \sum_m c_m x^{-m}$ let $v(y)$ be its
order, the least $m$ with $c_m \ne 0$, and let $v(0) = 0$; thus $|y| = |x|^{-v(y)}$ for
$y \ne 0$. Let $n \ge 0$, let $P, Q \in K[x]$ be coprime with $Q \ne 0$ and $P Q_n = Q P_n$,
and put $R_1 = DP - BQ$, $S_1 = -CP + AQ$, $R_2 = AP^q + BQ^q$ and $S_2 = CP^q + DQ^q$, with
the degree of the zero polynomial taken to be $0$. Then:
(i) if $v(\alpha - A/C) < v(\alpha - P/Q)$, then
$v(S_1 \alpha^q - R_1) = \deg S_1 - \deg \Delta - v(b_{n+1})$;
(ii) if $v(\alpha^q + D/C) < q \, v(\alpha - P/Q)$, then
$v(S_2 \alpha - R_2) = \deg S_2 - \deg \Delta - q \, v(b_{n+1})$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Lemma 7, (3.7) and (3.8).

Stated but not proved: `MetaMathlibExt.laurentMobius_order_identities` is written with `theorem_wanted` in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#laurent-mobius-order-identities).

## Lasjaunias's criterion for unbounded partial quotients

Let $\mathbb{F}_q$ be a finite
field, let $A, B, C, D \in \mathbb{F}_q[x]$ with $\Delta = AD - BC \ne 0$ and $C \ne 0$, and let
$\alpha \in \mathbb{F}_q((x^{-1}))$ be irrational with $\alpha = (A\alpha^q + B)/(C\alpha^q + D)$.
Write $|y| = |x|^{\deg y}$ for the absolute value on $\mathbb{F}_q((x^{-1}))$, where $\deg y$ is
the largest exponent of $x$ occurring in $y \ne 0$, and write $P_n/Q_n$ for the convergents and
$b_n$ for the partial quotients of $\alpha$. Suppose that for some $n \ge 0$ there are coprime
$P, Q \in \mathbb{F}_q[x]$ with $Q \ne 0$ and $P/Q = P_n/Q_n$ such that
$|\alpha - P/Q|^q < |\alpha^q + D/C|$, $|\alpha - P/Q|^{q-1} < |\Delta|\,|C\alpha^q + D|^2$ and
$|b_{n+1}|^{q-1} > |\Delta|$. Then $\alpha$ does not have bounded partial quotients.

In the paper these conditions read $|\alpha - P/Q| < |\alpha^q + D/C|^{1/q}$,
$|\alpha - P/Q| < |\Delta|^{1/(q-1)} |C\alpha^q + D|^{2/(q-1)}$ and
$|b_{n+1}| > |\Delta|^{1/(q-1)}$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Lemma 8 (quoting Lasjaunias).

Stated but not proved: `MetaMathlibExt.lasjaunias_unbounded_criterion` is written with `theorem_wanted` in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#lasjaunias-unbounded-criterion).

## Bounded partial quotients for a cubic of Ayadi et al

Let $\ell \ge 2$ and let
$A \in \mathbb{F}_2[x]$ be a polynomial of degree $2\ell$ whose constant and linear coefficients
are both $1$, that is, $A = x^{2\ell} + \sum_{i=2}^{2\ell-1} e_i x^i + x + 1$ with
$e_i \in \mathbb{F}_2$. If $\alpha \in \mathbb{F}_2((x^{-1}))$ has positive degree in $x$ (the
largest exponent of $x$ occurring in $\alpha$ is positive) and satisfies
$x^\ell \alpha^3 + A \alpha^2 + 1 = 0$, then $\alpha$ has bounded partial quotients.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Corollary 1.

Stated but not proved: `MetaMathlibExt.ayadi_cubic_boundedPartialQuotients` is written with `theorem_wanted` in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#ayadi-cubic-bounded-partial-quotients).

## Baum–Sweet cubic: partial quotients of degree at most 2

If
$\alpha \in \mathbb{F}_2((x^{-1}))$ satisfies $x\alpha^3 + \alpha + x = 0$, then every partial
quotient $b_n$ of $\alpha$, $n \ge 0$, has degree at most $2$ in $x$.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Corollary 2.

Stated but not proved: `MetaMathlibExt.baumSweet_x_cubic_partialQuotient_degree_le_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 435](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L435). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#baum-sweet-x-cubic-partial-quotient-degr).

## Small roots of a hyperquadratic equation have unbounded partial quotients

Let
$\mathbb{F}_q$ be a finite field, let $\ell \ge 1$ and let $D \in \mathbb{F}_q[x]$ with
$D(0) \ne 0$. Write $|y| = |x|^{\deg y}$ for the absolute value on $\mathbb{F}_q((x^{-1}))$, where
$\deg y$ is the largest exponent of $x$ occurring in $y \ne 0$. If
$\alpha \in \mathbb{F}_q((x^{-1}))$ is irrational, satisfies $x\alpha^{q+1} + D\alpha + x^\ell = 0$
and $|\alpha| < |x|^{-((q-1)\ell + 1)}$, then $\alpha$ does not have bounded partial quotients.

## Sources

- Tuangrat Chaichana, Natthaphong Chitmung, and Vichian Laohakosol, *Certain Algebraic Formal Laurent Series with Bounded Partial Quotients*, INTEGERS 26 (2026), Article A57, Theorem 6.

Stated but not proved: `MetaMathlibExt.lasjaunias_unboundedPartialQuotients_of_small` is written with `theorem_wanted` in [WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean, line 447](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LaurentSeriesBoundedPartialQuotientsWanted.lean#L447). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html#lasjaunias-unbounded-partial-quotients-o).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Continued fractions of Laurent series](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-laurent-series)
