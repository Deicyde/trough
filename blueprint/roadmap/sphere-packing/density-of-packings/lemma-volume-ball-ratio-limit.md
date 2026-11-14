---
declaration: lemma
origin: cited
lean: volume_ball_ratio_tendsto_nhds_one''
statement: formalized
proof: formalized
---

# volume-ball-ratio-limit

For any constant $C > 0$, we have

$$
\lim_{R \to \infty} \frac{\mathrm{Vol}(\mathcal{B}_d(R))}{\mathrm{Vol}(\mathcal{B}_d(R + C))} = 1
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Write out the formula for volume of a ball and simplify. More specifically, we have $\mathrm{Vol}(\mathcal{B}_d(R)) = R^d \pi^{d / 2} / \Gamma\left(\frac{d}{2} + 1\right)$, so $\mathrm{Vol}(\mathcal{B}_d(R)) / \mathrm{Vol}(\mathcal{B}_d(R + C)) = R^d / (R + C)^d = \left(1 - \frac{1}{R + C}\right)^d = 1$.

## Lean

Formalized as [`volume_ball_ratio_tendsto_nhds_one''`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/volume_ball_ratio_tendsto_nhds_one'').

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/packings-density.tex, line 62](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/packings-density.tex#L62)
