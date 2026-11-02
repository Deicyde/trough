---
declaration: proposition
origin: cited
lean: mutual_information_le_t_12, mutual_information_le_t_13, mutual_information_le_t_23
statement: formalized
proof: formalized
---

# Mutual information bound

We have

$$
\mathbb{I}[Z_1 : Z_2\, |\, W],\
\mathbb{I}[Z_2 : Z_3\, |\, W],\
\mathbb{I}[Z_1 : Z_3\, |\, W] \leq t
$$

where

$$
t :=  m(4m+1) \eta k.\qquad\text{(3)}
$$

## Depends on

- [Additional random variables](more-random.md)

## Proof depends on

- [Bounding mutual information](../bounding-the-mutual-information/key.md)
- [Data processing inequality](../data-processing-inequality/data-process.md)

## Proof

We analyze these variables by [Bounding mutual information](../bounding-the-mutual-information/key.md) in several different ways. In the first application, take $X_{i,j}=Y_{i,j}$. Note that each column $(X_{i,j})_{i=1}^m$ is indeed a permutation of $X_1,\dots,X_m$; in fact, the trivial permutation. Note also that for each $i \in \mathbb{Z}/m\mathbb{Z}$, the row sum is

$$
\sum_{j=1}^m X_{i,j} = \sum_{j \in \mathbb{Z}/m\mathbb{Z}} Y_{i,j} = P_i
$$

and for each $j \in \mathbb{Z}/m\mathbb{Z}$, the column sum is

$$
\sum_{i=1}^m X_{i,j} = \sum_{i \in \mathbb{Z}/m\mathbb{Z}} Y_{i,j} = Q_j.
$$

Finally note that $\sum_{i,j=1}^m X_{i,j} = W$. From [Bounding mutual information](../bounding-the-mutual-information/key.md) we then have

$$
\mathbb{I}[ (P_i)_{i \in \mathbb{Z}/m\mathbb{Z}} : (Q_j)_{j \in \mathbb{Z}/m\mathbb{Z} } \,\big|\, W ] \leq t,
$$

with $t$ as in (3). Since $Z_1$ is a function of $(P_i)_{i \in \mathbb{Z}/m\mathbb{Z}}$ by [(1)](more-random.md), and similarly $Z_2$ is a function of $(Q_j)_{j \in \mathbb{Z}/m\mathbb{Z}}$, it follows immediately from [Data processing inequality](../data-processing-inequality/data-process.md) that

$$
\mathbb{I}[ Z_1 : Z_2 \,|\, W ] \leq t.
$$

In the second application of [Bounding mutual information](../bounding-the-mutual-information/key.md), we instead consider $X'_{i,j} = Y_{i-j,j}$. Again, for each fixed $j$, the tuple $(X'_{i,j})_{i=1}^m$ is a permutation of $X_1,\dots,X_m$. This time the row sums for $i \in \{1,\dots, m\}$ are

$$
\sum_{j=1}^m X'_{i,j} = \sum_{j \in \mathbb{Z}/m\mathbb{Z}} Y_{i-j,j} = R_{-i}.
$$

Similarly, the column sums for $j \in \{1,\dots, m\}$ are

$$
\sum_{i=1}^m X'_{i,j} = \sum_{i \in \mathbb{Z}/m\mathbb{Z}} Y_{i-j,j} = Q_j.
$$

As before, $\sum_{i,j=1}^m X'_{i,j} = W$. Hence, using [(1)](more-random.md) and [Data processing inequality](../data-processing-inequality/data-process.md) again, [Bounding mutual information](../bounding-the-mutual-information/key.md) tells us

$$
\mathbb{I}[ Z_3 :  Z_2 \,|\, W] \leq \mathbb{I}[ (R_i)_{i \in \mathbb{Z}/m\mathbb{Z}} : (Q_j)_{j \in \mathbb{Z}/m\mathbb{Z} } \,\big|\, W ] \leq t.
$$

In the third application (In fact, by permuting the variables $(Y_{i,j})_{i,j \in \mathbb{Z}/m\mathbb{Z}}$, one can see that the random variables $(W, Z_1, Z_2)$ and $(W, Z_1, Z_3)$ have the same distribution, so this is in some sense identical to – and can be deduced from – the first application.) of [Bounding mutual information](../bounding-the-mutual-information/key.md), take $X''_{i,j} = Y_{i,j-i}$. The column and row sums are respectively

$$
\sum_{j=1}^m X''_{i,j} = \sum_{j \in \mathbb{Z}/m\mathbb{Z}} Y_{i,j-i} = P_i
$$

and

$$
\sum_{i=1}^m X''_{i,j} = \sum_{i \in \mathbb{Z}/m\mathbb{Z}} Y_{i,j-i} = R_{-j}.
$$

Hence, [Bounding mutual information](../bounding-the-mutual-information/key.md) and [Data processing inequality](../data-processing-inequality/data-process.md) give

$$
\mathbb{I}[ Z_1 : Z_3 \,|\, W] \leq \mathbb{I}[ (P_i)_{i \in \mathbb{Z}/m\mathbb{Z}} : (R_j)_{j \in \mathbb{Z}/m\mathbb{Z} } \,\big|\, W ] \leq t,
$$

which completes the proof.

## Lean

Formalized as [`mutual_information_le_t_12`](https://teorth.github.io/pfr/docs/find/#doc/mutual_information_le_t_12), [`mutual_information_le_t_13`](https://teorth.github.io/pfr/docs/find/#doc/mutual_information_le_t_13), [`mutual_information_le_t_23`](https://teorth.github.io/pfr/docs/find/#doc/mutual_information_le_t_23).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 623](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L623)
