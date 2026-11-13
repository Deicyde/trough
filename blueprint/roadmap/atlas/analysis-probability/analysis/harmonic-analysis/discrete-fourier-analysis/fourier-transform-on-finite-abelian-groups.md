---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Fourier.FiniteAbelianDFTWanted.dftFun, MathlibExt.Analysis.Fourier.FiniteAbelianDFTWanted.dft_inversion, MathlibExt.Analysis.Fourier.FiniteAbelianDFTWanted.dft_plancherel, MathlibExt.Analysis.Fourier.FiniteAbelianDFTWanted.dftFun_translate
statement: formalized
proof: formalized
---

# Fourier transform on finite abelian groups

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-transform-on-finite-abelian-groups/index.html).

## Discrete Fourier transform on a finite abelian group

Let $G$ be a finite abelian group and
$f : G \to \mathbb{C}$. The discrete Fourier transform of $f$ is the function on the additive
characters $\psi$ of $G$ with values in $\mathbb{C}$ (maps with $\psi(0) = 1$ and
$\psi(a + b) = \psi(a)\psi(b)$) given by $\hat f(\psi) = \sum_{x \in G} \psi(x) f(x)$.

No complex conjugate is applied to the character.

Formalized by `MathlibExt.Analysis.Fourier.FiniteAbelianDFTWanted.dftFun`, a definition declared in [MathlibExt/Analysis/Fourier/FiniteAbelianDFT.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/FiniteAbelianDFT.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-transform-on-finite-abelian-groups/index.html#dft-fun).

## Fourier inversion on a finite abelian group

Let $G$ be a finite abelian group with $|G|$
elements, let $f : G \to \mathbb{C}$, and write $\hat f(\psi) = \sum_{y \in G} \psi(y) f(y)$ for
the discrete Fourier transform of $f$ at an additive character $\psi$ of $G$ with values in
$\mathbb{C}$. Then for every $x \in G$,
$f(x) = \frac{1}{|G|} \sum_{\psi} \overline{\psi(x)} \, \hat f(\psi)$, where $\psi$ runs over
all additive characters of $G$ with values in $\mathbb{C}$.

Proof: expand the transform and collapse the inner sum with the orthogonality of characters.
This is the Fourier inversion formula (4.4) of K. Conrad, Characters of finite abelian groups,
Section 4, https://kconrad.math.uconn.edu/blurbs/grouptheory/charthy.pdf, up to reindexing
$\psi \mapsto \psi^{-1}$ (Conrad conjugates the character in the transform rather than in the
inversion sum).

## Sources

- A. Terras, Fourier Analysis on Finite Groups and Applications, Ch. 2, Fourier inversion theorem.

Formalized by `MathlibExt.Analysis.Fourier.FiniteAbelianDFTWanted.dft_inversion`, a theorem declared in [MathlibExt/Analysis/Fourier/FiniteAbelianDFT.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/FiniteAbelianDFT.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-transform-on-finite-abelian-groups/index.html#dft-inversion).

## Plancherel formula on a finite abelian group

Let $G$ be a finite abelian group with $|G|$
elements, let $f, g : G \to \mathbb{C}$, and write $\hat h(\psi) = \sum_{x \in G} \psi(x) h(x)$
for the discrete Fourier transform of $h : G \to \mathbb{C}$ at an additive character $\psi$ of
$G$ with values in $\mathbb{C}$. Then $\sum_{x \in G} \overline{f(x)} \, g(x)$ equals
$\frac{1}{|G|} \sum_{\psi} \overline{\hat f(\psi)} \, \hat g(\psi)$, where $\psi$ runs over all
additive characters of $G$ with values in $\mathbb{C}$.

Proof: apply Fourier inversion to $g$, exchange the finite sums, and identify the conjugated
inner sum with $\overline{\hat f(\psi)}$. K. Conrad, Characters of finite abelian groups,
Section 4, proves the same identity by checking it on characters.

## Sources

- A. Terras, Fourier Analysis on Finite Groups and Applications, Ch. 2, Plancherel formula.

Formalized by `MathlibExt.Analysis.Fourier.FiniteAbelianDFTWanted.dft_plancherel`, a theorem declared in [MathlibExt/Analysis/Fourier/FiniteAbelianDFT.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/FiniteAbelianDFT.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-transform-on-finite-abelian-groups/index.html#dft-plancherel).

## Translation modulates the discrete Fourier transform

Let $G$ be a finite abelian group,
$f : G \to \mathbb{C}$, $t \in G$, and $\psi$ an additive character of $G$ with values in
$\mathbb{C}$, and write $\hat h(\psi) = \sum_{x \in G} \psi(x) h(x)$ for the discrete Fourier
transform of $h : G \to \mathbb{C}$. If $g(x) = f(x - t)$ for all $x \in G$, then
$\hat g(\psi) = \psi(t) \hat f(\psi)$.

Proof: reindex the finite sum by $x \mapsto x + t$ and use $\psi(x + t) = \psi(x) \psi(t)$.

## Sources

- A. Terras, Fourier Analysis on Finite Groups and Applications, Ch. 2 (translation and modulation).

Formalized by `MathlibExt.Analysis.Fourier.FiniteAbelianDFTWanted.dftFun_translate`, a theorem declared in [MathlibExt/Analysis/Fourier/FiniteAbelianDFT.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/FiniteAbelianDFT.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-transform-on-finite-abelian-groups/index.html#dft-fun-translate).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fourier transform on finite abelian groups](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-transform-on-finite-abelian-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-transform-on-finite-abelian-groups)
