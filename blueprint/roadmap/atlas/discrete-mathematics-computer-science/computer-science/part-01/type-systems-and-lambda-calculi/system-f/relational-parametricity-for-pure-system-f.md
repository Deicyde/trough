---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.SystemF.fundamental, Cslib.Languages.LambdaCalculus.SystemF.fundamental_closed, Cslib.Languages.LambdaCalculus.SystemF.polyIdType, Cslib.Languages.LambdaCalculus.SystemF.polyId, Cslib.Languages.LambdaCalculus.SystemF.polyId_typed, Cslib.Languages.LambdaCalculus.SystemF.polymorphic_identity, Cslib.Languages.LambdaCalculus.SystemF.polymorphic_related, Cslib.Languages.LambdaCalculus.SystemF.forall_var_uninhabited
statement: formalized
proof: formalized
---

# Relational parametricity for pure System F

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/relational-parametricity-for-pure-system-f/index.html).

## Fundamental theorem of relational parametricity for System F

The fundamental binary relational-parametricity theorem of pure System F.

A syntactic-model adaptation of Reynolds' abstraction theorem (1983,
Sections 3 and 8), following Wadler's related-environment formulation (1989,
Section 6); see the module's provenance and model qualifications.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.fundamental`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Parametricity.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Parametricity.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/relational-parametricity-for-pure-system-f/index.html#fundamental).

## Closed typed System F terms are related to themselves

Every closed typed term is related to itself under arbitrary relations.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.fundamental_closed`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Parametricity.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Parametricity.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/relational-parametricity-for-pure-system-f/index.html#fundamental-closed).

## Polymorphic identity type

The polymorphic identity type, universally quantified at any type depth.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.polyIdType`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Parametricity.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Parametricity.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/relational-parametricity-for-pure-system-f/index.html#poly-id-type).

## Polymorphic identity term

The pure polymorphic identity term.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.polyId`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Parametricity.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Parametricity.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/relational-parametricity-for-pure-system-f/index.html#poly-id).

## Typing of the polymorphic identity

The polymorphic identity is well typed in any existing term context.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.polyId_typed`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Parametricity.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Parametricity.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/relational-parametricity-for-pure-system-f/index.html#poly-id-typed).

## Closed inhabitants of the polymorphic identity type are identities

Every closed inhabitant acts as identity after every type instantiation.

The conclusion is full-beta conversion in the existing erased term model,
for an arbitrary locally closed input. It makes no CBV termination claim.
This consumer specializes the free-theorem method of Wadler (1989, Figure 1)
to the declared syntactic model; it applies to every typed inhabitant.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.polymorphic_identity`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Parametricity.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Parametricity.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/relational-parametricity-for-pure-system-f/index.html#polymorphic-identity).

## Polymorphic identity inhabitants preserve admissible relations

Type instantiations preserve every admissible binary input relation.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.polymorphic_related`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Parametricity.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Parametricity.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/relational-parametricity-for-pure-system-f/index.html#polymorphic-related).

## No closed System F term inhabits $\forall X, X$

The empty relation rules out every closed inhabitant of `forall X, X`.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.forall_var_uninhabited`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Parametricity.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Parametricity.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/relational-parametricity-for-pure-system-f/index.html#forall-var-uninhabited).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Relational parametricity for pure System F](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/relational-parametricity-for-pure-system-f/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/relational-parametricity-for-pure-system-f)
