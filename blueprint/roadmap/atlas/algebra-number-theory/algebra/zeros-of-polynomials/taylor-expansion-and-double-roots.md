---
declaration: section
origin: cited
lean: Polynomial.existsUnique_taylor_remainder, Polynomial.eval_and_derivative_eval_eq_zero_iff, Polynomial.sq_dvd_iff_eval_and_derivative_eval_eq_zero, Polynomial.not_sq_dvd_of_derivative_eval_ne_zero
statement: formalized
proof: formalized
---

# Taylor expansion and double roots

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/taylor-expansion-and-double-roots/index.html).

## First-order Taylor expansion of a polynomial

Let $R$ be a commutative ring, let
$f \in R[X]$ and $a \in R$, and let $f'$ be the formal derivative of $f$. There is a unique
polynomial $g \in R[X]$ such that

$$f = f(a) + f'(a)\,(X - a) + g\,(X - a)^2.$$

Formalized by `Polynomial.existsUnique_taylor_remainder`, a theorem declared in [MathlibExt/Algebra/Polynomial/Taylor.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/Taylor.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/taylor-expansion-and-double-roots/index.html#exists-unique-taylor-remainder).

## Double root criterion

Let $R$ be a commutative ring, let $f \in R[x]$ and $a \in R$, and
let $f'$ be the formal derivative of $f$. Then $f(a) = 0$ and $f'(a) = 0$ if and only if
$f = (x - a)^2 g$ for some $g \in R[x]$.

## Sources

- ATLAS NumberTheoryI, Corollary 9.13.

Formalized by `Polynomial.eval_and_derivative_eval_eq_zero_iff`, a theorem declared in [MathlibExt/Algebra/Polynomial/DoubleRoot.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/DoubleRoot.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/taylor-expansion-and-double-roots/index.html#eval-and-derivative-eval-eq-zero-iff).

## Double root criterion in divisibility form

Let $R$ be a commutative ring, let
$f \in R[x]$ and $a \in R$, and let $f'$ be the formal derivative of $f$. Then $(x - a)^2$
divides $f$ in $R[x]$ if and only if $f(a) = 0$ and $f'(a) = 0$.

## Sources

- ATLAS NumberTheoryI, Corollary 9.13.

Formalized by `Polynomial.sq_dvd_iff_eval_and_derivative_eval_eq_zero`, a theorem declared in [MathlibExt/Algebra/Polynomial/DoubleRoot.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/DoubleRoot.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/taylor-expansion-and-double-roots/index.html#sq-dvd-iff-eval-and-derivative-eval-eq-z).

## A nonvanishing derivative excludes a double root

Let $R$ be a commutative ring, let
$f \in R[x]$ and $a \in R$, and let $f'$ be the formal derivative of $f$. If $f'(a) \neq 0$,
then $(x - a)^2$ does not divide $f$ in $R[x]$.

No assumption on $f(a)$ is needed.

## Sources

- ATLAS NumberTheoryI, consequence of Corollary 9.13.

Formalized by `Polynomial.not_sq_dvd_of_derivative_eval_ne_zero`, a theorem declared in [MathlibExt/Algebra/Polynomial/DoubleRoot.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/DoubleRoot.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/taylor-expansion-and-double-roots/index.html#not-sq-dvd-of-derivative-eval-ne-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Taylor expansion and double roots](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/taylor-expansion-and-double-roots/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/zeros-of-polynomials/taylor-expansion-and-double-roots)
