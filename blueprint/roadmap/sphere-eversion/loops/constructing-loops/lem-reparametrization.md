---
declaration: lemma
origin: cited
lean: SmoothSurroundingFamily.reparametrize_average
statement: formalized
proof: formalized
---

# reparametrization

Let $γ \!: E × 𝕊^1 → F$ be a smooth family of loops surrounding a map $g$. There is a smooth family $φ \!: E × 𝕊^1 → 𝕊^1$ such that each $γ_x ∘ φ_x$ has average $g(x)$ and $φ_x(0) = 0$.

## Depends on

- [surrounds](def-surrounds.md)

## Proof depends on

- [smooth_barycentric_coord](../surrounding-points/lem-smooth-barycentric-coord.md)
- [exists_cont_diff_of_convex₂](lem-exists-cont-diff-of-convex2.md)

## Proof

Gromov's main idea in order to prove this result is to translate the problem of constructing a family of circle maps $φ$ into the problem of constructing a family of smooth density functions $f$ on the circle. We introduce some vocabulary in order to describe this reduction. Let $f \!: E × ℝ → ℝ$ be a smooth positive function that is $1$-periodic in its second argument. We say that $f$ is a centering density for $(γ, g)$ at $x$ if $f_x \!: ℝ → ℝ$ has average value one when seen as a function on $𝕊¹$ and the average value of $f_x γ_x$ is $g(x)$. We claim that, in order to prove the lemma, it is sufficient to build such an $f$ which is centering at every $x$. Indeed, assume we have such an $f$. We then get a smooth family of $ℤ$-equivariant functions $ψ \!: E × ℝ → ℝ$ defined by $ψ_x(t) = \int_0^tf_x(s)ds$. Because $ψ$ is smooth and each $ψ_x$ is strictly monotone and $ℤ$-equivariant, one can check there is a smooth map $φ : E × ℝ → ℝ$ which is $ℤ$-equivariant and such that $φ_x ∘ ψ_x = \operatorname{Id}$ for each $x$. Seen as a family of functions from $𝕊¹$ to $𝕊¹$, those functions are suitable since, for every $x$, the change of variable formula gives:

$$
\int_{𝕊¹} γ_x ∘ φ_x(s)ds = \int_{𝕊¹} ψ_x'(s) γ_x ∘ φ_x(ψ_x(s))ds
= \int_{𝕊¹} f_x(s) γ_x(s)ds = g(x).
$$

We now prove the existence of a function which is a centering density at every point of $x$. For any given $x$, this constraint is clearly convex. Hence [Lemma exists_cont_diff_of_convex₂](lem-exists-cont-diff-of-convex2.md) ensures it is enough to prove existence of functions that are centering densities in a neighborhood of any given point $x$. So we fix some $x$ in $E$.

Since $γ_x$ strictly surrounds $g(x)$, there are points $s_1, …, s_{n+1}$ in $𝕊^1$ such that $g(x)$ is surrounded by the corresponding points $γ_x(s_j)$.

Let $f_1, …, f_{n+1}$ be smooth positive periodic maps from $ℝ$ to $ℝ$ which average value $1$ on a period and such that the corresponding measures on $𝕊¹$ are very close to the Dirac measures on $s_j$, ie. for any function $h$, the average value of $f_jh$ is almost $h(s_j)$. We set $p_j = \int f_jγ_x\, ds$, which is almost $γ_x(s_j)$ so that $g(x) = \sum w_j p_j$ for some weights $w_j$ in the open interval $(0, 1)$ according to [Lemma smooth_barycentric_coord](../surrounding-points/lem-smooth-barycentric-coord.md).

If $x'$ is in a sufficiently small neighborhood of $x$, [Lemma smooth_barycentric_coord](../surrounding-points/lem-smooth-barycentric-coord.md) gives smooth weight functions $w_j$ such that $g(x') = \sum w_j(x')p_j(x')$. Hence we can set $f_{x'}(s) = \sum w_j(x')f_j(s)$.

## Lean

Formalized as [`SmoothSurroundingFamily.reparametrize_average`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/SmoothSurroundingFamily.reparametrize_average).

## Sources

- [Sphere eversion blueprint: loops.tex, line 624](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/loops.tex#L624)
