---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsVariety, AlgebraicGeometry.IsVariety.isVariety_iff, AlgebraicGeometry.IsVariety.quasiSeparated
statement: formalized
proof: formalized
---

# Varieties over a field

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/varieties-over-a-field/index.html).

## Algebraic Geometry

## Geometrically reduced variety over a field

Let $k$ be a field. A scheme $X$ with a
chosen structure morphism $X \to \operatorname{Spec} k$ is a *variety* over $k$ if this morphism
is separated, of finite type (quasi-compact and locally of finite type), and geometrically
reduced.

Formalized by `AlgebraicGeometry.IsVariety`, a class declared in [MathlibExt/AlgebraicGeometry/Variety.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/Variety.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/varieties-over-a-field/index.html#is-variety).

## Characterization of varieties

Let $k$ be a field and let $X$ be a scheme with a
structure morphism $X \to \operatorname{Spec} k$. Then $X$ is a variety over $k$ if and only if
this structure morphism is separated, locally of finite type, quasi-compact and geometrically
reduced.

Formalized by `AlgebraicGeometry.IsVariety.isVariety_iff`, a theorem declared in [MathlibExt/AlgebraicGeometry/Variety.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/Variety.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/varieties-over-a-field/index.html#is-variety-iff).

## Varieties are quasi-separated

If $X$ is a variety over a field $k$, then its structure
morphism $X \to \operatorname{Spec} k$ is quasi-separated, since it is separated.

Formalized by `AlgebraicGeometry.IsVariety.quasiSeparated`, a theorem declared in [MathlibExt/AlgebraicGeometry/Variety.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/Variety.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/varieties-over-a-field/index.html#quasi-separated).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Varieties over a field](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/varieties-over-a-field/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/AlgebraicGeometry/schemes-and-morphisms/varieties-over-a-field)
