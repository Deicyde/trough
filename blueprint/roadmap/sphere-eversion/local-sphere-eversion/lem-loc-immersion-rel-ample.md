---
declaration: lemma
origin: cited
lean: loc_immersion_rel_ample
statement: formalized
proof: formalized
---

# loc_immersion_rel_ample

The relation $\mathcal{R}$ above is ample.

## Depends on

- [ample_codim_two](../local-theory-of-convex-integration/ample-differential-relations/lem-ample-codim-two.md)

## Proof

The core fact here is that if one fixes vector spaces $F$ and $F'$, a dual pair $(\pi, v)$ on $F$ and an injective linear map $\varphi \!: F \to F'$ then the updated map $\Upsilon_{p}\left(\varphi, w\right)$ is injective if and only if $w$ is not in $\varphi(\ker\pi)$. First we assume $\Upsilon_{p}\left(\varphi, \varphi(u)\right)$ is injective for some $u$ in $\varphi(\ker\pi)$ and derive a contradiction. We have $\Upsilon_{p}\left(\varphi, \varphi(u)\right)v = \varphi(u)$ by the general definition of updating and also $\Upsilon_{p}\left(\varphi, \varphi(u)\right)u = \varphi(u)$ since $u$ is in $\ker \pi$. Hence injectivity of $\varphi$ ensure $u = v$, which is absurd since $\pi(u) = 0$ and $\pi(v) = 1$. Conversely assume $w$ is not in $\varphi(\ker\pi)$ and let us prove $\Upsilon_{p}\left(\varphi, w\right)$ is injective. Assume $x$ is in the kernel of $\Upsilon_{p}\left(\varphi, w\right)$. Decompose $x = u + tv$ with $u \in \ker\pi$ and $t$ a real number. We have $\Upsilon_{p}\left(\varphi, w\right)(x) = \varphi(u) + tw$. Hence our assumption on $x$ implies $t$ vanishes otherwise we would have $w = -t⁻¹\varphi(u)$ contradicting that $w$ isn't in $\varphi(\ker\pi)$. This vanishing and the assumption on $x$ then imply $\varphi(u) = 0$. Since $\varphi$ is injective we conclude that $u = 0$ and finally $x = 0$.

We now turn to $\mathcal{R}$. It suffices to prove that for every $\sigma = (x, y, \varphi) \in \mathcal{R}$ and every dual pair $p = (\pi, v)$ on $E$, the slice $\mathcal{R}(\sigma, p)$ is ample. If $x$ is in $B$ then $\mathcal{R}(\sigma, p)$ is the whole $E$ which is obviously ample. So we assume $x$ is not in $B$. Since $\sigma$ is in $\mathcal{R}$, $\varphi$ is injective on $x^\perp$. The slice is the set of $w$ such that $\Upsilon_{p}\left(\varphi, w\right)$ is injective on $x^\perp$. Assume first $\ker\pi = x^\perp$. Then $\Upsilon_{p}\left(\varphi, w\right)$ coincides with $\varphi$ on $x^\perp$ hence the slice is the whole $E$. Assume now that $\ker\pi \neq x^\perp$. The slice is not very easy to picture in this case. But one should remember that, up to affine isomorphism, the slice depends only on $\ker \pi$. More specifically, if we keep $\pi$ but change $v$ then the slice is simply translated in $E$. Here we replace $v$ by the projection on $x^\perp$ of the vector dual to $\pi$ rescaled to keep the property $\pi(v) = 1$. What has been gained is that we now have $v \in x^\perp$ and $x^\perp = (x^\perp \cap \ker \pi) \oplus ℝ v$. Since $\varphi$ is injective on $x^\perp$, $\varphi(x^\perp \cap \ker \pi)$ is a hyperplane in $x^\perp$ and $\Upsilon_{p}\left(\varphi, w\right)$ is injective on $x^\perp$ if and only if $w$ is in the complement of $\varphi(x^\perp \cap \ker \pi)$ according to the core fact above. Since it is an hyperplane in $x^\perp$, it has codimension at least $2$ in $E$ hence its complement is ample.

## Lean

Formalized as [`loc_immersion_rel_ample`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/loc_immersion_rel_ample).

## Sources

- [Sphere eversion blueprint: appendix.tex, line 50](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/appendix.tex#L50)
