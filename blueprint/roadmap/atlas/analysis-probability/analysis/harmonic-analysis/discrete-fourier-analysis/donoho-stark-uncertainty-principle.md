---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Fourier.FiniteAbelianUncertainty.norm_addChar_apply, MathlibExt.Analysis.Fourier.FiniteAbelianUncertainty.sum_norm_sq_dftFun, MathlibExt.Analysis.Fourier.FiniteAbelianUncertainty.norm_sq_le_of_dftFun_eq_zero_of_notMem, MathlibExt.Analysis.Fourier.FiniteAbelianUncertainty.sum_norm_sq_le_of_dftFun_eq_zero_of_notMem, MathlibExt.Analysis.Fourier.FiniteAbelianUncertainty.sum_norm_sq_dftFun_le_of_eq_zero_of_notMem, MathlibExt.Analysis.Fourier.FiniteAbelianUncertainty.card_le_mul_card_filter_support, MathlibExt.Analysis.Fourier.FiniteAbelianUncertainty.eq_zero_of_card_mul_card_lt_card
statement: formalized
proof: formalized
---

# Donoho–Stark uncertainty principle

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/donoho-stark-uncertainty-principle/index.html).

## Characters of a finite abelian group have absolute value one

Let $G$ be a finite abelian
group and let $\psi$ be an additive character of $G$ with values in $\mathbb{C}$, that is, a map
$\psi : G \to \mathbb{C}$ with $\psi(0) = 1$ and $\psi(a + b) = \psi(a)\psi(b)$. Then
$|\psi(x)| = 1$ for every $x \in G$.

Formalized by `MathlibExt.Analysis.Fourier.FiniteAbelianUncertainty.norm_addChar_apply`, a theorem declared in [MathlibExt/Analysis/Fourier/FiniteAbelianUncertainty.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FiniteAbelianUncertainty.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/donoho-stark-uncertainty-principle/index.html#norm-add-char-apply).

## Squared-norm Plancherel identity for the finite Fourier transform

Let $G$ be a finite
abelian group and $f : G \to \mathbb{C}$, with discrete Fourier transform $\hat f$. Then
$\sum_{\psi} |\hat f(\psi)|^2 = |G| \sum_{x \in G} |f(x)|^2$, where $\psi$ runs over all
additive characters of $G$.

Formalized by `MathlibExt.Analysis.Fourier.FiniteAbelianUncertainty.sum_norm_sq_dftFun`, a theorem declared in [MathlibExt/Analysis/Fourier/FiniteAbelianUncertainty.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FiniteAbelianUncertainty.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/donoho-stark-uncertainty-principle/index.html#sum-norm-sq-dft-fun).

## Pointwise bound from a small Fourier support

Let $G$ be a finite abelian group, let
$f : G \to \mathbb{C}$, and let $B$ be a set of additive characters of $G$ such that the discrete
Fourier transform $\hat f$ vanishes outside $B$. Then for every $x \in G$,
$|f(x)|^2 \le \frac{|B|}{|G|} \sum_{y \in G} |f(y)|^2$.

Formalized by `MathlibExt.Analysis.Fourier.FiniteAbelianUncertainty.norm_sq_le_of_dftFun_eq_zero_of_notMem`, a theorem declared in [MathlibExt/Analysis/Fourier/FiniteAbelianUncertainty.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FiniteAbelianUncertainty.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/donoho-stark-uncertainty-principle/index.html#norm-sq-le-of-dft-fun-eq-zero-of-not-mem).

## Concentration bound for a function with small Fourier support

Let $G$ be a finite abelian
group, let $f : G \to \mathbb{C}$, and let $B$ be a set of additive characters of $G$ such that
the discrete Fourier transform $\hat f$ vanishes outside $B$. Then for every $A \subseteq G$,
$\sum_{x \in A} |f(x)|^2 \le \frac{|A| \cdot |B|}{|G|} \sum_{x \in G} |f(x)|^2$.

Formalized by `MathlibExt.Analysis.Fourier.FiniteAbelianUncertainty.sum_norm_sq_le_of_dftFun_eq_zero_of_notMem`, a theorem declared in [MathlibExt/Analysis/Fourier/FiniteAbelianUncertainty.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FiniteAbelianUncertainty.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/donoho-stark-uncertainty-principle/index.html#sum-norm-sq-le-of-dft-fun-eq-zero-of-not).

## Concentration bound for the Fourier transform of a function with small support

Let $G$
be a finite abelian group, let $A \subseteq G$, let $B$ be any set of additive characters of $G$,
and let $f : G \to \mathbb{C}$ vanish outside $A$, with discrete Fourier transform $\hat f$. Then
$\sum_{\psi \in B} |\hat f(\psi)|^2 \le \frac{|A| \cdot |B|}{|G|} \sum_{\psi} |\hat f(\psi)|^2$,
where the last sum runs over all additive characters $\psi$ of $G$.

Formalized by `MathlibExt.Analysis.Fourier.FiniteAbelianUncertainty.sum_norm_sq_dftFun_le_of_eq_zero_of_notMem`, a theorem declared in [MathlibExt/Analysis/Fourier/FiniteAbelianUncertainty.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FiniteAbelianUncertainty.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/donoho-stark-uncertainty-principle/index.html#sum-norm-sq-dft-fun-le-of-eq-zero-of-not).

## Donoho–Stark uncertainty principle

Let $G$ be a finite abelian group and let
$f : G \to \mathbb{C}$ be a nonzero function with discrete Fourier transform $\hat f$. Then
$|G| \le |\{x \in G : f(x) \neq 0\}| \cdot |\{\psi : \hat f(\psi) \neq 0\}|$, where $\psi$ ranges
over the additive characters of $G$.

Formalized by `MathlibExt.Analysis.Fourier.FiniteAbelianUncertainty.card_le_mul_card_filter_support`, a theorem declared in [MathlibExt/Analysis/Fourier/FiniteAbelianUncertainty.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FiniteAbelianUncertainty.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/donoho-stark-uncertainty-principle/index.html#card-le-mul-card-filter-support).

## Functions with small support and small Fourier support vanish

Let $G$ be a finite abelian
group, let $A \subseteq G$, and let $B$ be a set of additive characters of $G$ with
$|A| \cdot |B| < |G|$. If $f : G \to \mathbb{C}$ vanishes outside $A$ and its discrete Fourier
transform $\hat f$ vanishes outside $B$, then $f = 0$.

Formalized by `MathlibExt.Analysis.Fourier.FiniteAbelianUncertainty.eq_zero_of_card_mul_card_lt_card`, a theorem declared in [MathlibExt/Analysis/Fourier/FiniteAbelianUncertainty.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FiniteAbelianUncertainty.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/donoho-stark-uncertainty-principle/index.html#eq-zero-of-card-mul-card-lt-card).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Donoho–Stark uncertainty principle](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/donoho-stark-uncertainty-principle/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/donoho-stark-uncertainty-principle)
