---
declaration: definition
origin: cited
lean: ConNF.Enumeration
statement: formalized
---

# enumeration

Let $\tau$ be a type. An *enumeration* of $\tau$ is a pair $E = (i, f)$ where $i : \kappa$ and $f$ is a partial function $\kappa \to \tau$, such that all domain elements of $f$ are strictly less than $i$. (This should be encoded as a coinjective relation $\kappa \to \tau \to \mathsf{Prop}$; see [Definition relation_props](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/auxiliary.tex#L3).) If $x : \tau$, we write $x \in E$ for $x \in \operatorname{\mathsf{ran}} f$. The set $\{ y \mid y \in E \}$, which we may also loosely call $E$, is small. We will write $\varnothing$ for the empty enumeration $(0, \varnothing)$.

If $g : \tau \to \sigma$, then $g$ lifts to a direct image function mapping enumerations of $\tau$ to enumerations of $\sigma$:

$$
g(i, f) = (i, f');\quad f' = \{ (j, g(x)) \mid (j, x) \in f \}
$$

Thus, $x \in g(E) \leftrightarrow x \in g[E]$. In the same way, groups that act on $\tau$ also act on enumerations of $\tau$. (Actually, we should probably implement this using the inverse image not the direct image for better definitional equalities.) If $g : \sigma \to \tau$ is injective, then $g$ lifts to an inverse image function mapping enumerations of $\tau$ to enumerations of $\sigma$:

$$
g^{-1}(i, f) = (i, f');\quad f' = \{ (j, x) \mid (j, g(x)) \in f \}
$$

This operation may cause the domain of $f$ to shrink, but we will keep $i$ the same.

If $E = (i, e)$ and $F = (j, f)$ are enumerations of $\tau$, we define their *concatenation* by

$$
E + F = (i + j, e \cup f');\quad f' = \{(i + k, x) \mid (k, x) \in f \}
$$

This operation commutes with the others: $x \in E + F \leftrightarrow x \in E \vee x \in F$, $g[E + F] = g[E] + g[F]$, and $g^{-1}[E + F] = g^{-1}[E] + g^{-1}[F]$.

We define a partial order on enumerations by setting $(i, e) \leq (j, f)$ if and only if $f$ extends $e$ as a partial function. We obtain various corollaries, such as $E \leq F \to g(E) \leq g(F)$ and $E \leq E + F$.

Every small subset of $\tau$ is the range of some enumeration of $\tau$.

If $\#\tau \leq \#\mu$, then there are at most $\#\mu$-many enumerations of $\tau$: enumerations are determined by an element of $\kappa$ and a small subset of $\kappa \times \tau$. If $\#\tau < \#\mu$, then there are strictly less than $\#\mu$-many enumerations of $\tau$: use the same reasoning and apply [mathlib](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/auxiliary.tex#L104).

## Depends on

- [small](../model-parameters/def-small.md)

## Lean

Formalized as [`ConNF.Enumeration`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.Enumeration).

## Sources

- [Consistency of New Foundations blueprint: chapters/environment.tex, line 211](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/environment.tex#L211)
