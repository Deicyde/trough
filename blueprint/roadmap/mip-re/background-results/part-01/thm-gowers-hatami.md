---
declaration: theorem
origin: cited
lean: MIPRE.gowers_hatami
statement: formalized
proof: formalized
---

# Gowers–Hatami

Let $G$ be a finite group and $f : G \to U(d)$ an $\varepsilon$-approximate representation of $G$. Then there exist $d' \geq d$, an isometry $V : \mathbb{C}^d \to \mathbb{C}^{d'}$, and a representation $\rho : G \to U(d')$ such that

$$
\mathop{\mathbb{E}}_{x \sim G} \, \left\| {f(x) - V^\dagger \rho(x) V} \right\|_{hs}^2 \leq 2 \varepsilon\;.
$$

## Depends on

- [Normalized Hilbert–Schmidt norm](../../foundations/part-02/def-hs-norm.md)
- [Approximate representation](def-approx-rep.md)

## Proof

Let $L(G, \mathbb{C}^d) \cong \mathbb{C}^{|G| d}$ carry the inner product normalized by $1/|G|$, let $V : \mathbb{C}^d \to L(G, \mathbb{C}^d)$ be the map $u \mapsto (x \mapsto f(x) u)$, and let $\rho$ be the right regular representation, $(\rho(x) F)(y) = F(yx)$. Then $V$ is an isometry, and the compression $V^\dagger \rho(x) V = \mathop{\mathbb{E}}_{y \sim G} f(y)^\dagger f(yx)$ is an average of unitaries, hence has squared Hilbert–Schmidt norm at most $1$. Moreover $\mathop{\mathbb{E}}_{x} \mathrm{Re}\, \langle f(x), V^\dagger \rho(x) V \rangle_{hs} = \mathop{\mathbb{E}}_{x, y} \mathrm{Re}\, \langle f(x) f(y), f(xy) \rangle_{hs} \geq 1 - \varepsilon$ by hypothesis, and the claim follows by expanding $\left\| {f(x) - V^\dagger \rho(x) V} \right\|_{hs}^2$. The construction gives $d' = |G|\, d$.

## Lean

Formalized as [`MIPRE.gowers_hatami`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.gowers_hatami).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 82](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L82)
