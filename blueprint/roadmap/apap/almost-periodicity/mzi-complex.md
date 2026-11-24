---
declaration: lemma
origin: cited
lean: RCLike.marcinkiewicz_zygmund
statement: formalized
proof: formalized
---

# Complex-valued Marcinkiewicz-Zygmund inequality

Let $m\geq 1$. If $f:G\to\mathbb{C}$ is such that $\mathbb{E}_x f(x)=0$ and $\left\lvert f(x)\right\rvert\leq 2$ for all $x$ then

$$
\mathbb{E}_{x_1,\ldots,x_n} \left\lvert \sum_{i=1}^n f(x_i)\right\rvert^{2m} \leq (8mn)^{m}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Marcinkiewicz-Zygmund inequality](mzi.md)

## Lean

Formalized as [`RCLike.marcinkiewicz_zygmund`](https://yaeldillies.github.io/apap/docs/find/#doc/RCLike.marcinkiewicz_zygmund).

## Sources

- [Kelley-Meka bound blueprint: chapter/ap.tex, line 39](https://github.com/YaelDillies/apap/blob/b401f6e22417e6dbe6f87d6620571ea6c513aed3/blueprint/src/chapter/ap.tex#L39)
