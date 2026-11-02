---
declaration: lemma
origin: cited
lean: multidist_ruzsa_IV
statement: formalized
proof: formalized
---

# Multidistance and Ruzsa distance, IV

Let $m \ge 2$, and let $X_{[m]}$ be a tuple of independent $G$-valued random variables. Let $W := \sum_{i=1}^m X_i$. Then

$$
d[W;-W] \leq 2 D[X_i].
$$

## Depends on

- [Multidistance](multidist-def.md)

## Proof depends on

- [Existence of independent copies](../../entropic-ruzsa-calculus/part-01/independent-exist.md)
- [Kaimanovich-Vershik-Madiman inequality](../../entropic-ruzsa-calculus/part-02/kv.md)
- [Independent lower bound on sumset](../../entropic-ruzsa-calculus/part-01/sumset-lower.md)
- [Ruzsa distance in independent case](../../entropic-ruzsa-calculus/part-01/ruz-indep.md)
- [Multidistance of independent variables](multidist-indep.md)

## Proof

Take $(X'_i)_{1 \leq i \leq m}$ to be further independent copies of $(X_i)_{1 \leq i \leq m}$ (which exist by [Existence of independent copies](../../entropic-ruzsa-calculus/part-01/independent-exist.md)), and write $W' := \sum_{i=1}^m X'_i$. Fix any distinct $a,b \in I$.

From [Kaimanovich-Vershik-Madiman inequality](../../entropic-ruzsa-calculus/part-02/kv.md) one has

$$
\mathbb{H}[W + W'] \leq  \mathbb{H}[W] + \mathbb{H}[X_{a} + W'] - \mathbb{H}[X_{a}]\qquad\text{(1)}
$$

and also

$$
\mathbb{H}[X_a + W'] \leq \mathbb{H}[X_a + X_b] + \mathbb{H}[W'] - \mathbb{H}[X'_b].
$$

Combining this with (1) and then applying [Independent lower bound on sumset](../../entropic-ruzsa-calculus/part-01/sumset-lower.md) we have

$$
\begin{aligned}  \mathbb{H}[W + W']  & \leq    2\mathbb{H}[W] + \mathbb{H}[X_a + X_b]  - \mathbb{H}[X_a] - \mathbb{H}[X_b] \\ & \leq
3 \mathbb{H}[W] - \mathbb{H}[X_a] - \mathbb{H}[X_b].
\end{aligned}
$$

Averaging this over all choices of $(a,b)$ gives $\mathbb{H}[W] + 2 D[X_{[m]}]$, and the claim follows from [Ruzsa distance in independent case](../../entropic-ruzsa-calculus/part-01/ruz-indep.md).

## Lean

Formalized as [`multidist_ruzsa_IV`](https://teorth.github.io/pfr/docs/find/#doc/multidist_ruzsa_IV).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 246](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L246)
