---
declaration: lemma
origin: cited
lean: FiniteModel.Finite.f_gff_implies_f_fgf
statement: formalized
proof: formalized
---

# gff

Let $X$ be finite, and let $f, g: X \to X$ be such that $f = g \circ f \circ f$. Then $f = f \circ g \circ f$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By hypothesis, $f^2(x)$ uniquely determines $f(x)$. This prevents $n_x = 2$ for any $x$ (because if $n>2$ is such that $f^{n+2}(x) = f^2(x)$, then $f^{n+1}(x) \neq f(x)$), and hence also prevents $n_x > 2$ for any $x$. So again we have $f(x)$ periodic for all $x$, so $f^n = f$ for some $n>1$. Then $f = f^n = f \circ (g \circ f^2) \circ f^{n-2} = f \circ g \circ f^n = f \circ g \circ f$ as required.

## Lean

Formalized as [`FiniteModel.Finite.f_gff_implies_f_fgf`](https://teorth.github.io/equational_theories/docs/find/#doc/FiniteModel.Finite.f_gff_implies_f_fgf).

## Sources

- [Equational Theories blueprint: chapter/infinite_models.tex, line 97](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_models.tex#L97)
