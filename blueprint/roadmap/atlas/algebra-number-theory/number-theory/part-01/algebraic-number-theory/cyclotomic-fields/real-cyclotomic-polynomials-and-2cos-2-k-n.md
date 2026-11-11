---
declaration: section
origin: cited
lean: MetaMathlibExt.realCyclotomicPolynomial, MetaMathlibExt.realCyclotomicPolynomial_eq_minpoly_two_cos, MetaMathlibExt.realCyclotomicPolynomial_eq_minpoly_two_cos_of_coprime, MetaMathlibExt.lehmer_cyclotomic_identity, MetaMathlibExt.realCyclotomicPolynomial_eq_minpoly_trace, MetaMathlibExt.finrank_adjoin_two_cos
statement: formalized
---

# Real cyclotomic polynomials and 2cos(2πk/n)

8 results, 6 proved and 2 without a declaration, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/real-cyclotomic-polynomials-and-2cos-2-k-n/index.html).

## Degree of the real cyclotomic polynomial

For `2 < n`, `n.totient` is even and the `natDegree` of the real cyclotomic
polynomial `realCyclotomicPolynomial n` equals `n.totient / 2`. The `Even`
conjunct makes the source's exact half machine-visible under natural-number
division.

## Sources

- Pinthira Tangsupphathawat and Vichian Laohakosol, "Minimal Polynomials of Algebraic Cosine Values at Rational Multiples of π", Journal of Integer Sequences 19 (2016), source lines 83–90: https://cs.uwaterloo.ca/journals/JIS/VOL19/Laohakosol/lao2.tex

The vault records no Lean declaration for it. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/real-cyclotomic-polynomials-and-2cos-2-k-n/index.html#nat-degree-real-cyclotomic-polynomial-2).

## Real cyclotomic polynomial

For a natural number $n$, the real cyclotomic polynomial
$\psi_n \in \mathbb{Z}[X]$ is the minimal polynomial over $\mathbb{Z}$ of the complex number
$\zeta + \zeta^{-1}$, where $\zeta = e^{2\pi i/n}$; for $n \ge 1$ this number is $2\cos(2\pi/n)$.

The definition covers every $n$ (for $n = 0$ the exponent $2\pi i/n$ is read as $0$, so
$\zeta = 1$), but results about $\psi_n$ assume $n > 2$.

## Sources

- Pinthira Tangsupphathawat and Vichian Laohakosol, "Minimal Polynomials of Algebraic Cosine Values at Rational Multiples of π", Journal of Integer Sequences 19 (2016), source lines 83-90: https://cs.uwaterloo.ca/journals/JIS/VOL19/Laohakosol/lao2.tex

Formalized by `MetaMathlibExt.realCyclotomicPolynomial`, a definition declared in [MathlibExt/NumberTheory/Cyclotomic/RealCyclotomicPolynomial.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Cyclotomic/RealCyclotomicPolynomial.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/real-cyclotomic-polynomials-and-2cos-2-k-n/index.html#real-cyclotomic-polynomial).

## Minimal polynomial of $2\cos(2\pi k/n)$ for $k$ coprime to $n$

Let $n$ and $k$ be natural
numbers with $n > 2$ and $\gcd(k, n) = 1$. Then the real cyclotomic polynomial $\psi_n$ equals
the minimal polynomial over $\mathbb{Z}$ of the complex number $2\cos(2\pi k/n)$.

No bound on $k$ is needed, since the cosine depends only on $k$ modulo $n$.

Formalized by `MetaMathlibExt.realCyclotomicPolynomial_eq_minpoly_two_cos`, a theorem declared in [MathlibExt/NumberTheory/Cyclotomic/LehmerCoprimeIndexMinpoly.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Cyclotomic/LehmerCoprimeIndexMinpoly.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/real-cyclotomic-polynomials-and-2cos-2-k-n/index.html#real-cyclotomic-polynomial-eq-minpoly-tw).

## Minimal polynomial of $2\cos(2\pi k/n)$ for $1 \le k \le n$ coprime to $n$

Let $n$ and
$k$ be natural numbers with $n > 2$, $1 \le k \le n$ and $\gcd(k, n) = 1$. Then the real
cyclotomic polynomial $\psi_n$ equals the minimal polynomial over $\mathbb{Z}$ of the complex
number $2\cos(2\pi k/n)$.

The bounds $1 \le k \le n$ are not needed: the same holds for every $k$ coprime to $n$.

## Sources

- Pinthira Tangsupphathawat and Vichian Laohakosol, "Minimal Polynomials of Algebraic Cosine Values at Rational Multiples of π", Journal of Integer Sequences 19 (2016), source lines 83-90: https://cs.uwaterloo.ca/journals/JIS/VOL19/Laohakosol/lao2.tex

Formalized by `MetaMathlibExt.realCyclotomicPolynomial_eq_minpoly_two_cos_of_coprime`, a theorem declared in [MathlibExt/NumberTheory/Cyclotomic/LehmerCoprimeIndexMinpoly.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Cyclotomic/LehmerCoprimeIndexMinpoly.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/real-cyclotomic-polynomials-and-2cos-2-k-n/index.html#real-cyclotomic-polynomial-eq-minpoly-tw-2).

## Real cyclotomic polynomial has degree half the totient

For `2 < n`, `n.totient` is even and the `natDegree` of the real cyclotomic
polynomial `realCyclotomicPolynomial n` equals `n.totient / 2`. The `Even`
conjunct makes the source's exact half machine-visible under natural-number
division.

## Sources

- Pinthira Tangsupphathawat and Vichian Laohakosol, "Minimal Polynomials of Algebraic Cosine Values at Rational Multiples of π", Journal of Integer Sequences 19 (2016), source lines 83–90: https://cs.uwaterloo.ca/journals/JIS/VOL19/Laohakosol/lao2.tex

The vault records no Lean declaration for it. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/real-cyclotomic-polynomials-and-2cos-2-k-n/index.html#nat-degree-real-cyclotomic-polynomial).

## Lehmer's identity for the real cyclotomic polynomial

Let $n > 2$ be a natural number, let
$\psi_n$ be the real cyclotomic polynomial, let $\Phi_n \in \mathbb{Z}[X]$ be the $n$-th
cyclotomic polynomial, and let $\varphi$ be Euler's totient function. Then in the ring
$\mathbb{Z}[x, x^{-1}]$ of Laurent polynomials over $\mathbb{Z}$,
$x^{\varphi(n)/2} \, \psi_n(x + x^{-1}) = \Phi_n(x)$, that is,
$\psi_n(x + x^{-1}) = x^{-\varphi(n)/2} \, \Phi_n(x)$.

## Sources

- Pinthira Tangsupphathawat and Vichian Laohakosol, "Minimal Polynomials of Algebraic Cosine Values at Rational Multiples of π", Journal of Integer Sequences 19 (2016), source lines 83-90: https://cs.uwaterloo.ca/journals/JIS/VOL19/Laohakosol/lao2.tex

Formalized by `MetaMathlibExt.lehmer_cyclotomic_identity`, a theorem declared in [MathlibExt/NumberTheory/Cyclotomic/LehmerLaurentIdentity.lean, line 977](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Cyclotomic/LehmerLaurentIdentity.lean#L977). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/real-cyclotomic-polynomials-and-2cos-2-k-n/index.html#lehmer-cyclotomic-identity).

## The real cyclotomic polynomial is the minimal polynomial of $\zeta + \zeta^{-1}$

Let $K$
be a field of characteristic zero, let $n > 2$ be a natural number, and let $\zeta \in K$ be a
primitive $n$-th root of unity. Then the real cyclotomic polynomial $\psi_n$ equals the minimal
polynomial of $\zeta + \zeta^{-1}$ over $\mathbb{Z}$.

## Sources

- Pinthira Tangsupphathawat and Vichian Laohakosol, "Minimal Polynomials of Algebraic Cosine Values at Rational Multiples of π", Journal of Integer Sequences 19 (2016), source lines 83–90: https://cs.uwaterloo.ca/journals/JIS/VOL19/Laohakosol/lao2.tex

Formalized by `MetaMathlibExt.realCyclotomicPolynomial_eq_minpoly_trace`, a theorem declared in [MathlibExt/NumberTheory/Cyclotomic/LehmerMinpolyTrace.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Cyclotomic/LehmerMinpolyTrace.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/real-cyclotomic-polynomials-and-2cos-2-k-n/index.html#real-cyclotomic-polynomial-eq-minpoly-tr).

## Lehmer's theorem on the degree of 2cos(2πk/n)

Let $n$ and $k$ be natural numbers with
$n > 2$ and $\gcd(k, n) = 1$. Then the $\mathbb{Q}$-subalgebra of $\mathbb{R}$ generated by the
real number $2\cos(2\pi k/n)$ has dimension $\varphi(n)/2$ as a vector space over $\mathbb{Q}$,
where $\varphi$ is Euler's totient function.

Since $n > 2$, $\varphi(n)$ is even, so $\varphi(n)/2$ is an integer. Since this dimension is
finite and positive, $2\cos(2\pi k/n)$ is algebraic over $\mathbb{Q}$ of degree $\varphi(n)/2$.

## Sources

- Pinthira Tangsupphathawat and Vichian Laohakosol, "Minimal Polynomials of Algebraic Cosine Values at Rational Multiples of π," Journal of Integer Sequences 19 (2016), Article 16.2.8, Lehmer's theorem recalled in the Introduction, lines 83–90, https://cs.uwaterloo.ca/journals/JIS/VOL19/Laohakosol/lao2.tex

Formalized by `MetaMathlibExt.finrank_adjoin_two_cos`, a theorem declared in [MathlibExt/NumberTheory/Cyclotomic/TwoCosAlgebraicDegree.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Cyclotomic/TwoCosAlgebraicDegree.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/real-cyclotomic-polynomials-and-2cos-2-k-n/index.html#finrank-adjoin-two-cos).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Real cyclotomic polynomials and 2cos(2πk/n)](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/real-cyclotomic-polynomials-and-2cos-2-k-n/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/real-cyclotomic-polynomials-and-2cos-2-k-n)
