---
declaration: section
origin: cited
lean: RestrictedProduct.XS, RestrictedProduct.XS_mono, RestrictedProduct.mem_XS_of_restricted, RestrictedProduct.supportFinset, RestrictedProduct.mem_XS_support, RestrictedProduct.XS_mem_restricted, RestrictedProduct.supportFinset_le, RestrictedProduct.inclusionMap
statement: formalized
proof: formalized
---

# Restricted products of topological spaces

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html).

## Pieces of a restricted product

## Piece of a restricted product supported in a finite set

Let $(X_i)_{i \in \iota}$ be a
family of types with subsets $U_i \subseteq X_i$. For a finite set $S$ of indices, the piece
$X_S$ is the set of tuples $x \in \prod_{i \in \iota} X_i$ such that $x_i \in U_i$ for every
$i \notin S$.

Formalized by `RestrictedProduct.XS`, a definition declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#xs).

## The pieces grow with the finite set

Let $(X_i)_{i \in \iota}$ be a family of types with
subsets $U_i \subseteq X_i$, and for a finite set $S$ of indices let $X_S$ be the set of tuples
$x \in \prod_{i \in \iota} X_i$ with $x_i \in U_i$ for every $i \notin S$. If $S \subseteq T$ are
finite sets of indices, then $X_S \subseteq X_T$.

Formalized by `RestrictedProduct.XS_mono`, a theorem declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#xs-mono).

## Every element of the restricted product lies in a piece

Let $(X_i)_{i \in \iota}$ be
sets with subsets $U_i \subseteq X_i$, and let $x$ be an element of the restricted product of
the $X_i$ with respect to the $U_i$, that is, a tuple $x \in \prod_i X_i$ with $x_i \in U_i$ for
all but finitely many $i$. Then there is a finite set $S \subseteq \iota$ such that
$x_i \in U_i$ for all $i \notin S$, that is, $x$ lies in the piece $X_S$.

Formalized by `RestrictedProduct.mem_XS_of_restricted`, a theorem declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#mem-xs-of-restricted).

## Support of an element of a restricted product

Let $(X_i)_{i \in \iota}$ be sets with
subsets $U_i \subseteq X_i$. The support of an element $x$ of the restricted product of the $X_i$
with respect to the $U_i$ (a tuple with $x_i \in U_i$ for all but finitely many $i$) is the
finite set of indices $i$ with $x_i \notin U_i$.

Formalized by `RestrictedProduct.supportFinset`, a definition declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#support-finset).

## An element lies in the piece indexed by its support

Let $(X_i)_{i \in \iota}$ be sets
with subsets $U_i \subseteq X_i$, let $x$ be an element of the restricted product of the $X_i$
with respect to the $U_i$ (a tuple with $x_i \in U_i$ for all but finitely many $i$), and let
$\operatorname{supp}(x)$ be the finite set of indices $i$ with $x_i \notin U_i$. Then
$x_i \in U_i$ for every $i \notin \operatorname{supp}(x)$, that is, $x$ lies in the piece
$X_{\operatorname{supp}(x)}$.

Formalized by `RestrictedProduct.mem_XS_support`, a theorem declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#mem-xs-support).

## Tuples in a piece are eventually in the $U_i$

Let $(X_i)_{i \in \iota}$ be a family of
types with subsets $U_i \subseteq X_i$, and let $S$ be a finite set of indices. If a tuple
$x \in \prod_{i \in \iota} X_i$ lies in the piece $X_S$, that is, $x_i \in U_i$ for every
$i \notin S$, then $x_i \in U_i$ for all but finitely many indices $i$.

In other words, $x$ defines an element of the restricted product of the $X_i$ with respect to
the $U_i$.

Formalized by `RestrictedProduct.XS_mem_restricted`, a theorem declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#xs-mem-restricted).

## The support lies in the index set of every piece containing the element

Let
$(X_i)_{i \in \iota}$ be sets with subsets $U_i \subseteq X_i$, and let $x$ be an element of the
restricted product of the $X_i$ with respect to the $U_i$ (a tuple with $x_i \in U_i$ for all but
finitely many $i$), with support $\operatorname{supp}(x) = \{i : x_i \notin U_i\}$. If
$T \subseteq \iota$ is a finite set with $x_i \in U_i$ for all $i \notin T$, then
$\operatorname{supp}(x) \subseteq T$.

Formalized by `RestrictedProduct.supportFinset_le`, a theorem declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#support-finset-le).

## Inclusion of pieces

Let $(X_i)_{i \in \iota}$ be topological spaces with subsets
$U_i \subseteq X_i$, and for a finite set $S \subseteq \iota$ let $X_S$ be the set of tuples
$x \in \prod_i X_i$ with $x_i \in U_i$ for all $i \notin S$. For finite sets $S \subseteq T$, the
inclusion of pieces is the map $X_S \to X_T$ sending each tuple $x$ to itself.

Formalized by `RestrictedProduct.inclusionMap`, a definition declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#inclusion-map).

## Continuity of the inclusion of pieces

Let $(X_i)_{i \in \iota}$ be topological spaces with
subsets $U_i \subseteq X_i$, and for a finite set $S \subseteq \iota$ let $X_S$ be the set of
tuples $x \in \prod_i X_i$ with $x_i \in U_i$ for all $i \notin S$, with the subspace topology of
the product topology. For finite sets $S \subseteq T \subseteq \iota$, the inclusion map
$X_S \to X_T$ is continuous.

Formalized by `RestrictedProduct.continuous_inclusionMap`, a theorem declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#continuous-inclusion-map).

## Transition maps of the pieces

Let $(X_i)_{i \in \iota}$ be topological spaces with
subsets $U_i \subseteq X_i$, and for a finite set $S \subseteq \iota$ let $X_S$ be the set of
tuples $x \in \prod_i X_i$ with $x_i \in U_i$ for all $i \notin S$. For finite sets
$S \subseteq T$, the transition map $X_S \to X_T$ of the direct system of pieces sends each tuple
$x$ to itself.

Formalized by `RestrictedProduct.transitionMaps`, a definition declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#transition-maps).

## Continuity of the transition maps of the pieces

Let $(X_i)_{i \in \iota}$ be topological
spaces with subsets $U_i \subseteq X_i$, and for a finite set $S \subseteq \iota$ let $X_S$ be the
set of tuples $x \in \prod_i X_i$ with $x_i \in U_i$ for all $i \notin S$, with the subspace
topology of the product topology. For all finite sets $S \subseteq T \subseteq \iota$, the
transition map $X_S \to X_T$ of the direct system of the pieces, which is the inclusion, is
continuous.

Formalized by `RestrictedProduct.continuous_transitionMaps`, a theorem declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#continuous-transition-maps).

## Direct limit of the finite-support pieces

Let $(X_i)_{i \in \iota}$ be topological spaces
with subsets $U_i \subseteq X_i$, and for a finite set $S \subseteq \iota$ let $X_S$ be the set of
tuples $x \in \prod_i X_i$ with $x_i \in U_i$ for all $i \notin S$, with the subspace topology of
the product topology. The space $\varinjlim_S X_S$ is the direct limit of the $X_S$ over the
finite subsets $S$ of $\iota$ ordered by inclusion, with the inclusions $X_S \to X_T$ for
$S \subseteq T$ as transition maps: the quotient of the disjoint union of the $X_S$ by the
equivalence relation generated by identifying each $x \in X_S$ with its image in $X_T$, with the
quotient topology.

Formalized by `RestrictedProduct.DirectLimitXS`, an abbreviation declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#direct-limit-xs).

## The cofinite filter lies below the principal filter of the complement of a finite set

For every finite set $S$ of indices in $\iota$, the cofinite filter on $\iota$ is less than or
equal to the principal filter of the complement $\iota \setminus S$; that is, $\iota \setminus S$
belongs to the cofinite filter.

Formalized by `RestrictedProduct.cofinite_le_principal_compl`, a theorem declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#cofinite-le-principal-compl).

## Tuples restricted on a cofinite set lie in a piece

Let $(X_i)_{i \in \iota}$ be sets
with subsets $U_i \subseteq X_i$, and for a finite set $F \subseteq \iota$ let $X_F$ be the set
of tuples $x \in \prod_i X_i$ with $x_i \in U_i$ for all $i \notin F$. Let $S \subseteq \iota$
have finite complement. Then every tuple $y \in \prod_i X_i$ with $y_i \in U_i$ for all
$i \in S$ lies in $X_{\iota \setminus S}$.

Formalized by `RestrictedProduct.inclusion_mem_XS_of_principal`, a theorem declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#inclusion-mem-xs-of-principal).

## Forward map to the direct limit of the pieces

Let $(X_i)_{i \in \iota}$ be topological
spaces with subsets $U_i \subseteq X_i$, and let $L$ be the direct limit, over finite sets
$S \subseteq \iota$, of the pieces $X_S$ of tuples with $x_i \in U_i$ for all $i \notin S$. The
forward map sends an element $x$ of the restricted product of the $X_i$ with respect to the
$U_i$ (a tuple with $x_i \in U_i$ for all but finitely many $i$) to the class in $L$ of $x$,
viewed in the piece $X_{\operatorname{supp}(x)}$ indexed by its support
$\operatorname{supp}(x) = \{i : x_i \notin U_i\}$.

Formalized by `RestrictedProduct.toDirectLimit`, a definition declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#to-direct-limit).

## The map from the direct limit of the pieces to the restricted product

Let
$(X_i)_{i \in \iota}$ be topological spaces with subsets $U_i \subseteq X_i$, and for a finite set
$S \subseteq \iota$ let $X_S$ be the set of tuples $x \in \prod_i X_i$ with $x_i \in U_i$ for all
$i \notin S$, with the subspace topology of the product topology. The backward map sends the class
in the direct limit $\varinjlim_S X_S$ (over the finite subsets of $\iota$) of a tuple
$x \in X_S$ to $x$, regarded as an element of the restricted product $\prod'_i (X_i, U_i)$ with
respect to the cofinite filter; the result does not depend on the representative.

Formalized by `RestrictedProduct.fromDirectLimit`, a definition declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#from-direct-limit).

## The backward map undoes the forward map

Let $(X_i)_{i \in \iota}$ be topological spaces
with subsets $U_i \subseteq X_i$, and for a finite set $S \subseteq \iota$ let $X_S$ be the set of
tuples $x \in \prod_i X_i$ with $x_i \in U_i$ for all $i \notin S$. For every $x$ in the
restricted product $\prod'_i (X_i, U_i)$ with respect to the cofinite filter, let $S(x)$ be the
finite set of indices $i$ with $x_i \notin U_i$. Sending $x$ to its class in $X_{S(x)}$ in the
direct limit $\varinjlim_S X_S$, and then sending that class to the tuple carried by its
representative, returns $x$.

This holds definitionally: unfolding both maps, the quotient lift applied to the canonical
representative returns the representative itself.

Formalized by `RestrictedProduct.fromDirectLimit_toDirectLimit`, a theorem declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#from-direct-limit-to-direct-limit).

## The forward map undoes the backward map

Let $(X_i)_{i \in \iota}$ be topological spaces
with subsets $U_i \subseteq X_i$, let $P$ be their restricted product (the tuples with
$x_i \in U_i$ for all but finitely many $i$), and let $L$ be the direct limit, over finite sets
$S \subseteq \iota$, of the pieces $X_S$ of tuples with $x_i \in U_i$ for all $i \notin S$. Let
$f : P \to L$ be the forward map, sending $x$ to its class in the piece indexed by its support
$\{i : x_i \notin U_i\}$, and let $g : L \to P$ be the backward map, sending a class to the tuple
carried by any of its representatives. Then $f(g(q)) = q$ for every $q \in L$.

Formalized by `RestrictedProduct.toDirectLimit_fromDirectLimit`, a theorem declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#to-direct-limit-from-direct-limit).

## Chunk map of a piece

Let $(X_i)_{i \in \iota}$ be topological spaces with subsets
$U_i \subseteq X_i$, let $S \subseteq \iota$ be finite, and let $X_S$ be the set of tuples
$x \in \prod_i X_i$ with $x_i \in U_i$ for all $i \notin S$. The chunk map sends each $x \in X_S$
to the same tuple $x$, viewed as an element of the restricted product of the $X_i$ with respect
to the $U_i$ and the principal filter of $\iota \setminus S$; this restricted product consists
of the tuples whose $i$-th entry lies in $U_i$ for every $i \notin S$.

Formalized by `RestrictedProduct.toChunk`, a definition declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#to-chunk).

## Continuity of the chunk map

Let $(X_i)_{i \in \iota}$ be topological spaces with subsets
$U_i \subseteq X_i$, let $S \subseteq \iota$ be finite, and let $X_S$ be the set of tuples
$x \in \prod_i X_i$ with $x_i \in U_i$ for all $i \notin S$, with the subspace topology of the
product topology. The map that sends $x \in X_S$ to $x$, viewed in the restricted product of the
$(X_i, U_i)$ with respect to the principal filter of $\iota \setminus S$ with its restricted
product topology, is continuous.

Formalized by `RestrictedProduct.continuous_toChunk`, a theorem declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#continuous-to-chunk).

## Continuity of the map from the direct limit of the pieces

Let $(X_i)_{i \in \iota}$ be
topological spaces with subsets $U_i \subseteq X_i$, and for a finite set $S \subseteq \iota$ let
$X_S$ be the set of tuples $x \in \prod_i X_i$ with $x_i \in U_i$ for all $i \notin S$, with the
subspace topology of the product topology. The map from the direct limit $\varinjlim_S X_S$ over
the finite subsets of $\iota$ to the restricted product $\prod'_i (X_i, U_i)$ (with respect to the
cofinite filter, with its restricted product topology) that sends the class of $x \in X_S$ to $x$
is continuous.

This follows from the universal property of the direct limit.

Formalized by `RestrictedProduct.continuous_fromDirectLimit`, a theorem declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#continuous-from-direct-limit).

## Continuity of the map to the direct limit of the pieces

Let $(X_i)_{i \in \iota}$ be
topological spaces with subsets $U_i \subseteq X_i$, and for a finite set $S \subseteq \iota$ let
$X_S$ be the set of tuples $x \in \prod_i X_i$ with $x_i \in U_i$ for all $i \notin S$, with the
subspace topology of the product topology. The map from the restricted product
$\prod'_i (X_i, U_i)$ (with respect to the cofinite filter, with its restricted product topology)
to the direct limit $\varinjlim_S X_S$ over the finite subsets of $\iota$ that sends $x$ to its
class in $X_{S(x)}$, where $S(x)$ is the finite set of indices $i$ with $x_i \notin U_i$, is
continuous.

This follows from the universal property of the restricted product topology.

Formalized by `RestrictedProduct.continuous_toDirectLimit`, a theorem declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#continuous-to-direct-limit).

## The restricted product is the direct limit of its finite-support pieces

Let
$(X_i)_{i \in \iota}$ be topological spaces with subsets $U_i \subseteq X_i$, and for a finite set
$S \subseteq \iota$ let $X_S$ be the set of tuples $x \in \prod_i X_i$ with $x_i \in U_i$ for all
$i \notin S$, with the subspace topology of the product topology. Let $\prod'_i (X_i, U_i)$ be
the restricted product with respect to the cofinite filter, with its restricted product
topology, and for $x$ in it let $S(x)$ be the finite set of indices $i$ with $x_i \notin U_i$.
The map sending $x$ to its class in $X_{S(x)}$ is a homeomorphism from $\prod'_i (X_i, U_i)$ to
the direct limit $\varinjlim_S X_S$ over the finite subsets of $\iota$ ordered by inclusion; its
inverse sends the class of $x \in X_S$ to $x$.

## Sources

- ATLAS NumberTheoryI, Proposition 25.5.

Formalized by `RestrictedProduct.homeomorph_directLimit`, a definition declared in [MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/RestrictedProduct/DirectLimit.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html#homeomorph-direct-limit).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Restricted products of topological spaces](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/restricted-products-of-topological-spaces/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Topology/general-topology/restricted-products-of-topological-spaces)
