---
declaration: lemma
origin: cited
lean: book.irrational.lem_aux_iii
statement: formalized
---

# lem_aux_iii

- (iii) The derivatives $f^{(k)}(0)$ and $f^{(k)}(1)$ are integers for all $k \ge 0$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

For (iii) note that by (i) the $k$-th derivative $f^{(k)}$ vanishes at $x=0$ unless $n \le k \le 2n$, and in this range $f^{(k)}(0) = \frac{k!}{n!} c_k$ is an integer. From $f(x) = f(1-x)$ we get $f'(x) = (-1) f'(1-x)$ for all $x$, and hence $f^{(k)}(1) = (-1)^k f^{(k)}(0)$, which is an integer.

## Lean

Stated as [`book.irrational.lem_aux_iii`](https://mo271.github.io/FormalBook/docs/find/#doc/book.irrational.lem_aux_iii); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter08.tex, line 193](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter08.tex#L193)
