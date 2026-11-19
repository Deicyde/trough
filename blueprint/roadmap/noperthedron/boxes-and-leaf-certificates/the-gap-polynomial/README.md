# The gap polynomial

Fix a box in chart $j$, an inner vertex $S$, an outer vertex $T$ and a direction $w \in \operatorname{\mathbb{Z}}^2 \setminus \{0\}$. The separation criterion (Theorem [Separation criterion](../../rupert-pairs/shadows-and-the-separation-criterion/thm-separation.md)) asks for

$$
\mathrm{gap}_T(X) = \langle w, s\, Q_j(r)\, S \rangle - \langle w, s\, T \rangle \ge 0,
\qquad s = s(X_0, X_1).
$$

Multiplying by the positive denominators $D_o = 1 + u^2 + v^2$ and $D_r = D(r)$ and by an integer $\kappa_j \ge 1$ that makes $M_j = \kappa_j B_j$ an integer matrix ($\kappa_j = 1$ for $j \le 3$, and $\kappa_4 = x^2 + y^2$ in the notation of Definition [tau](../../the-reduction/step-b-the-relative-rotation/def-tau.md), after scaling $C_3$ to integers) clears every denominator.

- [Gap polynomial](lem-gap-poly.md)

The checker uses dyadic approximations $\hat S$, $\hat T$ of the vertices with error at most $2^{-60}$ per coordinate (Lemma [vertex_approx](../../irrational-data/lem-vertex-approx.md)). The error is absorbed by an explicit allowance $\mathrm{err} = 128\, \kappa_j\, 2^{-60} (|w_0| + |w_1|)$; this uses $u^2 + v^2 \le 1$, $|r_i| \le 2$ and the fact that orthogonal matrices do not enlarge vectors.
