---
declaration: lemma
origin: cited
lean: TileStructure.Forest.global_tree_control2
statement: formalized
proof: formalized
---

# global tree control 2

We have for all $J \in \mathcal{J}'$ and all bounded $g$ with bounded support

$$
\sup_{B'(J)} |T^*_{{\mathfrak T}({\mathfrak u}_2) \cap \mathfrak{S}} g| \le \inf_{B^\circ{}(J)} |T^*_{{\mathfrak T}({\mathfrak u}_2)} g| + 2^{129a^3} \inf_{J} M_{\mathcal{B},1}|g|\,.
$$

## Depends on

- [global tree control 1](global-tree-control-1.md)
- [local tree control](local-tree-control.md)

## Proof

By [global tree control 1](global-tree-control-1.md)

$$
\sup_{B'(J)} |T^*_{{\mathfrak T}({\mathfrak u}_2) \cap \mathfrak{S}} g| \le \inf_{B^\circ{}(J)} |T_{{\mathfrak T}({\mathfrak u}_2) \cap \mathfrak{S}}^* g| + 2^{128a^3+4a+3} \inf_{J} M_{\mathcal{B}, 1} |g|
$$

$$
\le \inf_{B^\circ{}(J)} |T_{{\mathfrak T}({\mathfrak u}_2)}^* g| + \sup_{B^\circ{}(J)} |T_{{\mathfrak T}({\mathfrak u}_2) \setminus \mathfrak{S}}^* g| + 2^{128a^3+4a+3} \inf_{J} M_{\mathcal{B}, 1} |g|\,,
$$

and by [local tree control](local-tree-control.md)

$$
\le \inf_{B^\circ{}(J)} |T_{{\mathfrak T}({\mathfrak u}_2)}^* g| + (2^{104a^3} + 2^{128a^3+4a+3}) \inf_{J} M_{\mathcal{B}, 1} |g|\,.
$$

This completes the proof.

## Lean

Formalized as [`TileStructure.Forest.global_tree_control2`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.global_tree_control2).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 5852](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L5852)
