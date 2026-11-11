---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry1.ramanujan_part1_ch5_entry1, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry1Euleriangf.chapter5PolynomialShift, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry1Euleriangf.ramanujan_part1_ch5_entry1_euleriangf, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry2iEuleriangf.chapter5PolynomialShift_eq_taylor, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry2iEuleriangf.ramanujan_part1_ch5_entry2i_euleriangf, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry3.ramanujan_part1_ch5_entry3
statement: formalized
proof: formalized
---

# Inverting shift and difference operators

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/inverting-shift-and-difference-operators/index.html).

## Ramanujan's operator identity for the Bernoulli numbers

For a sequence
$a = (a_n)_{n \ge 0}$ of real numbers, a real number $h$ and a real polynomial $\varphi$ of
degree $d$ (with $d = 0$ for $\varphi = 0$), let
$S_a(h, \varphi) = \sum_{n=0}^{d} a_n h^n \varphi^{(n)}$. Let $b_n = B_n / n!$, where $B_n$ are
the Bernoulli numbers with $B_1 = -\tfrac12$. Then for every real polynomial $\varphi$ and every
real $h$, $S_b(h, \varphi)(x + h) - S_b(h, \varphi)(x) = h \varphi'(x)$ as polynomials in $x$.
Moreover $b$ is the only such sequence: if a real sequence $a$ satisfies
$S_a(h, \varphi)(x + h) - S_a(h, \varphi)(x) = h \varphi'(x)$ for every real polynomial $\varphi$
and every real $h$, then $a_n = b_n$ for every $n$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 5. The source's shift `p(x) ↦ p(x + h)` is `Polynomial.taylor h`, and the operator `∑ aₙ hⁿ Dⁿ` is `Entry1Euleriangf.chapter5DerivativeExpansion`.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry1.ramanujan_part1_ch5_entry1`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry1.lean, line 623](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry1.lean#L623). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/inverting-shift-and-difference-operators/index.html#ramanujan-part1-ch5-entry1).

## Polynomial shift

For a semiring $R$, an element $h \in R$ and a polynomial
$p \in R[x]$, the shift of $p$ by $h$ is the polynomial $p(x + h)$, the composition of $p$ with
$x + h$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry1Euleriangf.chapter5PolynomialShift`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry1Euleriangf.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry1Euleriangf.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/inverting-shift-and-difference-operators/index.html#chapter5-polynomial-shift).

## Ramanujan's operator identity for $(1 - 2^n) B_n / n!$

For a sequence
$a = (a_n)_{n \ge 0}$ of real numbers, a real number $h$ and a real polynomial $\varphi$ of
degree $d$ (with $d = 0$ for $\varphi = 0$), let
$S_a(h, \varphi) = \sum_{n=0}^{d} a_n h^n \varphi^{(n)}$. Let $c_n = (1 - 2^n) B_n / n!$, where
$B_n$ are the Bernoulli numbers with $B_1 = -\tfrac12$. Then for every real polynomial $\varphi$
and every real $h$, $S_c(h, \varphi)(x + h) + S_c(h, \varphi)(x) = h \varphi'(x)$ as polynomials
in $x$. Moreover $c$ is the only such sequence: if a real sequence $a$ satisfies
$S_a(h, \varphi)(x + h) + S_a(h, \varphi)(x) = h \varphi'(x)$ for every real polynomial $\varphi$
and every real $h$, then $a_n = c_n$ for every $n$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 5.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry1Euleriangf.ramanujan_part1_ch5_entry1_euleriangf`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry1Euleriangf.lean, line 872](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry1Euleriangf.lean#L872). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/inverting-shift-and-difference-operators/index.html#ramanujan-part1-ch5-entry1-euleriangf).

## The polynomial shift is the Taylor shift

For a semiring $R$, an element $h \in R$ and a
polynomial $p \in R[x]$, the shift $p(x + h)$ (the composition of $p$ with $x + h$) equals the
Taylor expansion of $p$ at $h$, the polynomial whose coefficient of $x^k$ is the $k$-th Hasse
derivative of $p$ evaluated at $h$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry2iEuleriangf.chapter5PolynomialShift_eq_taylor`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry2iEuleriangf.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry2iEuleriangf.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/inverting-shift-and-difference-operators/index.html#chapter5-polynomial-shift-eq-taylor).

## Ramanujan's solutions of two central difference equations

Let $\varphi$ be a real
polynomial of degree $d$ (with $d = 0$ for $\varphi = 0$). For $n \ge 0$ let
$F_n(x) = \varphi(x) + \sum_{k=1}^{n} \frac{(-1)^k (n!)^2}{(n+k)!\,(n-k)!}
\bigl(\varphi(x+k) + \varphi(x-k)\bigr)$, and let
$M = \sum_{n=0}^{\lfloor d/2 \rfloor} \frac{1}{2n+1} F_n$ and
$P = \sum_{n=0}^{\lfloor d/2 \rfloor} \binom{2n}{n} 2^{-n} F_n$. Then $F_n = 0$ for every $n$
with $d < 2n$, $M(x+1) - M(x-1) = 2 \varphi'(x)$ and $P(x+1) + P(x-1) = 2 \varphi(x)$, as
polynomials in $x$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 5, Entry 2(i), pp. 111–112.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry2iEuleriangf.ramanujan_part1_ch5_entry2i_euleriangf`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry2iEuleriangf.lean, line 1010](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry2iEuleriangf.lean#L1010). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/inverting-shift-and-difference-operators/index.html#ramanujan-part1-ch5-entry2i-euleriangf).

## Eulerian-polynomial inverse of a shift-plus-multiple operator

Let $A(n, k)$ be the
Eulerian numbers, given by $A(0, 0) = 1$, $A(0, k) = 0$ for $k \ge 1$ and
$A(n + 1, k) = (k + 1) A(n, k) + (n + 1 - k) A(n, k - 1)$, the last term read as $0$ when
$k = 0$. For $p \in \mathbb{C}$ set $\psi_0(p) = 1$ and
$\psi_n(p) = \sum_{k=0}^{n-1} A(n, k) (-p)^k$ for $n \ge 1$. For a sequence $a_0, a_1, \ldots$
of complex numbers, $h \in \mathbb{C}$ and a polynomial $\varphi \in \mathbb{C}[x]$, write
$E_{a,h} \varphi = \sum_{n=0}^{\deg \varphi} a_n h^n \varphi^{(n)}$, where $\varphi^{(n)}$ is the
$n$-th derivative. Fix $p \in \mathbb{C}$ with $p \ne -1$ and put
$c_n = \frac{(-1)^n \psi_n(p)}{n! \, (p + 1)^{n + 1}}$. Then:
(1) for every $h \in \mathbb{C}$ and every $\varphi \in \mathbb{C}[x]$, the polynomial
$f = E_{c,h} \varphi$ satisfies $f(x + h) + p f(x) = \varphi(x)$ as polynomials in $x$;
(2) if a sequence $a$ of complex numbers is such that $f = E_{a,h} \varphi$ satisfies
$f(x + h) + p f(x) = \varphi(x)$ for every $h \in \mathbb{C}$ and every $\varphi \in \mathbb{C}[x]$,
then $a_n = c_n$ for every $n \ge 0$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 5.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry3.ramanujan_part1_ch5_entry3`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry3.lean, line 1163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry3.lean#L1163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/inverting-shift-and-difference-operators/index.html#ramanujan-part1-ch5-entry3).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Inverting shift and difference operators](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/inverting-shift-and-difference-operators/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/inverting-shift-and-difference-operators)
