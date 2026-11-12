---
declaration: section
origin: cited
lean: OAI.IntegralCharacterVarieties.SurfacePresentation.Diagram.producedMarkedValues_allSeams
statement: formalized
proof: formalized
---

# 027. Potential integral density on curve character varieties

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the determinant-one curve case of Litt's integral-density question. For every smooth connected complex algebraic curve and every rank, integral points become Zariski dense in every component of its SL$_{r}$ character variety over the full ring of integers of one number field. Prescribed quasi-unipotent boundary conjugacy classes are allowed, including nonsemisimple classes.

## Integral points on character varieties of curves

We prove potential Zariski density of integral points on SL$_{r}$-character varieties of smooth complex curves in every rank. The result allows prescribed quasi-unipotent boundary monodromy, including exact nonsemisimple conjugacy classes, and holds on every component over the full ring of integers of one finite extension. Here integrality is measured in the ambient character variety, while the exact boundary conditions are imposed on the complex representation.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The integral-density question asks whether integral points become Zariski dense in every component of a curve character variety after one finite extension of the number field. The linked formalization proves a supporting compatibility result for its marked-surface construction. Given a proper diagram with finitely many vertices, a chosen seam with maximal adjacent facet rank and a positive-genus parent, puncture data, an existing solution over a field, and a chosen boundary occurrence, the produced marked values satisfy every seam equation.

Existence of integral points and Zariski density are not established. The paper's main theorem—potential integral density for $\mathrm{SL}_r$ curve character varieties over one finite extension, including prescribed quasi-unipotent boundary data and every irreducible component—is outside this comparison.

## Lean: Compatibility of the produced marked solution with every seam equation

Stated in [CharacterVarietiesAllSeamsSupport.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CharacterVarietiesAllSeamsSupport.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem producedMarkedValues_allSeams :
    D.ProducedMarkedSeamEquations q hproper hmax hg P x b0 i0
```

Proved in [lean/OAI/AlgebraicGeometry/CharacterVarieties/Seams/ProducedSolution.lean, line 37](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/AlgebraicGeometry/CharacterVarieties/Seams/ProducedSolution.lean#L37).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/027.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/027.md)
