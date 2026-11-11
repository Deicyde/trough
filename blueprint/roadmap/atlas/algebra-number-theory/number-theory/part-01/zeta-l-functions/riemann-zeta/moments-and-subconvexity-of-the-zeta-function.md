---
declaration: section
origin: cited
lean: MetaMathlibExt.riemannZeta_twelfth_moment_le, MetaMathlibExt.riemannZeta_twelfth_moment_le_log, MetaMathlibExt.riemannZeta_twelfth_moment_five_sevenths_le, MetaMathlibExt.riemannZeta_norm_le_subconvex, MetaMathlibExt.dirichletLFunction_mod_four_norm_le_subconvex
statement: formalized
---

# Moments and subconvexity of the zeta function

5 results, 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/moments-and-subconvexity-of-the-zeta-function/index.html).

## Twelfth moment of the Riemann zeta function on the critical line

For every
$\varepsilon > 0$ there is a constant $C$ such that for every real $T \ge 1$,

$$\int_1^T |\zeta(1/2 + it)|^{12} \, dt \le C T^{2+\varepsilon}.$$

This is Heath-Brown's bound in the form quoted by the sources.

## Sources

- Guodong Hua, *The General Divisor Problem of Cusp Form Coefficients over Arithmetic Progressions*, INTEGERS 24 (2024), Article A3, Lemma 2.4, equation (9); Guodong Hua, *On Higher Moments of Dirichlet Coefficients Attached to Symmetric Power L-Functions Over Certain Sequences of Positive Integers*, INTEGERS 24 (2024), Article A28, Lemma 5, equation (21).

Stated but not proved: `MetaMathlibExt.riemannZeta_twelfth_moment_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/ZetaSubconvexityBoundsWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ZetaSubconvexityBoundsWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/moments-and-subconvexity-of-the-zeta-function/index.html#riemann-zeta-twelfth-moment-le).

## Heath-Brown's twelfth moment bound with the logarithmic factor

There are constants $C$
and $T_0$ such that for every real $T \ge T_0$,

$$\int_1^T |\zeta(1/2 + it)|^{12} \, dt \le C T^2 (\log T)^{17}.$$

## Sources

- M. S. Datt, Ekta Soni, and A. Sankaranarayanan, *On the Asymptotic Formula for the Gcd-Sum Function*, INTEGERS 26 (2026), Article A70, Lemma 4.

Stated but not proved: `MetaMathlibExt.riemannZeta_twelfth_moment_le_log` is written with `theorem_wanted` in [WantedExt/NumberTheory/ZetaSubconvexityBoundsWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ZetaSubconvexityBoundsWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/moments-and-subconvexity-of-the-zeta-function/index.html#riemann-zeta-twelfth-moment-le-log).

## Twelfth moment of the Riemann zeta function on the line of real part 5/7

For every
$\varepsilon > 0$ there is a constant $C$ such that for every real $T \ge 1$,

$$\int_0^T |\zeta(5/7 + it)|^{12} \, dt \le C T^{1+\varepsilon}.$$

## Sources

- M. S. Datt, Ekta Soni, and A. Sankaranarayanan, *On the Asymptotic Formula for the Gcd-Sum Function*, INTEGERS 26 (2026), Article A70, Lemma 1.

Stated but not proved: `MetaMathlibExt.riemannZeta_twelfth_moment_five_sevenths_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/ZetaSubconvexityBoundsWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ZetaSubconvexityBoundsWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/moments-and-subconvexity-of-the-zeta-function/index.html#riemann-zeta-twelfth-moment-five-seventh).

## Subconvexity bound for the Riemann zeta function

For every $\varepsilon > 0$ there is
a constant $C$ such that for all real $\sigma$ and $t$ with $1/2 \le \sigma \le 1 + \varepsilon$
and $|t| \ge 1$,

$$|\zeta(\sigma + it)| \le C (1 + |t|)^{\max(13(1 - \sigma)/42,\, 0) + \varepsilon}.$$

The exponent comes from the exponent $13/84$ on the critical line; the truncation at $0$
follows both cited equations.

## Sources

- Guodong Hua, *The General Divisor Problem of Cusp Form Coefficients over Arithmetic Progressions*, INTEGERS 24 (2024), Article A3, Lemma 2.4, equation (10); Guodong Hua, *On Higher Moments of Dirichlet Coefficients Attached to Symmetric Power L-Functions Over Certain Sequences of Positive Integers*, INTEGERS 24 (2024), Article A28, Lemma 5, equation (22).

Stated but not proved: `MetaMathlibExt.riemannZeta_norm_le_subconvex` is written with `theorem_wanted` in [WantedExt/NumberTheory/ZetaSubconvexityBoundsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ZetaSubconvexityBoundsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/moments-and-subconvexity-of-the-zeta-function/index.html#riemann-zeta-norm-le-subconvex).

## Subconvexity bound for the Dirichlet L-function modulo 4

Let $\varepsilon > 0$ and let
$\chi$ be a non-principal Dirichlet character modulo $4$ (there is exactly one). Then there is a
constant $C$ such that for all real $\sigma$ and $t$ with $1/2 \le \sigma \le 1 + \varepsilon$ and
$|t| \ge 1$,

$$|L(\sigma + it, \chi)| \le C (1 + |t|)^{\max((1 - \sigma)/3,\, 0) + \varepsilon}.$$

The truncation at $0$ follows equation (23) of the source.

## Sources

- Guodong Hua, *On Higher Moments of Dirichlet Coefficients Attached to Symmetric Power L-Functions Over Certain Sequences of Positive Integers*, INTEGERS 24 (2024), Article A28, Lemma 5, equation (23).

Stated but not proved: `MetaMathlibExt.dirichletLFunction_mod_four_norm_le_subconvex` is written with `theorem_wanted` in [WantedExt/NumberTheory/ZetaSubconvexityBoundsWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ZetaSubconvexityBoundsWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/moments-and-subconvexity-of-the-zeta-function/index.html#dirichlet-lfunction-mod-four-norm-le-sub).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Moments and subconvexity of the zeta function](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/moments-and-subconvexity-of-the-zeta-function/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/moments-and-subconvexity-of-the-zeta-function)
