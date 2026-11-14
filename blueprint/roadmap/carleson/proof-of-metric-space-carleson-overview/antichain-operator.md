---
declaration: proposition
origin: cited
lean: antichain_operator
statement: formalized
proof: formalized
---

# antichain operator

For any antichain $\mathfrak{A}$ and for all $f:X\to {\mathbb{C}}$ with $|f|\le \mathbf{1}_F$ and all $g:X\to{\mathbb{C}}$ with $|g| \le \mathbf{1}_G$

$$
|\int \overline{g(x)} \sum_{{\mathfrak p} \in \mathfrak{A}} T_{{\mathfrak p}} f(x)\, d\mu(x)|\qquad\text{(28)}
$$

$$
\le \frac{2^{117a^3}}{q-1} \operatorname{\operatorname{dens}}_1(\mathfrak{A})^{\frac {q-1}{8a^4}}\operatorname{\operatorname{dens}}_2(\mathfrak{A})^{\frac 1{q}-\frac 12} \|f\|_2 \|g\|_2\, .
$$

## Depends on

- [dens2 antichain](../proof-of-the-antichain-operator-proposition/dens2-antichain.md)
- [dens1 antichain](../proof-of-the-antichain-operator-proposition/dens1-antichain.md)

## Proof

*Proof of antichain operator.* We have

$$
\left(\frac 1{\tilde{q}} -\frac 12\right) (2-q)= \frac 1q -\frac 12\,.
$$

Multiplying the $(2-q)$-th power of [(4)](../proof-of-the-antichain-operator-proposition/dens2-antichain.md) and the $(q-1)$-th power of [(7)](../proof-of-the-antichain-operator-proposition/dens1-antichain.md) and estimating gives after simplification of some factors

$$
\Big|\int \overline{g(x)} \sum_{{\mathfrak p} \in \mathfrak{A}} T_{{\mathfrak p}} f(x)\, d\mu(x)\Big|\qquad\text{(29)}
$$

$$
\le 2^{117a^3}(q-1)^{-1} \operatorname{\operatorname{dens}}_1(\mathfrak{A})^{\frac {q-1}{2p}}\operatorname{\operatorname{dens}}_2(\mathfrak{A})^{\frac 1{q}-\frac 12} \|f\|_2\|g\|_2\, .
$$

With the definition of $p$, this implies antichain operator.

## Lean

Formalized as [`antichain_operator`](https://fpvandoorn.github.io/carleson/docs/find/#doc/antichain_operator).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 645](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L645)
