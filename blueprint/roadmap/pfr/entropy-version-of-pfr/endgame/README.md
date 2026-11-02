# Endgame

Let $X_1,X_2,\tilde X_1,\tilde X_2$ be as before, and introduce the random variables

$$
U := X_1 + X_2, \qquad V := \tilde X_1 + X_2, \qquad W := X_1 + \tilde X_1
$$

and

$$
S := X_1 + X_2 + \tilde X_1 + \tilde X_2.
$$

- [Symmetry identity](symm-lemma.md)
- [Bound on conditional mutual informations](uvw-s.md)
- [Bound on distance increments](total-dist.md)
- [Key identity](key-ident.md)

For the next two lemmas, let $(T_1,T_2,T_3)$ be a $G^3$-valued random variable such that $T_1+T_2+T_3=0$ holds identically. Set

$$
\delta := \sum_{1 \leq i < j \leq 3} \mathbb{I}[T_i;T_j].\qquad\text{(1)}
$$

- [Constructing good variables, I](construct-good-prelim.md)

(Note: in the paper, this lemma was phrased in a more intuitive formulation that is basically the contrapositive of the one here. Similarly for the next two lemmas.)

- [Constructing good variables, II](construct-good.md)
- [$\tau$-decrement](de-prop.md)
