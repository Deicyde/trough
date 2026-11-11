---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.VolterraSpace, MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.clamp01, MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.volterraExtend, MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.volterraExtend_continuous, MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.volterraExtend_apply_of_mem, MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.norm_volterraExtend_le, MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.volterraPrimitive_continuous, MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.volterraPrimitive_norm_le
statement: formalized
---

# Volterra operator

21 results, 20 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html).

## The domain of the Volterra operator

The space on which the Volterra operator acts is the
space of bounded continuous real functions on $[0, 1]$, with the sup norm.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.VolterraSpace`, an abbreviation declared in [MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html#volterra-space).

## Clamping to the unit interval

For a real number $t$, its clamp to the unit interval is
$\max(0, \min(t, 1))$, regarded as a point of $[0, 1]$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.clamp01`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html#clamp01).

## Extension by clamping

For a bounded continuous real function $f$ on $[0, 1]$, its
extension to $\mathbb{R}$ is the function $t \mapsto f(\max(0, \min(t, 1)))$.

This continuous extension is used to write $(Vf)(x)$, for $V$ the Volterra operator, as an
interval integral over $\mathbb{R}$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.volterraExtend`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html#volterra-extend).

## The clamped extension is continuous

For every bounded continuous real function $f$ on
$[0, 1]$, its extension $t \mapsto f(\max(0, \min(t, 1)))$ to $\mathbb{R}$ by clamping is
continuous on $\mathbb{R}$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.volterraExtend_continuous`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html#volterra-extend-continuous).

## The clamped extension agrees with the original function on the unit interval

For
every bounded continuous real function $f$ on $[0, 1]$ and every real $t$ with $0 \le t \le 1$,
the extension $s \mapsto f(\max(0, \min(s, 1)))$ of $f$ to $\mathbb{R}$ takes the value
$f(t)$ at $t$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.volterraExtend_apply_of_mem`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html#volterra-extend-apply-of-mem).

## The clamped extension is bounded by the sup norm

For every bounded continuous real
function $f$ on $[0, 1]$ and every real $t$, the extension of $f$ to $\mathbb{R}$ by clamping
satisfies $|f(\max(0, \min(t, 1)))| \le \|f\|_\infty$, where
$\|f\|_\infty = \sup_{x \in [0, 1]} |f(x)|$ is the sup norm of $f$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.norm_volterraExtend_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html#norm-volterra-extend-le).

## Continuity of the Volterra primitive

For every bounded continuous real function $f$ on
$[0, 1]$, the function $x \mapsto \int_0^x \tilde f(t)\,dt$ on $[0, 1]$ is continuous, where
$\tilde f(t) = f(\max(0, \min(t, 1)))$ is the extension of $f$ to $\mathbb{R}$ by clamping the
argument into $[0, 1]$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.volterraPrimitive_continuous`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html#volterra-primitive-continuous).

## Sup-norm bound for the Volterra primitive

For every bounded continuous real function $f$
on $[0, 1]$ and every $x \in [0, 1]$, $\left|\int_0^x \tilde f(t)\,dt\right| \le \|f\|$, where
$\|f\|$ is the sup norm of $f$ and $\tilde f(t) = f(\max(0, \min(t, 1)))$ is the extension of
$f$ to $\mathbb{R}$ by clamping the argument into $[0, 1]$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.volterraPrimitive_norm_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html#volterra-primitive-norm-le).

## The Volterra operator as a linear map

The real-linear map $V$ on the space of bounded
continuous real functions on $[0, 1]$ given by $(Vf)(x) = \int_0^x f(t)\,dt$ for
$x \in [0, 1]$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.volterraLinearMap`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html#volterra-linear-map).

## Sup-norm bound for the Volterra linear map

For every bounded continuous real function
$f$ on $[0, 1]$, the Volterra linear map $V$ satisfies $\|Vf\| \le 1 \cdot \|f\|$, where
$\|\cdot\|$ is the sup norm.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.volterraLinearMap_norm_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html#volterra-linear-map-norm-le).

## The Volterra operator

The bounded real-linear operator $V$ on the space of bounded
continuous real functions on $[0, 1]$ (equivalently $C([0, 1], \mathbb{R})$ with the sup norm)
given by $(Vf)(x) = \int_0^x f(t)\,dt$ for $x \in [0, 1]$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.volterraOperator`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html#volterra-operator).

## Evaluation formula for the Volterra operator

For every bounded continuous real function
$f$ on $[0, 1]$ and every $x \in [0, 1]$, the Volterra operator $V$ satisfies
$(Vf)(x) = \int_0^x \tilde f(t)\,dt$, where $\tilde f(t) = f(\max(0, \min(t, 1)))$ is the
extension of $f$ to $\mathbb{R}$ by clamping the argument into $[0, 1]$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.volterraOperator_apply`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html#volterra-operator-apply).

## Volterra integrals vanish at the left endpoint

For every bounded continuous real function
$f$ on $[0, 1]$, the Volterra operator $V$ satisfies $(Vf)(0) = 0$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.volterraOperator_apply_zero`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html#volterra-operator-apply-zero).

## The Volterra operator has norm at most one

The Volterra operator $V$,
$(Vf)(x) = \int_0^x f(t)\,dt$, acting on the space of bounded continuous real functions on
$[0, 1]$ with the sup norm, has operator norm $\|V\| \le 1$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.norm_volterraOperator_le_one`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html#norm-volterra-operator-le-one).

## Pointwise factorial bound for powers of the Volterra operator

Let $V$ be the Volterra
operator $(Vf)(x) = \int_0^x f(t)\,dt$ on the space of bounded continuous real functions on
$[0, 1]$. For every natural number $n$, every such function $f$ and every $x \in [0, 1]$,
$|(V^n f)(x)| \le \frac{x^n}{n!} \|f\|_\infty$, where $\|f\|_\infty$ is the sup norm of $f$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.pow_volterraOperator_apply_norm_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html#pow-volterra-operator-apply-norm-le).

## Factorial bound for powers of the Volterra operator

Let $V$ be the Volterra operator
$(Vf)(x) = \int_0^x f(t)\,dt$ on the space of bounded continuous real functions on $[0, 1]$
with the sup norm. For every natural number $n$, the operator norm of $V^n$ satisfies
$\|V^n\| \le 1/n!$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.norm_volterraOperator_pow_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html#norm-volterra-operator-pow-le).

## Nonzero reals lie in the resolvent set of the Volterra operator

For every nonzero real
$z$, $z$ lies in the real resolvent set of the Volterra operator $V$: the bounded operator
$z - V$ is invertible.

The operator $z - V$ is bijective, with inverse given by the Neumann series
$g \mapsto \sum_{n \ge 0} z^{-(n+1)} V^n g$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.volterraOperator_mem_resolventSet_of_ne_zero`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html#volterra-operator-mem-resolvent-set-of-n).

## The Volterra operator is not invertible

The Volterra operator $V$,
$(Vf)(x) = \int_0^x f(t)\,dt$, on the space of bounded continuous real functions on $[0, 1]$ is
not a unit in the algebra of bounded linear operators on that space.

The reason is that $(Vf)(0) = 0$ for every $f$, so $V$ is not surjective.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.not_isUnit_volterraOperator`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html#not-is-unit-volterra-operator).

## The spectrum of the Volterra operator is `{0}`

**The spectrum of the Volterra operator is `{0}`.**

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.volterraOperator_spectrum`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html#volterra-operator-spectrum).

## The spectral radius of the Volterra operator is zero

Let $V$ be the Volterra operator
$(Vf)(x) = \int_0^x f(t)\,dt$ on the space of bounded continuous real functions on $[0, 1]$.
Its spectral radius over the real scalars, the supremum of $|z|$ over real $z$ in the spectrum
of $V$, is $0$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.VolterraOperator.spectralRadius_volterraOperator`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean, line 418](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/VolterraOperator.lean#L418). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html#spectral-radius-volterra-operator).

## Expansion of $(XV)^n$ in Bessel numbers

Let $X$ and $V$ be the operators on functions
$\mathbb{R} \to \mathbb{R}$ given by $(Xg)(y) = y \, g(y)$ and $(Vg)(y) = \int_0^y g(t) \, dt$,
write $(XV)^n$ and $V^m$ for iterated composition, and let $a(m, k)$ be the coefficient of $x^k$
in the Bessel polynomial $y_m$. For every natural number $n \ge 1$, every continuous function
$f : \mathbb{R} \to \mathbb{R}$ and every real number $x$,

$$(XV)^n f(x) = \sum_{k=0}^{n-1} (-1)^k \, a(n-1, k) \, x^{n-k} \, (V^{n+k} f)(x).$$

## Sources

- Abdelhay Benmoussa, *On the Expansion of `(XV)^n` and Bessel Numbers*, Journal of Integer Sequences 29 (2026), Article 26.3.5, Theorem 1 (`jis-2026-26.3.5-thm-1`).

Stated but not proved: `MetaMathlibExt.xMul_volterra_iterate_eq_sum_bessel` is written with `theorem_wanted` in [WantedExt/Analysis/OperatorTheory/VolterraBesselExpansionWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/OperatorTheory/VolterraBesselExpansionWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html#x-mul-volterra-iterate-eq-sum-bessel).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Volterra operator](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/integral-and-multiplication/volterra-operator)
