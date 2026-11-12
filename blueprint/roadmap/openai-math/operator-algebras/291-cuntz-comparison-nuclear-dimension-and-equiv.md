---
declaration: section
origin: cited
lean: OAI.ComparatorModel.CurrentMain.main
statement: formalized
proof: formalized
---

# 291. Cuntz comparison, nuclear dimension, and equivariant Jiang–Su stability

4 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves equivariant Jiang–Su stability for every countable discrete amenable group action on a simple separable unital infinite-dimensional nuclear stably finite Jiang–Su-stable $C^{∗}$-algebra, resolving this case of Szabó's conjecture without restrictions on trace dynamics. The family also proves the unital Toms–Winter conjecture, equating strict comparison, finite nuclear dimension and Jiang–Su stability in the simple separable unital infinite-dimensional nuclear setting.

## Equivariant Jiang–Su Stability for Amenable Actions in the Unital Stably Finite Case

Every action of a countable discrete amenable group on a simple, separable, unital, infinite-dimensional, nuclear, stably finite complex C$^{∗}$-algebra that is already Jiang–Su stable absorbs the trivial action on the Jiang–Su algebra up to cocycle conjugacy. No restriction is imposed on the action on the tracial-state simplex. This proves the unital, stably finite case of Szabó's Conjecture A on automatic equivariant Jiang–Su stability.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Equivariant-Jiang-Su-Stability-for-Amenable-Actions-in-the-Unital-Stably-Finite-Case-October-5-2026/paper.pdf).

## Cuntz comparison and Jiang–Su absorption

We prove that strict comparison in the extended-functional sense implies Jiang–Su absorption for separable simple nuclear non-elementary $C^{∗}$-algebras. This resolves the corresponding implication of the Toms–Winter regularity problem, including nonunital algebras and allowing unbounded traces. More generally, every separable nuclear $C^{∗}$-algebra whose Cuntz semigroup is almost unperforated and fully almost divisible absorbs the Jiang–Su algebra.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Cuntz-comparison-and-Jiang-Su-absorption-September-23-2026/paper.pdf).

## Nuclear dimension and Jiang–Su stability without elementary subquotients

For separable nuclear $C^{∗}$-algebras with no nonzero elementary ideal subquotients, finite nuclear dimension is equivalent to Jiang–Su stability. More generally, $\dim_{\mathrm{nuc}}(A_0\otimes\mathcal Z)\le1$ for every separable nuclear $A_{0}$. This proves Robert and Tikuisis's Conjecture (C1) and the nuclear-dimension equivalence in the nonsimple Toms–Winter regularity question.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Nuclear-dimension-and-Jiang-Su-stability-without-elementary-subquotients-September-23-2026/paper.pdf).

## Tracial projection methods and uniform property Gamma

For a simple, separable, unital, infinite-dimensional, nuclear, stably finite $C^{∗}$-algebra with traces, real rank zero of the uniform tracial ultrapower of its uniform tracial completion implies uniform property Γ. This answers Problem XXI of Schafhauser, Tikuisis and White affirmatively. Independently, strict comparison implies Jiang–Su absorption for simple, separable, unital, infinite-dimensional nuclear algebras, resolving the unital Toms–Winter conjecture. Under comparison tested on traces of finite target rank, we also obtain uniform property Γ and absorption for simple, separable, nuclear, stably projectionless algebras whose densely finite traces are all bounded and have a nonempty compact normalized base.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves that real rank zero of the uniform tracial ultrapower of the uniform tracial completion implies uniform property $\Gamma$ for a simple separable unital infinite-dimensional nuclear stably finite $C^*$-algebra with traces. The conclusion holds at every specified free ultrafilter under the corresponding real-rank-zero hypothesis.

The linked comparison results also prove Jiang–Su absorption and uniform property $\Gamma$ for simple separable unital infinite-dimensional nuclear algebras with strict comparison, and for the stated stably projectionless nuclear algebras with bounded densely finite traces, a nonempty compact normalized trace base, and the prescribed finite-target-rank comparison condition.

## Lean: Uniform property $\Gamma$ from tracial real rank zero

Stated in [UniformGamma.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/UniformGamma.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem CurrentMain.main : MainClaim.{uNuclear}
```

Proved in [lean/OAI/Analysis/TracialSplitting/Challenge.lean, line 75](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/TracialSplitting/Challenge.lean#L75).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/291.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/291.md)
