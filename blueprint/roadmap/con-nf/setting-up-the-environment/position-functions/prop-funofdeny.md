---
declaration: proposition
origin: cited
lean: ConNF.funOfDeny
statement: formalized
proof: formalized
---

# injective functions from denied sets

Let $\tau$ be a type such that $\#\tau \leq \#\mu$. Let $D : \tau \to \operatorname{\mathsf{Set}}(\mu)$ be a function such that for each $x : \tau$, the set $D(x)$, called the *denied set* of $x$, has size less than $\operatorname{\mathsf{cof}}(\operatorname{\mathsf{ord}}(\#\mu))$. Then there is an injective function $f : \tau \to \mu$ such that if $\nu \in D(x)$, then $\nu < f(x)$.

## Depends on

- [model parameters](../model-parameters/def-params.md)

## Proof

Pick a well-ordering $\prec$ of $\tau$ of length at most $\operatorname{\mathsf{ord}}(\#\mu)$. Define $f$ by well-founded recursion on $\prec$. Suppose that we have already defined $f$ for all $y \prec x$. Then let

$$
X = \{ f(y) \mid y \prec x \} \cup \{ \nu \mid \exists \nu' \in D(x),\, \nu \leq \nu' \}
$$

This set has size strictly less than $\mu$, so there is some $\nu : \mu$ not contained in it. Set $f(x) = \nu$.

## Lean

Formalized as [`ConNF.funOfDeny`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.funOfDeny).

## Sources

- [Consistency of New Foundations blueprint: chapters/environment.tex, line 301](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/environment.tex#L301)
