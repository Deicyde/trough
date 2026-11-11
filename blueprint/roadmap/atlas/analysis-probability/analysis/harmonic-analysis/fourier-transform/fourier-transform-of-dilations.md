---
declaration: section
origin: cited
lean: Real.fourier_comp_mul_left, Real.fourier_comp_mul_left_of_pos, SchwartzMap.fourier_coe_comp_mul_left_of_pos
statement: formalized
proof: formalized
---

# Fourier transform of dilations

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-transform-of-dilations/index.html).

## Dilations

## Fourier transform of a dilation

Let $E$ be a complex normed space, and write
$\hat g(y) = \int_{\mathbb{R}} e^{-2\pi i x y} g(x)\,dx$ for the Fourier transform of a
function $g : \mathbb{R} \to E$. For every $f : \mathbb{R} \to E$, every real $a \ne 0$ and
every real $y$, the Fourier transform of $x \mapsto f(ax)$ at $y$ equals $|a|^{-1} \hat f(y/a)$.

No integrability hypothesis is needed because Mathlib's Bochner integral is
totalized, so the identity also uses that convention for nonintegrable
functions.

Formalized by `Real.fourier_comp_mul_left`, a theorem declared in [MathlibExt/Analysis/Fourier/Scaling.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/Scaling.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-transform-of-dilations/index.html#fourier-comp-mul-left).

## Fourier transform of a dilation by a positive factor

Write
$\hat g(y) = \int_{\mathbb{R}} e^{-2\pi i x y} g(x)\,dx$ for the Fourier transform of a
function $g : \mathbb{R} \to \mathbb{C}$. For every $f : \mathbb{R} \to \mathbb{C}$, every real
$a > 0$ and every real $y$, the Fourier transform of $x \mapsto f(ax)$ at $y$ equals
$a^{-1} \hat f(y/a)$.

No integrability hypothesis is needed because Mathlib's Bochner integral is
totalized, so the identity also uses that convention for nonintegrable
functions.

Formalized by `Real.fourier_comp_mul_left_of_pos`, a theorem declared in [MathlibExt/Analysis/Fourier/Scaling.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/Scaling.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-transform-of-dilations/index.html#fourier-comp-mul-left-of-pos).

## Fourier transform of a dilated Schwartz function

Write
$\hat g(y) = \int_{\mathbb{R}} e^{-2\pi i x y} g(x)\,dx$ for the Fourier transform of a
function $g : \mathbb{R} \to \mathbb{C}$. For every Schwartz function
$f : \mathbb{R} \to \mathbb{C}$, every real $a > 0$ and every real $y$, the Fourier transform of
$x \mapsto f(ax)$ at $y$ equals $a^{-1} \hat f(y/a)$.

Formalized by `SchwartzMap.fourier_coe_comp_mul_left_of_pos`, a theorem declared in [MathlibExt/Analysis/Fourier/Scaling.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/Scaling.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-transform-of-dilations/index.html#fourier-coe-comp-mul-left-of-pos).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fourier transform of dilations](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-transform-of-dilations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-transform-of-dilations)
