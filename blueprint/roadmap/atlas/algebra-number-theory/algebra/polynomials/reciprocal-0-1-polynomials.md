---
declaration: section
origin: cited
lean: MathlibExt.Algebra.PalindromicZeroOneWanted.IsReciprocalPoly, MathlibExt.Algebra.PalindromicZeroOneWanted.isReciprocalPoly_iff, MathlibExt.Algebra.PalindromicZeroOneWanted.IsZeroOnePoly, MathlibExt.Algebra.PalindromicZeroOneWanted.isZeroOnePoly_iff, MathlibExt.Algebra.PalindromicZeroOneWanted.IsNoncyclotomic, MathlibExt.Algebra.PalindromicZeroOneWanted.isNoncyclotomic_iff, MathlibExt.Algebra.PalindromicZeroOneWanted.existsUnique_evenOdd_reciprocal, MathlibExt.Algebra.PalindromicZeroOneWanted.existsUnique_evenOdd_zeroOne
statement: formalized
---

# Reciprocal 0,1-polynomials

13 results, 6 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/reciprocal-0-1-polynomials/index.html).

## Reciprocal polynomial

A polynomial $f(x) = a_0 + a_1 x + \dots + a_d x^d$ in
$\mathbb{Z}[x]$ of degree $d$ (with $d = 0$ for the zero polynomial) is *reciprocal*
(palindromic) if it equals its reversal $x^d f(1/x)$, that is, if $a_i = a_{d-i}$ for all
$0 \le i \le d$.

## Sources

- Pradipto Banerjee and Amit Kundu, "On an Irreducibility Question Concerning Palindromic Non-cyclotomic 0,1-Polynomials", Section 1 (terminology).

Formalized by `MathlibExt.Algebra.PalindromicZeroOneWanted.IsReciprocalPoly`, a definition declared in [WantedExt/Algebra/PalindromicZeroOneWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/PalindromicZeroOneWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/reciprocal-0-1-polynomials/index.html#is-reciprocal-poly).

## Characterization of reciprocal polynomials

A polynomial $f \in \mathbb{Z}[x]$ of
degree $d$ (with $d = 0$ for the zero polynomial) is reciprocal if and only if its reversal
$x^d f(1/x)$ equals $f$.

## Sources

- Pradipto Banerjee and Amit Kundu, "On an Irreducibility Question Concerning Palindromic Non-cyclotomic 0,1-Polynomials", Section 1 (terminology).

Formalized by `MathlibExt.Algebra.PalindromicZeroOneWanted.isReciprocalPoly_iff`, a theorem declared in [WantedExt/Algebra/PalindromicZeroOneWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/PalindromicZeroOneWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/reciprocal-0-1-polynomials/index.html#is-reciprocal-poly-iff).

## 0,1-polynomial

A polynomial $f \in \mathbb{Z}[x]$ is a *$0,1$-polynomial* if every
coefficient of $f$ is $0$ or $1$.

## Sources

- Pradipto Banerjee and Amit Kundu, "On an Irreducibility Question Concerning Palindromic Non-cyclotomic 0,1-Polynomials", Section 1 (terminology).

Formalized by `MathlibExt.Algebra.PalindromicZeroOneWanted.IsZeroOnePoly`, a definition declared in [WantedExt/Algebra/PalindromicZeroOneWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/PalindromicZeroOneWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/reciprocal-0-1-polynomials/index.html#is-zero-one-poly).

## Characterization of 0,1-polynomials

A polynomial $f \in \mathbb{Z}[x]$ is a
$0,1$-polynomial if and only if, for every $n \ge 0$, the coefficient of $x^n$ in $f$ is
$0$ or $1$.

## Sources

- Pradipto Banerjee and Amit Kundu, "On an Irreducibility Question Concerning Palindromic Non-cyclotomic 0,1-Polynomials", Section 1 (terminology).

Formalized by `MathlibExt.Algebra.PalindromicZeroOneWanted.isZeroOnePoly_iff`, a theorem declared in [WantedExt/Algebra/PalindromicZeroOneWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/PalindromicZeroOneWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/reciprocal-0-1-polynomials/index.html#is-zero-one-poly-iff).

## Non-cyclotomic polynomial

A polynomial $f \in \mathbb{Z}[x]$ is *non-cyclotomic* if
$f \ne \Phi_n$ for every positive integer $n$, where $\Phi_n$ denotes the $n$-th cyclotomic
polynomial.

## Sources

- Pradipto Banerjee and Amit Kundu, "On an Irreducibility Question Concerning Palindromic Non-cyclotomic 0,1-Polynomials", Section 1 (terminology).

Formalized by `MathlibExt.Algebra.PalindromicZeroOneWanted.IsNoncyclotomic`, a definition declared in [WantedExt/Algebra/PalindromicZeroOneWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/PalindromicZeroOneWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/reciprocal-0-1-polynomials/index.html#is-noncyclotomic).

## Characterization of non-cyclotomic polynomials

A polynomial $f \in \mathbb{Z}[x]$ is
non-cyclotomic if and only if $f \ne \Phi_n$ for every positive integer $n$, where $\Phi_n$
denotes the $n$-th cyclotomic polynomial.

## Sources

- Pradipto Banerjee and Amit Kundu, "On an Irreducibility Question Concerning Palindromic Non-cyclotomic 0,1-Polynomials", Section 1 (terminology).

Formalized by `MathlibExt.Algebra.PalindromicZeroOneWanted.isNoncyclotomic_iff`, a theorem declared in [WantedExt/Algebra/PalindromicZeroOneWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/PalindromicZeroOneWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/reciprocal-0-1-polynomials/index.html#is-noncyclotomic-iff).

## Even–odd decomposition of a reciprocal polynomial

Let $h \in \mathbb{Z}[x]$ be an
irreducible reciprocal polynomial of degree $2k$ such that $h \ne g(x^2)$ for every
$g \in \mathbb{Z}[x]$. Then there is exactly one $h_e \in \mathbb{Z}[x]$ for which there is
exactly one $h_o \in \mathbb{Z}[x]$ for which there is exactly one natural number $\ell$
such that $h_e$ and $h_o$ are reciprocal, $\ell$ is odd and positive, $\deg h_e = k$,
$\deg h_o = \max(k - \ell, 0)$, $h(x) = h_e(x^2) + x^\ell h_o(x^2)$ and
$h_e(0)\,h_o(0) \ne 0$.

Since $\ell$ is odd, $h_e(x^2)$ is the even part of $h$, and $h_o(0) \ne 0$ then determines
$\ell$ and $h_o$; so this amounts to a unique triple $(h_e, h_o, \ell)$.

## Sources

- Pradipto Banerjee and Amit Kundu, "On an Irreducibility Question Concerning Palindromic Non-cyclotomic 0,1-Polynomials", Lemma 2.1.

Stated but not proved: `MathlibExt.Algebra.PalindromicZeroOneWanted.existsUnique_evenOdd_reciprocal` is written with `theorem_wanted` in [WantedExt/Algebra/PalindromicZeroOneWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/PalindromicZeroOneWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/reciprocal-0-1-polynomials/index.html#exists-unique-even-odd-reciprocal).

## Even–odd decomposition of a reciprocal 0,1-polynomial

Let $f \in \mathbb{Z}[x]$ be
an irreducible reciprocal $0,1$-polynomial of degree $2m$ such that $f(x^2)$ is not
irreducible. Then there is exactly one $f_e \in \mathbb{Z}[x]$ for which there is exactly
one $f_o \in \mathbb{Z}[x]$ for which there is exactly one natural number $\ell$ such that
$f_e$ and $f_o$ are reciprocal $0,1$-polynomials, $\ell$ is odd and positive,
$\deg f_e = m$, $\deg f_o = \max(m - \ell, 0)$, $f(x) = f_e(x^2) + x^\ell f_o(x^2)$ and
$f_e(0)\,f_o(0) \ne 0$.

Since $\ell$ is odd, $f_e(x^2)$ is the even part of $f$, and $f_o(0) \ne 0$ then determines
$\ell$ and $f_o$; so this amounts to a unique triple $(f_e, f_o, \ell)$.

## Sources

- Pradipto Banerjee and Amit Kundu, "On an Irreducibility Question Concerning Palindromic Non-cyclotomic 0,1-Polynomials", Lemma 2.2.

Stated but not proved: `MathlibExt.Algebra.PalindromicZeroOneWanted.existsUnique_evenOdd_zeroOne` is written with `theorem_wanted` in [WantedExt/Algebra/PalindromicZeroOneWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/PalindromicZeroOneWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/reciprocal-0-1-polynomials/index.html#exists-unique-even-odd-zero-one).

## Position of the first odd exponent

Let $f \in \mathbb{Z}[x]$ be an irreducible,
reciprocal, non-cyclotomic $0,1$-polynomial of degree $2m$ such that $f(x^2)$ is not
irreducible. Let $f_e, f_o \in \mathbb{Z}[x]$ and let $\ell$ be a positive odd integer with
$f(x) = f_e(x^2) + x^\ell f_o(x^2)$, $\deg f_e = m$ and $\deg f_o = \max(m - \ell, 0)$, where
the degree of the zero polynomial is taken to be $0$. Then the coefficient of $x^e$ in $f$ is
$0$ for every $1 \le e < \ell$, the coefficient of $x^\ell$ in $f$ is nonzero, and $2\ell < m$.

## Sources

- Pradipto Banerjee and Amit Kundu, "On an Irreducibility Question Concerning Palindromic Non-cyclotomic 0,1-Polynomials", Lemma 2.3.

Stated but not proved: `MathlibExt.Algebra.PalindromicZeroOneWanted.l_eq_min_support_and_lt` is written with `theorem_wanted` in [WantedExt/Algebra/PalindromicZeroOneWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/PalindromicZeroOneWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/reciprocal-0-1-polynomials/index.html#l-eq-min-support-and-lt).

## Irreducibility under repeated squaring of the variable

Let $f \in \mathbb{Z}[x]$ be
an irreducible, reciprocal, non-cyclotomic $0,1$-polynomial with fewer than $15$ nonzero
coefficients. Then $f(x^{2^n})$ is irreducible in $\mathbb{Z}[x]$ for every natural
number $n$.

## Sources

- Pradipto Banerjee and Amit Kundu, "On an Irreducibility Question Concerning Palindromic Non-cyclotomic 0,1-Polynomials", Theorem 1.1.

Stated but not proved: `MathlibExt.Algebra.PalindromicZeroOneWanted.irreducible_comp_pow_two_pow_of_card_lt` is written with `theorem_wanted` in [WantedExt/Algebra/PalindromicZeroOneWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/PalindromicZeroOneWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/reciprocal-0-1-polynomials/index.html#irreducible-comp-pow-two-pow-of-card-lt).

## Capelli's theorem for $f(x^r)$

Let $f \in \mathbb{Z}[x]$ be irreducible in
$\mathbb{Z}[x]$ and let $r \ge 2$ be an integer. Then $f(x^r)$ is reducible if and only if
either $f(x^p)$ is reducible for some prime $p$ dividing $r$, or $4$ divides $r$ and
$f(x^4)$ is reducible. Here reducible means not irreducible in $\mathbb{Z}[x]$.

## Sources

- Pradipto Banerjee and Amit Kundu, "On an Irreducibility Question Concerning Palindromic Non-cyclotomic 0,1-Polynomials", Theorem 1.2 (Capelli; the root-theoretic equivalents stated there are omitted).

Stated but not proved: `MathlibExt.Algebra.PalindromicZeroOneWanted.not_irreducible_comp_pow_iff` is written with `theorem_wanted` in [WantedExt/Algebra/PalindromicZeroOneWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/PalindromicZeroOneWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/reciprocal-0-1-polynomials/index.html#not-irreducible-comp-pow-iff).

## Square compositions of $0,1$-polynomials modulo $4$

Let $f \in \mathbb{Z}[x]$ be
irreducible in $\mathbb{Z}[x]$, with every coefficient equal to $0$ or $1$ and with constant
term $f(0) = 1$. If $f(x^2)$ is not irreducible in $\mathbb{Z}[x]$, then
$f(x^2) \equiv f(x)\,f(-x) \pmod 4$ as polynomials, that is, the two polynomials have the
same image in $(\mathbb{Z}/4\mathbb{Z})[x]$.

## Sources

- Pradipto Banerjee and Amit Kundu, "On an Irreducibility Question Concerning Palindromic Non-cyclotomic 0,1-Polynomials", Theorem 1.3.

Stated but not proved: `MathlibExt.Algebra.PalindromicZeroOneWanted.map_comp_sq_eq_mul` is written with `theorem_wanted` in [WantedExt/Algebra/PalindromicZeroOneWanted.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/PalindromicZeroOneWanted.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/reciprocal-0-1-polynomials/index.html#map-comp-sq-eq-mul).

## Reducibility of $f(x^4)$ and $f(x^2)$ for $0,1$-polynomials

Let
$f \in \mathbb{Z}[x]$ be irreducible in $\mathbb{Z}[x]$ and of positive degree, with every
coefficient equal to $0$ or $1$ and with constant term $f(0) = 1$. Then $f(x^4)$ is not
irreducible in $\mathbb{Z}[x]$ if and only if $f(x^2)$ is not irreducible in $\mathbb{Z}[x]$.

## Sources

- Pradipto Banerjee and Amit Kundu, "On an Irreducibility Question Concerning Palindromic Non-cyclotomic 0,1-Polynomials", Theorem 1.4.

Stated but not proved: `MathlibExt.Algebra.PalindromicZeroOneWanted.not_irreducible_comp_four_iff` is written with `theorem_wanted` in [WantedExt/Algebra/PalindromicZeroOneWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/PalindromicZeroOneWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/reciprocal-0-1-polynomials/index.html#not-irreducible-comp-four-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reciprocal 0,1-polynomials](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/reciprocal-0-1-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/polynomials/reciprocal-0-1-polynomials)
