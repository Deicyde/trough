---
declaration: section
origin: cited
lean: MDifferentiable.eq_of_eqOn_of_isOpen, MathlibExt.Geometry.Manifold.ComplexRigidityWanted.holomorphic_identity_on_connected_complex_manifold, MDifferentiable.isOpenMap_of_finrank_eq_one, MathlibExt.Geometry.Manifold.ComplexRigidityWanted.holomorphic_open_mapping_one_dim
statement: formalized
proof: formalized
---

# Identity and open mapping theorems for holomorphic maps

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/identity-and-open-mapping-theorems-for-holomorph/index.html).

## Holomorphic maps on a connected manifold that agree on a nonempty open set are equal

Let $M$ be a connected complex manifold without boundary, modeled on a complex normed space with
complex $C^1$ (that is, holomorphic) transition maps, and let $F$ be a complex normed space. If
two holomorphic (everywhere complex differentiable) maps $f, g : M \to F$ agree on a nonempty
open subset $U \subseteq M$, then $f = g$.

Formalized by `MDifferentiable.eq_of_eqOn_of_isOpen`, a theorem declared in [MathlibExt/Geometry/Manifold/HolomorphicIdentity.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/HolomorphicIdentity.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/identity-and-open-mapping-theorems-for-holomorph/index.html#eq-of-eq-on-of-is-open).

## Identity theorem for holomorphic maps

Let $M$ be a connected complex manifold without
boundary, modeled on a complex normed space with complex $C^1$ (that is, holomorphic) transition
maps, and let $F$ be a complex normed space. If two holomorphic (everywhere complex
differentiable) maps $f, g : M \to F$ agree on a nonempty open subset $U \subseteq M$, then
$f = g$.

## Sources

- O. Forster, Lectures on Riemann Surfaces, identity theorem for holomorphic maps; Lean states connected-complex-manifold vector-valued form. It is `MDifferentiable.eq_of_eqOn_of_isOpen`, kept under the source's name.

Formalized by `MathlibExt.Geometry.Manifold.ComplexRigidityWanted.holomorphic_identity_on_connected_complex_manifold`, a theorem declared in [MathlibExt/Geometry/Manifold/HolomorphicIdentity.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/HolomorphicIdentity.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/identity-and-open-mapping-theorems-for-holomorph/index.html#holomorphic-identity-on-connected-comple).

## Open mapping theorem for one-dimensional complex manifolds

Let $M$ and $N$ be complex
manifolds without boundary modeled on complex normed spaces of dimension one, with complex $C^1$
(that is, holomorphic) transition maps, and suppose $M$ is connected. Then every holomorphic
(everywhere complex differentiable) map $f : M \to N$ that is not constant is an open map.

Formalized by `MDifferentiable.isOpenMap_of_finrank_eq_one`, a theorem declared in [MathlibExt/Geometry/Manifold/HolomorphicOpenMapping.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/HolomorphicOpenMapping.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/identity-and-open-mapping-theorems-for-holomorph/index.html#is-open-map-of-finrank-eq-one).

## Open mapping theorem for Riemann surfaces

Let $M$ and $N$ be complex manifolds without
boundary modeled on complex normed spaces of dimension one, with complex $C^1$ (that is,
holomorphic) transition maps, and suppose $M$ is connected. Then every holomorphic (everywhere
complex differentiable) map $f : M \to N$ that is not constant is an open map.

## Sources

- O. Forster, Lectures on Riemann Surfaces, open mapping theorem for Riemann surfaces; Lean states one-complex-dimensional specialization. It is `MDifferentiable.isOpenMap_of_finrank_eq_one`, kept under the source's name.

Formalized by `MathlibExt.Geometry.Manifold.ComplexRigidityWanted.holomorphic_open_mapping_one_dim`, a theorem declared in [MathlibExt/Geometry/Manifold/HolomorphicOpenMapping.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/HolomorphicOpenMapping.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/identity-and-open-mapping-theorems-for-holomorph/index.html#holomorphic-open-mapping-one-dim).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Identity and open mapping theorems for holomorphic maps](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/identity-and-open-mapping-theorems-for-holomorph/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/complex-and-symplectic-geometry/identity-and-open-mapping-theorems-for-holomorph)
