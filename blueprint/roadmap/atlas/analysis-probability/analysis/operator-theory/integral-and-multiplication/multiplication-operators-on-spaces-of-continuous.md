---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.MultiplicationOperator.mulCLM, MathlibExt.Analysis.FunctionalAnalysis.MultiplicationOperator.mulCLM_algebraMap, MathlibExt.Analysis.FunctionalAnalysis.MultiplicationOperator.spectrum_mulCLM, MathlibExt.Analysis.FunctionalAnalysis.MultiplicationOperator.isUnit_mulCLM_iff, MathlibExt.Analysis.FunctionalAnalysis.MultiplicationOperator.hasEigenvalue_mulCLM_iff
statement: formalized
proof: formalized
---

# Multiplication operators on spaces of continuous functions

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-spaces-of-continuous/index.html).

## The multiplication operator on continuous functions

Let $X$ be a compact topological
space, let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, and let $C(X, \mathbb{K})$ be the Banach
algebra of continuous functions $X \to \mathbb{K}$ with the supremum norm. For
$\varphi \in C(X, \mathbb{K})$, the multiplication operator $M_\varphi$ is the bounded linear
operator on $C(X, \mathbb{K})$ given by $M_\varphi f = \varphi f$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.MultiplicationOperator.mulCLM`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/MultiplicationOperator.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/MultiplicationOperator.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-spaces-of-continuous/index.html#mul-clm).

## Multiplication by a constant on continuous functions

Let $X$ be a compact topological
space, let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, and let $\mu \in \mathbb{K}$. The
multiplication operator on $C(X, \mathbb{K})$ by the constant function with value $\mu$ equals
$\mu$ times the identity operator.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.MultiplicationOperator.mulCLM_algebraMap`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/MultiplicationOperator.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/MultiplicationOperator.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-spaces-of-continuous/index.html#mul-clm-algebra-map).

## Spectrum of a multiplication operator

Let $X$ be a compact topological space, let
$\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, and let $\varphi \in C(X, \mathbb{K})$. The spectrum
of the multiplication operator $M_\varphi f = \varphi f$, as an element of the algebra of bounded
linear operators on $C(X, \mathbb{K})$, is the range $\varphi(X)$ of $\varphi$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.MultiplicationOperator.spectrum_mulCLM`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/MultiplicationOperator.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/MultiplicationOperator.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-spaces-of-continuous/index.html#spectrum-mul-clm).

## Invertibility of a multiplication operator

Let $X$ be a compact topological space, let
$\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, and let $\varphi \in C(X, \mathbb{K})$. The
multiplication operator $M_\varphi f = \varphi f$ is invertible in the algebra of bounded linear
operators on $C(X, \mathbb{K})$ if and only if $\varphi(x) \neq 0$ for every $x \in X$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.MultiplicationOperator.isUnit_mulCLM_iff`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/MultiplicationOperator.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/MultiplicationOperator.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-spaces-of-continuous/index.html#is-unit-mul-clm-iff).

## Eigenvalues of a multiplication operator

Let $X$ be a compact Hausdorff space, let
$\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, let $\varphi \in C(X, \mathbb{K})$ and let
$\mu \in \mathbb{K}$. Then $\mu$ is an eigenvalue of the multiplication operator
$M_\varphi f = \varphi f$ on $C(X, \mathbb{K})$ if and only if the level set
$\varphi^{-1}(\{\mu\})$ has nonempty interior.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.MultiplicationOperator.hasEigenvalue_mulCLM_iff`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/MultiplicationOperator.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/MultiplicationOperator.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-spaces-of-continuous/index.html#has-eigenvalue-mul-clm-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multiplication operators on spaces of continuous functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-spaces-of-continuous/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/integral-and-multiplication/multiplication-operators-on-spaces-of-continuous)
