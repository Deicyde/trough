---
declaration: lemma
origin: cited
lean: TileStructure.Forest.holder_correlation_tile
statement: formalized
proof: formalized
---

# Holder correlation tile

Let ${\mathfrak u} \in {\mathfrak U}$ and ${\mathfrak p} \in {\mathfrak T}({\mathfrak u})$. Then for all $y, y' \in X$ and all bounded $g$ with bounded support, we have

$$
|e({\mathcal{Q}}({\mathfrak u})(y)) T_{{\mathfrak p}}^* g(y) - e({\mathcal{Q}}({\mathfrak u})(y')) T_{{\mathfrak p}}^* g(y')|
$$

$$
\le \frac{2^{128a^3}}{\mu(B({\mathrm{c}}({\mathfrak p}), 4D^{{\mathrm{s}}({\mathfrak p})}))} \left(\frac{\rho(y, y')}{D^{{\mathrm{s}}({\mathfrak p})}}\right)^{1/a} \int_{E({\mathfrak p})} |g(x)| \, \mathrm{d}\mu(x)\,.\qquad\text{(46)}
$$

## Depends on

- [adjoint tile support](../part-01/adjoint-tile-support.md)

## Proof

By [(25)](../part-01/README.md), we have

$$
|e({\mathcal{Q}}({\mathfrak u})(y)) T_{{\mathfrak p}}^* g(y) - e({\mathcal{Q}}({\mathfrak u})(y')) T_{{\mathfrak p}}^* g(y')|
$$

$$
\begin{gathered}
=\bigg| \int_{E({\mathfrak p})} e({Q}(x)(x) - {Q}(x)(y) + {\mathcal{Q}}({\mathfrak u})(y)) \overline{K_{{\mathrm{s}}({\mathfrak p})}(x, y)} g(x) \\
- e({Q}(x)(x) - {Q}(x)(y') + {\mathcal{Q}}({\mathfrak u})(y')) \overline{K_{{\mathrm{s}}({\mathfrak p})}(x, y')} g(x) \, \mathrm{d}\mu(x)\bigg|
\end{gathered}
$$

$$
\begin{gathered}
\leq\int_{E({\mathfrak p})} |g(x)| |e({Q}(x)(y) - {Q}(x)(y') - {\mathcal{Q}}({\mathfrak u})(y) + {\mathcal{Q}}({\mathfrak u})(y'))\overline{K_{{\mathrm{s}}({\mathfrak p})}(x, y)}\\
- \overline{K_{{\mathrm{s}}({\mathfrak p})}(x, y')}| \, \mathrm{d}\mu(x)
\end{gathered}
$$

$$
\begin{gathered}
\leq\int_{E({\mathfrak p})} |g(x)| |e(-{Q}(x)(y) + {Q}(x)(y') + {\mathcal{Q}}({\mathfrak u})(y) - {\mathcal{Q}}({\mathfrak u})(y')) - 1| \\
\times |\overline{K_{{\mathrm{s}}({\mathfrak p})}(x, y)}|\, \mathrm{d}\mu(x)\qquad\text{(47)}\end{gathered}
$$

$$
+ \int_{E({\mathfrak p})} |g(x)| |\overline{K_{{\mathrm{s}}({\mathfrak p})}(x, y)} - \overline{K_{{\mathrm{s}}({\mathfrak p})}(x, y')} |\, \mathrm{d}\mu(x)\,.\qquad\text{(48)}
$$

By the oscillation estimate [(7)](../../introduction/README.md), we have

$$
|-{Q}(x)(y) + {Q}(x)(y') + {\mathcal{Q}}({\mathfrak u})(y) - {\mathcal{Q}}({\mathfrak u})(y')|
$$

$$
\le d_{B(y, 1.6\rho(y,y'))}({Q}(x), {\mathcal{Q}}({\mathfrak u}))\,.\qquad\text{(49)}
$$

Suppose that $y, y' \in B({\mathrm{c}}({\mathfrak p}), 5D^{{\mathrm{s}}({\mathfrak p})})$, so that $\rho(y,y') \le 10D^{{\mathrm{s}}({\mathfrak p})}$. Let $k \in \mathbb{Z}$ be such that $2^{ak}\rho(y,y') \le 10D^{{\mathrm{s}}({\mathfrak p})}$ but $2^{a(k+1)} \rho(y,y') > 10D^{{\mathrm{s}}({\mathfrak p})}$. In particular, $k \ge 0$. Then, using [(10)](../../introduction/README.md) followed by [(8)](../../introduction/README.md), we can bound (49) from above by

$$
2^{-k} d_{B({\mathrm{c}}({\mathfrak p}), 16 D^{{\mathrm{s}}({\mathfrak p})})}({Q}(x), {\mathcal{Q}}({\mathfrak u})) \le 2^{6a - k} d_{{\mathfrak p}}({Q}(x), {\mathcal{Q}}({\mathfrak u}))\,.
$$

Since $x \in E({\mathfrak p})$ we have ${Q}(x) \in \Omega({\mathfrak p}) \subset B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), 1)$, and since ${\mathfrak p} \in {\mathfrak T}({\mathfrak u})$ we have ${\mathcal{Q}}({\mathfrak u}) \in B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), 4)$, so this is estimated by

$$
\le 5 \cdot 2^{6a - k}\,.
$$

By definition of $k$, we have

$$
-k < 1 - \frac{1}{a} \log_2\left(\frac{10 D^{{\mathrm{s}}({\mathfrak p})}}{\rho(y,y')}\right)\,,
$$

which gives

$$
|-{Q}(x)(y) + {Q}(x)(y') + {\mathcal{Q}}({\mathfrak u})(y) - {\mathcal{Q}}({\mathfrak u})(y')| \le 10 \cdot 2^{6a} \left(\frac{\rho(y,y')}{10 D^{{\mathrm{s}}({\mathfrak p})}}\right)^{1/a}\,.\qquad\text{(50)}
$$

For all $x \in {\mathcal{I}}({\mathfrak p})$, we have by [(5)](../../introduction/README.md) that

$$
\mu(B(x, D^{{\mathrm{s}}({\mathfrak p})})) \ge 2^{-3a} \mu(B({\mathrm{c}}({\mathfrak p}), 4D^{{\mathrm{s}}({\mathfrak p})}))\,.
$$

Combining the above with [(66)](../../proof-of-metric-space-carleson-overview/kernel-summand.md), [(67)](../../proof-of-metric-space-carleson-overview/kernel-summand.md) and (50), we obtain

$$
\eqref{T*Holder1b}+\eqref{T*Holder1} \le \frac{2^{3a}}{\mu(B({\mathrm{c}}({\mathfrak p}), 4D^{{\mathrm{s}}({\mathfrak p})}))} \int_{E({\mathfrak p})}|g(x)| \, \mathrm{d}\mu(x) \times
$$

$$
(2^{102a^3} \cdot 10 \cdot 2^{6a} \left(\frac{\rho(y,y')}{ D^{{\mathrm{s}}({\mathfrak p})}}\right)^{1/a} + 2^{127a^3} \left(\frac{\rho(y,y')}{D^{{\mathrm{s}}({\mathfrak p})}}\right)^{1/a})
$$

Since $\rho(y,y') \le 10 D^{{\mathrm{s}}({\mathfrak p})}$, we conclude

$$
\eqref{T*Holder1b}+\eqref{T*Holder1} \le \frac{2^{128a^3}}{\mu(B({\mathrm{c}}({\mathfrak p}), 4D^{{\mathrm{s}}({\mathfrak p})}))} \left(\frac{\rho(y,y')}{D^{{\mathrm{s}}({\mathfrak p})}}\right)^{1/a} \int_{E({\mathfrak p})}|g(x)| \, \mathrm{d}\mu(x)\,.
$$

Next, if $y,y' \notin B({\mathrm{c}}({\mathfrak p}), 5D^{{\mathrm{s}}({\mathfrak p})})$, then $T_{{\mathfrak p}}^*g(y) = T_{{\mathfrak p}}^*g(y') = 0$, by [adjoint tile support](../part-01/adjoint-tile-support.md). Then (46) holds.

Finally, if $y \in B({\mathrm{c}}({\mathfrak p}), 5D^{{\mathrm{s}}({\mathfrak p})})$ and $y' \notin B({\mathrm{c}}({\mathfrak p}), 5D^{{\mathrm{s}}({\mathfrak p})})$, then

$$
|e({\mathcal{Q}}({\mathfrak u})(y)) T_{{\mathfrak p}}^* g(y) - e({\mathcal{Q}}({\mathfrak u})(y')) T_{{\mathfrak p}}^* g(y')| = |T_{{\mathfrak p}}^* g(y)|
$$

$$
\le \int_{E({\mathfrak p})} |K_{{\mathrm{s}}({\mathfrak p})}(x,y)| |g(x)| \, \mathrm{d}\mu(x)\,.
$$

By the same argument used to prove [(69)](../../proof-of-metric-space-carleson-overview/kernel-summand.md), this is bounded by

$$
\le 2^{102a^3} \int_{E({\mathfrak p})} \frac{1}{\mu(B(x, D^s))} \psi(D^{-s} \rho(x,y)) |g(x)| \, \mathrm{d}\mu(x)\,.\qquad\text{(51)}
$$

It follows from the definition of $\psi$ that

$$
\psi(x) \le \max\{0, (2 - 4x)^{1/a}\}\,.
$$

Now for all $x\in E({\mathfrak p})$, it follows by the triangle inequality and [(10)](../../proof-of-metric-space-carleson-overview/README.md) that

$$
\begin{gathered}
2 - 4D^{-{\mathrm{s}}({\mathfrak p})}\rho(x,y)\leq 2 - 4D^{-{\mathrm{s}}({\mathfrak p})}\rho(y, {\mathrm{c}}({\mathfrak p})) + 4 D^{-{\mathrm{s}}({\mathfrak p})}\rho(x, {\mathrm{c}}({\mathfrak p}))\\\leq 18 - 4 D^{-{\mathrm{s}}({\mathfrak p})} \rho(y, {\mathrm{c}}({\mathfrak p})) \leq 4 D^{-{\mathrm{s}}({\mathfrak p})}\rho(y,y') - 2 .
\end{gathered}
$$

Combining the above with the previous estimate on $\psi$, we get

$$
\psi(D^{-{\mathrm{s}}({\mathfrak p})}\rho(x,y)) \le 4 (D^{-{\mathrm{s}}({\mathfrak p})}\rho(y,y'))^{1/a}.
$$

Further, we obtain from the doubling property [(5)](../../introduction/README.md) and [(10)](../../proof-of-metric-space-carleson-overview/README.md) that

$$
\mu(B(x, D^{{\mathrm{s}}({\mathfrak p})})) \ge 2^{-3a} \mu(B({\mathrm{c}}({\mathfrak p}), 4D^{{\mathrm{s}}({\mathfrak p})}))\,.
$$

Plugging this into (51) and using $a \ge 4$, we get

$$
|T_{{\mathfrak p}}^* g(y)| \le \frac{2^{103a^3}}{\mu(B({\mathrm{c}}({\mathfrak p}), 4D^{{\mathrm{s}}({\mathfrak p})}))} \left(\frac{\rho(y,y')}{D^{{\mathrm{s}}({\mathfrak p})}}\right)^{1/a} \int_{E({\mathfrak p})} |g(x)| \, \mathrm{d}\mu(y)\,,
$$

which completes the proof of the lemma.

## Lean

Formalized as [`TileStructure.Forest.holder_correlation_tile`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.holder_correlation_tile).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 5562](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L5562)
