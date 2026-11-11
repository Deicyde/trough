---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.FloatingPoint.rne, Cslib.Algorithms.Lean.FloatingPoint.abs_rne_sub_le_min, Cslib.Algorithms.Lean.FloatingPoint.abs_rne_sub_le, Cslib.Algorithms.Lean.FloatingPoint.abs_rne_sub_le_half, Cslib.Algorithms.Lean.FloatingPoint.even_rne_of_abs_sub_eq_half, Cslib.Algorithms.Lean.FloatingPoint.rne_le_of_le, Cslib.Algorithms.Lean.FloatingPoint.le_rne_of_le, Cslib.Algorithms.Lean.FloatingPoint.IsFloat
statement: formalized
proof: formalized
---

# Floating-point rounding

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html).

## Rounding to an integer

## Nearest-integer rounding with ties to even

For $m$ in a linearly ordered field $K$ with a
floor function, $\operatorname{rne}(m)$ is the integer $\lfloor m \rfloor$ if
$m - \lfloor m \rfloor < 1/2$, the integer $\lfloor m \rfloor + 1$ if
$m - \lfloor m \rfloor > 1/2$, and, when $m - \lfloor m \rfloor = 1/2$, whichever of
$\lfloor m \rfloor$ and $\lfloor m \rfloor + 1$ is even.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.rne`, a definition declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#rne).

## Rounding error bounded by the distances to neighbouring integers

Let $K$ be a linearly
ordered field with a floor function. For every $m \in K$, the integer $\operatorname{rne}(m)$
obtained by rounding $m$ to the nearest integer, ties to even, satisfies
$|\operatorname{rne}(m) - m| \le m - \lfloor m \rfloor$ and
$|\operatorname{rne}(m) - m| \le \lfloor m \rfloor + 1 - m$.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.abs_rne_sub_le_min`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#abs-rne-sub-le-min).

## Round to nearest integer

Let $K$ be a linearly ordered field with a floor function. For
every $m \in K$ and every integer $k$, the integer $\operatorname{rne}(m)$ obtained by rounding
$m$ to the nearest integer, ties to even, satisfies $|\operatorname{rne}(m) - m| \le |k - m|$:
no integer is closer to $m$ than $\operatorname{rne}(m)$.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.abs_rne_sub_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#abs-rne-sub-le).

## Rounding to the nearest integer is within one half

Let $K$ be a linearly ordered field
with a floor function. For every $m \in K$, the integer $\operatorname{rne}(m)$ obtained by
rounding $m$ to the nearest integer, ties to even, satisfies
$|\operatorname{rne}(m) - m| \le 1/2$.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.abs_rne_sub_le_half`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#abs-rne-sub-le-half).

## Ties to even for the nearest integer

Let $K$ be a linearly ordered field with a floor
function, let $m \in K$, and let $\operatorname{rne}(m)$ be the integer obtained by rounding $m$
to the nearest integer, ties to even. If $|\operatorname{rne}(m) - m| = 1/2$, that is, $m$ is
halfway between two consecutive integers, then $\operatorname{rne}(m)$ is even.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.even_rne_of_abs_sub_eq_half`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#even-rne-of-abs-sub-eq-half).

## Rounding to nearest preserves integer upper bounds

Let $K$ be a linearly ordered field
with a floor function, let $m \in K$ and let $k$ be an integer. If $m \le k$, then
$\operatorname{rne}(m) \le k$, where $\operatorname{rne}(m)$ is $m$ rounded to the nearest
integer with ties to even.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.rne_le_of_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#rne-le-of-le).

## Rounding to nearest preserves integer lower bounds

Let $K$ be a linearly ordered field
with a floor function, let $m \in K$ and let $k$ be an integer. If $k \le m$, then
$k \le \operatorname{rne}(m)$, where $\operatorname{rne}(m)$ is $m$ rounded to the nearest
integer with ties to even.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.le_rne_of_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#le-rne-of-le).

## Binary floating-point numbers

For a natural number $p$, an element $x$ of a linearly
ordered field with a floor function is a binary floating-point number with a $p$-bit significand
and unbounded exponent when $x = m \cdot 2^e$ for some integers $m$ and $e$ with $|m| < 2^p$.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.IsFloat`, a definition declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#is-float).

## Floating-point numbers of a bounded format

For a natural number $p$ and integers
$q_{\min}$ and $q_{\max}$, an element $x$ of a linearly ordered field with a floor function is a
number of the binary format with $p$-bit significands and last-place exponents in
$[q_{\min}, q_{\max}]$ when $x = m \cdot 2^e$ for some integers $m$ and $e$ with $|m| < 2^p$ and
$q_{\min} \le e \le q_{\max}$. These are zero, the subnormal numbers and the normal numbers of
the format.

In IEEE 754 terms, $q_{\min} = e_{\min} - p + 1$ and $q_{\max} = e_{\max} - p + 1$.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.IsFloatIn`, a definition declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#is-float-in).

## Exponent of the last place

For a natural number $p$ (the significand length) and $x$ in a
linearly ordered field $K$ with a floor function, the exponent of the last place of $x$ is the
integer $\lfloor \log_2 |x| \rfloor - (p - 1)$. Here $\lfloor \log_2 |x| \rfloor$ is the integer
logarithm: the largest integer $n$ with $2^n \le |x|$ when $x \ne 0$, and $0$ when $x = 0$.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.ulpExp`, a definition declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#ulp-exp).

## Round to nearest, ties to even

For a natural number $p$ and an element $x$ of a linearly
ordered field with a floor function, let $e$ be the exponent of the last place of $x$ at precision
$p$, and let $\operatorname{rne}$ round to the nearest integer with ties to the even one. The
rounding of $x$ to nearest, ties to even, is
$\mathrm{fl}_p(x) = \operatorname{rne}(x / 2^e) \cdot 2^e$: scale $x$ so that its last place is the
units digit, round to the nearest integer with ties to even, and scale back.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.fl`, a definition declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#fl).

## Bounds on the scaled significand

Let $K$ be a linearly ordered field with a floor
function, let $p \ge 1$ be a natural number and let $x \in K$ be nonzero. Let
$e = \lfloor \log_2 |x| \rfloor - (p - 1)$ be the exponent of the last place of $x$ for
$p$-bit significands. Then $2^{p-1} \le |x / 2^e|$ and $|x / 2^e| < 2^p$.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.scaled_bounds`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#scaled-bounds).

## The rounding error at the scale of the last place

Let $x$ be an element of a linearly
ordered field with a floor function, let $p$ be a natural number, and let $e$ be the exponent of
the last place of $x$ at precision $p$. Writing $\operatorname{rne}$ for rounding to the nearest
integer with ties to even, the rounding $\mathrm{fl}_p(x)$ of $x$ to nearest, ties to even, at
precision $p$ has the error
$\mathrm{fl}_p(x) - x = (\operatorname{rne}(x / 2^e) - x / 2^e) \cdot 2^e$.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.fl_sub_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#fl-sub-eq).

## The relative error bound

Let $K$ be a linearly ordered field with a floor function and
let $p$ be a natural number. For every $x \in K$, the rounding $\mathrm{fl}(x)$ of $x$ to
nearest, ties to even, with $p$-bit significands satisfies
$|\mathrm{fl}(x) - x| \le u\,|x|$, where $u = 2^{-p}$ is the unit roundoff.

The exponent is unbounded, so the bound holds for every $x$, with no underflow or overflow.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.abs_fl_sub_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#abs-fl-sub-le).

## Round to nearest for floating-point numbers

Let $K$ be a linearly ordered field with a
floor function and let $p \ge 1$. For every $x \in K$ and every binary floating-point number
$f \in K$ with a $p$-bit significand (and unbounded exponent), the rounding $\mathrm{fl}(x)$ of
$x$ to nearest, ties to even, with $p$-bit significands satisfies
$|\mathrm{fl}(x) - x| \le |f - x|$: no floating-point number is closer to $x$ than
$\mathrm{fl}(x)$.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.abs_fl_sub_le_of_isFloat`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#abs-fl-sub-le-of-is-float).

## Floating-point numbers round to themselves

Let $p \ge 1$ and let $x$ be an element of a
linearly ordered field with a floor function. If $x$ is a binary floating-point number with a
$p$-bit significand, that is, $x = m \cdot 2^e$ for some integers $m$ and $e$ with $|m| < 2^p$,
then rounding $x$ to nearest, ties to even, at precision $p$ returns $x$: $\mathrm{fl}_p(x) = x$.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.fl_eq_self`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#fl-eq-self).

## Ties to even for floating-point rounding

Let $K$ be a linearly ordered field with a floor
function, let $p$ be a natural number, let $x \in K$, and let $e$ be the exponent of the last
place of $x$, which is $\lfloor \log_2 |x| \rfloor - (p - 1)$ for $x \ne 0$. If the rounding
$\mathrm{fl}(x)$ of $x$ to nearest, ties to even, with $p$-bit significands satisfies
$|\mathrm{fl}(x) - x| = 2^e / 2$, then the integer $\operatorname{rne}(x / 2^e)$, the significand
of $\mathrm{fl}(x)$ at the last place of $x$, is even.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.even_of_abs_fl_sub_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#even-of-abs-fl-sub-eq).

## Bound on the rounded significand

Let $K$ be a linearly ordered field with a floor
function, let $p \ge 1$, let $x \in K$ be nonzero, and let
$e = \lfloor \log_2 |x| \rfloor - (p - 1)$ be the exponent of the last place of $x$. Then
$|\operatorname{rne}(x / 2^e)| \le 2^p$, where $\operatorname{rne}$ rounds to the nearest
integer, ties to even.

Since $|x / 2^e| < 2^p$, the value $2^p$ occurs only when rounding carries into the next
binade.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.abs_rne_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#abs-rne-le).

## Rounding gives a floating-point number

Let $p \ge 1$. For every element $x$ of a linearly
ordered field with a floor function, the rounding $\mathrm{fl}_p(x)$ of $x$ to nearest, ties to
even, is a binary floating-point number with a $p$-bit significand: $\mathrm{fl}_p(x) = m \cdot 2^e$
for some integers $m$ and $e$ with $|m| < 2^p$.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.isFloat_fl`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#is-float-fl).

## In the normal range, rounding stays in the format

Let $p \ge 1$, let $q_{\min}$ and
$q_{\max}$ be integers, and let $x$ be an element of a linearly ordered field with a floor
function. If $2^{q_{\min} + p - 1} \le |x|$ ($x$ is at least the smallest normal number) and
$|x| \le (2^p - 1) \cdot 2^{q_{\max}}$ ($x$ is at most the largest finite number), then the
rounding $\mathrm{fl}_p(x)$ of $x$ to nearest, ties to even, is a number of the binary format
with $p$-bit significands whose last place has exponent in $[q_{\min}, q_{\max}]$.

Since $\mathrm{fl}_p(x)$ is also a nearest number of the format to $x$, with relative error at
most $2^{-p}$, rounding in the format in the normal range is the nearest-even rounding.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.isFloatIn_fl`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#is-float-in-fl).

## Round to nearest in a bounded format

Let $K$ be a linearly ordered field with a floor
function, let $p \ge 1$, and let $q_{\min}$ and $q_{\max}$ be integers. For every $x \in K$ and
every number $f$ of the binary format with $p$-bit significands and last-place exponents in
$[q_{\min}, q_{\max}]$, the rounding $\mathrm{fl}(x)$ of $x$ to nearest, ties to even, with
$p$-bit significands satisfies $|\mathrm{fl}(x) - x| \le |f - x|$.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.abs_fl_sub_le_of_isFloatIn`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#abs-fl-sub-le-of-is-float-in).

## The difference of floating-point numbers within a factor of two

Let $K$ be a linearly
ordered field with a floor function and let $p$ be a natural number. Let $x, y \in K$ and let
$m_x, m_y, e_x, e_y$ be integers with $|m_x| < 2^p$, $|m_y| < 2^p$, $x = m_x 2^{e_x}$ and
$y = m_y 2^{e_y}$. If $y / 2 \le x \le 2y$, then there is an integer $k$ with $|k| < 2^p$ and
$x - y = k \cdot 2^{\min(e_x, e_y)}$.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.exists_sub_eq_of_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 410](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L410). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#exists-sub-eq-of-le).

## Sterbenz's lemma

Let $p$ be a natural number and let $x$ and $y$ be binary floating-point
numbers with $p$-bit significands (and unbounded exponent) in a linearly ordered field with a
floor function. If $y / 2 \le x \le 2y$, then $x - y$ is also a binary floating-point number
with a $p$-bit significand.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.isFloat_sub`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 449](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L449). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#is-float-sub).

## Sterbenz's lemma in a bounded format

Let $p$ be a natural number, let $q_{\min}$ and
$q_{\max}$ be integers, and let $x$ and $y$ be numbers of the binary format with $p$-bit
significands whose last place has exponent in $[q_{\min}, q_{\max}]$ (subnormal numbers
included), in a linearly ordered field with a floor function. If $y / 2 \le x \le 2y$, then
$x - y$ is also a number of this format.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.isFloatIn_sub`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#is-float-in-sub).

## Floating-point subtraction is exact under Sterbenz's condition

Let $p \ge 1$ and let $x$
and $y$ be binary floating-point numbers with $p$-bit significands in a linearly ordered field
with a floor function. If $y / 2 \le x \le 2y$, then rounding $x - y$ to nearest, ties to even,
at precision $p$ returns it exactly: $\mathrm{fl}_p(x - y) = x - y$.

Formalized by `Cslib.Algorithms.Lean.FloatingPoint.fl_sub_eq_sub`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean, line 466](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/FloatingPoint.lean#L466). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html#fl-sub-eq-sub).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Floating-point rounding](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/algebraic-and-numerical-algorithms/floating-point-rounding)
