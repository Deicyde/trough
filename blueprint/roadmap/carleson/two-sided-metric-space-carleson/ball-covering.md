---
declaration: lemma
origin: cited
lean: ball_covering
statement: formalized
proof: formalized
---

# Ball covering

Given an open set $O\ne X$, there exists a countable family of balls $B_j = B(x_j, r_j)$ such that

$$
B_j \cap B_{j'} = \emptyset \quad \text{ for } j \ne j',\qquad\text{(44)}
$$

and

$$
\bigcup_j B_{3,j} = O,\qquad\text{(45)}
$$

and

$$
B_{7,j} \cap (X \setminus O) \ne \emptyset \quad \text{ for all } j\qquad\text{(46)}
$$

and we have the bounded intersection property that each $x\in O$ is contained in at most $2^{6a}$ of the $B_{3,j}$.

## Depends on

- [Disjoint family countable](disjoint-family-countable.md)

## Proof

Define for $x\in O$,

$$
\delta(x):= \sup \{\delta\in{\mathbb{R}} : B(x,\delta)\subset O\}.
$$

Since $O$ is open, and $O\ne X$, we have

$$
0 < \delta(x) < \infty \,.
$$

Using Zorn's Lemma, we select a maximal disjoint subfamily of $\{B(x,\frac{\delta(x)}{6}) : x \in O\}$. We obtain a (by [Disjoint family countable](disjoint-family-countable.md) countable) family of balls $B_j = B(x_j, \frac{\delta(x_j)}{6}), j \in J$ such that (44), (46), and $\bigcup_j B_{3,j} \subset O$ are also immediate. For the other inclusion, first observe that for $x,y\in X$, if $B(x,\frac{\delta(x)}{6}) \cap B(y,\frac{\delta(y)}{6}) \ne \emptyset$, then

$$
\delta(x) \le \rho(x,y) + \delta(y) \le (\frac{\delta(x)}{6} + \frac{\delta(y)}{6}) + \delta(y) = \frac{\delta(x)}{6} + \frac{7\delta(y)}{6},
$$

so

$$
\delta(x) \le 2 \delta(y).\qquad\text{(47)}
$$

Now let $z\in O$. By maximality, there exists some $j\in J$ with $B(z,\frac{\delta(z)}{6}) \cap B_j \ne \emptyset$. By (47),

$$
\rho(z,x_j)< \frac{\delta(z)}{6} + \frac{\delta(x_j)}{6} \le \frac{3\delta(x_j)}{6} = 3r_j
$$

and thus $z\in B_{3,j}$.

We now turn to the bounded intersection property. Assume that for some $j_1,\dots,j_N$,

$$
z\in \bigcap_{k=1}^N B_{3,j_k}.
$$

Similarly as above, observe for $1\le k \le N$,

$$
\delta(z) \le \rho(z,x_{j_k}) + \delta(x_{j_k}) \le \frac{\delta(x_{j_k})}{2} + \delta(x_{j_k}) = \frac{3\delta(x_{j_k})}{2}\qquad\text{(48)}
$$

and

$$
\delta(x_{j_k}) \le \rho(x_{j_k},z) + \delta(z) \le \frac{\delta(x_{j_k})}{2} + \delta(z),
$$

so

$$
\delta(x_{j_k}) \le 2 \delta(z).\qquad\text{(49)}
$$

By (48) and (49), for all $1\le k \le N$, $B(z,\frac{\delta(z)}{6}) \subset B(x_{j_k}, 5r_{j_k})$ and $B_{j_k} \subset B(z,\frac{8\delta(z)}{6})$. Using this and (44), we obtain

$$
\begin{aligned}
N \mu(B(z,\frac{\delta(z)}{6})) &\le \sum_{k=1}^N \mu(B(x_{j_k}, 5r_j)) \le 2^{3a} \sum_{k=1}^N \mu(B_{j_k}) \\
&= 2^{3a} \mu(\bigcup_{k=1}^N B_{j_k}) \le 2^{3a} \mu(B(z,\frac{8\delta(z)}{6})) \le 2^{6a} \mu(B(z,\frac{\delta(z)}{6}))
\end{aligned}
$$

and conclude $N\le 2^{6a}$.

## Lean

Formalized as [`ball_covering`](https://fpvandoorn.github.io/carleson/docs/find/#doc/ball_covering).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 7620](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L7620)
