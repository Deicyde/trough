---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Fourier.HausdorffYoungFiniteAbelian.dftFun_sup_le, MathlibExt.Analysis.Fourier.HausdorffYoungFiniteAbelian.sum_norm_sq_dftFun, MathlibExt.Analysis.Fourier.HausdorffYoungFiniteAbelian.hausdorffYoung_dft
statement: formalized
proof: formalized
---

# Hausdorff–Young inequality on finite abelian groups

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/hausdorff-young-inequality-on-finite-abelian-gro/index.html).

## The $p = 1$ endpoint of Hausdorff–Young

Let $G$ be a finite abelian group and
$f : G \to \mathbb{C}$, with discrete Fourier transform $\hat f$. For every additive character
$\psi$ of $G$, $|\hat f(\psi)| \le \sum_{x \in G} |f(x)|$.

Formalized by `MathlibExt.Analysis.Fourier.HausdorffYoungFiniteAbelian.dftFun_sup_le`, a theorem declared in [MathlibExt/Analysis/Fourier/HausdorffYoungFiniteAbelian.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/HausdorffYoungFiniteAbelian.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/hausdorff-young-inequality-on-finite-abelian-gro/index.html#dft-fun-sup-le).

## The $p = 2$ endpoint of Hausdorff–Young (Plancherel)

Let $G$ be a finite abelian
group and let $f : G \to \mathbb{C}$ have discrete Fourier transform $\hat f$. Then, with
$\psi$ running over the additive characters of $G$ and $|G|$ the number of elements of $G$,
$\sum_{\psi} |\hat f(\psi)|^2 = |G| \sum_{x \in G} |f(x)|^2$.

Formalized by `MathlibExt.Analysis.Fourier.HausdorffYoungFiniteAbelian.sum_norm_sq_dftFun`, a theorem declared in [MathlibExt/Analysis/Fourier/HausdorffYoungFiniteAbelian.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/HausdorffYoungFiniteAbelian.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/hausdorff-young-inequality-on-finite-abelian-gro/index.html#sum-norm-sq-dft-fun).

## Hausdorff–Young inequality on a finite abelian group

Let $G$ be a finite abelian
group, let $f : G \to \mathbb{C}$ have discrete Fourier transform $\hat f$, let $p$ be a real
number with $1 < p \le 2$, and let $q = p/(p - 1)$. Write $|G|$ for the number of elements
of $G$ and let $\psi$ run over the additive characters of $G$. Then
$\left(\sum_{\psi} |\hat f(\psi)|^q\right)^{1/q} \le
|G|^{1/q} \left(\sum_{x \in G} |f(x)|^p\right)^{1/p}$.

The statement also assumes $\sigma$-algebras on $G$ and on its character group in which
singletons are measurable; on a finite set such a $\sigma$-algebra contains every subset, so
this is no restriction.

Formalized by `MathlibExt.Analysis.Fourier.HausdorffYoungFiniteAbelian.hausdorffYoung_dft`, a theorem declared in [MathlibExt/Analysis/Fourier/HausdorffYoungFiniteAbelian.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/HausdorffYoungFiniteAbelian.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/hausdorff-young-inequality-on-finite-abelian-gro/index.html#hausdorff-young-dft).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hausdorff–Young inequality on finite abelian groups](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/hausdorff-young-inequality-on-finite-abelian-gro/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/hausdorff-young-inequality-on-finite-abelian-gro)
