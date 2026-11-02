---
declaration: corollary
origin: cited
lean: sum_of_rdist_eq
statement: formalized
proof: formalized
---

# Specific fibring identity

Let $Y_1,Y_2,Y_3$ and $Y_4$ be independent $G$-valued random variables. Then

$$
\begin{aligned}
& d[Y_1+Y_3; Y_2+Y_4] + d[Y_1|Y_1+Y_3; Y_2|Y_2+Y_4] \\
&\qquad + \mathbb{I}[Y_1+Y_2 : Y_2 + Y_4 | Y_1+Y_2+Y_3+Y_4] = d[Y_1; Y_2] + d[Y_3; Y_4].
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [General fibring identity](fibring-ident.md)
- [Additivity of entropy](../shannon-entropy-inequalities/part-02/add-entropy.md)
- [Conditional entropy and relabeling](../shannon-entropy-inequalities/part-01/relabeled-entropy-cond.md)

## Proof

We apply [General fibring identity](fibring-ident.md) with $H := G \times G$, $H' := G$, $\pi$ the addition homomorphism $\pi(x,y) := x+y$, and with the random variables $Z_1 := (Y_1,Y_3)$ and $Z_2 := (Y_2,Y_4)$. Then by independence ([Additivity of entropy](../shannon-entropy-inequalities/part-02/add-entropy.md))

$$
d[Z_1; Z_2] = d[Y_1; Y_2] + d[Y_3; Y_4]
$$

while by definition

$$
d[\pi(Z_1); \pi(Z_2)] = d[Y_1+Y_3; Y_2+Y_4].
$$

Furthermore,

$$
d[Z_1|\pi(Z_1); Z_2|\pi(Z_2)] = d[Y_1|Y_1+Y_3;Y_2|Y_2+Y_4],
$$

since $Z_1=(Y_1,Y_3)$ and $Y_1$ are linked by an invertible affine transformation once $\pi(Z_1)=Y_1+Y_3$ is fixed, and similarly for $Z_2$ and $Y_2$. (This has to do with [Conditional entropy and relabeling](../shannon-entropy-inequalities/part-01/relabeled-entropy-cond.md)) Finally, we have

$$
\begin{aligned}
&\mathbb{I}[Z_1 + Z_2 : (\pi(Z_1),\pi(Z_2)) \,|\, \pi(Z_1) + \pi(Z_2)] \\
&\ = \mathbb{I}[(Y_1+Y_2, Y_3+Y_4) : (Y_1+Y_3, Y_2+Y_4) \,|\, Y_1+Y_2+Y_3+Y_4] \\
&\ = \mathbb{I}[Y_1+Y_2 : Y_2+Y_4 \,|\, Y_1+Y_2+Y_3+Y_4]
\end{aligned}
$$

where in the last line we used the fact that $(Y_1+Y_2, Y_1+Y_2+Y_3+Y_4)$ uniquely determine $Y_3+Y_4$ and similarly $(Y_2+Y_4, Y_1+Y_2+Y_3+Y_4)$ uniquely determine $Y_1+Y_3$. (This requires another helper lemma about entropy.)

## Lean

Formalized as [`sum_of_rdist_eq`](https://teorth.github.io/pfr/docs/find/#doc/sum_of_rdist_eq).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/fibring.tex, line 51](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/fibring.tex#L51)
