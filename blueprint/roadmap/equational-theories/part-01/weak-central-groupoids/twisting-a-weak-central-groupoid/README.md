# Twisting a weak central groupoid

Occasionally, an equational law is preserved under a “twist” operation in which one replaces the magma operation $x \diamond y$ by $x \diamond' y := Tx \diamond Uy$ for some automorphisms $T,U$ of the magma $G$ that satisfy additional relations. In the case of the weak central groupoid law [(1)](../README.md), we see that

$$
(y \diamond' x) \diamond' (x \diamond' (z \diamond' y))= (T^2 y \diamond TUx) \diamond (UTx \diamond (UTUz \diamond U^3y))
$$

so if $T$ is an automorphism of order $5$ and $U = T^{-1}$ (so that $T^2 = U^3$), we conclude that this twisted magma is also a weak central groupoid. This can be used to generate further counterexamples. For instance, let $M_2$ be the order two weak central groupoid with carrier ${\mathbb F}_2$ and with the NAND operation $x \diamond y := 1 - xy$; this can easily be verified to be a weak central groupoid. It does not have any nontrivial automorphisms, but its fifth power $M_2^{\otimes 5}$ has a cyclic shift $T$ of order $5$: $T( (x_i)_{i\in \mathbb{Z}/5\mathbb{Z}} ) = (x_{i+1})_{i \in \mathbb{Z}/5\mathbb{Z}}$. If we twist $M_2^{\otimes 5}$ by $T$ and $T^{-1}$, we obtain a weak central groupoid $M$ with carrier ${\mathbb F}_2^5$ and magma operation

$$
(x_i)_{i\in \mathbb{Z}/5\mathbb{Z}} \diamond (y_i)_{i\in \mathbb{Z}/5\mathbb{Z}} = (1 - x_{i+1} y_{i-1})_{i \in \mathbb{Z}/5\mathbb{Z}}.
$$

In particular, if $x = (x_i)_{i\in \mathbb{Z}/5\mathbb{Z}}$, then

$$
x \diamond x = (1 - x_{i+1} x_{i-1})_{i \in \mathbb{Z}/5\mathbb{Z}}
$$

and

$$
(x \diamond x) \diamond (x \diamond x) = (1 - (1 - x_{i+2} x_{i}) (1 - x_i x_{i-2}) )_{i \in \mathbb{Z}/5\mathbb{Z}}
$$

which by the laws of boolean algebra simplify to

$$
(x \diamond x) \diamond (x \diamond x) = (x_i (x_{i-2} + x_i + x_{i+2}))_{i \in \mathbb{Z}/5\mathbb{Z}}
$$

from which one can easily refute equation 151,

$$
x = (x \diamond x) \diamond (x \diamond x).
$$

Informally, the reason for this is that equation 151 has a different semigroup twist symmetries: $T^2 = 1, T = U^{-1}$ instead of $T^5 = 1, T = U^{-1}$.
