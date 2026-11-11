---
declaration: section
origin: cited
lean: MetaMathlibExt.lipSubring, MetaMathlibExt.mem_lipSubring_iff, MetaMathlibExt.triangular_not_mem_lipSubring_univ, MetaMathlibExt.polynomialToLIP, MetaMathlibExt.polynomialToLIP_apply, MetaMathlibExt.interpolationPoly, MetaMathlibExt.eval_interpolationPoly, MetaMathlibExt.degree_interpolationPoly_lt
statement: formalized
---

# Locally integer polynomial functions

37 results, 8 proved and 29 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html).

## The ring $\mathrm{LIP}(U)$ of locally integer polynomial functions

For
$U \subseteq \mathbb{Z}$, $\mathrm{LIP}(U)$ is the subring of the ring of all functions
$U \to \mathbb{Z}$ (with pointwise operations) consisting of the functions $f$ such that for
every finite subset $X \subseteq U$ there is a polynomial $p \in \mathbb{Z}[x]$ with $p(x) = f(x)$
for all $x \in X$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Definitions 1 and 2.

Formalized by `MetaMathlibExt.lipSubring`, a definition declared in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#lip-subring).

## Membership in $\mathrm{LIP}(U)$

For $U \subseteq \mathbb{Z}$ and $f : U \to \mathbb{Z}$,
$f$ lies in $\mathrm{LIP}(U)$ if and only if for every finite subset $X \subseteq U$ there is a
polynomial $p \in \mathbb{Z}[x]$ with $p(x) = f(x)$ for all $x \in X$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Definition 1.

Formalized by `MetaMathlibExt.mem_lipSubring_iff`, a theorem declared in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#mem-lip-subring-iff).

## The triangular-number function is not LIP on the integers

The function
$x \mapsto x(x+1)/2$ on $\mathbb{Z}$ (an integer, since $x(x+1)$ is even) does not belong to
$\mathrm{LIP}(\mathbb{Z})$: no integer polynomial $p$ takes the values $0, 0, 1$ at $-1, 0, 1$,
since $1 - (-1)$ must divide $p(1) - p(-1)$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Section 1 and Example 2.

Formalized by `MetaMathlibExt.triangular_not_mem_lipSubring_univ`, a theorem declared in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#triangular-not-mem-lip-subring-univ).

## The evaluation map from $\mathbb{Z}(x)$ to $\mathrm{LIP}(U)$

For $U \subseteq \mathbb{Z}$,
the evaluation map is the ring homomorphism from $\mathbb{Z}[x]$ to the ring $\mathrm{LIP}(U)$ of
locally integer polynomial functions on $U$ that sends each integer polynomial $p$ to the function
$U \to \mathbb{Z}$, $u \mapsto p(u)$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Lemma 1.

Formalized by `MetaMathlibExt.polynomialToLIP`, a definition declared in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#polynomial-to-lip).

## Values of the evaluation map into LIP(U)

For $U \subseteq \mathbb{Z}$, an integer
polynomial $p \in \mathbb{Z}[x]$ and $u \in U$, the image of $p$ under the evaluation map
$\mathbb{Z}[x] \to \mathrm{LIP}(U)$ takes the value $p(u)$ at $u$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Lemma 1.

Formalized by `MetaMathlibExt.polynomialToLIP_apply`, a theorem declared in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#polynomial-to-lip-apply).

## Interpolation polynomial

Let $X \subseteq \mathbb{Z}$ be finite and
$f : \mathbb{Z} \to \mathbb{Z}$. The interpolation polynomial $f_X \in \mathbb{Q}[x]$ of $f$ on $X$
is the Lagrange interpolation polynomial: the unique polynomial with rational coefficients of
degree less than $|X|$ such that $f_X(x) = f(x)$ for every $x \in X$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Section 1 and Definition 3.

Formalized by `MetaMathlibExt.interpolationPoly`, a definition declared in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#interpolation-poly).

## The interpolation polynomial agrees with the function on its nodes

Let
$X \subseteq \mathbb{Z}$ be finite and $f : \mathbb{Z} \to \mathbb{Z}$. The interpolation polynomial
$f_X \in \mathbb{Q}[x]$ of $f$ on $X$ satisfies $f_X(x) = f(x)$ for every $x \in X$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Section 1.

Formalized by `MetaMathlibExt.eval_interpolationPoly`, a theorem declared in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#eval-interpolation-poly).

## Degree bound for the interpolation polynomial

Let $X \subseteq \mathbb{Z}$ be finite and
$f : \mathbb{Z} \to \mathbb{Z}$. The interpolation polynomial $f_X \in \mathbb{Q}[x]$ of $f$ on $X$
has degree less than $|X|$, where the zero polynomial has degree $-\infty$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Section 1.

Formalized by `MetaMathlibExt.degree_interpolationPoly_lt`, a theorem declared in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#degree-interpolation-poly-lt).

## Integer polynomials embed in LIP(U)

For every infinite set $U \subseteq \mathbb{Z}$, the
evaluation map $\mathbb{Z}[x] \to \mathrm{LIP}(U)$, sending $p$ to the function $u \mapsto p(u)$,
is injective: distinct integer polynomials give distinct functions on $U$.

The other part of Lemma 1, that $\mathrm{LIP}(U)$ is a subring of the ring of all functions
$U \to \mathbb{Z}$, holds by construction.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Lemma 1.

Stated but not proved: `MetaMathlibExt.polynomialToLIP_injective` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#polynomial-to-lip-injective).

## Integrality of low-degree interpolants

Let $X \subseteq \mathbb{Z}$ be finite, let
$q \in \mathbb{Q}[x]$ have degree less than $|X|$, and let $p \in \mathbb{Z}[x]$ satisfy
$q(x) = p(x)$ for all $x \in X$. Then $q$ has integer coefficients, that is, $q$ is the image in
$\mathbb{Q}[x]$ of a polynomial in $\mathbb{Z}[x]$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Lemma 2.

Stated but not proved: `MetaMathlibExt.mem_lifts_of_degree_lt_of_eval_eq` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#mem-lifts-of-degree-lt-of-eval-eq).

## A locally integer polynomial function with infinitely many zeros is zero

Let
$U \subseteq \mathbb{Z}$ and let $f : U \to \mathbb{Z}$ lie in the ring $\mathrm{LIP}(U)$ of
locally integer polynomial functions on $U$. If $f(x) = 0$ for infinitely many $x \in U$, then
$f(x) = 0$ for every $x \in U$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Lemma 3.

Stated but not proved: `MetaMathlibExt.lip_eq_zero_of_infinite_zeros` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#lip-eq-zero-of-infinite-zeros).

## Locally integer polynomial functions agreeing on an infinite subset are equal

Let
$U \subseteq V \subseteq \mathbb{Z}$ with $U$ infinite, and let $f, g : V \to \mathbb{Z}$ lie in
the ring $\mathrm{LIP}(V)$ of locally integer polynomial functions on $V$. If $f(x) = g(x)$ for
every $x \in U$, then $f = g$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Corollary 1.

Stated but not proved: `MetaMathlibExt.lip_restrict_injective` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#lip-restrict-injective).

## Locally integer polynomial functions on an infinite set form a domain

For every infinite
$U \subseteq \mathbb{Z}$, the ring $\mathrm{LIP}(U)$ of locally integer polynomial functions
$U \to \mathbb{Z}$ is an integral domain.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Lemma 4.

Stated but not proved: `MetaMathlibExt.lipSubring_isDomain` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#lip-subring-is-domain).

## Units of $\mathrm{LIP}(U)$

For every infinite set $U \subseteq \mathbb{Z}$, the only
units of the ring $\mathrm{LIP}(U)$ of locally integer polynomial functions on $U$ are the
constant functions $1$ and $-1$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Lemma 4.

Stated but not proved: `MetaMathlibExt.lipSubring_units_eq` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#lip-subring-units-eq).

## Integer polynomials take a large value at a small nonnegative integer

Let
$f \in \mathbb{Z}[x]$ have degree $d$. Then there is an integer $x$ with $0 \le x \le d$ such that
$|f(x)| \ge d!/2^d$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Lemma 5.

Stated but not proved: `MetaMathlibExt.exists_factorial_div_two_pow_le_abs_eval` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#exists-factorial-div-two-pow-le-abs-eval).

## Exchange formula for interpolation polynomials

Let $f : \mathbb{Z} \to \mathbb{Z}$, and for
a finite set $Y \subseteq \mathbb{Z}$ write $f_Y \in \mathbb{Q}[x]$ for the interpolation polynomial
of $f$ on $Y$. Let $X \subseteq \mathbb{Z}$ be finite and $a, b \in \mathbb{Z} \setminus X$, and let
$c$ be the coefficient of $x^{|X|+1}$ in $f_{X \cup \{a, b\}}$. Then

$$f_{X \cup \{a\}} = f_{X \cup \{b\}} + c\,(a - b) \prod_{z \in X} (x - z).$$

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Lemma 6.

Stated but not proved: `MetaMathlibExt.interpolationPoly_exchange` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#interpolation-poly-exchange).

## Denominator of the top coefficient on a circuit

Let $f : \mathbb{Z} \to \mathbb{Z}$, and
for a finite set $Y \subseteq \mathbb{Z}$ write $f_Y \in \mathbb{Q}[x]$ for the interpolation
polynomial of $f$ on $Y$. Let $X \subseteq \mathbb{Z}$ be a finite circuit for $f$: $f_X$ does not
have integer coefficients, but $f_{X \setminus \{a\}}$ has integer coefficients for every
$a \in X$. Let $c$ be the coefficient of $x^{|X|-1}$ in $f_X$ and let $q \ge 1$ be the denominator
of $c$ in lowest terms. Then $q \ne 1$, so $c$ is not an integer, and $q$ divides $a - b$ for all
$a, b \in X$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Lemma 7, with the circuit definition preceding it.

Stated but not proved: `MetaMathlibExt.circuit_coeff_den` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#circuit-coeff-den).

## Intersection of two arithmetic progressions of natural numbers

Let $a_1, a_2, d_1, d_2$
be natural numbers with $d_1, d_2 > 0$, where $\mathbb{N} = \{0, 1, 2, \dots\}$, and let
$P_i = \{a_i + d_i n : n \in \mathbb{N}\}$ for $i = 1, 2$. Then $P_1 \cap P_2$ is nonempty if
and only if $\gcd(d_1, d_2)$ divides the integer $a_1 - a_2$, and if $P_1 \cap P_2$ is nonempty,
then $P_1 \cap P_2 = \{a_3 + \operatorname{lcm}(d_1, d_2)\, n : n \in \mathbb{N}\}$ for some
$a_3 \in \mathbb{N}$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Lemma 8.

Stated but not proved: `MetaMathlibExt.natProgression_inter` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#nat-progression-inter).

## Two intersecting progressions share infinitely many terms with a third

Let
$a_1, a_2, d_1, d_2, a, b$ be natural numbers with $d_1, d_2 > 0$, where
$\mathbb{N} = \{0, 1, 2, \dots\}$, and let $P_i = \{a_i + d_i n : n \in \mathbb{N}\}$ for
$i = 1, 2$. If $a \in P_1$, $b \in P_2$, $P_1 \cap P_2$ is nonempty and $a \neq b$, then
$P_1 \cap P_2$ contains infinitely many elements of the progression
$\{\min(a, b) + |a - b|\, n : n \in \mathbb{N}\}$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Lemma 9.

Stated but not proved: `MetaMathlibExt.natProgression_inter_infinite` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#nat-progression-inter-infinite).

## Newton series of locally integer polynomial functions

Let $U \subseteq \mathbb{Z}$, let
$\mathbb{N} = \{0, 1, 2, \dots\}$, and let $\sigma : \mathbb{N} \to U$ be a bijection. For a
sequence of integers $a = (a_k)_{k \in \mathbb{N}}$ define $f_a : U \to \mathbb{Z}$ by

$$f_a(u) = \sum_{k=0}^{\sigma^{-1}(u)} a_k \prod_{i=0}^{k-1} (u - \sigma(i)).$$

Then $f_a$ lies in the ring $\mathrm{LIP}(U)$ of locally integer polynomial functions on $U$ for
every sequence $a$, and every $f \in \mathrm{LIP}(U)$ equals $f_a$ for exactly one sequence $a$.

For $u = \sigma(m)$ every product with $k > m$ contains the factor $u - \sigma(m) = 0$, so $f_a$
is the formal series $\sum_{k \ge 0} a_k \prod_{i < k} (x - \sigma(i))$ evaluated at $x = u$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Theorem 1, reindexed from `σ(1), σ(2), …`.

Stated but not proved: `MetaMathlibExt.lipSubring_newton_series` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#lip-subring-newton-series).

## LIP functions with infinitely many prime values are irreducible

Let
$U \subseteq \mathbb{Z}$, and write $\mathrm{LIP}(U)$ for the ring of locally integer polynomial
functions on $U$: the functions $U \to \mathbb{Z}$ whose restriction to every finite subset of $U$
agrees with a polynomial with integer coefficients. Let $f \in \mathrm{LIP}(U)$. If $|f(x)|$ is a
prime number for infinitely many $x \in U$, then $f$ is irreducible in the ring $\mathrm{LIP}(U)$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Theorem 2.

Stated but not proved: `MetaMathlibExt.irreducible_of_infinite_prime_values` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#irreducible-of-infinite-prime-values).

## A LIP function bounded by $C|x|^d$ infinitely often is a polynomial

Let
$U \subseteq \mathbb{Z}$, let $C$ be a real number and $d \ge 0$ an integer, and let
$f \in \mathrm{LIP}(U)$. If $|f(x)| \le C|x|^d$ for infinitely many $x \in U$, then there is a
polynomial $p \in \mathbb{Z}[x]$ with $f(x) = p(x)$ for all $x \in U$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Theorem 3.

Stated but not proved: `MetaMathlibExt.mem_range_polynomialToLIP_of_bound` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#mem-range-polynomial-to-lip-of-bound).

## Prime integer polynomials stay prime in LIP(U)

Let $U \subseteq \mathbb{Z}$ be infinite
and let $p$ be a prime element of $\mathbb{Z}[x]$ (a prime of $\mathbb{Z}$, or an irreducible
integer polynomial of content $1$). Then the function $u \mapsto p(u)$, the image of $p$ under
the evaluation map $\mathbb{Z}[x] \to \mathrm{LIP}(U)$, is a prime element of $\mathrm{LIP}(U)$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Corollary 2.

Stated but not proved: `MetaMathlibExt.prime_polynomialToLIP` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#prime-polynomial-to-lip).

## $\mathbb{Z}(x)$ is algebraically closed in $\mathrm{LIP}(U)$

Let $U \subseteq \mathbb{Z}$
be infinite, and map each $p \in \mathbb{Z}[x]$ to the function $u \mapsto p(u)$ in
$\mathrm{LIP}(U)$. Let $f \in \mathrm{LIP}(U)$ and let $Q$ be a nonzero polynomial with
coefficients in $\mathbb{Z}[x]$ such that $Q(f) = 0$ in $\mathrm{LIP}(U)$, where the
coefficients of $Q$ are mapped into $\mathrm{LIP}(U)$ in this way. Then there is
$p \in \mathbb{Z}[x]$ with $f(u) = p(u)$ for all $u \in U$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Corollary 3.

Stated but not proved: `MetaMathlibExt.mem_range_polynomialToLIP_of_isAlgebraic` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#mem-range-polynomial-to-lip-of-is-algebr).

## Infinite ascending chains of principal ideals in LIP rings

Let $U \subseteq \mathbb{Z}$ be
infinite, and write $\mathrm{LIP}(U)$ for the ring of locally integer polynomial functions on $U$:
the functions $U \to \mathbb{Z}$ whose restriction to every finite subset of $U$ agrees with a
polynomial with integer coefficients. Then there are $g_0, g_1, g_2, \ldots \in \mathrm{LIP}(U)$
such that the principal ideals of $\mathrm{LIP}(U)$ they generate form a strictly increasing chain
$(g_0) \subsetneq (g_1) \subsetneq (g_2) \subsetneq \cdots$.

In particular $\mathrm{LIP}(U)$ is not Noetherian.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Theorem 4.

Stated but not proved: `MetaMathlibExt.exists_strictMono_principal_ideals` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#exists-strict-mono-principal-ideals).

## $\mathrm{LIP}(\mathbb{Z})$ is closed under composition

If $f$ and $g$ lie in
$\mathrm{LIP}(\mathbb{Z})$, the ring of locally integer polynomial functions
$\mathbb{Z} \to \mathbb{Z}$, then so does the composite $x \mapsto f(g(x))$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Theorem 5.

Stated but not proved: `MetaMathlibExt.lip_univ_comp` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#lip-univ-comp).

## $\mathrm{LIP}(\mathbb{Z})$ is closed under the discrete derivative

If $f$ lies in
$\mathrm{LIP}(\mathbb{Z})$, the ring of locally integer polynomial functions
$\mathbb{Z} \to \mathbb{Z}$, then so does the function $x \mapsto f(x) - f(x - 1)$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Theorem 5.

Stated but not proved: `MetaMathlibExt.lip_univ_sub_shift` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#lip-univ-sub-shift).

## Non-polynomial LIP functions on the integers that are small on an infinite set

Let
$\tau : \mathbb{N} \to \mathbb{R}$ with $\tau(n) \to +\infty$ as $n \to \infty$. Write
$\mathrm{LIP}(\mathbb{Z})$ for the ring of locally integer polynomial functions on $\mathbb{Z}$:
the functions $\mathbb{Z} \to \mathbb{Z}$ whose restriction to every finite subset of $\mathbb{Z}$
agrees with a polynomial with integer coefficients. Then there is $f \in \mathrm{LIP}(\mathbb{Z})$
that is not of the form $x \mapsto p(x)$ for any $p \in \mathbb{Z}[x]$, together with an infinite
set $X \subseteq \mathbb{Z}$ such that $|f(x)| < |x|^{\tau(|x|)}$ for every $x \in X$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Theorem 6.

Stated but not proved: `MetaMathlibExt.exists_lip_univ_not_polynomial_lt_rpow` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#exists-lip-univ-not-polynomial-lt-rpow).

## LIP functions on $\mathbb{Z}$ below the factorial bound are polynomials

Let $f$ lie in
$\mathrm{LIP}(\mathbb{Z})$, the ring of locally integer polynomial functions
$\mathbb{Z} \to \mathbb{Z}$. If $|f(x)| < (2|x| - 1)!/2^{2|x| - 1}$ for all but finitely many
$x \in \mathbb{Z}$, then there is a polynomial $p \in \mathbb{Z}[x]$ with $f(x) = p(x)$ for all
$x \in \mathbb{Z}$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Theorem 7.

Stated but not proved: `MetaMathlibExt.mem_range_polynomialToLIP_of_factorial_bound` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#mem-range-polynomial-to-lip-of-factorial).

## LIP continuation at two points

Let $f : \mathbb{Z} \to \mathbb{Z}$, and for a finite set
$Y \subseteq \mathbb{Z}$ write $f_Y \in \mathbb{Q}[x]$ for the interpolation polynomial of $f$ on
$Y$. For $S \subseteq \mathbb{Z}$ write $\mathrm{LIP}(S)$ for the ring of locally integer
polynomial functions on $S$: the functions $S \to \mathbb{Z}$ whose restriction to every finite
subset of $S$ agrees with a polynomial with integer coefficients. Let $X \subseteq \mathbb{Z}$ be
finite and $a, b \in \mathbb{Z}$ such that $f_{X \cup \{a, b\}}$ does not have integer
coefficients, while $f_{X \cup \{a\}}$ and $f_{X \cup \{b\}}$ both do (this forces $a \ne b$ and
$a, b \notin X$). Put $V = \{x \in \mathbb{Z} : \gcd(x - a, a - b) = 1\}$. Then $|a - b| \ge 2$,
and there is a function $g : \mathbb{Z} \to \mathbb{Z}$ with $g(x) = f(x)$ for all
$x \in X \cup \{a, b\}$ whose restriction to $X \cup V \cup \{a\}$ lies in
$\mathrm{LIP}(X \cup V \cup \{a\})$ and whose restriction to $X \cup V \cup \{b\}$ lies in
$\mathrm{LIP}(X \cup V \cup \{b\})$.

This is the form of Theorem 8 established in its proof in the source.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Theorem 8.

Stated but not proved: `MetaMathlibExt.lip_continuation_two_points` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#lip-continuation-two-points).

## Locally integer polynomial functions on a union of sets

For $S \subseteq \mathbb{Z}$, write
$\mathrm{LIP}(S)$ for the ring of locally integer polynomial functions $S \to \mathbb{Z}$. Let
$(V_i)_{i \in I}$ be a family of subsets of $\mathbb{Z}$ with union $U = \bigcup_{i \in I} V_i$.
Suppose that for all $i, j \in I$, not necessarily distinct, and all $a_1 \in V_i$ and
$a_2 \in V_j$ with $a_1 \ne a_2$, the set $V_i \cap V_j$ contains infinitely many elements of
$\{a_1 + (a_2 - a_1) n : n \in \mathbb{Z}\}$. Then for every $f : \mathbb{Z} \to \mathbb{Z}$, the
restriction of $f$ to $U$ lies in $\mathrm{LIP}(U)$ if and only if, for every $i \in I$, the
restriction of $f$ to $V_i$ lies in $\mathrm{LIP}(V_i)$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Theorem 9.

Stated but not proved: `MetaMathlibExt.lip_iUnion_iff` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 354](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L354). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#lip-i-union-iff).

## Locally integer polynomial functions on cofinite sets of positive integers

Let
$\mathbb{N}^+ = \{n \in \mathbb{Z} : n > 0\}$, let $U \subseteq \mathbb{N}^+$ with
$\mathbb{N}^+ \setminus U$ finite, let $f : \mathbb{Z} \to \mathbb{Z}$, and for
$S \subseteq \mathbb{Z}$ write $\mathrm{LIP}(S)$ for the ring of locally integer polynomial (LIP)
functions $S \to \mathbb{Z}$. Then the restriction of $f$ to $U$ lies in $\mathrm{LIP}(U)$ if and
only if every $a \in U$ lies in some $W \subseteq U$ with $\mathbb{N}^+ \setminus W$ finite such
that the restriction of $f$ to $W$ lies in $\mathrm{LIP}(W)$.

In the cofinite topology on $\mathbb{N}^+$ the nonempty open sets are the subsets with finite
complement, so this says that a function which is LIP on an open neighbourhood of each point of
a nonempty open set $U$ is LIP on $U$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Corollary 4.

Stated but not proved: `MetaMathlibExt.lip_sheaf_cofinite_nat` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#lip-sheaf-cofinite-nat).

## Locally integer polynomial functions on cofinite subsets of the integers

Let
$U \subseteq \mathbb{Z}$ have finite complement, let $f : \mathbb{Z} \to \mathbb{Z}$, and for
$S \subseteq \mathbb{Z}$ write $\mathrm{LIP}(S)$ for the ring of locally integer polynomial (LIP)
functions $S \to \mathbb{Z}$. Then the restriction of $f$ to $U$ lies in $\mathrm{LIP}(U)$ if and
only if every $a \in U$ lies in some $W \subseteq U$ with finite complement in $\mathbb{Z}$ such
that the restriction of $f$ to $W$ lies in $\mathrm{LIP}(W)$.

In the cofinite topology on $\mathbb{Z}$ the nonempty open sets are the sets with finite
complement, so this says that a function which is LIP on an open neighbourhood of each point of
a nonempty open set $U$ is LIP on $U$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Corollary 4.

Stated but not proved: `MetaMathlibExt.lip_sheaf_cofinite_int` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#lip-sheaf-cofinite-int).

## Locally integer polynomial functions on density one sets of positive integers

Say that
a set $S$ of positive integers has natural density one if $\#(S \cap [1, x]) / x \to 1$ as the
natural number $x$ tends to infinity, and write $\mathrm{LIP}(S)$ for the ring of locally
integer polynomial (LIP) functions $S \to \mathbb{Z}$. Let $U$ be a set of positive integers of
natural density one and let $f : \mathbb{Z} \to \mathbb{Z}$. Then the restriction of $f$ to $U$
lies in $\mathrm{LIP}(U)$ if and only if every $a \in U$ lies in some $W \subseteq U$ of natural
density one such that the restriction of $f$ to $W$ lies in $\mathrm{LIP}(W)$.

In the density one topology on the positive integers the nonempty open sets are the sets of
natural density one, so this says that a function which is LIP on an open neighbourhood of each
point of a nonempty open set $U$ is LIP on $U$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Corollary 4.

Stated but not proved: `MetaMathlibExt.lip_sheaf_densityOne_nat` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#lip-sheaf-density-one-nat).

## Locally integer polynomial functions on density one subsets of the integers

Say that
$S \subseteq \mathbb{Z}$ has density one if $\#(S \cap [-x, x]) / (2x + 1) \to 1$ as the natural
number $x$ tends to infinity, and write $\mathrm{LIP}(S)$ for the ring of locally integer
polynomial (LIP) functions $S \to \mathbb{Z}$. Let $U \subseteq \mathbb{Z}$ have density one and
let $f : \mathbb{Z} \to \mathbb{Z}$. Then the restriction of $f$ to $U$ lies in $\mathrm{LIP}(U)$
if and only if every $a \in U$ lies in some $W \subseteq U$ of density one such that the
restriction of $f$ to $W$ lies in $\mathrm{LIP}(W)$.

In the density one topology on $\mathbb{Z}$ the nonempty open sets are the sets of density one,
so this says that a function which is LIP on an open neighbourhood of each point of a nonempty
open set $U$ is LIP on $U$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Corollary 4.

Stated but not proved: `MetaMathlibExt.lip_sheaf_densityOne_int` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 398](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L398). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#lip-sheaf-density-one-int).

## Locally integer polynomial functions on cofinite sets of primes

Let $P$ be the set of
positive prime numbers in $\mathbb{Z}$, let $U \subseteq P$ with $P \setminus U$ finite, let
$f : \mathbb{Z} \to \mathbb{Z}$, and for $S \subseteq \mathbb{Z}$ write $\mathrm{LIP}(S)$ for the
ring of locally integer polynomial (LIP) functions $S \to \mathbb{Z}$. Then the restriction of
$f$ to $U$ lies in $\mathrm{LIP}(U)$ if and only if every $a \in U$ lies in some $W \subseteq U$
with $P \setminus W$ finite such that the restriction of $f$ to $W$ lies in $\mathrm{LIP}(W)$.

In the cofinite topology on $P$ the nonempty open sets are the subsets with finite complement,
so this says that a function which is LIP on an open neighbourhood of each point of a nonempty
open set $U$ is LIP on $U$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Corollary 5.

Stated but not proved: `MetaMathlibExt.lip_sheaf_cofinite_primes` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 412](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L412). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#lip-sheaf-cofinite-primes).

## Gluing LIP functions on two intersecting progressions

Let $a_1, a_2 \ge 0$ and
$d_1, d_2 \ge 1$ be integers, let $U_i = \{a_i + d_i n : n \in \mathbb{Z}, n \ge 0\}$ for
$i = 1, 2$, and suppose $U_1 \cap U_2$ is nonempty. If $f : \mathbb{Z} \to \mathbb{Z}$ restricts
to an element of $\mathrm{LIP}(U_1)$ on $U_1$ and to an element of $\mathrm{LIP}(U_2)$ on $U_2$,
then the restriction of $f$ to $U_1 \cup U_2$ lies in $\mathrm{LIP}(U_1 \cup U_2)$.

## Sources

- Alexander Borisov, *Locally Integer Polynomial Functions*, INTEGERS 25 (2025), Article A41, Corollary 6.

Stated but not proved: `MetaMathlibExt.lip_union_natProgression` is written with `theorem_wanted` in [WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/LocallyIntegerPolynomialWanted.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html#lip-union-nat-progression).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Locally integer polynomial functions](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/ideals-and-constructions/locally-integer-polynomial-functions)
