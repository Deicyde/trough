---
declaration: lemma
origin: cited
lean: transitive_boundary
statement: formalized
proof: formalized
---

# transitive boundary

Assume $-S\le k''< k'< k\le S$ and $y''\in Y_{k''}$, $y'\in Y_{k'}$, $y\in Y_k$. Assume there is $x\in X$ such that

$$
x\in I_3(y'',k'')\cap I_3(y',k')\cap I_3(y,k)\, .
$$

If $(y'',k''|y,k)$, the also $(y'',k''|y',k')$ and $(y',k'|y,k)$

## Depends on

- [dyadic property](dyadic-property.md)

## Proof

As $x\in I_3(y'',k'')\cap I_3(y',k')$ and $k''< k'$, we have by [dyadic property](dyadic-property.md) that $I_3(y'',k'')\subset I_3(y',k')$. Similarly, $I_3(y',k')\subset I_3(y,k)$. Pick $x'\in X\setminus I_3(y,k)$ such that

$$
\rho(y'',x')< 6D^{k''}\, ,\qquad\text{(17)}
$$

which exists as $(y'',k''|y,k)$. As $x'\in X\setminus I_3(y',k')$ as well, we conclude $(y'',k''| y',k')$. By the triangle inequality, we have

$$
\rho(y',x')\le \rho(y',x)+\rho(x,y'')+\rho(y'',x')
$$

Using the choice of $x$ and [(12)](basic-grid-structure.md) as well as (17), we estimate this by

$$
< 4D^{k'}+4D^{k''}+6D^{k''}\le 6D^{k'}\, ,
$$

where we have used $D>5$ and $k''\lt k'$. We conclude $(y',k'|y,k)$.

## Lean

Formalized as [`transitive_boundary`](https://fpvandoorn.github.io/carleson/docs/find/#doc/transitive_boundary).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 1528](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L1528)
