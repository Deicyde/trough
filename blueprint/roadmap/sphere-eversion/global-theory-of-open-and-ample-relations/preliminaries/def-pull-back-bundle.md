---
declaration: definition
origin: cited
lean: Bundle.Pullback
statement: formalized
---

# pull_back_bundle

For every bundle $p : E → B$ and every map $f \!: B' → B$, the pull-back bundle $f^*E → B'$ is defined by $f^*E = \{(b', e) ∈ B' × E \;|\; p(e) = f(b')\}$ with the obvious projection to $B'$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Bundle.Pullback`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/Bundle.Pullback).

## Sources

- [Sphere eversion blueprint: global_convex_integration.tex, line 273](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/global_convex_integration.tex#L273)
