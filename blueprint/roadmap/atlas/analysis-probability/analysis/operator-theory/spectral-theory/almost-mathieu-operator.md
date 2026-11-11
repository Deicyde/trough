---
declaration: section
origin: cited
lean: MathlibExt.Analysis.TenMartiniWanted.Analysis.TenMartini.EllTwo, MathlibExt.Analysis.TenMartiniWanted.Analysis.TenMartini.IsAlmostMathieuOperator, MathlibExt.Analysis.TenMartiniWanted.Analysis.TenMartini.ten_martini_problem
statement: formalized
---

# Almost Mathieu operator

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/almost-mathieu-operator/index.html).

## The sequence space $\ell^2(\mathbb{Z})$

We write $\ell^2(\mathbb{Z})$ for the Hilbert
space of square-summable sequences $(u_n)_{n \in \mathbb{Z}}$ of complex numbers.

Formalized by `MathlibExt.Analysis.TenMartiniWanted.Analysis.TenMartini.EllTwo`, an abbreviation declared in [WantedExt/Analysis/TenMartiniWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/TenMartiniWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/almost-mathieu-operator/index.html#ell-two).

## Almost Mathieu operator

Let $\alpha$, $\lambda$ and $\theta$ be real numbers. A bounded
complex-linear operator $H$ on $\ell^2(\mathbb{Z})$ is an almost Mathieu operator with frequency
$\alpha$, coupling $\lambda$ and phase $\theta$ when, for every $u \in \ell^2(\mathbb{Z})$ and
every $n \in \mathbb{Z}$,

$$(Hu)(n) = u(n+1) + u(n-1) + 2\lambda \cos(2\pi(\theta + n\alpha))\, u(n).$$

Formalized by `MathlibExt.Analysis.TenMartiniWanted.Analysis.TenMartini.IsAlmostMathieuOperator`, a definition declared in [WantedExt/Analysis/TenMartiniWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/TenMartiniWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/almost-mathieu-operator/index.html#is-almost-mathieu-operator).

## Ten Martini theorem (Avila–Jitomirskaya)

Let $\alpha$, $\lambda$ and $\theta$ be real
numbers with $\alpha$ irrational and $\lambda \neq 0$. Then there is an almost Mathieu operator $H$
on $\ell^2(\mathbb{Z})$ with frequency $\alpha$, coupling $\lambda$ and phase $\theta$, and the
spectrum of $H$ is nonempty, compact, perfect and totally disconnected, that is, a Cantor set.

## Sources

- A. Avila and S. Jitomirskaya, 'The Ten Martini Problem', Ann. of Math. 170 (2009), 303-342, https://doi.org/10.4007/annals.2009.170.303. Problem `ten_martini_problem` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.TenMartiniWanted.Analysis.TenMartini.ten_martini_problem` is written with `theorem_wanted` in [WantedExt/Analysis/TenMartiniWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/TenMartiniWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/almost-mathieu-operator/index.html#ten-martini-problem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Almost Mathieu operator](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/almost-mathieu-operator/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/spectral-theory/almost-mathieu-operator)
