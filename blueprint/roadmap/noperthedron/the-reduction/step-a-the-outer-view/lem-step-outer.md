---
declaration: lemma
origin: cited
lean: Cayley.step_flip, Cayley.step_azimuth, Cayley.step_outer
statement: formalized
proof: formalized
---

# step_outer

If there is a Rupert pair in $SO(3)$, then there is one of the form $(s(u, v), R_i)$ with

$$
u \ge 0, \qquad 0 \le v \le \tfrac{57}{128}\, u, \qquad u^2 + v^2 \le 1.
$$

## Depends on

- [Common left factor](../moves-that-preserve-rupert-pairs/lem-move-left.md)
- [Symmetries](../moves-that-preserve-rupert-pairs/lem-move-sym.md)
- [Same view](../moves-that-preserve-rupert-pairs/lem-outer-unique.md)
- [outer_view](../../cayley-coordinates/outer-views/lem-outer-view.md)
- [sin_wedge](../../irrational-data/lem-sin-wedge.md)

## Proof

Let $n$ be the view (third row) of $R_o$. Applying $R_x(\pi)$ on the left if necessary (Lemma [Common left factor](../moves-that-preserve-rupert-pairs/lem-move-left.md)) makes $n_z \ge 0$. Replacing $R_o$ by $R_o g_k$ for a suitable $k$ (Lemma [Symmetries](../moves-that-preserve-rupert-pairs/lem-move-sym.md)) rotates the azimuth of $n$ into $[0, 2\pi/15]$, a wedge in which $n_y \le \frac{57}{128} n_x$ because $\tan(2\pi/15) \le 57/128$ (Lemma [sin_wedge](../../irrational-data/lem-sin-wedge.md)). A view with $n_z \ge 0$ in this wedge is the view of $s(u, v)$ for $(u, v)$ in the stated set (Lemma [outer_view](../../cayley-coordinates/outer-views/lem-outer-view.md)), so $R_o$ can be replaced by $s(u, v)$ (Lemma [Same view](../moves-that-preserve-rupert-pairs/lem-outer-unique.md)).

## Lean

Formalized as [`Cayley.step_flip`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.step_flip), [`Cayley.step_azimuth`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.step_azimuth), [`Cayley.step_outer`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.step_outer).

## Sources

- [Noperthedron blueprint: chapters/reduction.tex, line 87](https://github.com/jcreedcmu/Noperthedron/blob/0143f65be7f59b3ac09b99debb9c37944a0a2f4b/blueprint/src/chapters/reduction.tex#L87)
