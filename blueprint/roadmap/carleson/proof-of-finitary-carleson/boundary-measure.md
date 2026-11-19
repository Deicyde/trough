---
declaration: lemma
origin: cited
lean: boundary_measure
statement: formalized
proof: formalized
---

# boundary measure

For each $-S\le k\le S$ and $y\in Y_k$ and $0\lt t<1$ with $tD^k\ge D^{-S}$ we have

$$
\mu(\{x \in I_3(y,k) \ : \ \rho(x, X \setminus I_3(y,k)) \leq t D^{k}\}) \le 2 t^\kappa \mu(I_3(y,k))\,.\qquad\text{(25)}
$$

## Depends on

- [smaller boundary](smaller-boundary.md)

## Proof

Let $x\in I_3(y,k)$ with $\rho(x, X \setminus I_3(y,k)) \leq t D^{k}$. Let $K = 2^{4a+1}$ as in [smaller boundary](smaller-boundary.md). Let $n$ be the largest integer such that $D^{nK} \le \frac{1}{t}$, so that $tD^k \le D^{k-nK}$ and

$$
D^{nK} > \frac{1}{tD^K}\,.\qquad\text{(26)}
$$

Let $k' = k - nK$, by the assumption $tD^k \ge D^{-S}$, we have $k' \ge -S$. By [(13)](cover-by-cubes.md), there exists $y' \in Y_{k'}$ with $x \in I_3(y',k')$. By the squeezing property [(12)](basic-grid-structure.md) and the assumption on $x$, we have

$$
\rho(y', X \setminus I_3(y,k)) \le \rho(x,y') + \rho(x, X \setminus I_3(y,k)) \le 4 D^{k'} + t D^{k}\,.
$$

By the assumption on $n$ and the definition of $k'$, this is

$$
\le 4D^{k'} + D^{k - nK} < 6D^{k'}\,.
$$

Together with [(14)](dyadic-property.md) thus $(y',k'|y,k)$. We have shown that

$$
\{x \in I_3(y,k) \ : \ \rho(x, X \setminus I_3(y,k)) \leq t D^{k}\}
$$

$$
\subset \bigcup_{y'\in Y_{k-nK}: (y',k-nK|y,k)}I_3(y',k-nK)\,.
$$

Using monotonicity and additivity of the measure and [smaller boundary](smaller-boundary.md), we obtain

$$
\mu(\{x \in I_3(y,k) \ : \ \rho(x, X \setminus I_3(y,k)) \leq t D^{k}\}) \le 2^{-n} \mu(I_3(y,k))\,.
$$

By (26) and the definition [(1)](../proof-of-metric-space-carleson-overview/README.md) of $D$, this is bounded by

$$
2 t^{1/(100a^2 K)}  \mu(I_3(y,k))\,,
$$

which completes the proof by the definition [(2)](../proof-of-metric-space-carleson-overview/README.md) of $\kappa$.

## Lean

Formalized as [`boundary_measure`](https://fpvandoorn.github.io/carleson/docs/find/#doc/boundary_measure).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 1683](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L1683)
