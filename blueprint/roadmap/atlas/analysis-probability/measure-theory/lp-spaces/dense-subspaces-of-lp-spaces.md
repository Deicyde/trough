---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.vanishingCutoff, MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.vanishingCutoff_nonneg, MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.vanishingCutoff_le_one, MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.vanishingCutoff_continuous, MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.vanishingCutoff_eq_zero_left, MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.vanishingCutoff_eq_zero_right, MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.vanishingCutoff_eq_one, MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.cutoffApprox
statement: formalized
proof: formalized
---

# Dense subspaces of Lp spaces

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/dense-subspaces-of-lp-spaces/index.html).

## Vanishing cutoff factor

For real numbers $a$, $b$, $\delta$ and $x$, the value at $x$
of the vanishing cutoff factor with endpoints $a$, $b$ and width $\delta$ is
$\max\bigl(0, \min\bigl(1, \min((x - a)/\delta, (b - x)/\delta)\bigr)\bigr)$, where division
by $0$ is read as $0$.

It vanishes at $a$ and at $b$. For $\delta > 0$ it equals $1$ on $[a + \delta, b - \delta]$,
an interval that is nonempty when $2\delta \le b - a$. At $\delta = 0$ it is identically
zero.

Formalized by `MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.vanishingCutoff`, a definition declared in [MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/dense-subspaces-of-lp-spaces/index.html#vanishing-cutoff).

## The vanishing cutoff factor is nonnegative

For all real numbers $a$, $b$, $\delta$
and $x$, the value at $x$ of the vanishing cutoff factor with endpoints $a$, $b$ and width
$\delta$ is at least $0$.

Formalized by `MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.vanishingCutoff_nonneg`, a theorem declared in [MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/dense-subspaces-of-lp-spaces/index.html#vanishing-cutoff-nonneg).

## The vanishing cutoff factor is at most one

For all real numbers $a$, $b$, $\delta$
and $x$, the value at $x$ of the vanishing cutoff factor with endpoints $a$, $b$ and width
$\delta$ is at most $1$.

Formalized by `MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.vanishingCutoff_le_one`, a theorem declared in [MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/dense-subspaces-of-lp-spaces/index.html#vanishing-cutoff-le-one).

## Continuity of the vanishing cutoff factor

For all $a, b, \delta \in \mathbb{R}$, the
vanishing cutoff factor with endpoints $a$, $b$ and width $\delta$ is a continuous function
$\mathbb{R} \to \mathbb{R}$.

Formalized by `MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.vanishingCutoff_continuous`, a theorem declared in [MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/dense-subspaces-of-lp-spaces/index.html#vanishing-cutoff-continuous).

## The vanishing cutoff factor vanishes at the left endpoint

For all
$a, b, \delta \in \mathbb{R}$, the vanishing cutoff factor with endpoints $a$, $b$ and width
$\delta$ takes the value $0$ at $a$.

Formalized by `MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.vanishingCutoff_eq_zero_left`, a theorem declared in [MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/dense-subspaces-of-lp-spaces/index.html#vanishing-cutoff-eq-zero-left).

## The vanishing cutoff factor vanishes at the right endpoint

For all real numbers $a$, $b$ and $\delta$, the vanishing cutoff factor with endpoints $a$, $b$
and width $\delta$ takes the value $0$ at $b$.

Formalized by `MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.vanishingCutoff_eq_zero_right`, a theorem declared in [MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/dense-subspaces-of-lp-spaces/index.html#vanishing-cutoff-eq-zero-right).

## The vanishing cutoff factor equals one on its plateau

Let $a, b \in \mathbb{R}$ and
$\delta > 0$. For every real $x$ with $a + \delta \le x \le b - \delta$, the vanishing cutoff
factor with endpoints $a$, $b$ and width $\delta$ takes the value $1$ at $x$.

Formalized by `MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.vanishingCutoff_eq_one`, a theorem declared in [MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/dense-subspaces-of-lp-spaces/index.html#vanishing-cutoff-eq-one).

## Cutoff approximants

Let $a, b \in \mathbb{R}$, let $E$ be a real normed space, let
$g_0 : \mathbb{R} \to E$ and $n \in \mathbb{N}$, and put $\delta_n = (b - a)/(n + 1)$. The $n$-th
cutoff approximant of $g_0$ with endpoints $a$ and $b$ is the function
$x \mapsto \varphi(x)\, g_0(x)$, where $\varphi$ is the vanishing cutoff factor with endpoints $a$,
$b$ and width $\delta_n$.

Formalized by `MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.cutoffApprox`, a definition declared in [MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/dense-subspaces-of-lp-spaces/index.html#cutoff-approx).

## Continuity of the cutoff approximants

Let $a, b \in \mathbb{R}$, let $E$ be a real
normed space and let $g_0 : \mathbb{R} \to E$ be continuous. Then for every $n \in \mathbb{N}$
the $n$-th cutoff approximant of $g_0$ with endpoints $a$ and $b$ is continuous.

Formalized by `MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.cutoffApprox_continuous`, a theorem declared in [MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/dense-subspaces-of-lp-spaces/index.html#cutoff-approx-continuous).

## Cutoff approximants vanish at the left endpoint

Let $a, b \in \mathbb{R}$, let $E$ be a
real normed space and let $g_0 : \mathbb{R} \to E$ be any function. For every $n \in \mathbb{N}$,
the $n$-th cutoff approximant of $g_0$ with endpoints $a$ and $b$ takes the value $0$ at $a$.

Formalized by `MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.cutoffApprox_eq_zero_left`, a theorem declared in [MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/dense-subspaces-of-lp-spaces/index.html#cutoff-approx-eq-zero-left).

## Cutoff approximants vanish at the right endpoint

Let $a, b \in \mathbb{R}$, let $E$ be a
real normed space and let $g_0 : \mathbb{R} \to E$ be any function. For every $n \in \mathbb{N}$,
the $n$-th cutoff approximant of $g_0$ with endpoints $a$ and $b$ takes the value $0$ at $b$.

Formalized by `MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.cutoffApprox_eq_zero_right`, a theorem declared in [MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/dense-subspaces-of-lp-spaces/index.html#cutoff-approx-eq-zero-right).

## Cutoff approximants stay in $L^p$

Let $E$ be a real normed space, let $\mu$ be a measure
on $\mathbb{R}$, let $p \in [0, \infty]$, and let $g_0 : \mathbb{R} \to E$ be continuous with
$g_0 \in L^p(\mu)$. Then for all $a, b \in \mathbb{R}$ and $n \in \mathbb{N}$, the $n$-th cutoff
approximant of $g_0$ with endpoints $a$ and $b$ lies in $L^p(\mu)$.

The approximant is pointwise dominated by $\|g_0\|$, since the cutoff factor takes values in
$[0, 1]$.

Formalized by `MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.cutoffApprox_memLp`, a theorem declared in [MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/dense-subspaces-of-lp-spaces/index.html#cutoff-approx-mem-lp).

## Pointwise bound on the cutoff error

Let $a, b \in \mathbb{R}$, let $E$ be a real normed
space and let $g_0 : \mathbb{R} \to E$. If $g_n$ denotes the $n$-th cutoff approximant of $g_0$
with endpoints $a$ and $b$, then $\|g_0(x) - g_n(x)\| \le \|g_0(x)\|$ for every
$n \in \mathbb{N}$ and every $x \in \mathbb{R}$.

Formalized by `MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.norm_sub_cutoffApprox_le`, a theorem declared in [MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/dense-subspaces-of-lp-spaces/index.html#norm-sub-cutoff-approx-le).

## Continuous functions vanishing at the endpoints are dense in $L^p$ of a compact interval

Let $a < b$ be real numbers, let $1 \le p < \infty$ and let $E$ be a real normed space. Write
$L^p([a, b])$ for $L^p$ with respect to Lebesgue measure restricted to $[a, b]$. For every
$f : \mathbb{R} \to E$ in $L^p([a, b])$ and every $\varepsilon \in (0, \infty]$, there is a
continuous $g : \mathbb{R} \to E$ with $g(a) = g(b) = 0$, $g \in L^p([a, b])$ and
$\|f - g\|_{L^p([a, b])} < \varepsilon$.

Formalized by `MathlibExt.MeasureTheory.Function.VanishingEndpointsDenseLp.exists_continuous_vanishing_endpoints_eLpNorm_sub_lt`, a theorem declared in [MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/VanishingEndpointsDenseLp.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/dense-subspaces-of-lp-spaces/index.html#exists-continuous-vanishing-endpoints-e).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dense subspaces of Lp spaces](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/dense-subspaces-of-lp-spaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/lp-spaces/dense-subspaces-of-lp-spaces)
