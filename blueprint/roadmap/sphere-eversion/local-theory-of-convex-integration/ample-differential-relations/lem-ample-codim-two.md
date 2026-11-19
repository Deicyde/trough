---
declaration: lemma
origin: cited
lean: AmpleSet.of_one_lt_codim
statement: formalized
proof: formalized
---

# ample_codim_two

The complement of a linear subspace of codimension at least 2 is ample.

## Depends on

- [ample_subset](def-ample-subset.md)

## Proof

Let $F$ be subspace of $E$ with codimension at least $2$. Let $F'$ be a complement subspace. Its dimension is at least $2$ since it is isomorphic to $E/F$ and $\dim(E/F) = \operatorname{codim}(F) ≥ 2$. First note the complement of $F$ is path-connected. Indeed let $x$ and $y$ be points outside $F$. Decomposing on $F ⊕ F'$, we get $x = u + u'$ and $y = v + v'$ with $u' ≠ 0$ and $v' ≠ 0$. The segments from $x$ to $u'$ and $y$ to $v'$ stay outside $F$, so it suffices to connect $u'$ and $v'$ in $F' ∖ \{0\}$. If the segment from $u'$ to $v'$ doesn't contains the origin then we are done. Otherwise $v' = μu'$ for some (negative) $u'$. Since $\dim(F') ≥ 2$ and $u' ≠ 0$, there exists $f ∈ F'$ which is linearly independent from $u'$, hence from $v'$. We can then connect both $u'$ and $v'$ to $f$ by a segment away from zero.

We now turn to ampleness. The connectedness result reduces to prove that every $e$ in $E$ is in the convex hull of $E ∖ F$. If $e$ is not in $F$ then it is the convex combination of itself with coefficient $1$ and we are done. Now assume $e$ is in $F$. The codimension assumption guarantees the existence of a subspace $G$ such that $\dim(G) = 2$ and $G ∩ F = \{0\}$. Let $(g_1, g_2)$ be a basis of $G$. We set $p_1 = e + g_1$, $p_2 = e + g_2$, $p_3 = e - g_1 - g_2$. All these points are in $E ∖ F$ and $e = p_1/3 + p_2/3 + p_3/3$.

## Lean

Formalized as [`AmpleSet.of_one_lt_codim`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/AmpleSet.of_one_lt_codim).

## Sources

- [Sphere eversion blueprint: local_convex_integration.tex, line 327](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/local_convex_integration.tex#L327)
