---
declaration: proposition
origin: cited
lean: ConNF.fuzz
statement: formalized
proof: formalized
---

# fuzz maps

Let $\beta$ be a type index with model data, and suppose that $\mathsf{Tang}_\beta$ has a position function. Let $\gamma$ be any proper type index not equal to $\beta$. Then there is an injective *fuzz map* $f_{\beta,\gamma} : \mathsf{Tang}_\beta \to {\mathcal L}$ such that $\iota(t) < \iota(f_{\beta,\gamma}(t))$, and the different $f_{\beta,\gamma}$ all have disjoint ranges. In particular, for any near-litter $N$ with $N^\circ = f_{\beta,\gamma}(t)$, we have $\iota(t) < \iota(N)$, and additionally, for any atom $a$ with $a^\circ = f_{\beta,\gamma}(t)$, we have $\iota(t) < \iota(a)$. (We might want to encapsulate atoms and near-litters somehow. We could make a typeclass, or write theorems in terms of the coproduct ${\mathcal A} \oplus {\mathcal N}$.)

## Depends on

- [tangle](def-tangle.md)
- [position function](../position-functions/def-position.md)

## Proof depends on

- [injective functions from denied sets](../position-functions/prop-funofdeny.md)

## Proof

We define $g : \mathsf{Tang}_\beta \to \mu$ by [injective functions from denied sets](../position-functions/prop-funofdeny.md), where the denied sets are given by $D(t) = \{ \iota(t) \}$. Then we set $f_{\beta,\gamma}(t) = (g(t), \beta, \gamma)$.

## Lean

Formalized as [`ConNF.fuzz`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.fuzz).

## Sources

- [Consistency of New Foundations blueprint: chapters/environment.tex, line 378](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/environment.tex#L378)
