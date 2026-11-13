---
declaration: section
origin: cited
lean: TorusSobolev.OneLogBound, TorusSobolev.DoubleLogBound, TorusSobolev.oneLogLeadingCoefficientInfimum
statement: formalized
proof: formalized
---

# One-log and double-log bounds on actual torus functions

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/one-log-and-double-log-bounds-on-actual-torus-fu/index.html).

## One-log bound with coefficient $c$ and constant $K$

For real numbers $c$ and $K$, the
one-log bound holds when every continuous function $u : \mathbb{T} \to \mathbb{R}$ on the torus
$\mathbb{T} = (\mathbb{R}/2\pi\mathbb{Z})^2$ that is a zero-mean $H^2$ function, has gradient energy
$E(u) > 0$ and has frequency ratio $\delta(u) \ge 1$ (the Laplacian energy divided by $E(u)$)
satisfies, at every point $x \in \mathbb{T}$,

$$u(x)^2 \le c\,E(u)\bigl(\log\delta(u) + K\bigr).$$

Formalized by `TorusSobolev.OneLogBound`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/LogarithmicBounds.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/TorusSobolev/LogarithmicBounds.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/one-log-and-double-log-bounds-on-actual-torus-fu/index.html#one-log-bound).

## Double-log bound with coefficient $a$ and constant $L$

For real numbers $a$ and $L$, the
double-log bound holds when every continuous function $u : \mathbb{T} \to \mathbb{R}$ on the torus
$\mathbb{T} = (\mathbb{R}/2\pi\mathbb{Z})^2$ that is a zero-mean $H^2$ function, has gradient energy
$E(u) > 0$ and has frequency ratio $\delta(u) \ge 1$ (the Laplacian energy divided by $E(u)$)
satisfies, at every point $x \in \mathbb{T}$,

$$u(x)^2 \le \frac{E(u)}{4\pi}\bigl(\log\delta(u) + a\log\bigl(1 + \log\delta(u)\bigr) + L\bigr).$$

The inner logarithm is taken of $1 + \log\delta(u)$, which is at least $1$ because
$\delta(u) \ge 1$.

Formalized by `TorusSobolev.DoubleLogBound`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/LogarithmicBounds.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/TorusSobolev/LogarithmicBounds.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/one-log-and-double-log-bounds-on-actual-torus-fu/index.html#double-log-bound).

## Optimal one-log coefficient

The infimum, taken in the extended reals, of all real
numbers $c$ for which there is a real constant $K$ such that the one-log bound with
coefficient $c$ and constant $K$ holds. It is $+\infty$ when no such $c$ exists.

Formalized by `TorusSobolev.oneLogLeadingCoefficientInfimum`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/LogarithmicBounds.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/TorusSobolev/LogarithmicBounds.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/one-log-and-double-log-bounds-on-actual-torus-fu/index.html#one-log-leading-coefficient-infimum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: One-log and double-log bounds on actual torus functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/one-log-and-double-log-bounds-on-actual-torus-fu/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/one-log-and-double-log-bounds-on-actual-torus-fu)
