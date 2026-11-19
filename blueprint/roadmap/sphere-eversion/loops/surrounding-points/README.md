# Surrounding points

This section collects elementary results about convex sets in finite dimensional real vector spaces that will help to construct families of loops. In this section, $E$ is a real vector space with (finite) dimension $d$. The discussion will center around the following definition which is tailored to our ulterior needs.

- [surrounds_points](def-surrounds-points.md)

Note that, in the above definition, the number of points $p_i$ is fixed by the dimension $d$ of $E$, and that the weights $w_i$ are the barycentric coordinates of $x$ with respect to the affine basis $p_0, \ldots, p_d$.

The first important point in this definition is that surrounding is smoothly locally stable: if $x$ is surrounded by a collection of points $p$ then points that are close to $y$ are surrounded by every collection of points $q$ that is closed to $p$, and the relevant barycentric coordinates smoothly depend on $y$ and $q$. The precise statement follows.

- [smooth_barycentric_coord](lem-smooth-barycentric-coord.md)

Then we need a criterion ensuring a point $x$ is surrounded by a collection of points taken in a given subset $P$. The first temptation is to hope that $x$ being in the interior of the convex hull of $P$ is enough. But this is not true. For instance the center of a square in a plane is in the interior of the convex hull of the set $P$ of vertices of the square, but it isn't surrounded by any set of vertices. This counter example also shows that the stability lemma above is slightly less trivial than it sounds.

The rest of this section is devoted to the following result that proves no such issue arises when $P$ is open.

- [surrounded_by_open](prop-surrounded-by-open.md)

This proposition will be proven at the end of this section. We'll first need the Carathéodory lemma:

- [Carathéodory's lemma](lem-caratheodory.md)
- [interior_chab](lem-interior-chab.md)
- [int_homothety_cvx](lem-int-homothety-cvx.md)

We are now ready to come back to [Proposition surrounded_by_open](prop-surrounded-by-open.md).

*Proof of Proposition surrounded_by_open: shown with [Proposition surrounded_by_open](prop-surrounded-by-open.md).*
