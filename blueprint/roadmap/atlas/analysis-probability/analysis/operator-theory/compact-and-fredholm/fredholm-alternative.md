---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointFredholmAlternative.ker_smul_id_sub_eq_eigenspace, MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointFredholmAlternative.fredholm_alternative_of_isCompactOperator_isSelfAdjoint, MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointFredholmAlternative.isClosed_range_smul_id_sub_of_isCompactOperator_isSelfAdjoint, MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointFredholmAlternative.fredholm_alternative_sub_of_isCompactOperator_isSelfAdjoint
statement: formalized
proof: formalized
---

# Fredholm alternative

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/fredholm-alternative/index.html).

## The kernel of a scalar minus an operator is an eigenspace

Let $H$ be an inner product
space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $T$ be a bounded linear operator on $H$,
let $I$ be the identity of $H$, and let $\mu \in \mathbb{K}$. Then the kernel of $\mu I - T$
equals the eigenspace $\{x \in H : T x = \mu x\}$ of $T$ for $\mu$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointFredholmAlternative.ker_smul_id_sub_eq_eigenspace`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointFredholmAlternative.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointFredholmAlternative.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/fredholm-alternative/index.html#ker-smul-id-sub-eq-eigenspace).

## Fredholm alternative for compact self-adjoint operators

Let $H$ be a Hilbert space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $T$ be a compact self-adjoint bounded operator on
$H$, let $I$ be the identity of $H$, and let $\mu \in \mathbb{K}$ with $\mu \neq 0$. Then the range
of $\mu I - T$ equals the orthogonal complement $(\ker(\mu I - T))^\perp$ of its kernel, and either
$\mu I - T$ is bijective, or its kernel is nonzero and finite-dimensional.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointFredholmAlternative.fredholm_alternative_of_isCompactOperator_isSelfAdjoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointFredholmAlternative.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointFredholmAlternative.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/fredholm-alternative/index.html#fredholm-alternative-of-is-compact-opera).

## Closed range for compact self-adjoint perturbations of nonzero scalars

Let $H$ be a
Hilbert space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $T$ be a compact self-adjoint
bounded operator on $H$, let $I$ be the identity of $H$, and let $\mu \in \mathbb{K}$ with
$\mu \neq 0$. Then the range of $\mu I - T$ is a closed subset of $H$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointFredholmAlternative.isClosed_range_smul_id_sub_of_isCompactOperator_isSelfAdjoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointFredholmAlternative.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointFredholmAlternative.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/fredholm-alternative/index.html#is-closed-range-smul-id-sub-of-is-compac).

## Fredholm alternative for compact self-adjoint operators, operator-minus-scalar form

Let $H$ be a Hilbert space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $T$ be a compact
self-adjoint bounded operator on $H$, let $I$ be the identity of $H$, and let $\mu \in \mathbb{K}$
with $\mu \neq 0$. Then the range of $T - \mu I$ equals the orthogonal complement
$(\ker(T - \mu I))^\perp$ of its kernel, and either $T - \mu I$ is bijective, or its kernel is
nonzero and finite-dimensional.

This differs from the $\mu I - T$ form of the Fredholm alternative only by a sign.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactSelfAdjointFredholmAlternative.fredholm_alternative_sub_of_isCompactOperator_isSelfAdjoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointFredholmAlternative.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CompactSelfAdjointFredholmAlternative.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/fredholm-alternative/index.html#fredholm-alternative-sub-of-is-compact-o).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fredholm alternative](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/fredholm-alternative/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/compact-and-fredholm/fredholm-alternative)
