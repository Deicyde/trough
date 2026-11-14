---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Adapter.qmap, MIPRE.LIDT.Adapter.amap, MIPRE.LIDT.Adapter.hD_qmap
statement: formalized
proof: formalized
---

# The adapter's two maps, and acceptance

Assume $m\mid q$ and fix a family member: a seed position $\sigma(i)$ in each $\chi$-fibre, and a scale $c\neq0$. Let $\rho$ be coordinate reversal on $\mathbb{F}_q^m$. Map a canonical-line question to a seeded one by

$$
\mathtt{point}\ u \mapsto \mathtt{Point}\ \rho u,\qquad
\ell \mapsto (L^{\mathrm{Ln}}_{\rho w}(\rho u_0),\ s_{\sigma},\ c\cdot\rho w),
$$

$w$ the direction of $\ell$ and $u_0$ its base point, with $s_\sigma$ the seed $\sigma$ selects in the fibre of the $\chi$-index of $\rho w$, and the third component omitted for an axis-parallel line. Map a seeded answer back by reading its single component, reparametrizing a diagonal-line polynomial affinely by $t\mapsto c^{-1}t+c^{-1}\mathrm{sh}(\ell)$, where $\mathrm{sh}(\ell)$ is the shift between the two tests' base points for $\ell$, and sending an answer whose format does not match its question to a fixed answer.

Then on every question pair the canonical-line test gives positive weight, every answer pair the seeded test accepts at the images is accepted by the canonical-line test at the originals.

## Depends on

- [Seeded CL low individual degree test](def-lidt-cl.md)
- [Canonical-line low individual degree test](def-lidt.md)
- [Tensor-product strategy](../../foundations/part-01/def-tensor-strategy.md)
- [Orthogonal and canonical complements](../../structure-of-the-proof/part-01/def-cl-canonical.md)

## Proof

Five cases, one per shape of a canonical-line sample: point self-consistency, an axis-parallel line against a point, a diagonal line against a point, and the last two with the roles swapped. The format branches are unreachable, because the seeded test *rejects* an answer whose format does not match its question.

On axis-parallel lines the two tests' base points agree exactly, so the reparametrization is the identity there. On diagonal lines they do not: the seeded base point zeroes the coordinate at the first nonzero entry of $\rho w$, which is the reversal of the *last* nonzero entry of $w$, while the canonical presentation zeroes it at the first. The two parameters of a point of the line therefore differ by the shift $\mathrm{sh}(\ell)$, and by the scale $c$; the affine reparametrization undoes both, and preserves the degree bound because composing with a degree-one polynomial does.

The restriction to the support is not cosmetic: off it the claim is false, a pair of two line questions being a real question pair of the seeded test that the canonical-line test has no subtest for.

## Lean

Formalized as [`MIPRE.LIDT.Adapter.qmap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Adapter.qmap), [`MIPRE.LIDT.Adapter.amap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Adapter.amap), [`MIPRE.LIDT.Adapter.hD_qmap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Adapter.hD_qmap).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 813](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L813)
