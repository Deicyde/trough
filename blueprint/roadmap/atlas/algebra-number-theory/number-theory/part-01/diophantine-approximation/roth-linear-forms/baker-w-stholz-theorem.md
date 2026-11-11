---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.BakerWustholzWanted.BakerWustholz.C, MathlibExt.NumberTheory.BakerWustholzWanted.BakerWustholz.modifiedHeight, MathlibExt.NumberTheory.BakerWustholzWanted.bakerWustholz_linearForms_logs
statement: formalized
---

# Baker–Wüstholz theorem

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/baker-w-stholz-theorem/index.html).

## Baker Wustholz

## The Baker–Wüstholz constant

For natural numbers $n$ and $d$, the Baker–Wüstholz constant
is the real number
$C(n, d) = 18 \cdot (n + 1)! \cdot n^{n+1} \cdot (32 d)^{n+2} \cdot \log(2nd)$.

Formalized by `MathlibExt.NumberTheory.BakerWustholzWanted.BakerWustholz.C`, a definition declared in [WantedExt/NumberTheory/BakerWustholzWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BakerWustholzWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/baker-w-stholz-theorem/index.html#c).

## Modified height

Let $K$ be a number field of degree $d = [K : \mathbb{Q}]$ and let
$\varphi : K \to \mathbb{C}$ be a ring homomorphism. For $\alpha \in K$, the modified height of
$\alpha$ with respect to $\varphi$ is

$$h'(\alpha) = \max\left(h(\alpha), \frac{|\log \varphi(\alpha)|}{d}, \frac{1}{d}\right),$$

where $\log$ is the principal branch of the complex logarithm (with $\log 0 = 0$) and $h(\alpha)$
is the absolute logarithmic Weil height of $\alpha$: $\frac{1}{d}$ times the sum of
$\log \max(1, |\alpha|_v)$ over the places $v$ of $K$, with the absolute values normalized so that
the product formula holds and each complex place counted twice.

Formalized by `MathlibExt.NumberTheory.BakerWustholzWanted.BakerWustholz.modifiedHeight`, a definition declared in [WantedExt/NumberTheory/BakerWustholzWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BakerWustholzWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/baker-w-stholz-theorem/index.html#modified-height).

## Baker–Wüstholz theorem on linear forms in logarithms

Let $n \ge 1$, let $K$ be a number
field of degree $d = [K : \mathbb{Q}]$, let $\varphi : K \to \mathbb{C}$ be a ring homomorphism,
and let $\alpha_1, \dots, \alpha_n$ be nonzero elements of $K$. Let $b_1, \dots, b_n$ be integers
and let $B \ge 2$ be a natural number with $|b_i| \le B$ for every $i$. With $\log$ the principal
branch of the complex logarithm, suppose that $\Lambda = \sum_{i=1}^n b_i \log \varphi(\alpha_i)$
is nonzero. Then

$$\log |\Lambda| \ge -C(n, d) \max\left(\log B, \frac{1}{d}\right) \prod_{i=1}^n h'(\alpha_i),$$

where $C(n, d)$ is the Baker–Wüstholz constant and $h'$ is the modified height with respect to
$\varphi$.

## Sources

- A. Baker, G. Wüstholz, Logarithmic forms and group varieties, J. reine angew. Math. 442 (1993), 19-62. Problem `bakerWustholz_linearForms_logs` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.BakerWustholzWanted.bakerWustholz_linearForms_logs` is written with `theorem_wanted` in [WantedExt/NumberTheory/BakerWustholzWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BakerWustholzWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/baker-w-stholz-theorem/index.html#baker-wustholz-linear-forms-logs).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Baker–Wüstholz theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/baker-w-stholz-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/baker-w-stholz-theorem)
