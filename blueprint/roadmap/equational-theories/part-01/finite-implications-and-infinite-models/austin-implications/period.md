---
declaration: lemma
origin: cited
lean: FiniteModel.Finite.fn_eventually_periodic'
statement: formalized
proof: formalized
---

# Eventual period

Let $X$ be finite and $f: X \to X$. Then there exists $n \geq 1$ such that $f^{2n} = f^n$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By the pigeonhole principle, there exists $n \geq 1$, $m \geq 0$ such that $f^{m+n} = f^m$, which implies on iteration that $f^{m+mn} = f^m$ and hence $f^{2mn} = f^{mn}$, giving the claim.

## Lean

Formalized as [`FiniteModel.Finite.fn_eventually_periodic'`](https://teorth.github.io/equational_theories/docs/find/#doc/FiniteModel.Finite.fn_eventually_periodic').

## Sources

- [Equational Theories blueprint: chapter/infinite_models.tex, line 105](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_models.tex#L105)
