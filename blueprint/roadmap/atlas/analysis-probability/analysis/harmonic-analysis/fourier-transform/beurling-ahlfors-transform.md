---
declaration: section
origin: cited
lean: MathlibExt.Analysis.BeurlingAhlfors.pstar, MathlibExt.Analysis.BeurlingAhlfors.beurlingTrunc, MathlibExt.Analysis.BeurlingAhlfors.beurlingTransform, MathlibExt.Analysis.BeurlingAhlfors.IsBound, MathlibExt.Analysis.BeurlingAhlfors.beurlingNorm, MathlibExt.Analysis.BeurlingAhlfors.beurlingNorm_le_of_isBound, MathlibExt.Analysis.BeurlingAhlfors.beurlingAhlforsConstant, MathlibExt.Analysis.BeurlingAhlfors.IwaniecConjecture
statement: formalized
---

# Beurling–Ahlfors transform

11 results, 8 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/beurling-ahlfors-transform/index.html).

## Larger of an exponent and its conjugate

For a real number $p$,
$p^* = \max(p, p/(p-1))$, with division by zero taken to be $0$ (so $p^* = 1$ at $p = 1$). For
$p > 1$ this is the larger of $p$ and its conjugate exponent $p/(p-1)$.

Formalized by `MathlibExt.Analysis.BeurlingAhlfors.pstar`, a definition declared in [MathlibExt/Analysis/BeurlingAhlfors.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/BeurlingAhlfors.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/beurling-ahlfors-transform/index.html#pstar).

## Truncated Beurling–Ahlfors integral

For a real number $\varepsilon$, a function
$f : \mathbb{C} \to \mathbb{C}$ and $z \in \mathbb{C}$, the truncated Beurling–Ahlfors integral
at cutoff $\varepsilon$ is
$-\frac{1}{\pi} \int_{|w - z| > \varepsilon} \frac{f(w)}{(z - w)^2} \, dw$, the integral being
with respect to Lebesgue measure on $\mathbb{C}$ and taken to be $0$ when the integrand is not
integrable.

Formalized by `MathlibExt.Analysis.BeurlingAhlfors.beurlingTrunc`, a definition declared in [MathlibExt/Analysis/BeurlingAhlfors.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/BeurlingAhlfors.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/beurling-ahlfors-transform/index.html#beurling-trunc).

## Beurling–Ahlfors transform

For $f : \mathbb{C} \to \mathbb{C}$ and $z \in \mathbb{C}$,
$Bf(z)$ is the limit as $\varepsilon \to 0^+$ of the truncated Beurling–Ahlfors integrals
$-\frac{1}{\pi} \int_{|w - z| > \varepsilon} \frac{f(w)}{(z - w)^2} \, dw$ (each taken to be $0$
when its integrand is not integrable). Where this limit does not exist, $Bf(z)$ is an
unspecified complex number.

For $f \in L^p$ with $1 < p < \infty$ the limit exists almost everywhere.

Formalized by `MathlibExt.Analysis.BeurlingAhlfors.beurlingTransform`, a definition declared in [MathlibExt/Analysis/BeurlingAhlfors.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/BeurlingAhlfors.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/beurling-ahlfors-transform/index.html#beurling-transform).

## Admissible bounds for the Beurling–Ahlfors transform

For real numbers $p$ and $C$, $C$
is an admissible $L^p$ bound constant for the Beurling–Ahlfors transform $B$ when
$\|Bf\|_q \le \max(C, 0) \, \|f\|_q$ for every almost everywhere strongly measurable function
$f : \mathbb{C} \to \mathbb{C}$, where $q = \max(p, 0)$ and $\|\cdot\|_q$ is the extended
$L^q$ norm with respect to Lebesgue measure (identically $0$ when $q = 0$), with values in
$[0, \infty]$ and the convention $0 \cdot \infty = 0$.

Formalized by `MathlibExt.Analysis.BeurlingAhlfors.IsBound`, a definition declared in [MathlibExt/Analysis/BeurlingAhlfors.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/BeurlingAhlfors.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/beurling-ahlfors-transform/index.html#is-bound).

## Norm of the Beurling–Ahlfors transform

For a real number $p$, the norm $\|B\|_p$ of the
Beurling–Ahlfors transform $B$ is the infimum of the real numbers $C \ge 0$ that are admissible
$L^p$ bound constants for $B$, and is $0$ when there is no such $C$. In particular an upper
bound on $\|B\|_p$ alone does not imply that $B$ is bounded on $L^p$.

Formalized by `MathlibExt.Analysis.BeurlingAhlfors.beurlingNorm`, a definition declared in [MathlibExt/Analysis/BeurlingAhlfors.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/BeurlingAhlfors.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/beurling-ahlfors-transform/index.html#beurling-norm).

## Nonnegative admissible bounds bound the Beurling–Ahlfors norm

Let $p$ and $C$ be real
numbers with $C \ge 0$, and let $\|B\|_p$ be the infimum of the nonnegative admissible $L^p$
bound constants for the Beurling–Ahlfors transform $B$ ($0$ if there are none). If $C$ is an
admissible $L^p$ bound constant for $B$, then $\|B\|_p \le C$.

Formalized by `MathlibExt.Analysis.BeurlingAhlfors.beurlingNorm_le_of_isBound`, a theorem declared in [MathlibExt/Analysis/BeurlingAhlfors.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/BeurlingAhlfors.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/beurling-ahlfors-transform/index.html#beurling-norm-le-of-is-bound).

## Beurling–Ahlfors constant

The Beurling–Ahlfors constant is the supremum, over real
numbers $p > 1$, of $\|B\|_p / (p^* - 1)$, where $B$ is the Beurling–Ahlfors transform,
$\|B\|_p$ is the infimum of the real numbers $C \ge 0$ that are admissible $L^p$ bound
constants for $B$ (and $0$ if there is no such $C$), and $p^* = \max(p, p/(p-1))$. The
supremum is taken in $\mathbb{R}$, so it is $0$ when these ratios are not bounded above.

Formalized by `MathlibExt.Analysis.BeurlingAhlfors.beurlingAhlforsConstant`, a definition declared in [MathlibExt/Analysis/BeurlingAhlfors.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/BeurlingAhlfors.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/beurling-ahlfors-transform/index.html#beurling-ahlfors-constant).

## Iwaniec's conjecture

For every real number $p > 1$, the $L^p$ norm of the
Beurling–Ahlfors transform $B$ satisfies $\|B\|_p = p^* - 1$, where $p^* = \max(p, p/(p-1))$.

Given Lehto's lower bound $\|B\|_p \ge p^* - 1$, this is equivalent to the Beurling–Ahlfors
constant being equal to $1$.

Formalized by `MathlibExt.Analysis.BeurlingAhlfors.IwaniecConjecture`, a definition declared in [MathlibExt/Analysis/BeurlingAhlfors.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/BeurlingAhlfors.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/beurling-ahlfors-transform/index.html#iwaniec-conjecture).

## Lehto's lower bound for the Beurling–Ahlfors transform

For a function
$f : \mathbb{C} \to \mathbb{C}$ let $Bf(z)$ be the limit as $\varepsilon \to 0^+$ of
$-\frac{1}{\pi} \int_{|w - z| > \varepsilon} \frac{f(w)}{(z - w)^2} \, dA(w)$, where $dA$ is
Lebesgue area measure (a junk value where the limit does not exist). For real $p > 1$ let
$p^* = \max(p, p/(p - 1))$ and let $\|B\|_p$ be the infimum of the constants $C \ge 0$ such that
$\|Bf\|_{L^p} \le C\,\|f\|_{L^p}$ in $[0, \infty]$ for every almost everywhere strongly
measurable $f : \mathbb{C} \to \mathbb{C}$, taken to be $0$ when there is no such $C$. Then
$p^* - 1 \le \|B\|_p$ for every real $p > 1$.

Because $\|B\|_p$ is $0$ when no such $C$ exists, this also asserts that $B$ has an admissible
$L^p$ bound for every $p > 1$.

## Sources

- Lehto (1965): `‖B‖ₚ ≥ p* - 1` for all `1 < p`.

Stated but not proved: `MathlibExt.Analysis.BeurlingAhlforsWanted.lehtoLowerBound_wanted` is written with `theorem_wanted` in [WantedExt/Analysis/BeurlingAhlforsWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/BeurlingAhlforsWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/beurling-ahlfors-transform/index.html#lehto-lower-bound-wanted).

## Bañuelos–Janakiraman upper bound for the Beurling–Ahlfors transform

For a function
$f : \mathbb{C} \to \mathbb{C}$ let $Bf(z)$ be the limit as $\varepsilon \to 0^+$ of
$-\frac{1}{\pi} \int_{|w - z| > \varepsilon} \frac{f(w)}{(z - w)^2} \, dA(w)$, where $dA$ is
Lebesgue area measure (a junk value where the limit does not exist), and for real $p > 1$ let
$p^* = \max(p, p/(p - 1))$. For every real $p > 1$ and every almost everywhere strongly measurable
$f : \mathbb{C} \to \mathbb{C}$, $\|Bf\|_{L^p} \le 1.575\,(p^* - 1)\,\|f\|_{L^p}$, with the
$L^p$ norms taken in $[0, \infty]$.

## Sources

- Bañuelos and Janakiraman, *Lp-bounds for the Beurling--Ahlfors transform*, Trans. Amer. Math. Soc. 360 (2008): `‖B‖ₚ ≤ 1.575 (p* - 1)` for all `1 < p`. Stated as the actual finite exponential bound (an admissible `L^p` bound constant), not as an inequality for the totalized infimum; combined with `beurlingNorm_le_of_isBound` (and `0 ≤ 1.575 * (pstar p - 1)`, from `two_le_pstar`) it yields `beurlingNorm p ≤ 1.575 * (pstar p - 1)`.

Stated but not proved: `MathlibExt.Analysis.BeurlingAhlforsWanted.banuelosJanakiramanUpperBound_wanted` is written with `theorem_wanted` in [WantedExt/Analysis/BeurlingAhlforsWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/BeurlingAhlforsWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/beurling-ahlfors-transform/index.html#banuelos-janakiraman-upper-bound-wanted).

## The Beurling–Ahlfors transform has $L^2$ norm $1$

For a function
$f : \mathbb{C} \to \mathbb{C}$ let $Bf(z)$ be the limit as $\varepsilon \to 0^+$ of
$-\frac{1}{\pi} \int_{|w - z| > \varepsilon} \frac{f(w)}{(z - w)^2} \, dA(w)$, where $dA$ is
Lebesgue area measure (a junk value where the limit does not exist). The infimum $\|B\|_2$ of the
constants $C \ge 0$ such that $\|Bf\|_{L^2} \le C\,\|f\|_{L^2}$ in $[0, \infty]$ for every almost
everywhere strongly measurable $f : \mathbb{C} \to \mathbb{C}$ (taken to be $0$ when there is no
such $C$) equals $1$.

## Sources

- the `L²` isometry recorded in Bañuelos--Janakiraman (2008), introduction: `‖B‖₂ = 1`.

Stated but not proved: `MathlibExt.Analysis.BeurlingAhlforsWanted.l2Norm_wanted` is written with `theorem_wanted` in [WantedExt/Analysis/BeurlingAhlforsWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/BeurlingAhlforsWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/beurling-ahlfors-transform/index.html#l2-norm-wanted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Beurling–Ahlfors transform](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/beurling-ahlfors-transform/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/harmonic-analysis/fourier-transform/beurling-ahlfors-transform)
