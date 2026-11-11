---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Fourier.finGroupConv, MathlibExt.Analysis.Fourier.finGroupConv_comm, MathlibExt.Analysis.Fourier.finGroupConv_assoc, MathlibExt.Analysis.Fourier.finGroupConv_delta_left, MathlibExt.Analysis.Fourier.young_convolution_finite_group
statement: formalized
proof: formalized
---

# Young's convolution inequality on finite groups

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/young-s-convolution-inequality-on-finite-groups/index.html).

## Convolution on a finite abelian group

Let $G$ be a finite abelian group. The
convolution of functions $f, g : G \to \mathbb{C}$ is the function $f * g : G \to \mathbb{C}$
given by $(f * g)(x) = \sum_{y \in G} f(y)\,g(x - y)$, with no normalizing factor $1/|G|$,
where $|G|$ is the number of elements of $G$.

Formalized by `MathlibExt.Analysis.Fourier.finGroupConv`, a definition declared in [MathlibExt/Analysis/Fourier/FiniteGroupYoung.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FiniteGroupYoung.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/young-s-convolution-inequality-on-finite-groups/index.html#fin-group-conv).

## Convolution on a finite abelian group is commutative

For a finite abelian group $G$
and functions $f, g : G \to \mathbb{C}$, we have $f * g = g * f$, where the convolution is
$(f * g)(x) = \sum_{y \in G} f(y)\,g(x - y)$.

Formalized by `MathlibExt.Analysis.Fourier.finGroupConv_comm`, a theorem declared in [MathlibExt/Analysis/Fourier/FiniteGroupYoung.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FiniteGroupYoung.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/young-s-convolution-inequality-on-finite-groups/index.html#fin-group-conv-comm).

## Convolution on a finite abelian group is associative

For a finite abelian group $G$
and functions $f, g, h : G \to \mathbb{C}$, we have $(f * g) * h = f * (g * h)$, where the
convolution is $(f * g)(x) = \sum_{y \in G} f(y)\,g(x - y)$.

Formalized by `MathlibExt.Analysis.Fourier.finGroupConv_assoc`, a theorem declared in [MathlibExt/Analysis/Fourier/FiniteGroupYoung.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FiniteGroupYoung.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/young-s-convolution-inequality-on-finite-groups/index.html#fin-group-conv-assoc).

## The delta function is a left identity for convolution

Let $G$ be a finite abelian
group and let $\delta_0 : G \to \mathbb{C}$ be the function with $\delta_0(0) = 1$ and
$\delta_0(y) = 0$ for $y \ne 0$. Then $\delta_0 * g = g$ for every $g : G \to \mathbb{C}$,
where the convolution is $(f * g)(x) = \sum_{y \in G} f(y)\,g(x - y)$.

Formalized by `MathlibExt.Analysis.Fourier.finGroupConv_delta_left`, a theorem declared in [MathlibExt/Analysis/Fourier/FiniteGroupYoung.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FiniteGroupYoung.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/young-s-convolution-inequality-on-finite-groups/index.html#fin-group-conv-delta-left).

## Young's convolution inequality on a finite abelian group

Let $G$ be a finite abelian
group and, for $u : G \to \mathbb{C}$ and real $s > 0$, write
$\|u\|_s = \left(\sum_{x \in G} |u(x)|^s\right)^{1/s}$. Let $f, g : G \to \mathbb{C}$ and let
$p, q, r$ be real numbers with $p > 1$, $q > 1$, $r > 1$ and $1/p + 1/q = 1 + 1/r$. Then the
convolution $(f * g)(x) = \sum_{y \in G} f(y)\,g(x - y)$ satisfies
$\|f * g\|_r \le \|f\|_p \, \|g\|_q$.

Formalized by `MathlibExt.Analysis.Fourier.young_convolution_finite_group`, a theorem declared in [MathlibExt/Analysis/Fourier/FiniteGroupYoung.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FiniteGroupYoung.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/young-s-convolution-inequality-on-finite-groups/index.html#young-convolution-finite-group).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Young's convolution inequality on finite groups](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/young-s-convolution-inequality-on-finite-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/young-s-convolution-inequality-on-finite-groups)
