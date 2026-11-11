---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.RadonRiesz.tendsto_of_tendsto_inner_and_tendsto_norm, MathlibExt.Analysis.InnerProductSpace.RadonRiesz.tendsto_of_forall_tendsto_and_tendsto_norm, MathlibExt.Analysis.InnerProductSpace.RadonRiesz.tendsto_of_tendsto_weakSpace_and_tendsto_norm, MathlibExt.Analysis.InnerProductSpace.RadonRiesz.tendsto_iff_tendsto_inner_and_tendsto_norm
statement: formalized
proof: formalized
---

# Radon–Riesz property

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/radon-riesz-property/index.html).

## Radon–Riesz theorem, inner-product form

Let $H$ be an inner product space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, not necessarily complete, let
$(u_n)_{n \in \mathbb{N}}$ be a sequence in $H$ and let $x \in H$. If
$\langle u_n, y \rangle \to \langle x, y \rangle$ for every $y \in H$ and $\|u_n\| \to \|x\|$,
then $u_n \to x$ in norm.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RadonRiesz.tendsto_of_tendsto_inner_and_tendsto_norm`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RadonRiesz.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RadonRiesz.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/radon-riesz-property/index.html#tendsto-of-tendsto-inner-and-tendsto-nor).

## Radon–Riesz theorem, dual-functionals form

Let $H$ be an inner product space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, not necessarily complete, let
$(u_n)_{n \in \mathbb{N}}$ be a sequence in $H$ and let $x \in H$. If $f(u_n) \to f(x)$ for
every continuous linear functional $f : H \to \mathbb{K}$ and $\|u_n\| \to \|x\|$, then
$u_n \to x$ in norm.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RadonRiesz.tendsto_of_forall_tendsto_and_tendsto_norm`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RadonRiesz.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RadonRiesz.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/radon-riesz-property/index.html#tendsto-of-forall-tendsto-and-tendsto-no).

## Radon–Riesz theorem, weak-topology form

Let $H$ be an inner product space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, not necessarily complete, let
$(u_n)_{n \in \mathbb{N}}$ be a sequence in $H$ and let $x \in H$. If $u_n \to x$ in the weak
topology of $H$ (the coarsest topology making every continuous linear functional
$H \to \mathbb{K}$ continuous) and $\|u_n\| \to \|x\|$, then $u_n \to x$ in norm.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RadonRiesz.tendsto_of_tendsto_weakSpace_and_tendsto_norm`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RadonRiesz.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RadonRiesz.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/radon-riesz-property/index.html#tendsto-of-tendsto-weak-space-and-tendst).

## Radon–Riesz characterization of norm convergence

Let $H$ be an inner product space
over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, not necessarily complete, let
$(u_n)_{n \in \mathbb{N}}$ be a sequence in $H$ and let $x \in H$. Then $u_n \to x$ in norm if
and only if $\langle u_n, y \rangle \to \langle x, y \rangle$ for every $y \in H$ and
$\|u_n\| \to \|x\|$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RadonRiesz.tendsto_iff_tendsto_inner_and_tendsto_norm`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RadonRiesz.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RadonRiesz.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/radon-riesz-property/index.html#tendsto-iff-tendsto-inner-and-tendsto-no).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Radon–Riesz property](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/radon-riesz-property/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/hilbert-spaces/radon-riesz-property)
