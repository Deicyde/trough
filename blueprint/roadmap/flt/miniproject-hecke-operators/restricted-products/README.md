# Restricted products

In the concrete example of Hecke operators which we care about, the invariants $A^G$ will be spaces of quaternionic automorphic forms (by definition). We do not need to worry about the definition of $A$ in this project at all. However we will need to do various computations with the specific groups $G$ which we are interested in, and they are restricted products. So we now develop some theory for restricted products, starting by recalling the definition.

If $I$ is an index set, if $X_i$ are sets indexed by $i\in I$ and if $Y_i$ are subsets, then the *restricted product* $\prod'_iX_i$ (note the dash) is defined to be the subset of the full product $\prod_i X_i$ consisting of those tuples $(x_i)$ such that $x_i\in Y_i$ for all but finitely many $i$. We suppress the $Y_i$ from the notation in this document, although in Lean we cannot do this and the restricted product looks something like $\prod{}^{r} i,[X\ i, Y\ i]$.

It is straightforward to check that if the $X_i$ are groups or rings or $R$-modules, and the $Y_i$ are subgroups or subrings or submodules, then the restricted product is a group, ring or $R$-module; indeed the structure is inherited via the inclusion $\prod'_iX_i\subseteq\prod_iX_i$ (and the fact that arbitrary products of groups/rings/modules are groups/rings/modules).

More subtle is the theory of topological space structures. If the $X_i$ are topological spaces then we do *not* give $\prod'_iX_i$ the subspace topology coming from the product topology on $\prod_iX_i$; instead we give it the finest topology making all of the natural maps $\prod_{i\in S}X_i\times\prod_{i\notin S}Y_i\to \prod'_iX_i$ continuous, as $S$ runs through all finite subsets of $I$; here the product of $X_i$s and $Y_i$s has the product topology. For example if all of the $Y_i$ are open then one can check that $\prod_iY_i$ is an open subset of $\prod'_iX_i$ (this is RestrictedProduct.isOpen\_forall\_mem in mathlib), whereas it is not of the form $\left(\prod'_iX_i\right)\cap U$ for any open subset $U$ of $\prod_iX_i$ in general; the map from $\prod'_i X_i$ to $\prod_i X_i$ is continuous but is not in general an embedding.

If you've seen automorphic forms before, then here is an obvious-sounding claim: because the adeles $\mathbb{A}_F$ of a number field are a restricted product of completions $F_v$ with respect to the integer rings $\mathcal{O}_v$, then $GL_2(\mathbb{A}_F)$ is obviously topologically a restricted product of $GL_2(F_v)$ with respect to $GL_2(\mathcal{O}_v)$. We now spend some time justifying this claim, which is a little more intricate than it sounds.

## Products

Here are some basic facts we need about restricted products.

- [Homeomorph.restrictedProductProd](homeomorph-restrictedproductprod.md)

**Remark.** This may well not be true if $B_i$ and $D_i$ are not open, because filtered colimits and binary products do not appear in general to commute in the category of topological spaces. I don't know an explicit counterexample though.

- [Homeomorph.restrictedProductPi](homeomorph-restrictedproductpi.md)

Let $n$ be a natural and let $M_n(X)$ for a set $X$ denote “$n\times n$ matrices with coefficient in $X$”, i.e. $X^{n^2}$. If $X$ is a topological spaces then give $M_n(X)$ the product topology.

- [Homeomorph.restrictedProductMatrix](homeomorph-restrictedproductmatrix.md)

## Units

We now want to move from matrices to invertible matrices whilst keeping track of topology, so we need to understand units of topological monoids. Openness of the subobject was crucial in the above arguments, so we need the next lemma before we can get anywhere.

- [Submonoid.units\_isOpen](submonoid-units-isopen.md)

**Remark.** Note that $M^\times$ doesn't get the subspace topology from $M$, it is embedded into $M\times M$ via $g\mapsto (g,g^{-1})$ and gets the subspace topology from the product. This makes it into a topological group.

Later on, compactness will be key for us, so we record the analogous result for compactness.

- [Submonoid.units\_isCompact](submonoid-units-iscompact.md)

**Remark.** Is Hausdorffness necessary?

- [ContinuousMulEquiv.piUnits](continuousmulequiv-piunits.md)
- [ContinuousMulEquiv.restrictedProductUnits](continuousmulequiv-restrictedproductunits.md)
