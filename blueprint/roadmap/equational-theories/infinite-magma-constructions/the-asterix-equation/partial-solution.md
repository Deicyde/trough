---
declaration: definition
origin: cited
---

# partial-solution

A *partial solution* $(E_0, E_1, E_2, f)$ to fh consists of nested finite sets

$$
E_0 \subseteq E_1 \subseteq E_2 \subseteq \mathbb{Z}
$$

together with a function $f: E_1 \to E_2$ with the following properties:

- **(a)** If $h \in E_0$, then $f(h) \in E_1$, so that $f^2(h)$ is well-defined as an element of $E_2$; furthermore, $h + f(h) + f^2(h)$ lies in $E_1$, so that the left-hand side of fh makes sense; and fh holds.
- **(b)** The function $f$ is a bijection from $E_1 \backslash E_0$ to $E_2 \backslash E_1$.
- **(c)** $f(0)=0$.
- **(d)** $h+f(h) \neq 0$ for all non-zero $h \in E_1$.

We partially order the space of partial solutions to fh by writing $(E_0, E_1, E_2, f) \leq (E'_0, E'_1, E'_2, f')$ if the following properties hold:

- $E_i \subseteq E'_i$ for $i=0,1,2$.
- $f$ agrees with $f'$ on $E_0$.

When this occurs we say that the partial solution $(E'_0, E'_1, E'_2, f')$ *extends* the partial solution $(E_0, E_1, E_2, f)$.

We define the *trivial partial solution* $(E_0,E_1,E_2,f)$ by setting $E_0=E_1=E_2=\{0\}$ and $f(0)=0$; it is the minimal element of the above partial order.

## Depends on

Its statement uses no other node of the blueprint.

## Sources

- [Equational Theories blueprint: chapter/infinite_magma_constructions.tex, line 49](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_magma_constructions.tex#L49)
