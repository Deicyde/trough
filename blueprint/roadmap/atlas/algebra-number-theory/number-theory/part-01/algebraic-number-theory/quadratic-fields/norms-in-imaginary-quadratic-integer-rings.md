---
declaration: section
origin: cited
lean: Zsqrtd.prime_of_natAbs_norm_prime, Zsqrtd.natAbs_norm_dvd_of_dvd, Zsqrtd.eq_zero_of_norm_natAbs_eq_zero, Zsqrtd.dvd_of_coprime_norms, Zsqrtd.prime_pow_norm_of_prime, Zsqrtd.exists_factor_of_coprime, Zsqrtd.card_repr_of_shape, Zsqrtd.card_mul_of_coprime
statement: formalized
proof: formalized
---

# Norms in imaginary quadratic integer rings

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/norms-in-imaginary-quadratic-integer-rings/index.html).

## Elements of $\mathbb{Z}(\sqrt{d})$ of prime norm are prime

Let $d$ be an integer such that
the ring $\mathbb{Z}[\sqrt{d}]$ of formal expressions $a + b\sqrt{d}$ with $a, b \in \mathbb{Z}$
and $\sqrt{d}^2 = d$ is a unique factorization domain, with norm
$N(a + b\sqrt{d}) = a^2 - db^2$. If $\pi \in \mathbb{Z}[\sqrt{d}]$ and $|N(\pi)|$ is a prime
number, then $\pi$ is prime in $\mathbb{Z}[\sqrt{d}]$.

Formalized by `Zsqrtd.prime_of_natAbs_norm_prime`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/norms-in-imaginary-quadratic-integer-rings/index.html#prime-of-nat-abs-norm-prime).

## The norm respects divisibility in $\mathbb{Z}(\sqrt{d})$

Let $d$ be an integer and let
$N(a + b\sqrt{d}) = a^2 - db^2$ be the norm on the ring $\mathbb{Z}[\sqrt{d}]$ of formal
expressions $a + b\sqrt{d}$ with $a, b \in \mathbb{Z}$ and $\sqrt{d}^2 = d$. If $x$ divides $y$ in
$\mathbb{Z}[\sqrt{d}]$, then $|N(x)|$ divides $|N(y)|$.

Formalized by `Zsqrtd.natAbs_norm_dvd_of_dvd`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/norms-in-imaginary-quadratic-integer-rings/index.html#nat-abs-norm-dvd-of-dvd).

## Only zero has norm zero in $\mathbb{Z}(\sqrt d)$ for $d < 0$

Let $d < 0$ be an integer and
let $N(a + b\sqrt d) = a^2 - db^2$ be the norm on the ring $\mathbb{Z}[\sqrt d]$ of elements
$a + b\sqrt d$ ($a, b \in \mathbb{Z}$). If $\alpha \in \mathbb{Z}[\sqrt d]$ satisfies
$|N(\alpha)| = 0$, then $\alpha = 0$.

Formalized by `Zsqrtd.eq_zero_of_norm_natAbs_eq_zero`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/norms-in-imaginary-quadratic-integer-rings/index.html#eq-zero-of-norm-nat-abs-eq-zero).

## Cancelling a factor of coprime norm

Let $d < 0$ be an integer such that the ring
$\mathbb{Z}[\sqrt d]$ of elements $a + b\sqrt d$ ($a, b \in \mathbb{Z}$) is a unique factorization
domain, and let $N(a + b\sqrt d) = a^2 - db^2$ be the norm. Let $u$ and $v$ be coprime natural
numbers with $u \ne 0$. If $\beta, \beta_0, \gamma \in \mathbb{Z}[\sqrt d]$ satisfy
$|N(\beta)| \mid u$, $|N(\gamma)| = v$ and $\beta \mid \beta_0\gamma$, then $\beta \mid \beta_0$.

Formalized by `Zsqrtd.dvd_of_coprime_norms`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/norms-in-imaginary-quadratic-integer-rings/index.html#dvd-of-coprime-norms).

## Primes of $\mathbb{Z}(\sqrt{d})$ have prime-power norm

Let $d < 0$ be an integer and let
$N(a + b\sqrt{d}) = a^2 - db^2$ be the norm on the ring $\mathbb{Z}[\sqrt{d}]$ of numbers
$a + b\sqrt{d}$ with $a, b \in \mathbb{Z}$. For every prime $\varpi$ of $\mathbb{Z}[\sqrt{d}]$
there are a prime number $\ell$ and a natural number $s \ne 0$ such that $|N(\varpi)| = \ell^s$
and $\varpi$ divides $\ell$ in $\mathbb{Z}[\sqrt{d}]$.

Formalized by `Zsqrtd.prime_pow_norm_of_prime`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/norms-in-imaginary-quadratic-integer-rings/index.html#prime-pow-norm-of-prime).

## Splitting an element along coprime norms

Let $d < 0$ be an integer such that the ring
$\mathbb{Z}[\sqrt d]$ of elements $a + b\sqrt d$ ($a, b \in \mathbb{Z}$) is a unique factorization
domain, and let $N(a + b\sqrt d) = a^2 - db^2$ be the norm. Let $u$ and $v$ be coprime nonzero
natural numbers. Every $\alpha \in \mathbb{Z}[\sqrt d]$ with $|N(\alpha)| = uv$ factors as
$\alpha = \beta\gamma$ with $|N(\beta)| = u$ and $|N(\gamma)| = v$.

Formalized by `Zsqrtd.exists_factor_of_coprime`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/norms-in-imaginary-quadratic-integer-rings/index.html#exists-factor-of-coprime).

## Counting a norm class generated by one element

Let $d$ be an integer such that the ring
$\mathbb{Z}[\sqrt d]$ of formal sums $a + b\sqrt d$ ($a, b \in \mathbb{Z}$) is an integral domain
with exactly $k$ units, and let $N(a + b\sqrt d) = a^2 - db^2$ be the norm. Assume that for each
$m \in \mathbb{N}$ the set of $\alpha \in \mathbb{Z}[\sqrt d]$ with $|N(\alpha)| = m$ is finite. Let
$n \in \mathbb{N}$ and let $s \ne 0$ satisfy $|N(s)| = n$. If every $\alpha$ with $|N(\alpha)| = n$
equals $us$ for some unit $u$, then exactly $k$ elements $\alpha$ satisfy $|N(\alpha)| = n$.

Formalized by `Zsqrtd.card_repr_of_shape`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/norms-in-imaginary-quadratic-integer-rings/index.html#card-repr-of-shape).

## Norm counts are multiplicative up to units

Let $d < 0$ be an integer such that the ring
$\mathbb{Z}[\sqrt d]$ of elements $a + b\sqrt d$ ($a, b \in \mathbb{Z}$) is a unique factorization
domain with exactly $k$ units, and let $N(a + b\sqrt d) = a^2 - db^2$ be the norm. Assume that for
each $n \in \mathbb{N}$ the set of $\alpha \in \mathbb{Z}[\sqrt d]$ with $|N(\alpha)| = n$ is
finite, and let $r(n)$ be its size. If $u$ and $v$ are coprime nonzero natural numbers, then
$r(u)\,r(v) = k\,r(uv)$.

Formalized by `Zsqrtd.card_mul_of_coprime`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean, line 411](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean#L411). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/norms-in-imaginary-quadratic-integer-rings/index.html#card-mul-of-coprime).

## The norm of a power in $\mathbb{Z}(\sqrt{d})$

Let $d$ be an integer and let
$N(a + b\sqrt{d}) = a^2 - db^2$ be the norm on the ring $\mathbb{Z}[\sqrt{d}]$ of formal
expressions $a + b\sqrt{d}$ with $a, b \in \mathbb{Z}$ and $\sqrt{d}^2 = d$. Then
$N(x^n) = N(x)^n$ for every $x \in \mathbb{Z}[\sqrt{d}]$ and every natural number $n$.

Formalized by `Zsqrtd.norm_pow`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean, line 536](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean#L536). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/norms-in-imaginary-quadratic-integer-rings/index.html#norm-pow).

## Elements whose norm is a power of a ramified two

Let $d < 0$ be an integer such that the
ring $\mathbb{Z}[\sqrt d]$ of elements $a + b\sqrt d$ ($a, b \in \mathbb{Z}$) is a unique
factorization domain, and let $N(a + b\sqrt d) = a^2 - db^2$ be the norm. Suppose
$2 = \varepsilon\rho^2$ for a unit $\varepsilon$ and a prime $\rho$ with $|N(\rho)| = 2$. Then for
every $e \in \mathbb{N}$, every $\alpha$ with $|N(\alpha)| = 2^e$ equals $u\rho^e$ for some unit
$u$.

Formalized by `Zsqrtd.exists_unit_mul_pow_of_norm_two_pow`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean, line 541](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean#L541). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/norms-in-imaginary-quadratic-integer-rings/index.html#exists-unit-mul-pow-of-norm-two-pow).

## Norm counts at powers of a ramified two

Let $d < 0$ be an integer such that the ring
$\mathbb{Z}[\sqrt d]$ of elements $a + b\sqrt d$ ($a, b \in \mathbb{Z}$) is a unique factorization
domain with exactly $k$ units, and let $N(a + b\sqrt d) = a^2 - db^2$ be the norm. Assume that for
each $n \in \mathbb{N}$ the set of $\alpha \in \mathbb{Z}[\sqrt d]$ with $|N(\alpha)| = n$ is
finite, and let $r(n)$ be its size. If $2 = \varepsilon\rho^2$ for a unit $\varepsilon$ and a
prime $\rho$ with $|N(\rho)| = 2$, then $r(2^e) = k$ for every $e \in \mathbb{N}$.

Formalized by `Zsqrtd.card_norm_two_pow`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean, line 621](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean#L621). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/norms-in-imaginary-quadratic-integer-rings/index.html#card-norm-two-pow).

## Peeling an inert prime off an element of norm $q^f$

Let $d < 0$ be an integer such that
the ring $\mathbb{Z}[\sqrt{d}]$ of numbers $a + b\sqrt{d}$ with $a, b \in \mathbb{Z}$ is a unique
factorization domain, with norm $N(a + b\sqrt{d}) = a^2 - db^2$. Let $q$ be a natural number
that is prime in $\mathbb{Z}[\sqrt{d}]$, let $f$ be a natural number, and let
$\alpha \in \mathbb{Z}[\sqrt{d}]$ be nonzero and not a unit with $|N(\alpha)| = q^f$. Then
$\alpha = wq\beta$ for some unit $w$ and some $\beta \in \mathbb{Z}[\sqrt{d}]$ with
$q^2 \cdot |N(\beta)| = q^f$.

Formalized by `Zsqrtd.inert_peel`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean, line 633](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean#L633). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/norms-in-imaginary-quadratic-integer-rings/index.html#inert-peel).

## Elements of norm $q^{2n}$ over an inert prime

Let $d < 0$ be an integer such that the
ring $\mathbb{Z}[\sqrt{d}]$ of numbers $a + b\sqrt{d}$ with $a, b \in \mathbb{Z}$ is a unique
factorization domain, with norm $N(a + b\sqrt{d}) = a^2 - db^2$. Let $q$ be a prime number that
is also prime in $\mathbb{Z}[\sqrt{d}]$. Then for every natural number $n$, every
$\alpha \in \mathbb{Z}[\sqrt{d}]$ with $|N(\alpha)| = q^{2n}$ is of the form $\alpha = uq^n$ for
some unit $u$.

Formalized by `Zsqrtd.inert_even`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean, line 683](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean#L683). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/norms-in-imaginary-quadratic-integer-rings/index.html#inert-even).

## No element has norm $q^{2n+1}$ over an inert prime

Let $d < 0$ be an integer such that
the ring $\mathbb{Z}[\sqrt{d}]$ of numbers $a + b\sqrt{d}$ with $a, b \in \mathbb{Z}$ is a unique
factorization domain, with norm $N(a + b\sqrt{d}) = a^2 - db^2$. Let $q$ be a prime number that
is also prime in $\mathbb{Z}[\sqrt{d}]$. Then for every natural number $n$, no
$\alpha \in \mathbb{Z}[\sqrt{d}]$ satisfies $|N(\alpha)| = q^{2n+1}$.

Formalized by `Zsqrtd.inert_odd`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean, line 725](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean#L725). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/norms-in-imaginary-quadratic-integer-rings/index.html#inert-odd).

## Norm counts at an inert prime

Let $d < 0$ be an integer such that the ring
$\mathbb{Z}[\sqrt d]$ of elements $a + b\sqrt d$ ($a, b \in \mathbb{Z}$) is a unique factorization
domain with exactly $k$ units, and let $N(a + b\sqrt d) = a^2 - db^2$ be the norm. Assume that for
each $n \in \mathbb{N}$ the set of $\alpha \in \mathbb{Z}[\sqrt d]$ with $|N(\alpha)| = n$ is
finite, and let $r(n)$ be its size. If $q$ is a prime number that is also a prime element of
$\mathbb{Z}[\sqrt d]$, then for every $f \in \mathbb{N}$ we have $r(q^f) = k$ when $f$ is even and
$r(q^f) = 0$ when $f$ is odd.

Formalized by `Zsqrtd.card_norm_inert_pow`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean, line 772](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean#L772). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/norms-in-imaginary-quadratic-integer-rings/index.html#card-norm-inert-pow).

## Elements of norm $p^e$ over a split prime

Let $d < 0$ be an integer such that the ring
$\mathbb{Z}[\sqrt{d}]$ of numbers $a + b\sqrt{d}$ with $a, b \in \mathbb{Z}$ is a unique
factorization domain, with norm $N(a + b\sqrt{d}) = a^2 - db^2$ and conjugation
$\overline{a + b\sqrt{d}} = a - b\sqrt{d}$. Let $p$ be a prime number and let $\pi$ be a prime of
$\mathbb{Z}[\sqrt{d}]$ with $N(\pi) = p$ and $p = \pi\bar{\pi}$ such that $\bar{\pi}$ is also
prime. Then for every natural number $e$, every $\alpha \in \mathbb{Z}[\sqrt{d}]$ with
$|N(\alpha)| = p^e$ is of the form $\alpha = u\pi^j\bar{\pi}^k$ for some unit $u$ and natural
numbers $j, k$ with $j + k = e$.

Formalized by `Zsqrtd.exists_unit_mul_split_pow`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean, line 815](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean#L815). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/norms-in-imaginary-quadratic-integer-rings/index.html#exists-unit-mul-split-pow).

## Norm counts at a split prime

Let $d < 0$ be an integer such that the ring
$\mathbb{Z}[\sqrt d]$ of elements $a + b\sqrt d$ ($a, b \in \mathbb{Z}$) is a unique factorization
domain with exactly $k$ units, and let $N(a + b\sqrt d) = a^2 - db^2$ be the norm. Assume that for
each $n \in \mathbb{N}$ the set of $\alpha \in \mathbb{Z}[\sqrt d]$ with $|N(\alpha)| = n$ is
finite, and let $r(n)$ be its size. Let $p$ be a prime number and $\pi \in \mathbb{Z}[\sqrt d]$
with $N(\pi) = p$ and $p = \pi\bar\pi$, where $\overline{a + b\sqrt d} = a - b\sqrt d$. If $\pi$
and $\bar\pi$ are prime and $\bar\pi$ is not associated to $\pi$, then $r(p^e) = k(e + 1)$ for
every $e \in \mathbb{N}$.

Formalized by `Zsqrtd.card_norm_split_pow`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean, line 920](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean#L920). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/norms-in-imaginary-quadratic-integer-rings/index.html#card-norm-split-pow).

## Norm counts determined by prime powers

Let $d < 0$ be an integer such that the ring
$\mathbb{Z}[\sqrt d]$ of elements $a + b\sqrt d$ ($a, b \in \mathbb{Z}$) is a unique factorization
domain with exactly $k$ units, and let $N(a + b\sqrt d) = a^2 - db^2$ be the norm. Assume that for
each $n \in \mathbb{N}$ the set of $\alpha \in \mathbb{Z}[\sqrt d]$ with $|N(\alpha)| = n$ is
finite, and let $r(n)$ be its size. Let $D : \mathbb{N} \to \mathbb{Z}$ satisfy $D(1) = 1$ and
$D(mn) = D(m)\,D(n)$ for all coprime $m, n$. If $r(p^e) = k\,D(p^e)$ for every prime $p$ and every
$e \ge 1$, then $r(n) = k\,D(n)$ for every $n \ne 0$.

Formalized by `Zsqrtd.card_norm_eq_mul_of_prime_pow`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean, line 1066](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ZsqrtdNormFactorization.lean#L1066). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/norms-in-imaginary-quadratic-integer-rings/index.html#card-norm-eq-mul-of-prime-pow).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Norms in imaginary quadratic integer rings](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/norms-in-imaginary-quadratic-integer-rings/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/norms-in-imaginary-quadratic-integer-rings)
