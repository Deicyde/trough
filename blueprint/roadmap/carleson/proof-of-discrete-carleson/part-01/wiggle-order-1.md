---
declaration: lemma
origin: cited
lean: smul_mono
statement: formalized
proof: formalized
---

# wiggle order 1

If $n{\mathfrak p} \lesssim m{\mathfrak p}'$ and $n' \ge n$ and $m \ge m'$ then $n'{\mathfrak p} \lesssim m'{\mathfrak p}'$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This follows immediately from the definition [(23)](../../proof-of-metric-space-carleson-overview/README.md) of $\lesssim$ and the two inclusions $B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), n) \subset B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), n')$ and $B_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), m') \subset B_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), m)$.

## Lean

Formalized as [`smul_mono`](https://fpvandoorn.github.io/carleson/docs/find/#doc/smul_mono).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2632](https://github.com/fpvandoorn/carleson/blob/f7487cc9da4d1e73f009dc0280cd5b958f3e2c78/blueprint/src/chapter/main.tex#L2632)
