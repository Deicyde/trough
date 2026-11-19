# Preliminaries

## Localisation data

In order to conveniently globalize the theory of the previous chapter, we'll need a number of constructions and lemmas. By definition, manifolds are covered by open sets that are diffeomorphic to open sets of vector spaces. But for us it is slightly more convenient to work with smooth open embeddings of whole vector spaces. Here a smooth open embedding from a manifold $X$ to a manifold $Y$ is a smooth map $φ : X → Y$ which is open and for which there is some smooth $ψ : φ(X) → X$ such that $ψ ∘ φ = \operatorname{Id}_X$ (hence also and $φ ∘ ψ = \operatorname{Id}_{φ(X)}$). Remember that a family of sets $V_i$ in a topological space $X$ is locally finite if every point of $X$ has a neighborhood that intersects only finitely many $V_i$. Note that in this whole text, every manifold is paracompact by definition. In particular their topology are metrizable and we will arbitrarily fix a compatible distance function on every manifold.

- [update](def-update.md)
- [smooth_updating](lem-smooth-updating.md)
- [dist_updating](lem-dist-updating.md)

In order to handle in a uniform way compact and non-compact manifolds, we will index sequences by the family of sets $\mathcal{I}_{N}$ defined for each natural number $N$ by:

$$
\mathcal{I}_{N} =
\begin{cases}
ℕ \text{ if $N = 0$}\\
\{0, \dots, N - 1\} \text{otherwise}
\end{cases}
$$

- [nice_atlas](lem-nice-atlas.md)
- [localisation_data](def-localisation-data.md)
- [ex_localisation](lem-ex-localisation.md)

The general idea will be to apply the results of the previous chapters to all the $ψ_{j(i)}⁻¹ ∘ f ∘ φ_i : E → F$ for some maps $f$. However we must be careful that doing this for some $i$ does not ruin the setup for the next $i$. This is easier to control using a distance function on the target manifold as in [Lemma localisation_stability](lem-localisation-stability.md) below. First we need a general lemma about a single metric space (actually the formalized statement is stronger, it assumes only closed sets instead of compact ones, but here we explain the easier proof which is sufficient for our purposes).

- [stability_cover](lem-stability-cover.md)
- [localisation_stability](lem-localisation-stability.md)

Note that, in the preceding lemma, the conclusion $g(φ_i(E)) ⊂ ψ_{j(i)}(F)$ is weaker than the condition $f(φ_i(E)) ⊂ ψ_{j(i)}(B_F)$ that appears in the definition of localisation data.

The condition $∀ m,\; d(g(m), f(m)) < ε(m)$ will be abbreviated $d(g, f) < ε$.

*The proof of [Lemma localisation_stability](lem-localisation-stability.md) is shown with its statement.*

## Jets spaces

We now need to introduce the bundles that will replace the jet spaces $E × F × \operatorname{Hom}(E, F)$ from the previous chapter. We need a couple of fiber bundles constructions.

- [pull_back_bundle](def-pull-back-bundle.md)
- [hom_bundle](def-hom-bundle.md)

Set-theoretically, one can define $\operatorname{Hom}(E, F)$ as the set of subsets $S$ of $E × F$ such that there exists $b$ such that $S ⊂ E_b × F_b$ and $S$ is the graph of a linear map. But the type theory formalization will use other tricks here. The facts that really matter are listed in [Lemma one_jet_section](lem-one-jet-section.md) below.

- [one_jet_space](def-one-jet-space.md)

We will use notations like $(m, n, φ)$ to denote an element of $J^1(M, N)$, but one should keep in mind that $J^1(M, N)$ is not a product, since $φ$ lives in $\operatorname{Hom}(T_mM, T_nN)$ which depends on $m$ and $n$.

- [one_jet_extension](def-one-jet-extension.md)

The composition of a section $\mathcal{F} \!: M → J^1(M, N)$ with the projection onto $N$ will sometimes be denoted by $\operatorname{bs} \mathcal{F} \!: M → N$ and called the base map of $\mathcal{F}$. For any $m$, $\mathcal{F}(m)_φ$ will denote the component of $\mathcal{F}(m)$ living in $\operatorname{Hom}(T_mM, T_{\operatorname{bs}\mathcal{F}(m)}N)$.

- [one_jet_section](lem-one-jet-section.md)
- [holonomic_section](def-holonomic-section.md)
