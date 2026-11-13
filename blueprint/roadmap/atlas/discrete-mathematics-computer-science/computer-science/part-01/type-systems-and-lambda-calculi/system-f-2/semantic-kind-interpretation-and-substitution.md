---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.FOmega.Kind.Sem, Cslib.Languages.LambdaCalculus.FOmega.KEnv, Cslib.Languages.LambdaCalculus.FOmega.KEnv.extend, Cslib.Languages.LambdaCalculus.FOmega.KindAlgebra, Cslib.Languages.LambdaCalculus.FOmega.Ty.eval, Cslib.Languages.LambdaCalculus.FOmega.Ty.eval_congr, Cslib.Languages.LambdaCalculus.FOmega.Ty.eval_rename, Cslib.Languages.LambdaCalculus.FOmega.Ty.eval_subst
statement: formalized
proof: formalized
---

# Semantic kind interpretation and substitution

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/semantic-kind-interpretation-and-substitution/index.html).

## Semantic interpretation of kinds

## Semantic interpretation of kinds

Interpret kinds over a carrier for term types.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Kind.Sem`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/KindSemantics.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/KindSemantics.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/semantic-kind-interpretation-and-substitution/index.html#sem).

## Kinded semantic environment

An environment supplies a value of the declared kind for every variable.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.KEnv`, an abbreviation declared in [CSLibExt/Languages/LambdaCalculus/FOmega/KindSemantics.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/KindSemantics.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/semantic-kind-interpretation-and-substitution/index.html#kenv).

## Extension of a kinded semantic environment

Extend a semantic environment at its newest kinded variable.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.KEnv.extend`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/KindSemantics.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/KindSemantics.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/semantic-kind-interpretation-and-substitution/index.html#extend).

## Kind algebra of arrow and universal type constructors

The two type constructors at `star`; higher kinds need no extra laws.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.KindAlgebra`, a structure declared in [CSLibExt/Languages/LambdaCalculus/FOmega/KindSemantics.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/KindSemantics.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/semantic-kind-interpretation-and-substitution/index.html#kind-algebra).

## Semantic evaluation of kinded type operators

Interpret a kinded operator by ordinary function abstraction/application.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.eval`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/KindSemantics.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/KindSemantics.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/semantic-kind-interpretation-and-substitution/index.html#eval).

## Evaluation depends only on the environment pointwise

Interpretation depends only on the pointwise kinded environment.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.eval_congr`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/KindSemantics.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/KindSemantics.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/semantic-kind-interpretation-and-substitution/index.html#eval-congr).

## Evaluation of a renamed type operator

Semantic renaming is precomposition of the kinded environment.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.eval_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/KindSemantics.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/KindSemantics.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/semantic-kind-interpretation-and-substitution/index.html#eval-rename).

## Evaluation of a substituted type operator

Semantic simultaneous substitution at every kind, including higher kinds.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.eval_subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/KindSemantics.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/KindSemantics.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/semantic-kind-interpretation-and-substitution/index.html#eval-subst).

## Evaluation of an instantiated type operator

Semantic instantiation is environment extension by the argument value.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.eval_instantiate`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/KindSemantics.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/KindSemantics.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/semantic-kind-interpretation-and-substitution/index.html#eval-instantiate).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Semantic kind interpretation and substitution](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/semantic-kind-interpretation-and-substitution/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/semantic-kind-interpretation-and-substitution)
