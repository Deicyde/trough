---
declaration: definition
origin: cited
---

# Additional random variables

By a slight abuse of notation, we identify $\mathbb{Z}/m\mathbb{Z}$ and $\{1,\dots,m\}$ in the obvious way, and let $Y_{i,j}$ be an independent copy of $X_i$ for $i,j \in \mathbb{Z}/m\mathbb{Z}$. Then also define:

$$
W := \sum_{i,j \in \mathbb{Z}/m\mathbb{Z}} Y_{i,j}
$$

and

$$
Z_1 := \sum_{i,j \in \mathbb{Z}/m\mathbb{Z}} i Y_{i,j},\ \ \
Z_2 := \sum_{i,j \in \mathbb{Z}/m\mathbb{Z}} j Y_{i,j},\ \ \
Z_3 := \sum_{i,j \in \mathbb{Z}/m\mathbb{Z}} (-i-j) Y_{i,j}.
$$

The addition $(-i-j)$ takes place over $\mathbb{Z}/m\mathbb{Z}$. Note that, because we are assuming $G$ is $m$-torsion, it is well-defined to multiply elements of $G$ by elements of $\mathbb{Z}/m\mathbb{Z}$. We will also define for $i,j,r \in \mathbb{Z}/m\mathbb{Z}$ the variables

$$
P_i := \sum_{j \in \mathbb{Z}/m\mathbb{Z}} Y_{i,j} , \quad
Q_j := \sum_{i \in \mathbb{Z}/m\mathbb{Z}} Y_{i,j} , \quad
R_r := \sum_{\substack{i,j \in \mathbb{Z}/m\mathbb{Z} \\ i+j=-r}} Y_{i,j} .\qquad\text{(1)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

The blueprint marks this formalized but names no Lean declaration.

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 594](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L594)
