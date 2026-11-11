---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.essentialRange, MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.essentialRange_congr_ae, MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.not_mem_essentialRange_iff, MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.essentialRange_const, MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.essentialRange_count_eq_range, MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.memLp_const_top, MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.memLp_mul_of_memLp_top, MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.lpMulCLM
statement: formalized
---

# Multiplication operators on L²

29 results, 27 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html).

## Essential range

Let $\mu$ be a measure on a measurable space $\alpha$ and let
$\varphi : \alpha \to \mathbb{C}$. The essential range of $\varphi$ with respect to $\mu$ is the
set of $z \in \mathbb{C}$ such that $\mu(\{x \in \alpha : |\varphi(x) - z| < \varepsilon\}) > 0$
for every $\varepsilon > 0$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.essentialRange`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#essential-range).

## The essential range is invariant under almost-everywhere equality

Let $\mu$ be a
measure on a measurable space $\alpha$ and let $\varphi, \psi : \alpha \to \mathbb{C}$. If
$\varphi = \psi$ $\mu$-almost everywhere, then $\varphi$ and $\psi$ have the same essential range
with respect to $\mu$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.essentialRange_congr_ae`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#essential-range-congr-ae).

## Points outside the essential range

Let $\mu$ be a measure on a measurable space $\alpha$,
let $\varphi : \alpha \to \mathbb{C}$ and let $z \in \mathbb{C}$. Then $z$ is not in the essential
range of $\varphi$ with respect to $\mu$ if and only if there is $\varepsilon > 0$ such that the
preimage under $\varphi$ of the open ball
$B(z, \varepsilon) = \{w \in \mathbb{C} : |w - z| < \varepsilon\}$ has $\mu$-measure zero.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.not_mem_essentialRange_iff`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#not-mem-essential-range-iff).

## Essential range of a constant function

Let $\mu$ be a measure on a measurable space
$\alpha$ with $\mu(\alpha) \neq 0$, and let $c \in \mathbb{C}$. Then the essential range of the
constant function $x \mapsto c$ with respect to $\mu$ is $\{c\}$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.essentialRange_const`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#essential-range-const).

## Essential range for counting measure on a finite type

Let $\alpha$ be a finite type
with a measurable structure in which singletons are measurable, and let
$\varphi : \alpha \to \mathbb{C}$. Then the essential range of $\varphi$ with respect to counting
measure on $\alpha$ is the range $\varphi(\alpha)$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.essentialRange_count_eq_range`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#essential-range-count-eq-range).

## Constant functions are essentially bounded

Let $\mu$ be a measure on a measurable space
$\alpha$ and let $c \in \mathbb{C}$. The constant function $x \mapsto c$ belongs to
$\mathcal{L}^\infty(\mu)$: it is almost everywhere strongly measurable and essentially
bounded.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.memLp_const_top`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#mem-lp-const-top).

## An essentially bounded multiple of an $L^2$ function is in $L^2$

Let $\mu$ be a measure
on a measurable space $\alpha$, let $\varphi \colon \alpha \to \mathbb{C}$ be an essentially
bounded, almost everywhere strongly measurable function, and let $f \in L^2(\mu)$. Then the
pointwise product $x \mapsto \varphi(x) f(x)$, formed with a representative of $f$, belongs
to $\mathcal{L}^2(\mu)$: it is almost everywhere strongly measurable and square integrable.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.memLp_mul_of_memLp_top`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#mem-lp-mul-of-mem-lp-top).

## Multiplication operator on $L^2$

Let $\mu$ be a measure on a measurable space $\alpha$
and let $\varphi \colon \alpha \to \mathbb{C}$ be an essentially bounded, almost everywhere
strongly measurable function. The multiplication operator $M_\varphi$ is the continuous
$\mathbb{C}$-linear operator on $L^2(\mu)$ that sends $f$ to the class of the pointwise product
$x \mapsto \varphi(x) f(x)$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.lpMulCLM`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#lp-mul-clm).

## Multiplication operators with almost everywhere equal multipliers coincide

Let $\mu$ be
a measure on a measurable space $\alpha$ and let $\varphi, \psi \colon \alpha \to \mathbb{C}$ be
essentially bounded, almost everywhere strongly measurable functions. If $\varphi = \psi$
$\mu$-almost everywhere, then the multiplication operators $M_\varphi$ and $M_\psi$ on
$L^2(\mu)$ are equal.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.lpMulCLM_congr_ae`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#lp-mul-clm-congr-ae).

## Multiplication by a constant function on $L^2$

Let $\mu$ be a measure on a measurable
space $\alpha$ and let $c \in \mathbb{C}$. The multiplication operator on $L^2(\mu)$ by the
constant function $x \mapsto c$ sends every $f \in L^2(\mu)$ to the scalar multiple $c f$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.lpMulCLM_const_apply`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#lp-mul-clm-const-apply).

## Multiplication by one is the identity

Let $\mu$ be a measure on a measurable space
$\alpha$. The multiplication operator on $L^2(\mu)$ by the constant function $1$ is the
identity operator.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.lpMulCLM_one`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#lp-mul-clm-one).

## Product of multiplication operators

Let $\mu$ be a measure on a measurable space
$\alpha$ and, for an essentially bounded, almost everywhere strongly measurable function
$\chi \colon \alpha \to \mathbb{C}$, let $M_\chi$ be the multiplication operator
$f \mapsto \chi f$ on $L^2(\mu)$. Let $\varphi, \psi \colon \alpha \to \mathbb{C}$ be essentially
bounded, almost everywhere strongly measurable functions such that the pointwise product
$\varphi\psi \colon x \mapsto \varphi(x)\psi(x)$ is also essentially bounded and almost
everywhere strongly measurable. Then $M_{\varphi\psi} = M_\varphi M_\psi$, where the right side
is the composition of operators.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.lpMulCLM_mul`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#lp-mul-clm-mul).

## Shifting a multiplication operator by a scalar

Let $\mu$ be a measure on a measurable
space $\alpha$, let $\varphi : \alpha \to \mathbb{C}$ be in $L^\infty(\mu)$, let
$z \in \mathbb{C}$, and suppose the function $x \mapsto z - \varphi(x)$ is also in
$L^\infty(\mu)$. For $\psi \in L^\infty(\mu)$ write $M_\psi$ for the multiplication operator
$f \mapsto \psi f$ on $L^2(\mu)$. Then $z I - M_\varphi = M_{z - \varphi}$, where $I$ is the
identity operator on $L^2(\mu)$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.algebraMap_sub_lpMulCLM`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#algebra-map-sub-lp-mul-clm).

## Measurable representatives of essentially bounded functions

Let $\mu$ be a measure on a
measurable space $\alpha$ and let $\varphi : \alpha \to \mathbb{C}$ be in $L^\infty(\mu)$, that
is, $\mu$-almost everywhere strongly measurable and essentially bounded. Then there is a measurable
$\psi : \alpha \to \mathbb{C}$ such that $\varphi = \psi$ $\mu$-almost everywhere and $\psi$ is in
$L^\infty(\mu)$.

In particular $\varphi$ and $\psi$ define the same multiplication operator on $L^2(\mu)$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.exists_measurable_memLp`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#exists-measurable-mem-lp).

## Pointwise bound by the essential supremum norm

Let $\mu$ be a measure on a measurable
space $\alpha$ and let $\varphi : \alpha \to \mathbb{C}$ be in $L^\infty(\mu)$, that is,
$\mu$-almost everywhere strongly measurable and essentially bounded. Then
$|\varphi(x)| \le \|\varphi\|_{L^\infty(\mu)}$ for $\mu$-almost every $x \in \alpha$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.ae_norm_le_eLpNorm_top`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#ae-norm-le-e-lp-norm-top).

## Almost everywhere bound for a multiplication operator

Let $\mu$ be a measure on a
measurable space $\alpha$, let $\varphi \colon \alpha \to \mathbb{C}$ be an essentially
bounded, almost everywhere strongly measurable function, and let $M_\varphi$ be the
multiplication operator on $L^2(\mu)$. If $C$ is a real number with $|\varphi(x)| \le C$ for
$\mu$-almost every $x$, then $\|M_\varphi f\| \le C \|f\|$ for every $f \in L^2(\mu)$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.norm_lpMulCLM_apply_le_of_ae_bound`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#norm-lp-mul-clm-apply-le-of-ae-bound).

## Bound for a multiplication operator on the support of a vector

Let $\mu$ be a measure
on a measurable space $\alpha$, let $\varphi \colon \alpha \to \mathbb{C}$ be an essentially
bounded, almost everywhere strongly measurable function, and let $M_\varphi$ be the
multiplication operator on $L^2(\mu)$. If $C$ is a real number and $f \in L^2(\mu)$ is such
that, for $\mu$-almost every $x$, either $|\varphi(x)| \le C$ or $f(x) = 0$, then
$\|M_\varphi f\| \le C \|f\|$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.norm_lpMulCLM_apply_le_of_ae_support`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#norm-lp-mul-clm-apply-le-of-ae-support).

## Lower bound for the norm of a multiplication operator

Let $\mu$ be a measure on a
measurable space $\alpha$, let $\varphi \colon \alpha \to \mathbb{C}$ be an essentially
bounded, almost everywhere strongly measurable function, and let $M_\varphi$ be the
multiplication operator $f \mapsto \varphi f$ on $L^2(\mu)$. If $C \ge 0$ is a real number and
$f \in L^2(\mu)$ satisfies $\|f\| = 1$ and $C\,|f(x)| \le |\varphi(x)|\,|f(x)|$ for
$\mu$-almost every $x$, then $C \le \|M_\varphi\|$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.le_norm_lpMulCLM_of_ae_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#le-norm-lp-mul-clm-of-ae-le).

## Norm bound for multiplication operators on L²

Let $\mu$ be a measure on a measurable
space $\alpha$ and let $\varphi : \alpha \to \mathbb{C}$ be in $L^\infty(\mu)$, with essential
supremum norm $\|\varphi\|_\infty$. Then the multiplication operator $M_\varphi$ on the complex
space $L^2(\mu)$ has operator norm $\|M_\varphi\| \le \|\varphi\|_\infty$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.norm_lpMulCLM_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#norm-lp-mul-clm-le).

## Normalized indicator of a set of finite positive measure

Let $\mu$ be a measure on a
measurable space $\alpha$ and let $t \subseteq \alpha$ be a measurable set with
$0 < \mu(t) < \infty$. Then there is $u \in L^2(\mu)$ (complex valued) with $\|u\| = 1$ such that
$u(x) = \mu(t)^{-1/2}$ for $\mu$-almost every $x \in t$ and $u(x) = 0$ for $\mu$-almost every
$x \notin t$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.exists_unit_vector`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#exists-unit-vector).

## Norm of an L² multiplication operator with measurable multiplier

Let $\mu$ be a
$\sigma$-finite measure on a measurable space $\alpha$ and let $\varphi : \alpha \to \mathbb{C}$
be a measurable function in $L^\infty(\mu)$, with essential supremum norm $\|\varphi\|_\infty$.
Then the multiplication operator $M_\varphi$ on the complex space $L^2(\mu)$ has operator norm
$\|M_\varphi\| = \|\varphi\|_\infty$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.norm_lpMulCLM_of_measurable`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#norm-lp-mul-clm-of-measurable).

## Norm of a multiplication operator on L²

Let $\mu$ be a $\sigma$-finite measure on a
measurable space $\alpha$ and let $\varphi : \alpha \to \mathbb{C}$ be in $L^\infty(\mu)$, with
essential supremum norm $\|\varphi\|_\infty$. Then the multiplication operator $M_\varphi$ on the
complex space $L^2(\mu)$ has operator norm $\|M_\varphi\| = \|\varphi\|_\infty$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.norm_lpMulCLM`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 453](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L453). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#norm-lp-mul-clm).

## Spectrum of an L² multiplication operator with measurable multiplier

Let $\mu$ be a
$\sigma$-finite measure on a measurable space $\alpha$ and let $\varphi : \alpha \to \mathbb{C}$
be a measurable function in $L^\infty(\mu)$. Then the spectrum of the multiplication operator
$M_\varphi$, as an element of the complex algebra of bounded operators on $L^2(\mu)$, equals the
essential range of $\varphi$ with respect to $\mu$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.spectrum_lpMulCLM_of_measurable`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 460](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#spectrum-lp-mul-clm-of-measurable).

## Spectrum of a multiplication operator on L²

Let $\mu$ be a $\sigma$-finite measure on a
measurable space $\alpha$ and let $\varphi : \alpha \to \mathbb{C}$ be in $L^\infty(\mu)$. Then the
spectrum of the multiplication operator $M_\varphi$, as an element of the complex algebra of
bounded operators on $L^2(\mu)$, equals the essential range of $\varphi$ with respect to $\mu$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.spectrum_lpMulCLM`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 574](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L574). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#spectrum-lp-mul-clm).

## Eigenvalues of a multiplication operator on $L^2$, measurable multiplier

Let $\mu$ be a
$\sigma$-finite measure on a measurable space $\alpha$, let $\varphi : \alpha \to \mathbb{C}$ be
measurable and in $L^\infty(\mu)$, and let $M_\varphi$ be the multiplication operator
$f \mapsto \varphi f$ on $L^2(\mu)$. Then $z \in \mathbb{C}$ is an eigenvalue of $M_\varphi$ if and
only if $\mu(\{x \in \alpha : \varphi(x) = z\}) > 0$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.hasEigenvalue_lpMulCLM_iff_of_measurable`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 581](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L581). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#has-eigenvalue-lp-mul-clm-iff-of-measura).

## Eigenvalues of a multiplication operator on $L^2$

Let $\mu$ be a $\sigma$-finite measure
on a measurable space $\alpha$, let $\varphi : \alpha \to \mathbb{C}$ be in $L^\infty(\mu)$, and let
$M_\varphi$ be the multiplication operator $f \mapsto \varphi f$ on $L^2(\mu)$. Then
$z \in \mathbb{C}$ is an eigenvalue of $M_\varphi$ if and only if
$\mu(\{x \in \alpha : \varphi(x) = z\}) > 0$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LpMultiplicationOperator.hasEigenvalue_lpMulCLM_iff`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean, line 636](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LpMultiplicationOperator.lean#L636). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#has-eigenvalue-lp-mul-clm-iff).

## The space $L^2((1,2))$

$L^2([1,2])$ is the space of real-valued functions on
$\mathbb{R}$ that are square-integrable for Lebesgue measure restricted to $[1,2]$, taken modulo
equality almost everywhere on $[1,2]$.

Formalized by `MathlibExt.Analysis.OperatorTheory.MulByIdOnL2OneTwoSelfAdjointWanted.L2OnOneTwo`, an abbreviation declared in [WantedExt/Analysis/OperatorTheory/MulByIdOnL2OneTwoSelfAdjointWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/OperatorTheory/MulByIdOnL2OneTwoSelfAdjointWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#l2-on-one-two).

## Multiplication by $x$ on $L^2((1,2))$ is bounded, bijective and self-adjoint

Let
$L^2([1,2])$ be the real Hilbert space of square-integrable real functions for Lebesgue measure
on $[1,2]$, with inner product $\langle f, g\rangle = \int_1^2 f(x)g(x)\,dx$. Let
$T : L^2([1,2]) \to L^2([1,2])$ be a linear map such that for every $f$, $(Tf)(x) = x f(x)$ for
almost every $x \in [1,2]$. Then $T$ is continuous and bijective, and $T = T^*$, where $T^*$ is
the Hilbert space adjoint of $T$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Operator theory; General theory of linear operators), problem `ma_proofbench_l2_26`.

Stated but not proved: `MathlibExt.Analysis.OperatorTheory.MulByIdOnL2OneTwoSelfAdjointWanted.continuous_bijective_selfAdjoint_of_mul_id_L2_Icc_one_two` is written with `theorem_wanted` in [WantedExt/Analysis/OperatorTheory/MulByIdOnL2OneTwoSelfAdjointWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/OperatorTheory/MulByIdOnL2OneTwoSelfAdjointWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#continuous-bijective-self-adjoint-of-mul).

## Multiplication by $t$ is bounded on $L^2((0,1))$

Let $L^2([0,1])$ be the space of real
square-integrable functions for Lebesgue measure on $[0,1]$. There is a bounded linear operator
$T : L^2([0,1]) \to L^2([0,1])$ such that for every $f \in L^2([0,1])$, $(Tf)(t) = t f(t)$ for
almost every $t \in [0,1]$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Operator theory; General theory of linear operators), problem `ma_proofbench_l1_31`.

Stated but not proved: `MathlibExt.Analysis.OperatorTheory.MulByIdentityBoundedOnL2UnitIntervalWanted.exists_continuousLinearMap_mul_id_L2_Icc` is written with `theorem_wanted` in [WantedExt/Analysis/OperatorTheory/MulByIdentityBoundedOnL2UnitIntervalWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/OperatorTheory/MulByIdentityBoundedOnL2UnitIntervalWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html#exists-continuous-linear-map-mul-id-l2-i).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multiplication operators on L²](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-l)
