---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.gramPair, MIPRE.LowDegree.gramPair_ofAlg, MIPRE.LowDegree.isUnit_gram, MIPRE.LowDegree.exists_gramPair_eq_one, MIPRE.LowDegree.exists_isSelfDualBasis_isNormalBasis, MIPRE.LowDegree.exists_selfDualNormalBasis_two
statement: formalized
proof: formalized
---

# Existence of a self-dual normal basis

Let $K / \mathbb{F}$ be a Galois extension of finite fields of characteristic two whose degree is odd. Then $K$ has a basis over $\mathbb{F}$ that is at once normal and self-dual. In particular $\mathbb{F}_{2^k}$ has a self-dual normal basis over $\mathbb{F}_2$ for every odd $k \geq 1$.

## Depends on

- [Self-dual and normal bases](def-self-dual-basis.md)
- [Self-dualization in the group algebra](lem-group-algebra-selfdualization.md)

## Proof

Let $G = \mathrm{Gal}(K/\mathbb{F})$, which is cyclic, hence abelian, so $\mathbb{F}[G]$ is a commutative ring, and $\left\vert {G} \right\vert = [K : \mathbb{F}]$ is odd. Let $\alpha$ be the normal element Mathlib's normal basis theorem supplies, write $\mathrm{ofAlg}(a)$ for the element of $K$ with normal-basis coordinates $a \in \mathbb{F}[G]$, and let

$$
c(x, y) \in \mathbb{F}[G], \qquad c(x, y)_g = \mathrm{tr}(x \cdot g y), \qquad c = c(\alpha, \alpha).
$$

Because $\mathrm{tr} \circ g = \mathrm{tr}$, the pairing of two members of one orbit depends only on their ratio, and expanding both coordinate sums gives the transformation law

$$
c(\mathrm{ofAlg}(a), \mathrm{ofAlg}(b)) = a \cdot \tau(b) \cdot c,
$$

where $\tau$ is the involution of $\mathbb{F}[G]$ induced by $g \mapsto g^{-1}$. The element $c$ is fixed by $\tau$, because $\mathrm{tr}(\alpha \cdot g^{-1}\alpha) = \mathrm{tr}(g\alpha \cdot \alpha)$, and it is a unit: if $c \cdot z = 0$ then the transformation law with $b = \tau(z)$ makes $\mathrm{tr}(\mathrm{ofAlg}(\tau z) \cdot x)$ vanish for every $x \in K$, so $\mathrm{ofAlg}(\tau z) = 0$ by nondegeneracy of the trace form, so $z = 0$; a non-zero-divisor in a finite commutative ring is a unit. Then $c^{-1}$ is also $\tau$-fixed, and Lemma [Self-dualization in the group algebra](lem-group-algebra-selfdualization.md) — squaring is bijective on $\mathbb{F}[G]$ in characteristic two with $\left\vert {G} \right\vert$ odd — gives $a$ with $a \cdot \tau(a) = c^{-1}$. For $\beta = \mathrm{ofAlg}(a)$ the transformation law reads $c(\beta, \beta) = 1$, which says exactly that the Frobenius orbit of $\beta$ is orthonormal for the trace form. It is in particular linearly independent, so it is a basis, and it is normal by construction.

## Lean

Formalized as [`MIPRE.LowDegree.gramPair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.gramPair), [`MIPRE.LowDegree.gramPair_ofAlg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.gramPair_ofAlg), [`MIPRE.LowDegree.isUnit_gram`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.isUnit_gram), [`MIPRE.LowDegree.exists_gramPair_eq_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.exists_gramPair_eq_one), [`MIPRE.LowDegree.exists_isSelfDualBasis_isNormalBasis`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.exists_isSelfDualBasis_isNormalBasis), [`MIPRE.LowDegree.exists_selfDualNormalBasis_two`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.exists_selfDualNormalBasis_two).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6463](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6463)
