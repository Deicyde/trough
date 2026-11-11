---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.FOmega.Ty.Par, Cslib.Languages.LambdaCalculus.FOmega.Ty.Par.refl, Cslib.Languages.LambdaCalculus.FOmega.Ty.Par.rename, Cslib.Languages.LambdaCalculus.FOmega.Ty.Par.subst, Cslib.Languages.LambdaCalculus.FOmega.Ty.Par.instantiate, Cslib.Languages.LambdaCalculus.FOmega.Ty.develop, Cslib.Languages.LambdaCalculus.FOmega.Ty.Par.to_develop, Cslib.Languages.LambdaCalculus.FOmega.Ty.par_diamond
statement: formalized
proof: formalized
---

# Type-beta confluence and conversion inversion

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html).

## Parallel type-beta reduction in Fω

Parallel type-beta reduction, retaining the context and kind indices.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Par`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#par).

## Reflexivity of parallel type-beta reduction

Parallel reduction is reflexive on every kinded operator.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Par.refl`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#refl).

## Parallel type-beta reduction is stable under renaming

Parallel beta reduction is stable under kinded renaming.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Par.rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#rename).

## Parallel type-beta reduction is stable under substitution

Parallel reduction respects simultaneous substitution on both sides.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Par.subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#subst).

## Parallel type-beta reduction is stable under instantiation

Parallel reduction respects discharging a binder and reducing its image.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Par.instantiate`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#instantiate).

## Complete development of type-beta redexes

Contract all originally present type-beta redexes recursively.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.develop`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#develop).

## Parallel reducts reduce to the complete development

Every parallel reduct reduces to the original complete development.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Par.to_develop`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#to-develop).

## Diamond property of parallel type-beta reduction

Parallel beta reduction has the diamond property at each kind.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.par_diamond`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#par-diamond).

## Confluence of parallel type-beta reduction

Parallel type-beta reduction is confluent; no termination premise.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.par_confluent`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#par-confluent).

## Multistep parallel type-beta reduction

Finitely many parallel beta reductions, including zero reductions.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Red`, an abbreviation declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#red).

## Multistep type-beta reduction under an operator abstraction

Multiple parallel reductions are stable under an operator binder.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Red.lam`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#lam).

## Multistep type-beta reduction under a universal quantifier

Multiple parallel reductions are stable under a universal binder.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Red.all`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#all).

## Multistep type-beta reduction in type applications

Multiple reductions are congruent in both type-application arguments.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Red.app`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#app).

## Multistep type-beta reduction in function types

Multiple reductions are congruent in both term-function type arguments.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Red.arr`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#arr).

## Church–Rosser property of type-beta conversion

Conversion entails a common parallel-beta reduct (Church-Rosser).

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Conv.join`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#join).

## Parallel type-beta reduction implies conversion

Every parallel-beta reduction is a proved conversion.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Par.conv`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#conv).

## Multistep type-beta reduction implies conversion

Finitely many parallel-beta reductions are a proved conversion.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Red.conv`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#conv-2).

## Type-beta conversion is joinability by a common reduct

Conversion is exactly common-reduct joinability, not semantic equality.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.conv_iff_join`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#conv-iff-join).

## Reducts of function types are function types

Reduction of a term-function type keeps its outer constructor.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Red.arr_inv`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#arr-inv).

## Reducts of quantified types are quantified types

Reduction of a quantified type keeps its binder kind and outer shape.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Red.all_inv`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#all-inv).

## Injectivity of function types up to conversion

Convertible term-function types have convertible domains and codomains.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Conv.arr_inj`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#arr-inj).

## Conversion preserves the kind of a universal binder

Conversion cannot change the kind of a universal binder.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Conv.all_kind`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#all-kind).

## Injectivity of quantified types up to conversion

Convertible quantified types at the same kind have convertible bodies.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Conv.all_inj`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Confluence.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html#all-inj).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Type-beta confluence and conversion inversion](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/type-beta-confluence-and-conversion-inversion)
