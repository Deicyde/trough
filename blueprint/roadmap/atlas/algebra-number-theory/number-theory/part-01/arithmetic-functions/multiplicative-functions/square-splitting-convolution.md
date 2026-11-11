---
declaration: section
origin: cited
lean: MetaMathlibExt.squareSplitU, MetaMathlibExt.squareSplitV, MetaMathlibExt.squareSplitU_one, MetaMathlibExt.squareSplitV_one, MetaMathlibExt.squareSplitU_mul_squareSplitV_sq, MetaMathlibExt.squareSplitDivisors, MetaMathlibExt.squareSplitDivisors_one, MetaMathlibExt.squareSplitConv
statement: formalized
---

# Square-splitting convolution

23 results, 9 proved and 14 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html).

## Squarefree part

For a natural number $n \ge 1$ with prime factorization
$n = \prod_p p^{e_p}$, its squarefree part is $u(n) = \prod_p p^{e_p \bmod 2}$, the product of the
primes dividing $n$ to an odd power. By convention $u(0) = 1$.

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Section 2 (`n = u(n) v(n)²`, Theorems 2 and 3).

Formalized by `MetaMathlibExt.squareSplitU`, a definition declared in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-u).

## The square-root part of a natural number

For $n \ge 1$ with prime factorization
$n = \prod_p p^{e_p}$, the square-root part of $n$ is $v(n) = \prod_p p^{\lfloor e_p/2 \rfloor}$;
by convention $v(0) = 1$. For $n \ge 1$, $v(n)^2$ is the largest square dividing $n$, and
$n = u(n)\, v(n)^2$ where $u(n) = n / v(n)^2$ is squarefree.

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Section 2.

Formalized by `MetaMathlibExt.squareSplitV`, a definition declared in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-v).

## Squarefree part of one

We have $u(1) = 1$, where $u(n)$ is the product of the primes
dividing $n$ to an odd power.

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Section 2.

Formalized by `MetaMathlibExt.squareSplitU_one`, a theorem declared in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-u-one).

## The square-root part of $1$ is $1$

We have $v(1) = 1$, where for $n \ge 1$ the
square-root part $v(n)$ is the product of $p^{\lfloor e/2 \rfloor}$ over the prime powers $p^e$
exactly dividing $n$.

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Section 2.

Formalized by `MetaMathlibExt.squareSplitV_one`, a theorem declared in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-v-one).

## Square-splitting decomposition

For every natural number $n \ne 0$ with prime
factorization $n = \prod_p p^{e_p}$, we have $n = u(n)\,v(n)^2$, where
$u(n) = \prod_p p^{e_p \bmod 2}$ and $v(n) = \prod_p p^{\lfloor e_p/2 \rfloor}$.

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Section 2.

Formalized by `MetaMathlibExt.squareSplitU_mul_squareSplitV_sq`, a theorem declared in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-u-mul-square-split-v-sq).

## Square-splitting divisors

For a natural number $n \ge 1$ with prime factorization
$n = \prod_p p^{e_p}$, let $u(n) = \prod_p p^{e_p \bmod 2}$ and
$v(n) = \prod_p p^{\lfloor e_p/2 \rfloor}$, and let $u(0) = v(0) = 1$. The set of
square-splitting divisors of $n$ is $A(n) = \{u_1 v_1^2 : u_1 \mid u(n),\ v_1 \mid v(n)\}$, where
$u_1$ and $v_1$ range over the positive divisors of $u(n)$ and $v(n)$.

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Theorem 1.

Formalized by `MetaMathlibExt.squareSplitDivisors`, a definition declared in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-divisors).

## The square-splitting divisor set of $1$

Let
$A(n) = \{u_1 v_1^2 : u_1 \mid u(n),\ v_1 \mid v(n)\}$ be the square-splitting divisor set of
$n \ge 1$, where $u(n)$ is the squarefree part of $n$ and $v(n)$ is the positive integer with
$n = u(n) v(n)^2$. Then $A(1) = \{1\}$.

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Theorem 1.

Formalized by `MetaMathlibExt.squareSplitDivisors_one`, a theorem declared in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-divisors-one).

## Square-splitting convolution

For complex arithmetic functions $f$ and $g$, the
square-splitting $A$-convolution of Narkiewicz type is the arithmetic function $f \star g$ given by
$(f \star g)(n) = \sum_{d \in A(n)} f(d)\, g(n/d)$ for $n \ge 1$ and $(f \star g)(0) = 0$. Here
$A(n) = \{u_1 v_1^2 : u_1 \mid u(n),\ v_1 \mid v(n)\}$ is the square-splitting divisor set of $n$,
where $u(n)$ is the squarefree part of $n$ and $n = u(n) v(n)^2$.

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Section 2 and Theorem 4 (`F = 1 ⋆ f` means `F(n) = ∑_{d ∈ A(n)} f(d)`).

Formalized by `MetaMathlibExt.squareSplitConv`, a definition declared in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-conv).

## Value of the square-splitting convolution at a positive integer

For complex arithmetic
functions $f$ and $g$ and every natural number $n \ne 0$, the square-splitting convolution of $f$
and $g$ takes the value $(f \star g)(n) = \sum_{d \in A(n)} f(d)\, g(n/d)$ at $n$, where $A(n)$ is
the square-splitting divisor set of $n$.

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Section 2.

Formalized by `MetaMathlibExt.squareSplitConv_apply`, a theorem declared in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-conv-apply).

## The square-splitting convolution preserves multiplicativity

If $f$ and $g$ are
multiplicative complex arithmetic functions, then their square-splitting convolution $f \star g$
is multiplicative. Here an arithmetic function $h$ is multiplicative when $h(1) = 1$ and
$h(mn) = h(m)\, h(n)$ for all coprime $m$ and $n$.

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Corollary 1.

Stated but not proved: `MetaMathlibExt.squareSplitConv_isMultiplicative` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-conv-is-multiplicative).

## Basic properties of the square-splitting divisor sets

Let
$A(n) = \{u_1 v_1^2 : u_1 \mid u(n),\ v_1 \mid v(n)\}$ be the square-splitting divisor set of
$n$, where $u(n)$ is the squarefree part of $n$ and $n = u(n) v(n)^2$ for $n \ge 1$. Then
(i) for every $n \ge 1$, both $1$ and $n$ belong to $A(n)$, and every element of $A(n)$ divides
$n$; (ii) for all coprime natural numbers $m$ and $n$, $A(mn) = \{ab : a \in A(m),\ b \in A(n)\}$;
and (iii) for every $n \ge 1$, $|A(n)| = d(u(n))\, d(v(n))$ and $|A(n)| = 2^{\omega(u(n))} d(v(n))$,
where $d(k)$ is the number of divisors of $k$ and $\omega(k)$ is the number of distinct prime
factors of $k$.

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Theorem 1.

Stated but not proved: `MetaMathlibExt.squareSplitDivisors_properties` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-divisors-properties).

## Ring axioms for the square-splitting convolution

For all complex arithmetic functions
$f$, $g$ and $h$, the square-splitting convolution $\star$ satisfies $f \star g = g \star f$,
$(f \star g) \star h = f \star (g \star h)$, $f \star (g + h) = f \star g + f \star h$ and
$\varepsilon \star f = f$, where $\varepsilon$ is the arithmetic function with $\varepsilon(1) = 1$
and $\varepsilon(n) = 0$ for $n \ne 1$.

With pointwise addition, these identities make the complex arithmetic functions a commutative ring
under $\star$ with identity $\varepsilon$.

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Theorem 2.

Stated but not proved: `MetaMathlibExt.squareSplitConv_commRing_axioms` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-conv-comm-ring-axioms).

## Square-splitting convolution as a bivariate Dirichlet convolution

Let $\star$ be the
square-splitting convolution. For all complex arithmetic functions $f$ and $g$, every squarefree
natural number $u$ and every natural number $v \ge 1$,

$$(f \star g)(u v^2) = \sum_{u_1 \mid u} \sum_{v_1 \mid v} f(u_1 v_1^2)\, g((u/u_1)(v/v_1)^2).$$

Moreover, for every function $F : \mathbb{N} \times \mathbb{N} \to \mathbb{C}$ there is exactly
one complex arithmetic function $f$ with $f(u v^2) = F(u, v)$ for every squarefree $u$ and every
$v \ge 1$.

Thus $f \mapsto \big((u, v) \mapsto f(u v^2)\big)$ is a bijection from complex arithmetic functions
onto functions on $\{(u, v) : u \text{ squarefree},\ v \ge 1\}$, and it turns $\star$ into the
bivariate Dirichlet convolution
$(\Phi \odot \Psi)(u, v) = \sum_{u_1 \mid u} \sum_{v_1 \mid v} \Phi(u_1, v_1)\, \Psi(u/u_1, v/v_1)$.

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Theorem 2.

Stated but not proved: `MetaMathlibExt.squareSplitConv_bivariate_iso` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-conv-bivariate-iso).

## Möbius function of the square-splitting convolution

Let $\star$ be the square-splitting
convolution, $\mathbf{1}$ the constant function $1$ on the positive integers, $\varepsilon$ the
identity element ($\varepsilon(1) = 1$ and $\varepsilon(n) = 0$ for $n \ne 1$), and let $\mu_\star$
be any complex-valued arithmetic function with $\mathbf{1} \star \mu_\star = \varepsilon$. Then
$\mu_\star(n) = \mu(u(n))\,\mu(v(n))$ for every $n \ge 1$, where $\mu$ is the Möbius function,
$u(n)$ is the product of the primes dividing $n$ to an odd power and $v(n)$ is the positive
integer with $n = u(n)\,v(n)^2$. For every prime $p$, $\mu_\star(p) = \mu_\star(p^2) = -1$,
$\mu_\star(p^3) = 1$ and $\mu_\star(p^k) = 0$ for every $k \ge 4$. For every complex $s$ with
$\operatorname{Re} s > 1$,

$$\sum_{n \ge 1} \frac{\mu_\star(n)}{n^s} = \prod_p \left(1 - p^{-s} - p^{-2s} + p^{-3s}\right)
= \frac{1}{\zeta(s)\,\zeta(2s)}.$$

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Theorem 3.

Stated but not proved: `MetaMathlibExt.squareSplitMoebius_formula` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-moebius-formula).

## Möbius inversion for the square-splitting convolution

Let $\star$ be the
square-splitting convolution, $\mathbf{1}$ the constant function $1$ on the positive integers,
$\varepsilon$ the identity element ($\varepsilon(1) = 1$ and $\varepsilon(n) = 0$ for $n \ne 1$),
and let $\mu_\star$ be any complex-valued arithmetic function with
$\mathbf{1} \star \mu_\star = \varepsilon$. Then for all complex-valued arithmetic functions $f$
and $F$, $F = \mathbf{1} \star f$ if and only if $f = \mu_\star \star F$; that is,
$F(n) = \sum_{d \in A(n)} f(d)$ for every $n \ge 1$ if and only if
$f(n) = \sum_{d \in A(n)} \mu_\star(d)\,F(n/d)$ for every $n \ge 1$, where $A(n)$ is the set of
square-splitting divisors of $n$.

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Theorem 4.

Stated but not proved: `MetaMathlibExt.squareSplit_moebius_inversion` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-moebius-inversion).

## Inverse of a multiplicative function under the square-splitting convolution

Let $f$ be a
multiplicative complex arithmetic function (an arithmetic function $h$ is multiplicative when
$h(1) = 1$ and $h(mn) = h(m)\, h(n)$ for coprime $m$ and $n$), let $\star$ be the square-splitting
convolution, and let $\varepsilon$ be the arithmetic function with $\varepsilon(1) = 1$ and
$\varepsilon(n) = 0$ for $n \ne 1$. Then there is a complex arithmetic function $g$ with
$f \star g = \varepsilon$ such that every complex arithmetic function $g'$ with
$f \star g' = \varepsilon$ equals $g$. Moreover, $g$ is multiplicative; for every prime $p$ and
every $k \ge 1$, $\sum_{j=0}^{\lfloor k/2 \rfloor} f(p^{2j})\, g(p^{k-2j}) = 0$ if $k$ is even and
$\sum_{j=0}^{\lfloor k/2 \rfloor} (f(p^{2j}) g(p^{k-2j}) + f(p^{2j+1}) g(p^{k-2j-1})) = 0$ if $k$ is
odd; $g(1) = 1/f(1)$; and for every prime $p$, $g(p) = -f(p)/f(1)^2$,
$g(p^2) = -f(p^2)/f(1)^2$ and $g(p^3) = \big(2 f(p) f(p^2) - f(p^3) f(1)\big)/f(1)^3$.

Multiplicativity includes $f(1) = 1$, so the source's hypothesis $f(1) \ne 0$ holds automatically.

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Theorem 5.

Stated but not proved: `MetaMathlibExt.squareSplitConv_inverse_of_isMultiplicative` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-conv-inverse-of-is-multipli).

## The square-splitting totient function

Let $A(n)$ be the set of square-splitting divisors
of $n$, and let $\varphi_\star$ be any integer-valued arithmetic function with
$\sum_{d \in A(n)} \varphi_\star(d) = n$ for every $n \ge 1$. Then $\varphi_\star$ is
multiplicative and $\varphi_\star(1) = 1$. For every prime $p$, $\varphi_\star(p) = p - 1$, and
for every $b \ge 1$, $\varphi_\star(p^{2b}) = (p^2 - 1)\,p^{2b-2}$ and
$\varphi_\star(p^{2b+1}) = (p - 1)(p^2 - 1)\,p^{2b-2}$. Moreover, for every $n \ge 1$,

$$\varphi_\star(n) = \varphi(u(n))\,v(n)^2 \prod_{p \mid v(n)} \left(1 - \frac{1}{p^2}\right),$$

where $\varphi$ is Euler's totient function, $u(n)$ is the product of the primes dividing $n$ to
an odd power and $v(n)$ is the positive integer with $n = u(n)\,v(n)^2$.

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Theorem 7.

Stated but not proved: `MetaMathlibExt.squareSplitTotient_formula` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-totient-formula).

## Average order of the square-splitting totient function

Let $A(n)$ be the set of
square-splitting divisors of $n$, and let $\varphi_\star$ be any integer-valued arithmetic function
with $\sum_{d \in A(n)} \varphi_\star(d) = n$ for every $n \ge 1$. Then the product
$M = \prod_p \left(1 - \frac{1}{p^2} + \frac{(p-1)^2}{p^5}\right)$ converges absolutely, that is,
$\sum_p \left|\frac{(p-1)^2}{p^5} - \frac{1}{p^2}\right| < \infty$, and for every
$0 < \varepsilon < 1/2$,

$$\sum_{1 \le n \le x} \varphi_\star(n) = \frac{M}{2}\,x^2 + O(x^{1+\varepsilon})
\quad (x \to \infty).$$

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Theorem 8.

Stated but not proved: `MetaMathlibExt.squareSplitTotient_sum_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-totient-sum-asymptotic).

## Dirichlet series of the square-splitting divisor function

Let $\tau^\star(n) = |A(n)|$ be
the number of elements of the square-splitting divisor set $A(n)$, and let
$H(s) = \prod_p (1 - 3p^{-2s} + 2p^{-3s})$, where $p$ runs over the primes. For every complex
number $s$ with $\operatorname{Re} s > 1$, the series $\sum_{k \ge 0} \tau^\star(p^k) p^{-ks}$
converges to $(1 + 2p^{-s})/(1 - p^{-2s})^2$ for each prime $p$, and the Dirichlet series
$\sum_{n \ge 1} \tau^\star(n) n^{-s}$ equals both $\prod_p (1 + 2p^{-s})/(1 - p^{-2s})^2$ and
$\zeta(s)^2 \zeta(2s)^2 H(s)$. Moreover, for every $s$ with $\operatorname{Re} s > 1/2$ the series
$\sum_p |-3p^{-2s} + 2p^{-3s}|$ converges (so the product defining $H(s)$ converges absolutely),
$H$ is holomorphic on the half-plane $\operatorname{Re} s > 1/2$, and $H(1) \ne 0$.

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Theorem 9.

Stated but not proved: `MetaMathlibExt.squareSplitDivisorCount_LSeries` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-divisor-count-lseries).

## Partial-sum asymptotics for a Riemann zeta quotient times a Dirichlet series

Let
$f, g : \mathbb{N} \to \mathbb{C}$ and let $\sigma_0 < 1/2$ be a real number. Suppose that the
Dirichlet series $G(s) = \sum_{n \ge 1} g(n) n^{-s}$ converges absolutely for
$\operatorname{Re} s > \sigma_0$, that $G(1) \ne 0$, and that for every complex $s$ with
$\operatorname{Re} s > 1$ the Dirichlet series $F(s) = \sum_{n \ge 1} f(n) n^{-s}$ converges
absolutely and $F(s) = \zeta(s)^2 G(s) / \zeta(2s)$, where $\zeta$ is the Riemann zeta
function. Then, as the real number $x$ tends to infinity,

$$
\sum_{1 \le n \le x} f(n) = \frac{G(1)}{\zeta(2)}\, x \log x +
\frac{G(1)}{\zeta(2)} \left(2\gamma - 1 + \frac{G'(1)}{G(1)} -
\frac{2\zeta'(2)}{\zeta(2)}\right) x + O\big(x^{1/2} (\log x)^3\big),
$$

where $\gamma$ is the Euler–Mascheroni constant and $G'$, $\zeta'$ are complex derivatives.

The hypothesis $G(1) \ne 0$ is added so that the quotient $G'(1)/G(1)$ is meaningful.

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Lemma 1.

Stated but not proved: `MetaMathlibExt.sum_asymptotic_of_LSeries_eq_zeta_sq_div_zeta_two_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#sum-asymptotic-of-lseries-eq-zeta-sq-div).

## Average order of the square-splitting divisor function

Let $\tau^\star(n) = |A(n)|$ be
the number of elements of the square-splitting divisor set $A(n)$, let $\gamma$ be the
Euler–Mascheroni constant, and let $A_\tau = \prod_p (1 - 1/(p+1)^2)$ and
$B_\tau = 6 \sum_p \log p / ((p-1)(p+1)(p+2))$, where $p$ runs over the primes. Then, as the real
number $x$ tends to infinity,
$\sum_{1 \le n \le x} \tau^\star(n) - A_\tau x \log x - A_\tau (2\gamma - 1 - B_\tau - c) x$ is
$O(x^{1/2} (\log x)^3)$, where $c = 2\zeta'(2)/\zeta(2)$.

These constants are the ones forced by the Dirichlet series of $\tau^\star$: with
$H(s) = \prod_p (1 - 3p^{-2s} + 2p^{-3s})$, one has $A_\tau = \zeta(2)^2 H(1)$ and
$-B_\tau - 2\zeta'(2)/\zeta(2) = 4\zeta'(2)/\zeta(2) + H'(1)/H(1)$.

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Theorem 10.

Stated but not proved: `MetaMathlibExt.squareSplitDivisorCount_sum_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-divisor-count-sum-asymptoti).

## Support and density of the square-splitting Möbius function

Let $\star$ be the
square-splitting convolution, $\mathbf{1}$ the constant function $1$ on the positive integers,
$\varepsilon$ the identity element ($\varepsilon(1) = 1$ and $\varepsilon(n) = 0$ for $n \ne 1$),
and let $\mu_\star$ be any complex-valued arithmetic function with
$\mathbf{1} \star \mu_\star = \varepsilon$. Then for every $n \ge 1$, $\mu_\star(n) \ne 0$ if and
only if every prime exponent of $n$ is at most $3$. The proportion of the integers
$1 \le n \le N$ with $\mu_\star(n) \ne 0$ tends to $\prod_p (1 - p^{-4})$ as $N \to \infty$, and
$\prod_p (1 - p^{-4}) = 1/\zeta(4)$. Finally,
$\sum_{1 \le n \le x} |\mu_\star(n)|^2 \sim x/\zeta(4)$ as $x \to \infty$.

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Theorem 11.

Stated but not proved: `MetaMathlibExt.squareSplitMoebius_support_density` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-moebius-support-density).

## A square-splitting divisor function and its Euler product

Let
$\alpha \in \mathbb{C}$, let $\sigma_\beta(m) = \sum_{d \mid m} d^\beta$ for $\beta \in \mathbb{C}$
(complex powers), and let $f(n) = \sigma_\alpha(u(n))\,\sigma_{2\alpha}(v(n))$, where $u(n)$ is
the product of the primes dividing $n$ to an odd power and $v(n)$ is the positive integer with
$n = u(n)\,v(n)^2$. Then $f(1) = 1$ and $f(mn) = f(m)\,f(n)$ for all coprime $m$ and $n$. For
every prime $p$ and every $b \ge 0$, $f(p^{2b}) = \sum_{j=0}^{b} p^{2j\alpha}$ and
$f(p^{2b+1}) = (1 + p^\alpha) \sum_{j=0}^{b} p^{2j\alpha}$. For every complex $s$ with
$\operatorname{Re} s > \max(1, 1 + \operatorname{Re} \alpha)$, for every prime $p$

$$\sum_{k \ge 0} \frac{f(p^k)}{p^{ks}}
= \frac{1 + p^{-s} + p^{-(s-\alpha)}}{(1 - p^{-2s})(1 - p^{-(2s-2\alpha)})},$$

the series $\sum_{n \ge 1} f(n)\,n^{-s}$ converges absolutely, and

$$\sum_{n \ge 1} \frac{f(n)}{n^s}
= \zeta(2s)\,\zeta(2s - 2\alpha) \prod_p \left(1 + p^{-s} + p^{-(s-\alpha)}\right).$$

The paper identifies $f$ with its divisor function $\sigma_{\star,\alpha}$; that identification is
not part of this statement.

## Sources

- Champak Talukdar and Helen K. Saikia, *A Square-Splitting A-Convolution of Narkiewicz Type*, INTEGERS 26 (2026), Article A56, Theorem 6.

Stated but not proved: `MetaMathlibExt.squareSplitSigma_multiplicative_eulerProduct` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquareSplittingConvolutionWanted.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html#square-split-sigma-multiplicative-euler).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Square-splitting convolution](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/square-splitting-convolution)
