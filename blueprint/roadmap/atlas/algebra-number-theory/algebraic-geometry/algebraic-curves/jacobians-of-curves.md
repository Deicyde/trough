---
declaration: section
origin: cited
lean: MathlibExt.AlgebraicGeometry.JacobianChallengeWanted.AlgebraicGeometry.JacobianChallenge.genus, MathlibExt.AlgebraicGeometry.JacobianChallengeWanted.AlgebraicGeometry.JacobianChallenge.Jacobian, MathlibExt.AlgebraicGeometry.JacobianChallengeWanted.AlgebraicGeometry.JacobianChallenge.Jacobian.smoothOfRelativeDimension_genus, MathlibExt.AlgebraicGeometry.JacobianChallengeWanted.AlgebraicGeometry.JacobianChallenge.Jacobian.ofCurve, MathlibExt.AlgebraicGeometry.JacobianChallengeWanted.AlgebraicGeometry.JacobianChallenge.Jacobian.comp_ofCurve, MathlibExt.AlgebraicGeometry.JacobianChallengeWanted.AlgebraicGeometry.JacobianChallenge.Jacobian.exists_unique_ofCurve_comp, MathlibExt.AlgebraicGeometry.JacobianChallengeWanted.AlgebraicGeometry.JacobianChallenge.instCommGroup_eq, MathlibExt.AlgebraicGeometry.JacobianChallengeWanted.c
statement: formalized
---

# Jacobians of curves

10 results, 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-curves/index.html).

## Genus of a smooth proper curve

For a field $k$ and a curve $C$ over $k$, that is, a
$k$-scheme that is proper, smooth of relative dimension $1$ and geometrically irreducible, the
genus of $C$ is a natural number.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge/near/587802685. Problem `jacobian_challenge_alggeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.JacobianChallengeWanted.AlgebraicGeometry.JacobianChallenge.genus` is written with `def_wanted` in [WantedExt/AlgebraicGeometry/JacobianChallengeWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/JacobianChallengeWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-curves/index.html#genus).

## Jacobian of a smooth proper curve

For a field $k$ and a curve $C$ over $k$, that is, a
$k$-scheme that is proper, smooth of relative dimension $1$ and geometrically irreducible, the
Jacobian $J(C)$ of $C$ is a $k$-scheme.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge/near/587802685. Problem `jacobian_challenge_alggeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.JacobianChallengeWanted.AlgebraicGeometry.JacobianChallenge.Jacobian` is written with `def_wanted` in [WantedExt/AlgebraicGeometry/JacobianChallengeWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/JacobianChallengeWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-curves/index.html#jacobian).

## The Jacobian has dimension equal to the genus

Let $C$ be a proper, smooth, geometrically
irreducible curve over a field $k$. The Jacobian $J(C)$ is smooth of relative dimension $g$ over
$k$, where $g$ is the genus of $C$.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge/near/587802685. Problem `jacobian_challenge_alggeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.JacobianChallengeWanted.AlgebraicGeometry.JacobianChallenge.Jacobian.smoothOfRelativeDimension_genus` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/JacobianChallengeWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/JacobianChallengeWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-curves/index.html#smooth-of-relative-dimension-genus).

## Abel–Jacobi map

Let $C$ be a proper, smooth, geometrically irreducible curve over a field
$k$. Each $k$-rational point $P$ of $C$ gives a morphism of $k$-schemes $C \to J(C)$ from $C$ to
its Jacobian, the Abel–Jacobi map based at $P$.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge/near/587802685. Problem `jacobian_challenge_alggeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.JacobianChallengeWanted.AlgebraicGeometry.JacobianChallenge.Jacobian.ofCurve` is written with `def_wanted` in [WantedExt/AlgebraicGeometry/JacobianChallengeWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/JacobianChallengeWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-curves/index.html#of-curve).

## The Abel–Jacobi map sends the base point to zero

Let $C$ be a proper, smooth,
geometrically irreducible curve over a field $k$, let $J(C)$ be its Jacobian, and let $P$ be a
$k$-rational point of $C$. The Abel–Jacobi map $C \to J(C)$ based at $P$ sends $P$ to the
identity point of $J(C)$ for its group scheme structure.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge/near/587802685. Problem `jacobian_challenge_alggeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.JacobianChallengeWanted.AlgebraicGeometry.JacobianChallenge.Jacobian.comp_ofCurve` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/JacobianChallengeWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/JacobianChallengeWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-curves/index.html#comp-of-curve).

## Universal property of the Jacobian

Let $C$ be a proper, smooth, geometrically irreducible
curve over a field $k$, let $J(C)$ be its Jacobian, let $P$ be a $k$-rational point of $C$, and
let $\iota_P : C \to J(C)$ be the Abel–Jacobi map based at $P$. Let $A$ be a group scheme over $k$
that is smooth, proper and geometrically irreducible. For every morphism of $k$-schemes
$f : C \to A$ sending $P$ to the identity point of $A$, there is a unique morphism of $k$-schemes
$g : J(C) \to A$ with $f = g \circ \iota_P$.

In other words, the Jacobian of $C$ is the Albanese variety of $C$.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge/near/587802685. Problem `jacobian_challenge_alggeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.JacobianChallengeWanted.AlgebraicGeometry.JacobianChallenge.Jacobian.exists_unique_ofCurve_comp` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/JacobianChallengeWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/JacobianChallengeWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-curves/index.html#exists-unique-of-curve-comp).

## Group law on the rational points of the Jacobian

Let $C$ be a proper, smooth,
geometrically irreducible curve over a field $k$. The commutative group structure on the set of
$k$-rational points of the Jacobian $J(C)$ is the one induced by its commutative group scheme
structure: the product of two $k$-points $x$ and $y$ is $\mu \circ (x, y)$, where $\mu$ is the
multiplication morphism of $J(C)$.

This pins down the group law rather than allowing an arbitrary commutative group structure.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge/near/587802685. Problem `jacobian_challenge_alggeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.JacobianChallengeWanted.AlgebraicGeometry.JacobianChallenge.instCommGroup_eq` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/JacobianChallengeWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/JacobianChallengeWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-curves/index.html#inst-comm-group-eq).

## Uniform Mordell–Lang constant

For natural numbers $g$ and $d$, $c(g, d)$ is a natural
number: the constant in the uniform bound on rational points of curves in Theorem 1.1 of
Dimitrov, Gao and Habegger.

## Sources

- V. Dimitrov, Z. Gao, and P. Habegger, `Uniformity in Mordell–Lang for curves`, Annals of Math, 194 (1) 2021. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_uniform_mordell_lang` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.JacobianChallengeWanted.c` is written with `def_wanted` in [WantedExt/AlgebraicGeometry/JacobianChallengeWanted.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/JacobianChallengeWanted.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-curves/index.html#c).

## The uniform Mordell–Lang constant is at least one

For all natural numbers $g$ and
$d$, the uniform constant satisfies $c(g, d) \ge 1$.

Stated but not proved: `MathlibExt.AlgebraicGeometry.JacobianChallengeWanted.c_pos` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/JacobianChallengeWanted.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/JacobianChallengeWanted.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-curves/index.html#c-pos).

## Uniform Mordell–Lang for curves

Let $g \ge 2$ and $d \ge 1$ be natural numbers, let $F$
be a number field with $[F : \mathbb{Q}] \le d$, and let $C$ be a proper, smooth, geometrically
irreducible curve over $F$. If $C$ has genus $g$, then the number of $F$-rational points of $C$,
possibly infinite, is at most $c(g, d)^{1 + \rho}$, where $c$ is the uniform constant and $\rho$
is the free rank of the group of $F$-rational points of the Jacobian of $C$.

## Sources

- V. Dimitrov, Z. Gao, and P. Habegger, `Uniformity in Mordell–Lang for curves`, Annals of Math, 194 (1) 2021. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_uniform_mordell_lang` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.JacobianChallengeWanted.theorem_1_1` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/JacobianChallengeWanted.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/JacobianChallengeWanted.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-curves/index.html#theorem-1-1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Jacobians of curves](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-curves/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-curves)
