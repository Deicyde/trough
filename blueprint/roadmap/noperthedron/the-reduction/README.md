# The reduction

This chapter shows that if $\operatorname{\mathbf{P}}$ is Rupert, then there is a Rupert pair of a special form, with coordinates in a bounded set.

Theorem [rupert_implies_rot_rupert](../rupert-pairs/rupert-sets/thm-rupert-implies-rot-rupert.md) has already removed the translation, leaving two rotations with three parameters each. Rotating both shadows together in the screen preserves containment, so one of these six parameters is redundant. We use two parameters for the outer viewing direction and three for the relative rotation of the inner copy. Concretely, the coordinates reconstruct the pair as

$$
R_o = s(u,v), \qquad R_i = s(u,v)\,B_j\,\mathrm{Cay}(r).
$$

Here $(u,v)$ specifies the outer view (Lemma [outer_view](../cayley-coordinates/outer-views/lem-outer-view.md)), $r=(r_0,r_1,r_2)$ specifies the relative rotation within a chart, and $j\in\{0,\dots,4\}$ is a discrete chart label (Definition [charts](step-c-the-chart/def-charts.md)), not an additional continuous parameter. The symmetries and chart choices below restrict these five coordinates to a bounded domain while preserving a representative of every possible Rupert pair; coordinates need not be unique on chart boundaries or at ties in the symmetry reduction.

Throughout, $g_k = R_z(2\pi k/15)$ for $k = 0, \dots, 14$; these are the rotations in $\mathcal{C}_{30}$, and $\operatorname{\mathbf{P}} = -\operatorname{\mathbf{P}}$.

- [Moves that preserve Rupert pairs](moves-that-preserve-rupert-pairs/README.md)
- [Step A: the outer view](step-a-the-outer-view/README.md)
- [Step B: the relative rotation](step-b-the-relative-rotation/README.md)
- [Step C: the chart](step-c-the-chart/README.md)
- [The reduced domain](the-reduced-domain/README.md)
- [Blowing up charts 0 and 4](blowing-up-charts-0-and-4/README.md)
