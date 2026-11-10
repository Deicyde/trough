---
declaration: lemma
origin: cited
lean: Eq1323.extend
statement: formalized
---

# Greedy extension

If $\diamond$ is defined by a partial solution, and $(x,a) \diamond (y,b)$ is undefined for some $x,y \in \mathbb{Q}^\times$ and distinct $a,b \in G \backslash \{0\}$, then it is possible to extend the partial solution so that $(x,a) \diamond (y,b)$ is now defined.

## Depends on

Its statement uses no other node that has an article here.

## Proof

We select a $c \in G \backslash \{0\}$ that has not previously been used by the partial solution, let $z \in \mathbb{Q}^\times$ be arbitrary, (e.g., one could take $z=1$ if desired), and add $(x,y,z,a,b,c)$ to ${\mathcal F}$, thus we now also assign

$$
(\phi_a(b)^n x,a) \diamond (\phi_b(c)^n y,b) = (\phi_c(a)^n z,c)
$$

$$
(\phi_b(c)^n y,b) \diamond (\phi_c(a)^n z,c) = (\phi_a(b)^{n+1} x, a)
$$

$$
(\phi_c(a)^n z,c) \diamond (\phi_a(b)^{n+1} x, a) = (\phi_b(c)^{n+1} y,b)
$$

for all natural numbers $n$. As the $a,b,c$ are distinct, the $\phi_a(b), \phi_b(c), \phi_c(a)$ are not equal to $\pm 1$, and the members of this infinite sequence do not collide with each other. The second and third equations in this family cannot collide with previous assignments because $c$ is novel. If we arrange matters so that $\phi_b(c)$ involves primes in the numerator or denominator that do not appear in any previous $\phi_a(b), \phi_b(c), \phi_c(a), x, y, z$ used by the greedy algorithm, or the current $x,y,z$, then we also see that the first infinite sequence does not collide with any previously assigned value of $\diamond$ either.

## Lean

Stated as [`Eq1323.extend`](https://teorth.github.io/equational_theories/docs/find/#doc/Eq1323.extend); the blueprint marks no proof of it as formalized.

## Sources

- [Equational Theories blueprint: chapter/1323.tex, line 101](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/1323.tex#L101)
