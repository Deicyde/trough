---
declaration: lemma
origin: cited
lean: second_exception
statement: formalized
proof: formalized
---

# second exception

We have

$$
\mu(G_2)\le 2^{-2} \mu(G)\, .
$$

## Depends on

- [John Nirenberg](john-nirenberg.md)

## Proof

We use [John Nirenberg](john-nirenberg.md) and sum twice a geometric series to obtain

$$
\sum_{0\le k}\sum_{k\le n}
\mu(A(2n+6,k,n))\le \sum_{0\le k}\sum_{k\le n} 2^{k-5-2n}\mu(G)
$$

$$
\le \sum_{0\le k} 2^{-k-3}\mu(G)\le 2^{-2}\mu(G)\, .
$$

This proves the lemma.

## Lean

Formalized as [`second_exception`](https://fpvandoorn.github.io/carleson/docs/find/#doc/second_exception).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2385](https://github.com/fpvandoorn/carleson/blob/f7487cc9da4d1e73f009dc0280cd5b958f3e2c78/blueprint/src/chapter/main.tex#L2385)
