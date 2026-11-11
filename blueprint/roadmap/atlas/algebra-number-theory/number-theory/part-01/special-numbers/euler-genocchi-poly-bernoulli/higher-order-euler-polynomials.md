---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.EulerPolynomialFormulasWanted.eulerPoly, MathlibExt.NumberTheory.EulerPolynomialFormulasWanted.genStirlingPoly, MathlibExt.NumberTheory.EulerPolynomialFormulasWanted.eulerAlpha, MathlibExt.NumberTheory.EulerPolynomialFormulasWanted.eulerNumGenAux, MathlibExt.NumberTheory.EulerPolynomialFormulasWanted.eulerNumGen, MathlibExt.NumberTheory.EulerPolynomialFormulasWanted.eulerPolyGen, MathlibExt.NumberTheory.EulerPolynomialFormulasWanted.eulerPoly_half_eq_sum, MathlibExt.NumberTheory.EulerPolynomialFormulasWanted.eulerPolyGen_recurrence
statement: formalized
---

# Higher-order Euler polynomials

11 results, 6 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/higher-order-euler-polynomials/index.html).

## Euler polynomials

Let $B_m(x)$ denote the $m$-th Bernoulli polynomial. For $n \ge 0$,
the Euler polynomial $E_n(x)$ is the polynomial with rational coefficients
$E_n(x) = \frac{2}{n + 1} \left(B_{n+1}(x) - 2^{n+1} B_{n+1}(x/2)\right)$.

## Sources

- Nouara Mokhtari, Rachid Boumahdi, and Farid Bencherif, "Generalizations of Several Explicit Formulas for Euler Polynomials", Section 1 (Euler polynomials).

Formalized by `MathlibExt.NumberTheory.EulerPolynomialFormulasWanted.eulerPoly`, a definition declared in [WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/higher-order-euler-polynomials/index.html#euler-poly).

## Generalized Stirling polynomial

For natural numbers $n$ and $k$, the generalized
Stirling polynomial $S(n, k, x)$ is the polynomial in $x$ with rational coefficients

$$S(n, k, x) = \frac{1}{k!} \sum_{j=0}^{k} \binom{k}{j} (-1)^{k-j} (x + j)^n.$$

## Sources

- Nouara Mokhtari, Rachid Boumahdi, and Farid Bencherif, "Generalizations of Several Explicit Formulas for Euler Polynomials", Proposition 3.1 (definition).

Formalized by `MathlibExt.NumberTheory.EulerPolynomialFormulasWanted.genStirlingPoly`, a definition declared in [WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/higher-order-euler-polynomials/index.html#gen-stirling-poly).

## Taylor coefficients of (2 + 2z)/(2 + 2z + z²)

The rational numbers $\alpha_k$,
$k \ge 0$, are defined by $\alpha_0 = 1$, $\alpha_1 = 0$ and
$2\alpha_{k+2} + 2\alpha_{k+1} + \alpha_k = 0$ for every $k \ge 0$. They are the Taylor
coefficients of $(2 + 2z)/(2 + 2z + z^2)$ at $z = 0$.

## Sources

- Nouara Mokhtari, Rachid Boumahdi, and Farid Bencherif, "Generalizations of Several Explicit Formulas for Euler Polynomials", Lemma 2.2 (generating function).

Formalized by `MathlibExt.NumberTheory.EulerPolynomialFormulasWanted.eulerAlpha`, a definition declared in [WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/higher-order-euler-polynomials/index.html#euler-alpha).

## Fuel-bounded recurrence for the Euler numbers of order α

Let $E_m(x)$ denote the Euler
polynomial. For a complex number $\alpha$, the complex numbers $a_\alpha(f, n)$, for natural
numbers $f$ (the fuel) and $n$, are defined by $a_\alpha(0, n) = 1$, $a_\alpha(f + 1, 0) = 1$
and $a_\alpha(f + 1, n + 1) = -\alpha \, a_\alpha(f, n) +
\frac{\alpha}{2} \sum_{k=0}^{n} \binom{n}{k} a_\alpha(f, k) \, E_{n-k}(0)$.

Whenever $n \le f$, $a_\alpha(f, n)$ equals the Euler number of order $\alpha$,
$E_n^{(\alpha)}(0)$.

Formalized by `MathlibExt.NumberTheory.EulerPolynomialFormulasWanted.eulerNumGenAux`, a definition declared in [WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/higher-order-euler-polynomials/index.html#euler-num-gen-aux).

## Euler numbers of order α

Let $E_m(x)$ denote the Euler polynomial. For a complex number
$\alpha$, the Euler numbers of order $\alpha$ are the complex numbers $E_n^{(\alpha)}(0)$,
$n \ge 0$, defined by $E_0^{(\alpha)}(0) = 1$ and
$E_{n+1}^{(\alpha)}(0) = -\alpha E_n^{(\alpha)}(0) +
\frac{\alpha}{2} \sum_{k=0}^{n} \binom{n}{k} E_k^{(\alpha)}(0) \, E_{n-k}(0)$ for $n \ge 0$.

This is the coefficient recurrence of the generating function $(2/(e^t + 1))^\alpha$.

## Sources

- Nouara Mokhtari, Rachid Boumahdi, and Farid Bencherif, "Generalizations of Several Explicit Formulas for Euler Polynomials", Section 1 (generalized Euler polynomials).

Formalized by `MathlibExt.NumberTheory.EulerPolynomialFormulasWanted.eulerNumGen`, a definition declared in [WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/higher-order-euler-polynomials/index.html#euler-num-gen).

## Euler polynomials of order α

For a complex number $\alpha$ and $n \ge 0$, let
$E_k^{(\alpha)}(0)$ denote the Euler numbers of order $\alpha$. The Euler polynomial of order
$\alpha$ is the complex polynomial
$E_n^{(\alpha)}(x) = \sum_{k=0}^{n} \binom{n}{k} E_k^{(\alpha)}(0) \, x^{n-k}$.

## Sources

- Nouara Mokhtari, Rachid Boumahdi, and Farid Bencherif, "Generalizations of Several Explicit Formulas for Euler Polynomials", Section 1 (generalized Euler polynomials).

Formalized by `MathlibExt.NumberTheory.EulerPolynomialFormulasWanted.eulerPolyGen`, a definition declared in [WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/higher-order-euler-polynomials/index.html#euler-poly-gen).

## Euler polynomials at (x + 1)/2 via generalized Stirling polynomials

Let $E_n(x)$ denote
the Euler polynomial, $\alpha_k$ the Taylor coefficients of $(2 + 2z)/(2 + 2z + z^2)$, and
$S(n, k, x) = \frac{1}{k!} \sum_{j=0}^{k} \binom{k}{j} (-1)^{k-j} (x + j)^n$ the generalized
Stirling polynomial. For every $n \ge 0$, as polynomials in $x$ with rational coefficients,
$2^n E_n\left(\frac{x + 1}{2}\right) = \sum_{k=0}^{n} k! \, \alpha_k \, S(n, k, x)$.

## Sources

- Nouara Mokhtari, Rachid Boumahdi, and Farid Bencherif, "Generalizations of Several Explicit Formulas for Euler Polynomials", Proposition 3.1.

Stated but not proved: `MathlibExt.NumberTheory.EulerPolynomialFormulasWanted.eulerPoly_half_eq_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/higher-order-euler-polynomials/index.html#euler-poly-half-eq-sum).

## Recurrence for Euler polynomials of order α

Let $E_m(x)$ denote the Euler polynomial
and $E_m^{(\alpha)}(x)$ the Euler polynomial of order $\alpha$. For every complex number
$\alpha$ and every integer $n \ge 1$, as polynomials in $x$,
$E_n^{(\alpha)}(x) = (x - \alpha/2) \, E_{n-1}^{(\alpha)}(x) +
\frac{\alpha}{2} \sum_{k=0}^{n-2} \binom{n-1}{k} (-1)^{n-k} E_{n-1-k}(0) \, E_k^{(\alpha)}(x)$,
where the sum is empty when $n = 1$.

## Sources

- Nouara Mokhtari, Rachid Boumahdi, and Farid Bencherif, "Generalizations of Several Explicit Formulas for Euler Polynomials", Proposition 3.2.

Stated but not proved: `MathlibExt.NumberTheory.EulerPolynomialFormulasWanted.eulerPolyGen_recurrence` is written with `theorem_wanted` in [WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/higher-order-euler-polynomials/index.html#euler-poly-gen-recurrence).

## Euler polynomials as alternating sums of shifted powers

Let $E_n(x)$ denote the Euler
polynomial. For all natural numbers $m \ge 2$ and $n \le 2m + 1$,
$E_n(x) = \sum_{k=0}^{m} \frac{(-1)^k}{2^k} \binom{m+1}{k+1}
\sum_{j=0}^{k} \binom{k}{j} \left(x + j - \frac{k+1}{2}\right)^n$
as polynomials in $x$ with rational coefficients.

## Sources

- Nouara Mokhtari, Rachid Boumahdi, and Farid Bencherif, "Generalizations of Several Explicit Formulas for Euler Polynomials", Theorem 4.1.

Stated but not proved: `MathlibExt.NumberTheory.EulerPolynomialFormulasWanted.eulerPoly_eq_binomial_average` is written with `theorem_wanted` in [WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/higher-order-euler-polynomials/index.html#euler-poly-eq-binomial-average).

## Euler polynomials via generalized Stirling polynomials

Let $E_n(x)$ denote the Euler
polynomial, $\alpha_k$ the Taylor coefficients of $(2 + 2z)/(2 + 2z + z^2)$, and
$S(n, k, x) = \frac{1}{k!} \sum_{j=0}^{k} \binom{k}{j} (-1)^{k-j} (x + j)^n$ the generalized
Stirling polynomial. For every integer $n \ge 1$, as polynomials in $x$ with rational
coefficients, $2^n E_n(x) = \sum_{k=0}^{n} k! \, \alpha_k \, S(n, k, 2x - 1)$.

## Sources

- Nouara Mokhtari, Rachid Boumahdi, and Farid Bencherif, "Generalizations of Several Explicit Formulas for Euler Polynomials", Theorem 4.2.

Stated but not proved: `MathlibExt.NumberTheory.EulerPolynomialFormulasWanted.eulerPoly_eq_sum_genStirling` is written with `theorem_wanted` in [WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/higher-order-euler-polynomials/index.html#euler-poly-eq-sum-gen-stirling).

## Double-sum formula for Euler polynomials

Let $E_n(x)$ denote the Euler polynomial and
$S(n, k, x) = \frac{1}{k!} \sum_{j=0}^{k} \binom{k}{j} (-1)^{k-j} (x + j)^n$ the generalized
Stirling polynomial. For every $n \ge 0$, as polynomials in $x$ with rational coefficients,
$2^n E_n(x) = \sum_{\ell=0}^{n} \frac{(-1)^\ell}{\ell + 1}
\sum_{k=0}^{n-\ell} \frac{(k + \ell + 1)!}{2^k} \binom{\ell + 1}{k} S(n, k + \ell, 2x - 1)$.

## Sources

- Nouara Mokhtari, Rachid Boumahdi, and Farid Bencherif, "Generalizations of Several Explicit Formulas for Euler Polynomials", Theorem 4.3.

Stated but not proved: `MathlibExt.NumberTheory.EulerPolynomialFormulasWanted.eulerPoly_eq_double_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EulerPolynomialFormulasWanted.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/higher-order-euler-polynomials/index.html#euler-poly-eq-double-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Higher-order Euler polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/higher-order-euler-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/higher-order-euler-polynomials)
