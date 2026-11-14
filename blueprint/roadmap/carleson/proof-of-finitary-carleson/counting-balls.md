---
declaration: lemma
origin: cited
lean: counting_balls
statement: formalized
proof: formalized
---

# counting balls

Let $-S\le k\le S$. Consider $Y\subset X$ such that for any $y\in Y$, we have

$$
y\in B(o,4D^S-D^k),\qquad\text{(4)}
$$

furthermore, for any $y'\in Y$ with $y\neq y'$, we have

$$
B(y,D^k)\cap B(y',D^k)=\emptyset.\qquad\text{(5)}
$$

Then the cardinality of $Y$ is bounded by

$$
|Y|\le 2^{3a + 200Sa^3}\, .\qquad\text{(6)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $k$ and $Y$ be given. By applying the doubling property [(5)](../introduction/README.md) inductively, we have for each integer $j\ge 0$

$$
\mu(B(y,2^{j}D^k))\le 2^{aj} \mu(B(y,D^k))\, .\qquad\text{(7)}
$$

Since $X$ is the union of the balls $B(y,2^{j}D^k)$ and $\mu$ is not zero, at least one of the balls $B(y,2^{j}D^k)$ has positive measure, thus $B(y,D^k)$ has positive measure.

Applying (7) for $j' = \ln_2(8D^{2S}) = 3 + 2S \cdot 100a^2$ by [(1)](../proof-of-metric-space-carleson-overview/README.md), using $-S\le k\le S$, $y\in B(o,4D^S)$, and the triangle inequality, we have

$$
B(o, 4D^S) \subset B(y, 8D^S) \subset B(y,2^{j'}D^k) \, .
$$

Using the disjointedness of the balls in (5), (4), and the triangle inequality for $\rho$, we obtain

$$
|Y|\mu(B(o,4D^S))\le 2^{j'a}\sum_{y\in Y}\mu(B(y,D^k))
$$

$$
\le
2^{j'a}\mu(\bigcup_{y\in Y}B(y,D^k))
\le 2^{j'a}\mu(o,4D^S)\, .
$$

As $\mu(o,4D^S)$ is not zero, the lemma follows.

## Lean

Formalized as [`counting_balls`](https://fpvandoorn.github.io/carleson/docs/find/#doc/counting_balls).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 1327](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L1327)
