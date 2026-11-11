---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ChowlaAndTwinPrimeOverFqTWanted.ChowlaAndTwinPrimeOverFqT.cardQuot_span_eq_pow_natDegree, MathlibExt.NumberTheory.ChowlaAndTwinPrimeOverFqTWanted.ChowlaAndTwinPrimeOverFqT.ringNorm, MathlibExt.NumberTheory.ChowlaAndTwinPrimeOverFqTWanted.ChowlaAndTwinPrimeOverFqT.norm_eq_cardQuot, MathlibExt.NumberTheory.ChowlaAndTwinPrimeOverFqTWanted.ChowlaAndTwinPrimeOverFqT.norm_eq_pow_natDegree, MathlibExt.NumberTheory.ChowlaAndTwinPrimeOverFqTWanted.ChowlaAndTwinPrimeOverFqT.primes, MathlibExt.NumberTheory.ChowlaAndTwinPrimeOverFqTWanted.ChowlaAndTwinPrimeOverFqT.indicator, MathlibExt.NumberTheory.ChowlaAndTwinPrimeOverFqTWanted.ChowlaAndTwinPrimeOverFqT.𝔖_q, MathlibExt.NumberTheory.ChowlaAndTwinPrimeOverFqTWanted.ChowlaAndTwinPrimeOverFqT.theorem_1_1
statement: formalized
---

# Twin primes and Chowla's conjecture over function fields

10 results, 8 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/twin-primes-and-chowla-s-conjecture-over-functio/index.html).

## Size of the quotient of $F(T)$ by a nonzero polynomial

Let $F$ be a field and let
$f \in F[T]$ be a nonzero polynomial. Then the cardinality of the quotient ring $F[T]/(f)$ is
$|F|^{\deg f}$, where cardinalities are natural numbers and an infinite set has cardinality $0$.

## Sources

- W. Sawin and M. Shusterman, *On the Chowla and twin primes conjectures over $\mathbb{F}_q[T]$*, Annals of Math. 196 (2) 2022, Equation (1.1).

Formalized by `MathlibExt.NumberTheory.ChowlaAndTwinPrimeOverFqTWanted.ChowlaAndTwinPrimeOverFqT.cardQuot_span_eq_pow_natDegree`, a theorem declared in [WantedExt/NumberTheory/ChowlaAndTwinPrimeOverFqTWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ChowlaAndTwinPrimeOverFqTWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/twin-primes-and-chowla-s-conjecture-over-functio/index.html#card-quot-span-eq-pow-nat-degree).

## The norm on $F(T)$

Let $F$ be a finite field. The ring norm on the polynomial ring $F[T]$
sends $f$ to the number of elements of the quotient ring $F[T]/(f)$, written
$|f| = |F[T]/(f)|$; for $f = 0$ the quotient is infinite and $|0| = 0$. It is a ring norm: $|f| = 0$
only for $f = 0$, $|-f| = |f|$, $|f + g| \le |f| + |g|$ and $|fg| \le |f|\,|g|$.

## Sources

- W. Sawin and M. Shusterman, *On the Chowla and twin primes conjectures over $\mathbb{F}_q[T]$*, Annals of Math. 196 (2) 2022, Equation (1.1).

Formalized by `MathlibExt.NumberTheory.ChowlaAndTwinPrimeOverFqTWanted.ChowlaAndTwinPrimeOverFqT.ringNorm`, a definition declared in [WantedExt/NumberTheory/ChowlaAndTwinPrimeOverFqTWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ChowlaAndTwinPrimeOverFqTWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/twin-primes-and-chowla-s-conjecture-over-functio/index.html#ring-norm).

## The norm of a polynomial is the size of its quotient ring

Let $F$ be a finite field and
give $F[T]$ its ring norm. For every $f \in F[T]$, the norm $|f|$ equals the number of elements of
the quotient ring $F[T]/(f)$, where an infinite quotient (the case $f = 0$) counts as $0$.

## Sources

- W. Sawin and M. Shusterman, *On the Chowla and twin primes conjectures over $\mathbb{F}_q[T]$*, Annals of Math. 196 (2) 2022, Equation (1.1).

Formalized by `MathlibExt.NumberTheory.ChowlaAndTwinPrimeOverFqTWanted.ChowlaAndTwinPrimeOverFqT.norm_eq_cardQuot`, a theorem declared in [WantedExt/NumberTheory/ChowlaAndTwinPrimeOverFqTWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ChowlaAndTwinPrimeOverFqTWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/twin-primes-and-chowla-s-conjecture-over-functio/index.html#norm-eq-card-quot).

## Norm of a nonzero polynomial

Let $F$ be a finite field and give $F[T]$ its ring norm.
For every nonzero $f \in F[T]$, the norm of $f$ is $|f| = |F|^{\deg f}$, where $|F|$ is the number
of elements of $F$.

## Sources

- W. Sawin and M. Shusterman, *On the Chowla and twin primes conjectures over $\mathbb{F}_q[T]$*, Annals of Math. 196 (2) 2022, Equation (1.1).

Formalized by `MathlibExt.NumberTheory.ChowlaAndTwinPrimeOverFqTWanted.ChowlaAndTwinPrimeOverFqT.norm_eq_pow_natDegree`, a theorem declared in [WantedExt/NumberTheory/ChowlaAndTwinPrimeOverFqTWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ChowlaAndTwinPrimeOverFqTWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/twin-primes-and-chowla-s-conjecture-over-functio/index.html#norm-eq-pow-nat-degree).

## Primes of $F(T)$

Let $F$ be a finite field. The primes of the polynomial ring $F[T]$ are
its monic irreducible polynomials.

## Sources

- W. Sawin and M. Shusterman, *On the Chowla and twin primes conjectures over $\mathbb{F}_q[T]$*, Annals of Math. 196 (2) 2022, the sentence after Equation (1.4).

Formalized by `MathlibExt.NumberTheory.ChowlaAndTwinPrimeOverFqTWanted.ChowlaAndTwinPrimeOverFqT.primes`, a definition declared in [WantedExt/NumberTheory/ChowlaAndTwinPrimeOverFqTWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ChowlaAndTwinPrimeOverFqTWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/twin-primes-and-chowla-s-conjecture-over-functio/index.html#primes).

## Indicator of a statement

For a proposition $P$, the indicator $\mathbf{1}_P$ is the real
number $1$ if $P$ holds and $0$ otherwise.

## Sources

- W. Sawin and M. Shusterman, *On the Chowla and twin primes conjectures over $\mathbb{F}_q[T]$*, Annals of Math. 196 (2) 2022, Equation (1.4).

Formalized by `MathlibExt.NumberTheory.ChowlaAndTwinPrimeOverFqTWanted.ChowlaAndTwinPrimeOverFqT.indicator`, a definition declared in [WantedExt/NumberTheory/ChowlaAndTwinPrimeOverFqTWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ChowlaAndTwinPrimeOverFqTWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/twin-primes-and-chowla-s-conjecture-over-functio/index.html#indicator).

## Singular series for twin primes in $F(T)$

Let $F$ be a finite field with $q$ elements and
let $h \in F[T]$. The Hardy–Littlewood constant of the prime pair $\{f, f + h\}$ is the infinite
product over all primes $P$ of $F[T]$ (the monic irreducible polynomials)

$$\mathfrak{S}_q(h) =
\prod_P \frac{1 - |P|^{-1} - |P|^{-1}\,\mathbf{1}_{P \nmid h}}{(1 - |P|^{-1})^2},$$

where $|P|$ is the norm of $P$ and $\mathbf{1}_{P \nmid h}$ is $1$ if $P$ does not divide $h$ and
$0$ otherwise.

The product is an unconditional infinite product of real numbers; when it does not converge its
value is taken to be $1$.

## Sources

- W. Sawin and M. Shusterman, *On the Chowla and twin primes conjectures over $\mathbb{F}_q[T]$*, Annals of Math. 196 (2) 2022, Equation (1.4).

Formalized by `MathlibExt.NumberTheory.ChowlaAndTwinPrimeOverFqTWanted.ChowlaAndTwinPrimeOverFqT.𝔖_q`, a definition declared in [WantedExt/NumberTheory/ChowlaAndTwinPrimeOverFqTWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ChowlaAndTwinPrimeOverFqTWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/twin-primes-and-chowla-s-conjecture-over-functio/index.html#q).

## Twin prime asymptotic over $\mathbb{F}_q(T)$ for large $q$

Let $p$ be an odd prime and let
$q$ be a power of $p$ with $q > 685090\,p^2$; write $\mathbb{F}_q$ for the finite field with $q$
elements. Then there is a real number $\varepsilon > 0$ such that for every nonzero
$h \in \mathbb{F}_q[T]$, as $X \to \infty$ through the powers of $q$,

$$\#\{f \in \mathbb{F}_q[T] : |f| = X,\ f \text{ and } f + h \text{ are prime}\} =
\frac{\mathfrak{S}_q(h)\, X}{(\log_q X)^2} + O\bigl(X^{1 - \varepsilon}\bigr),$$

where $|f| = |\mathbb{F}_q[T]/(f)|$ is the norm of $f$, the primes of $\mathbb{F}_q[T]$ are its
monic irreducible polynomials, $\mathfrak{S}_q(h)$ is the singular series for twin primes, and
the implied constant may depend on $h$ (but $\varepsilon$ does not).

## Sources

- W. Sawin and M. Shusterman, `On the Chowla and twin primes conjectures over 𝔽_q[T]`, Annals of Math, 196 (2) 2022. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_chowla_and_twin_prime_over_fq_t` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.ChowlaAndTwinPrimeOverFqTWanted.ChowlaAndTwinPrimeOverFqT.theorem_1_1` is written with `theorem_wanted` in [WantedExt/NumberTheory/ChowlaAndTwinPrimeOverFqTWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ChowlaAndTwinPrimeOverFqTWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/twin-primes-and-chowla-s-conjecture-over-functio/index.html#theorem-1-1).

## Monic polynomials of bounded norm

Let $F$ be a finite field and let $X$ be a real number.
This is the set of monic polynomials $f \in F[T]$ whose norm $|f| = |F[T]/(f)|$, the number of
elements of the quotient ring $F[T]/(f)$, satisfies $|f| \le X$.

Formalized by `MathlibExt.NumberTheory.ChowlaAndTwinPrimeOverFqTWanted.ChowlaAndTwinPrimeOverFqT.monicBounded`, a definition declared in [WantedExt/NumberTheory/ChowlaAndTwinPrimeOverFqTWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ChowlaAndTwinPrimeOverFqTWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/twin-primes-and-chowla-s-conjecture-over-functio/index.html#monic-bounded).

## Chowla's conjecture over $\mathbb{F}_q(T)$ for large $q$

Let $p$ be an odd prime, let $k \ge 1$
be a natural number, and let $q$ be a power of $p$ with $q > p^2 k^2 e^2$, where $e$ is Euler's
number; write $\mathbb{F}_q$ for the finite field with $q$ elements. Let
$h_1, \dots, h_k \in \mathbb{F}_q[T]$ be distinct polynomials. Then, as the real number $X$ tends
to $\infty$,

$$\sum_{f \text{ monic},\ |f| \le X} \mu(f + h_1)\,\mu(f + h_2) \cdots \mu(f + h_k) = o(X),$$

where the sum runs over the monic $f \in \mathbb{F}_q[T]$ of norm $|f| = |\mathbb{F}_q[T]/(f)|$ at
most $X$, and $\mu$ is the Möbius function of $\mathbb{F}_q[T]$: $\mu(g) = (-1)^r$ if $g$ is
squarefree with $r$ irreducible factors, and $\mu(g) = 0$ otherwise.

## Sources

- W. Sawin and M. Shusterman, `On the Chowla and twin primes conjectures over 𝔽_q[T]`, Annals of Math, 196 (2) 2022. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_chowla_and_twin_prime_over_fq_t` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.ChowlaAndTwinPrimeOverFqTWanted.ChowlaAndTwinPrimeOverFqT.theorem_1_3` is written with `theorem_wanted` in [WantedExt/NumberTheory/ChowlaAndTwinPrimeOverFqTWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ChowlaAndTwinPrimeOverFqTWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/twin-primes-and-chowla-s-conjecture-over-functio/index.html#theorem-1-3).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Twin primes and Chowla's conjecture over function fields](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/twin-primes-and-chowla-s-conjecture-over-functio/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields/twin-primes-and-chowla-s-conjecture-over-functio)
