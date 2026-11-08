---
declaration: lemma
origin: cited
lean: Eq1323.op_Ly_Ry_eq_LSy
statement: formalized
---

# Building a magma

Let $G$ be a countably infinite abelian torsion group of exponent $2$, and let $\phi_a$ be as in the previous lemma. Let $N$ be the set of pairs $(x,a)$ with $x \in \mathbb{Q}^\times$ and $a \in G \backslash \{0\}$, and let $M = G \uplus N$ be the disjoint union of $G$ and $N$. Suppose that we have an operation $\diamond : M \times M \to M$ satisfying the following axioms:

- (i) We have

    $$
    a \diamond b = a+b\qquad\text{(4)}
    $$

    for $a,b \in G$.

- (ii) We have

    $$
    (x,a) \diamond b = (\phi_a(b) x, a)\qquad\text{(5)}
    $$

    $$
    b \diamond (x,a) = (x / \phi_a(b), a)\qquad\text{(6)}
    $$

    and

    $$
    (\phi_a(b) x,a) \diamond (x,a) = a+b\qquad\text{(7)}
    $$

    for $x \in \mathbb{Q}^\times$, $b \in G$, and $a \in G \backslash \{0\}$.

- (iii) If $a,b,0 \in G$ are distinct and $(x,a) \diamond (y,b) = (z,c)$ for some $x,y,z \in \mathbb{Q}^\times$ and $c \in G$, then $(y,b) \diamond (z,c) = (\phi_a(b) x,a)$.

Then [(2)](1323-construct.md), [(3)](1323-construct.md) and hence [(1)](README.md) holds.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Bijections](bij.md)

## Proof

With these rules, $0$ is a unit, and the squaring operator is given by $Sa = 0$ and $S(x,a) = a$, so the set of squares is $G$. If $a \in G$ is a square number, we have

$$
L_a b = R_a b = a+b
$$

and

$$
L_a (x,b) = (x/\phi_b(a), b); \quad R_a (x,b) = (x \phi_b(a), b)
$$

so [(2)](1323-construct.md) is satisfied.

Now we verify [(3)](1323-construct.md). If $y$ is a square, then the claim already follows from [(2)](1323-construct.md) since $Sy=0$ is a unit. Otherwise, for $y \in \mathbb{Q}^\times$ and $b \in G \backslash \{0\}$, we have to show that

$$
L_{(y,b)} R_{(y,b)} a = R_b a = a+b
$$

for $a \in G$ and

$$
L_{(y,b)} R_{(y,b)} (x,a) = R_b (x,a) = (\phi_a(b) x, a)
$$

for $x \in \mathbb{Q}^\times$ and $a \in G \backslash \{0\}$. In the first case, we have from (6) that

$$
R_{(y,b)} a = (y/\phi_a(b), b)
$$

and then from (7) we have

$$
L_{(y,b)} R_{(y,b)} a = a+b
$$

as required. In the second case, if $a=b$, then by the bijective nature of $\phi_a$, we can write $x = \phi_a(c) y$ for some $c \in G$, then from (7) we have

$$
R_{(y,b)} (x,a) = a+c
$$

and then by (5)

$$
L_{(y,b)} R_{(y,b)} (x,a) = (\phi_a(a+c) y, a)
$$

but from construction we have $\phi_a(a+c)=-\phi_a(c) = \phi_a(b)\phi_a(c)$ and hence $\phi_a(a+c) y = \phi_a(b) x$ as required.

It remains to handle the case when $a,b$ are distinct elements of $G \backslash \{0\}$. But this follows from (iii).

## Lean

Stated as [`Eq1323.op_Ly_Ry_eq_LSy`](https://teorth.github.io/equational_theories/docs/find/#doc/Eq1323.op_Ly_Ry_eq_LSy); the blueprint marks no proof of it as formalized.

## Sources

- [Equational Theories blueprint: chapter/1323.tex, line 37](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/1323.tex#L37)
