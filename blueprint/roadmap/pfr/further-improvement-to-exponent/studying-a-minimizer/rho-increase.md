---
declaration: lemma
origin: cited
lean: condRho_sum_le
statement: formalized
proof: formalized
---

# rho-increase

For independent random variables $Y_1,Y_2,Y_3,Y_4$ over $G$, define $S:=Y_1+Y_2+Y_3+Y_4$, $T_1:=Y_1+Y_2$, $T_2:=Y_1+Y_3$. Then

$$
\rho(T_1|T_2,S)+\rho(T_2|T_1,S) - \frac{1}{2}\sum_{i} \rho(Y_i)\le \frac{1}{2}(d[Y_1;Y_2]+d[Y_3;Y_4]+d[Y_1;Y_3]+d[Y_2;Y_4]).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Rho and sums, symmetrized](../rho-functionals/rho-sums-sym.md)
- [Rho and conditioning](../rho-functionals/rho-cond.md)
- [Rho and conditioning, symmetrized](../rho-functionals/rho-cond-sym.md)
- [Conditional rho and relabeling](../rho-functionals/rho-cond-relabeled.md)
- [Specific fibring identity](../../the-fibring-lemma/cor-fibre.md)

## Proof

Let $T_1':=Y_3+Y_4$, $T_2':=Y_2+Y_4$. First note that

$$
\begin{aligned}
\rho(T_1|T_2,S)
&\le \rho(T_1|S) + \frac{1}{2}\mathbb{I}(T_1:T_2\mid S)  \\
&\le \frac{1}{2}(\rho(T_1)+\rho(T_1'))+\frac{1}{2}(d[T_1;T_1']+\mathbb{I}(T_1:T_2\mid S)) \\
&\le \frac{1}{4} \sum_{i} \rho(Y_i) +\frac{1}{4}(d[Y_1;Y_2]+d[Y_3;Y_4]) + \frac{1}{2}(d[T_1;T_1']+\mathbb{I}(T_1:T_2\mid S)).
\end{aligned}
$$

by [Rho and conditioning](../rho-functionals/rho-cond.md), [Rho and conditioning, symmetrized](../rho-functionals/rho-cond-sym.md), [Rho and sums, symmetrized](../rho-functionals/rho-sums-sym.md) respectively. On the other hand, observe that

$$
\begin{aligned}
\rho(T_1|T_2,S)
&=\rho(Y_1+Y_2|T_2,T_2') \\
&\le \frac{1}{2}(\rho(Y_1|T_2)+\rho(Y_2|T_2'))+\frac{1}{2}(d[Y_1|T_2;Y_2|T_2'])  \\
&\le \frac{1}{4} \sum_{i} \rho(Y_i) +\frac{1}{4}(d[Y_1;Y_3]+d[Y_2;Y_4]) + \frac{1}{2}(d[Y_1|T_2;Y_2|T_2']).
\end{aligned}
$$

by [Conditional rho and relabeling](../rho-functionals/rho-cond-relabeled.md), [Rho and sums, symmetrized](../rho-functionals/rho-sums-sym.md), [Rho and conditioning, symmetrized](../rho-functionals/rho-cond-sym.md) respectively. By replacing $(Y_1,Y_2,Y_3,Y_4)$ with $(Y_1,Y_3,Y_2,Y_4)$ in the above inequalities, one has

$$
\rho(T_2|T_1,S) \le \frac{1}{4} \sum_{i} \rho(Y_i) +\frac{1}{4}(d[Y_1;Y_3]+d[Y_2;Y_4]) + \frac{1}{2}(d[T_2;T_2']+\mathbb{I}(T_1:T_2\mid S))
$$

and

$$
\rho(T_2|T_1,S) \le \frac{1}{4} \sum_{i} \rho(Y_i) +\frac{1}{4}(d[Y_1;Y_2]+d[Y_3;Y_4]) + \frac{1}{2}(d[Y_1|T_1;Y_3|T_1']).
$$

Finally, take the sum of all four inequalities, apply [Specific fibring identity](../../the-fibring-lemma/cor-fibre.md) on $(Y_1,Y_2,Y_3,Y_4)$ and $(Y_1,Y_3,Y_2,Y_4)$ to rewrite the sum of last terms in the four inequalities, and divide the result by $2$.

## Lean

Formalized as [`condRho_sum_le`](https://teorth.github.io/pfr/docs/find/#doc/condRho_sum_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 281](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/further_improvement.tex#L281)
