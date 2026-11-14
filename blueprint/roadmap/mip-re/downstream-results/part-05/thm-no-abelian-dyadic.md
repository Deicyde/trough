---
declaration: theorem
origin: cited
lean: MIPRE.mul_star_le_mul_of_commute, MIPRE.VecTrace.tr, MIPRE.VecTrace.tr_one, MIPRE.VecTrace.tr_mul_comm, MIPRE.VecTrace.re_tr_nonneg, MIPRE.VecTrace.re_tr_mono, MIPRE.VecTrace.tr_star_mul_self, MIPRE.VecTrace.card_mul_re_tr_le_one, MIPRE.VecTrace.eq_zero_of_dyadicUnits, MIPRE.BipartiteModel.mul_mem_opsA, MIPRE.BipartiteModel.star_mem_opsA, MIPRE.BipartiteModel.IsFinitePair.eq_zero_of_abelianA, MIPRE.BipartiteModel.IsFinitePair.eq_zero_of_abelianB
statement: formalized
proof: formalized
---

# Dyadic matrix units exclude abelian projections

Let $s$ be a set of bounded operators on a Hilbert space, closed under products and adjoints, with a vector trace $\tau$ (Definition [Finite pairs](../part-04/def-finite-pair.md)), extended to all operators by $\tau(T) = \sum_k \langle g_k, T g_k \rangle$. Call a projection $p \in s$ *abelian* in $s$ if $(pxp)(pyp) = (pyp)(pxp)$ for all $x, y \in s$, and let $p$ be one.

- (K1) If $s$ contains unital matrix units $(f_{ij})_{i, j \in \iota}$ (Definition [Unital dyadic matrix units](def-dyadic-units.md)), then $\left\vert {\iota} \right\vert \cdot \mathrm{Re}\, \tau(p) \leq 1$.
- (K2) If $s$ contains unital dyadic matrix units, then $p = 0$.
- (K$'$) In a finite pair whose first player's algebra has unital dyadic matrix units, the first player's operators contain no nonzero abelian projection; and likewise for the second player.

## Depends on

- [Finite pairs](../part-04/def-finite-pair.md)
- [Finite pairs are closed under ancilla extensions](../part-04/lem-finite-pair-expand.md)
- [Transport of dyadic matrix units](lem-dyadic-units-closure.md)

## Proof

The tool is a Cauchy–Schwarz inequality in a commutative corner: for operators $x, y$ with $\alpha = x^* x$, $\beta = y^* y$ and $\gamma = x^* y$, if $\alpha$ commutes with $\beta$ and $\beta$ with $\gamma$, then $\gamma \gamma^* \leq \alpha \beta$. For $\varepsilon > 0$ the operator $b = \beta + \varepsilon$ is invertible and positive and commutes with $\alpha$, $\gamma$ and $\gamma^*$; with $z = x b - y \gamma^*$, $b (\alpha b - \gamma \gamma^*) = z^* z + \varepsilon \gamma \gamma^* \geq 0$, so $\alpha b - \gamma \gamma^* \geq 0$, and $\varepsilon \to 0$ gives the claim, the positive cone being closed.

For (K1), fix $i_0 \in \iota$ and put $w_i = f_{i_0 i}\, p$ and $a_{ij} = w_i^* w_j = p f_{ij} p$. The $a_{ij}$ commute pairwise because $p$ is abelian, $\sum_i a_{ii} = p$, and $a_{ij} a_{ij}^* \leq a_{ii} a_{jj}$ by the corner inequality. The operator $X = \sum_i w_i w_i^*$ is self-adjoint and $f_{i_0 i_0} X = X = X f_{i_0 i_0}$; by traciality $\tau(X) = \tau(p)$ and $\mathrm{Re}\, \tau(X^2) = \sum_{i, j} \mathrm{Re}\, \tau(a_{ij} a_{ij}^*) \leq \mathrm{Re}\, \tau(p)$, and $\tau(f_{ii}) = \tau(f_{i_0 i_0})$ for every $i$, so $\tau(f_{i_0 i_0}) = 1/\left\vert {\iota} \right\vert$. With $t = \mathrm{Re}\, \tau(p) \geq 0$, the positivity of $(X - c f_{i_0 i_0})^* (X - c f_{i_0 i_0}) = X^2 - 2cX + c^2 f_{i_0 i_0}$ for real $c$ gives $0 \leq t - 2ct + c^2/\left\vert {\iota} \right\vert$, and $c = \left\vert {\iota} \right\vert\, t$ gives $t (1 - \left\vert {\iota} \right\vert\, t) \geq 0$. For (K2), $2^n t \leq 1$ for every $n$, so $t = 0$; and $\tau(p) = \tau(p^* p) = \sum_k \|p g_k\|^2$, so $p$ kills every $g_k$ and vanishes, the family separating $s$. For (K$'$), the first player's operators are the image of a $*$-homomorphism, hence closed under products and adjoints; they carry the vector trace of the finite pair, and contain the images of the units (Lemma [Transport of dyadic matrix units](lem-dyadic-units-closure.md)). The second player's case is the first for the model with the players exchanged, again a finite pair (Lemma [Finite pairs are closed under ancilla extensions](../part-04/lem-finite-pair-expand.md)). No comparison theory and no centre-valued trace is used. The full proof is `reports/c6b-paper-proofs.md`, Section 3, Theorems K and K$'$ (Lemmas 1–4 and 6).

## Lean

Formalized as [`MIPRE.mul_star_le_mul_of_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.mul_star_le_mul_of_commute), [`MIPRE.VecTrace.tr`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.VecTrace.tr), [`MIPRE.VecTrace.tr_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.VecTrace.tr_one), [`MIPRE.VecTrace.tr_mul_comm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.VecTrace.tr_mul_comm), [`MIPRE.VecTrace.re_tr_nonneg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.VecTrace.re_tr_nonneg), [`MIPRE.VecTrace.re_tr_mono`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.VecTrace.re_tr_mono), [`MIPRE.VecTrace.tr_star_mul_self`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.VecTrace.tr_star_mul_self), [`MIPRE.VecTrace.card_mul_re_tr_le_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.VecTrace.card_mul_re_tr_le_one), [`MIPRE.VecTrace.eq_zero_of_dyadicUnits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.VecTrace.eq_zero_of_dyadicUnits), [`MIPRE.BipartiteModel.mul_mem_opsA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.mul_mem_opsA), [`MIPRE.BipartiteModel.star_mem_opsA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.star_mem_opsA), [`MIPRE.BipartiteModel.IsFinitePair.eq_zero_of_abelianA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.IsFinitePair.eq_zero_of_abelianA), [`MIPRE.BipartiteModel.IsFinitePair.eq_zero_of_abelianB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.IsFinitePair.eq_zero_of_abelianB).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2914](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2914)
