---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.KirszbraunWanted.kirszbraun_general, MathlibExt.Analysis.InnerProductSpace.KirszbraunWanted.kirszbraun
statement: formalized
proof: formalized
---

# Kirszbraun theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/kirszbraun-theorem/index.html).

## Kirszbraun extension theorem

Let $E$ be a real inner product space (not necessarily
complete), let $F$ be a complete real inner product space, let $s \subseteq E$ and let $K \ge 0$.
Every map $f : E \to F$ that is $K$-Lipschitz on $s$ agrees on $s$ with some map
$g : E \to F$ that is $K$-Lipschitz on all of $E$.

## Sources

- M. Kirszbraun, Fund. Math. 22 (1934) 77-108 thesis; Valentine 1945 extension to Hilbert; Federer, Geometric Measure Theory, 2.10.43; the Lean theorem takes a real inner-product-space domain `E` and a complete real inner-product-space target `F`, with the same Lipschitz constant `LipschitzWith K`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.KirszbraunWanted.kirszbraun_general`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/Kirszbraun.lean, line 670](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/Kirszbraun.lean#L670). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/kirszbraun-theorem/index.html#kirszbraun-general).

## Kirszbraun extension theorem for Hilbert spaces

Let $E$ and $F$ be real Hilbert spaces,
let $s \subseteq E$ and let $K \ge 0$. Every map $f : E \to F$ that is $K$-Lipschitz on $s$
agrees on $s$ with some map $g : E \to F$ that is $K$-Lipschitz on all of $E$.

Completeness of $E$ is not used: this is a special case of the Kirszbraun extension theorem for
an arbitrary real inner product space domain.

Formalized by `MathlibExt.Analysis.InnerProductSpace.KirszbraunWanted.kirszbraun`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/Kirszbraun.lean, line 705](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/Kirszbraun.lean#L705). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/kirszbraun-theorem/index.html#kirszbraun).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kirszbraun theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/kirszbraun-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/hilbert-spaces/kirszbraun-theorem)
