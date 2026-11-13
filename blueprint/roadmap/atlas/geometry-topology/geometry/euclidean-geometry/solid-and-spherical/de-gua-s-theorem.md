---
declaration: section
origin: cited
lean: MetaMathlibExt.deGua, MetaMathlibExt.deGua_theorem
statement: formalized
proof: formalized
---

# De Gua's theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/solid-and-spherical/de-gua-s-theorem/index.html).

## De Gua's theorem

Let $u, v, w \in \mathbb{R}^3$ be pairwise orthogonal vectors, so that
the tetrahedron with vertices $0, u, v, w$ has a right angle between any two of the edges at $0$.
Write $|x|$ for the Euclidean norm and $\langle x, y \rangle$ for the inner product. Let
$A_{uv}, A_{uw}, A_{vw}, A$ be real numbers with $A_{uv} = |u||v|/2$, $A_{uw} = |u||w|/2$,
$A_{vw} = |v||w|/2$ (the areas of the three right-angled faces) and
$(2A)^2 = |u - v|^2 |u - w|^2 - \langle u - v, u - w \rangle^2$, so that $A$ is, up to sign, the
area of the face with vertices $u, v, w$. Then $A^2 = A_{uv}^2 + A_{uw}^2 + A_{vw}^2$.

## Sources

- https://en.wikipedia.org/wiki/De_Gua%27s_theorem

Formalized by `MetaMathlibExt.deGua`, a theorem declared in [MathlibExt/Geometry/Euclidean/DeGua.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/DeGua.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/solid-and-spherical/de-gua-s-theorem/index.html#de-gua).

## De Gua's theorem with Heron's formula

Let $a, b, c > 0$ and let $p_0 = (a, 0, 0)$,
$p_1 = (0, b, 0)$, $p_2 = (0, 0, c)$ in $\mathbb{R}^3$, so that the tetrahedron with vertices
$0, p_0, p_1, p_2$ has a right angle between any two of the edges at $0$, with legs of lengths
$a$, $b$, $c$. Let $d_{01} = d(p_0, p_1)$, $d_{12} = d(p_1, p_2)$ and $d_{20} = d(p_2, p_0)$ be the
Euclidean distances, let $s = (d_{01} + d_{12} + d_{20})/2$, and let
$A = \sqrt{s(s - d_{01})(s - d_{12})(s - d_{20})}$, the area of the face $p_0 p_1 p_2$ by Heron's
formula. Then $A^2 = (ab/2)^2 + (bc/2)^2 + (ca/2)^2$.

## Sources

- https://en.wikipedia.org/wiki/De_Gua%27s_theorem

Formalized by `MetaMathlibExt.deGua_theorem`, a theorem declared in [MathlibExt/Geometry/Euclidean/DeGuaHeron.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/DeGuaHeron.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/solid-and-spherical/de-gua-s-theorem/index.html#de-gua-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: De Gua's theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/solid-and-spherical/de-gua-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/euclidean-geometry/solid-and-spherical/de-gua-s-theorem)
