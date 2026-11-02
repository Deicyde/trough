---
declaration: lemma
origin: cited
---

# 73 extension

Suppose that $\diamond$ is a partial solution, and $a \diamond b$ is currently undefined. Then there exists an extension $\diamond'$ of $\diamond$ for which $a \diamond' b$ is defined.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

If $a \diamond b$ is undefined, set it equal to a new element $c$. If we also have $b = d \diamond a$ for some $d$ (unique by Law 2, and only possible for $a \neq b$ by Law 3), set $a \diamond c = d$.

It is obvious that Laws 2, 3 are preserved. Now we case check Law 1:

- Case 1: $x=c$ or $y=c$. Not possible since no left multiplication with $c$ is defined.
- Case 2: $x \diamond y = c$. Only possible when $x = a$, $y = b$, but then $y \diamond (x \diamond y)$ is undefined since $y = b \neq a$ if $d$ is defined.
- Case 3. $y \diamond (x \diamond y) = c$. Only possible when $y=a$ and $x=d$, and holds in this case.
- Case 4: $x, y, x \diamond y, y \diamond (x \diamond y) \neq c$: this case is already covered by the previous seed.

## Sources

- [Equational Theories blueprint: chapter/infinite_magma_constructions.tex, line 470](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_magma_constructions.tex#L470)
