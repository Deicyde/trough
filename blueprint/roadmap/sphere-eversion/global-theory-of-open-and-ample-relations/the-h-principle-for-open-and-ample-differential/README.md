# The $h$-principle for open and ample differential relations

In this chapter, $X$ and $Y$ are smooth manifolds and $\mathcal{R}$ is a first order differential relation on maps from $X$ to $Y$: $\mathcal{R} ⊂ J^1(X, Y)$. For any $σ = (x, y, φ)$ in $\mathcal{R}$ and any dual pair $(λ, v) ∈ T^*_xX × T_xX$, we set:

$$
\mathcal{R}_{σ, λ, v} =
\operatorname{Conn}_{φ(v)}\left\{w ∈ T_yY \;;\;
\big(x,\; y,\; φ + (w - φ(v))⊗λ\big) ∈ \mathcal{R}\right\}
$$

where $\operatorname{Conn}_a A$ is the connected component of $A$ containing $a$. In order to decipher this definition, it suffices to notice that $φ + (w - φ(v))⊗λ$ is the unique linear map from $T_xX$ to $T_yY$ which coincides with $φ$ on $\ker λ$ and sends $v$ to $w$. In particular, $w = φ(v)$ gives back $φ$.

Of course we will want to deal with more than one point, so we will consider a vector field $V$ and a $1$–form $λ$ such that $λ(V) = 1$ on some subset $U$ of $X$, a formal solution $F$ (defined at least on $U$), and get the corresponding $\mathcal{R}_{F, λ, v}$ over $U$.

One easily checks that $\mathcal{R}_{σ, κ^{-1}λ, κv} = κ\mathcal{R}_{σ, λ, v}$ hence the above definition only depends on $\ker λ$ and the direction $ℝV$.

- [ample_relation](def-ample-relation.md)
- [ample_iff_loc](lem-ample-iff-loc.md)
- [open_ample_immersion](lem-open-ample-immersion.md)
- [Gromov](thm-open-ample.md)

We first explain how to get rid of parameters, using the relation $\mathcal{R}^P$ for families of solutions parametrized by $P$.

- [ample_parameter](lem-ample-parameter.md)

*Proof of Theorem Gromov: shown with [Gromov](thm-open-ample.md).*

- [Smale 1958](thm-sphere-eversion.md)
