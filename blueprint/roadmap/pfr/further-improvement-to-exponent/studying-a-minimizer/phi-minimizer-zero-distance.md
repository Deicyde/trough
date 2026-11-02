---
declaration: proposition
origin: cited
lean: dist_of_min_eq_zero
statement: formalized
proof: formalized
---

# phi-minimizer-zero-distance

If $X_1,X_2$ is a $\phi$-minimizer, then $d[X_1;X_2] = 0$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [rho-BSG-triplet-symmetrized](rho-bsg-triplet-symmetrized.md)
- [rho-increase-symmetrized](rho-increase-symmetrized.md)
- [I1-I2-diff](i1-i2-diff.md)
- [phi-first-estimate](phi-first-estimate.md)
- [phi-second-estimate](phi-second-estimate.md)

## Proof

Consider $T_1:=X_1+X_2,T_2:=X_1+\tilde X_1, T_3:=\tilde X_1 + X_2$, and $S=X_1+X_2+\tilde X_1 + \tilde X_2$. Note that $T_1+T_2+T_3=0$. First apply [Lemma rho-BSG-triplet-symmetrized](rho-bsg-triplet-symmetrized.md) on $(T_1,T_2,T_3)$ when conditioned on $S$ to get

$$
\begin{aligned}
d[X_1;X_2] &\leq  \sum_{1 \leq i\lt j \leq 3} \mathbb{I}[T_i:T_j\mid S] + \frac{\eta}{3}   \sum_{1 \leq i\lt j \leq 3} (\rho(T_i|T_j,S) + \rho(T_j|T_i,S) -\rho(X_1)-\rho(X_2))\qquad\text{(1)}\\
&= (I_1+2I_2) + \frac{\eta}{3}   \sum_{1 \leq i\lt j \leq 3} (\rho(T_i|T_j,S) + \rho(T_j|T_i,S) -\rho(X_1)-\rho(X_2)).
\end{aligned}
$$

Then apply [Lemma rho-increase-symmetrized](rho-increase-symmetrized.md) on $(X_1,X_2,\tilde X_1,\tilde X_2)$ and get

$$
\sum_{1 \leq i\lt j \leq 3} (\rho(T_i|T_j,S) + \rho(T_j|T_i,S) -  \rho(X_1)-\rho(X_2))\le (4d[X_1;X_2]+d[X_1;X_2]+d[X_2;X_2])= 6 d[X_1;X_2]+(I_2-I_1)
$$

by [Lemma I1-I2-diff](i1-i2-diff.md). Plug in the inequality above to (1), we get

$$
d[X_1;X_2] \le (I_1+2I_2)+2\eta d[X_1;X_2]+\frac{\eta}{3}(I_2-I_1).
$$

By [Lemma phi-second-estimate](phi-second-estimate.md) we can conclude that

$$
d[X_1;X_2] \le 8\eta d[X_1;X_2]-\frac{3-10\eta}{3-3\eta} (2\eta d[X_1;X_2]-I_1).
$$

Finally by [Lemma phi-first-estimate](phi-first-estimate.md) and $\eta<1$ we get that the second term is $\le 0$, and thus $d[X_1;X_2] \le 8\eta d[X_1;X_2]$. By the choice $\eta<1/8$ and the non-negativity of $d$ we have $d[X_1;X_2]=0$.

## Lean

Formalized as [`dist_of_min_eq_zero`](https://teorth.github.io/pfr/docs/find/#doc/dist_of_min_eq_zero).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 320](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/further_improvement.tex#L320)
