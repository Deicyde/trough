---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.FOmega.erasure_step, Cslib.Languages.LambdaCalculus.FOmega.erasure_steps
statement: formalized
proof: formalized
---

# Fω weak-CBV erasure into the existing full-beta term model

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/f-weak-cbv-erasure-into-the-existing-full-beta-t/index.html).

## Erasure of an Fω evaluation step is a beta conversion

Every actual Fω CBV step preserves beta conversion of arbitrary closing instances.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.erasure_step`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/ErasureSimulation.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/ErasureSimulation.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/f-weak-cbv-erasure-into-the-existing-full-beta-t/index.html#erasure-step).

## Erasure of multistep Fω evaluation is a beta conversion

Finite Fω evaluation preserves beta conversion of the closing instances.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.erasure_steps`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/ErasureSimulation.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/ErasureSimulation.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/f-weak-cbv-erasure-into-the-existing-full-beta-t/index.html#erasure-steps).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fω weak-CBV erasure into the existing full-beta term model](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/f-weak-cbv-erasure-into-the-existing-full-beta-t/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/f-weak-cbv-erasure-into-the-existing-full-beta-t)
