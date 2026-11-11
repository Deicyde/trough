---
declaration: proposition
origin: cited
lean: mutual_information_le
statement: formalized
proof: formalized
---

# Bounding mutual information

Suppose that $X_{i,j}$, $1 \leq i,j \leq m$, are jointly independent $G$-valued random variables, such that for each $j = 1,\dots,m$, the random variables $(X_{i,j})_{i = 1}^m$ coincide in distribution with some permutation of $X_{[m]}$. Write

$$
{\mathcal I} := \mathbb{I}[ \bigl(\sum_{i=1}^m X_{i,j}\bigr)_{j =1}^{m} : \bigl(\sum_{j=1}^m X_{i,j}\bigr)_{i = 1}^m \; \big| \; \sum_{i=1}^m \sum_{j = 1}^m  X_{i,j} ].
$$

Then

$$
{\mathcal I} \leq m(4m+1) \eta k.\qquad\text{(1)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [cor-multid](../the-multidistance-chain-rule/cor-multid.md)
- [Relabeling](../multidistance/multidist-perm.md)
- [Lower bound on conditional multidistance, II](../the-tau-functional/cond-multidist-lower-ii.md)
- [Comparison of Ruzsa distances, I](../../entropic-ruzsa-calculus/part-02/first-useful.md)
- [Kaimonovich–Vershik–Madiman inequality, III](../more-ruzsa-distance-estimates/klm-3.md)
- [Independent lower bound on sumset](../../entropic-ruzsa-calculus/part-01/sumset-lower.md)
- [Ruzsa triangle inequality](../../entropic-ruzsa-calculus/part-01/ruzsa-triangle.md)
- [Comparing sums](../more-ruzsa-distance-estimates/compare-sums.md)
- [Multidistance and Ruzsa distance, II](../multidistance/multidist-ruzsa-ii.md)

## Proof

For each $j \in \{1,\dots,m\}$ we call the tuple $(X_{i,j})_{i = 1}^m$ a *column* and for each $i \in \{1,\dots, m\}$ we call the tuple $(X_{i,j})_{j = 1}^m$ a *row*. Hence, by hypothesis, each column is a permutation of $X_{[m]} = (X_i)_{i=1}^m$.

From [Corollary cor-multid](../the-multidistance-chain-rule/cor-multid.md) we have

$$
{\mathcal I} \leq \sum_{j=1}^{m-1} A_j + B,\qquad\text{(2)}
$$

where

$$
A_j := D[ (X_{i, j})_{i = 1}^m] - D[ (X_{i, j})_{i = 1}^m  \; \big| \; (X_{i,j} + \cdots + X_{i,m})_{i =1}^m  ]
$$

and

$$
B := D[ (X_{i,m})_{i=1}^m ] - D[ \bigl(\sum_{j=1}^m X_{i,j}\bigr)_{i=1}^m ].
$$

We first consider the $A_j$, for fixed $j \in \{1,\dots, m-1\}$. By [Relabeling](../multidistance/multidist-perm.md) and our hypothesis on columns, we have

$$
D[ (X_{i, j})_{i = 1}^m ]= D[ (X_i)_{i=1}^m ] = k.
$$

Let $\sigma = \sigma_j \colon I \to I$ be a permutation such that $X_{i,j} \equiv X_{\sigma(i)}$, and write $X'_i := X_{i,j}$ and $Y_i := X_{i,j} + \cdots + X_{i,m}$. By [Lower bound on conditional multidistance, II](../the-tau-functional/cond-multidist-lower-ii.md), we have

$$
\begin{aligned}
A_j & \leq \eta (\sum_{i = 1}^{m} d[X_{i,j}; X_{i, j}|X_{i, j} + \cdots + X_{i,m}]).\qquad\text{(3)}\end{aligned}
$$

We similarly consider $B$. By [Relabeling](../multidistance/multidist-perm.md) applied to the $m$-th column,

$$
D[ (X_{i, m})_{i = 1}^m ] = D[X_{[m]}] = k.
$$

For $1 \leq i \leq m$, denote the sum of row $i$ by

$$
V_i := \sum_{j=1}^m X_{i,j};
$$

if we apply [Lower bound on conditional multidistance, II](../the-tau-functional/cond-multidist-lower-ii.md) again, now with $X_{\sigma(i)} = X_{i,m}$, $X'_i := V_i$, and with the variable $Y_i$ being trivial, we obtain

$$
B \leq \eta \sum_{i = 1}^m d[X_{i,m}; V_i].\qquad\text{(4)}
$$

It remains to bound the distances appearing in (3) and (4) further using Ruzsa calculus. For $1 \leq j \leq m-1$ and $1 \leq i \leq m$, by [Comparison of Ruzsa distances, I](../../entropic-ruzsa-calculus/part-02/first-useful.md) we have

$$
\begin{aligned} &d[ X_{i,j}; X_{i,j}| X_{i,j}+\cdots+X_{i,m}]
\leq d[X_{i,j}; X_{i,j}] \\
&\quad + \tfrac{1}{2} \bigl(\mathbb{H}[X_{i,j}+\cdots+X_{i,m}] - \mathbb{H}[X_{i,{j+1}}+\cdots+X_{i,m}]\bigr).
\end{aligned}
$$

For each $i$, summing over $j = 1,\dots, m-1$ gives

$$
\begin{aligned}
&\sum_{j=1}^{m-1} d[X_{i,j}; X_{i,j}| X_{i,j}+\cdots+X_{i,m}] \\
&\qquad \leq \sum_{j=1}^{m-1} d[X_{i,j}; X_{i,j}] + \frac12 \bigl( \mathbb{H}[V_i] - \mathbb{H}[X_{i,m}] \bigr).\qquad\text{(5)}\end{aligned}
$$

On the other hand, by [Kaimonovich–Vershik–Madiman inequality, III](../more-ruzsa-distance-estimates/klm-3.md) (since $X_{i,m}$ appears in the sum $V_i$) we have

$$
\begin{aligned}
d[X_{i,m}; V_i]
&\leq d[X_{i,m}; X_{i,m}] + \frac12 \bigl( \mathbb{H}[V_i] - \mathbb{H}[X_{i,m}] \bigr).\qquad\text{(6)}\end{aligned}
$$

Combining (2), (3) and (4) with (5) and (6) (the latter two summed over $i$), we get

$$
\begin{aligned}
\frac1{\eta} {\mathcal I} &\leq \sum_{i,j=1}^m d[X_{i,j};X_{i,j}] + \sum_{i=1}^m (\mathbb{H}[V_i] - \mathbb{H}[X_{i,m}]) \\
&= m \sum_{i=1}^m d[X_i; X_i] + \sum_{i=1}^m \mathbb{H}[V_i] - \sum_{i=1}^m \mathbb{H}[X_i].\qquad\text{(7)}\end{aligned}
$$

By [Comparing sums](../more-ruzsa-distance-estimates/compare-sums.md) (with $f$ taking each $j$ to the index $j'$ such that $X_{i,j}$ is a copy of $X_{j'}$) we obtain the bound

$$
\mathbb{H}[V_i] \leq \mathbb{H}[\sum_{j=1}^m X_j] + \sum_{j=1}^m d[X_{i,j}; X_{i,j}].
$$

Finally, summing over $i$ and using $D[X_{[m]}] = k$ gives

$$
\begin{aligned}
\sum_{i=1}^m \mathbb{H}[V_i] - \sum_{i=1}^m \mathbb{H}[X_i] & \leq \sum_{i,j=1}^m d[X_{i,j}; X_{i,j}] + m k \\ & = m\sum_{i = 1}^m d[X_i; X_i] + mk,
\end{aligned}
$$

where in the second step we used the permutation hypothesis. Combining this with (7) gives the

$$
{\mathcal I} \leq 2\eta m \biggl( \sum_{i=1}^m d[X_i;X_i] \biggr) + mk.
$$

The claim (1) is now immediate from [Multidistance and Ruzsa distance, II](../multidistance/multidist-ruzsa-ii.md).

## Lean

Formalized as [`mutual_information_le`](https://teorth.github.io/pfr/docs/find/#doc/mutual_information_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 501](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/torsion.tex#L501)
