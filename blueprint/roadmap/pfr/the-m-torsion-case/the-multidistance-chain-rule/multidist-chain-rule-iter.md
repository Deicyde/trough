---
declaration: lemma
origin: cited
lean: iter_multiDist_chainRule, iter_multiDist_chainRule'
statement: formalized
proof: formalized
---

# multidist-chain-rule-iter

Let $m$ be a positive integer. Suppose one has a sequence

$$
G_m \to G_{m-1} \to \dots \to G_1 \to G_0 = \{0\}\qquad\text{(5)}
$$

of homomorphisms between abelian groups $G_0,\dots,G_m$, and for each $d=0,\dots,m$, let $\pi_d : G_m \to G_d$ be the homomorphism from $G_m$ to $G_d$ arising from this sequence by composition (so for instance $\pi_m$ is the identity homomorphism and $\pi_0$ is the zero homomorphism). Let $X_{[m]} = (X_i)_{1 \leq i \leq m}$ be a jointly independent tuple of $G_m$-valued random variables. Then

$$
\begin{split}
D[ X_{[m]} ] &=  \sum_{d=1}^m D[ \pi_d(X_{[m]}) \,|\, \pi_{d-1}(X_{[m]})] \\
&\quad + \sum_{d=1}^{m-1} \mathbb{I}[ \sum_i X_i : \pi_d(X_{[m]}) \; \big| \; \pi_d\big(\sum_i X_i\big), \pi_{d-1}(X_{[m]}) ].
\end{split}\qquad\text{(6)}
$$

In particular, by [Nonnegativity of conditional mutual information](../../shannon-entropy-inequalities/part-02/conditional-nonneg.md),

$$
\begin{aligned}
D[ X_{[m]} ] \geq  & \sum_{d=1}^m D[ \pi_d(X_{[m]})|\pi_{d-1}(X_{[m]}) ] \\
& + \mathbb{I}[ \sum_i X_i : \pi_1(X_{[m]}) \; \big| \; \pi_1\bigl(\sum_i X_i\bigr) ].\qquad\text{(7)}\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Conditional multidistance chain rule](multidist-chain-rule-cond.md)
- [Nonnegativity of conditional mutual information](../../shannon-entropy-inequalities/part-02/conditional-nonneg.md)

## Proof

From [Conditional multidistance chain rule](multidist-chain-rule-cond.md) (taking $Y_{[m]} = \pi_{d-1}(X_{[m]})$ and $\pi = \pi_d$ there, and noting that $\pi_d(X_{[m]})$ determines $Y_{[m]}$) we have

$$
\begin{aligned}
D[ X_{[m]} \,|\, \pi_{d-1}(X_{[m]}) ] &=  D[ X_{[m]} \,|\, \pi_d(X_{[m]}) ] + D[  \pi_d(X_{[m]})\,|\,\pi_{d-1}(X_{[m]}) ] \\
&\quad + \mathbb{I}[ \sum_{i=1}^m X_i : \pi_d(X_{[m]}) \; \big| \; \pi_d\bigl(\sum_{i=1}^m X_i\bigr), \pi_{d-1}(X_{[m]}) ]
\end{aligned}
$$

for $d=1,\dots,m$. The claim follows by telescoping series, noting that $D[X_{[m]} | \pi_0(X_{[m]})] = D[X_{[m]}]$ and that $\pi_m(X_{[m]})=X_{[m]}$ (and also $\pi_m( \sum_i X_i ) = \sum_i X_i$).

## Lean

Formalized as [`iter_multiDist_chainRule`](https://teorth.github.io/pfr/docs/find/#doc/iter_multiDist_chainRule), [`iter_multiDist_chainRule'`](https://teorth.github.io/pfr/docs/find/#doc/iter_multiDist_chainRule').

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 423](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/torsion.tex#L423)
