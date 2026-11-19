# Constructing loops

## Surrounding families

It will be convenient to introduce some more vocabulary.

- [surrounds](def-surrounds.md)

The first main task in proving [Proposition ∃\_loops](../introduction/prop-loops.md) is to construct suitable families of loops $γ_x$ surrounding $g(x)$, by assembling local families of loops. Those will then be reparametrized to get the correct average in the next section. In this section, we will work only with *continuous* loops. This will make constructions easier and we will smooth those loops in the end, taking advantage of the fact that $Ω$ and the surrounding condition are open.

Thanks to Carathéodory's lemma, constructing *one* such loop with values in some open $O$ is easy as soon as $v$ belongs to the convex hull of $O$.

- [loop_of_hull](lem-loop-of-hull.md)
- [family_surrounds](def-family-surrounds.md)

Families of surrounding loops are easy to construct locally.

- [local_loops](lem-local-loops.md)

The difficulty in constructing global families of surrounding loops is that there are plenty of surrounding loops and we need to choose them consistently. The key feature of the above definition is that the $t$ parameter not only allows us to cut out the corrugation process in the next chapter, but also brings a “satisfied or refund” guarantee, as explained in the next lemma.

- [satisfied_or_refund](lem-satisfied-or-refund.md)

The construction below morally proves that each $\operatorname{\mathcal{L}}(g, β, U, Ω)$ is contractible, but we will not even specify a topology on those spaces. The definition of “path connected” in quotation marks is the above specific statement, and only this statement will be used.

*The proof of [Lemma satisfied_or_refund](lem-satisfied-or-refund.md) is shown with its statement.*

- [extend_loops](cor-extend-loops.md)
- [∃\_surrounding_loops](lem-surrounding-loops.md)

## The reparametrization lemma

The second ingredient needed to prove [Proposition ∃\_loops](../introduction/prop-loops.md) is a parametric reparametrization lemma. Gromov's original proof of this lemma makes explicit use of a partition of unity. Motivated in particular by formalization purposes, we will first state more abstract versions whose statements do not involve any partition of unity but directly state a local-to-global property.

- [exists_cont_diff_of_convex](lem-exists-cont-diff-of-convex.md)

We will also need a version where $F$ is a space of smooth functions. Since there is no relevant norm to put on such a space, we cannot deduce this version from the above one.

- [exists_cont_diff_of_convex₂](lem-exists-cont-diff-of-convex2.md)
- [reparametrization](lem-reparametrization.md)

## Proof of the loop construction proposition

We finally assemble the ingredients from the previous two sections.

*Proof of Proposition ∃\_loops: shown with [Proposition ∃\_loops](../introduction/prop-loops.md).*
