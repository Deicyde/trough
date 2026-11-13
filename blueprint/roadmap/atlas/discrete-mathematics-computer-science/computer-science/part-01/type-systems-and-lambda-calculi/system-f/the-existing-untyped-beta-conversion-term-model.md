---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.SystemF.Model, Cslib.Languages.LambdaCalculus.SystemF.BetaEq, Cslib.Languages.LambdaCalculus.SystemF.Model.app, Cslib.Languages.LambdaCalculus.SystemF.Model.lc, Cslib.Languages.LambdaCalculus.SystemF.Model.atom, Cslib.Languages.LambdaCalculus.SystemF.BetaEq.refl, Cslib.Languages.LambdaCalculus.SystemF.BetaEq.symm, Cslib.Languages.LambdaCalculus.SystemF.BetaEq.trans
statement: formalized
proof: formalized
---

# The existing untyped beta-conversion term model

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-existing-untyped-beta-conversion-term-model/index.html).

## System F

## Untyped locally closed term model

Locally closed terms in the pinned CSLib untyped calculus.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Model`, an abbreviation declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Model.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Model.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-existing-untyped-beta-conversion-term-model/index.html#model).

## Beta equivalence in the untyped term model

Equivalence closure of the existing full-beta reduction.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.BetaEq`, an abbreviation declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Model.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Model.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-existing-untyped-beta-conversion-term-model/index.html#beta-eq).

## Application in the untyped term model

Application in the existing untyped term model preserves local closure.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Model.app`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Model.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Model.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-existing-untyped-beta-conversion-term-model/index.html#app).

## Model terms are locally closed

The Boolean carrier invariant implies CSLib's cofinite local closure.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Model.lc`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Model.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Model.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-existing-untyped-beta-conversion-term-model/index.html#lc).

## Symbolic atoms of the untyped term model

A symbolic atom is locally closed; it is not a new System F constant.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Model.atom`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Model.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Model.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-existing-untyped-beta-conversion-term-model/index.html#atom).

## Reflexivity of beta equivalence

Upstream beta equivalence is reflexive.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.BetaEq.refl`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Model.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Model.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-existing-untyped-beta-conversion-term-model/index.html#refl).

## Symmetry of beta equivalence

Upstream beta equivalence is symmetric.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.BetaEq.symm`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Model.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Model.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-existing-untyped-beta-conversion-term-model/index.html#symm).

## Transitivity of beta equivalence

Upstream beta equivalence is transitive.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.BetaEq.trans`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Model.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Model.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-existing-untyped-beta-conversion-term-model/index.html#trans).

## Beta equivalence is a congruence in function position

Application preserves beta equivalence in its function position.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.BetaEq.appFun`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Model.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Model.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-existing-untyped-beta-conversion-term-model/index.html#app-fun).

## Beta equivalence is a congruence in argument position

Application preserves beta equivalence in its argument position.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.BetaEq.appArg`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Model.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Model.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-existing-untyped-beta-conversion-term-model/index.html#app-arg).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The existing untyped beta-conversion term model](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-existing-untyped-beta-conversion-term-model/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-existing-untyped-beta-conversion-term-model)
