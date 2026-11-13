---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.SystemF.erasure_step, Cslib.Languages.LambdaCalculus.SystemF.erasure_steps
statement: formalized
proof: formalized
---

# The call-by-value erasure bridge

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-call-by-value-erasure-bridge/index.html).

## Erasure of a System F evaluation step is a beta conversion

Actual CBV steps preserve beta conversion of closing instances.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.erasure_step`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/ErasureSimulation.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/ErasureSimulation.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-call-by-value-erasure-bridge/index.html#erasure-step).

## Erasure of multistep System F evaluation is a beta conversion

Finite CBV evaluation preserves conversion of erased instances.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.erasure_steps`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/ErasureSimulation.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/ErasureSimulation.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-call-by-value-erasure-bridge/index.html#erasure-steps).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The call-by-value erasure bridge](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-call-by-value-erasure-bridge/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-call-by-value-erasure-bridge)
