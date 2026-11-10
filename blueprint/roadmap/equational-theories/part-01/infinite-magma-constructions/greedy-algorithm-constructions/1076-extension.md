---
declaration: lemma
origin: cited
lean: Eq1076.Greedy.lift
statement: formalized
---

# 1076 extension

Suppose that $\diamond$ is a partial solution, and $a \diamond b$ is currently undefined. Then there exists an extension $\diamond'$ of $\diamond$ for which $a \diamond' b$ is defined.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Set $a \diamond' b = c$ for some new element $c$. If $d_1,d_2,...,d_n$ are the elements for which $a \diamond d_i = b$, set $c \diamond' d_i = c'_i$ for some new element $c'_i$, and also set $d_i \diamond' c'_i = a$. If $d_i \diamond a$ is equal to some $e_i$, set $e_i \diamond' c'_i = c''_i$ and $c'_i \diamond' c''_i = d_i$, where $c''_i$ is equal to $a$ if $e_i = d_i$, or is some new element otherwise.

One can verify that no collisions are caused by this construction (this is why we have to take $c''_i=a$ when $e_i=d_i$), and that Law 2 is preserved.

We need to verify that these constructions preserve Law 1. There are several cases:

- $y=c$. Not possible since there are no right multiplications by $c$ defined.
- $x=c$. Not possible since it forces $y = d_i$, $x \diamond y = c'_i$ for some $i$.
- $y=c'_i$, $x = d_i$. True by construction.
- $y=c'_i$, $x \neq d_i$. This forces $x = e_i \neq d_i$ and $x \diamond' y = c''_i$, but then $x \diamond' (x \diamond' y)$ is undefined.
- $x=c'_i$. Not possible because this forces $x \diamond' y = d_i$, and $x \diamond' (x \diamond' y)$ will be undefined. (Here we use the fact that $e_i=d_i$ can only occur when $d_i \neq a$, by Law 2.)
- $x = c''_i$ is new. Not possible as no left multiplications by $c''_i$ are defined.
- $y=c''_i$ is new. This forces $x = c'_i$ and $x \diamond' y = d_i$, but then $x \diamond' (x \diamond' y)$ is undefined.
- $x$ and $y$ are not new and $x \diamond y$ was undefined. This requires $x=a, y=b$, but then $x \diamond' (x \diamond' y)$ is undefined since right multiplication by $c$ is undefined.
- $x$, $y$ are not new and $x \diamond y$ was defined, but $x \diamond (x \diamond y)$ was undefined. This requires $x=a$, $x \diamond y = b$, and hence $y = d_i$ for some $i$. The claim now follows from construction.
- $x$, $y$, are not new and $x \diamond y$, $x \diamond (x \diamond y)$ were defined. This then follows from the previous seed.

## Lean

Stated as [`Eq1076.Greedy.lift`](https://teorth.github.io/equational_theories/docs/find/#doc/Eq1076.Greedy.lift); the blueprint marks no proof of it as formalized.

## Sources

- [Equational Theories blueprint: chapter/infinite_magma_constructions.tex, line 538](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_magma_constructions.tex#L538)
