---
declaration: section
origin: cited
lean: MetaMathlibExt.LagrangeInversion.coeff_mul_pow_eq_coeff_of_eq_X_mul_subst, MetaMathlibExt.LagrangeInversion.hermite_lagrange_diagonal_formula, MetaMathlibExt.hermite_lagrange_inversion, fps_lagrange_burmann_coeff', fps_lagrange_burmann_coeff
statement: formalized
proof: formalized
---

# Lagrange inversion theorem

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/lagrange-inversion-theorem/index.html).

## Hermite's diagonal form of Lagrange inversion without side conditions

Let $R$ be a
commutative ring, let $F$, $\varphi$, $w$ and $G$ be formal power series over $R$, and write
$[X^n]H$ for the coefficient of $X^n$ in a power series $H$. Write $\varphi'$ for the formal
derivative of $\varphi$, and $\varphi(w)$, $\varphi'(w)$, $F(w)$ for the substitution of $w$ into
$\varphi$, $\varphi'$, $F$. If $w = X\,\varphi(w)$ and $(1 - X\,\varphi'(w))\,G = F(w)$, then
$[X^n](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/formal-power-series/lagrange-inversion-theorem/F\varphi^n) = [X^n]G$ for every natural number $n$.

The constant term of $w$ vanishes automatically, and $\varphi$ may have zero constant term.

Formalized by `MetaMathlibExt.LagrangeInversion.coeff_mul_pow_eq_coeff_of_eq_X_mul_subst`, a theorem declared in [MathlibExt/RingTheory/PowerSeries/HermiteLagrangeDiagonal.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/PowerSeries/HermiteLagrangeDiagonal.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/lagrange-inversion-theorem/index.html#coeff-mul-pow-eq-coeff-of-eq-x-mul-subst).

## Hermite's diagonal form of Lagrange inversion

Let $R$ be a commutative ring, let $F$,
$\varphi$, $w$ and $G$ be formal power series over $R$, and write $[X^n]H$ for the coefficient
of $X^n$ in a power series $H$. Write $\varphi'$ for the formal derivative of $\varphi$, and
$\varphi(w)$, $\varphi'(w)$, $F(w)$ for the substitution of $w$ into $\varphi$, $\varphi'$, $F$.
Suppose that $w$ has constant term $0$, that $\varphi$ has nonzero constant term, that
$w = X\,\varphi(w)$, and that $(1 - X\,\varphi'(w))\,G = F(w)$. Then
$[X^n](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/formal-power-series/lagrange-inversion-theorem/F\varphi^n) = [X^n]G$ for every natural number $n$.

In contrast to the derivative-coefficient form of the Lagrange–Bürmann formula, the derivative
here is absorbed into the defining equation for $G$.

Reference: Bakir Farhi, "Some Applications of the Lagrange Inversion Formula
for the k-Fibonacci Numbers", Journal of Integer Sequences 27 (2024),
Hermite corollary and derivation lines 205-240.

## Sources

- https://cs.uwaterloo.ca/journals/JIS/VOL27/Farhi/farhi35.tex, statement lines 205-210; lines 205-240.

Formalized by `MetaMathlibExt.LagrangeInversion.hermite_lagrange_diagonal_formula`, a theorem declared in [MathlibExt/RingTheory/PowerSeries/HermiteLagrangeDiagonal.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/PowerSeries/HermiteLagrangeDiagonal.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/lagrange-inversion-theorem/index.html#hermite-lagrange-diagonal-formula).

## Hermite's form of Lagrange inversion as a series identity

Let $\varphi$, $g$, $F$ and $\psi$
be formal power series over $\mathbb{C}$, write $F'$ for the formal derivative of $F$, and write
$h(k)$ for the substitution of a power series $k$ into a power series $h$. Suppose that $\varphi$
has nonzero constant term, that $F\varphi = X$, and that $\psi$ is a two-sided compositional
inverse of $F$, that is, $F(\psi) = X$ and $\psi(F) = X$. Let $H = \sum_{n \ge 0} c_n X^n$,
where $c_n$ is the coefficient of $X^n$ in $g\varphi^n$. Then

$$X\, g(\psi) = H\, \psi\, F'(\psi).$$

The source states this, with $F = X/\varphi$, as $X\, g(\psi) / (\psi\, F'(\psi)) = H$; the
form here is cleared of denominators.

## Sources

- Bakir Farhi, "Some Applications of the Lagrange Inversion Formula for the k-Fibonacci Numbers," Journal of Integer Sequences 27 (2024), Article 24.1.1, Corollary (Hermite, label t-her), lines 205–210, https://cs.uwaterloo.ca/journals/JIS/VOL27/Farhi/farhi35.tex

Formalized by `MetaMathlibExt.hermite_lagrange_inversion`, a theorem declared in [MathlibExt/RingTheory/PowerSeries/HermiteLagrangeSeries.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/PowerSeries/HermiteLagrangeSeries.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/lagrange-inversion-theorem/index.html#hermite-lagrange-inversion).

## Lagrange–Bürmann formula from the fixed-point equation alone

Let $R$ be a commutative
ring and let $A$, $\varphi$ and $g$ be formal power series over $R$ with $A = X\,\varphi(A)$,
where $\varphi(A)$ and $g(A)$ denote the substitution of $A$ into $\varphi$ and $g$. Write
$[X^m]H$ for the coefficient of $X^m$ in a power series $H$ and $g'$ for the formal derivative
of $g$. Then for every natural number $n \ge 1$,

$$n\, [X^n]\, g(A) = [X^{n-1}]\left(g' \varphi^n\right).$$

No condition on the constant term of $\varphi$ is needed.

Formalized by `fps_lagrange_burmann_coeff'`, a theorem declared in [MathlibExt/RingTheory/PowerSeries/LagrangeBurmannCoefficient.lean, line 660](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/PowerSeries/LagrangeBurmannCoefficient.lean#L660). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/lagrange-inversion-theorem/index.html#fps-lagrange-burmann-coeff).

## Lagrange–Bürmann formula, coefficient form

Let $R$ be a commutative ring and let $A$,
$\varphi$ and $g$ be formal power series over $R$ such that the constant term of $A$ is
nilpotent, $\varphi$ has nonzero constant term, and $A = X\,\varphi(A)$, where $\varphi(A)$ and
$g(A)$ denote the substitution of $A$ into $\varphi$ and $g$. Write $[X^m]H$ for the coefficient
of $X^m$ in a power series $H$ and $g'$ for the formal derivative of $g$. Then for every
natural number $n \ge 1$,

$$n\, [X^n]\, g(A) = [X^{n-1}]\left(g' \varphi^n\right).$$

This is the division-free form over a commutative ring: no division by $n$ is required.

## Sources

- Alexander M. Haupt, "Enumeration of S-omino Towers and Row-Convex k-omino Towers," JIS 24 (2021), proposition at lines 400–407, https://cs.uwaterloo.ca/journals/JIS/VOL24/Haupt/haupt4.tex. Corroborating power specialization: Dmitry Kruchinin and Vladimir Kruchinin, "A Method for Obtaining Generating Functions for Central Coefficients of Triangles," JIS 15 (2012), lines 199–210, https://cs.uwaterloo.ca/journals/JIS/VOL15/Kruchinin/kruchinin5.tex.

Formalized by `fps_lagrange_burmann_coeff`, a theorem declared in [MathlibExt/RingTheory/PowerSeries/LagrangeBurmannCoefficient.lean, line 700](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/PowerSeries/LagrangeBurmannCoefficient.lean#L700). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/lagrange-inversion-theorem/index.html#fps-lagrange-burmann-coeff-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lagrange inversion theorem](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/lagrange-inversion-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/formal-power-series/lagrange-inversion-theorem)
