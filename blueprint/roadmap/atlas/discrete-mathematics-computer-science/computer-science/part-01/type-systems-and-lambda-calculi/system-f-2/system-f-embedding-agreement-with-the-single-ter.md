---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.FOmega.Tm.close_fromSystemF, Cslib.Languages.LambdaCalculus.FOmega.Tm.close_embed, Cslib.Languages.LambdaCalculus.FOmega.Tm.eraseModel_embed, Cslib.Languages.LambdaCalculus.FOmega.Ty.interpret_fromSystemF, Cslib.Languages.LambdaCalculus.FOmega.Ty.interpret_embed
statement: formalized
proof: formalized
---

# System F embedding agreement with the single term/relation model

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/system-f-embedding-agreement-with-the-single-ter/index.html).

## Translated System F terms have the same closing instances

Translated System F terms have exactly the same model closing instances.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.close_fromSystemF`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/EmbeddingModel.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/EmbeddingModel.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/system-f-embedding-agreement-with-the-single-ter/index.html#close-from-system-f).

## Canonical embedding preserves closing instances

Canonical embedding preserves arbitrary model closing instances exactly.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.close_embed`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/EmbeddingModel.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/EmbeddingModel.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/system-f-embedding-agreement-with-the-single-ter/index.html#close-embed).

## Canonical embedding preserves model erasure

A System F term and its Fω embedding have identical model erasures.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.eraseModel_embed`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/EmbeddingModel.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/EmbeddingModel.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/system-f-embedding-agreement-with-the-single-ter/index.html#erase-model-embed).

## Type translation preserves the relational interpretation

The star/forall translation preserves the same binary type interpretation.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.interpret_fromSystemF`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/EmbeddingModel.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/EmbeddingModel.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/system-f-embedding-agreement-with-the-single-ter/index.html#interpret-from-system-f).

## Relational interpretation of canonically embedded types

Canonical embedding interprets each source variable by its matching kinded lookup.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.interpret_embed`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/EmbeddingModel.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/EmbeddingModel.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/system-f-embedding-agreement-with-the-single-ter/index.html#interpret-embed).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: System F embedding agreement with the single term/relation model](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/system-f-embedding-agreement-with-the-single-ter/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/system-f-embedding-agreement-with-the-single-ter)
