---
declaration: definition
origin: cited
lean: Eq1729.N, Eq1729.N_order, Eq1729.parent
statement: formalized
---

# Definition of $N$

Take $N$ to be the free non-abelian group with a generator $e_a$ for each $a \in SM$, thus $N$ is the set of reduced words using the alphabet $e_a$, $e_a^{-1}$. Two elements $x,y \in SM$ are said to be *adjacent* if $x = e_a y$ or $y = e_a x$ for some $a \in SM$; this defines a left Cayley graph on $N$. We make a partial ordering $\leq$ on $N$ by declaring $y \leq x$ if $y$ is a right subword of $x$ (or equivalently, $y$ is on the unique simple path from $1$ to $x$). For instance, if $a,b,c \in SM$ are distinct, then

$$
1 \leq e_c \leq e_b^{-1} e_c \leq e_a e_b^{-1} e_c.
$$

If $x \in N$ is not the identity, we define the *parent* of $x$ to be the unique element $y \in N$ adjacent to $x$ whose reduced word is shorter. For instance, the parent of $e_a e_b^{-1} e_c$ is $e_b^{-1} e_c$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Eq1729.N`](https://teorth.github.io/equational_theories/docs/find/#doc/Eq1729.N), [`Eq1729.N_order`](https://teorth.github.io/equational_theories/docs/find/#doc/Eq1729.N_order), [`Eq1729.parent`](https://teorth.github.io/equational_theories/docs/find/#doc/Eq1729.parent).

## Sources

- [Equational Theories blueprint: chapter/1729.tex, line 76](https://github.com/teorth/equational_theories/blob/8b87204d5b201e1cf6c69b8dcabb0558109bee00/blueprint/src/chapter/1729.tex#L76)
