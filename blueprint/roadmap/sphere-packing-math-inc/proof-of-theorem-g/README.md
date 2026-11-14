# Proof of Theorem g

Our proof of the Theorem [g](../cohn-elkies-linear-programming-bounds/thm-g.md) relies on the following two inequalities for modular objects.

- [ineqA](prop-ineqa.md)
- [ineqB](prop-ineqb.md)

Here we formalize the proof of the inequalities by Lee (Lee). First, we can rewrite the inequality in [ineqA](prop-ineqa.md) as follows.

- [FG-definition](def-fg-definition.md)
- [F-G-phi-psi-identities](lemma-f-g-phi-psi-identities.md)
- [ineqABnew-equiv](lemma-ineqabnew-equiv.md)

Now, the first inequality [(9)](lemma-ineqabnew-equiv.md) follows from the positivity of each $F(it)$ and $G(it)$.

- [F-G-pos](lemma-f-g-pos.md)
- [ineqAnew](cor-ineqanew.md)

To prove the second inequality [(10)](lemma-ineqabnew-equiv.md), we need some identities satisfied by $F$ and $G$.

- [FG-de](lemma-fg-de.md)
- [MLDE-pos](cor-mlde-pos.md)

The second inequality [(10)](lemma-ineqabnew-equiv.md) follows from the following two observations. Since $G(it) > 0$ for all $t > 0$, we can define the quotient

$$
Q(t) := \frac{F(it)}{G(it)}\qquad\text{(15)}
$$

as a function on $(0, \infty)$.

- [Qlim](lemma-qlim.md)
- [Qdec](prop-qdec.md)
- [ineqBnew](cor-ineqbnew.md)

Finally, we are ready to prove Theorem [g](../cohn-elkies-linear-programming-bounds/thm-g.md).

- [g1](thm-g1.md)
