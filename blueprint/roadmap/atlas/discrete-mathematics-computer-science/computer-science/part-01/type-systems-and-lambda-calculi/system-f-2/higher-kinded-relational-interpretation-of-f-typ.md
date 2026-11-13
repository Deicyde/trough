---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.FOmega.relationalAlgebra, Cslib.Languages.LambdaCalculus.FOmega.Ty.interpret, Cslib.Languages.LambdaCalculus.FOmega.Ty.interpret_subst, Cslib.Languages.LambdaCalculus.FOmega.Ty.Conv.interpret, Cslib.Languages.LambdaCalculus.FOmega.Ty.interpret_rename, Cslib.Languages.LambdaCalculus.FOmega.Ty.interpret_instantiate, Cslib.Languages.LambdaCalculus.FOmega.Ty.interpret_all, Cslib.Languages.LambdaCalculus.FOmega.Ty.interpret_arr
statement: formalized
proof: formalized
---

# Higher-kinded relational interpretation of Fω types

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-interpretation-of-f-typ/index.html).

## Relational interpretation of Fω

## Kind algebra of beta-invariant relations

The generic kind algebra instantiated with the banked relation substrate.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.relationalAlgebra`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/RelationalTypes.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/RelationalTypes.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-interpretation-of-f-typ/index.html#relational-algebra).

## Relational interpretation of Fω types

A kinded type denotes a relation or an appropriately kinded function.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.interpret`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/RelationalTypes.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/RelationalTypes.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-interpretation-of-f-typ/index.html#interpret).

## Relational interpretation of a substituted Fω type

Relational substitution at every kind, with arbitrary higher-kind values.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.interpret_subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/RelationalTypes.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/RelationalTypes.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-interpretation-of-f-typ/index.html#interpret-subst).

## Type-beta conversion preserves the relational interpretation

Proved type-beta conversion is sound for the higher-kinded relations.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Conv.interpret`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/RelationalTypes.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/RelationalTypes.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-interpretation-of-f-typ/index.html#interpret-2).

## Relational interpretation of a renamed Fω type

Type renaming transports an arbitrary higher-kinded relation environment.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.interpret_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/RelationalTypes.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/RelationalTypes.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-interpretation-of-f-typ/index.html#interpret-rename).

## Relational interpretation of an instantiated Fω type

A kinded type argument is interpreted before its universal is discharged.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.interpret_instantiate`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/RelationalTypes.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/RelationalTypes.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-interpretation-of-f-typ/index.html#interpret-instantiate).

## Relational interpretation of an Fω universal type

A universal quantifies every semantic value of its bound kind.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.interpret_all`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/RelationalTypes.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/RelationalTypes.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-interpretation-of-f-typ/index.html#interpret-all).

## Relational interpretation of an Fω function type

An arrow relates every related pair of inputs at its codomain.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.interpret_arr`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/RelationalTypes.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/RelationalTypes.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-interpretation-of-f-typ/index.html#interpret-arr).

## Relational interpretation of a weakened Fω type

Weakening ignores the arbitrary new semantic value, at every binder kind.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.interpret_weaken`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/RelationalTypes.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/RelationalTypes.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-interpretation-of-f-typ/index.html#interpret-weaken).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Higher-kinded relational interpretation of Fω types](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-interpretation-of-f-typ/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/higher-kinded-relational-interpretation-of-f-typ)
