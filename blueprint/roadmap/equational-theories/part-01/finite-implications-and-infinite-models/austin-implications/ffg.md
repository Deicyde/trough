---
declaration: lemma
origin: cited
lean: FiniteModel.Finite.f_ffg_implies_f_fgf
statement: formalized
proof: formalized
---

# ffg

Let $X$ be finite, and let $f, g: X \to X$ be such that $f = f \circ f \circ g$. Then $f = f \circ g \circ f$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Call a point $x \in X$ *periodic* if $f^n(x) = x$ for some $n>0$. Because the forward orbit $x, f(x), f^2(x), \dots$ in a finite space $X$ must repeat, we see that for each $x$ there exists an $n$ such that $f^n(x)$ is periodic. Let $n_x$ be the first $n$ for which this occurs. If $n_x > 1$, then $g(x), f(g(x)), f(f(g(x))$ cannot be periodic (as this would imply $f(x)$ periodic), and then we can see that $n_{g(x)} = n_x + 1$. Hence the maximal value of $n_x$ is at most $1$, which implies that $f(x)$ is periodic for every $x$. Thus there is an $n > 1$ such that $f^n = f$. Since $f = f^2 \circ g$, we have $f^n = f^{n-2} \circ f \circ f = f^{n-2} \circ (f^2 \circ g) \circ f = f^n \circ g \circ f = f \circ g \circ f$, as desired.

## Lean

Formalized as [`FiniteModel.Finite.f_ffg_implies_f_fgf`](https://teorth.github.io/equational_theories/docs/find/#doc/FiniteModel.Finite.f_ffg_implies_f_fgf).

## Sources

- [Equational Theories blueprint: chapter/infinite_models.tex, line 91](https://github.com/teorth/equational_theories/blob/8b87204d5b201e1cf6c69b8dcabb0558109bee00/blueprint/src/chapter/infinite_models.tex#L91)
