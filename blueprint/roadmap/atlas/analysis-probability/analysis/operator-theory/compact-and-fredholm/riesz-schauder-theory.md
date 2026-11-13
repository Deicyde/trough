---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Normed.Operator.Compact.RieszSchauder.finiteDimensional_ker, MathlibExt.Analysis.Normed.Operator.Compact.RieszSchauder.exists_continuous_projection, MathlibExt.Analysis.Normed.Operator.Compact.RieszSchauder.isClosed_range_smul_one_sub, MathlibExt.Analysis.Normed.Operator.Compact.RieszSchauder.fredholm_alternative, MathlibExt.Analysis.InnerProductSpace.RieszSchauder.range_eq_orthogonal_ker_adjoint, MathlibExt.Analysis.InnerProductSpace.RieszSchauder.adjoint_smul_one_sub, MathlibExt.Analysis.InnerProductSpace.RieszSchauder.range_eq_orthogonal_ker_smul_one_sub_adjoint
statement: formalized
proof: formalized
---

# Riesz–Schauder theory

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/riesz-schauder-theory/index.html).

## Riesz–Schauder theorem, kernel part

Let $E$ be a Banach space over $\mathbb{R}$ or
$\mathbb{C}$, let $T : E \to E$ be a compact bounded linear operator, let $\mu \neq 0$ be a
scalar and let $I$ be the identity of $E$. Then the kernel of $\mu I - T$ is
finite-dimensional.

The proof is the standard restriction trick: $T$ maps the kernel of $\mu I - T$ into itself and
agrees with $\mu I$ there, so the identity of the kernel is a compact operator.

Formalized by `MathlibExt.Analysis.Normed.Operator.Compact.RieszSchauder.finiteDimensional_ker`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/Compact/RieszSchauder.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Operator/Compact/RieszSchauder.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/riesz-schauder-theory/index.html#finite-dimensional-ker).

## Continuous projection onto a finite-dimensional subspace

Let $E$ be a normed space
over $\mathbb{R}$ or $\mathbb{C}$ and let $K$ be a finite-dimensional subspace of $E$. Then
there is a continuous linear map $P : E \to E$ such that $P x = x$ for every $x \in K$ and
$P x \in K$ for every $x \in E$.

The projection is built from a basis of $K$, with the coordinate functionals extended to all
of $E$ by Hahn–Banach.

Formalized by `MathlibExt.Analysis.Normed.Operator.Compact.RieszSchauder.exists_continuous_projection`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/Compact/RieszSchauder.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Operator/Compact/RieszSchauder.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/riesz-schauder-theory/index.html#exists-continuous-projection).

## Riesz–Schauder theorem, range part

Let $E$ be a Banach space over $\mathbb{R}$ or
$\mathbb{C}$, let $T : E \to E$ be a compact bounded linear operator, let $\mu \neq 0$ be a
scalar and let $I$ be the identity of $E$. Then the range of $\mu I - T$ is closed in $E$.

The proof restricts $\mu I - T$ to a closed complement of its kernel, where a sequence argument
using compactness of $T$ shows that it is bounded below, hence has closed range.

Formalized by `MathlibExt.Analysis.Normed.Operator.Compact.RieszSchauder.isClosed_range_smul_one_sub`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/Compact/RieszSchauder.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Operator/Compact/RieszSchauder.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/riesz-schauder-theory/index.html#is-closed-range-smul-one-sub).

## Fredholm alternative, Riesz–Schauder form

Let $E$ be a Banach space over $\mathbb{R}$
or $\mathbb{C}$, let $T : E \to E$ be a compact bounded linear operator, let $\mu \neq 0$ be a
scalar and let $I$ be the identity of $E$. Then either $\mu I - T$ is bijective, or the kernel
of $\mu I - T$ is nonzero and finite-dimensional and the range of $\mu I - T$ is closed.

Formalized by `MathlibExt.Analysis.Normed.Operator.Compact.RieszSchauder.fredholm_alternative`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/Compact/RieszSchauder.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Operator/Compact/RieszSchauder.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/riesz-schauder-theory/index.html#fredholm-alternative).

## Riesz–Schauder theorem on a Hilbert space

Let $E$ be a Hilbert space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $T$ be a compact operator on $E$, let
$\mu \in \mathbb{K}$ with $\mu \ne 0$, and let $I$ be the identity operator on $E$. Then the range
of $\mu I - T$ is the orthogonal complement of the kernel of its adjoint:
$\operatorname{ran}(\mu I - T) = \ker\big((\mu I - T)^*\big)^\perp$.

For self-adjoint $T$ this gives $\operatorname{ran}(\mu I - T) = \ker(\mu I - T)^\perp$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RieszSchauder.range_eq_orthogonal_ker_adjoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RieszSchauder.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RieszSchauder.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/riesz-schauder-theory/index.html#range-eq-orthogonal-ker-adjoint).

## Adjoint of a shifted operator

Let $E$ be a Hilbert space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $T$ be a bounded linear operator on $E$ with
adjoint $T^*$, let $\mu \in \mathbb{K}$ and let $I$ be the identity operator on $E$. Then
$(\mu I - T)^* = \overline{\mu} I - T^*$, where $\overline{\mu}$ is the complex conjugate of
$\mu$ (so $\overline{\mu} = \mu$ when $\mathbb{K} = \mathbb{R}$).

Formalized by `MathlibExt.Analysis.InnerProductSpace.RieszSchauder.adjoint_smul_one_sub`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RieszSchauder.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RieszSchauder.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/riesz-schauder-theory/index.html#adjoint-smul-one-sub).

## Riesz–Schauder theorem on a Hilbert space, adjoint form

Let $E$ be a Hilbert space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $T$ be a compact operator on $E$ with adjoint $T^*$,
let $\mu \in \mathbb{K}$ with $\mu \ne 0$, and let $I$ be the identity operator on $E$. Then the
range of $\mu I - T$ is the orthogonal complement of the kernel of $\overline{\mu} I - T^*$,
where $\overline{\mu}$ is the complex conjugate of $\mu$:
$\operatorname{ran}(\mu I - T) = \ker(\overline{\mu} I - T^*)^\perp$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RieszSchauder.range_eq_orthogonal_ker_smul_one_sub_adjoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RieszSchauder.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RieszSchauder.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/riesz-schauder-theory/index.html#range-eq-orthogonal-ker-smul-one-sub-adj).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Riesz–Schauder theory](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/riesz-schauder-theory/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/operator-theory/compact-and-fredholm/riesz-schauder-theory)
